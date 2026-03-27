"""
Ch09 프로젝트 — 구현 세부 섹션 (5~9단계 + 연습문제)
ch09_project.py에서 임포트하여 사용한다.
"""


def _section_pytest() -> dict:
    """3단계: pytest API 테스트"""
    return {
        "title": "9.5 3단계: pytest로 API 테스트",
        "content": [
            (
                "FastAPI의 TestClient를 사용하면 실제 서버를 실행하지 않고도 "
                "API 엔드포인트를 테스트할 수 있습니다. "
                "테스트용 인메모리 SQLite DB를 별도로 사용하여 "
                "테스트가 실제 데이터에 영향을 주지 않도록 합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# tests/conftest.py — pytest fixture 설정\n"
                    "import pytest\n"
                    "from fastapi.testclient import TestClient\n"
                    "from sqlalchemy import create_engine\n"
                    "from sqlalchemy.orm import sessionmaker\n"
                    "from app.main import app\n"
                    "from app.database import Base, get_db\n"
                    "\n"
                    "\n"
                    "TEST_DATABASE_URL = 'sqlite:///./test.db'\n"
                    "\n"
                    "test_engine = create_engine(\n"
                    "    TEST_DATABASE_URL,\n"
                    "    connect_args={'check_same_thread': False},\n"
                    ")\n"
                    "TestSessionLocal = sessionmaker(\n"
                    "    autocommit=False, autoflush=False, bind=test_engine\n"
                    ")\n"
                    "\n"
                    "\n"
                    "@pytest.fixture(scope='function')\n"
                    "def client():\n"
                    '    """각 테스트마다 새로운 DB와 클라이언트를 생성한다."""\n'
                    "    Base.metadata.create_all(bind=test_engine)\n"
                    "\n"
                    "    def override_get_db():\n"
                    "        db = TestSessionLocal()\n"
                    "        try:\n"
                    "            yield db\n"
                    "        finally:\n"
                    "            db.close()\n"
                    "\n"
                    "    app.dependency_overrides[get_db] = override_get_db\n"
                    "\n"
                    "    with TestClient(app) as c:\n"
                    "        yield c\n"
                    "\n"
                    "    # 테스트 후 DB 초기화\n"
                    "    Base.metadata.drop_all(bind=test_engine)\n"
                    "    app.dependency_overrides.clear()\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# tests/test_todos.py — API 테스트\n"
                    "from fastapi.testclient import TestClient\n"
                    "\n"
                    "\n"
                    "class TestCreateTodo:\n"
                    '    """할 일 생성 API 테스트"""\n'
                    "\n"
                    "    def test_create_todo_success(self, client: TestClient):\n"
                    '        """정상적인 할 일 생성 — 201 반환"""\n'
                    "        payload = {'title': '장보기', 'description': '우유, 계란'}\n"
                    "        response = client.post('/todos/', json=payload)\n"
                    "\n"
                    "        assert response.status_code == 201\n"
                    "        data = response.json()\n"
                    "        assert data['title'] == '장보기'\n"
                    "        assert data['is_done'] is False\n"
                    "        assert 'id' in data and 'created_at' in data\n"
                    "\n"
                    "    def test_create_todo_empty_title(self, client: TestClient):\n"
                    '        """빈 제목으로 생성 시도 — 422 반환"""\n'
                    "        response = client.post('/todos/', json={'title': ''})\n"
                    "        assert response.status_code == 422\n"
                    "\n"
                    "\n"
                    "class TestReadTodos:\n"
                    '    """할 일 조회 API 테스트"""\n'
                    "\n"
                    "    def test_list_todos_empty(self, client: TestClient):\n"
                    '        """빈 목록 조회 — 빈 배열 반환"""\n'
                    "        response = client.get('/todos/')\n"
                    "        assert response.status_code == 200\n"
                    "        assert response.json() == []\n"
                    "\n"
                    "    def test_list_todos_with_data(self, client: TestClient):\n"
                    '        """데이터 있는 목록 조회"""\n'
                    "        client.post('/todos/', json={'title': '공부하기'})\n"
                    "        client.post('/todos/', json={'title': '운동하기'})\n"
                    "        response = client.get('/todos/')\n"
                    "        assert len(response.json()) == 2\n"
                    "\n"
                    "    def test_get_todo_not_found(self, client: TestClient):\n"
                    '        """존재하지 않는 id 조회 — 404 반환"""\n'
                    "        assert client.get('/todos/999').status_code == 404\n"
                    "\n"
                    "\n"
                    "class TestUpdateDeleteTodo:\n"
                    '    """할 일 수정 & 삭제 API 테스트"""\n'
                    "\n"
                    "    def test_update_todo_done(self, client: TestClient):\n"
                    '        """할 일 완료 처리"""\n'
                    "        todo_id = client.post('/todos/', json={'title': '보고서'}).json()['id']\n"
                    "        resp = client.put(f'/todos/{todo_id}', json={'is_done': True})\n"
                    "        assert resp.status_code == 200\n"
                    "        assert resp.json()['is_done'] is True\n"
                    "\n"
                    "    def test_delete_todo(self, client: TestClient):\n"
                    '        """삭제 후 404 확인"""\n'
                    "        todo_id = client.post('/todos/', json={'title': '삭제 테스트'}).json()['id']\n"
                    "        assert client.delete(f'/todos/{todo_id}').status_code == 204\n"
                    "        assert client.get(f'/todos/{todo_id}').status_code == 404\n"
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 테스트 실행 & 커버리지 측정\n"
                    "pytest tests/ -v\n"
                    "pytest tests/ --cov=app --cov-report=term-missing --cov-fail-under=80\n"
                ),
            },
        ],
    }


