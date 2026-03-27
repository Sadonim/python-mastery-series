"""챕터 5: 데이터베이스 연동 — SQLite, SQLAlchemy ORM, FastAPI 통합."""


def get_chapter():
    """챕터 5 콘텐츠를 반환한다."""
    return {
        "number": 5,
        "title": "데이터베이스 연동",
        "subtitle": "SQLite · SQLAlchemy ORM · FastAPI 통합",
        "big_picture": (
            "지금까지 만든 API는 서버를 재시작하면 모든 데이터가 사라졌습니다. "
            "실제 서비스는 데이터베이스에 데이터를 영구 저장합니다. "
            "이 챕터에서는 파이썬 내장 SQLite로 SQL의 기초를 익히고, "
            "SQLAlchemy ORM으로 파이썬 클래스를 DB 테이블로 매핑하는 방법을 배웁니다. "
            "마지막으로 FastAPI와 SQLAlchemy를 통합해 "
            "완전한 CRUD API를 완성합니다. "
            "MLOps에서는 실험 결과, 모델 메타데이터, 예측 로그를 DB에 저장하는 데 활용합니다."
        ),
        "sections": [
            # ── 섹션 1: SQLite 기초 ────────────────────────────────
            {
                "title": "SQLite 기초 — SQL 핵심 문법",
                "content": [
                    "SQL(Structured Query Language)은 관계형 데이터베이스를 다루는 표준 언어입니다. "
                    "SQLite는 파일 하나로 동작하는 내장 DB로, "
                    "별도 서버 설치 없이 파이썬 표준 라이브러리로 사용할 수 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "데이터베이스는 엑셀 파일과 비슷합니다. "
                            "데이터베이스 = 엑셀 파일, 테이블 = 시트, 행(row) = 데이터 한 줄, 열(column) = 항목명. "
                            "SQL은 이 엑셀을 조작하는 명령어 언어입니다. "
                            "다만 수백만 줄도 빠르게 처리하고 동시 접근도 안전하게 관리합니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "핵심 SQL 문법: DDL (테이블 정의)",
                    },
                    {
                        "type": "code",
                        "language": "sql",
                        "code": (
                            "-- 테이블 생성\n"
                            "CREATE TABLE IF NOT EXISTS soldiers (\n"
                            "    id        INTEGER PRIMARY KEY AUTOINCREMENT,  -- 자동 증가 기본키\n"
                            "    name      TEXT    NOT NULL,                    -- 필수 문자열\n"
                            "    rank      TEXT    NOT NULL,\n"
                            "    unit      TEXT    NOT NULL,\n"
                            "    age       INTEGER CHECK (age >= 18),           -- 18세 이상 제약\n"
                            "    created_at TEXT   DEFAULT (datetime('now'))    -- 생성 시각 자동 기록\n"
                            ");\n\n"
                            "-- 테이블 삭제\n"
                            "DROP TABLE IF EXISTS soldiers;\n\n"
                            "-- 컬럼 추가 (ALTER TABLE)\n"
                            "ALTER TABLE soldiers ADD COLUMN email TEXT;"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "핵심 SQL 문법: DML (데이터 조작)",
                    },
                    {
                        "type": "code",
                        "language": "sql",
                        "code": (
                            "-- INSERT: 데이터 삽입\n"
                            "INSERT INTO soldiers (name, rank, unit, age)\n"
                            "VALUES ('홍길동', '이병', '1사단', 20);\n\n"
                            "-- SELECT: 데이터 조회\n"
                            "SELECT * FROM soldiers;                          -- 전체 조회\n"
                            "SELECT name, rank FROM soldiers WHERE unit = '1사단';  -- 조건 조회\n"
                            "SELECT * FROM soldiers ORDER BY age DESC LIMIT 5; -- 정렬 후 5개\n"
                            "SELECT rank, COUNT(*) AS cnt FROM soldiers GROUP BY rank; -- 집계\n\n"
                            "-- UPDATE: 데이터 수정\n"
                            "UPDATE soldiers\n"
                            "SET rank = '일병'\n"
                            "WHERE id = 1;\n\n"
                            "-- DELETE: 데이터 삭제\n"
                            "DELETE FROM soldiers WHERE id = 1;\n\n"
                            "-- JOIN: 두 테이블 결합\n"
                            "SELECT s.name, u.unit_name\n"
                            "FROM soldiers s\n"
                            "JOIN units u ON s.unit_id = u.id\n"
                            "WHERE s.rank = '병장';"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["SQL 구문", "역할", "예시"],
                        "rows": [
                            ["SELECT", "데이터 조회", "SELECT * FROM users WHERE active=1"],
                            ["INSERT", "데이터 삽입", "INSERT INTO users (name) VALUES ('홍')"],
                            ["UPDATE", "데이터 수정", "UPDATE users SET name='김' WHERE id=1"],
                            ["DELETE", "데이터 삭제", "DELETE FROM users WHERE id=1"],
                            ["CREATE TABLE", "테이블 생성", "CREATE TABLE users (id INTEGER PRIMARY KEY)"],
                            ["WHERE", "조건 필터", "WHERE age >= 20 AND rank = '상병'"],
                            ["ORDER BY", "정렬", "ORDER BY created_at DESC"],
                            ["LIMIT", "결과 개수 제한", "LIMIT 10 OFFSET 20"],
                        ],
                    },
                ],
            },
            # ── 섹션 2: Python sqlite3 모듈 ───────────────────────
            {
                "title": "Python sqlite3 모듈로 DB 다루기",
                "content": [
                    "파이썬 표준 라이브러리의 sqlite3 모듈로 SQLite를 바로 사용할 수 있습니다. "
                    "별도 설치 없이 파일 기반 DB를 생성·조작할 수 있어 "
                    "개발·테스트 단계에 이상적입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import sqlite3\n"
                            "from contextlib import contextmanager\n"
                            "from typing import Generator\n\n\n"
                            "# DB 연결 컨텍스트 매니저 (자동 닫기)\n"
                            "@contextmanager\n"
                            "def get_connection(db_path: str = 'army.db') -> Generator:\n"
                            "    \"\"\"DB 연결을 관리하는 컨텍스트 매니저.\"\"\"\n"
                            "    conn = sqlite3.connect(db_path)\n"
                            "    conn.row_factory = sqlite3.Row  # 결과를 딕셔너리처럼 접근\n"
                            "    try:\n"
                            "        yield conn\n"
                            "        conn.commit()  # 성공 시 커밋\n"
                            "    except Exception:\n"
                            "        conn.rollback()  # 실패 시 롤백\n"
                            "        raise\n"
                            "    finally:\n"
                            "        conn.close()\n\n\n"
                            "# 테이블 생성\n"
                            "def init_db(db_path: str = 'army.db') -> None:\n"
                            "    \"\"\"DB와 테이블을 초기화한다.\"\"\"\n"
                            "    with get_connection(db_path) as conn:\n"
                            "        conn.execute('''\n"
                            "            CREATE TABLE IF NOT EXISTS soldiers (\n"
                            "                id   INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                            "                name TEXT NOT NULL,\n"
                            "                rank TEXT NOT NULL,\n"
                            "                unit TEXT NOT NULL\n"
                            "            )\n"
                            "        ''')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# CRUD 함수 구현\n"
                            "def create_soldier(name: str, rank: str, unit: str) -> int:\n"
                            "    \"\"\"군인을 등록하고 새 id를 반환한다.\"\"\"\n"
                            "    with get_connection() as conn:\n"
                            "        cursor = conn.execute(\n"
                            "            'INSERT INTO soldiers (name, rank, unit) VALUES (?, ?, ?)',\n"
                            "            (name, rank, unit),  # ? 플레이스홀더로 SQL 인젝션 방지\n"
                            "        )\n"
                            "        return cursor.lastrowid\n\n\n"
                            "def get_soldier(soldier_id: int) -> dict | None:\n"
                            "    \"\"\"특정 군인 정보를 반환한다. 없으면 None.\"\"\"\n"
                            "    with get_connection() as conn:\n"
                            "        row = conn.execute(\n"
                            "            'SELECT * FROM soldiers WHERE id = ?', (soldier_id,)\n"
                            "        ).fetchone()\n"
                            "        return dict(row) if row else None\n\n\n"
                            "def list_soldiers(rank: str | None = None) -> list[dict]:\n"
                            "    \"\"\"군인 목록을 반환한다. rank로 필터링 가능.\"\"\"\n"
                            "    with get_connection() as conn:\n"
                            "        if rank:\n"
                            "            rows = conn.execute(\n"
                            "                'SELECT * FROM soldiers WHERE rank = ?', (rank,)\n"
                            "            ).fetchall()\n"
                            "        else:\n"
                            "            rows = conn.execute('SELECT * FROM soldiers').fetchall()\n"
                            "        return [dict(row) for row in rows]\n\n\n"
                            "def update_soldier_rank(soldier_id: int, new_rank: str) -> bool:\n"
                            "    \"\"\"계급을 승진시키고 성공 여부를 반환한다.\"\"\"\n"
                            "    with get_connection() as conn:\n"
                            "        cursor = conn.execute(\n"
                            "            'UPDATE soldiers SET rank = ? WHERE id = ?',\n"
                            "            (new_rank, soldier_id),\n"
                            "        )\n"
                            "        return cursor.rowcount > 0  # 변경된 행이 있으면 True\n\n\n"
                            "def delete_soldier(soldier_id: int) -> bool:\n"
                            "    \"\"\"군인을 삭제하고 성공 여부를 반환한다.\"\"\"\n"
                            "    with get_connection() as conn:\n"
                            "        cursor = conn.execute(\n"
                            "            'DELETE FROM soldiers WHERE id = ?', (soldier_id,)\n"
                            "        )\n"
                            "        return cursor.rowcount > 0"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "SQL 인젝션 방지: 반드시 ? 플레이스홀더를 사용하세요. "
                            "f'SELECT * FROM users WHERE name = \"{name}\"' 처럼 "
                            "문자열 포맷팅으로 SQL을 직접 조합하면 "
                            "악의적인 입력으로 DB 전체가 삭제될 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: SQLAlchemy ORM ────────────────────────────
            {
                "title": "SQLAlchemy ORM 소개",
                "content": [
                    "ORM(Object-Relational Mapping)은 파이썬 클래스와 DB 테이블을 연결합니다. "
                    "SQL을 직접 작성하지 않고 파이썬 코드로 DB를 조작할 수 있습니다. "
                    "SQLAlchemy는 파이썬에서 가장 널리 쓰이는 ORM입니다.",
                    {
                        "type": "flow_diagram",
                        "title": "ORM 계층 구조",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "Application Layer", "sub": "FastAPI 핸들러 / 비즈니스 로직"},
                            {"label": "ORM Layer", "sub": "SQLAlchemy 모델 클래스 (Python 객체)"},
                            {"label": "SQL Layer", "sub": "자동 생성 SQL 쿼리"},
                            {"label": "DB Driver Layer", "sub": "sqlite3 / psycopg2 / aiomysql"},
                            {"label": "Database", "sub": "SQLite / PostgreSQL / MySQL"},
                        ],
                        "note": "ORM은 Python 객체를 SQL로 변환합니다. 개발 생산성이 높아지지만 복잡한 쿼리는 직접 SQL 작성이 더 효율적입니다.",
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": "pip install sqlalchemy",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# database.py — DB 엔진과 세션 설정\n"
                            "from sqlalchemy import create_engine\n"
                            "from sqlalchemy.orm import sessionmaker, DeclarativeBase\n\n"
                            "# SQLite 연결 URL\n"
                            "DATABASE_URL = 'sqlite:///./army.db'\n\n"
                            "# 엔진 생성\n"
                            "engine = create_engine(\n"
                            "    DATABASE_URL,\n"
                            "    connect_args={'check_same_thread': False},  # SQLite 멀티스레드 허용\n"
                            ")\n\n"
                            "# 세션 팩토리\n"
                            "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n\n\n"
                            "# 모든 모델의 기반 클래스\n"
                            "class Base(DeclarativeBase):\n"
                            "    pass"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 모델 정의, 세션, CRUD ─────────────────────
            {
                "title": "모델 정의, 세션 관리, CRUD 작성",
                "content": [
                    "SQLAlchemy 모델은 DB 테이블과 1:1로 대응합니다. "
                    "클래스 속성으로 컬럼을 정의하고, 관계를 선언하면 JOIN도 자동 처리됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# models.py — SQLAlchemy 모델 정의\n"
                            "from datetime import datetime\n"
                            "from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean\n"
                            "from sqlalchemy.orm import relationship\n"
                            "from database import Base\n\n\n"
                            "class Unit(Base):\n"
                            "    \"\"\"부대 테이블.\"\"\"\n"
                            "    __tablename__ = 'units'\n\n"
                            "    id   = Column(Integer, primary_key=True, index=True)\n"
                            "    name = Column(String(100), unique=True, nullable=False)\n\n"
                            "    # 역방향 관계: unit.soldiers 로 소속 군인 목록 접근\n"
                            "    soldiers = relationship('Soldier', back_populates='unit')\n\n\n"
                            "class Soldier(Base):\n"
                            "    \"\"\"군인 테이블.\"\"\"\n"
                            "    __tablename__ = 'soldiers'\n\n"
                            "    id         = Column(Integer, primary_key=True, index=True)\n"
                            "    name       = Column(String(50), nullable=False)\n"
                            "    rank       = Column(String(20), nullable=False)\n"
                            "    unit_id    = Column(Integer, ForeignKey('units.id'), nullable=False)\n"
                            "    is_active  = Column(Boolean, default=True)\n"
                            "    created_at = Column(DateTime, default=datetime.utcnow)\n\n"
                            "    # 관계: soldier.unit 으로 소속 부대 접근\n"
                            "    unit = relationship('Unit', back_populates='soldiers')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# crud.py — CRUD 함수 (SQLAlchemy 사용)\n"
                            "from sqlalchemy.orm import Session\n"
                            "from models import Soldier, Unit\n\n\n"
                            "def get_soldier(db: Session, soldier_id: int) -> Soldier | None:\n"
                            "    \"\"\"ID로 군인을 조회한다.\"\"\"\n"
                            "    return db.query(Soldier).filter(Soldier.id == soldier_id).first()\n\n\n"
                            "def list_soldiers(\n"
                            "    db: Session, skip: int = 0, limit: int = 10, rank: str | None = None\n"
                            ") -> list[Soldier]:\n"
                            "    \"\"\"군인 목록을 반환한다. rank로 필터링, 페이지네이션 지원.\"\"\"\n"
                            "    query = db.query(Soldier).filter(Soldier.is_active.is_(True))\n"
                            "    if rank:\n"
                            "        query = query.filter(Soldier.rank == rank)\n"
                            "    return query.offset(skip).limit(limit).all()\n\n\n"
                            "def create_soldier(db: Session, name: str, rank: str, unit_id: int) -> Soldier:\n"
                            "    \"\"\"군인을 등록하고 저장된 객체를 반환한다.\"\"\"\n"
                            "    new_soldier = Soldier(name=name, rank=rank, unit_id=unit_id)\n"
                            "    db.add(new_soldier)      # 세션에 추가\n"
                            "    db.commit()              # DB에 저장\n"
                            "    db.refresh(new_soldier)  # DB에서 최신 상태로 갱신 (id, created_at 반영)\n"
                            "    return new_soldier\n\n\n"
                            "def update_soldier_rank(db: Session, soldier_id: int, new_rank: str) -> Soldier | None:\n"
                            "    \"\"\"계급을 변경하고 수정된 객체를 반환한다.\"\"\"\n"
                            "    soldier = get_soldier(db, soldier_id)\n"
                            "    if not soldier:\n"
                            "        return None\n"
                            "    soldier.rank = new_rank  # 속성 변경 — ORM이 변경 추적\n"
                            "    db.commit()\n"
                            "    db.refresh(soldier)\n"
                            "    return soldier\n\n\n"
                            "def deactivate_soldier(db: Session, soldier_id: int) -> bool:\n"
                            "    \"\"\"군인을 비활성화(소프트 삭제)한다.\"\"\"\n"
                            "    soldier = get_soldier(db, soldier_id)\n"
                            "    if not soldier:\n"
                            "        return False\n"
                            "    soldier.is_active = False\n"
                            "    db.commit()\n"
                            "    return True"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "소프트 삭제(Soft Delete): 실제로 행을 지우는 대신 is_active=False로 표시합니다. "
                            "데이터 복구 가능성을 남기고 감사 로그를 유지할 수 있어 "
                            "군 시스템 같은 중요 데이터에 권장됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: FastAPI + SQLAlchemy 통합 ─────────────────
            {
                "title": "FastAPI + SQLAlchemy 통합",
                "content": [
                    "FastAPI의 Depends를 이용해 요청마다 DB 세션을 생성하고 "
                    "요청이 끝나면 자동으로 닫는 패턴을 구현합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# main.py — FastAPI + SQLAlchemy 통합\n"
                            "from fastapi import FastAPI, Depends, HTTPException, status\n"
                            "from sqlalchemy.orm import Session\n"
                            "from pydantic import BaseModel\n"
                            "from typing import Optional\n"
                            "from database import SessionLocal, engine, Base\n"
                            "import crud\n\n"
                            "# 앱 시작 시 테이블 생성\n"
                            "Base.metadata.create_all(bind=engine)\n\n"
                            "app = FastAPI(title='군 인사 관리 API')\n\n\n"
                            "# ── Pydantic 스키마 (API 입출력) ──\n"
                            "class SoldierCreate(BaseModel):\n"
                            "    name: str\n"
                            "    rank: str\n"
                            "    unit_id: int\n\n\n"
                            "class SoldierResponse(BaseModel):\n"
                            "    id: int\n"
                            "    name: str\n"
                            "    rank: str\n"
                            "    unit_id: int\n"
                            "    is_active: bool\n\n"
                            "    class Config:\n"
                            "        from_attributes = True  # SQLAlchemy 모델 → Pydantic 자동 변환\n\n\n"
                            "# ── DB 세션 의존성 ──\n"
                            "def get_db():\n"
                            "    \"\"\"요청마다 DB 세션을 생성하고 완료 후 닫는다.\"\"\"\n"
                            "    db = SessionLocal()\n"
                            "    try:\n"
                            "        yield db\n"
                            "    finally:\n"
                            "        db.close()\n\n\n"
                            "# ── 엔드포인트 ──\n"
                            "@app.post(\n"
                            "    '/soldiers/',\n"
                            "    response_model=SoldierResponse,\n"
                            "    status_code=status.HTTP_201_CREATED,\n"
                            ")\n"
                            "def create_soldier(\n"
                            "    soldier_in: SoldierCreate,\n"
                            "    db: Session = Depends(get_db),\n"
                            "):\n"
                            "    \"\"\"군인을 등록한다.\"\"\"\n"
                            "    return crud.create_soldier(\n"
                            "        db, soldier_in.name, soldier_in.rank, soldier_in.unit_id\n"
                            "    )\n\n\n"
                            "@app.get('/soldiers/', response_model=list[SoldierResponse])\n"
                            "def list_soldiers(\n"
                            "    skip: int = 0,\n"
                            "    limit: int = 10,\n"
                            "    rank: Optional[str] = None,\n"
                            "    db: Session = Depends(get_db),\n"
                            "):\n"
                            "    \"\"\"군인 목록을 조회한다.\"\"\"\n"
                            "    return crud.list_soldiers(db, skip=skip, limit=limit, rank=rank)\n\n\n"
                            "@app.get('/soldiers/{soldier_id}', response_model=SoldierResponse)\n"
                            "def read_soldier(soldier_id: int, db: Session = Depends(get_db)):\n"
                            "    \"\"\"특정 군인을 조회한다.\"\"\"\n"
                            "    soldier = crud.get_soldier(db, soldier_id)\n"
                            "    if not soldier:\n"
                            "        raise HTTPException(status_code=404, detail='군인을 찾을 수 없습니다')\n"
                            "    return soldier\n\n\n"
                            "@app.delete('/soldiers/{soldier_id}', status_code=status.HTTP_204_NO_CONTENT)\n"
                            "def deactivate_soldier(soldier_id: int, db: Session = Depends(get_db)):\n"
                            "    \"\"\"군인을 소프트 삭제한다.\"\"\"\n"
                            "    if not crud.deactivate_soldier(db, soldier_id):\n"
                            "        raise HTTPException(status_code=404, detail='군인을 찾을 수 없습니다')\n"
                            "    return None"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Pydantic 모델(SoldierResponse)의 Config 클래스에 "
                            "from_attributes = True (Pydantic v2) 또는 orm_mode = True (Pydantic v1)를 "
                            "설정해야 SQLAlchemy 객체를 직접 반환할 수 있습니다. "
                            "이 설정이 없으면 ValidationError가 발생합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 마이그레이션 — Alembic 소개 ──────────────
            {
                "title": "마이그레이션 — Alembic 소개",
                "content": [
                    "개발하다 보면 테이블 컬럼을 추가하거나 변경해야 하는 경우가 생깁니다. "
                    "Alembic은 SQLAlchemy를 위한 마이그레이션 도구로, "
                    "DB 스키마 변경 이력을 버전으로 관리합니다. "
                    "Git으로 코드를 관리하듯 DB 구조를 관리한다고 생각하면 됩니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Alembic 설치\n"
                            "pip install alembic\n\n"
                            "# 프로젝트에서 Alembic 초기화\n"
                            "alembic init alembic\n\n"
                            "# 마이그레이션 파일 자동 생성 (모델 변경 감지)\n"
                            "alembic revision --autogenerate -m '군인 테이블에 email 컬럼 추가'\n\n"
                            "# 최신 버전으로 DB 업그레이드 (실제 DB에 적용)\n"
                            "alembic upgrade head\n\n"
                            "# 이전 버전으로 롤백\n"
                            "alembic downgrade -1\n\n"
                            "# 마이그레이션 이력 확인\n"
                            "alembic history --verbose"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# alembic/env.py — 핵심 설정 (프로젝트 모델 연결)\n"
                            "from database import Base  # 프로젝트 Base 임포트\n"
                            "import models  # 모든 모델이 Base에 등록되도록 임포트\n\n"
                            "# target_metadata 에 Base.metadata 를 지정해야\n"
                            "# --autogenerate 가 모델 변경을 감지합니다\n"
                            "target_metadata = Base.metadata\n\n\n"
                            "# alembic/versions/xxxx_add_email.py — 자동 생성 예시\n"
                            "def upgrade() -> None:\n"
                            "    \"\"\"email 컬럼을 soldiers 테이블에 추가한다.\"\"\"\n"
                            "    op.add_column('soldiers', sa.Column('email', sa.String(200)))\n\n\n"
                            "def downgrade() -> None:\n"
                            "    \"\"\"email 컬럼을 제거한다 (롤백).\"\"\"\n"
                            "    op.drop_column('soldiers', 'email')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["마이그레이션 명령", "설명"],
                        "rows": [
                            ["alembic init alembic", "프로젝트에 Alembic 설정 초기화"],
                            ["alembic revision --autogenerate -m '설명'", "모델 변경 자동 감지해 마이그레이션 파일 생성"],
                            ["alembic upgrade head", "최신 버전까지 DB에 적용"],
                            ["alembic downgrade -1", "한 단계 롤백"],
                            ["alembic current", "현재 DB 버전 확인"],
                            ["alembic history", "전체 마이그레이션 이력 보기"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "실무 팁: 운영 DB에 alembic upgrade head를 실행하기 전에 "
                            "반드시 DB 백업을 먼저 하세요. "
                            "--autogenerate는 편리하지만 모든 변경을 완벽히 감지하지 못합니다 "
                            "(특히 컬럼 이름 변경). 생성된 파일을 꼭 검토하세요."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": {
            "title": "실무 팁",
            "content": [
                {
                    "type": "tip",
                    "text": (
                        "개발: SQLite → 운영: PostgreSQL 전환 시 "
                        "DATABASE_URL만 변경하면 됩니다. "
                        "SQLite: 'sqlite:///./app.db' "
                        "PostgreSQL: 'postgresql://user:pass@localhost/dbname' "
                        "SQLAlchemy가 나머지를 처리합니다."
                    ),
                },
                {
                    "type": "tip",
                    "text": (
                        "MLOps DB 패턴: 실험 결과 저장 예시 — "
                        "Experiment(name, model_type, hyperparams JSON, accuracy, created_at) 테이블을 만들어 "
                        "각 학습 실행 결과를 기록합니다. "
                        "MLflow도 내부적으로 SQLAlchemy를 사용합니다."
                    ),
                },
                {
                    "type": "warning",
                    "text": (
                        "FastAPI + SQLAlchemy 비동기 사용 시 "
                        "sqlalchemy.ext.asyncio의 AsyncSession과 "
                        "create_async_engine을 사용해야 합니다. "
                        "일반 Session을 async def 핸들러에서 쓰면 "
                        "이벤트 루프가 블로킹될 수 있습니다."
                    ),
                },
            ],
        },
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "SQL 인젝션을 방지하는 올바른 파이썬 sqlite3 코드는?",
                "choices": [
                    "A) conn.execute(f'SELECT * FROM users WHERE name = \"{name}\"')",
                    "B) conn.execute('SELECT * FROM users WHERE name = ?', (name,))",
                    "C) conn.execute('SELECT * FROM users WHERE name = ' + name)",
                    "D) conn.execute('SELECT * FROM users WHERE name = %s' % name)",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "SQLAlchemy에서 DB에 데이터를 추가하는 올바른 순서는?",
                "choices": [
                    "A) db.commit() → db.add(obj) → db.refresh(obj)",
                    "B) db.add(obj) → db.commit() → db.refresh(obj)",
                    "C) db.refresh(obj) → db.add(obj) → db.commit()",
                    "D) db.add(obj) → db.refresh(obj) → db.commit()",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "FastAPI에서 SQLAlchemy Session을 Depends로 주입할 때 "
                    "get_db() 함수에 yield를 사용하는 이유를 설명하시오."
                ),
                "answer": (
                    "yield를 사용하면 핸들러 실행 전 DB 세션을 생성해 전달하고, "
                    "핸들러 실행 완료 후 finally 블록에서 db.close()를 자동 실행합니다. "
                    "요청마다 세션 누수 없이 안전하게 관리할 수 있습니다."
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "sqlite3를 사용해 'books' 테이블을 만들고 CRUD 함수를 작성하세요. "
                    "테이블 컬럼: id(자동 증가), title(TEXT 필수), author(TEXT 필수), year(INTEGER). "
                    "함수: add_book(title, author, year) → id 반환, "
                    "get_books() → 전체 목록 반환 (딕셔너리 리스트)."
                ),
                "hint": (
                    "conn.row_factory = sqlite3.Row 설정 후 "
                    "dict(row)로 딕셔너리 변환. "
                    "INSERT: cursor.lastrowid로 새 id 반환. "
                    "SELECT: conn.execute('SELECT * FROM books').fetchall()"
                ),
                "answer": (
                    "import sqlite3\n"
                    "from contextlib import contextmanager\n\n\n"
                    "@contextmanager\n"
                    "def get_conn():\n"
                    "    conn = sqlite3.connect('books.db')\n"
                    "    conn.row_factory = sqlite3.Row\n"
                    "    try:\n"
                    "        yield conn\n"
                    "        conn.commit()\n"
                    "    finally:\n"
                    "        conn.close()\n\n\n"
                    "def init_db():\n"
                    "    with get_conn() as conn:\n"
                    "        conn.execute('''\n"
                    "            CREATE TABLE IF NOT EXISTS books (\n"
                    "                id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                    "                title TEXT NOT NULL,\n"
                    "                author TEXT NOT NULL,\n"
                    "                year INTEGER\n"
                    "            )\n"
                    "        ''')\n\n\n"
                    "def add_book(title: str, author: str, year: int) -> int:\n"
                    "    with get_conn() as conn:\n"
                    "        cur = conn.execute(\n"
                    "            'INSERT INTO books (title, author, year) VALUES (?, ?, ?)',\n"
                    "            (title, author, year)\n"
                    "        )\n"
                    "        return cur.lastrowid\n\n\n"
                    "def get_books() -> list[dict]:\n"
                    "    with get_conn() as conn:\n"
                    "        rows = conn.execute('SELECT * FROM books').fetchall()\n"
                    "        return [dict(row) for row in rows]"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "SQLAlchemy ORM으로 Task 모델을 정의하고 FastAPI와 통합하세요. "
                    "Task 모델: id, title(String), is_done(Boolean, 기본값 False), created_at(DateTime). "
                    "GET /tasks/ — 전체 할 일 목록 반환, "
                    "POST /tasks/ — 할 일 생성 (title만 입력받음), "
                    "PATCH /tasks/{task_id}/done — is_done을 True로 변경."
                ),
                "hint": (
                    "Base.metadata.create_all(bind=engine) 로 테이블 생성. "
                    "PATCH 엔드포인트: task = db.query(Task).filter(Task.id==task_id).first() "
                    "task.is_done = True; db.commit(); db.refresh(task)"
                ),
                "answer": (
                    "from fastapi import FastAPI, Depends, HTTPException\n"
                    "from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime\n"
                    "from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session\n"
                    "from pydantic import BaseModel\n"
                    "from datetime import datetime\n\n"
                    "engine = create_engine('sqlite:///./tasks.db', connect_args={'check_same_thread': False})\n"
                    "SessionLocal = sessionmaker(bind=engine)\n\n\n"
                    "class Base(DeclarativeBase):\n"
                    "    pass\n\n\n"
                    "class Task(Base):\n"
                    "    __tablename__ = 'tasks'\n"
                    "    id = Column(Integer, primary_key=True)\n"
                    "    title = Column(String(200), nullable=False)\n"
                    "    is_done = Column(Boolean, default=False)\n"
                    "    created_at = Column(DateTime, default=datetime.utcnow)\n\n\n"
                    "Base.metadata.create_all(bind=engine)\n"
                    "app = FastAPI()\n\n\n"
                    "class TaskCreate(BaseModel):\n"
                    "    title: str\n\n\n"
                    "class TaskResponse(BaseModel):\n"
                    "    id: int\n"
                    "    title: str\n"
                    "    is_done: bool\n"
                    "    class Config:\n"
                    "        from_attributes = True\n\n\n"
                    "def get_db():\n"
                    "    db = SessionLocal()\n"
                    "    try:\n"
                    "        yield db\n"
                    "    finally:\n"
                    "        db.close()\n\n\n"
                    "@app.get('/tasks/', response_model=list[TaskResponse])\n"
                    "def list_tasks(db: Session = Depends(get_db)):\n"
                    "    return db.query(Task).all()\n\n\n"
                    "@app.post('/tasks/', response_model=TaskResponse, status_code=201)\n"
                    "def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):\n"
                    "    task = Task(title=task_in.title)\n"
                    "    db.add(task); db.commit(); db.refresh(task)\n"
                    "    return task\n\n\n"
                    "@app.patch('/tasks/{task_id}/done', response_model=TaskResponse)\n"
                    "def complete_task(task_id: int, db: Session = Depends(get_db)):\n"
                    "    task = db.query(Task).filter(Task.id == task_id).first()\n"
                    "    if not task:\n"
                    "        raise HTTPException(status_code=404, detail='할 일을 찾을 수 없습니다')\n"
                    "    task.is_done = True\n"
                    "    db.commit(); db.refresh(task)\n"
                    "    return task"
                ),
            },
        ],
        "challenge": {
            "question": (
                "MLOps를 위한 '모델 실험 추적 API'를 만드세요. "
                "1) Experiment 모델 (id, name, model_type, learning_rate FLOAT, epochs INT, "
                "accuracy FLOAT, created_at DateTime) "
                "2) Run 모델 (id, experiment_id → Experiment FK, status, started_at, finished_at) "
                "3) POST /experiments/ — 실험 등록 "
                "4) POST /experiments/{exp_id}/runs/ — 실험 실행 기록 생성 (status='running') "
                "5) PATCH /runs/{run_id}/complete — 실행 완료 처리 (accuracy, status='completed', finished_at 업데이트) "
                "6) GET /experiments/ — 모든 실험 목록 (accuracy 내림차순 정렬) "
                "실제 MLflow가 하는 일의 미니 버전입니다."
            ),
            "hint": (
                "relationship으로 Experiment.runs 역참조 설정. "
                "Alembic 없이 Base.metadata.create_all(bind=engine)로 테이블 생성. "
                "PATCH 완료 엔드포인트: run.status='completed', run.finished_at=datetime.utcnow(), "
                "run.accuracy=accuracy (요청 본문). "
                "정렬: db.query(Experiment).order_by(Experiment.accuracy.desc()).all()"
            ),
        },
        "summary": [
            "SQL의 핵심 4가지: SELECT(조회), INSERT(삽입), UPDATE(수정), DELETE(삭제).",
            "sqlite3 모듈은 표준 라이브러리로 파일 기반 DB를 즉시 사용할 수 있으며, ? 플레이스홀더로 SQL 인젝션을 방지한다.",
            "SQLAlchemy ORM은 파이썬 클래스를 DB 테이블로 매핑해 SQL 없이 객체로 DB를 조작한다.",
            "db.add() → db.commit() → db.refresh() 순서가 ORM에서 객체를 저장하는 표준 흐름이다.",
            "FastAPI의 Depends(get_db)와 yield 패턴으로 요청마다 DB 세션을 안전하게 생성·반납한다.",
            "Alembic은 DB 스키마 변경을 버전으로 관리하며 upgrade/downgrade로 이력을 추적한다.",
        ],
    }
