"""
Chapter 9: 미니 프로젝트 — 할 일 관리 API 서버
FastAPI + SQLAlchemy + Docker + GitHub Actions를 종합하여 실전 배포 가능한 API 서버를 만든다.

섹션 5~9 및 연습문제는 _ch09_impl.py에 분리 정의되어 있다.
"""
from content._ch09_impl import (
    CHALLENGE,
    EXERCISES,
    SUMMARY,
    _section_ci,
    _section_deploy,
    _section_docker,
    _section_pytest,
    _section_wrapup,
)


def get_chapter():
    return {
        "number": 9,
        "title": "미니 프로젝트 — 할 일 관리 API 서버",
        "subtitle": "FastAPI + SQLAlchemy + Docker + CI/CD 풀 스택 배포",
        "big_picture": (
            "Chapter 1~8에서 배운 FastAPI, SQLAlchemy, pytest, Docker, GitHub Actions를 "
            "하나의 완결된 프로젝트에 녹여냅니다. "
            "할 일(Todo)을 관리하는 REST API 서버를 단계별로 만들고, "
            "Docker 컨테이너로 패키징한 뒤, GitHub Actions CI/CD로 자동 테스트까지 구성합니다. "
            "'API 설계 → DB 연동 → 테스트 → 컨테이너화 → CI/CD'의 전체 흐름을 직접 경험합니다."
        ),
        "sections": [
            _section_overview(),
            _section_structure(),
            _section_fastapi(),
            _section_sqlalchemy(),
            _section_pytest(),
            _section_docker(),
            _section_ci(),
            _section_deploy(),
            _section_wrapup(),
        ],
        "exercises": EXERCISES,
        "challenge": CHALLENGE,
        "summary": SUMMARY,
    }


def _section_overview() -> dict:
    """9.1 프로젝트 소개 & 전체 아키텍처"""
    return {
        "title": "9.1 프로젝트 소개 & 전체 아키텍처",
        "content": [
            (
                "이번 프로젝트는 **할 일 관리 API 서버(Todo API)**입니다. "
                "할 일 항목을 생성·조회·수정·삭제(CRUD)하는 REST API를 FastAPI로 구현하고, "
                "SQLite 데이터베이스에 SQLAlchemy ORM으로 저장합니다. "
                "완성된 앱을 Docker 이미지로 빌드하고, "
                "GitHub Actions로 코드 변경 시 자동 테스트가 실행되도록 설정합니다."
            ),
            {
                "type": "flow_diagram",
                "title": "할 일 관리 API 서버 — 전체 아키텍처",
                "direction": "horizontal",
                "nodes": [
                    {"label": "클라이언트", "sub": "브라우저 / curl / Swagger UI"},
                    {"label": "FastAPI 앱", "sub": "라우터 / Pydantic 스키마"},
                    {"label": "SQLAlchemy", "sub": "ORM / 세션 관리"},
                    {"label": "SQLite DB", "sub": "todo.db 파일"},
                ],
                "note": "Docker 컨테이너로 패키징 → GitHub Actions로 CI 자동화",
            },
            "**프로젝트 요구사항:**",
            {
                "type": "numbered_list",
                "items": [
                    "할 일 CRUD API: POST /todos, GET /todos, GET /todos/{id}, PUT /todos/{id}, DELETE /todos/{id}",
                    "SQLite + SQLAlchemy ORM으로 데이터를 영구 저장한다",
                    "Pydantic 스키마로 요청/응답 데이터를 검증한다",
                    "pytest로 API 엔드포인트 테스트를 작성한다 (커버리지 80% 이상)",
                    "Dockerfile과 docker-compose.yml로 컨테이너화한다",
                    "GitHub Actions CI로 Push 시 자동 테스트를 실행한다",
                    "환경 변수와 헬스체크 엔드포인트로 운영 준비를 완료한다",
                ],
            },
            "**사용하는 기술 스택:**",
            {
                "type": "table",
                "headers": ["기술", "역할", "주요 활용", "챕터"],
                "rows": [
                    ["FastAPI", "웹 프레임워크", "라우터, 의존성 주입", "Ch1-2"],
                    ["Pydantic v2", "데이터 검증", "BaseModel, Field, validator", "Ch2"],
                    ["SQLAlchemy", "ORM", "모델, 세션, 쿼리", "Ch5"],
                    ["SQLite", "데이터베이스", "파일 기반 DB", "Ch5"],
                    ["pytest", "테스트", "TestClient, fixture", "Ch6"],
                    ["Docker", "컨테이너화", "Dockerfile, compose", "Ch7"],
                    ["GitHub Actions", "CI/CD", "워크플로우 YAML", "Ch8"],
                ],
            },
        ],
    }


