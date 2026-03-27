"""
Ch 0: 복습 & 웹 개발 준비
Python Mastery Series Vol.4 — 웹 & 배포
"""


def get_chapter():
    return {
        "number": 0,
        "title": "복습 & 웹 개발 준비",
        "subtitle": "Vol.3 핵심 정리와 웹 개발 환경 구축",
        "big_picture": (
            "Vol.4를 시작하기 전에 Vol.3에서 배운 데이터 분석 핵심 개념을 빠르게 복습하고, "
            "웹 개발이 무엇인지 이해합니다. 클라이언트-서버 구조, HTTP 프로토콜, "
            "요청-응답 사이클은 Flask와 FastAPI를 배우기 위한 필수 배경 지식입니다. "
            "또한 가상환경(venv)으로 깔끔한 웹 개발 환경을 준비합니다."
        ),
        "sections": [
            {
                "title": "Vol.3 핵심 복습 — 데이터 분석 & 시각화",
                "content": [
                    "Vol.4 웹 개발을 본격적으로 시작하기 전, Vol.3에서 다뤘던 핵심 도구들을 "
                    "빠르게 정리해봅시다. 특히 Pandas와 JSON 처리는 웹 API를 만들 때 "
                    "데이터를 다루는 핵심 기술로 계속 등장합니다.",
                    {
                        "type": "heading",
                        "text": "Pandas — 데이터프레임 핵심 요약",
                    },
                    "Pandas의 DataFrame은 웹 서비스에서 DB 조회 결과를 처리하거나 "
                    "JSON 응답을 구조화할 때 자주 활용됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.3 복습 — Pandas 핵심 패턴\n"
                            "import pandas as pd\n"
                            "\n"
                            "# DataFrame 생성\n"
                            "data = [\n"
                            "    {'이름': '김철수', '점수': 85, '등급': 'B'},\n"
                            "    {'이름': '이영희', '점수': 92, '등급': 'A'},\n"
                            "    {'이름': '박민준', '점수': 78, '등급': 'C'},\n"
                            "]\n"
                            "df = pd.DataFrame(data)\n"
                            "\n"
                            "# 필터링\n"
                            "a_grade = df[df['등급'] == 'A']\n"
                            "print(a_grade)  # 이영희만 출력\n"
                            "\n"
                            "# JSON으로 변환 (웹 API 응답에 활용)\n"
                            "json_data = df.to_dict(orient='records')\n"
                            "# [{'이름': '김철수', '점수': 85, '등급': 'B'}, ...]\n"
                            "\n"
                            "# 통계 요약\n"
                            "print(df['점수'].describe())"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "JSON — 웹 개발의 공용어",
                    },
                    "웹 API에서 데이터를 주고받을 때는 거의 항상 JSON 형식을 사용합니다. "
                    "Vol.3에서 배운 json 모듈 활용이 여기서도 핵심입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.3 복습 — JSON 처리\n"
                            "import json\n"
                            "\n"
                            "# Python 딕셔너리 → JSON 문자열\n"
                            "user = {'id': 1, '이름': '김철수', '나이': 25}\n"
                            "json_str = json.dumps(user, ensure_ascii=False, indent=2)\n"
                            "print(json_str)\n"
                            "# {\n"
                            "#   \"id\": 1,\n"
                            "#   \"이름\": \"김철수\",\n"
                            "#   \"나이\": 25\n"
                            "# }\n"
                            "\n"
                            "# JSON 문자열 → Python 딕셔너리\n"
                            "parsed = json.loads(json_str)\n"
                            "print(parsed['이름'])  # 김철수\n"
                            "\n"
                            "# requests로 외부 API 호출 (Vol.3 Ch.6 복습)\n"
                            "import requests\n"
                            "response = requests.get('https://api.example.com/users/1')\n"
                            "if response.status_code == 200:\n"
                            "    data = response.json()  # JSON 자동 파싱\n"
                            "    print(data)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "시각화 — Matplotlib / Seaborn 핵심",
                    },
                    "웹 서비스에서 데이터 시각화 결과를 이미지로 서빙하거나, "
                    "대시보드를 만들 때 Vol.3 시각화 지식이 연결됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.3 복습 — Matplotlib 차트를 바이트 스트림으로 변환\n"
                            "# (Flask에서 이미지를 동적으로 반환할 때 활용)\n"
                            "import matplotlib.pyplot as plt\n"
                            "import io\n"
                            "import base64\n"
                            "\n"
                            "def create_chart_base64(labels, values):\n"
                            "    \"\"\"차트를 Base64 인코딩 문자열로 반환\"\"\"\n"
                            "    fig, ax = plt.subplots(figsize=(8, 4))\n"
                            "    ax.bar(labels, values, color='#3182f6')\n"
                            "    ax.set_title('월별 방문자 수')\n"
                            "\n"
                            "    # 파일 저장 없이 메모리 버퍼에 저장\n"
                            "    buf = io.BytesIO()\n"
                            "    plt.savefig(buf, format='png', bbox_inches='tight')\n"
                            "    plt.close(fig)  # 메모리 누수 방지\n"
                            "    buf.seek(0)\n"
                            "\n"
                            "    # HTML img 태그에 바로 삽입 가능한 형태로 변환\n"
                            "    encoded = base64.b64encode(buf.read()).decode('utf-8')\n"
                            "    return f'data:image/png;base64,{encoded}'"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Vol.3 내용이 잘 기억나지 않아도 괜찮습니다. "
                            "Vol.4에서는 웹 개발에 필요한 Python 개념이 나올 때마다 "
                            "자연스럽게 복습하게 됩니다. "
                            "특히 딕셔너리, JSON, requests 모듈 사용법은 미리 확인해두세요."
                        ),
                    },
                ],
            },
            {
                "title": "웹 개발이란? — 클라이언트와 서버",
                "content": [
                    "웹 개발을 시작하기 전에 '웹이 어떻게 동작하는가'를 이해해야 합니다. "
                    "브라우저에서 URL을 입력하는 순간부터 페이지가 보이기까지 "
                    "무슨 일이 일어나는지 알면, Flask를 배울 때 훨씬 빠르게 이해됩니다.",
                    {
                        "type": "heading",
                        "text": "클라이언트-서버 아키텍처",
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "클라이언트-서버 구조는 식당과 같습니다. "
                            "손님(클라이언트)은 메뉴를 주문하고, 주방(서버)은 음식을 만들어 제공합니다. "
                            "손님은 음식이 어떻게 만들어지는지 몰라도 됩니다. "
                            "서버는 어떤 손님이 올지 몰라도 주문이 오면 응답하면 됩니다. "
                            "이 분리가 웹의 핵심 구조입니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["구분", "역할", "예시"],
                        "rows": [
                            ["클라이언트", "요청을 보내고 응답을 받아 표시", "브라우저, 모바일 앱, curl"],
                            ["서버", "요청을 받아 처리하고 응답 반환", "Flask, FastAPI, Nginx"],
                            ["네트워크", "클라이언트와 서버 사이 데이터 전달", "인터넷, 로컬 네트워크"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "HTTP — 웹의 통신 규약",
                    },
                    "HTTP(HyperText Transfer Protocol)는 클라이언트와 서버가 데이터를 주고받는 "
                    "약속(프로토콜)입니다. 모든 웹 통신은 HTTP 요청과 응답으로 이루어집니다.",
                    {
                        "type": "table",
                        "headers": ["HTTP 메서드", "의미", "주요 사용 사례"],
                        "rows": [
                            ["GET", "데이터 조회", "페이지 로드, 검색, 목록 조회"],
                            ["POST", "데이터 생성", "회원가입, 게시글 작성, 파일 업로드"],
                            ["PUT", "데이터 전체 수정", "프로필 전체 업데이트"],
                            ["PATCH", "데이터 일부 수정", "비밀번호만 변경"],
                            ["DELETE", "데이터 삭제", "게시글 삭제, 계정 탈퇴"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "HTTP 상태 코드",
                    },
                    "서버는 요청을 처리한 결과를 3자리 숫자 코드로 알려줍니다. "
                    "이 코드를 이해해야 API 개발과 디버깅이 쉬워집니다.",
                    {
                        "type": "table",
                        "headers": ["코드", "의미", "언제 사용"],
                        "rows": [
                            ["200 OK", "성공", "GET/PUT/PATCH 성공"],
                            ["201 Created", "생성됨", "POST로 리소스 생성 성공"],
                            ["400 Bad Request", "잘못된 요청", "입력값 유효성 오류"],
                            ["401 Unauthorized", "인증 필요", "로그인 없이 접근"],
                            ["403 Forbidden", "접근 거부", "권한 없음"],
                            ["404 Not Found", "리소스 없음", "존재하지 않는 URL"],
                            ["500 Internal Server Error", "서버 오류", "서버 코드 버그"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "HTTP 상태 코드를 외울 필요는 없습니다. "
                            "2xx는 성공, 4xx는 클라이언트 오류, 5xx는 서버 오류라는 "
                            "큰 그림만 이해하면 됩니다. "
                            "자주 쓰는 200, 201, 400, 401, 404, 500 정도만 기억하세요."
                        ),
                    },
                ],
            },
            {
                "title": "HTTP 요청-응답 사이클 상세",
                "content": [
                    "브라우저에서 'https://example.com/users/1'을 입력하면 "
                    "어떤 일이 벌어지는지 단계별로 추적해봅시다. "
                    "이 흐름을 이해하면 Flask 라우팅이 왜 그렇게 설계됐는지 명확해집니다.",
                    {
                        "type": "flow_diagram",
                        "title": "HTTP 요청-응답 사이클",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "1. 클라이언트 요청", "sub": "GET /users/1 HTTP/1.1"},
                            {"label": "2. DNS 조회", "sub": "example.com -> 93.184.216.34"},
                            {"label": "3. TCP 연결", "sub": "3-way handshake"},
                            {"label": "4. HTTP 요청 전송", "sub": "Headers + Body"},
                            {"label": "5. 서버 처리", "sub": "라우터 -> 컨트롤러 -> DB"},
                            {"label": "6. HTTP 응답 반환", "sub": "200 OK + JSON"},
                            {"label": "7. 클라이언트 수신", "sub": "렌더링 또는 처리"},
                        ],
                        "note": "Flask는 5번 단계의 '서버 처리' 부분을 담당합니다.",
                    },
                    {
                        "type": "heading",
                        "text": "HTTP 요청 구조",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# HTTP 요청 예시 (텍스트 형태)\n"
                            "# ──────────────────────────────────────\n"
                            "# POST /api/users HTTP/1.1          ← 요청 라인 (메서드 + 경로 + 버전)\n"
                            "# Host: api.example.com             ← 헤더 시작\n"
                            "# Content-Type: application/json\n"
                            "# Authorization: Bearer eyJhbGci...\n"
                            "# Content-Length: 42\n"
                            "#                                    ← 빈 줄 (헤더/바디 구분)\n"
                            "# {\"name\": \"김철수\", \"email\": \"kim@example.com\"}  ← 바디\n"
                            "\n"
                            "# Python requests로 동일한 요청 만들기\n"
                            "import requests\n"
                            "\n"
                            "response = requests.post(\n"
                            "    'https://api.example.com/api/users',\n"
                            "    headers={'Authorization': 'Bearer eyJhbGci...'},\n"
                            "    json={'name': '김철수', 'email': 'kim@example.com'},\n"
                            "    # json= 파라미터는 자동으로 Content-Type: application/json 추가\n"
                            ")\n"
                            "print(response.status_code)  # 201\n"
                            "print(response.json())       # {'id': 42, 'name': '김철수', ...}"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "URL 구조 분석",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# URL 구조: https://api.example.com:8080/users/1?sort=name&limit=10\n"
                            "#\n"
                            "# https          → 프로토콜 (HTTP의 보안 버전)\n"
                            "# api.example.com → 도메인 (호스트)\n"
                            "# :8080           → 포트 (생략 시 HTTPS=443, HTTP=80)\n"
                            "# /users/1        → 경로 (path) ← Flask 라우팅 대상\n"
                            "# ?sort=name      → 쿼리 파라미터 시작\n"
                            "# &limit=10       → 추가 쿼리 파라미터\n"
                            "\n"
                            "from urllib.parse import urlparse, parse_qs\n"
                            "\n"
                            "url = 'https://api.example.com:8080/users/1?sort=name&limit=10'\n"
                            "parsed = urlparse(url)\n"
                            "\n"
                            "print(parsed.scheme)   # https\n"
                            "print(parsed.netloc)   # api.example.com:8080\n"
                            "print(parsed.path)     # /users/1\n"
                            "print(parsed.query)    # sort=name&limit=10\n"
                            "\n"
                            "params = parse_qs(parsed.query)\n"
                            "print(params)          # {'sort': ['name'], 'limit': ['10']}"
                        ),
                    },
                ],
            },
            {
                "title": "개발 환경 준비 — venv와 프로젝트 구조",
                "content": [
                    "웹 개발 프로젝트는 항상 가상환경을 기반으로 시작합니다. "
                    "패키지 의존성이 복잡해지면 버전 충돌 문제가 생기는데, "
                    "프로젝트별 venv는 이 문제를 완벽하게 차단합니다.",
                    {
                        "type": "heading",
                        "text": "Vol.4 필수 패키지 설치",
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 1. 프로젝트 디렉터리 생성\n"
                            "mkdir my_web_app && cd my_web_app\n"
                            "\n"
                            "# 2. 가상환경 생성 및 활성화\n"
                            "python3 -m venv venv\n"
                            "source venv/bin/activate        # macOS / Linux\n"
                            "# venv\\Scripts\\activate        # Windows\n"
                            "\n"
                            "# 3. Vol.4 핵심 패키지 설치\n"
                            "pip install flask fastapi uvicorn sqlalchemy\n"
                            "pip install requests python-dotenv pytest httpx\n"
                            "\n"
                            "# 4. requirements.txt 저장 (버전 고정)\n"
                            "pip freeze > requirements.txt\n"
                            "\n"
                            "# 5. 나중에 다른 환경에서 동일하게 설치\n"
                            "pip install -r requirements.txt"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["패키지", "버전 (권장)", "역할"],
                        "rows": [
                            ["flask", "3.x", "가벼운 웹 프레임워크 (Ch1-2)"],
                            ["fastapi", "0.110+", "고성능 비동기 API 프레임워크 (Ch3-4)"],
                            ["uvicorn", "0.27+", "FastAPI 실행용 ASGI 서버"],
                            ["sqlalchemy", "2.x", "데이터베이스 ORM (Ch5)"],
                            ["python-dotenv", "1.x", ".env 파일로 환경변수 관리"],
                            ["pytest", "7.x", "테스트 프레임워크 (Ch7)"],
                            ["httpx", "0.27+", "비동기 HTTP 클라이언트 (테스트용)"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "Flask 프로젝트 표준 구조",
                    },
                    "Flask 프로젝트는 작게 시작해서 커질 수 있습니다. "
                    "처음부터 확장 가능한 구조로 시작하는 것이 좋습니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Flask 프로젝트 표준 디렉터리 구조\n"
                            "my_flask_app/\n"
                            "  app/\n"
                            "    __init__.py       # Flask 앱 팩토리 함수\n"
                            "    routes/           # 라우트 모듈 (Blueprint)\n"
                            "      __init__.py\n"
                            "      users.py\n"
                            "      posts.py\n"
                            "    models.py         # 데이터 모델\n"
                            "    utils.py          # 유틸리티 함수\n"
                            "  templates/          # Jinja2 HTML 템플릿\n"
                            "    base.html\n"
                            "    index.html\n"
                            "  static/             # CSS, JS, 이미지\n"
                            "    style.css\n"
                            "  tests/              # pytest 테스트\n"
                            "    test_routes.py\n"
                            "  .env                # 환경변수 (Git에 올리면 안 됨!)\n"
                            "  .gitignore\n"
                            "  requirements.txt\n"
                            "  run.py              # 앱 실행 진입점"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            ".env 파일에는 API 키, DB 비밀번호 등 민감한 정보가 담깁니다. "
                            "절대 Git에 커밋하지 마세요. "
                            ".gitignore 파일에 반드시 '.env'를 추가하고, "
                            ".env.example 파일을 만들어 어떤 환경변수가 필요한지 문서화하세요."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# .env 파일 내용 예시\n"
                            "# SECRET_KEY=my-super-secret-key-change-this\n"
                            "# DATABASE_URL=sqlite:///app.db\n"
                            "# DEBUG=True\n"
                            "\n"
                            "# Python에서 .env 파일 읽기\n"
                            "from dotenv import load_dotenv\n"
                            "import os\n"
                            "\n"
                            "load_dotenv()  # .env 파일을 환경변수로 로드\n"
                            "\n"
                            "SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')\n"
                            "DATABASE_URL = os.environ['DATABASE_URL']  # 없으면 KeyError\n"
                            "DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'\n"
                            "\n"
                            "print(f'DEBUG 모드: {DEBUG}')\n"
                            "print(f'DB URL: {DATABASE_URL}')"
                        ),
                    },
                ],
            },
            {
                "title": "Vol.4 학습 로드맵",
                "content": [
                    "Vol.4는 'Python으로 웹 서비스를 만들고 세상에 배포하는 법'을 배웁니다. "
                    "Flask로 시작해서 FastAPI, DB 연동, Docker, 클라우드 배포까지 "
                    "실제 서비스 개발 전체 흐름을 경험합니다.",
                    {
                        "type": "flow_diagram",
                        "title": "Vol.4 학습 흐름",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "Ch 0: 준비", "sub": "HTTP 기초, 환경 구축"},
                            {"label": "Ch 1: Flask 기초", "sub": "라우팅, 템플릿, 정적 파일"},
                            {"label": "Ch 2: Flask REST API", "sub": "CRUD, Blueprint, 유효성 검사"},
                            {"label": "Ch 3: FastAPI 기초", "sub": "자동 문서화, 타입 힌트"},
                            {"label": "Ch 4: FastAPI 심화", "sub": "비동기, 인증(JWT)"},
                            {"label": "Ch 5: 데이터베이스", "sub": "SQLAlchemy, 마이그레이션"},
                            {"label": "Ch 6: Docker", "sub": "컨테이너화, Docker Compose"},
                            {"label": "Ch 7: 테스트 & CI/CD", "sub": "pytest, GitHub Actions"},
                            {"label": "Ch 8: 클라우드 배포", "sub": "AWS/GCP, 도메인, HTTPS"},
                            {"label": "Ch 9: 종합 프로젝트", "sub": "MLOps API 서비스 구축"},
                        ],
                        "note": "각 챕터는 이전 챕터를 기반으로 확장됩니다. Ch1부터 순서대로 학습하세요.",
                    },
                    {
                        "type": "table",
                        "headers": ["단계", "챕터", "핵심 기술", "MLOps 연결"],
                        "rows": [
                            ["웹 기초", "Ch 1-2", "Flask, REST API", "모델 결과 API 서빙"],
                            ["고성능 API", "Ch 3-4", "FastAPI, 비동기", "ML 추론 엔드포인트"],
                            ["데이터 저장", "Ch 5", "SQLAlchemy, SQLite", "실험 결과 DB 저장"],
                            ["컨테이너화", "Ch 6", "Docker, Compose", "모델 환경 재현성"],
                            ["자동화", "Ch 7", "pytest, CI/CD", "모델 품질 자동 검증"],
                            ["운영", "Ch 8", "클라우드, HTTPS", "실서비스 배포"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "MLOps를 목표로 한다면 Flask/FastAPI로 모델 API를 만드는 능력이 필수입니다. "
                            "데이터 사이언티스트가 만든 모델을 '실제로 쓸 수 있는 서비스'로 "
                            "만드는 사람이 바로 ML 엔지니어 / MLOps 엔지니어입니다. "
                            "Vol.4는 그 핵심 역량을 위한 챕터입니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "HTTP 메서드와 상태 코드는 외우지 말고 의미를 이해하세요. "
            "GET은 '가져다줘', POST는 '만들어줘', 404는 '없어'처럼 직관적으로 기억하면 됩니다.",
            "가상환경(venv)은 절대 Git에 커밋하지 마세요. "
            ".gitignore에 venv/ 를 추가하고, requirements.txt만 공유하세요.",
            "웹 개발을 처음 배울 때는 curl 또는 Postman으로 직접 HTTP 요청을 보내보세요. "
            "브라우저는 GET 요청만 쉽게 테스트할 수 있지만, curl은 모든 메서드를 지원합니다.",
            "ERROR 메시지를 보면 겁먹지 말고 상태 코드부터 확인하세요. "
            "5xx면 서버 코드 문제, 4xx면 요청 방법 문제입니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "브라우저에서 웹 페이지를 조회할 때 사용하는 HTTP 메서드는?",
                "choices": [
                    "POST",
                    "GET",
                    "PUT",
                    "DELETE",
                ],
                "answer": "2번",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "HTTP 상태 코드 404의 의미로 올바른 것은?",
                "choices": [
                    "서버 내부 오류 발생",
                    "요청 성공",
                    "요청한 리소스를 찾을 수 없음",
                    "인증 정보가 필요함",
                ],
                "answer": "3번",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "다음 URL에서 경로(path)와 쿼리 파라미터를 각각 구분하세요.\n"
                    "URL: https://api.example.com/products/42?category=shoes&sort=price"
                ),
                "answer": (
                    "경로(path): /products/42  |  "
                    "쿼리 파라미터: category=shoes, sort=price"
                ),
            },
        ],
        "challenge": {
            "question": (
                "Python의 http.server 내장 모듈을 사용해 간단한 HTTP 서버를 만들어보세요.\n\n"
                "요구사항:\n"
                "① 포트 8080에서 실행\n"
                "② GET /health 요청에 JSON 응답 반환: {\"status\": \"ok\", \"version\": \"1.0\"}\n"
                "③ 그 외 경로는 404 응답\n\n"
                "힌트: http.server.BaseHTTPRequestHandler를 상속하고 "
                "do_GET 메서드를 오버라이드하세요."
            ),
            "hint": (
                "self.path로 요청 경로를 확인하고, "
                "self.send_response(200), self.send_header('Content-Type', 'application/json'), "
                "self.end_headers(), self.wfile.write(json_bytes) 순서로 응답을 구성합니다."
            ),
        },
        "summary": [
            "Pandas DataFrame의 to_dict(orient='records')로 JSON 응답 데이터를 쉽게 만들 수 있습니다.",
            "HTTP는 클라이언트-서버 통신의 약속이며, 메서드(GET/POST/...)와 상태 코드(2xx/4xx/5xx)가 핵심입니다.",
            "URL은 프로토콜, 도메인, 포트, 경로, 쿼리 파라미터로 구성됩니다.",
            "Flask 프로젝트는 app/, templates/, static/, tests/ 구조로 시작하는 것이 표준입니다.",
            "환경변수(.env)로 비밀 정보를 관리하고, .gitignore로 Git에서 제외하세요.",
            "MLOps에서 웹 개발은 '모델을 서비스로 만드는 능력'의 핵심입니다.",
        ],
    }