def _section_docker() -> dict:
    """4단계: Dockerfile & docker-compose"""
    return {
        "title": "9.6 4단계: Dockerfile & docker-compose 작성",
        "content": [
            (
                "애플리케이션을 Docker 컨테이너로 패키징합니다. "
                "docker-compose로 로컬 개발 환경을 구성하고, "
                "레이어 캐시를 활용하여 빌드 속도를 최적화합니다."
            ),
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# Dockerfile\n"
                    "FROM python:3.12-slim\n"
                    "WORKDIR /app\n"
                    "\n"
                    "# 의존성 파일만 먼저 복사 (캐시 활용)\n"
                    "COPY requirements.txt .\n"
                    "RUN pip install --no-cache-dir -r requirements.txt\n"
                    "\n"
                    "# 소스 코드 복사\n"
                    "COPY app/ ./app/\n"
                    "\n"
                    "EXPOSE 8000\n"
                    "\n"
                    "HEALTHCHECK --interval=30s --timeout=10s --start-period=5s \\\n"
                    "  CMD python -c \"import urllib.request; urllib.request.urlopen('http://localhost:8000/health')\"\n"
                    "\n"
                    "CMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\", \"--workers\", \"4\"]\n"
                ),
            },
            {
                "type": "code",
                "language": "yaml",
                "code": (
                    "# docker-compose.yml — 로컬 개발 환경\n"
                    "version: '3.9'\n"
                    "\n"
                    "services:\n"
                    "  api:\n"
                    "    build: .\n"
                    "    ports:\n"
                    "      - '8000:8000'\n"
                    "    environment:\n"
                    "      - DATABASE_URL=sqlite:///./data/todo.db\n"
                    "    volumes:\n"
                    "      - ./data:/app/data      # DB 파일 영구 보존\n"
                    "      - ./app:/app/app        # 소스 코드 마운트 (개발용)\n"
                    "    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload\n"
                    "    healthcheck:\n"
                    "      test: [\"CMD\", \"python\", \"-c\",\n"
                    "             \"import urllib.request; urllib.request.urlopen('http://localhost:8000/health')\"]\n"
                    "      interval: 30s\n"
                    "      timeout: 10s\n"
                    "      retries: 3\n"
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# Docker 주요 명령어\n"
                    "docker build -t todo-api:latest .\n"
                    "docker run -p 8000:8000 todo-api:latest\n"
                    "docker compose up --build    # 개발 환경\n"
                    "docker compose up -d         # 백그라운드 실행\n"
                    "docker compose logs -f api   # 로그 확인\n"
                    "docker compose down          # 중지 & 정리\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "requirements.txt를 먼저 복사하고 pip install을 실행한 다음 "
                    "소스 코드를 복사하면 Docker 레이어 캐시를 효율적으로 활용합니다. "
                    "소스 코드만 바뀌어도 pip install 레이어는 캐시에서 재사용됩니다."
                ),
            },
        ],
    }


