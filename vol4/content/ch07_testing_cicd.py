"""챕터 7: 테스트 & CI/CD — 자동화된 품질 보증과 지속적 배포."""


def get_chapter():
    """챕터 7 콘텐츠를 반환한다."""
    return {
        "number": 7,
        "title": "테스트 & CI/CD",
        "subtitle": "자동화된 품질 보증과 지속적 배포",
        "big_picture": (
            "코드를 작성하는 시간보다 버그를 찾고 고치는 시간이 더 길다는 것은 "
            "개발자 사이의 오래된 통설입니다. "
            "테스트는 이 시간을 역전시키는 투자입니다. "
            "CI/CD(지속적 통합/배포)는 테스트를 자동화하여 "
            "코드를 Push할 때마다 자동으로 검증하고 배포합니다. "
            "이 챕터에서는 pytest로 테스트를 작성하는 법, "
            "FastAPI 엔드포인트를 테스트하는 법, "
            "GitHub Actions으로 CI/CD 파이프라인을 구축하는 법을 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: 왜 테스트하는가? ─────────────────────────
            {
                "title": "왜 테스트하는가?",
                "content": [
                    "수동 테스트는 반복적이고, 느리고, 사람이 빠뜨리기 쉽습니다. "
                    "자동화된 테스트는 수 초 만에 수백 가지 시나리오를 검증하고, "
                    "코드 변경 시 의도치 않은 기능 파괴(regression)를 즉시 감지합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "테스트는 건물의 안전 점검과 같습니다. "
                            "매번 건물을 지을 때마다 눈으로만 확인하면 숨겨진 결함을 놓칩니다. "
                            "자동화된 안전 점검 도구(테스트)는 매 공사 단계마다 "
                            "구조적 무결성을 확인합니다. "
                            "초기에는 시간이 걸리지만, 나중에 발생할 대형 사고(버그)를 막습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["테스트 유형", "범위", "속도", "목적"],
                        "rows": [
                            ["단위 테스트 (Unit)", "함수/클래스 하나", "매우 빠름 (밀리초)", "로직 검증"],
                            ["통합 테스트 (Integration)", "모듈 간 상호작용", "보통 (초 단위)", "인터페이스 검증"],
                            ["E2E 테스트 (End-to-End)", "전체 사용자 흐름", "느림 (수십 초)", "시나리오 검증"],
                            ["API 테스트", "HTTP 엔드포인트", "빠름 (밀리초~초)", "계약 검증"],
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["항목", "수동 테스트", "자동화 테스트"],
                        "rows": [
                            ["실행 속도", "수십 분 ~ 시간", "수 초 ~ 수 분"],
                            ["반복 실행", "사람이 매번 해야 함", "코드 push마다 자동 실행"],
                            ["커버리지", "중요 경로 위주", "엣지 케이스 포함 가능"],
                            ["회귀 발견", "놓치기 쉬움", "즉각 감지"],
                            ["비용", "인력 비용 높음", "초기 작성 후 자동화"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "TDD(Test-Driven Development): 테스트를 먼저 작성하고(Red), "
                            "테스트를 통과하는 최소한의 코드를 작성하며(Green), "
                            "코드를 개선합니다(Refactor). "
                            "테스트가 설계 문서 역할을 하여 코드의 의도가 명확해집니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: pytest 기초 ───────────────────────────────
            {
                "title": "pytest 기초: assert, fixture, parametrize",
                "content": [
                    "pytest는 Python 표준 테스트 프레임워크입니다. "
                    "파일명 test_*.py, 함수명 test_로 시작하면 자동으로 인식합니다. "
                    "설치: pip install pytest pytest-cov",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# tests/test_calculator.py\n"
                            "# 테스트할 코드 (app/calculator.py)\n"
                            "def add(a: float, b: float) -> float:\n"
                            "    \"\"\"두 수를 더한다.\"\"\"\n"
                            "    return a + b\n\n\n"
                            "def divide(a: float, b: float) -> float:\n"
                            "    \"\"\"a를 b로 나눈다. b가 0이면 ValueError 발생.\"\"\"\n"
                            "    if b == 0:\n"
                            "        raise ValueError('0으로 나눌 수 없습니다')\n"
                            "    return a / b\n\n\n"
                            "# ── 기본 테스트 ──────────────────────────────────────\n"
                            "def test_add_positive_numbers():\n"
                            "    \"\"\"양수 덧셈을 검증한다.\"\"\"\n"
                            "    result = add(2, 3)\n"
                            "    assert result == 5\n\n\n"
                            "def test_add_negative_numbers():\n"
                            "    \"\"\"음수 덧셈을 검증한다.\"\"\"\n"
                            "    assert add(-1, -2) == -3\n\n\n"
                            "def test_divide_by_zero_raises():\n"
                            "    \"\"\"0으로 나눌 때 ValueError가 발생함을 검증한다.\"\"\"\n"
                            "    import pytest\n"
                            "    with pytest.raises(ValueError, match='0으로 나눌 수 없습니다'):\n"
                            "        divide(10, 0)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── fixture: 테스트 간 공유 객체/데이터 설정 ──────────\n"
                            "import pytest\n"
                            "from app.models import User\n"
                            "from app.services import UserService\n\n\n"
                            "@pytest.fixture\n"
                            "def sample_user():\n"
                            "    \"\"\"테스트용 사용자 객체를 반환한다.\"\"\"\n"
                            "    return User(id=1, name='홍길동', email='hong@example.com')\n\n\n"
                            "@pytest.fixture\n"
                            "def user_service():\n"
                            "    \"\"\"테스트용 UserService 인스턴스를 반환한다.\"\"\"\n"
                            "    return UserService()\n\n\n"
                            "def test_user_name(sample_user):\n"
                            "    \"\"\"사용자 이름이 올바른지 검증한다.\"\"\"\n"
                            "    assert sample_user.name == '홍길동'\n\n\n"
                            "def test_user_email_format(sample_user):\n"
                            "    \"\"\"이메일에 '@'가 포함되어 있는지 검증한다.\"\"\"\n"
                            "    assert '@' in sample_user.email\n\n\n"
                            "# ── scope: fixture의 생명주기 제어 ────────────────────\n"
                            "@pytest.fixture(scope='module')  # 모듈 전체에서 한 번만 생성\n"
                            "def db_connection():\n"
                            "    \"\"\"테스트용 DB 연결을 반환한다.\"\"\"\n"
                            "    conn = create_test_db()\n"
                            "    yield conn          # yield 이후는 teardown\n"
                            "    conn.close()"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── parametrize: 여러 입력값으로 같은 테스트 반복 ──────\n"
                            "import pytest\n\n\n"
                            "@pytest.mark.parametrize('a, b, expected', [\n"
                            "    (1, 2, 3),        # 양수\n"
                            "    (-1, 1, 0),       # 음수 + 양수\n"
                            "    (0, 0, 0),        # 영\n"
                            "    (1.5, 2.5, 4.0),  # 실수\n"
                            "])\n"
                            "def test_add_parametrize(a, b, expected):\n"
                            "    \"\"\"다양한 입력으로 add 함수를 검증한다.\"\"\"\n"
                            "    assert add(a, b) == expected\n\n\n"
                            "# ── 테스트 실행 명령어 ──────────────────────────────────\n"
                            "# pytest                    # 전체 테스트\n"
                            "# pytest -v                 # 상세 출력\n"
                            "# pytest tests/test_calc.py # 특정 파일만\n"
                            "# pytest -k 'add'           # 이름에 'add'가 포함된 테스트만\n"
                            "# pytest -x                 # 첫 번째 실패 시 중단\n"
                            "# pytest --tb=short         # 간략한 traceback"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "conftest.py 파일에 fixture를 정의하면 같은 디렉토리의 모든 테스트 파일에서 "
                            "자동으로 사용할 수 있습니다. "
                            "import 없이 파라미터 이름만 맞추면 pytest가 자동으로 주입합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: FastAPI API 테스트 ────────────────────────
            {
                "title": "FastAPI API 테스트 (TestClient, httpx)",
                "content": [
                    "FastAPI는 TestClient를 내장하고 있어 실제 HTTP 서버를 시작하지 않고도 "
                    "API 엔드포인트를 테스트할 수 있습니다. "
                    "내부적으로 httpx 라이브러리를 사용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# app/main.py — 테스트 대상 FastAPI 앱\n"
                            "from fastapi import FastAPI, HTTPException\n"
                            "from pydantic import BaseModel\n\n\n"
                            "app = FastAPI()\n"
                            "_items: dict[int, dict] = {}  # 인메모리 저장소\n\n\n"
                            "class Item(BaseModel):\n"
                            "    name: str\n"
                            "    price: float\n\n\n"
                            "@app.get('/health')\n"
                            "def health_check():\n"
                            "    return {'status': 'ok'}\n\n\n"
                            "@app.post('/items', status_code=201)\n"
                            "def create_item(item: Item):\n"
                            "    item_id = len(_items) + 1\n"
                            "    _items[item_id] = item.model_dump()\n"
                            "    return {'id': item_id, **item.model_dump()}\n\n\n"
                            "@app.get('/items/{item_id}')\n"
                            "def get_item(item_id: int):\n"
                            "    if item_id not in _items:\n"
                            "        raise HTTPException(status_code=404, detail='아이템 없음')\n"
                            "    return {'id': item_id, **_items[item_id]}"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# tests/test_main.py\n"
                            "import pytest\n"
                            "from fastapi.testclient import TestClient\n"
                            "from app.main import app\n\n\n"
                            "@pytest.fixture\n"
                            "def client():\n"
                            "    \"\"\"테스트용 FastAPI 클라이언트를 반환한다.\"\"\"\n"
                            "    with TestClient(app) as c:\n"
                            "        yield c\n\n\n"
                            "def test_health_check(client):\n"
                            "    \"\"\"헬스체크 엔드포인트가 200을 반환하는지 검증한다.\"\"\"\n"
                            "    response = client.get('/health')\n"
                            "    assert response.status_code == 200\n"
                            "    assert response.json() == {'status': 'ok'}\n\n\n"
                            "def test_create_item(client):\n"
                            "    \"\"\"아이템 생성 엔드포인트를 검증한다.\"\"\"\n"
                            "    payload = {'name': '노트북', 'price': 1200000.0}\n"
                            "    response = client.post('/items', json=payload)\n\n"
                            "    assert response.status_code == 201\n"
                            "    data = response.json()\n"
                            "    assert data['name'] == '노트북'\n"
                            "    assert data['price'] == 1200000.0\n"
                            "    assert 'id' in data\n\n\n"
                            "def test_get_item_not_found(client):\n"
                            "    \"\"\"존재하지 않는 아이템 조회 시 404를 반환하는지 검증한다.\"\"\"\n"
                            "    response = client.get('/items/9999')\n"
                            "    assert response.status_code == 404\n"
                            "    assert response.json()['detail'] == '아이템 없음'\n\n\n"
                            "def test_create_item_invalid_price(client):\n"
                            "    \"\"\"가격이 문자열인 경우 422 Unprocessable Entity를 반환한다.\"\"\"\n"
                            "    response = client.post('/items', json={'name': '책', 'price': '비쌈'})\n"
                            "    assert response.status_code == 422"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "TestClient는 실제 서버를 띄우지 않으므로 "
                            "DB, 외부 API 등 외부 의존성을 Mock으로 대체해야 합니다. "
                            "pytest-mock 또는 unittest.mock을 사용하거나, "
                            "FastAPI의 dependency_overrides를 활용하면 "
                            "테스트용 의존성을 쉽게 교체할 수 있습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# dependency_overrides로 DB 의존성 테스트용으로 교체\n"
                            "from app.database import get_db\n"
                            "from app.main import app\n"
                            "from fastapi.testclient import TestClient\n\n\n"
                            "# 테스트용 인메모리 DB 세션\n"
                            "def override_get_db():\n"
                            "    \"\"\"테스트용 SQLite 인메모리 세션을 반환한다.\"\"\"\n"
                            "    from sqlalchemy import create_engine\n"
                            "    from sqlalchemy.orm import sessionmaker\n"
                            "    engine = create_engine('sqlite://')  # 인메모리\n"
                            "    Session = sessionmaker(bind=engine)\n"
                            "    Base.metadata.create_all(engine)\n"
                            "    db = Session()\n"
                            "    try:\n"
                            "        yield db\n"
                            "    finally:\n"
                            "        db.close()\n\n\n"
                            "# 의존성 교체\n"
                            "app.dependency_overrides[get_db] = override_get_db\n\n"
                            "client = TestClient(app)"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 테스트 커버리지 ───────────────────────────
            {
                "title": "테스트 커버리지 측정 (pytest-cov)",
                "content": [
                    "커버리지는 테스트가 실행한 코드 라인의 비율입니다. "
                    "80% 이상을 목표로 하되, 100%가 목표가 아닌 "
                    "중요한 비즈니스 로직 커버가 진짜 목표입니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── 설치 ────────────────────────────────────────────\n"
                            "pip install pytest-cov\n\n"
                            "# ── 커버리지 측정 실행 ──────────────────────────────\n"
                            "# 터미널에 커버리지 요약 출력\n"
                            "pytest --cov=app --cov-report=term-missing\n\n"
                            "# HTML 리포트 생성 (htmlcov/index.html)\n"
                            "pytest --cov=app --cov-report=html\n\n"
                            "# 커버리지 기준 미달 시 실패 (CI에서 필수)\n"
                            "pytest --cov=app --cov-fail-under=80\n\n"
                            "# ── 출력 예시 ────────────────────────────────────────\n"
                            "# Name                    Stmts   Miss  Cover   Missing\n"
                            "# -------------------------------------------------------\n"
                            "# app/main.py                 32      4    88%   45-48\n"
                            "# app/services.py             28      2    93%   67, 71\n"
                            "# -------------------------------------------------------\n"
                            "# TOTAL                       60      6    90%"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# pytest.ini 또는 pyproject.toml에 기본 설정 저장\n"
                            "# pyproject.toml 예시:\n"
                            "[tool.pytest.ini_options]\n"
                            "testpaths = ['tests']\n"
                            "addopts = '--cov=app --cov-report=term-missing --cov-fail-under=80'\n\n"
                            "# 특정 코드를 커버리지에서 제외 (pragma 주석)\n"
                            "def debug_only_function():  # pragma: no cover\n"
                            "    \"\"\"개발 중에만 사용하는 함수.\"\"\"\n"
                            "    ..."
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "커버리지 100%가 버그 없음을 보장하지는 않습니다. "
                            "assert result is not None 처럼 의미 없는 테스트로 커버리지를 채우는 것은 "
                            "오히려 유지보수 비용을 높입니다. "
                            "엣지 케이스(경계값, 오류 케이스)를 중심으로 의미 있는 테스트를 작성하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: GitHub Actions 소개 ──────────────────────
            {
                "title": "GitHub Actions 소개",
                "content": [
                    "GitHub Actions는 GitHub 저장소에 통합된 CI/CD 플랫폼입니다. "
                    ".github/workflows/ 디렉토리에 YAML 파일을 추가하면 "
                    "코드 Push, PR 생성, 스케줄 등 다양한 이벤트에 반응하여 "
                    "자동으로 워크플로우를 실행합니다.",
                    {
                        "type": "table",
                        "headers": ["개념", "설명", "예시"],
                        "rows": [
                            ["Workflow", "자동화 전체 프로세스", "CI 파이프라인 전체"],
                            ["Event", "워크플로우 트리거", "push, pull_request, schedule"],
                            ["Job", "독립적으로 실행되는 작업 단위", "test, build, deploy"],
                            ["Step", "Job 내의 개별 명령어", "pip install, pytest 실행"],
                            ["Action", "재사용 가능한 스텝 묶음", "actions/checkout@v4"],
                            ["Runner", "워크플로우를 실행하는 서버", "ubuntu-latest, macos-latest"],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "CI/CD 파이프라인: Push → Test → Build → Deploy",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "개발자 Push", "sub": "git push origin main"},
                            {"label": "CI 트리거", "sub": "GitHub Actions 시작"},
                            {"label": "테스트 실행", "sub": "pytest + 커버리지"},
                            {"label": "이미지 빌드", "sub": "docker build"},
                            {"label": "레지스트리 Push", "sub": "Docker Hub / ECR"},
                            {"label": "배포", "sub": "서버 자동 업데이트"},
                        ],
                        "note": "테스트 실패 시 이후 단계가 실행되지 않아 불안정한 코드가 배포되지 않습니다.",
                    },
                    {
                        "type": "note",
                        "text": (
                            "GitHub Actions는 공개 저장소에서 무료로 사용할 수 있습니다. "
                            "비공개 저장소는 매월 2,000분의 무료 실행 시간이 제공됩니다. "
                            "ubuntu-latest Runner를 사용하는 것이 가장 빠르고 경제적입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: CI 파이프라인 구축 ────────────────────────
            {
                "title": "CI 파이프라인 구축 (.github/workflows YAML)",
                "content": [
                    "실제 FastAPI 프로젝트에 CI 파이프라인을 구축해봅시다. "
                    "Pull Request가 생성되거나 main 브랜치에 Push될 때마다 "
                    "린트, 타입 체크, 테스트를 자동으로 실행합니다.",
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": (
                            "# .github/workflows/ci.yml\n"
                            "name: CI\n\n"
                            "on:\n"
                            "  push:\n"
                            "    branches: [main, develop]\n"
                            "  pull_request:\n"
                            "    branches: [main]\n\n"
                            "jobs:\n"
                            "  test:\n"
                            "    name: 테스트 및 린트\n"
                            "    runs-on: ubuntu-latest\n\n"
                            "    steps:\n"
                            "      # 1. 소스 코드 체크아웃\n"
                            "      - name: 코드 체크아웃\n"
                            "        uses: actions/checkout@v4\n\n"
                            "      # 2. Python 환경 설정\n"
                            "      - name: Python 3.11 설정\n"
                            "        uses: actions/setup-python@v5\n"
                            "        with:\n"
                            "          python-version: '3.11'\n"
                            "          cache: 'pip'       # pip 캐시로 빌드 속도 향상\n\n"
                            "      # 3. 의존성 설치\n"
                            "      - name: 의존성 설치\n"
                            "        run: |\n"
                            "          pip install --upgrade pip\n"
                            "          pip install -r requirements.txt\n"
                            "          pip install pytest pytest-cov ruff\n\n"
                            "      # 4. 코드 스타일 검사 (ruff)\n"
                            "      - name: 린트 (ruff)\n"
                            "        run: ruff check .\n\n"
                            "      # 5. 테스트 실행 및 커버리지 측정\n"
                            "      - name: pytest 실행\n"
                            "        run: |\n"
                            "          pytest --cov=app \\\n"
                            "                 --cov-report=xml \\\n"
                            "                 --cov-fail-under=80 \\\n"
                            "                 -v\n\n"
                            "      # 6. 커버리지 리포트 업로드 (선택)\n"
                            "      - name: Codecov 업로드\n"
                            "        uses: codecov/codecov-action@v4\n"
                            "        with:\n"
                            "          file: ./coverage.xml"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": (
                            "# .github/workflows/ci.yml — 환경 변수와 시크릿 사용\n"
                            "jobs:\n"
                            "  test:\n"
                            "    runs-on: ubuntu-latest\n\n"
                            "    # 테스트 DB를 서비스 컨테이너로 실행\n"
                            "    services:\n"
                            "      postgres:\n"
                            "        image: postgres:15-alpine\n"
                            "        env:\n"
                            "          POSTGRES_USER: testuser\n"
                            "          POSTGRES_PASSWORD: testpassword\n"
                            "          POSTGRES_DB: testdb\n"
                            "        options: >-\n"
                            "          --health-cmd pg_isready\n"
                            "          --health-interval 10s\n"
                            "          --health-retries 5\n"
                            "        ports:\n"
                            "          - 5432:5432\n\n"
                            "    env:\n"
                            "      DATABASE_URL: postgresql://testuser:testpassword@localhost:5432/testdb\n"
                            "      SECRET_KEY: ${{ secrets.TEST_SECRET_KEY }}  # GitHub Secrets 사용\n\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-python@v5\n"
                            "        with:\n"
                            "          python-version: '3.11'\n"
                            "      - run: pip install -r requirements.txt\n"
                            "      - run: pytest -v"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "GitHub Secrets(저장소 Settings > Secrets)에 API 키, 비밀번호 등을 저장하고 "
                            "${{ secrets.MY_SECRET }}으로 참조하세요. "
                            "시크릿 값은 로그에 출력되지 않아 안전합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 7: CD — 자동 배포 개념 ─────────────────────
            {
                "title": "CD: 지속적 배포 개념",
                "content": [
                    "CI가 코드 검증을 자동화한다면, "
                    "CD(Continuous Delivery/Deployment)는 검증된 코드를 "
                    "자동으로 배포 환경에 반영합니다. "
                    "main 브랜치에 머지되면 자동으로 스테이징 또는 운영 서버에 배포됩니다.",
                    {
                        "type": "table",
                        "headers": ["용어", "설명"],
                        "rows": [
                            ["Continuous Integration (CI)", "코드 통합 시 자동 테스트 및 빌드"],
                            ["Continuous Delivery (CD)", "언제든 배포 가능한 상태 유지 (수동 배포 승인)"],
                            ["Continuous Deployment", "검증 후 자동으로 운영 배포 (승인 없이)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": (
                            "# .github/workflows/cd.yml — Docker 이미지 빌드 후 Docker Hub Push\n"
                            "name: CD\n\n"
                            "on:\n"
                            "  push:\n"
                            "    branches: [main]\n\n"
                            "jobs:\n"
                            "  deploy:\n"
                            "    name: Docker 이미지 빌드 및 배포\n"
                            "    runs-on: ubuntu-latest\n"
                            "    needs: [test]        # CI 잡이 성공한 후에만 실행\n\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n\n"
                            "      # Docker Hub 로그인\n"
                            "      - name: Docker Hub 로그인\n"
                            "        uses: docker/login-action@v3\n"
                            "        with:\n"
                            "          username: ${{ secrets.DOCKERHUB_USERNAME }}\n"
                            "          password: ${{ secrets.DOCKERHUB_TOKEN }}\n\n"
                            "      # 이미지 빌드 및 Push\n"
                            "      - name: 이미지 빌드 및 Push\n"
                            "        uses: docker/build-push-action@v5\n"
                            "        with:\n"
                            "          push: true\n"
                            "          tags: |\n"
                            "            myusername/my-app:latest\n"
                            "            myusername/my-app:${{ github.sha }}"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "github.sha는 커밋 해시로, 이미지에 태그를 붙이면 "
                            "어느 커밋으로 만들어진 이미지인지 추적할 수 있습니다. "
                            "latest 태그만 사용하면 이전 버전으로 롤백하기 어렵습니다. "
                            "커밋 SHA 또는 버전 태그(v1.2.3)를 함께 사용하세요."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "테스트 파일은 tests/ 디렉토리에 모아두고, 테스트 대상 모듈과 같은 이름에 test_ 접두사를 붙입니다 (예: app/services.py → tests/test_services.py).",
            "conftest.py에 공통 fixture를 정의하면 모든 테스트 파일에서 import 없이 사용할 수 있습니다.",
            "FastAPI의 dependency_overrides를 활용하면 테스트에서 DB나 외부 API 의존성을 쉽게 Mock으로 대체할 수 있습니다.",
            "GitHub Actions에서 actions/setup-python의 cache: 'pip' 옵션을 사용하면 의존성 설치 시간을 크게 단축합니다.",
            "CI 워크플로우에 --cov-fail-under=80 옵션을 추가하면 커버리지가 80% 미만일 때 CI가 실패하여 품질을 강제합니다.",
            "배포 워크플로우는 needs: [test]로 테스트 잡에 의존하게 하여, 테스트 실패 시 배포가 차단되도록 합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "pytest에서 여러 입력값으로 동일한 테스트 함수를 반복 실행하는 데코레이터는?"
                ),
                "choices": [
                    "A) @pytest.fixture",
                    "B) @pytest.mark.parametrize",
                    "C) @pytest.mark.repeat",
                    "D) @pytest.mark.loop",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "FastAPI 테스트에서 실제 서버 없이 HTTP 요청을 보낼 수 있게 해주는 클래스는?"
                ),
                "choices": [
                    "A) requests.Session",
                    "B) httpx.AsyncClient",
                    "C) fastapi.testclient.TestClient",
                    "D) unittest.mock.MagicMock",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "GitHub Actions에서 다른 Job이 성공한 후에만 현재 Job을 실행하려면 어떤 키워드를 사용하나요?"
                ),
                "choices": [
                    "A) after:",
                    "B) requires:",
                    "C) needs:",
                    "D) depends_on:",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "문자열이 유효한 이메일 형식인지 확인하는 함수 is_valid_email(email: str) -> bool을 "
                    "테스트하는 pytest 코드를 작성하세요. "
                    "유효한 케이스 2개(user@example.com, test.user+tag@domain.co.kr)와 "
                    "유효하지 않은 케이스 2개(@nodomain.com, nodomain.com)를 "
                    "@pytest.mark.parametrize로 테스트해야 합니다."
                ),
                "hint": (
                    "@pytest.mark.parametrize('email, expected', [...])로 "
                    "(email, True/False) 튜플 리스트를 전달하고, "
                    "assert is_valid_email(email) == expected를 검증하세요."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "main 브랜치에 push될 때 실행되는 GitHub Actions CI 워크플로우를 작성하세요. "
                    "Python 3.11을 사용하고, requirements.txt를 설치한 후, "
                    "pytest를 실행하며 커버리지가 80% 미만이면 실패해야 합니다."
                ),
                "hint": (
                    ".github/workflows/ci.yml 파일을 생성합니다. "
                    "on: push: branches: [main], "
                    "jobs > test > steps: checkout, setup-python(3.11), pip install, "
                    "pytest --cov=app --cov-fail-under=80 순서로 작성합니다."
                ),
            },
        ],
        "challenge": {
            "question": (
                "챕터 5~6에서 만든 FastAPI + Docker 프로젝트에 완전한 CI/CD 파이프라인을 구축하세요. "
                "요구사항: "
                "1) tests/ 디렉토리를 만들고 최소 5개의 테스트를 작성합니다 "
                "(헬스체크, CRUD 엔드포인트 각 1개 이상, 유효성 검사 실패 케이스 포함). "
                "2) pytest --cov=app --cov-fail-under=80이 통과해야 합니다. "
                "3) .github/workflows/ci.yml을 작성하여 PR 생성 및 main Push 시 "
                "lint(ruff) + test가 자동 실행되도록 합니다. "
                "4) .github/workflows/cd.yml을 작성하여 CI 성공 후 "
                "Docker 이미지를 Docker Hub에 자동 Push합니다. "
                "5) GitHub Secrets에 DOCKERHUB_USERNAME과 DOCKERHUB_TOKEN을 등록하여 "
                "워크플로우가 실제로 동작함을 확인합니다."
            ),
            "hint": (
                "TestClient fixture는 conftest.py에 정의하세요. "
                "ruff check . 명령으로 린트를 실행합니다. "
                "docker/build-push-action@v5를 사용하면 이미지 빌드와 Push를 한 번에 처리합니다. "
                "needs: [test] 설정으로 테스트 Job이 성공한 후에만 배포 Job이 실행됩니다."
            ),
        },
        "summary": [
            "pytest는 Python 표준 테스트 프레임워크로, fixture로 공유 객체를 관리하고 parametrize로 다양한 입력을 효율적으로 테스트한다.",
            "FastAPI TestClient를 사용하면 실제 서버 없이 HTTP 엔드포인트를 빠르게 테스트할 수 있다.",
            "pytest-cov로 커버리지를 측정하고 --cov-fail-under=80으로 최소 기준을 강제한다.",
            "GitHub Actions는 .github/workflows/ YAML 파일로 정의하며, push/PR 이벤트에 반응하여 자동으로 실행된다.",
            "CI 파이프라인은 lint → test → build 순서로 구성하고, 각 단계 실패 시 이후 단계가 실행되지 않는다.",
            "CD 파이프라인은 needs: [test]로 CI 성공 후에만 실행되어, 검증되지 않은 코드가 배포되지 않도록 보장한다.",
        ],
    }