def _section_structure() -> dict:
    """9.2 프로젝트 구조 설계"""
    return {
        "title": "9.2 프로젝트 구조 설계",
        "content": [
            (
                "프로젝트를 시작하기 전에 디렉터리 구조를 먼저 설계합니다. "
                "기능별로 파일을 분리하면 코드 가독성이 높아지고 유지보수가 쉬워집니다."
            ),
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "todo-api/\n"
                    "├── app/\n"
                    "│   ├── __init__.py\n"
                    "│   ├── main.py          # FastAPI 앱 인스턴스 & 라우터 등록\n"
                    "│   ├── config.py        # 환경 변수 관리 (pydantic-settings)\n"
                    "│   ├── database.py      # SQLAlchemy 엔진 & 세션 설정\n"
                    "│   ├── models.py        # SQLAlchemy ORM 모델\n"
                    "│   ├── schemas.py       # Pydantic 요청/응답 스키마\n"
                    "│   └── router.py        # CRUD 엔드포인트 정의\n"
                    "├── tests/\n"
                    "│   ├── __init__.py\n"
                    "│   ├── conftest.py      # pytest fixture\n"
                    "│   └── test_todos.py    # API 테스트\n"
                    "├── .env.example         # 환경 변수 예시 (git 포함)\n"
                    "├── .gitignore\n"
                    "├── Dockerfile\n"
                    "├── docker-compose.yml\n"
                    "├── requirements.txt\n"
                    "└── .github/\n"
                    "    └── workflows/\n"
                    "        └── ci.yml       # GitHub Actions 워크플로우\n"
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 프로젝트 초기화\n"
                    "mkdir todo-api && cd todo-api\n"
                    "python -m venv venv\n"
                    "source venv/bin/activate\n"
                    "\n"
                    "pip install fastapi uvicorn[standard] sqlalchemy pydantic-settings\n"
                    "pip install pytest httpx pytest-cov\n"
                    "pip freeze > requirements.txt\n"
                    "\n"
                    "mkdir -p app tests .github/workflows\n"
                    "touch app/__init__.py tests/__init__.py\n"
                ),
            },
        ],
    }


def _section_fastapi() -> dict:
    """9.3 1단계: FastAPI CRUD API 구현"""
    return {
        "title": "9.3 1단계: FastAPI CRUD API 구현",
        "content": [
            (
                "Pydantic 스키마로 요청/응답 데이터를 정의하고, "
                "FastAPI 라우터로 5개의 CRUD 엔드포인트를 구현합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# app/schemas.py — Pydantic 요청/응답 스키마\n"
                    "from datetime import datetime\n"
                    "from pydantic import BaseModel, Field\n"
                    "\n"
                    "\n"
                    "class TodoCreate(BaseModel):\n"
                    '    """할 일 생성 요청"""\n'
                    "    title: str = Field(..., min_length=1, max_length=100)\n"
                    "    description: str | None = Field(None, max_length=500)\n"
                    "\n"
                    "\n"
                    "class TodoUpdate(BaseModel):\n"
                    '    """할 일 수정 요청 (모든 필드 선택)"""\n'
                    "    title: str | None = Field(None, min_length=1, max_length=100)\n"
                    "    description: str | None = None\n"
                    "    is_done: bool | None = None\n"
                    "\n"
                    "\n"
                    "class TodoResponse(BaseModel):\n"
                    '    """할 일 응답"""\n'
                    "    id: int\n"
                    "    title: str\n"
                    "    description: str | None\n"
                    "    is_done: bool\n"
                    "    created_at: datetime\n"
                    "\n"
                    "    model_config = {'from_attributes': True}  # ORM 모드\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# app/router.py — CRUD 엔드포인트\n"
                    "from fastapi import APIRouter, Depends, HTTPException, status\n"
                    "from sqlalchemy.orm import Session\n"
                    "from app import models, schemas\n"
                    "from app.database import get_db\n"
                    "\n"
                    "\n"
                    "router = APIRouter()\n"
                    "\n"
                    "\n"
                    "@router.post('/', response_model=schemas.TodoResponse,\n"
                    "             status_code=status.HTTP_201_CREATED)\n"
                    "def create_todo(payload: schemas.TodoCreate,\n"
                    "                db: Session = Depends(get_db)) -> models.Todo:\n"
                    "    todo = models.Todo(title=payload.title,\n"
                    "                      description=payload.description)\n"
                    "    db.add(todo)\n"
                    "    db.commit()\n"
                    "    db.refresh(todo)\n"
                    "    return todo\n"
                    "\n"
                    "\n"
                    "@router.get('/', response_model=list[schemas.TodoResponse])\n"
                    "def list_todos(skip: int = 0, limit: int = 20,\n"
                    "               db: Session = Depends(get_db)) -> list[models.Todo]:\n"
                    "    return db.query(models.Todo).offset(skip).limit(limit).all()\n"
                    "\n"
                    "\n"
                    "@router.get('/{todo_id}', response_model=schemas.TodoResponse)\n"
                    "def get_todo(todo_id: int,\n"
                    "             db: Session = Depends(get_db)) -> models.Todo:\n"
                    "    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()\n"
                    "    if todo is None:\n"
                    "        raise HTTPException(status_code=404,\n"
                    "                            detail=f'id={todo_id}인 할 일을 찾을 수 없습니다.')\n"
                    "    return todo\n"
                    "\n"
                    "\n"
                    "@router.put('/{todo_id}', response_model=schemas.TodoResponse)\n"
                    "def update_todo(todo_id: int, payload: schemas.TodoUpdate,\n"
                    "                db: Session = Depends(get_db)) -> models.Todo:\n"
                    "    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()\n"
                    "    if todo is None:\n"
                    "        raise HTTPException(status_code=404, detail='할 일을 찾을 수 없습니다.')\n"
                    "    for key, value in payload.model_dump(exclude_unset=True).items():\n"
                    "        setattr(todo, key, value)\n"
                    "    db.commit()\n"
                    "    db.refresh(todo)\n"
                    "    return todo\n"
                    "\n"
                    "\n"
                    "@router.delete('/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)\n"
                    "def delete_todo(todo_id: int,\n"
                    "                db: Session = Depends(get_db)) -> None:\n"
                    "    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()\n"
                    "    if todo is None:\n"
                    "        raise HTTPException(status_code=404, detail='할 일을 찾을 수 없습니다.')\n"
                    "    db.delete(todo)\n"
                    "    db.commit()\n"
                ),
            },
        ],
    }