def _section_ci() -> dict:
    """5단계: GitHub Actions CI"""
    return {
        "title": "9.7 5단계: GitHub Actions CI 파이프라인",
        "content": [
            (
                "GitHub에 코드를 Push하면 자동으로 테스트가 실행되는 "
                "CI(Continuous Integration) 파이프라인을 설정합니다. "
                "main 브랜치와 PR에 모두 적용하여 코드 품질을 유지합니다."
            ),
            {
                "type": "code",
                "language": "yaml",
                "code": (
                    "# .github/workflows/ci.yml\n"
                    "name: CI\n"
                    "\n"
                    "on:\n"
                    "  push:\n"
                    "    branches: [main, develop]\n"
                    "  pull_request:\n"
                    "    branches: [main]\n"
                    "\n"
                    "jobs:\n"
                    "  test:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    steps:\n"
                    "      - uses: actions/checkout@v4\n"
                    "\n"
                    "      - uses: actions/setup-python@v5\n"
                    "        with:\n"
                    "          python-version: '3.12'\n"
                    "          cache: 'pip'\n"
                    "\n"
                    "      - name: 의존성 설치\n"
                    "        run: pip install -r requirements.txt\n"
                    "\n"
                    "      - name: 테스트 실행 (커버리지 80% 이상 필수)\n"
                    "        run: pytest tests/ -v --cov=app --cov-report=xml --cov-fail-under=80\n"
                    "\n"
                    "  docker-build:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    needs: test\n"
                    "    steps:\n"
                    "      - uses: actions/checkout@v4\n"
                    "      - name: Docker 이미지 빌드 검증\n"
                    "        run: docker build -t todo-api:test .\n"
                ),
            },
            {
                "type": "table",
                "headers": ["단계", "설명", "실패 시 동작"],
                "rows": [
                    ["checkout", "저장소 코드를 가져옴", "워크플로우 중단"],
                    ["setup-python", "Python 버전 설정 + pip 캐시", "워크플로우 중단"],
                    ["pip install", "의존성 설치", "워크플로우 중단"],
                    ["pytest", "테스트 + 커버리지 80% 체크", "빨간 X, PR 머지 차단 가능"],
                    ["docker build", "Dockerfile 빌드 검증", "빨간 X 표시"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "GitHub 저장소 설정에서 'Require status checks to pass before merging'을 "
                    "활성화하면 CI가 실패한 PR은 자동으로 머지가 차단됩니다."
                ),
            },
        ],
    }


def _section_deploy() -> dict:
    """6단계: 배포 준비"""
    return {
        "title": "9.8 6단계: 배포 준비 — 환경 변수 & 헬스체크",
        "content": [
            (
                "프로덕션 배포 전에 환경 변수 관리와 헬스체크를 완성합니다. "
                "환경 변수로 설정을 분리하면 개발·스테이징·프로덕션 환경에서 "
                "같은 코드를 다른 설정으로 실행할 수 있습니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# app/config.py — pydantic-settings로 환경 변수 관리\n"
                    "from pydantic_settings import BaseSettings\n"
                    "\n"
                    "\n"
                    "class Settings(BaseSettings):\n"
                    '    """앱 설정 — .env 파일 또는 환경 변수에서 자동으로 읽는다."""\n'
                    "    database_url: str = 'sqlite:///./todo.db'\n"
                    "    app_name: str = '할 일 관리 API'\n"
                    "    app_version: str = '1.0.0'\n"
                    "    debug: bool = False\n"
                    "    secret_key: str = 'dev-secret-key-change-in-production'\n"
                    "\n"
                    "    class Config:\n"
                    "        env_file = '.env'\n"
                    "        case_sensitive = False\n"
                    "\n"
                    "\n"
                    "settings = Settings()\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# app/main.py — DB 헬스체크 포함 최종 버전\n"
                    "from fastapi import FastAPI\n"
                    "from sqlalchemy import text\n"
                    "from app import models\n"
                    "from app.config import settings\n"
                    "from app.database import engine, SessionLocal\n"
                    "from app.router import router\n"
                    "\n"
                    "\n"
                    "models.Base.metadata.create_all(bind=engine)\n"
                    "\n"
                    "app = FastAPI(\n"
                    "    title=settings.app_name,\n"
                    "    version=settings.app_version,\n"
                    "    debug=settings.debug,\n"
                    ")\n"
                    "app.include_router(router, prefix='/todos', tags=['todos'])\n"
                    "\n"
                    "\n"
                    "@app.get('/health', tags=['system'])\n"
                    "def health_check() -> dict:\n"
                    '    """DB 연결까지 확인하는 헬스체크"""\n'
                    "    db_status = 'ok'\n"
                    "    try:\n"
                    "        db = SessionLocal()\n"
                    "        db.execute(text('SELECT 1'))\n"
                    "        db.close()\n"
                    "    except Exception:\n"
                    "        db_status = 'error'\n"
                    "    return {\n"
                    "        'status': 'ok' if db_status == 'ok' else 'degraded',\n"
                    "        'version': settings.app_version,\n"
                    "        'database': db_status,\n"
                    "    }\n"
                ),
            },
            {
                "type": "table",
                "headers": ["배포 준비 항목", "확인 방법", "비고"],
                "rows": [
                    ["환경 변수 분리", ".env 파일 + .gitignore 설정", "SECRET_KEY 반드시 교체"],
                    ["헬스체크 엔드포인트", "GET /health 200 응답 확인", "로드밸런서 연동"],
                    ["데이터 볼륨 마운트", "docker-compose volumes 설정", "DB 파일 영구 보존"],
                    ["Worker 수 설정", "uvicorn --workers 4", "CPU 코어 수 기준"],
                    ["로그 레벨 설정", "uvicorn --log-level info", "프로덕션은 warning"],
                    ["CORS 설정", "FastAPI CORSMiddleware 추가", "프론트엔드 도메인 허용"],
                ],
            },
        ],
    }


