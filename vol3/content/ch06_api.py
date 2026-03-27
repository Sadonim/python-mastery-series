"""챕터 6: API로 데이터 수집하기 — 인터넷의 데이터를 코드로 가져오는 법."""


def get_chapter():
    """챕터 6 콘텐츠를 반환한다."""
    return {
        "number": 6,
        "title": "API로 데이터 수집하기",
        "subtitle": "인터넷의 데이터를 코드로 가져오는 법",
        "big_picture": (
            "우리가 매일 사용하는 날씨 앱, 지도 앱, 번역 앱은 모두 API를 통해 데이터를 주고받습니다. "
            "API(Application Programming Interface)는 프로그램과 프로그램이 대화하는 규칙입니다. "
            "Python의 requests 라이브러리를 사용하면 단 몇 줄로 인터넷에 있는 "
            "방대한 데이터를 수집하고 분석할 수 있습니다. "
            "이 챕터에서는 REST API의 개념부터 실제 공공 API 활용까지 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: API란? REST API 기초 개념 ───────────────
            {
                "title": "API란 무엇인가? REST API 기초",
                "content": [
                    "API는 서로 다른 소프트웨어가 서로 소통하는 방법을 정의한 규칙의 집합입니다. "
                    "REST API는 웹에서 가장 널리 쓰이는 API 방식으로, "
                    "HTTP 프로토콜 위에서 동작합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "API는 식당의 메뉴판과 같습니다. "
                            "손님(클라이언트)은 주방(서버)에 직접 들어갈 수 없지만, "
                            "메뉴판(API)에 있는 항목을 주문(요청)하면 "
                            "원하는 음식(데이터)을 받을 수 있습니다. "
                            "주방 내부 구현(데이터베이스, 로직)은 알 필요가 없습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["개념", "설명", "예시"],
                        "rows": [
                            ["엔드포인트(Endpoint)", "API가 제공하는 특정 기능의 URL 주소", "https://api.example.com/weather"],
                            ["요청(Request)", "클라이언트가 서버에 보내는 메시지", "서울 날씨 알려줘"],
                            ["응답(Response)", "서버가 클라이언트에 돌려주는 메시지", "현재 기온 20°C, 맑음"],
                            ["상태 코드(Status Code)", "요청 처리 결과를 나타내는 숫자", "200(성공), 404(없음), 500(서버 오류)"],
                            ["JSON", "API 응답의 표준 데이터 형식", '{\"temp\": 20, \"weather\": \"맑음\"}'],
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["HTTP 상태 코드", "의미", "대응 방법"],
                        "rows": [
                            ["200 OK", "성공", "응답 데이터 처리"],
                            ["201 Created", "생성 성공 (POST)", "새 리소스 ID 저장"],
                            ["400 Bad Request", "잘못된 요청 (파라미터 오류)", "요청 파라미터 확인"],
                            ["401 Unauthorized", "인증 실패 (API 키 오류)", "API 키 확인"],
                            ["403 Forbidden", "권한 없음", "접근 권한 확인"],
                            ["404 Not Found", "리소스 없음", "URL/ID 확인"],
                            ["429 Too Many Requests", "요청 한도 초과", "대기 후 재시도"],
                            ["500 Internal Server Error", "서버 내부 오류", "잠시 후 재시도"],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "API 요청/응답 흐름",
                        "steps": [
                            "클라이언트 (Python 코드)",
                            "HTTP 요청 전송 (URL + 메서드 + 헤더 + 본문)",
                            "인터넷 (네트워크)",
                            "API 서버 (요청 처리)",
                            "HTTP 응답 반환 (상태 코드 + JSON 데이터)",
                            "클라이언트 (응답 파싱 및 활용)",
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "REST(Representational State Transfer)는 URL이 자원(resource)을 나타내고, "
                            "HTTP 메서드(GET/POST/PUT/DELETE)가 동작을 나타내는 설계 방식입니다. "
                            "예: GET /users/123 → 123번 사용자 조회, "
                            "DELETE /users/123 → 123번 사용자 삭제."
                        ),
                    },
                ],
            },
            # ── 섹션 2: HTTP 메서드와 requests 라이브러리 ────────
            {
                "title": "HTTP 메서드와 requests 라이브러리",
                "content": [
                    "HTTP 메서드는 서버에 어떤 작업을 요청하는지 나타냅니다. "
                    "Python의 requests 라이브러리는 이를 매우 직관적으로 구현합니다.",
                    {
                        "type": "table",
                        "headers": ["HTTP 메서드", "의미", "사용 상황", "requests 함수"],
                        "rows": [
                            ["GET", "데이터 조회", "날씨 조회, 목록 가져오기", "requests.get()"],
                            ["POST", "데이터 생성", "회원가입, 글 작성", "requests.post()"],
                            ["PUT", "데이터 전체 수정", "프로필 전체 업데이트", "requests.put()"],
                            ["PATCH", "데이터 부분 수정", "비밀번호만 변경", "requests.patch()"],
                            ["DELETE", "데이터 삭제", "게시글 삭제", "requests.delete()"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# pip install requests\n"
                            "import requests\n\n\n"
                            "# 기본 GET 요청\n"
                            "response = requests.get('https://httpbin.org/get')\n\n"
                            "print(response.status_code)   # 200\n"
                            "print(response.headers['Content-Type'])  # application/json\n"
                            "print(response.text)          # 응답 본문 (문자열)\n"
                            "print(response.json())        # JSON → Python 딕셔너리 자동 변환\n\n\n"
                            "# 쿼리 파라미터 전달 (params)\n"
                            "# URL: https://httpbin.org/get?name=철수&age=25\n"
                            "params = {'name': '철수', 'age': 25}\n"
                            "response = requests.get('https://httpbin.org/get', params=params)\n"
                            "print(response.url)  # 최종 URL 확인\n"
                            "print(response.json()['args'])  # {'name': '철수', 'age': '25'}"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "# POST 요청: JSON 데이터 전송\n"
                            "data = {'username': '철수', 'score': 95}\n"
                            "response = requests.post(\n"
                            "    'https://httpbin.org/post',\n"
                            "    json=data,  # json= 옵션: Content-Type 자동 설정 + 직렬화\n"
                            ")\n"
                            "print(response.status_code)   # 200\n"
                            "result = response.json()\n"
                            "print(result['json'])  # 서버가 받은 데이터 확인\n\n\n"
                            "# 타임아웃 설정 (중요! 없으면 영원히 대기할 수 있음)\n"
                            "try:\n"
                            "    response = requests.get(\n"
                            "        'https://httpbin.org/delay/3',\n"
                            "        timeout=5,  # 5초 안에 응답 없으면 예외 발생\n"
                            "    )\n"
                            "except requests.exceptions.Timeout:\n"
                            "    print('요청 시간 초과 — 네트워크 상태를 확인하세요')\n"
                            "except requests.exceptions.ConnectionError:\n"
                            "    print('연결 실패 — 인터넷 연결을 확인하세요')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "requests는 표준 라이브러리가 아니므로 설치가 필요합니다: "
                            "`pip install requests`. "
                            "타임아웃 없이 요청하면 서버가 응답하지 않을 때 프로그램이 멈춥니다. "
                            "항상 `timeout` 매개변수를 지정하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 3: JSON 응답 처리 ────────────────────────────
            {
                "title": "JSON 응답 처리",
                "content": [
                    "대부분의 REST API는 JSON 형식으로 응답합니다. "
                    "중첩된 JSON 구조를 안전하게 탐색하고 필요한 데이터를 추출하는 방법을 익힙니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "# JSONPlaceholder: 연습용 무료 API\n"
                            "response = requests.get(\n"
                            "    'https://jsonplaceholder.typicode.com/users/1',\n"
                            "    timeout=10,\n"
                            ")\n"
                            "response.raise_for_status()  # 4xx/5xx면 예외 발생 (중요!)\n\n"
                            "user = response.json()\n"
                            "print(user['name'])             # Leanne Graham\n"
                            "print(user['email'])            # Sincere@april.biz\n"
                            "print(user['address']['city'])  # 중첩 구조 접근\n"
                            "print(user['company']['name'])  # 깊은 중첩 접근\n\n\n"
                            "# 안전한 중첩 접근 (KeyError 방지)\n"
                            "city = user.get('address', {}).get('city', '알 수 없음')\n"
                            "print(f'도시: {city}')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "# 배열(리스트) 형태 응답 처리\n"
                            "response = requests.get(\n"
                            "    'https://jsonplaceholder.typicode.com/posts',\n"
                            "    params={'userId': 1},\n"
                            "    timeout=10,\n"
                            ")\n"
                            "response.raise_for_status()\n\n"
                            "posts = response.json()  # 리스트 반환\n"
                            "print(f'게시글 수: {len(posts)}')\n\n"
                            "# 리스트 컴프리헨션으로 필요한 필드만 추출\n"
                            "titles = [post['title'] for post in posts]\n"
                            "print('첫 번째 제목:', titles[0])\n\n"
                            "# 조건 필터링\n"
                            "long_posts = [\n"
                            "    post for post in posts\n"
                            "    if len(post['body']) > 100\n"
                            "]\n"
                            "print(f'긴 게시글: {len(long_posts)}개')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "def safe_api_call(url, params=None, timeout=10):\n"
                            "    \"\"\"API를 안전하게 호출하고 결과를 반환한다.\"\"\"\n"
                            "    try:\n"
                            "        response = requests.get(url, params=params, timeout=timeout)\n"
                            "        response.raise_for_status()\n"
                            "        return response.json()\n"
                            "    except requests.exceptions.HTTPError as e:\n"
                            "        print(f'HTTP 오류: {e.response.status_code} — {url}')\n"
                            "    except requests.exceptions.Timeout:\n"
                            "        print(f'타임아웃: {url}')\n"
                            "    except requests.exceptions.ConnectionError:\n"
                            "        print(f'연결 실패: {url}')\n"
                            "    except requests.exceptions.JSONDecodeError:\n"
                            "        print(f'JSON 파싱 오류: {url}')\n"
                            "    return None  # 실패 시 None 반환\n\n\n"
                            "# 사용 예\n"
                            "data = safe_api_call(\n"
                            "    'https://jsonplaceholder.typicode.com/todos/1'\n"
                            ")\n"
                            "if data:\n"
                            "    print(f'할 일: {data[\"title\"]} (완료: {data[\"completed\"]})')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "`response.raise_for_status()`는 상태 코드가 4xx 또는 5xx일 때 "
                            "자동으로 예외를 발생시킵니다. "
                            "이를 생략하면 오류 응답도 정상 처리되어 조용히 잘못된 결과를 낼 수 있습니다. "
                            "항상 응답 처리 전에 호출하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: API 키 인증과 헤더 설정 ─────────────────
            {
                "title": "API 키 인증과 헤더 설정",
                "content": [
                    "대부분의 실제 API는 무단 사용을 막기 위해 인증을 요구합니다. "
                    "API 키는 가장 일반적인 인증 방식으로, "
                    "헤더나 쿼리 파라미터로 전달합니다.",
                    {
                        "type": "table",
                        "headers": ["인증 방식", "전달 위치", "예시"],
                        "rows": [
                            ["API 키 (쿼리)", "URL 파라미터", "?api_key=YOUR_KEY"],
                            ["API 키 (헤더)", "Authorization 헤더", "Authorization: Bearer YOUR_KEY"],
                            ["API 키 (커스텀 헤더)", "커스텀 헤더", "X-API-Key: YOUR_KEY"],
                            ["Basic Auth", "Authorization 헤더", "Base64(user:password)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import os\n"
                            "import requests\n\n\n"
                            "# API 키는 환경변수에서 읽어야 합니다 (하드코딩 금지!)\n"
                            "API_KEY = os.environ.get('WEATHER_API_KEY', '')\n\n"
                            "if not API_KEY:\n"
                            "    raise ValueError('WEATHER_API_KEY 환경변수를 설정하세요')\n\n\n"
                            "# 방법 1: 쿼리 파라미터로 API 키 전달\n"
                            "params = {\n"
                            "    'q': '서울',\n"
                            "    'appid': API_KEY,\n"
                            "    'units': 'metric',  # 섭씨 온도\n"
                            "    'lang': 'kr',\n"
                            "}\n"
                            "# response = requests.get(\n"
                            "#     'https://api.openweathermap.org/data/2.5/weather',\n"
                            "#     params=params,\n"
                            "#     timeout=10,\n"
                            "# )\n\n\n"
                            "# 방법 2: Authorization 헤더로 API 키 전달\n"
                            "GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')\n"
                            "headers = {\n"
                            "    'Authorization': f'Bearer {GITHUB_TOKEN}',\n"
                            "    'Accept': 'application/vnd.github.v3+json',\n"
                            "    'X-GitHub-Api-Version': '2022-11-28',\n"
                            "}\n"
                            "response = requests.get(\n"
                            "    'https://api.github.com/user',\n"
                            "    headers=headers,\n"
                            "    timeout=10,\n"
                            ")\n"
                            "if response.status_code == 200:\n"
                            "    print(response.json()['login'])  # GitHub 사용자명"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import os\n"
                            "import requests\n\n\n"
                            "# Session 객체: 헤더를 한 번만 설정하고 재사용\n"
                            "GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')\n\n"
                            "session = requests.Session()\n"
                            "session.headers.update({\n"
                            "    'Authorization': f'Bearer {GITHUB_TOKEN}',\n"
                            "    'Accept': 'application/vnd.github.v3+json',\n"
                            "})\n\n"
                            "# 이후 모든 요청에 자동으로 헤더 포함\n"
                            "user = session.get('https://api.github.com/user', timeout=10)\n"
                            "repos = session.get('https://api.github.com/user/repos', timeout=10)\n\n"
                            "# Session은 TCP 연결도 재사용 → 성능 향상\n"
                            "session.close()  # 사용 후 닫기\n\n\n"
                            "# with 문으로 자동 close\n"
                            "with requests.Session() as s:\n"
                            "    s.headers.update({'Authorization': f'Bearer {GITHUB_TOKEN}'})\n"
                            "    result = s.get('https://api.github.com/user', timeout=10)\n"
                            "    print(result.json())"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "API 키를 코드에 직접 작성하지 마세요! "
                            "GitHub에 올리면 자동 봇이 수 초 만에 발견해 악용합니다. "
                            "항상 환경변수(os.environ)나 .env 파일(python-dotenv)을 사용하고, "
                            ".env 파일은 .gitignore에 추가하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 페이지네이션 처리 ─────────────────────────
            {
                "title": "페이지네이션 처리",
                "content": [
                    "API는 한 번에 모든 데이터를 반환하지 않습니다. "
                    "대용량 데이터는 페이지 단위로 나누어 제공합니다. "
                    "페이지네이션을 올바르게 처리해야 전체 데이터를 수집할 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["페이지네이션 방식", "설명", "예시"],
                        "rows": [
                            ["페이지 번호 방식", "page, per_page 파라미터", "?page=2&per_page=30"],
                            ["오프셋 방식", "offset, limit 파라미터", "?offset=30&limit=30"],
                            ["커서 방식", "next 커서 값 사용", "?cursor=abc123"],
                            ["Link 헤더 방식", "응답 헤더에 다음 URL", "Link: <url>; rel=\"next\""],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "def fetch_all_pages(base_url, params=None, max_pages=10):\n"
                            "    \"\"\"페이지네이션을 처리하며 전체 데이터를 수집한다.\"\"\"\n"
                            "    all_items = []\n"
                            "    page = 1\n"
                            "    params = dict(params or {})\n\n"
                            "    while page <= max_pages:\n"
                            "        params['page'] = page\n"
                            "        params['per_page'] = 30\n\n"
                            "        response = requests.get(base_url, params=params, timeout=10)\n"
                            "        response.raise_for_status()\n"
                            "        items = response.json()\n\n"
                            "        if not items:  # 빈 배열이면 마지막 페이지\n"
                            "            break\n\n"
                            "        all_items.extend(items)\n"
                            "        print(f'  페이지 {page}: {len(items)}건 수집')\n\n"
                            "        if len(items) < 30:  # 30건 미만이면 마지막 페이지\n"
                            "            break\n\n"
                            "        page += 1\n\n"
                            "    return all_items\n\n\n"
                            "# JSONPlaceholder로 테스트 (실제로는 페이지네이션 없음)\n"
                            "posts = fetch_all_pages(\n"
                            "    'https://jsonplaceholder.typicode.com/posts',\n"
                            ")\n"
                            "print(f'총 {len(posts)}개 수집 완료')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "def fetch_github_repos(username, token=None):\n"
                            "    \"\"\"GitHub Link 헤더 방식 페이지네이션 처리.\"\"\"\n"
                            "    headers = {}\n"
                            "    if token:\n"
                            "        headers['Authorization'] = f'Bearer {token}'\n\n"
                            "    url = f'https://api.github.com/users/{username}/repos'\n"
                            "    all_repos = []\n\n"
                            "    while url:  # next URL이 없으면 None → 루프 종료\n"
                            "        response = requests.get(\n"
                            "            url,\n"
                            "            params={'per_page': 30},\n"
                            "            headers=headers,\n"
                            "            timeout=10,\n"
                            "        )\n"
                            "        response.raise_for_status()\n"
                            "        all_repos.extend(response.json())\n\n"
                            "        # Link 헤더에서 next URL 추출\n"
                            "        links = response.links\n"
                            "        url = links.get('next', {}).get('url')  # 없으면 None\n\n"
                            "    return all_repos\n\n\n"
                            "# 사용 예 (공개 사용자)\n"
                            "# repos = fetch_github_repos('torvalds')\n"
                            "# print(f'저장소 수: {len(repos)}')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "페이지네이션 루프에는 항상 최대 페이지 수 제한(`max_pages`)을 두세요. "
                            "API 응답 오류나 무한 루프를 방지합니다. "
                            "또한 연속 요청 시 서버 부하를 줄이기 위해 "
                            "`time.sleep(0.5)` 같은 짧은 대기를 추가하는 것이 예의입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 ─────────────────────────────────
            {
                "title": "실용 예제: 공공 API와 GitHub API",
                "content": [
                    "배운 내용을 실제 API에 적용해봅니다. "
                    "공공 API로 날씨 데이터를 수집하고, "
                    "GitHub API로 저장소 정보를 분석하는 예제를 작성합니다.",
                    {
                        "type": "heading",
                        "text": "예제 1: OpenWeatherMap API로 날씨 데이터 수집",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import os\n"
                            "import requests\n\n\n"
                            "def get_weather(city, api_key):\n"
                            "    \"\"\"OpenWeatherMap API로 도시 날씨를 조회한다.\"\"\"\n"
                            "    url = 'https://api.openweathermap.org/data/2.5/weather'\n"
                            "    params = {\n"
                            "        'q': city,\n"
                            "        'appid': api_key,\n"
                            "        'units': 'metric',\n"
                            "        'lang': 'kr',\n"
                            "    }\n\n"
                            "    response = requests.get(url, params=params, timeout=10)\n\n"
                            "    if response.status_code == 401:\n"
                            "        raise ValueError('API 키가 유효하지 않습니다')\n"
                            "    if response.status_code == 404:\n"
                            "        raise ValueError(f'도시를 찾을 수 없습니다: {city}')\n\n"
                            "    response.raise_for_status()\n"
                            "    data = response.json()\n\n"
                            "    return {\n"
                            "        'city': data['name'],\n"
                            "        'temp': data['main']['temp'],\n"
                            "        'feels_like': data['main']['feels_like'],\n"
                            "        'humidity': data['main']['humidity'],\n"
                            "        'description': data['weather'][0]['description'],\n"
                            "        'wind_speed': data['wind']['speed'],\n"
                            "    }\n\n\n"
                            "# 사용 예\n"
                            "# api_key = os.environ['OPENWEATHER_API_KEY']\n"
                            "# weather = get_weather('Seoul', api_key)\n"
                            "# print(f\"{weather['city']}: {weather['temp']}°C, {weather['description']}\")\n"
                            "# print(f\"습도: {weather['humidity']}%, 풍속: {weather['wind_speed']}m/s\")"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "예제 2: GitHub API로 저장소 정보 분석",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import requests\n\n\n"
                            "def analyze_github_user(username):\n"
                            "    \"\"\"GitHub 사용자의 공개 저장소를 분석한다.\"\"\"\n"
                            "    url = f'https://api.github.com/users/{username}/repos'\n"
                            "    params = {'per_page': 100, 'sort': 'updated'}\n\n"
                            "    response = requests.get(url, params=params, timeout=10)\n"
                            "    response.raise_for_status()\n"
                            "    repos = response.json()\n\n"
                            "    if not repos:\n"
                            "        return {'username': username, 'repo_count': 0}\n\n"
                            "    # 언어별 저장소 수 집계\n"
                            "    lang_count = {}\n"
                            "    total_stars = 0\n\n"
                            "    for repo in repos:\n"
                            "        lang = repo.get('language') or '알 수 없음'\n"
                            "        lang_count[lang] = lang_count.get(lang, 0) + 1\n"
                            "        total_stars += repo.get('stargazers_count', 0)\n\n"
                            "    top_lang = max(lang_count, key=lang_count.get)\n\n"
                            "    return {\n"
                            "        'username': username,\n"
                            "        'repo_count': len(repos),\n"
                            "        'total_stars': total_stars,\n"
                            "        'top_language': top_lang,\n"
                            "        'languages': lang_count,\n"
                            "    }\n\n\n"
                            "# 공개 API (인증 불필요)\n"
                            "result = analyze_github_user('torvalds')\n"
                            "print(f\"사용자: {result['username']}\")\n"
                            "print(f\"저장소: {result['repo_count']}개\")\n"
                            "print(f\"스타 합계: {result['total_stars']}\")\n"
                            "print(f\"주 언어: {result['top_language']}\")"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "API 개발 중에는 실제 API 대신 "
                            "https://httpbin.org 또는 https://jsonplaceholder.typicode.com 을 "
                            "사용해 연습하세요. "
                            "이 서비스들은 실제 API 키 없이도 HTTP 요청/응답을 테스트할 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "API 키는 절대 코드에 직접 쓰지 말고 환경변수(os.environ)로 관리하세요.",
            "requests.get()에는 항상 timeout 매개변수를 지정해 무한 대기를 방지하세요.",
            "raise_for_status()를 항상 호출해 4xx/5xx 오류를 즉시 감지하세요.",
            "Session 객체를 사용하면 헤더를 한 번만 설정하고 TCP 연결도 재사용할 수 있습니다.",
            "페이지네이션 루프에는 최대 페이지 수 제한을 두어 무한 루프를 방지하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "HTTP GET 요청에서 쿼리 파라미터를 전달하는 올바른 방법은?",
                "choices": [
                    "A) requests.get(url, data={'key': 'value'})",
                    "B) requests.get(url, params={'key': 'value'})",
                    "C) requests.get(url, json={'key': 'value'})",
                    "D) requests.get(url, body={'key': 'value'})",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "API 응답이 4xx 또는 5xx일 때 자동으로 예외를 발생시키는 메서드는?",
                "choices": [
                    "A) response.check_status()",
                    "B) response.assert_ok()",
                    "C) response.raise_for_status()",
                    "D) response.verify()",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "API 키를 안전하게 관리하는 올바른 방법은?",
                "choices": [
                    "A) 코드 파일에 문자열로 직접 작성한다",
                    "B) 주석으로 숨겨서 작성한다",
                    "C) 환경변수로 설정하고 os.environ으로 읽는다",
                    "D) 별도의 변수 이름에 저장해 혼동을 방지한다",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "JSONPlaceholder API(https://jsonplaceholder.typicode.com/todos)에서 "
                    "userId=1인 할 일(todos) 목록을 가져와 "
                    "완료된 항목 수와 미완료 항목 수를 출력하는 함수 "
                    "`count_todos(user_id)`를 작성하세요."
                ),
                "hint": (
                    "params={'userId': user_id}로 필터링합니다. "
                    "각 항목의 'completed' 필드가 True이면 완료입니다. "
                    "sum(1 for t in todos if t['completed'])으로 완료 수를 셀 수 있습니다."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "requests.Session을 사용하여 GitHub API에서 "
                    "특정 사용자의 공개 저장소 이름 목록을 반환하는 "
                    "함수 `get_repo_names(username)`을 작성하세요. "
                    "오류 발생 시 빈 리스트를 반환해야 합니다."
                ),
                "hint": (
                    "with requests.Session() as s: 안에서 "
                    "s.headers.update({'Accept': 'application/vnd.github.v3+json'})를 설정합니다. "
                    "[r['name'] for r in response.json()]으로 이름 목록을 추출하세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "여러 도시의 날씨를 비교하는 프로그램을 작성하세요. "
                "OpenWeatherMap API(또는 테스트 시 Mock 데이터)를 사용하여 "
                "도시 목록(['서울', '부산', '인천', '대구', '광주'])의 "
                "현재 온도와 날씨를 수집하고, "
                "1) 온도순으로 정렬한 결과 출력, "
                "2) 평균 온도 계산, "
                "3) 결과를 weather_report.json 파일로 저장하는 기능을 구현하세요. "
                "API 호출 실패 시 해당 도시는 건너뛰고 계속 진행해야 합니다."
            ),
            "hint": (
                "각 도시마다 safe_api_call()을 호출하고 None이면 건너뜁니다. "
                "sorted(results, key=lambda x: x['temp'])으로 정렬합니다. "
                "결과는 json.dump(results, f, ensure_ascii=False, indent=2)로 저장하세요."
            ),
        },
        "summary": [
            "API는 프로그램 간 소통 규칙으로, REST API는 HTTP 메서드(GET/POST/PUT/DELETE)와 URL로 자원을 다룬다.",
            "requests 라이브러리로 HTTP 요청을 보내고, response.json()으로 JSON을 Python 객체로 변환한다.",
            "raise_for_status()와 timeout 매개변수는 안정적인 API 호출을 위한 필수 요소다.",
            "API 키는 환경변수로 관리하고 코드에 직접 작성하지 않는다.",
            "Session 객체는 헤더 재사용과 TCP 연결 재사용으로 코드를 간결하고 효율적으로 만든다.",
            "페이지네이션을 올바르게 처리해야 API의 전체 데이터를 수집할 수 있다.",
        ],
    }
