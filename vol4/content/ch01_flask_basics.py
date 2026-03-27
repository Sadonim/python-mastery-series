"""
Ch 1: Flask 웹 개발 기초
Python Mastery Series Vol.4 — 웹 & 배포
"""


def get_chapter():
    return {
        "number": 1,
        "title": "Flask 웹 개발 기초",
        "subtitle": "Python으로 웹 서버를 만드는 가장 빠른 방법",
        "big_picture": (
            "Flask는 Python 웹 프레임워크 중 가장 가볍고 직관적입니다. "
            "'마이크로 프레임워크'라는 별명답게 핵심 기능만 제공하고, "
            "필요한 기능은 확장 라이브러리로 추가합니다. "
            "이 챕터에서는 라우팅, 요청/응답 처리, Jinja2 템플릿, 정적 파일 서빙까지 "
            "Flask의 핵심 기능을 실습합니다."
        ),
        "sections": [
            {
                "title": "Flask 소개와 첫 번째 웹 앱",
                "content": [
                    "Flask는 2010년 Armin Ronacher가 만든 Python 웹 프레임워크입니다. "
                    "Django와 달리 '필요한 것만' 제공합니다. "
                    "소규모 API, 프로토타입, 내부 도구 개발에 특히 적합합니다.",
                    {
                        "type": "table",
                        "headers": ["구분", "Flask", "Django"],
                        "rows": [
                            ["철학", "마이크로 (최소한의 기능)", "배터리 포함 (모든 기능 내장)"],
                            ["학습 곡선", "낮음 (빠르게 시작)", "높음 (많은 개념 필요)"],
                            ["유연성", "높음 (자유로운 구조)", "낮음 (정해진 구조)"],
                            ["적합한 용도", "API, 소규모 앱, 프로토타입", "대형 웹 서비스, CMS"],
                            ["ORM", "별도 설치 필요", "Django ORM 내장"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "Flask 설치",
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 가상환경 활성화 후 설치\n"
                            "pip install flask\n"
                            "\n"
                            "# 설치 확인\n"
                            "python3 -c \"import flask; print('Flask', flask.__version__)\"\n"
                            "# Flask 3.0.x"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "Hello World — 최소한의 Flask 앱",
                    },
                    "Flask 앱은 단 5줄로 시작할 수 있습니다. "
                    "이 단순함이 Flask의 가장 큰 매력입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# app.py — 가장 단순한 Flask 앱\n"
                            "from flask import Flask\n"
                            "\n"
                            "# Flask 앱 인스턴스 생성\n"
                            "# __name__: 현재 모듈 이름 (정적 파일 경로 탐색에 사용)\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "@app.route('/')          # URL '/'에 대한 핸들러 등록\n"
                            "def index():\n"
                            "    return '안녕하세요! Flask 웹 앱입니다.'\n"
                            "\n"
                            "@app.route('/hello')\n"
                            "def hello():\n"
                            "    return '<h1>Hello, World!</h1>'  # HTML도 반환 가능\n"
                            "\n"
                            "if __name__ == '__main__':\n"
                            "    # debug=True: 코드 변경 시 자동 재시작 + 상세 에러 표시\n"
                            "    # 운영 환경에서는 반드시 debug=False\n"
                            "    app.run(debug=True, host='0.0.0.0', port=5000)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 앱 실행\n"
                            "python3 app.py\n"
                            "#  * Running on http://127.0.0.1:5000\n"
                            "#  * Debug mode: on\n"
                            "\n"
                            "# 또는 Flask CLI로 실행 (권장)\n"
                            "export FLASK_APP=app.py\n"
                            "export FLASK_DEBUG=1\n"
                            "flask run --port 5000\n"
                            "\n"
                            "# 브라우저에서 확인: http://localhost:5000\n"
                            "# curl로 테스트: curl http://localhost:5000"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "debug=True 모드에서는 코드를 수정하면 서버가 자동으로 재시작됩니다. "
                            "또한 오류 발생 시 브라우저에서 인터랙티브 디버거가 열립니다. "
                            "하지만 운영 환경에서는 절대 debug=True를 사용하지 마세요. "
                            "내부 코드가 외부에 노출될 수 있습니다."
                        ),
                    },
                ],
            },
            {
                "title": "라우팅 — URL과 함수 연결하기",
                "content": [
                    "라우팅(Routing)은 특정 URL 요청을 어떤 함수가 처리할지 매핑하는 것입니다. "
                    "Flask에서는 @app.route() 데코레이터로 라우팅을 설정합니다.",
                    {
                        "type": "heading",
                        "text": "기본 라우팅",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# 기본 라우팅 — 고정 경로\n"
                            "@app.route('/')\n"
                            "def home():\n"
                            "    return '홈 페이지'\n"
                            "\n"
                            "@app.route('/about')\n"
                            "def about():\n"
                            "    return '소개 페이지'\n"
                            "\n"
                            "@app.route('/contact')\n"
                            "def contact():\n"
                            "    return '연락처 페이지'"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "URL 변수 — 동적 라우팅",
                    },
                    "URL 경로의 일부를 변수로 받아 처리할 수 있습니다. "
                    "RESTful API에서 특정 리소스를 ID로 조회할 때 필수입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# URL 변수 — 문자열 타입 (기본값)\n"
                            "@app.route('/users/[username]')\n"
                            "def user_profile(username):\n"
                            "    # /users/김철수 → username = '김철수'\n"
                            "    return f'{username}님의 프로필입니다.'\n"
                            "\n"
                            "# URL 변수 — 정수 타입 (자동 변환 + 검증)\n"
                            "@app.route('/posts/[int:post_id]')\n"
                            "def get_post(post_id):\n"
                            "    # /posts/42   → post_id = 42 (정수)\n"
                            "    # /posts/abc  → 404 자동 반환 (정수 변환 실패)\n"
                            "    return f'게시글 {post_id}번'\n"
                            "\n"
                            "# URL 변수 — 실수 타입\n"
                            "@app.route('/price/[float:amount]')\n"
                            "def show_price(amount):\n"
                            "    return f'가격: {amount:,.2f}원'\n"
                            "\n"
                            "# URL 변수 — 경로 타입 (슬래시 포함)\n"
                            "@app.route('/files/[path:filepath]')\n"
                            "def get_file(filepath):\n"
                            "    # /files/docs/2024/report.pdf → filepath = 'docs/2024/report.pdf'\n"
                            "    return f'파일 경로: {filepath}'"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "URL 변수 타입 변환자(converter): "
                            "string(기본), int(정수), float(실수), path(슬래시 포함 문자열), "
                            "uuid(UUID 형식). "
                            "타입 불일치 시 Flask가 자동으로 404를 반환합니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "HTTP 메서드 처리",
                    },
                    "기본적으로 @app.route()는 GET 요청만 처리합니다. "
                    "POST, PUT, DELETE를 처리하려면 methods 파라미터를 지정해야 합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask, request\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# 단일 메서드\n"
                            "@app.route('/login', methods=['POST'])\n"
                            "def login():\n"
                            "    data = request.get_json()\n"
                            "    # {'username': '...', 'password': '...'}\n"
                            "    return '로그인 처리'\n"
                            "\n"
                            "# 여러 메서드 처리\n"
                            "@app.route('/api/items', methods=['GET', 'POST'])\n"
                            "def items():\n"
                            "    if request.method == 'GET':\n"
                            "        return '전체 목록 반환'\n"
                            "    elif request.method == 'POST':\n"
                            "        return '새 항목 생성', 201\n"
                            "\n"
                            "# 개별 메서드별로 함수 분리 (더 명확)\n"
                            "@app.get('/api/products')\n"
                            "def list_products():\n"
                            "    return '상품 목록'\n"
                            "\n"
                            "@app.post('/api/products')\n"
                            "def create_product():\n"
                            "    return '상품 생성', 201"
                        ),
                    },
                ],
            },
            {
                "title": "요청과 응답 — request와 jsonify",
                "content": [
                    "Flask에서 요청 데이터를 읽고 응답을 만드는 핵심 객체가 "
                    "request와 jsonify입니다. API 개발에서 가장 자주 사용하는 패턴입니다.",
                    {
                        "type": "heading",
                        "text": "request 객체 — 요청 데이터 읽기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask, request\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "@app.route('/search')\n"
                            "def search():\n"
                            "    # 쿼리 파라미터: /search?keyword=python&page=2\n"
                            "    keyword = request.args.get('keyword', '')  # 기본값 ''\n"
                            "    page = request.args.get('page', 1, type=int)  # 정수 변환\n"
                            "    return f'키워드: {keyword}, 페이지: {page}'\n"
                            "\n"
                            "@app.route('/login', methods=['POST'])\n"
                            "def login():\n"
                            "    # JSON 바디: Content-Type: application/json\n"
                            "    data = request.get_json()\n"
                            "    if data is None:\n"
                            "        return '잘못된 JSON 형식', 400\n"
                            "    username = data.get('username', '')\n"
                            "    password = data.get('password', '')\n"
                            "    return f'{username}으로 로그인 시도'\n"
                            "\n"
                            "@app.route('/upload', methods=['POST'])\n"
                            "def upload():\n"
                            "    # 폼 데이터: Content-Type: multipart/form-data\n"
                            "    name = request.form.get('name', '')\n"
                            "    file = request.files.get('photo')  # 파일 업로드\n"
                            "    return f'이름: {name}, 파일: {file.filename if file else \"없음\"}'\n"
                            "\n"
                            "@app.route('/api/info')\n"
                            "def api_info():\n"
                            "    # 요청 메타 정보\n"
                            "    return {\n"
                            "        'method': request.method,\n"
                            "        'path': request.path,\n"
                            "        'remote_addr': request.remote_addr,\n"
                            "        'user_agent': request.headers.get('User-Agent', ''),\n"
                            "    }"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "jsonify — JSON 응답 만들기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask, jsonify, request\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# 샘플 데이터 (실제로는 DB에서 조회)\n"
                            "USERS = [\n"
                            "    {'id': 1, '이름': '김철수', '나이': 28},\n"
                            "    {'id': 2, '이름': '이영희', '나이': 25},\n"
                            "]\n"
                            "\n"
                            "@app.route('/api/users')\n"
                            "def get_users():\n"
                            "    # jsonify: 딕셔너리/리스트를 JSON 응답으로 변환\n"
                            "    # Content-Type: application/json 자동 설정\n"
                            "    return jsonify({'users': USERS, 'total': len(USERS)})\n"
                            "\n"
                            "@app.route('/api/users/[int:user_id]')\n"
                            "def get_user(user_id):\n"
                            "    # 리스트 컴프리헨션으로 사용자 탐색 (불변 패턴)\n"
                            "    matched = [u for u in USERS if u['id'] == user_id]\n"
                            "    if not matched:\n"
                            "        # 두 번째 인자로 상태 코드 지정\n"
                            "        return jsonify({'error': '사용자를 찾을 수 없습니다'}), 404\n"
                            "    return jsonify(matched[0])\n"
                            "\n"
                            "@app.route('/api/users', methods=['POST'])\n"
                            "def create_user():\n"
                            "    data = request.get_json()\n"
                            "    if not data or '이름' not in data:\n"
                            "        return jsonify({'error': '이름은 필수입니다'}), 400\n"
                            "    # 새 사용자 생성 (불변 패턴: 원본 리스트를 직접 수정하지 않음)\n"
                            "    new_id = max(u['id'] for u in USERS) + 1\n"
                            "    new_user = {'id': new_id, **data}\n"
                            "    # 실제 앱에서는 DB에 저장\n"
                            "    return jsonify(new_user), 201"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Flask 1.0+ 에서는 딕셔너리를 직접 반환해도 자동으로 JSON 응답이 됩니다. "
                            "즉, return {'key': 'value'} 는 return jsonify({'key': 'value'})와 동일합니다. "
                            "그러나 상태 코드를 함께 지정할 때는 jsonify를 명시적으로 사용하는 것이 더 명확합니다."
                        ),
                    },
                ],
            },
            {
                "title": "Jinja2 템플릿 — HTML 동적 생성",
                "content": [
                    "API만 만든다면 JSON 응답으로 충분하지만, "
                    "웹 페이지(HTML)를 서빙할 때는 Jinja2 템플릿 엔진을 사용합니다. "
                    "Jinja2는 Python 변수를 HTML에 삽입하고, 조건문/반복문을 HTML에서 사용할 수 있게 합니다.",
                    {
                        "type": "heading",
                        "text": "render_template 기본 사용",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# app.py\n"
                            "from flask import Flask, render_template\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "@app.route('/')\n"
                            "def index():\n"
                            "    # templates/index.html 파일을 렌더링\n"
                            "    return render_template(\n"
                            "        'index.html',\n"
                            "        title='내 홈페이지',           # 템플릿 변수 전달\n"
                            "        username='김철수',\n"
                            "        items=['Python', 'Flask', 'Docker'],\n"
                            "    )\n"
                            "\n"
                            "@app.route('/users')\n"
                            "def users_page():\n"
                            "    users = [\n"
                            "        {'id': 1, '이름': '김철수', '등급': 'A'},\n"
                            "        {'id': 2, '이름': '이영희', '등급': 'B'},\n"
                            "    ]\n"
                            "    return render_template('users.html', users=users)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "Jinja2 템플릿 문법",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# templates/index.html (Jinja2 문법 예시)\n"
                            "# 변수 출력: {{ 변수명 }}\n"
                            "# 제어문: {% if %}, {% for %}, {% block %}\n"
                            "# 주석: {# 주석 내용 #}\n"
                            "\n"
                            "# ─── 실제 HTML 파일 내용 (Python 문자열로 표현) ───\n"
                            "TEMPLATE_EXAMPLE = '''\n"
                            "<!DOCTYPE html>\n"
                            "<html lang=\"ko\">\n"
                            "<head>\n"
                            "    <title>{{ title }}</title>\n"
                            "</head>\n"
                            "<body>\n"
                            "    <h1>안녕하세요, {{ username }}님!</h1>\n"
                            "\n"
                            "    {# 조건문 #}\n"
                            "    {% if items %}\n"
                            "        <ul>\n"
                            "        {% for item in items %}\n"
                            "            <li>{{ loop.index }}. {{ item }}</li>\n"
                            "        {% endfor %}\n"
                            "        </ul>\n"
                            "    {% else %}\n"
                            "        <p>항목이 없습니다.</p>\n"
                            "    {% endif %}\n"
                            "\n"
                            "    {# 필터: |upper, |lower, |length, |default #}\n"
                            "    <p>이름 대문자: {{ username|upper }}</p>\n"
                            "    <p>항목 수: {{ items|length }}</p>\n"
                            "</body>\n"
                            "</html>\n"
                            "'''"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "템플릿 상속 — base.html 패턴",
                    },
                    "중복 HTML을 제거하는 강력한 패턴입니다. "
                    "헤더, 푸터, 내비게이션 같은 공통 레이아웃을 base.html에 두고, "
                    "각 페이지는 내용만 오버라이드합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# templates/base.html\n"
                            "BASE_HTML = '''\n"
                            "<!DOCTYPE html>\n"
                            "<html>\n"
                            "<head>\n"
                            "    <title>{% block title %}기본 제목{% endblock %}</title>\n"
                            "    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='style.css') }}\">\n"
                            "</head>\n"
                            "<body>\n"
                            "    <nav><a href=\"/\">홈</a> | <a href=\"/about\">소개</a></nav>\n"
                            "    <main>\n"
                            "        {% block content %}{% endblock %}\n"
                            "    </main>\n"
                            "    <footer><p>Python Mastery Series</p></footer>\n"
                            "</body>\n"
                            "</html>\n"
                            "'''\n"
                            "\n"
                            "# templates/index.html (base.html 상속)\n"
                            "INDEX_HTML = '''\n"
                            "{% extends 'base.html' %}\n"
                            "\n"
                            "{% block title %}홈페이지{% endblock %}\n"
                            "\n"
                            "{% block content %}\n"
                            "    <h1>환영합니다!</h1>\n"
                            "    <p>Flask로 만든 첫 번째 웹 앱입니다.</p>\n"
                            "{% endblock %}\n"
                            "'''"
                        ),
                    },
                ],
            },
            {
                "title": "정적 파일 서빙과 Flask 요청 처리 흐름",
                "content": [
                    "정적 파일(CSS, JavaScript, 이미지)은 Flask의 static/ 폴더에 저장하고, "
                    "url_for('static', filename='파일명')으로 경로를 생성합니다. "
                    "이 섹션에서는 정적 파일 서빙과 Flask의 전체 요청 처리 흐름을 정리합니다.",
                    {
                        "type": "heading",
                        "text": "정적 파일 서빙",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Flask는 static/ 폴더를 자동으로 /static/ URL에 매핑합니다.\n"
                            "# 디렉터리 구조:\n"
                            "#   static/\n"
                            "#     css/\n"
                            "#       style.css    → /static/css/style.css\n"
                            "#     js/\n"
                            "#       main.js      → /static/js/main.js\n"
                            "#     img/\n"
                            "#       logo.png     → /static/img/logo.png\n"
                            "\n"
                            "from flask import Flask, url_for\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "@app.route('/demo')\n"
                            "def demo():\n"
                            "    # url_for로 정적 파일 URL 생성 (하드코딩 금지)\n"
                            "    css_url = url_for('static', filename='css/style.css')\n"
                            "    js_url = url_for('static', filename='js/main.js')\n"
                            "    # /static/css/style.css, /static/js/main.js 반환\n"
                            "    return f'CSS: {css_url}, JS: {js_url}'\n"
                            "\n"
                            "# 템플릿에서 정적 파일 참조\n"
                            "# {{ url_for('static', filename='css/style.css') }}\n"
                            "# → /static/css/style.css\n"
                            "\n"
                            "# 운영 환경 팁: 정적 파일은 Nginx/CDN에서 직접 서빙하는 것이 더 효율적\n"
                            "# Flask는 개발/소규모 서비스에서만 정적 파일을 직접 서빙"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "Flask 요청 처리 흐름 전체 그림",
                    },
                    {
                        "type": "flow_diagram",
                        "title": "Flask 요청 처리 흐름",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "클라이언트 HTTP 요청", "sub": "GET /users/1"},
                            {"label": "WSGI 서버 수신", "sub": "Werkzeug (개발), Gunicorn (운영)"},
                            {"label": "Flask 라우터", "sub": "@app.route 매핑 탐색"},
                            {"label": "Before Request Hook", "sub": "@app.before_request 실행"},
                            {"label": "뷰 함수 실행", "sub": "def get_user(user_id): ..."},
                            {"label": "After Request Hook", "sub": "@app.after_request 실행"},
                            {"label": "Response 객체 생성", "sub": "jsonify / render_template"},
                            {"label": "HTTP 응답 반환", "sub": "200 OK + JSON/HTML"},
                        ],
                        "note": "라우터에서 매핑이 없으면 404, 뷰 함수에서 예외 발생 시 500 자동 반환",
                    },
                    {
                        "type": "heading",
                        "text": "에러 핸들러 등록",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from flask import Flask, jsonify\n"
                            "app = Flask(__name__)\n"
                            "\n"
                            "# 404 에러 핸들러\n"
                            "@app.errorhandler(404)\n"
                            "def not_found(error):\n"
                            "    return jsonify({'error': '요청한 리소스를 찾을 수 없습니다',\n"
                            "                    'code': 404}), 404\n"
                            "\n"
                            "# 500 에러 핸들러\n"
                            "@app.errorhandler(500)\n"
                            "def server_error(error):\n"
                            "    return jsonify({'error': '서버 내부 오류가 발생했습니다',\n"
                            "                    'code': 500}), 500\n"
                            "\n"
                            "# Before/After Request Hook\n"
                            "@app.before_request\n"
                            "def log_request():\n"
                            "    \"\"\"모든 요청 전에 실행 — 로깅, 인증 체크 등\"\"\"\n"
                            "    from flask import request\n"
                            "    print(f'[요청] {request.method} {request.path}')\n"
                            "\n"
                            "@app.after_request\n"
                            "def add_cors_headers(response):\n"
                            "    \"\"\"모든 응답 후 실행 — 헤더 추가 등\"\"\"\n"
                            "    response.headers['X-Powered-By'] = 'Flask'\n"
                            "    return response  # 반드시 response 반환"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "url_for() 함수를 사용하면 URL을 하드코딩하지 않아도 됩니다. "
                            "라우트 경로가 바뀌어도 url_for('함수명')이 자동으로 올바른 URL을 생성합니다. "
                            "템플릿 내부에서도, Python 코드에서도 항상 url_for를 사용하세요."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "Flask 개발 서버(app.run)는 한 번에 하나의 요청만 처리합니다. "
            "운영 환경에서는 반드시 Gunicorn이나 uWSGI 같은 WSGI 서버를 사용하세요.",
            "request.get_json()이 None을 반환하면 Content-Type 헤더가 application/json이 아닌 경우입니다. "
            "Postman이나 curl로 테스트할 때 헤더를 꼭 확인하세요.",
            "템플릿 파일은 반드시 templates/ 폴더에, 정적 파일은 static/ 폴더에 두세요. "
            "Flask가 자동으로 이 경로를 탐색합니다.",
            "에러 핸들러(@app.errorhandler)를 반드시 등록하세요. "
            "HTML 기반 앱이라면 HTML 에러 페이지를, API라면 JSON 에러 응답을 반환하도록 분기하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "Flask에서 GET /users/42 요청이 들어올 때 user_id 변수가 정수 42로 자동 변환되는 올바른 라우트 정의는?",
                "choices": [
                    "@app.route('/users/user_id')",
                    "@app.route('/users/{user_id}')",
                    "@app.route('/users/[int:user_id]')",
                    "@app.route('/users/?user_id=int')",
                ],
                "answer": "3번",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "Flask에서 POST /login 요청의 JSON 바디를 읽는 올바른 방법은?",
                "choices": [
                    "request.body.json()",
                    "request.get_json()",
                    "request.data.parse()",
                    "request.form.get_json()",
                ],
                "answer": "2번",
            },
            {
                "number": 3,
                "type": "code",
                "question": (
                    "다음 요구사항을 만족하는 Flask 앱을 작성하세요.\n"
                    "- GET /api/calc?a=10&b=5 요청 처리\n"
                    "- JSON 응답: {\"합\": 15, \"차\": 5, \"곱\": 50, \"나눗셈\": 2.0}\n"
                    "- a 또는 b가 없으면 400 에러와 함께 {\"error\": \"a, b 파라미터가 필요합니다\"} 반환"
                ),
                "hint": "request.args.get('a', type=float)으로 쿼리 파라미터를 읽고, None 체크 후 계산하세요.",
                "answer": (
                    "from flask import Flask, jsonify, request\n"
                    "app = Flask(__name__)\n"
                    "\n"
                    "@app.get('/api/calc')\n"
                    "def calculate():\n"
                    "    a = request.args.get('a', type=float)\n"
                    "    b = request.args.get('b', type=float)\n"
                    "    if a is None or b is None:\n"
                    "        return jsonify({'error': 'a, b 파라미터가 필요합니다'}), 400\n"
                    "    result = {\n"
                    "        '합': a + b,\n"
                    "        '차': a - b,\n"
                    "        '곱': a * b,\n"
                    "        '나눗셈': a / b if b != 0 else None,\n"
                    "    }\n"
                    "    return jsonify(result)"
                ),
            },
            {
                "number": 4,
                "type": "short_answer",
                "question": "Flask에서 URL을 하드코딩하지 않고 동적으로 생성하는 데 사용하는 함수는?",
                "answer": "url_for('뷰_함수명')  — 라우트 경로가 바뀌어도 자동으로 올바른 URL을 생성합니다.",
            },
            {
                "number": 5,
                "type": "multiple_choice",
                "question": "Flask에서 @app.before_request 데코레이터로 등록된 함수는 언제 실행되는가?",
                "choices": [
                    "앱 시작 시 한 번만 실행",
                    "에러 발생 시 실행",
                    "모든 요청이 뷰 함수에 도달하기 전에 실행",
                    "응답이 클라이언트에게 전송된 후 실행",
                ],
                "answer": "3번",
            },
        ],
        "challenge": {
            "question": (
                "간단한 방문자 카운터 API를 Flask로 구현하세요.\n\n"
                "요구사항:\n"
                "① GET /api/counter → 현재 방문 횟수 반환: {\"count\": N}\n"
                "② POST /api/counter/reset → 카운터 초기화: {\"count\": 0, \"message\": \"초기화 완료\"}\n"
                "③ GET / → HTML 페이지 반환 (방문할 때마다 카운터 1 증가)\n"
                "④ Jinja2 템플릿으로 방문 횟수를 보여주는 HTML 페이지 제공\n\n"
                "주의: 상태를 메모리에 저장하는 딕셔너리를 사용하되, "
                "딕셔너리 자체를 교체하는 방식으로 불변 패턴을 유지하세요."
            ),
            "hint": (
                "전역 딕셔너리 counter = {'count': 0}을 사용하세요. "
                "값을 증가시킬 때는 counter = {**counter, 'count': counter['count'] + 1} 형태로 "
                "새 딕셔너리를 할당합니다."
            ),
        },
        "summary": [
            "Flask는 마이크로 프레임워크로 핵심 기능만 제공하며, @app.route() 데코레이터로 URL과 함수를 연결합니다.",
            "URL 변수에 [int:name], [float:name] 타입 지정자를 사용하면 자동 변환과 검증이 됩니다.",
            "request.args(쿼리 파라미터), request.get_json()(바디), request.form(폼)으로 요청 데이터를 읽습니다.",
            "jsonify()로 JSON 응답을 만들고, 두 번째 반환값으로 HTTP 상태 코드를 지정합니다.",
            "Jinja2 템플릿에서 {{ 변수 }}, {% if %}, {% for %}, {% extends %}로 동적 HTML을 생성합니다.",
            "url_for('함수명')으로 URL을 하드코딩 없이 생성하세요. 라우트가 바뀌어도 자동으로 동작합니다.",
            "@app.before_request, @app.after_request, @app.errorhandler로 요청/응답 파이프라인을 확장합니다.",
        ],
    }
