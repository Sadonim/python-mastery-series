"""
부록 A: HTTP 상태 코드 & REST API 치트시트
웹 개발과 API 설계에 필요한 핵심 지식을 한눈에 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 A: HTTP 상태 코드 & REST API 치트시트",
        "sections": [
            _section_http_methods(),
            _section_status_codes(),
            _section_rest_best_practices(),
            _section_fastapi_decorators(),
            _section_headers(),
        ],
    }


def _section_http_methods() -> dict:
    return {
        "title": "A.1 HTTP 메서드",
        "content": [
            (
                "HTTP 메서드는 클라이언트가 서버에게 '어떤 작업을 할지' 알려주는 동사입니다. "
                "REST API 설계의 기초이며, 각 메서드는 명확한 의미와 역할을 가집니다."
            ),
            {
                "type": "table",
                "headers": ["메서드", "의미", "CRUD", "멱등성", "사용 예"],
                "rows": [
                    ["GET", "리소스 조회", "Read", "O (반복 호출 결과 동일)", "GET /todos — 목록 조회"],
                    ["POST", "리소스 생성", "Create", "X (호출마다 새 리소스)", "POST /todos — 할 일 생성"],
                    ["PUT", "리소스 전체 수정", "Update", "O (전체 교체)", "PUT /todos/1 — 전체 수정"],
                    ["PATCH", "리소스 부분 수정", "Update", "조건부 O", "PATCH /todos/1 — 일부 수정"],
                    ["DELETE", "리소스 삭제", "Delete", "O (이미 없으면 동일)", "DELETE /todos/1 — 삭제"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "멱등성(Idempotency): 같은 요청을 여러 번 보내도 결과가 동일한 성질. "
                    "GET, PUT, DELETE는 멱등적이고, POST는 멱등적이지 않습니다. "
                    "네트워크 오류 재시도 설계 시 멱등성을 반드시 고려하세요."
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# curl로 각 메서드 사용 예시\n"
                    "\n"
                    "# GET — 할 일 목록 조회\n"
                    "curl http://localhost:8000/todos/\n"
                    "\n"
                    "# POST — 할 일 생성\n"
                    "curl -X POST http://localhost:8000/todos/ \\\n"
                    "     -H 'Content-Type: application/json' \\\n"
                    "     -d '{\"title\": \"공부하기\", \"description\": \"Python 복습\"}'\n"
                    "\n"
                    "# PUT — 전체 수정\n"
                    "curl -X PUT http://localhost:8000/todos/1 \\\n"
                    "     -H 'Content-Type: application/json' \\\n"
                    "     -d '{\"title\": \"공부하기\", \"is_done\": true}'\n"
                    "\n"
                    "# PATCH — 부분 수정 (is_done만)\n"
                    "curl -X PATCH http://localhost:8000/todos/1 \\\n"
                    "     -H 'Content-Type: application/json' \\\n"
                    "     -d '{\"is_done\": true}'\n"
                    "\n"
                    "# DELETE — 삭제\n"
                    "curl -X DELETE http://localhost:8000/todos/1\n"
                ),
            },
        ],
    }


def _section_status_codes() -> dict:
    return {
        "title": "A.2 HTTP 상태 코드",
        "content": [
            (
                "HTTP 상태 코드는 서버가 클라이언트에게 '요청 처리 결과'를 알려주는 3자리 숫자입니다. "
                "API 응답에서 올바른 상태 코드를 사용하면 클라이언트가 결과를 명확히 이해할 수 있습니다."
            ),
            {
                "type": "table",
                "headers": ["분류", "범위", "의미", "주요 코드"],
                "rows": [
                    ["1xx", "100-199", "정보 — 요청 처리 중", "100 Continue"],
                    ["2xx", "200-299", "성공 — 요청 정상 처리", "200 OK, 201 Created, 204 No Content"],
                    ["3xx", "300-399", "리다이렉션 — 다른 URL로 이동", "301 Moved Permanently, 302 Found"],
                    ["4xx", "400-499", "클라이언트 오류 — 잘못된 요청", "400 Bad Request, 401, 403, 404, 422"],
                    ["5xx", "500-599", "서버 오류 — 서버 내부 문제", "500 Internal Server Error, 503"],
                ],
            },
            {
                "type": "table",
                "headers": ["상태 코드", "이름", "언제 사용하나"],
                "rows": [
                    ["200 OK", "성공", "GET, PUT, PATCH 성공 시"],
                    ["201 Created", "생성됨", "POST로 리소스 생성 성공 시"],
                    ["204 No Content", "내용 없음", "DELETE 성공 또는 응답 바디가 필요 없을 때"],
                    ["400 Bad Request", "잘못된 요청", "필수 파라미터 누락, 잘못된 형식"],
                    ["401 Unauthorized", "인증 필요", "로그인/토큰 없이 접근 시"],
                    ["403 Forbidden", "접근 금지", "권한 없는 리소스 접근 시"],
                    ["404 Not Found", "찾을 수 없음", "존재하지 않는 리소스 요청 시"],
                    ["409 Conflict", "충돌", "중복 데이터 생성 시도 (이메일 중복 등)"],
                    ["422 Unprocessable Entity", "처리 불가", "FastAPI Pydantic 검증 실패 시"],
                    ["429 Too Many Requests", "요청 초과", "Rate Limit 초과 시"],
                    ["500 Internal Server Error", "서버 오류", "예상치 못한 서버 내부 오류"],
                    ["503 Service Unavailable", "서비스 불가", "서버 과부하 또는 점검 중"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# FastAPI에서 상태 코드 사용 예시\n"
                    "from fastapi import FastAPI, HTTPException, status\n"
                    "\n"
                    "app = FastAPI()\n"
                    "\n"
                    "\n"
                    "# 201 Created — 리소스 생성 성공\n"
                    "@app.post('/items/', status_code=status.HTTP_201_CREATED)\n"
                    "def create_item(name: str):\n"
                    "    return {'id': 1, 'name': name}\n"
                    "\n"
                    "\n"
                    "# 404 Not Found — 리소스 없음\n"
                    "@app.get('/items/{item_id}')\n"
                    "def get_item(item_id: int):\n"
                    "    if item_id > 100:\n"
                    "        raise HTTPException(\n"
                    "            status_code=status.HTTP_404_NOT_FOUND,\n"
                    "            detail='아이템을 찾을 수 없습니다.',\n"
                    "        )\n"
                    "    return {'id': item_id}\n"
                    "\n"
                    "\n"
                    "# 204 No Content — 삭제 성공 (응답 바디 없음)\n"
                    "@app.delete('/items/{item_id}',\n"
                    "            status_code=status.HTTP_204_NO_CONTENT)\n"
                    "def delete_item(item_id: int):\n"
                    "    return None  # 응답 바디 없음\n"
                ),
            },
        ],
    }


def _section_rest_best_practices() -> dict:
    return {
        "title": "A.3 REST API 설계 Best Practices",
        "content": [
            (
                "좋은 REST API는 URL 구조, 메서드 선택, 응답 형식이 직관적입니다. "
                "팀 내 일관성을 위해 아래 규칙을 따르면 유지보수가 쉬워집니다."
            ),
            {
                "type": "table",
                "headers": ["규칙", "나쁜 예", "좋은 예"],
                "rows": [
                    ["URL에 동사 사용 금지 (명사 사용)", "/getTodos, /createTodo", "/todos"],
                    ["복수형 명사 사용", "/todo, /user", "/todos, /users"],
                    ["계층 관계는 중첩 URL로", "/getCommentsByTodo?id=1", "/todos/1/comments"],
                    ["소문자 + 하이픈 사용", "/TodoItems, /todo_items", "/todo-items"],
                    ["버전 명시", "/todos, /v2/todos (혼재)", "/v1/todos, /v2/todos"],
                    ["필터링은 쿼리 파라미터로", "/done-todos", "/todos?is_done=true"],
                    ["페이지네이션 표준화", "page=1&count=20 (비일관)", "?skip=0&limit=20 또는 ?page=1&per_page=20"],
                ],
            },
            {
                "type": "table",
                "headers": ["리소스", "목록 조회", "단건 조회", "생성", "수정", "삭제"],
                "rows": [
                    ["todos", "GET /todos", "GET /todos/1", "POST /todos", "PUT /todos/1", "DELETE /todos/1"],
                    ["users", "GET /users", "GET /users/1", "POST /users", "PUT /users/1", "DELETE /users/1"],
                    ["중첩: 댓글", "GET /todos/1/comments", "GET /todos/1/comments/5", "POST /todos/1/comments", "PUT /todos/1/comments/5", "DELETE /todos/1/comments/5"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 일관된 API 응답 봉투(Envelope) 패턴 예시\n"
                    "from pydantic import BaseModel\n"
                    "from typing import TypeVar, Generic\n"
                    "\n"
                    "T = TypeVar('T')\n"
                    "\n"
                    "\n"
                    "class ApiResponse(BaseModel, Generic[T]):\n"
                    '    """표준 API 응답 봉투"""\n'
                    "    success: bool\n"
                    "    data: T | None = None\n"
                    "    message: str | None = None\n"
                    "\n"
                    "\n"
                    "# 성공 응답\n"
                    "# {\"success\": true, \"data\": {\"id\": 1, \"title\": \"공부\"}, \"message\": null}\n"
                    "\n"
                    "# 에러 응답\n"
                    "# {\"success\": false, \"data\": null, \"message\": \"할 일을 찾을 수 없습니다.\"}\n"
                ),
            },
            {
                "type": "note",
                "text": (
                    "FastAPI는 응답 봉투 없이도 status_code와 HTTPException으로 "
                    "충분한 정보를 전달할 수 있습니다. "
                    "작은 프로젝트는 봉투 패턴 없이 심플하게, "
                    "대규모 프로젝트는 봉투 패턴으로 일관성을 확보하세요."
                ),
            },
        ],
    }


def _section_fastapi_decorators() -> dict:
    return {
        "title": "A.4 FastAPI 데코레이터 & 핵심 기능 요약",
        "content": [
            "FastAPI의 주요 데코레이터와 파라미터 타입을 한눈에 정리합니다.",
            {
                "type": "table",
                "headers": ["데코레이터 / 함수", "설명", "예시"],
                "rows": [
                    ["@app.get(path)", "GET 엔드포인트 등록", "@app.get('/todos/')"],
                    ["@app.post(path)", "POST 엔드포인트 등록", "@app.post('/todos/', status_code=201)"],
                    ["@app.put(path)", "PUT 엔드포인트 등록", "@app.put('/todos/{id}')"],
                    ["@app.delete(path)", "DELETE 엔드포인트 등록", "@app.delete('/todos/{id}')"],
                    ["@app.on_event('startup')", "앱 시작 이벤트 핸들러", "DB 연결, 초기화 작업"],
                    ["Depends(func)", "의존성 주입 — DB 세션, 인증 등", "db: Session = Depends(get_db)"],
                    ["Path(...)", "경로 파라미터 검증", "Path(gt=0, description='할 일 ID')"],
                    ["Query(...)", "쿼리 파라미터 검증", "Query(default=0, ge=0)"],
                    ["Body(...)", "요청 바디 검증", "Body(embed=True)"],
                    ["HTTPException", "HTTP 오류 발생", "raise HTTPException(status_code=404)"],
                    ["BackgroundTasks", "비동기 백그라운드 작업", "이메일 전송, 로그 기록"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# FastAPI 주요 파라미터 타입 활용 예시\n"
                    "from fastapi import FastAPI, Depends, Path, Query, HTTPException\n"
                    "from fastapi import BackgroundTasks\n"
                    "\n"
                    "app = FastAPI()\n"
                    "\n"
                    "\n"
                    "@app.get('/todos/{todo_id}')\n"
                    "def get_todo(\n"
                    "    # 경로 파라미터: 1 이상의 정수만 허용\n"
                    "    todo_id: int = Path(..., ge=1, description='할 일 ID'),\n"
                    "):\n"
                    "    return {'id': todo_id}\n"
                    "\n"
                    "\n"
                    "@app.get('/todos/')\n"
                    "def list_todos(\n"
                    "    # 쿼리 파라미터: 기본값 0, 0 이상만 허용\n"
                    "    skip: int = Query(default=0, ge=0),\n"
                    "    limit: int = Query(default=20, ge=1, le=100),\n"
                    "    is_done: bool | None = Query(default=None),\n"
                    "):\n"
                    "    return {'skip': skip, 'limit': limit, 'is_done': is_done}\n"
                    "\n"
                    "\n"
                    "@app.post('/todos/')\n"
                    "def create_todo_with_bg(\n"
                    "    title: str,\n"
                    "    background_tasks: BackgroundTasks,\n"
                    "):\n"
                    "    # 응답 반환 후 백그라운드에서 이메일 발송\n"
                    "    background_tasks.add_task(send_notification, title)\n"
                    "    return {'title': title, 'message': '생성 완료'}\n"
                ),
            },
        ],
    }


def _section_headers() -> dict:
    return {
        "title": "A.5 요청/응답 헤더 주요 항목",
        "content": [
            (
                "HTTP 헤더는 요청과 응답에 메타데이터를 포함시키는 방법입니다. "
                "인증, 콘텐츠 타입, 캐시 제어 등 API 동작에 직접 영향을 미칩니다."
            ),
            {
                "type": "table",
                "headers": ["헤더", "방향", "설명", "예시 값"],
                "rows": [
                    ["Content-Type", "요청/응답", "바디 데이터 형식", "application/json"],
                    ["Authorization", "요청", "인증 토큰", "Bearer eyJhbGci..."],
                    ["Accept", "요청", "클라이언트가 원하는 응답 형식", "application/json"],
                    ["X-Request-ID", "요청", "요청 추적 ID (로그 연동)", "550e8400-e29b-41d4"],
                    ["Cache-Control", "응답", "캐시 정책", "no-cache, max-age=3600"],
                    ["X-RateLimit-Limit", "응답", "분당 최대 요청 수", "1000"],
                    ["X-RateLimit-Remaining", "응답", "남은 요청 수", "999"],
                    ["Location", "응답", "생성된 리소스 URL (201 응답 시)", "/todos/42"],
                    ["ETag", "응답", "리소스 버전 식별자 (캐시 검증)", "abc123def"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# FastAPI에서 커스텀 헤더 추가 & 읽기\n"
                    "from fastapi import FastAPI, Header, Response\n"
                    "from fastapi.responses import JSONResponse\n"
                    "\n"
                    "app = FastAPI()\n"
                    "\n"
                    "\n"
                    "# 요청 헤더 읽기\n"
                    "@app.get('/todos/')\n"
                    "def list_todos(\n"
                    "    x_request_id: str | None = Header(default=None),\n"
                    "):\n"
                    "    return {'request_id': x_request_id}\n"
                    "\n"
                    "\n"
                    "# 응답 헤더 추가\n"
                    "@app.post('/todos/', status_code=201)\n"
                    "def create_todo(title: str, response: Response):\n"
                    "    todo_id = 42  # DB 저장 후 받은 ID\n"
                    "    # 생성된 리소스 URL을 Location 헤더에 추가\n"
                    "    response.headers['Location'] = f'/todos/{todo_id}'\n"
                    "    return {'id': todo_id, 'title': title}\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "Authorization 헤더의 'Bearer' 토큰은 JWT(JSON Web Token)를 주로 사용합니다. "
                    "FastAPI에서는 python-jose 또는 PyJWT 라이브러리로 JWT를 생성/검증하고, "
                    "Depends()로 모든 보호 엔드포인트에 인증을 적용합니다."
                ),
            },
        ],
    }