def _section_wrapup() -> dict:
    """9단계: 마무리"""
    return {
        "title": "9.9 마무리",
        "content": [
            (
                "전체 프로젝트를 완성했습니다. "
                "FastAPI로 REST API를 만들고, SQLAlchemy로 DB를 연결하고, "
                "pytest로 테스트를 작성하고, Docker로 컨테이너화하고, "
                "GitHub Actions로 CI 파이프라인을 구성했습니다. "
                "이 구조는 실제 스타트업과 기업에서 사용하는 백엔드 아키텍처와 동일합니다."
            ),
            {
                "type": "note",
                "text": (
                    "MLOps 관점에서: 이 프로젝트 구조에 ML 모델을 추가하면 "
                    "모델 서빙 API가 됩니다. "
                    "Vol.5에서는 이 API 서버에 Scikit-learn 모델을 올리고 "
                    "MLflow로 실험을 관리하는 방법을 배웁니다."
                ),
            },
            "**핵심 정리:**",
            {
                "type": "bullet_list",
                "items": [
                    "FastAPI: 라우터 분리, Pydantic 스키마, 의존성 주입(Depends)으로 깔끔한 API 설계",
                    "SQLAlchemy: ORM 모델, 세션 관리, get_db() 의존성 패턴",
                    "pytest: TestClient, fixture, dependency_overrides로 격리된 테스트",
                    "Docker: 레이어 캐시 최적화, HEALTHCHECK, 볼륨 마운트",
                    "GitHub Actions: push/PR 트리거, 커버리지 임계값, Docker 빌드 검증",
                ],
            },
        ],
    }