def _section_sqlalchemy() -> dict:
    """9.4 2단계: SQLAlchemy DB 연동"""
    return {
        "title": "9.4 2단계: SQLAlchemy DB 연동",
        "content": [
            (
                "SQLAlchemy ORM으로 데이터를 SQLite 파일에 영구 저장합니다. "
                "데이터베이스 연결 설정, ORM 모델 정의, 세션 관리를 구현합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# app/database.py — SQLAlchemy 엔진 & 세션\n"
                    "import os\n"
                    "from sqlalchemy import create_engine\n"
                    "from sqlalchemy.orm import sessionmaker, DeclarativeBase\n"
                    "\n"
                    "\n"
                    "DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./todo.db')\n"
                    "\n"
                    "# SQLite는 멀티스레드 허용 옵션 필요\n"
                    "connect_args = (\n"
                    "    {'check_same_thread': False}\n"
                    "    if DATABASE_URL.startswith('sqlite') else {}\n"
                    ")\n"
                    "\n"
                    "engine = create_engine(DATABASE_URL, connect_args=connect_args)\n"
                    "SessionLocal = sessionmaker(autocommit=False, autoflush=False,\n"
                    "                           bind=engine)\n"
                    "\n"
                    "\n"
                    "class Base(DeclarativeBase):\n"
                    "    pass\n"
                    "\n"
                    "\n"
                    "def get_db():\n"
                    '    """요청마다 DB 세션을 생성하고, 요청 완료 후 닫는 의존성 함수."""\n'
                    "    db = SessionLocal()\n"
                    "    try:\n"
                    "        yield db\n"
                    "    finally:\n"
                    "        db.close()\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# app/models.py — SQLAlchemy ORM 모델 (SQLAlchemy 2.0 스타일)\n"
                    "from datetime import datetime, UTC\n"
                    "from sqlalchemy import Boolean, DateTime, Integer, String, Text\n"
                    "from sqlalchemy.orm import Mapped, mapped_column\n"
                    "from app.database import Base\n"
                    "\n"
                    "\n"
                    "class Todo(Base):\n"
                    '    """할 일 ORM 모델 — todos 테이블에 매핑"""\n'
                    "    __tablename__ = 'todos'\n"
                    "\n"
                    "    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)\n"
                    "    title: Mapped[str] = mapped_column(String(100), nullable=False)\n"
                    "    description: Mapped[str | None] = mapped_column(Text, nullable=True)\n"
                    "    is_done: Mapped[bool] = mapped_column(Boolean, default=False)\n"
                    "    created_at: Mapped[datetime] = mapped_column(\n"
                    "        DateTime(timezone=True),\n"
                    "        default=lambda: datetime.now(UTC),\n"
                    "    )\n"
                ),
            },
            {
                "type": "note",
                "text": (
                    "SQLAlchemy 2.0부터는 Mapped와 mapped_column을 사용하는 "
                    "새로운 선언적 방식을 권장합니다. "
                    "타입 힌트 기반이므로 IDE 자동완성이 잘 동작하고 "
                    "코드 가독성도 크게 향상됩니다."
                ),
            },
        ],
    }
