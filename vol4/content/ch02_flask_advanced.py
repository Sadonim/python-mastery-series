"""
Ch 2: Flask 심화 — REST API 구축
Python Mastery Series Vol.4 — 웹 & 배포
"""


def get_chapter():
    return {
        "number": 2,
        "title": "Flask 심화 — REST API 구축",
        "subtitle": "CRUD, Blueprint 모듈화, 유효성 검사, CORS",
        "big_picture": (
            "RESTful API는 현대 웹 서비스의 표준 통신 방식입니다. "
            "프론트엔드, 모바일 앱, 다른 서비스가 모두 API를 통해 데이터를 주고받습니다. "
            "이 챕터에서는 REST 설계 원칙에 따라 완전한 CRUD API를 만들고, "
            "Blueprint로 모듈화하며, 요청 유효성 검사와 CORS 처리까지 실무 수준의 Flask API를 구축합니다."
        ),
        "sections": [
            {
                "title": "RESTful API 설계 원칙",
                "content": [
                    "REST(Representational State Transfer)는 API 설계의 아키텍처 스타일입니다. "
                    "'RESTful'하다는 것은 REST 원칙을 따라 URL과 HTTP 메서드를 "
                    "일관성 있게 설계했다는 의미입니다.",
                    {
                        "type": "heading",
                        "text": "REST 핵심 원칙",
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "리소스(Resource) 중심 설계: URL은 동사가 아닌 명사로 표현 (/getUsers 금지, /users 권장)",
                            "HTTP 메서드로 행위 표현: GET=조회, POST=생성, PUT=전체 수정, PATCH=부분 수정, DELETE=삭제",
                            "무상태(Stateless): 각 요청은 독립적이며 서버는 이전 요청 상태를 기억하지 않음",
                            "적절한 HTTP 상태 코드 사용: 성공은 200/201, 클라이언트 오류는 4xx, 서버 오류는 5xx",
                            "일관된 응답 형식: 모든 응답은 동일한 envelope 구조 사용",
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "REST API CRUD 매핑",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "GET /users", "sub": "전체 목록 조회"},
                            {"label": "POST /users", "sub": "새 사용자 생성"},
                            {"label": "GET /users/1", "sub": "특정 사용자 조회"},
                            {"label": "PATCH /users/1", "sub": "부분 수정"},
                            {"label": "DELETE /users/1", "sub": "삭제"},
                        ],
                        "note": "URL 명사 복수형 사용, HTTP 메서드로 동작 구분",
                    },
                    {
                        "type": "table",
                        "headers": ["REST 패턴", "HTTP 메서드", "URL 예시", "응답 코드"],
                        "rows": [
                            ["목록 조회", "GET", "/api/users", "200 OK"],
                            ["단건 조회", "GET", "/api/users/1", "200 OK / 404"],
                            ["생성", "POST", "/api/users", "201 Created"],
                            ["전체 수정", "PUT", "/api/users/1", "200 OK / 404"],
                            ["부분 수정", "PATCH", "/api/users/1", "200 OK / 404"],
                            ["삭제", "DELETE", "/api/users/1", "204 No Content / 404"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "REST URL 설계 규칙",
                    },
                    {
                        "type": "table",
                        "headers": ["나쁜 예 (동사 URL)", "좋은 예 (명사 + 메서드)"],
                        "rows": [
                            ["GET /getUsers", "GET /users"],
                            ["POST /createUser", "POST /users"],
                            ["GET /deleteUser?id=1", "DELETE /users/1"],
                            ["POST /updateUserProfile", "PATCH /users/1/profile"],
                            ["GET /getUserPosts?userId=1", "GET /users/1/posts"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "URL에서 동사를 사용하는 유일한 예외는 '행위(action)' 엔드포인트입니다. "
                            "예: POST /users/1/activate (사용자 활성화), "
                            "POST /orders/1/cancel (주문 취소). "
                            "상태 변경을 리소스 업데이트(PATCH)로 표현하기 어려울 때만 허용합니다."
                        ),
                    },
                ],
            },
            {
                "title": "완전한 CRUD REST API 구현",
                "content": [
                    "게시글(Post) 리소스를 기준으로 완전한 CRUD API를 구현합니다. "
                    "메모리 딕셔너리를 저장소로 사용하며, Ch5에서 DB로 교체합니다.",
                    {
                        "type": "heading",
                        "text": "데이터 저장소와 일관된 응답 형식",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# posts_api.py\n"
                            "from flask import Flask, jsonify, request\n"
                            "from datetime import datetime\n"
                            "\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# 메모리 저장소 (불변 패턴: 딕셔너리 복사본으로 관리)\n"
                            "_store = {\n"
                            "    'posts': {\n"
                            "        1: {'id': 1, '제목': 'Flask 입문', '내용': '첫 번째 글',\n"
                            "            '작성자': '김철수', 'created_at': '2024-01-01'},\n"
                            "        2: {'id': 2, '제목': 'REST API', '내용': '두 번째 글',\n"
                            "            '작성자': '이영희', 'created_at': '2024-01-02'},\n"
                            "    },\n"
                            "    'next_id': 3,\n"
                            "}\n"
                            "\n"
                            "# ─── 일관된 응답 형식 헬퍼 ───\n"
                            "def success_response(data, status=200):\n"
                            "    \"\"\"성공 응답 Envelope\"\"\"\n"
                            "    return jsonify({'success': True, 'data': data}), status\n"
                            "\n"
                            "def error_response(message, status=400):\n"
                            "    \"\"\"에러 응답 Envelope\"\"\"\n"
                            "    return jsonify({'success': False, 'error': message}), status"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "CRUD 엔드포인트 구현",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ─── 목록 조회 (GET /api/posts) ───\n"
                            "@app.get('/api/posts')\n"
                            "def list_posts():\n"
                            "    posts = list(_store['posts'].values())\n"
                            "    # 쿼리 파라미터: ?author=김철수\n"
                            "    author = request.args.get('author')\n"
                            "    if author:\n"
                            "        posts = [p for p in posts if p['작성자'] == author]\n"
                            "    return success_response({'posts': posts, 'total': len(posts)})\n"
                            "\n"
                            "# ─── 단건 조회 (GET /api/posts/1) ───\n"
                            "@app.get('/api/posts/[int:post_id]')\n"
                            "def get_post(post_id):\n"
                            "    post = _store['posts'].get(post_id)\n"
                            "    if post is None:\n"
                            "        return error_response('게시글을 찾을 수 없습니다', 404)\n"
                            "    return success_response(post)\n"
                            "\n"
                            "# ─── 생성 (POST /api/posts) ───\n"
                            "@app.post('/api/posts')\n"
                            "def create_post():\n"
                            "    data = request.get_json()\n"
                            "    if not data:\n"
                            "        return error_response('JSON 바디가 필요합니다')\n"
                            "    required = ['제목', '내용', '작성자']\n"
                            "    missing = [f for f in required if not data.get(f)]\n"
                            "    if missing:\n"
                            "        return error_response(f'필수 필드 누락: {\", \".join(missing)}')\n"
                            "    new_id = _store['next_id']\n"
                            "    new_post = {\n"
                            "        'id': new_id,\n"
                            "        '제목': data['제목'],\n"
                            "        '내용': data['내용'],\n"
                            "        '작성자': data['작성자'],\n"
                            "        'created_at': datetime.now().isoformat(),\n"
                            "    }\n"
                            "    # 불변 패턴: 기존 딕셔너리를 복사한 새 딕셔너리 할당\n"
                            "    updated_posts = {**_store['posts'], new_id: new_post}\n"
                            "    _store.update({'posts': updated_posts, 'next_id': new_id + 1})\n"
                            "    return success_response(new_post, 201)\n"
                            "\n"
                            "# ─── 부분 수정 (PATCH /api/posts/1) ───\n"
                            "@app.patch('/api/posts/[int:post_id]')\n"
                            "def update_post(post_id):\n"
                            "    post = _store['posts'].get(post_id)\n"
                            "    if post is None:\n"
                            "        return error_response('게시글을 찾을 수 없습니다', 404)\n"
                            "    data = request.get_json() or {}\n"
                            "    allowed = {'제목', '내용'}  # 수정 가능한 필드만 허용\n"
                            "    updates = {k: v for k, v in data.items() if k in allowed}\n"
                            "    updated_post = {**post, **updates}  # 불변 패턴\n"
                            "    _store['posts'] = {**_store['posts'], post_id: updated_post}\n"
                            "    return success_response(updated_post)\n"
                            "\n"
                            "# ─── 삭제 (DELETE /api/posts/1) ───\n"
                            "@app.delete('/api/posts/[int:post_id]')\n"
                            "def delete_post(post_id):\n"
                            "    if post_id not in _store['posts']:\n"
                            "        return error_response('게시글을 찾을 수 없습니다', 404)\n"
                            "    new_posts = {k: v for k, v in _store['posts'].items()\n"
                            "                 if k != post_id}\n"
                            "    _store['posts'] = new_posts\n"
                            "    return '', 204  # 삭제 성공: 빈 바디 + 204"
                        ),
                    },
                ],
            },
            {
                "title": "Blueprint — 대규모 앱 모듈화",
                "content": [
                    "앱이 커지면 모든 라우트를 app.py 하나에 두면 관리가 불가능해집니다. "
                    "Flask의 Blueprint는 라우트를 기능/도메인별로 분리하는 공식 모듈화 방법입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "Blueprint는 군대의 '소대' 개념과 같습니다. "
                            "중대(Flask 앱) 전체 지휘는 app.py(중대장)가 하지만, "
                            "각 소대(Blueprint)는 자기 임무를 독립적으로 처리합니다. "
                            "users 소대는 사용자 관련 라우트, posts 소대는 게시글 관련 라우트를 담당하며, "
                            "중대에 편입될 때 URL 접두사(/api/users, /api/posts)를 받습니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "Blueprint 생성 및 등록",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# app/routes/users.py — 사용자 Blueprint\n"
                            "from flask import Blueprint, jsonify, request\n"
                            "\n"
                            "# Blueprint 생성: 이름, 모듈 이름\n"
                            "users_bp = Blueprint('users', __name__)\n"
                            "\n"
                            "_users = {1: {'id': 1, '이름': '김철수', '이메일': 'kim@example.com'}}\n"
                            "_next_id = 2\n"
                            "\n"
                            "# Blueprint에 라우트 등록 (app.route 대신 users_bp.route)\n"
                            "@users_bp.get('/')           # /api/users/\n"
                            "def list_users():\n"
                            "    return jsonify(list(_users.values()))\n"
                            "\n"
                            "@users_bp.get('/[int:uid]')  # /api/users/1\n"
                            "def get_user(uid):\n"
                            "    user = _users.get(uid)\n"
                            "    if not user:\n"
                            "        return jsonify({'error': '사용자 없음'}), 404\n"
                            "    return jsonify(user)\n"
                            "\n"
                            "@users_bp.post('/')          # /api/users/\n"
                            "def create_user():\n"
                            "    global _next_id\n"
                            "    data = request.get_json() or {}\n"
                            "    if not data.get('이름'):\n"
                            "        return jsonify({'error': '이름은 필수입니다'}), 400\n"
                            "    new_user = {'id': _next_id, **data}\n"
                            "    _next_id += 1\n"
                            "    return jsonify(new_user), 201"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# app/__init__.py — Flask 앱 팩토리\n"
                            "from flask import Flask\n"
                            "from app.routes.users import users_bp\n"
                            "from app.routes.posts import posts_bp  # 다른 Blueprint\n"
                            "\n"
                            "def create_app(config=None):\n"
                            "    \"\"\"앱 팩토리 패턴 — 테스트 환경에서 다른 설정으로 생성 가능\"\"\"\n"
                            "    app = Flask(__name__)\n"
                            "\n"
                            "    if config:\n"
                            "        app.config.update(config)\n"
                            "\n"
                            "    # Blueprint 등록: url_prefix로 URL 접두사 설정\n"
                            "    app.register_blueprint(users_bp, url_prefix='/api/users')\n"
                            "    app.register_blueprint(posts_bp, url_prefix='/api/posts')\n"
                            "    # users_bp의 '/' → /api/users/\n"
                            "    # users_bp의 '/[int:uid]' → /api/users/1\n"
                            "\n"
                            "    return app\n"
                            "\n"
                            "# run.py — 진입점\n"
                            "# from app import create_app\n"
                            "# app = create_app()\n"
                            "# if __name__ == '__main__':\n"
                            "#     app.run(debug=True)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "앱 팩토리 패턴(create_app 함수)은 테스트에서 매우 중요합니다. "
                            "pytest에서 테스트용 설정(SQLite 임시 DB 등)을 주입해 앱을 생성할 수 있습니다. "
                            "모든 Flask 프로젝트는 처음부터 앱 팩토리 패턴으로 시작하세요."
                        ),
                    },
                ],
            },
            {
                "title": "요청 유효성 검사",
                "content": [
                    "외부에서 들어오는 모든 요청 데이터는 신뢰할 수 없습니다. "
                    "유효성 검사(Validation)는 잘못된 데이터가 시스템 안으로 들어오기 전에 차단합니다. "
                    "'쓰레기가 들어오면 쓰레기가 나온다'(GIGO)는 원칙을 기억하세요.",
                    {
                        "type": "heading",
                        "text": "직접 구현 — 검사 함수 분리",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# validators.py — 유효성 검사 함수 모음\n"
                            "import re\n"
                            "from typing import Any\n"
                            "\n"
                            "def validate_user(data: dict) -> list[str]:\n"
                            "    \"\"\"사용자 생성 요청 유효성 검사. 오류 메시지 리스트 반환.\"\"\"\n"
                            "    errors = []\n"
                            "\n"
                            "    # 이름 검사\n"
                            "    name = data.get('이름', '')\n"
                            "    if not name:\n"
                            "        errors.append('이름은 필수입니다')\n"
                            "    elif len(name) > 50:\n"
                            "        errors.append('이름은 50자 이하여야 합니다')\n"
                            "\n"
                            "    # 이메일 검사\n"
                            "    email = data.get('이메일', '')\n"
                            "    email_pattern = r'^[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,}$'\n"
                            "    if not email:\n"
                            "        errors.append('이메일은 필수입니다')\n"
                            "    elif not re.match(email_pattern, email):\n"
                            "        errors.append('올바른 이메일 형식이 아닙니다')\n"
                            "\n"
                            "    # 나이 검사 (선택 필드)\n"
                            "    age = data.get('나이')\n"
                            "    if age is not None:\n"
                            "        if not isinstance(age, int) or age < 1 or age > 150:\n"
                            "            errors.append('나이는 1 이상 150 이하의 정수여야 합니다')\n"
                            "\n"
                            "    return errors\n"
                            "\n"
                            "# 라우트에서 사용\n"
                            "# @app.post('/api/users')\n"
                            "# def create_user():\n"
                            "#     data = request.get_json() or {}\n"
                            "#     errors = validate_user(data)\n"
                            "#     if errors:\n"
                            "#         return jsonify({'success': False,\n"
                            "#                          'errors': errors}), 400\n"
                            "#     # 유효성 통과 후 처리..."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "marshmallow 라이브러리로 스키마 기반 검사",
                    },
                    "marshmallow는 Python의 강력한 직렬화/역직렬화 + 유효성 검사 라이브러리입니다. "
                    "스키마를 한 번 정의하면 검사, 변환, 직렬화가 자동으로 됩니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": "pip install marshmallow",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# schemas.py\n"
                            "from marshmallow import Schema, fields, validate, ValidationError\n"
                            "\n"
                            "class UserCreateSchema(Schema):\n"
                            "    이름 = fields.Str(\n"
                            "        required=True,\n"
                            "        validate=validate.Length(min=1, max=50, error='이름은 1~50자여야 합니다'),\n"
                            "    )\n"
                            "    이메일 = fields.Email(required=True, error_messages={'invalid': '이메일 형식 오류'})\n"
                            "    나이 = fields.Int(\n"
                            "        load_default=None,\n"
                            "        validate=validate.Range(min=1, max=150),\n"
                            "    )\n"
                            "\n"
                            "# 라우트에서 사용\n"
                            "from flask import Flask, jsonify, request\n"
                            "app = Flask(__name__)\n"
                            "user_schema = UserCreateSchema()\n"
                            "\n"
                            "@app.post('/api/users')\n"
                            "def create_user():\n"
                            "    raw_data = request.get_json() or {}\n"
                            "    try:\n"
                            "        validated = user_schema.load(raw_data)  # 검사 + 변환\n"
                            "    except ValidationError as e:\n"
                            "        return jsonify({'success': False, 'errors': e.messages}), 400\n"
                            "    # validated는 검증된 딕셔너리\n"
                            "    return jsonify({'success': True, 'data': validated}), 201"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "절대로 유효성 검사를 생략하지 마세요. "
                            "SQL 인젝션, XSS, 버퍼 오버플로우 등 대부분의 보안 공격은 "
                            "입력 유효성 검사 부재에서 시작됩니다. "
                            "특히 숫자 범위, 문자열 길이, 이메일 형식은 반드시 검사하세요."
                        ),
                    },
                ],
            },
            {
                "title": "CORS 처리 — 브라우저 보안 정책 대응",
                "content": [
                    "CORS(Cross-Origin Resource Sharing)는 브라우저가 "
                    "다른 출처(도메인, 포트)의 API에 접근할 때 적용하는 보안 정책입니다. "
                    "프론트엔드(React, Vue 등)에서 Flask API를 호출하면 반드시 맞닥뜨리는 문제입니다.",
                    {
                        "type": "heading",
                        "text": "CORS가 필요한 상황",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# CORS 오류가 발생하는 상황:\n"
                            "# 프론트엔드: http://localhost:3000 (React 개발 서버)\n"
                            "# 백엔드 API: http://localhost:5000 (Flask)\n"
                            "#\n"
                            "# 브라우저 콘솔 오류:\n"
                            "# Access to fetch at 'http://localhost:5000/api/users'\n"
                            "# from origin 'http://localhost:3000' has been blocked by CORS policy.\n"
                            "#\n"
                            "# 해결: Flask 응답 헤더에 Access-Control-Allow-Origin 추가 필요"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "flask-cors 라이브러리 사용",
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": "pip install flask-cors",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask\n"
                            "from flask_cors import CORS\n"
                            "\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# ─── 방법 1: 모든 출처 허용 (개발 환경 전용) ───\n"
                            "CORS(app)\n"
                            "\n"
                            "# ─── 방법 2: 특정 출처만 허용 (운영 환경 권장) ───\n"
                            "# CORS(app, origins=['https://myapp.com', 'https://www.myapp.com'])\n"
                            "\n"
                            "# ─── 방법 3: Blueprint별 세밀한 CORS 설정 ───\n"
                            "# from app.routes.users import users_bp\n"
                            "# app.register_blueprint(users_bp, url_prefix='/api/users')\n"
                            "# CORS(users_bp, origins=['https://myapp.com'])\n"
                            "\n"
                            "# ─── 방법 4: 직접 헤더 추가 (flask-cors 없이) ───\n"
                            "@app.after_request\n"
                            "def add_cors_headers(response):\n"
                            "    import os\n"
                            "    allowed_origin = os.environ.get('ALLOWED_ORIGIN', '*')\n"
                            "    response.headers['Access-Control-Allow-Origin'] = allowed_origin\n"
                            "    response.headers['Access-Control-Allow-Methods'] = \\\n"
                            "        'GET, POST, PUT, PATCH, DELETE, OPTIONS'\n"
                            "    response.headers['Access-Control-Allow-Headers'] = \\\n"
                            "        'Content-Type, Authorization'\n"
                            "    return response\n"
                            "\n"
                            "@app.route('/api/test')\n"
                            "def test():\n"
                            "    return {'message': 'CORS 설정 완료'}"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "운영 환경에서 origins='*' (모든 출처 허용)는 보안 위험입니다. "
                            "허용할 출처를 명시적으로 지정하세요. "
                            "특히 인증이 필요한 API에서 '*'를 사용하면 "
                            "CSRF(Cross-Site Request Forgery) 공격에 취약해집니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "환경별 CORS 설정",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# config.py — 환경별 설정 분리\n"
                            "import os\n"
                            "\n"
                            "class DevelopmentConfig:\n"
                            "    DEBUG = True\n"
                            "    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:5173']\n"
                            "\n"
                            "class ProductionConfig:\n"
                            "    DEBUG = False\n"
                            "    CORS_ORIGINS = ['https://myapp.com', 'https://www.myapp.com']\n"
                            "\n"
                            "# 환경변수로 설정 선택\n"
                            "CONFIG_MAP = {\n"
                            "    'development': DevelopmentConfig,\n"
                            "    'production': ProductionConfig,\n"
                            "}\n"
                            "\n"
                            "# app/__init__.py\n"
                            "from flask import Flask\n"
                            "from flask_cors import CORS\n"
                            "\n"
                            "def create_app():\n"
                            "    app = Flask(__name__)\n"
                            "    env = os.environ.get('FLASK_ENV', 'development')\n"
                            "    cfg = CONFIG_MAP.get(env, DevelopmentConfig)\n"
                            "    app.config.from_object(cfg)\n"
                            "    CORS(app, origins=cfg.CORS_ORIGINS)\n"
                            "    return app"
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "REST API URL은 항상 소문자 복수 명사로 작성하세요 (/users, /posts, /products). "
            "동사(/getUser), 단수(/user), 대문자(/Users)는 일관성을 깨뜨립니다.",
            "응답 형식은 성공/실패 모두 동일한 Envelope 구조를 유지하세요. "
            "{\"success\": true, \"data\": ...} 또는 {\"success\": false, \"error\": ...} 형태로 통일하면 "
            "프론트엔드 팀이 일관되게 처리할 수 있습니다.",
            "Blueprint를 사용하면 기능별로 파일이 분리되어 팀 협업이 쉬워집니다. "
            "users.py, posts.py, auth.py처럼 도메인 단위로 분리하세요.",
            "CORS는 개발 환경에서는 와일드카드(*)를 허용하되, "
            "운영 배포 전에 반드시 허용할 도메인을 명시적으로 제한하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "RESTful API 설계에서 상품 목록을 조회하는 올바른 엔드포인트 설계는?",
                "choices": [
                    "GET /getProductList",
                    "POST /product/fetch",
                    "GET /products",
                    "GET /product/all/list",
                ],
                "answer": "3번",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "새 리소스를 생성하는 POST 요청이 성공했을 때 반환해야 하는 HTTP 상태 코드는?",
                "choices": [
                    "200 OK",
                    "201 Created",
                    "204 No Content",
                    "202 Accepted",
                ],
                "answer": "2번",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "Flask Blueprint를 사용하면 얻을 수 있는 이점 두 가지를 설명하세요."
                ),
                "answer": (
                    "① 기능별 파일 분리로 코드 가독성 향상 및 팀 협업 용이 | "
                    "② url_prefix로 URL 접두사를 일괄 관리하여 경로 충돌 방지"
                ),
            },
            {
                "number": 4,
                "type": "code",
                "question": (
                    "아래 Flask 라우트에 유효성 검사를 추가하세요.\n"
                    "입력: {\"title\": \"...\", \"score\": N}\n"
                    "검사 조건: title은 1~100자 문자열, score는 0~100 사이 정수\n"
                    "실패 시: 400과 함께 {\"errors\": [...]} 반환"
                ),
                "hint": "data.get()으로 값을 읽고, isinstance()와 범위 조건으로 errors 리스트를 채운 뒤, errors가 비어 있지 않으면 400 반환하세요.",
                "answer": (
                    "@app.post('/api/reviews')\n"
                    "def create_review():\n"
                    "    data = request.get_json() or {}\n"
                    "    errors = []\n"
                    "    title = data.get('title', '')\n"
                    "    if not isinstance(title, str) or not (1 <= len(title) <= 100):\n"
                    "        errors.append('title은 1~100자 문자열이어야 합니다')\n"
                    "    score = data.get('score')\n"
                    "    if not isinstance(score, int) or not (0 <= score <= 100):\n"
                    "        errors.append('score는 0~100 사이의 정수여야 합니다')\n"
                    "    if errors:\n"
                    "        return jsonify({'errors': errors}), 400\n"
                    "    return jsonify({'success': True, 'data': data}), 201"
                ),
            },
            {
                "number": 5,
                "type": "multiple_choice",
                "question": "CORS(Cross-Origin Resource Sharing) 오류가 발생하는 상황으로 올바른 것은?",
                "choices": [
                    "서버와 클라이언트가 동일한 도메인과 포트를 사용하는 경우",
                    "브라우저에서 다른 출처(도메인 또는 포트)의 API를 호출하는 경우",
                    "curl 또는 Postman으로 API를 직접 호출하는 경우",
                    "API 응답이 JSON이 아닌 HTML인 경우",
                ],
                "answer": "2번",
            },
        ],
        "challenge": {
            "question": (
                "도서 관리 REST API를 Blueprint를 사용해 구현하세요.\n\n"
                "요구사항:\n"
                "① books_bp Blueprint를 만들어 /api/books URL 접두사로 등록\n"
                "② GET /api/books — 전체 목록 (선택: ?genre=소설로 장르 필터)\n"
                "③ GET /api/books/[int:book_id] — 단건 조회 (없으면 404)\n"
                "④ POST /api/books — 생성 (title, author, genre, year 필수 검사)\n"
                "⑤ DELETE /api/books/[int:book_id] — 삭제 (없으면 404, 성공 시 204)\n"
                "⑥ 모든 응답은 {\"success\": true/false, \"data\": ...} Envelope 구조\n"
                "⑦ flask-cors로 http://localhost:3000 출처만 허용\n\n"
                "보너스: year는 1000~현재 연도 사이만 허용하는 유효성 검사 추가"
            ),
            "hint": (
                "datetime.now().year로 현재 연도를 구할 수 있습니다. "
                "Blueprint 파일(books.py), 앱 팩토리(__init__.py), 진입점(run.py) "
                "세 파일로 구조를 분리하면 깔끔합니다."
            ),
        },
        "summary": [
            "REST API는 URL에 명사, HTTP 메서드에 동사(GET/POST/PATCH/DELETE)를 사용해 설계합니다.",
            "CRUD 응답 코드: 조회 200, 생성 201, 삭제 204, 없음 404, 잘못된 입력 400.",
            "Blueprint로 라우트를 도메인별로 분리하고, 앱 팩토리(create_app)에서 url_prefix와 함께 등록합니다.",
            "모든 외부 입력은 유효성 검사 후 처리하세요. marshmallow 스키마를 사용하면 재사용 가능합니다.",
            "CORS는 브라우저 보안 정책이며, flask-cors로 허용할 출처를 운영 환경에서는 명시적으로 제한하세요.",
            "일관된 응답 Envelope(success/data/error)을 유지하면 프론트엔드 팀과의 협업이 매끄러워집니다.",
        ],
    }
