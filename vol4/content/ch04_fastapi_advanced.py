"""챕터 4: FastAPI 심화 — 비동기 & 의존성 주입."""


def get_chapter():
    """챕터 4 콘텐츠를 반환한다."""
    return {
        "number": 4,
        "title": "FastAPI 심화 — 비동기 & 의존성 주입",
        "subtitle": "async/await, Depends, 미들웨어, 에러 핸들링",
        "big_picture": (
            "챕터 3에서 FastAPI의 기본 문법을 익혔다면, "
            "이번 챕터는 FastAPI를 실무 수준으로 만드는 핵심 기능들을 다룹니다. "
            "비동기(async/await)는 I/O 병목을 해소해 서버 처리량을 극적으로 늘리고, "
            "의존성 주입(Depends)은 코드 중복을 없애며 테스트를 쉽게 만듭니다. "
            "CORS 미들웨어, 백그라운드 태스크, 체계적인 에러 핸들링까지 갖추면 "
            "프로덕션에 배포할 수 있는 API가 완성됩니다."
        ),
        "sections": [
            # ── 섹션 1: async/await 기초 ──────────────────────────
            {
                "title": "async/await 기초 — 동기 vs 비동기",
                "content": [
                    "파이썬은 기본적으로 동기(synchronous) 실행 모델입니다. "
                    "한 작업이 끝나야 다음 작업이 시작됩니다. "
                    "비동기(asynchronous)는 I/O 대기 중에 다른 작업을 처리할 수 있게 합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "동기 방식은 라면을 끓이면서 물이 끓을 때까지 냄비 앞에 서서 기다리는 것입니다. "
                            "비동기 방식은 라면 물을 올려놓고 그 사이 반찬을 준비하다가, "
                            "물이 끓으면 알림을 받고 면을 넣는 것입니다. "
                            "CPU는 I/O 대기 중에 다른 요청을 처리합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import asyncio\n"
                            "import time\n\n\n"
                            "# 동기 방식 — 순차 실행\n"
                            "def sync_fetch(url: str) -> str:\n"
                            "    \"\"\"동기 방식 데이터 수집 — I/O 동안 블로킹.\"\"\"\n"
                            "    time.sleep(1)  # 네트워크 대기 시뮬레이션\n"
                            "    return f'{url}의 데이터'\n\n\n"
                            "def sync_main():\n"
                            "    \"\"\"3개 URL을 순차적으로 수집 — 총 3초 소요.\"\"\"\n"
                            "    urls = ['url1', 'url2', 'url3']\n"
                            "    results = [sync_fetch(url) for url in urls]\n"
                            "    return results\n\n\n"
                            "# 비동기 방식 — 동시 실행\n"
                            "async def async_fetch(url: str) -> str:\n"
                            "    \"\"\"비동기 방식 데이터 수집 — 대기 중 다른 작업 가능.\"\"\"\n"
                            "    await asyncio.sleep(1)  # 블로킹 없이 대기\n"
                            "    return f'{url}의 데이터'\n\n\n"
                            "async def async_main():\n"
                            "    \"\"\"3개 URL을 동시에 수집 — 총 약 1초 소요.\"\"\"\n"
                            "    urls = ['url1', 'url2', 'url3']\n"
                            "    results = await asyncio.gather(*[async_fetch(url) for url in urls])\n"
                            "    return results"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "async/await 핵심 규칙",
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "async def로 정의한 함수는 코루틴(coroutine)이 된다",
                            "코루틴 내부에서만 await를 사용할 수 있다",
                            "await는 비동기 작업이 완료될 때까지 현재 코루틴을 일시 중단한다",
                            "일시 중단된 동안 이벤트 루프가 다른 코루틴을 실행한다",
                            "CPU 집약 작업(계산)은 비동기 효과가 없다 — I/O 작업에만 의미있다",
                        ],
                    },
                ],
            },
            # ── 섹션 2: 비동기 엔드포인트 ──────────────────────────
            {
                "title": "비동기 FastAPI 엔드포인트 작성",
                "content": [
                    "FastAPI에서 엔드포인트는 동기(def)와 비동기(async def) 둘 다 작성할 수 있습니다. "
                    "DB 조회, 외부 API 호출, 파일 I/O처럼 대기가 발생하는 작업은 async def로 작성하세요.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import asyncio\n"
                            "import httpx  # 비동기 HTTP 클라이언트 (pip install httpx)\n"
                            "from fastapi import FastAPI\n\n"
                            "app = FastAPI()\n\n\n"
                            "# 동기 엔드포인트 — CPU 작업에 적합\n"
                            "@app.get('/calculate/')\n"
                            "def heavy_calculation(n: int):\n"
                            "    \"\"\"무거운 계산 — 비동기 불필요.\"\"\"\n"
                            "    result = sum(i * i for i in range(n))\n"
                            "    return {'result': result}\n\n\n"
                            "# 비동기 엔드포인트 — I/O 작업에 적합\n"
                            "@app.get('/external-data/')\n"
                            "async def fetch_external_data():\n"
                            "    \"\"\"외부 API 호출 — 비동기로 대기 시간 동안 다른 요청 처리.\"\"\"\n"
                            "    async with httpx.AsyncClient() as client:\n"
                            "        response = await client.get(\n"
                            "            'https://jsonplaceholder.typicode.com/todos/1',\n"
                            "            timeout=10.0,\n"
                            "        )\n"
                            "        response.raise_for_status()\n"
                            "        return response.json()\n\n\n"
                            "# 여러 비동기 작업을 동시에 실행\n"
                            "@app.get('/multi-fetch/')\n"
                            "async def fetch_multiple():\n"
                            "    \"\"\"여러 외부 API를 동시에 호출한다.\"\"\"\n"
                            "    async with httpx.AsyncClient() as client:\n"
                            "        # asyncio.gather로 동시 실행\n"
                            "        responses = await asyncio.gather(\n"
                            "            client.get('https://jsonplaceholder.typicode.com/todos/1'),\n"
                            "            client.get('https://jsonplaceholder.typicode.com/todos/2'),\n"
                            "            client.get('https://jsonplaceholder.typicode.com/todos/3'),\n"
                            "        )\n"
                            "    return [r.json() for r in responses]"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["상황", "권장 방식", "이유"],
                        "rows": [
                            ["DB 조회 (비동기 드라이버)", "async def + await", "I/O 대기 동안 다른 요청 처리"],
                            ["외부 API 호출", "async def + httpx", "네트워크 대기 비차단"],
                            ["파일 읽기/쓰기", "async def + aiofiles", "I/O 대기 비차단"],
                            ["순수 계산", "def (동기)", "await가 필요 없음"],
                            ["동기 라이브러리 사용 불가피", "def (동기)", "FastAPI가 스레드에서 자동 실행"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "FastAPI에서 def로 작성한 동기 함수는 자동으로 스레드 풀에서 실행됩니다. "
                            "따라서 동기 함수가 이벤트 루프를 블로킹하지 않습니다. "
                            "httpx는 requests의 비동기 버전입니다: pip install httpx"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 의존성 주입 ────────────────────────────────
            {
                "title": "의존성 주입 — Depends",
                "content": [
                    "의존성 주입(Dependency Injection)은 함수가 필요로 하는 객체나 값을 "
                    "외부에서 제공받는 패턴입니다. "
                    "FastAPI의 Depends를 사용하면 인증, 페이지네이션, DB 세션 등 "
                    "공통 로직을 재사용하고 테스트하기 쉽게 만들 수 있습니다.",
                    {
                        "type": "flow_diagram",
                        "title": "의존성 주입 체인",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "요청 수신", "sub": "클라이언트 → 라우터"},
                            {"label": "의존성 해결", "sub": "Depends(get_db) → DB 세션 생성"},
                            {"label": "상위 의존성", "sub": "Depends(get_current_user) → 토큰 검증"},
                            {"label": "핸들러 실행", "sub": "검증된 user + db 세션 전달"},
                            {"label": "정리(cleanup)", "sub": "yield 이후 DB 세션 닫기"},
                        ],
                        "note": "의존성은 체인처럼 연결됩니다. 상위 의존성이 실패하면 핸들러는 호출되지 않습니다.",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI, Depends, HTTPException, status\n"
                            "from typing import Optional\n\n"
                            "app = FastAPI()\n\n\n"
                            "# ── 의존성 1: 공통 페이지네이션 매개변수 ──\n"
                            "class PaginationParams:\n"
                            "    \"\"\"페이지네이션 매개변수 의존성.\"\"\"\n"
                            "    def __init__(self, skip: int = 0, limit: int = 10):\n"
                            "        if limit > 100:\n"
                            "            raise HTTPException(\n"
                            "                status_code=400, detail='limit은 100 이하여야 합니다'\n"
                            "            )\n"
                            "        self.skip = skip\n"
                            "        self.limit = limit\n\n\n"
                            "FAKE_ITEMS = [f'item_{i}' for i in range(50)]\n\n\n"
                            "@app.get('/items/')\n"
                            "def list_items(pagination: PaginationParams = Depends()):\n"
                            "    \"\"\"Depends()는 클래스 의존성을 자동으로 인스턴스화한다.\"\"\"\n"
                            "    return FAKE_ITEMS[pagination.skip : pagination.skip + pagination.limit]\n\n\n"
                            "@app.get('/orders/')\n"
                            "def list_orders(pagination: PaginationParams = Depends()):\n"
                            "    \"\"\"같은 페이지네이션 의존성을 재사용한다.\"\"\"\n"
                            "    return {'skip': pagination.skip, 'limit': pagination.limit}"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 의존성 2: 인증 (토큰 검증) ──\n"
                            "from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials\n\n"
                            "security = HTTPBearer()\n\n"
                            "# 실제 환경에서는 JWT 라이브러리(python-jose 등) 사용\n"
                            "VALID_TOKENS = {'secret-token-admin': 'admin', 'secret-token-user': 'user'}\n\n\n"
                            "def get_current_user(\n"
                            "    credentials: HTTPAuthorizationCredentials = Depends(security),\n"
                            ") -> dict:\n"
                            "    \"\"\"Authorization 헤더의 Bearer 토큰을 검증한다.\"\"\"\n"
                            "    token = credentials.credentials\n"
                            "    username = VALID_TOKENS.get(token)\n"
                            "    if not username:\n"
                            "        raise HTTPException(\n"
                            "            status_code=status.HTTP_401_UNAUTHORIZED,\n"
                            "            detail='유효하지 않은 토큰입니다',\n"
                            "            headers={'WWW-Authenticate': 'Bearer'},\n"
                            "        )\n"
                            "    return {'username': username}\n\n\n"
                            "@app.get('/profile/')\n"
                            "def read_profile(current_user: dict = Depends(get_current_user)):\n"
                            "    \"\"\"인증된 사용자의 프로필을 반환한다.\"\"\"\n"
                            "    return {'user': current_user['username'], 'message': '환영합니다!'}\n\n\n"
                            "# ── 의존성 3: yield를 사용한 DB 세션 관리 ──\n"
                            "def get_db():\n"
                            "    \"\"\"DB 세션을 생성하고 요청 완료 후 닫는다.\"\"\"\n"
                            "    db = {'connected': True}  # 실제로는 SQLAlchemy Session\n"
                            "    try:\n"
                            "        yield db  # 핸들러에 DB 세션 전달\n"
                            "    finally:\n"
                            "        db['connected'] = False  # 요청 완료 후 정리\n\n\n"
                            "@app.get('/data/')\n"
                            "def read_data(db=Depends(get_db)):\n"
                            "    \"\"\"DB 세션을 사용해 데이터를 조회한다.\"\"\"\n"
                            "    return {'db_connected': db['connected']}"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 미들웨어 ───────────────────────────────────
            {
                "title": "미들웨어 — CORS, 로깅, 인증",
                "content": [
                    "미들웨어(Middleware)는 모든 요청과 응답 사이에 끼어드는 코드입니다. "
                    "로깅, CORS 설정, 응답 시간 측정, 공통 인증 등에 사용합니다.",
                    {
                        "type": "heading",
                        "text": "CORS 미들웨어 — 프론트엔드와 API 연동 필수",
                    },
                    "CORS(Cross-Origin Resource Sharing)는 다른 도메인에서의 API 호출을 허용하는 정책입니다. "
                    "React/Vue 프론트엔드와 FastAPI 백엔드를 분리 운영할 때 반드시 설정해야 합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI\n"
                            "from fastapi.middleware.cors import CORSMiddleware\n\n"
                            "app = FastAPI()\n\n"
                            "# CORS 미들웨어 등록\n"
                            "app.add_middleware(\n"
                            "    CORSMiddleware,\n"
                            "    allow_origins=[\n"
                            "        'http://localhost:3000',   # React 개발 서버\n"
                            "        'https://myapp.com',       # 운영 프론트엔드\n"
                            "    ],\n"
                            "    allow_credentials=True,\n"
                            "    allow_methods=['*'],  # GET, POST, PUT, DELETE 등 모두 허용\n"
                            "    allow_headers=['*'],  # Authorization, Content-Type 등 모두 허용\n"
                            ")\n\n\n"
                            "# 커스텀 미들웨어 — 요청 처리 시간 측정\n"
                            "import time\n"
                            "from starlette.middleware.base import BaseHTTPMiddleware\n"
                            "from starlette.requests import Request\n\n\n"
                            "class TimingMiddleware(BaseHTTPMiddleware):\n"
                            "    \"\"\"요청 처리 시간을 응답 헤더에 추가하는 미들웨어.\"\"\"\n\n"
                            "    async def dispatch(self, request: Request, call_next):\n"
                            "        start = time.perf_counter()\n"
                            "        response = await call_next(request)  # 다음 처리로 전달\n"
                            "        elapsed = time.perf_counter() - start\n"
                            "        response.headers['X-Process-Time'] = f'{elapsed:.4f}s'\n"
                            "        return response\n\n\n"
                            "app.add_middleware(TimingMiddleware)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "로깅 미들웨어",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import logging\n"
                            "from starlette.middleware.base import BaseHTTPMiddleware\n"
                            "from starlette.requests import Request\n\n"
                            "# 로거 설정\n"
                            "logging.basicConfig(\n"
                            "    level=logging.INFO,\n"
                            "    format='%(asctime)s %(levelname)s %(message)s',\n"
                            ")\n"
                            "logger = logging.getLogger('api')\n\n\n"
                            "class LoggingMiddleware(BaseHTTPMiddleware):\n"
                            "    \"\"\"모든 요청과 응답을 로깅하는 미들웨어.\"\"\"\n\n"
                            "    async def dispatch(self, request: Request, call_next):\n"
                            "        logger.info(f'요청: {request.method} {request.url}')\n"
                            "        response = await call_next(request)\n"
                            "        logger.info(f'응답: {response.status_code}')\n"
                            "        return response\n\n\n"
                            "app.add_middleware(LoggingMiddleware)"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "allow_origins=['*']는 모든 도메인을 허용합니다. "
                            "개발 중에만 사용하고, 운영 환경에서는 반드시 특정 도메인만 허용하세요. "
                            "특히 allow_credentials=True와 함께 allow_origins=['*']를 동시에 쓰면 보안 위험이 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 백그라운드 태스크 ──────────────────────────
            {
                "title": "백그라운드 태스크",
                "content": [
                    "백그라운드 태스크(BackgroundTask)는 요청 응답을 먼저 반환한 후 "
                    "나머지 작업을 비동기적으로 처리합니다. "
                    "이메일 발송, 로그 저장, 리포트 생성 등 시간이 걸리는 작업에 적합합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import time\n"
                            "from fastapi import FastAPI, BackgroundTasks\n"
                            "from pydantic import BaseModel\n\n"
                            "app = FastAPI()\n\n\n"
                            "def send_email_notification(email: str, message: str):\n"
                            "    \"\"\"이메일 발송 — 시간이 걸리는 작업 시뮬레이션.\"\"\"\n"
                            "    time.sleep(2)  # 실제로는 이메일 서버 호출\n"
                            "    print(f'[이메일 발송] {email}: {message}')\n\n\n"
                            "def log_access(user_id: int, action: str):\n"
                            "    \"\"\"접근 로그를 DB에 저장한다.\"\"\"\n"
                            "    print(f'[로그] user_id={user_id}, action={action}')\n\n\n"
                            "class OrderRequest(BaseModel):\n"
                            "    user_email: str\n"
                            "    item_name: str\n\n\n"
                            "@app.post('/orders/')\n"
                            "def create_order(\n"
                            "    order: OrderRequest,\n"
                            "    background_tasks: BackgroundTasks,  # 자동 주입\n"
                            "):\n"
                            "    \"\"\"주문 생성 후 즉시 응답 — 이메일은 백그라운드에서 발송.\"\"\"\n"
                            "    order_id = 12345\n\n"
                            "    # 백그라운드 태스크 등록 (응답 후 실행됨)\n"
                            "    background_tasks.add_task(\n"
                            "        send_email_notification,\n"
                            "        order.user_email,\n"
                            "        f'주문 {order_id}번이 접수되었습니다',\n"
                            "    )\n"
                            "    background_tasks.add_task(\n"
                            "        log_access, 1, f'order_created:{order_id}'\n"
                            "    )\n\n"
                            "    # 이메일 발송 완료를 기다리지 않고 즉시 응답\n"
                            "    return {'order_id': order_id, 'message': '주문이 접수되었습니다'}"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "BackgroundTasks는 경량 작업에 적합합니다. "
                            "수십 초 이상 걸리는 작업이나 재시도가 필요한 작업에는 "
                            "Celery + Redis 같은 전용 작업 큐를 사용하세요. "
                            "MLOps에서 모델 재학습 같은 작업은 Celery를 권장합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 에러 핸들링 ───────────────────────────────
            {
                "title": "에러 핸들링 — HTTPException과 커스텀 예외",
                "content": [
                    "실무 API에서 에러 핸들링은 사용자 경험과 디버깅 효율에 직결됩니다. "
                    "FastAPI는 HTTPException으로 HTTP 에러를 쉽게 발생시키고, "
                    "커스텀 예외 핸들러로 일관된 에러 응답 형식을 강제할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from fastapi import FastAPI, HTTPException, Request, status\n"
                            "from fastapi.responses import JSONResponse\n"
                            "from pydantic import BaseModel\n\n"
                            "app = FastAPI()\n\n"
                            "ITEMS = {1: '노트북', 2: '마우스', 3: '키보드'}\n\n\n"
                            "# ── 기본 HTTPException ──\n"
                            "@app.get('/items/{item_id}')\n"
                            "def read_item(item_id: int):\n"
                            "    \"\"\"아이템이 없으면 404를 발생시킨다.\"\"\"\n"
                            "    if item_id not in ITEMS:\n"
                            "        raise HTTPException(\n"
                            "            status_code=status.HTTP_404_NOT_FOUND,\n"
                            "            detail=f'아이템 {item_id}번을 찾을 수 없습니다',\n"
                            "        )\n"
                            "    return {'name': ITEMS[item_id]}"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 커스텀 예외 클래스 정의 ──\n"
                            "class NotFoundError(Exception):\n"
                            "    \"\"\"리소스를 찾을 수 없을 때 발생하는 예외.\"\"\"\n"
                            "    def __init__(self, resource: str, resource_id: int):\n"
                            "        self.resource = resource\n"
                            "        self.resource_id = resource_id\n\n\n"
                            "class AuthorizationError(Exception):\n"
                            "    \"\"\"권한이 없을 때 발생하는 예외.\"\"\"\n"
                            "    def __init__(self, message: str = '접근 권한이 없습니다'):\n"
                            "        self.message = message\n\n\n"
                            "# ── 커스텀 예외 핸들러 등록 ──\n"
                            "@app.exception_handler(NotFoundError)\n"
                            "async def not_found_handler(request: Request, exc: NotFoundError):\n"
                            "    \"\"\"NotFoundError를 일관된 JSON 형식으로 응답한다.\"\"\"\n"
                            "    return JSONResponse(\n"
                            "        status_code=404,\n"
                            "        content={\n"
                            "            'error': 'NOT_FOUND',\n"
                            "            'message': f'{exc.resource} {exc.resource_id}번이 존재하지 않습니다',\n"
                            "            'resource': exc.resource,\n"
                            "        },\n"
                            "    )\n\n\n"
                            "@app.exception_handler(AuthorizationError)\n"
                            "async def auth_error_handler(request: Request, exc: AuthorizationError):\n"
                            "    return JSONResponse(\n"
                            "        status_code=403,\n"
                            "        content={'error': 'FORBIDDEN', 'message': exc.message},\n"
                            "    )\n\n\n"
                            "# ── 전역 예외 핸들러 — 예상치 못한 에러 처리 ──\n"
                            "@app.exception_handler(Exception)\n"
                            "async def global_exception_handler(request: Request, exc: Exception):\n"
                            "    \"\"\"서버 내부 오류를 클라이언트에 노출하지 않는다.\"\"\"\n"
                            "    import logging\n"
                            "    logging.error(f'예상치 못한 오류: {exc}', exc_info=True)\n"
                            "    return JSONResponse(\n"
                            "        status_code=500,\n"
                            "        content={'error': 'INTERNAL_ERROR', 'message': '서버 오류가 발생했습니다'},\n"
                            "    )\n\n\n"
                            "@app.get('/soldiers/{soldier_id}')\n"
                            "def read_soldier(soldier_id: int):\n"
                            "    \"\"\"커스텀 예외를 사용한 엔드포인트 예시.\"\"\"\n"
                            "    soldiers = {1: '홍길동', 2: '이순신'}\n"
                            "    if soldier_id not in soldiers:\n"
                            "        raise NotFoundError('군인', soldier_id)\n"
                            "    return {'name': soldiers[soldier_id]}"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["방법", "사용 시기", "장점"],
                        "rows": [
                            ["HTTPException", "간단한 HTTP 오류 (404, 401 등)", "빠르고 간결"],
                            ["커스텀 예외 + 핸들러", "도메인 특화 에러, 일관된 에러 포맷", "재사용 가능, 구조화"],
                            ["전역 핸들러", "예상치 못한 오류 캐치", "서버 에러 정보 숨기기, 로깅"],
                        ],
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
                        "의존성 주입으로 테스트하기: "
                        "app.dependency_overrides[get_db] = lambda: mock_db 처럼 "
                        "의존성을 모의 객체로 교체할 수 있습니다. "
                        "실제 DB 없이 테스트 가능합니다."
                    ),
                },
                {
                    "type": "tip",
                    "text": (
                        "MLOps 패턴: 모델 추론 엔드포인트는 async def + 비동기 전처리로 작성하고, "
                        "모델 로드는 lifespan 이벤트(FastAPI 0.93+)나 startup 이벤트에서 한 번만 수행하세요. "
                        "전처리/후처리가 CPU 집약적이면 asyncio.run_in_executor로 스레드에서 실행하세요."
                    ),
                },
                {
                    "type": "warning",
                    "text": (
                        "커스텀 전역 예외 핸들러(Exception)를 등록하면 "
                        "FastAPI 내부 422 검증 오류도 가로챌 수 있습니다. "
                        "RequestValidationError도 별도로 처리해 Pydantic 오류 포맷을 유지하는 것을 권장합니다."
                    ),
                },
            ],
        },
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "FastAPI에서 Depends()를 사용하는 주된 이유는?",
                "choices": [
                    "A) 코드 실행 속도를 높이기 위해",
                    "B) 공통 로직을 재사용하고 테스트하기 쉽게 만들기 위해",
                    "C) 비동기 함수를 동기 함수로 변환하기 위해",
                    "D) 응답 모델을 자동으로 생성하기 위해",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "BackgroundTasks.add_task()의 특징으로 올바른 것은?",
                "choices": [
                    "A) 태스크가 완료될 때까지 응답을 기다린다",
                    "B) 응답을 먼저 반환한 후 태스크를 실행한다",
                    "C) 별도 프로세스에서 실행된다",
                    "D) 태스크 실패 시 자동으로 재시도한다",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "다음 코드에서 await가 필요한 이유를 설명하시오: "
                    "response = await client.get(url)"
                ),
                "answer": (
                    "client.get()은 비동기 함수(코루틴)이므로 await로 완료를 기다려야 합니다. "
                    "await 없이 호출하면 코루틴 객체만 반환되고 실제 HTTP 요청은 실행되지 않습니다."
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "공통 인증 의존성을 만드세요. "
                    "쿼리 매개변수 api_key를 받아 올바른 키('my-secret-key')이면 True를 반환하고, "
                    "아니면 401 HTTPException을 발생시키는 verify_api_key 함수를 작성하고, "
                    "GET /secure-data/ 엔드포인트에 Depends(verify_api_key)로 적용하세요."
                ),
                "hint": (
                    "def verify_api_key(api_key: str) 형태로 쿼리 매개변수를 받습니다. "
                    "raise HTTPException(status_code=401, detail='유효하지 않은 API 키') "
                    "@app.get('/secure-data/'): def read_secure(auth=Depends(verify_api_key))"
                ),
                "answer": (
                    "from fastapi import FastAPI, Depends, HTTPException\n\n"
                    "app = FastAPI()\n\n\n"
                    "def verify_api_key(api_key: str) -> bool:\n"
                    "    if api_key != 'my-secret-key':\n"
                    "        raise HTTPException(status_code=401, detail='유효하지 않은 API 키')\n"
                    "    return True\n\n\n"
                    "@app.get('/secure-data/')\n"
                    "def read_secure(auth: bool = Depends(verify_api_key)):\n"
                    "    return {'data': '기밀 데이터'}"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "모든 요청의 처리 시간을 측정하는 미들웨어를 작성하세요. "
                    "BaseHTTPMiddleware를 상속하고, "
                    "응답 헤더 'X-Process-Time'에 처리 시간(초)을 추가하세요. "
                    "처리 시간은 소수점 4자리까지 표시합니다."
                ),
                "hint": (
                    "import time; start = time.perf_counter() "
                    "response = await call_next(request) "
                    "elapsed = time.perf_counter() - start "
                    "response.headers['X-Process-Time'] = f'{elapsed:.4f}'"
                ),
                "answer": (
                    "import time\n"
                    "from fastapi import FastAPI\n"
                    "from starlette.middleware.base import BaseHTTPMiddleware\n"
                    "from starlette.requests import Request\n\n"
                    "app = FastAPI()\n\n\n"
                    "class TimingMiddleware(BaseHTTPMiddleware):\n"
                    "    async def dispatch(self, request: Request, call_next):\n"
                    "        start = time.perf_counter()\n"
                    "        response = await call_next(request)\n"
                    "        elapsed = time.perf_counter() - start\n"
                    "        response.headers['X-Process-Time'] = f'{elapsed:.4f}'\n"
                    "        return response\n\n\n"
                    "app.add_middleware(TimingMiddleware)"
                ),
            },
        ],
        "challenge": {
            "question": (
                "JWT 인증이 적용된 Todo API를 만드세요. "
                "1) POST /auth/token — 사용자명/비밀번호를 받아 토큰 반환 "
                "(실제 JWT 대신 f'token-{username}' 형식의 가짜 토큰 사용 가능) "
                "2) GET /todos/ — 인증된 사용자의 할 일 목록 조회 (Depends로 토큰 검증) "
                "3) POST /todos/ — 할 일 생성 (title, description 필드) "
                "4) DELETE /todos/{todo_id} — 할 일 삭제 (204 반환) "
                "5) 이메일 알림은 BackgroundTasks로 처리 (실제 전송 없이 print로 시뮬레이션) "
                "모든 에러는 커스텀 예외 핸들러를 통해 일관된 JSON 형식으로 반환하세요."
            ),
            "hint": (
                "토큰 저장: USER_TOKENS = {} 전역 딕셔너리. "
                "token = f'token-{username}' 생성 후 USER_TOKENS[token] = username. "
                "get_current_user 의존성: Authorization 헤더 또는 쿼리 api_token으로 검증. "
                "Todo 저장: TODOS = {} 딕셔너리, id 자동 부여. "
                "background_tasks.add_task(print, f'이메일 알림: ...')"
            ),
        },
        "summary": [
            "async def 함수는 코루틴으로, await로 I/O 대기 중에 이벤트 루프가 다른 요청을 처리한다.",
            "httpx.AsyncClient는 비동기 HTTP 클라이언트로 외부 API 호출에 사용한다.",
            "Depends()는 의존성 주입을 구현해 인증·DB 세션·페이지네이션 등 공통 로직을 재사용한다.",
            "미들웨어는 모든 요청/응답에 적용되며 CORS, 로깅, 처리 시간 측정에 활용한다.",
            "BackgroundTasks는 응답 후 이메일 발송 등 시간이 걸리는 작업을 비차단 처리한다.",
            "HTTPException과 커스텀 예외 핸들러로 일관된 에러 응답 형식을 제공할 수 있다.",
        ],
    }