EXERCISES = [
    {
        "number": 1,
        "type": "coding",
        "question": (
            "Todo 항목에 '마감일(due_date)' 필드를 추가하세요. "
            "ORM 모델, Pydantic 스키마, 라우터를 모두 수정하고 "
            "마감일이 지난 항목을 조회하는 GET /todos/overdue 엔드포인트를 추가하세요."
        ),
        "hint": (
            "models.py에 due_date: Mapped[date | None] = mapped_column(Date, nullable=True) 추가. "
            "overdue 엔드포인트는 db.query(Todo).filter(Todo.due_date < date.today()).all() 사용."
        ),
    },
    {
        "number": 2,
        "type": "coding",
        "question": (
            "할 일 목록 조회(GET /todos/)에 필터링 기능을 추가하세요. "
            "쿼리 파라미터 is_done(True/False)으로 완료 여부를 필터링할 수 있어야 합니다."
        ),
        "hint": (
            "list_todos 함수에 is_done: bool | None = None 파라미터를 추가하고, "
            "값이 있을 때만 .filter(Todo.is_done == is_done)을 적용하세요."
        ),
    },
    {
        "number": 3,
        "type": "short_answer",
        "question": (
            "Dockerfile에서 requirements.txt를 소스 코드보다 먼저 복사하는 이유는 무엇인가요? "
            "Docker 레이어 캐시와 연관지어 설명하세요."
        ),
        "answer": (
            "Docker는 각 명령어를 레이어로 캐시합니다. "
            "requirements.txt를 먼저 복사하고 pip install을 실행하면, "
            "소스 코드만 변경되고 requirements.txt가 바뀌지 않은 경우 "
            "pip install 레이어가 캐시에서 재사용되어 빌드 시간이 크게 단축됩니다."
        ),
    },
]

CHALLENGE = {
    "question": (
        "Todo API에 '카테고리' 기능을 추가하여 다대일(N:1) 관계를 구현하세요. "
        "Category 테이블을 별도로 만들고 Todo가 Category를 참조합니다. "
        "POST /categories로 카테고리를 생성하고, "
        "GET /todos/?category_id=1로 특정 카테고리의 할 일만 조회할 수 있어야 합니다."
    ),
    "hint": (
        "models.py에 Category 모델 추가 후 Todo에 "
        "category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id')) 연결. "
        "schemas.py에 CategoryResponse를 만들고 TodoResponse에 "
        "category: CategoryResponse | None 포함."
    ),
}

SUMMARY = [
    "FastAPI + SQLAlchemy + Docker + GitHub Actions 조합은 현업 백엔드 서비스의 표준 스택입니다.",
    "Pydantic 스키마로 입력을 검증하고, ORM 모델로 DB를 조작하는 역할 분리가 핵심입니다.",
    "pytest TestClient와 dependency_overrides로 격리된 API 테스트를 작성합니다.",
    "Docker 레이어 캐시를 활용하면 빌드 시간을 크게 단축할 수 있습니다.",
    "환경 변수로 설정을 분리하면 개발/스테이징/프로덕션 환경에서 같은 코드를 사용할 수 있습니다.",
    "이 구조에 ML 모델을 추가하면 Vol.5에서 배울 모델 서빙 API가 됩니다.",
]
