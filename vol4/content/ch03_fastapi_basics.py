"""챕터 3: FastAPI 입문 — 현대적인 Python 웹 API 프레임워크."""


def get_chapter():
    """챕터 3 콘텐츠를 반환한다."""
    return {
        "number": 3,
        "title": "FastAPI 입문",
        "subtitle": "현대적인 Python 웹 API 프레임워크",
        "big_picture": (
            "FastAPI는 2018년 등장한 파이썬 웹 프레임워크로, "
            "Flask의 단순함과 Django의 강력함 사이 어딘가에 위치하면서도, "
            "자동 문서화·타입 검증·비동기 처리라는 현대적 기능을 기본으로 제공합니다. "
            "MLOps 분야에서 특히 중요한데, 머신러닝 모델을 REST API로 서빙할 때 "
            "FastAPI가 사실상 표준이 되었기 때문입니다. "
            "이 챕터에서는 FastAPI의 핵심 개념을 익히고 "
            "첫 번째 API 서버를 직접 만들어봅니다."
        ),
        "sections": [
            # ── 섹션 1: FastAPI 소개 ─────────────────────────────
            {
                "title": "FastAPI 소개 — 왜 FastAPI인가",
                "content": [
                    "Python 웹 프레임워크에는 Django, Flask, FastAPI 등이 있습니다. "
                    "각각의 목적이 다르므로, 프로젝트 성격에 맞게 선택하는 것이 중요합니다.",
                    {
                        "type": "table",
                        "headers": ["프레임워크", "특징", "주요 사용처"],
                        "rows": [
                            ["Django", "풀스택, 배터리 포함 (ORM/어드민/인증)", "웹 사이트, 관리자 도구"],
                            ["Flask", "마이크로, 최소한의 구조", "간단한 API, 프로토타입"],
                            ["FastAPI", "비동기, 자동 문서화, 타입 기반 검증", "ML 서빙, 고성능 API"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "FastAPI의 3가지 핵심 강점",
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "빠름: Node.js·Go 수준의 고성능 (Starlette + uvicorn 기반)",
                            "자동 문서화: Swagger UI와 ReDoc을 코드 작성만으로 자동 생성",
                            "타입 안전: Pydantic으로 요청/응답 데이터를 자동 검증·직렬화",
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "WSGI vs ASGI — 비동기 서버 게이트웨이 인터페이스",
                    },
                    "전통적인 파이썬 웹 서버는 WSGI(Web Server Gateway Interface) 방식을 사용합니다. "
                    "Flask와 Django는 기본적으로 WSGI 기반입니다. "
                    "반면 FastAPI는 ASGI(Asynchronous Server Gateway Interface) 기반으로 "
                    "비동기 요청을 네이티브로 지원합니다.",
                    {
                        "type": "table",
                        "headers": ["구분", "WSGI", "ASGI"],
                        "rows": [
                            ["동작 방식", "요청 하나씩 순차 처리", "여러 요청 동시 처리 (비동기)"],
                            ["대표 서버", "gunicorn, uWSGI", "uvicorn, hypercorn, daphne"],
                            ["대표 프레임워크", "Flask, Django", "FastAPI, Starlette, Django 4+ (async)"],
                            ["적합 상황", "CPU 집중 작업, 단순 웹사이트", "I/O 집중 작업, ML API, 실시간 서비스"],
                        ],
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "WSGI는 은행 창구 한 명이 손님 한 명씩 처리하는 방식입니다. "
                            "앞 손님이 서류 작성 중이어도 뒤 손님은 기다려야 합니다. "
                            "ASGI는 창구 직원이 서류 작성 대기 중에 다른 손님을 처리할 수 있는 방식입니다. "
                            "I/O 대기(DB 조회, 파일 읽기, 외부 API 호출) 시간에 다른 요청을 처리합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 설치 및 첫 번째 앱 ───────────────────────
            {
                "title": "설치 및 첫 번째 FastAPI 앱",
                "content": [
                    "FastAPI와 비동기 서버 uvicorn을 설치하고 첫 번째 API를 만들어봅니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# FastAPI + uvicorn 설치\n"
                            "pip install fastapi uvicorn[standard]\n\n"
                            "# 개발 시 자동 재시작 옵션\n"
                            "# pip install fastapi[all]  # 모든 선택 의존성 포함"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# main.py\n"
                            "from fastapi import FastAPI\n\n"
                            "# 앱 인스턴스 생성\n"
                            "app = FastAPI(\n"
                            "    title='나의 첫 번째 API',\n"
                            "    description='Python Mastery Series Vol.4 실습',\n"
                            "    version='1.0.0',\n"
                            ")\n\n\n"
                            "@app.get('/')  # GET / 요청을 처리하는 엔드포인트\n"
                            "def read_root():\n"
                            "    \"\"\"루트 엔드포인트 — 서버 상태 확인용.\"\"\"\n"
                            "    return {'message': '안녕하세요, FastAPI!'}\n\n\n"
                            "@app.get('/health')\n"
                            "def health_check():\n"
                            "    \"\"\"헬스 체크 엔드포인트 — 서버 정상 동작 확인.\"\"\"\n"
                            "    return {'status': 'ok'}"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 서버 실행\n"
                            "uvicorn main:app --reload\n\n"
                            "# --reload: 코드 변경 시 자동 재시작 (개발 시 편리)\n"
                            "# main: 파일명 (main.py)\n"
                            "# app: FastAPI 인스턴스 변수명\n\n"
                            "# 실행 후 브라우저에서 확인\n"
                            "# http://127.0.0.1:8000       ← API 엔드포인트\n"
                            "# http://127.0.0.1:8000/docs  ← Swagger UI\n"
                            "# http://127.0.0.1:8000/redoc ← ReDoc"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "uvicorn main:app --reload --host 0.0.0.0 --port 8080 처럼 "
                            "호스트와 포트를 지정할 수 있습니다. "
                            "배포 환경에서는 --reload를 제거하고, "
                            "gunicorn과 함께 사용합니다: "
                            "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 경로 & 쿼리 매개변수 ──────────────────────
            {
                "title": "경로 매개변수와 쿼리 매개변수",
                "content": [
                    "API 엔드포인트는 URL에 변수를 포함할 수 있습니다. "
                    "FastAPI는 두 가지 방식의 매개변수를 지원합니다.",
                    {
                        "type": "heading",
                        "text": "경로 매개변수 (Path Parameter)",
                    },
                    "URL 경로 자체에 포함된 변수입니다. 중괄호로 선언합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI\n\n"
                            "app = FastAPI()\n\n\n"
                            "@app.get('/items/{item_id}')  # {item_id}가 경로 매개변수\n"
                            "def read_item(item_id: int):\n"
                            "    \"\"\"특정 아이템을 조회한다.\"\"\"\n"
                            "    return {'item_id': item_id}\n\n\n"
                            "@app.get('/users/{user_id}/orders/{order_id}')\n"
                            "def read_user_order(user_id: int, order_id: int):\n"
                            "    \"\"\"특정 사용자의 특정 주문을 조회한다.\"\"\"\n"
                            "    return {'user_id': user_id, 'order_id': order_id}\n\n\n"
                            "# 타입 힌트가 자동 검증 역할을 함\n"
                            "# GET /items/abc → 422 Unprocessable Entity (int가 아니므로)\n"
                            "# GET /items/42  → {'item_id': 42}"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "쿼리 매개변수 (Query Parameter)",
                    },
                    "URL 뒤에 ?key=value 형태로 붙는 선택적 변수입니다. "
                    "함수 매개변수에 기본값을 주면 쿼리 매개변수가 됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI\n\n"
                            "app = FastAPI()\n\n"
                            "# 가상 데이터베이스\n"
                            "FAKE_DB = [f'아이템 {i}' for i in range(100)]\n\n\n"
                            "@app.get('/items/')\n"
                            "def list_items(skip: int = 0, limit: int = 10):\n"
                            "    \"\"\"아이템 목록을 페이지네이션으로 반환한다.\"\"\"\n"
                            "    return FAKE_DB[skip : skip + limit]\n\n\n"
                            "# 선택적 쿼리 매개변수 (None 기본값)\n"
                            "from typing import Optional\n\n\n"
                            "@app.get('/search/')\n"
                            "def search_items(q: Optional[str] = None, active: bool = True):\n"
                            "    \"\"\"아이템을 검색한다.\"\"\"\n"
                            "    result = {'active': active}\n"
                            "    if q:\n"
                            "        result['query'] = q\n"
                            "    return result\n\n\n"
                            "# GET /items/?skip=20&limit=5  → 21~25번 아이템\n"
                            "# GET /search/?q=노트북        → {'active': True, 'query': '노트북'}"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["구분", "선언 방법", "URL 예시", "특징"],
                        "rows": [
                            ["경로 매개변수", "경로에 {변수명} 표기", "/users/42", "필수, 리소스 식별"],
                            ["쿼리 매개변수", "함수 인자에 기본값 지정", "/items/?page=2", "선택적, 필터/정렬/페이징"],
                        ],
                    },
                ],
            },
            # ── 섹션 4: Pydantic 모델과 요청 본문 ─────────────────
            {
                "title": "Pydantic 모델로 요청 본문 처리",
                "content": [
                    "POST/PUT 요청은 JSON 형태의 요청 본문(Request Body)을 포함합니다. "
                    "FastAPI는 Pydantic 모델을 이용해 자동으로 파싱하고 검증합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI\n"
                            "from pydantic import BaseModel, Field\n"
                            "from typing import Optional\n\n"
                            "app = FastAPI()\n\n\n"
                            "# Pydantic 모델 정의 — 요청/응답 데이터 구조\n"
                            "class ItemCreate(BaseModel):\n"
                            "    \"\"\"아이템 생성 요청 모델.\"\"\"\n"
                            "    name: str = Field(..., min_length=1, max_length=100, description='아이템 이름')\n"
                            "    price: float = Field(..., gt=0, description='가격 (0 초과)')\n"
                            "    description: Optional[str] = Field(None, max_length=500)\n"
                            "    is_available: bool = True\n\n\n"
                            "@app.post('/items/')\n"
                            "def create_item(item: ItemCreate):\n"
                            "    \"\"\"새 아이템을 생성한다.\"\"\"\n"
                            "    # item은 이미 검증된 Python 객체\n"
                            "    return {\n"
                            "        'message': f'{item.name} 생성 완료',\n"
                            "        'item': item.model_dump(),  # Pydantic v2\n"
                            "    }\n\n\n"
                            "# 잘못된 요청 예시 — FastAPI가 자동으로 422 반환\n"
                            "# {'name': '', 'price': -100}  → 422 Unprocessable Entity\n"
                            "# {'name': '노트북'}           → 422 (price 누락)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "경로 + 쿼리 + 본문을 함께 사용하기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class ItemUpdate(BaseModel):\n"
                            "    \"\"\"아이템 수정 요청 모델.\"\"\"\n"
                            "    name: Optional[str] = None\n"
                            "    price: Optional[float] = Field(None, gt=0)\n"
                            "    is_available: Optional[bool] = None\n\n\n"
                            "@app.put('/items/{item_id}')\n"
                            "def update_item(\n"
                            "    item_id: int,         # 경로 매개변수\n"
                            "    notify: bool = False,  # 쿼리 매개변수\n"
                            "    item: ItemUpdate = ...,  # 요청 본문\n"
                            "):\n"
                            "    \"\"\"아이템을 수정한다.\"\"\"\n"
                            "    result = {'item_id': item_id, 'updated': item.model_dump(exclude_none=True)}\n"
                            "    if notify:\n"
                            "        result['notification'] = '수정 알림이 전송되었습니다'\n"
                            "    return result"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Pydantic v2(FastAPI 0.100+ 기본)에서는 .dict() 대신 .model_dump()를 사용합니다. "
                            "Field()의 ... (Ellipsis)는 '필수 값'을 의미합니다. "
                            "gt=0은 'greater than 0'으로 0 초과를 강제합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 자동 API 문서 ──────────────────────────────
            {
                "title": "자동 API 문서 — Swagger UI와 ReDoc",
                "content": [
                    "FastAPI의 가장 강력한 기능 중 하나는 코드를 작성하면 "
                    "자동으로 대화형 API 문서가 생성된다는 것입니다. "
                    "별도의 설정 없이 두 가지 문서 인터페이스를 제공합니다.",
                    {
                        "type": "table",
                        "headers": ["URL", "도구", "특징"],
                        "rows": [
                            ["/docs", "Swagger UI", "대화형 테스트 가능, 버튼 클릭으로 API 호출"],
                            ["/redoc", "ReDoc", "읽기 전용, 깔끔한 레이아웃, 인쇄용"],
                            ["/openapi.json", "OpenAPI 스펙", "JSON 형태의 API 명세서 (자동 생성)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI\n"
                            "from pydantic import BaseModel\n\n"
                            "app = FastAPI(\n"
                            "    title='군 보급 관리 API',\n"
                            "    description='''\n"
                            "## 보급품 관리 시스템 API\n\n"
                            "이 API로 보급품을 등록·조회·수정·삭제합니다.\n"
                            "    ''',\n"
                            "    version='2.1.0',\n"
                            ")\n\n\n"
                            "class Supply(BaseModel):\n"
                            "    \"\"\"보급품 모델.\"\"\"\n"
                            "    name: str\n"
                            "    quantity: int\n"
                            "    unit: str  # 단위: 개, 박스, kg 등\n\n\n"
                            "@app.get(\n"
                            "    '/supplies/',\n"
                            "    summary='보급품 목록 조회',\n"
                            "    description='현재 재고에 있는 보급품 전체 목록을 반환합니다.',\n"
                            "    tags=['보급품'],  # Swagger UI에서 그룹화\n"
                            ")\n"
                            "def list_supplies():\n"
                            "    \"\"\"보급품 목록을 반환한다.\"\"\"\n"
                            "    return []  # 실제로는 DB 조회"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "tags 매개변수로 관련 엔드포인트를 그룹화하면 Swagger UI가 훨씬 깔끔해집니다. "
                            "summary는 엔드포인트 한 줄 설명, description은 상세 설명입니다. "
                            "docstring도 description으로 자동 반영됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 응답 모델과 상태 코드 ─────────────────────
            {
                "title": "응답 모델과 상태 코드",
                "content": [
                    "FastAPI는 응답 모델을 명시해 반환 데이터를 검증하고, "
                    "불필요한 필드(비밀번호 등)를 자동으로 제거할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI, status\n"
                            "from pydantic import BaseModel\n"
                            "from typing import Optional\n\n"
                            "app = FastAPI()\n\n\n"
                            "class UserCreate(BaseModel):\n"
                            "    \"\"\"사용자 생성 요청 모델 (비밀번호 포함).\"\"\"\n"
                            "    username: str\n"
                            "    email: str\n"
                            "    password: str  # 입력 시에만 사용\n\n\n"
                            "class UserResponse(BaseModel):\n"
                            "    \"\"\"사용자 응답 모델 (비밀번호 제외).\"\"\"\n"
                            "    id: int\n"
                            "    username: str\n"
                            "    email: str\n"
                            "    # password 필드 없음 → 응답에서 자동 제거\n\n\n"
                            "@app.post(\n"
                            "    '/users/',\n"
                            "    response_model=UserResponse,    # 응답 모델 지정\n"
                            "    status_code=status.HTTP_201_CREATED,  # 201 Created\n"
                            ")\n"
                            "def create_user(user: UserCreate):\n"
                            "    \"\"\"사용자를 생성한다. 비밀번호는 응답에 포함되지 않는다.\"\"\"\n"
                            "    # DB 저장 후 ID 부여 (시뮬레이션)\n"
                            "    return {\n"
                            "        'id': 1,\n"
                            "        'username': user.username,\n"
                            "        'email': user.email,\n"
                            "        'password': user.password,  # 있어도 응답에서 필터링됨!\n"
                            "    }"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["상태 코드", "FastAPI 상수", "의미"],
                        "rows": [
                            ["200", "HTTP_200_OK", "조회 성공 (기본값)"],
                            ["201", "HTTP_201_CREATED", "생성 성공"],
                            ["204", "HTTP_204_NO_CONTENT", "삭제 성공 (본문 없음)"],
                            ["400", "HTTP_400_BAD_REQUEST", "잘못된 요청"],
                            ["401", "HTTP_401_UNAUTHORIZED", "인증 필요"],
                            ["403", "HTTP_403_FORBIDDEN", "권한 없음"],
                            ["404", "HTTP_404_NOT_FOUND", "리소스 없음"],
                            ["422", "HTTP_422_UNPROCESSABLE_ENTITY", "Pydantic 검증 실패 (자동)"],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "FastAPI 요청 처리 파이프라인",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "클라이언트", "sub": "HTTP 요청"},
                            {"label": "uvicorn", "sub": "ASGI 서버"},
                            {"label": "미들웨어", "sub": "CORS·로깅"},
                            {"label": "라우터", "sub": "경로 매칭"},
                            {"label": "Pydantic", "sub": "입력 검증"},
                            {"label": "핸들러 함수", "sub": "비즈니스 로직"},
                            {"label": "Pydantic", "sub": "출력 직렬화"},
                            {"label": "클라이언트", "sub": "JSON 응답"},
                        ],
                        "note": "검증 실패 시 422 응답을 즉시 반환하며 핸들러 함수는 호출되지 않습니다.",
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
                        "MLOps에서 FastAPI 활용: 학습된 모델(pickle/joblib/ONNX)을 "
                        "앱 시작 시 로드해 전역 변수에 저장하고, "
                        "예측 엔드포인트에서 호출합니다. "
                        "@app.on_event('startup') 이벤트를 사용하면 "
                        "서버 시작 시 모델을 한 번만 로드할 수 있습니다."
                    ),
                },
                {
                    "type": "tip",
                    "text": (
                        "프로젝트 구조 권장안: "
                        "main.py (앱 진입점), "
                        "routers/ (엔드포인트 모음), "
                        "schemas/ (Pydantic 모델), "
                        "models/ (DB 모델), "
                        "services/ (비즈니스 로직)으로 분리하면 "
                        "코드가 커져도 관리하기 쉽습니다."
                    ),
                },
                {
                    "type": "warning",
                    "text": (
                        "--reload는 개발 전용입니다. "
                        "운영 환경에서는 반드시 제거하세요. "
                        "운영 배포: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker"
                    ),
                },
            ],
        },
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "FastAPI에서 URL 경로의 일부를 변수로 받으려면 어떻게 선언하는가?",
                "choices": [
                    "A) @app.get('/items/:id') 처럼 콜론(:) 사용",
                    "B) @app.get('/items/{item_id}') 처럼 중괄호 사용",
                    "C) @app.get('/items/<item_id>') 처럼 꺾쇠괄호 사용",
                    "D) @app.get('/items/') 후 함수 인자로만 선언",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "Pydantic 모델에서 Field(None, gt=0)의 의미는?",
                "choices": [
                    "A) 기본값 None, 0 이상인 값만 허용",
                    "B) 기본값 None, 0 초과(양수)인 값만 허용",
                    "C) 기본값 0, None 이면 통과",
                    "D) 기본값 None, 반드시 입력해야 함",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": "FastAPI 서버를 --reload 옵션으로 실행하는 명령어를 작성하시오. (파일명: main.py, 앱 변수명: app)",
                "answer": "uvicorn main:app --reload",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "다음 요구사항을 만족하는 FastAPI 앱을 작성하세요. "
                    "1) POST /soldiers/ 엔드포인트 생성 "
                    "2) 요청 본문: name(str), rank(str), unit(str), years_served(int, 0 이상) "
                    "3) 응답: 입력 데이터에 id=1을 추가해 반환 "
                    "4) 상태 코드 201 반환"
                ),
                "hint": (
                    "BaseModel을 상속한 Soldier 모델을 만드세요. "
                    "years_served: int = Field(..., ge=0)으로 0 이상을 강제합니다. "
                    "status_code=status.HTTP_201_CREATED를 @app.post에 추가하세요."
                ),
                "answer": (
                    "from fastapi import FastAPI, status\n"
                    "from pydantic import BaseModel, Field\n\n"
                    "app = FastAPI()\n\n\n"
                    "class Soldier(BaseModel):\n"
                    "    name: str\n"
                    "    rank: str\n"
                    "    unit: str\n"
                    "    years_served: int = Field(..., ge=0)\n\n\n"
                    "@app.post('/soldiers/', status_code=status.HTTP_201_CREATED)\n"
                    "def create_soldier(soldier: Soldier):\n"
                    "    return {'id': 1, **soldier.model_dump()}"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "응답 모델을 활용해 보안을 강화하세요. "
                    "UserCreate 모델: username(str), password(str), role(str) "
                    "UserResponse 모델: id(int), username(str) (password, role 제외) "
                    "POST /users/ 엔드포인트에 response_model=UserResponse 적용 후 "
                    "password와 role이 응답에서 사라지는지 확인하세요."
                ),
                "hint": (
                    "두 개의 Pydantic 모델을 만들고, "
                    "@app.post('/users/', response_model=UserResponse)로 지정합니다. "
                    "핸들러에서 password와 role을 포함해 반환해도 "
                    "response_model이 필터링합니다."
                ),
                "answer": (
                    "from fastapi import FastAPI\n"
                    "from pydantic import BaseModel\n\n"
                    "app = FastAPI()\n\n\n"
                    "class UserCreate(BaseModel):\n"
                    "    username: str\n"
                    "    password: str\n"
                    "    role: str\n\n\n"
                    "class UserResponse(BaseModel):\n"
                    "    id: int\n"
                    "    username: str\n\n\n"
                    "@app.post('/users/', response_model=UserResponse)\n"
                    "def create_user(user: UserCreate):\n"
                    "    return {'id': 1, 'username': user.username,\n"
                    "            'password': user.password, 'role': user.role}"
                ),
            },
        ],
        "challenge": {
            "question": (
                "간단한 '군 인사 관리 API'를 만드세요. "
                "데이터는 인메모리 딕셔너리로 관리합니다. "
                "1) POST /soldiers/ — 군인 등록 (name, rank, unit, age 필드, 201 반환) "
                "2) GET /soldiers/ — 전체 목록 조회 (rank로 필터링 가능, 쿼리 매개변수) "
                "3) GET /soldiers/{soldier_id} — 특정 군인 조회 (없으면 404) "
                "4) DELETE /soldiers/{soldier_id} — 제대 처리 (204 반환) "
                "응답 모델을 정의해 age가 응답에 포함되지 않도록 하세요."
            ),
            "hint": (
                "SOLDIERS: dict = {} 전역 변수로 데이터 저장. "
                "id는 len(SOLDIERS) + 1로 자동 부여. "
                "rank 필터: if rank: filtered = [s for s in SOLDIERS.values() if s['rank'] == rank] "
                "404 처리: from fastapi import HTTPException, raise HTTPException(status_code=404, detail='군인을 찾을 수 없습니다') "
                "204 반환: @app.delete(..., status_code=204), return None (본문 없음)"
            ),
        },
        "summary": [
            "FastAPI는 ASGI 기반의 현대적 파이썬 웹 프레임워크로 고성능·자동 문서화·타입 검증을 기본 제공한다.",
            "ASGI는 WSGI와 달리 비동기 요청을 동시에 처리하며, uvicorn이 ASGI 서버 역할을 한다.",
            "경로 매개변수는 URL에 {변수명}으로 선언하고, 쿼리 매개변수는 함수 인자 기본값으로 선언한다.",
            "Pydantic 모델은 요청 본문을 자동으로 파싱·검증하며 검증 실패 시 422를 자동 반환한다.",
            "response_model로 응답 스키마를 지정하면 민감한 필드(비밀번호 등)를 자동으로 제거할 수 있다.",
            "/docs(Swagger UI)와 /redoc(ReDoc)은 코드 작성만으로 자동 생성되는 대화형 API 문서다.",
        ],
    }
