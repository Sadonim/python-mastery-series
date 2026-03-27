"""챕터 6: 정규표현식 — 텍스트를 자유자재로 다루는 도구."""


def get_chapter():
    """챕터 6 콘텐츠를 반환한다."""
    return {
        "number": 6,
        "title": "정규표현식",
        "subtitle": "텍스트를 자유자재로 다루는 도구",
        "big_picture": (
            "로그 파일에서 IP 주소를 찾고, 입력된 이메일이 유효한지 확인하고, "
            "전화번호 형식을 통일하는 일 — 이 모든 것을 몇 줄의 코드로 해결할 수 있다면 어떨까요? "
            "정규표현식(Regular Expression, Regex)은 텍스트 패턴을 기술하는 일종의 '미니 언어'입니다. "
            "복잡한 문자열 검색, 추출, 치환 작업을 간결하게 표현할 수 있어 "
            "데이터 처리, 로그 분석, 입력 검증 등 실무에서 매일 활용되는 핵심 기술입니다."
        ),
        "sections": [
            # ── 섹션 1: 정규표현식이란? ──────────────────────────
            {
                "title": "정규표현식이란 무엇인가",
                "content": [
                    "**정규표현식(Regular Expression)**은 문자열에서 특정 패턴을 나타내는 표기법입니다. "
                    "단순 문자열 검색과 달리, 규칙 기반으로 다양한 형태의 텍스트를 한 번에 처리할 수 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "정규표현식은 군대의 인원 점검 기준서 같은 것입니다. "
                            "'계급장이 붙어 있고, 이름표가 있고, 전투복을 입은 사람'이라는 규칙을 "
                            "만들어 두면, 수백 명 중에서 조건에 맞는 사람을 한 번에 찾을 수 있습니다. "
                            "정규표현식도 마찬가지입니다 — 패턴을 한 번 정의하면 "
                            "어떤 긴 텍스트에서도 그 패턴과 일치하는 부분을 찾아냅니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "왜 정규표현식이 필요한가",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 일반 문자열 방식: 이메일 형식 검사 (비효율적)\n"
                            "def is_valid_email_naive(email):\n"
                            "    if '@' not in email:\n"
                            "        return False\n"
                            "    parts = email.split('@')\n"
                            "    if len(parts) != 2:\n"
                            "        return False\n"
                            "    if '.' not in parts[1]:\n"
                            "        return False\n"
                            "    # ... 수십 줄 더 필요 ...\n"
                            "    return True\n\n"
                            "# 정규표현식 방식: 한 줄로 처리\n"
                            "import re\n\n"
                            "def is_valid_email(email):\n"
                            "    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\n"
                            "    return bool(re.match(pattern, email))"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "re 모듈 임포트",
                    },
                    "Python의 정규표현식 기능은 표준 라이브러리 `re` 모듈에 들어 있습니다. "
                    "별도 설치 없이 바로 사용할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 가장 기본적인 사용 예\n"
                            "text = '오늘 서울 날씨는 맑음입니다.'\n"
                            "result = re.search(r'서울', text)\n\n"
                            "if result:\n"
                            "    print('패턴 찾음:', result.group())  # 서울\n"
                            "    print('위치:', result.start(), '~', result.end())  # 3 ~ 5\n"
                            "else:\n"
                            "    print('패턴 없음')"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "패턴 문자열 앞에 `r`을 붙이면 '원시 문자열(raw string)'이 됩니다. "
                            "`\\n`을 줄바꿈이 아니라 백슬래시+n 그대로 전달하기 위해 "
                            "정규표현식에서는 항상 `r'패턴'` 형태로 작성하는 것을 권장합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: re 모듈 주요 함수 ────────────────────────
            {
                "title": "re 모듈 주요 함수",
                "content": [
                    "re 모듈에서 가장 많이 쓰이는 네 가지 함수를 익혀 봅시다. "
                    "각 함수는 목적이 다르므로 상황에 맞게 선택해야 합니다.",
                    {
                        "type": "table",
                        "headers": ["함수", "용도", "반환값"],
                        "rows": [
                            ["re.search()", "텍스트 전체에서 첫 번째 매치 찾기", "Match 객체 또는 None"],
                            ["re.match()", "문자열 시작 부분에서만 매치 확인", "Match 객체 또는 None"],
                            ["re.findall()", "모든 매치를 리스트로 반환", "문자열 리스트"],
                            ["re.sub()", "매치된 부분을 다른 문자열로 치환", "새 문자열"],
                            ["re.compile()", "패턴을 컴파일하여 객체로 저장", "Pattern 객체"],
                            ["re.split()", "패턴 기준으로 문자열 분리", "문자열 리스트"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "re.search() — 전체 검색",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "log = '2024-01-15 ERROR: 데이터베이스 연결 실패 (코드: 500)'\n\n"
                            "# 에러 코드 추출\n"
                            "match = re.search(r'코드: (\\d+)', log)\n"
                            "if match:\n"
                            "    print('에러 코드:', match.group(1))  # 500\n"
                            "    print('전체 매치:', match.group(0))  # 코드: 500\n\n"
                            "# search vs match 차이\n"
                            "text = '안녕하세요 Python 세계'\n"
                            "print(re.search(r'Python', text))   # Match 객체 (중간에 있어도 찾음)\n"
                            "print(re.match(r'Python', text))    # None (시작 부분에 없으므로)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "re.findall() — 모든 매치 수집",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 텍스트에서 모든 숫자 추출\n"
                            "report = '1분기: 1200만원, 2분기: 980만원, 3분기: 1450만원'\n"
                            "numbers = re.findall(r'\\d+', report)\n"
                            "print(numbers)  # ['1', '1200', '2', '980', '3', '1450']\n\n"
                            "# 특정 형식만 추출 (4자리 이상 숫자)\n"
                            "amounts = re.findall(r'\\d{3,}', report)\n"
                            "print(amounts)  # ['1200', '980', '1450']"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "re.sub() — 패턴 치환",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 전화번호 형식 통일 (하이픈 제거)\n"
                            "phones = '010-1234-5678 또는 010.9876.5432'\n"
                            "clean = re.sub(r'[-.\\s]', '', phones)\n"
                            "print(clean)  # 01012345678또는01098765432\n\n"
                            "# 개인정보 마스킹 (이름 뒤 가리기)\n"
                            "data = '김철수(25세), 이영희(30세), 박민수(22세)'\n"
                            "masked = re.sub(r'(\\S+)\\(\\d+세\\)', r'***', data)\n"
                            "print(masked)  # ***, ***, ***\n\n"
                            "# 치환 횟수 제한\n"
                            "text = 'aaa bbb aaa ccc aaa'\n"
                            "result = re.sub(r'aaa', 'XXX', text, count=2)\n"
                            "print(result)  # XXX bbb XXX ccc aaa"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "같은 패턴을 반복 사용한다면 `re.compile()`로 미리 컴파일하세요. "
                            "패턴 객체를 재사용하면 성능이 향상됩니다:\n"
                            "```\n"
                            "pattern = re.compile(r'\\d+')\n"
                            "pattern.findall('점수: 85, 92, 77')  # ['85', '92', '77']\n"
                            "```"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 기본 패턴과 메타문자 ─────────────────────
            {
                "title": "기본 패턴과 메타문자",
                "content": [
                    "정규표현식의 힘은 **메타문자**에서 나옵니다. "
                    "메타문자는 특수한 의미를 가진 문자로, "
                    "다양한 패턴을 간결하게 표현할 수 있게 해 줍니다.",
                    {
                        "type": "table",
                        "headers": ["메타문자", "의미", "예시"],
                        "rows": [
                            [".", "임의의 문자 1개 (줄바꿈 제외)", r"a.c → abc, a1c, a-c"],
                            ["^", "문자열 시작", r"^Hello → Hello로 시작"],
                            ["$", "문자열 끝", r"world$ → world로 끝"],
                            ["*", "0회 이상 반복", r"ab* → a, ab, abb, abbb"],
                            ["+", "1회 이상 반복", r"ab+ → ab, abb, abbb (a 제외)"],
                            ["?", "0회 또는 1회", r"colou?r → color, colour"],
                            ["{n}", "정확히 n회 반복", r"\\d{4} → 4자리 숫자"],
                            ["{n,m}", "n회 이상 m회 이하 반복", r"\\d{2,4} → 2~4자리 숫자"],
                            ["[]", "문자 클래스 (중 하나)", r"[aeiou] → 모음 한 글자"],
                            ["|", "OR 연산", r"cat|dog → cat 또는 dog"],
                            ["\\", "메타문자 이스케이프", r"\\. → 마침표 그 자체"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "문자 클래스 [ ]",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 모음 찾기\n"
                            "text = 'Python Programming'\n"
                            "vowels = re.findall(r'[aeiouAEIOU]', text)\n"
                            "print(vowels)  # ['o', 'o', 'a', 'i']\n\n"
                            "# 범위 지정: [a-z], [0-9], [A-Za-z0-9]\n"
                            "alphanumeric = re.findall(r'[A-Za-z0-9]+', 'Hello, 123 World!')\n"
                            "print(alphanumeric)  # ['Hello', '123', 'World']\n\n"
                            "# ^ 를 [ ] 안에 쓰면 '제외' 의미\n"
                            "no_digits = re.sub(r'[^0-9]', '', '전화: 010-1234-5678')\n"
                            "print(no_digits)  # 01012345678"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "수량자와 반복",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# {n,m} 으로 자릿수 제어\n"
                            "texts = ['12', '123', '1234', '12345']\n"
                            "for t in texts:\n"
                            "    match = re.fullmatch(r'\\d{3,4}', t)  # 3~4자리만\n"
                            "    print(f'{t}: {\"✓\" if match else \"✗\"}')\n"
                            "# 12: ✗\n"
                            "# 123: ✓\n"
                            "# 1234: ✓\n"
                            "# 12345: ✗\n\n"
                            "# ? 로 선택적 매칭\n"
                            "pattern = r'https?://\\S+'  # http 또는 https\n"
                            "urls = re.findall(pattern, 'http://example.com https://secure.com')\n"
                            "print(urls)  # ['http://example.com', 'https://secure.com']"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "`.`(점)은 정규표현식에서 '임의의 한 글자'를 의미합니다. "
                            "실제 마침표를 매칭하려면 반드시 `\\.`으로 이스케이프하세요. "
                            "`re.search(r'www.naver.com', text)` 는 "
                            "'wwwXnaverYcom' 도 매칭해 버립니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 특수 시퀀스와 그룹핑 ─────────────────────
            {
                "title": "특수 시퀀스와 그룹핑",
                "content": [
                    "자주 쓰이는 패턴을 위한 **특수 시퀀스**와, "
                    "매치된 일부분만 추출하기 위한 **그룹핑** 기법을 익혀 봅시다.",
                    {
                        "type": "table",
                        "headers": ["시퀀스", "의미", "반대 (대문자)"],
                        "rows": [
                            ["\\d", "숫자 [0-9]", "\\D — 숫자가 아닌 것"],
                            ["\\w", "단어 문자 [a-zA-Z0-9_]", "\\W — 단어 문자가 아닌 것"],
                            ["\\s", "공백 문자 (스페이스, 탭, 줄바꿈)", "\\S — 공백이 아닌 것"],
                            ["\\b", "단어 경계", "\\B — 단어 경계가 아닌 곳"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "text = 'ID: user_123, 점수: 95점, 시간: 12:30'\n\n"
                            "# \\d: 숫자 추출\n"
                            "digits = re.findall(r'\\d+', text)\n"
                            "print('숫자들:', digits)  # ['123', '95', '12', '30']\n\n"
                            "# \\w: 단어 문자 (영문+숫자+밑줄)\n"
                            "words = re.findall(r'\\w+', 'hello world_2 test-3')\n"
                            "print('단어들:', words)  # ['hello', 'world_2', 'test', '3']\n\n"
                            "# \\b: 단어 경계 (정확한 단어만 찾기)\n"
                            "sent = 'cat catfish cats'\n"
                            "exact = re.findall(r'\\bcat\\b', sent)\n"
                            "print('정확한 cat:', exact)  # ['cat'] (catfish, cats 제외)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "캡처 그룹 ( )",
                    },
                    "괄호 `()`로 묶인 부분은 **캡처 그룹**이 됩니다. "
                    "매치된 전체 문자열 중 특정 부분만 추출할 때 사용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 날짜 파싱: 연-월-일 분리\n"
                            "date_str = '2024-03-15'\n"
                            "match = re.search(r'(\\d{4})-(\\d{2})-(\\d{2})', date_str)\n\n"
                            "if match:\n"
                            "    print('전체:', match.group(0))   # 2024-03-15\n"
                            "    print('연도:', match.group(1))   # 2024\n"
                            "    print('월:', match.group(2))     # 03\n"
                            "    print('일:', match.group(3))     # 15\n\n"
                            "# 네임드 그룹 (?P<name>...) 으로 이름 붙이기\n"
                            "match = re.search(\n"
                            "    r'(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})',\n"
                            "    date_str\n"
                            ")\n"
                            "if match:\n"
                            "    print('연도:', match.group('year'))   # 2024\n"
                            "    print('월:', match.group('month'))    # 03"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "비캡처 그룹 (?:...)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 그룹핑은 하지만 캡처는 하지 않을 때\n"
                            "# 예: 'Mr.' 또는 'Ms.' 접두사를 허용하되 이름만 추출\n"
                            "text = 'Mr. Kim과 Ms. Lee가 참석합니다.'\n\n"
                            "# 캡처 그룹 사용: 접두사도 같이 잡힘\n"
                            "names1 = re.findall(r'(?:Mr\\.|Ms\\.) (\\w+)', text)\n"
                            "print('이름:', names1)  # ['Kim', 'Lee']\n\n"
                            "# findall에서 그룹이 있으면 그룹 내용만 반환됨\n"
                            "# 그룹이 여러 개면 튜플로 반환\n"
                            "log = 'ERROR 500: 서버 오류 | INFO 200: 성공'\n"
                            "pairs = re.findall(r'(\\w+) (\\d+)', log)\n"
                            "print(pairs)  # [('ERROR', '500'), ('INFO', '200')]"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "그룹을 사용할 때 `re.findall()`의 동작:\n"
                            "- 그룹 없음: 매치된 전체 문자열 리스트 반환\n"
                            "- 그룹 1개: 해당 그룹의 문자열 리스트 반환\n"
                            "- 그룹 여러 개: 각 그룹이 담긴 튜플의 리스트 반환"
                        ),
                    },
                ],
            },
            # ── 섹션 5: 탐욕적 vs 비탐욕적 매칭 ─────────────────
            {
                "title": "탐욕적 vs 비탐욕적 매칭",
                "content": [
                    "기본적으로 정규표현식의 수량자(`*`, `+`, `?`)는 **탐욕적(greedy)**입니다. "
                    "가능한 한 많이 매칭하려는 성질이 있습니다. "
                    "뒤에 `?`를 붙이면 **비탐욕적(non-greedy, lazy)** 모드가 됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "html = '<b>첫 번째</b> 텍스트 <b>두 번째</b>'\n\n"
                            "# 탐욕적 매칭: 최대한 많이 매칭\n"
                            "greedy = re.findall(r'<b>.*</b>', html)\n"
                            "print('탐욕적:', greedy)\n"
                            "# ['<b>첫 번째</b> 텍스트 <b>두 번째</b>'] — 너무 많이 먹음!\n\n"
                            "# 비탐욕적 매칭: 가능한 한 적게 매칭\n"
                            "lazy = re.findall(r'<b>.*?</b>', html)\n"
                            "print('비탐욕적:', lazy)\n"
                            "# ['<b>첫 번째</b>', '<b>두 번째</b>'] — 원하는 결과!"
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "탐욕적 .*"},
                            {"label": "전체 텍스트 소비", "color": "#f04452"},
                            {"label": "오른쪽에서 한 글자씩 반납"},
                            {"label": "패턴 완성 시 중단"},
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 탐욕적 vs 비탐욕적 비교 표\n"
                            "text = 'aXbXcXd'\n\n"
                            "print(re.search(r'a.*d', text).group())    # aXbXcXd (탐욕적)\n"
                            "print(re.search(r'a.*?d', text).group())   # aXbXcXd (같음 — 여기선 d가 하나)\n\n"
                            "text2 = 'start...end...end2'\n"
                            "print(re.search(r'start.*end', text2).group())   # start...end...end2\n"
                            "print(re.search(r'start.*?end', text2).group())  # start...end"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "HTML/XML 파싱에서 태그 내용을 추출할 때는 항상 비탐욕적 `.*?`를 사용하세요. "
                            "탐욕적 `.*`는 생각보다 너무 많은 내용을 가져올 수 있습니다. "
                            "단, 실제 HTML 파싱에는 BeautifulSoup 같은 전용 라이브러리가 더 적합합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 ─────────────────────────────────
            {
                "title": "실용 예제: 이메일 검증, 전화번호, 로그 파싱",
                "content": [
                    "지금까지 배운 내용을 실제 문제에 적용해 봅시다. "
                    "이메일 검증, 전화번호 추출, 서버 로그 파싱은 "
                    "실무에서 가장 자주 마주치는 정규표현식 활용 사례입니다.",
                    {
                        "type": "heading",
                        "text": "이메일 주소 검증",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 이메일 검증 패턴\n"
                            "# - 로컬 파트: 영문/숫자/특수문자(._+-)\n"
                            "# - @ 기호\n"
                            "# - 도메인: 영문/숫자/하이픈\n"
                            "# - 최상위 도메인: 2글자 이상\n"
                            "EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'\n\n"
                            "test_emails = [\n"
                            "    'user@example.com',      # ✓ 유효\n"
                            "    'hong.gildong@mil.kr',   # ✓ 유효\n"
                            "    'invalid@',              # ✗ 도메인 없음\n"
                            "    '@nodomain.com',         # ✗ 로컬 파트 없음\n"
                            "    'no spaces@test.com',    # ✗ 공백 포함\n"
                            "]\n\n"
                            "for email in test_emails:\n"
                            "    valid = bool(re.match(EMAIL_PATTERN, email))\n"
                            "    status = '유효' if valid else '무효'\n"
                            "    print(f'{email:<30} → {status}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "전화번호 추출 및 정규화",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "def extract_phone_numbers(text):\n"
                            "    \"\"\"텍스트에서 한국 전화번호를 모두 추출하여 정규화된 형태로 반환한다.\"\"\"\n"
                            "    # 010-1234-5678, 010.1234.5678, 01012345678 모두 허용\n"
                            "    pattern = r'01[016789][-.\\s]?\\d{3,4}[-.\\s]?\\d{4}'\n"
                            "    matches = re.findall(pattern, text)\n\n"
                            "    # 정규화: 숫자만 남기고 하이픈 형식으로\n"
                            "    normalized = []\n"
                            "    for m in matches:\n"
                            "        digits = re.sub(r'[^\\d]', '', m)  # 숫자만 추출\n"
                            "        # 010-XXXX-XXXX 또는 010-XXX-XXXX\n"
                            "        if len(digits) == 11:\n"
                            "            formatted = f'{digits[:3]}-{digits[3:7]}-{digits[7:]}'\n"
                            "        else:\n"
                            "            formatted = f'{digits[:3]}-{digits[3:6]}-{digits[6:]}'\n"
                            "        normalized.append(formatted)\n\n"
                            "    return normalized\n\n"
                            "# 테스트\n"
                            "text = '연락처: 010-1234-5678 또는 010.9876.5432, 비상연락: 01099998888'\n"
                            "phones = extract_phone_numbers(text)\n"
                            "print('추출된 전화번호:', phones)\n"
                            "# ['010-1234-5678', '010-9876-5432', '010-9999-8888']"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "서버 로그 파싱",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n"
                            "from collections import defaultdict\n\n"
                            "def parse_access_log(log_text):\n"
                            "    \"\"\"\n"
                            "    Apache/Nginx 접근 로그에서 상태 코드별 통계를 추출한다.\n"
                            "    형식: IP - - [날짜] \"메서드 경로 프로토콜\" 상태코드 바이트수\n"
                            "    \"\"\"\n"
                            "    # 네임드 그룹으로 각 필드 추출\n"
                            "    pattern = (\n"
                            "        r'(?P<ip>\\d+\\.\\d+\\.\\d+\\.\\d+).*?'\n"
                            "        r'\"(?P<method>\\w+) (?P<path>\\S+).*?\"\\s'\n"
                            "        r'(?P<status>\\d{3})\\s(?P<bytes>\\d+)'\n"
                            "    )\n\n"
                            "    stats = defaultdict(int)\n"
                            "    errors = []\n\n"
                            "    for line in log_text.strip().split('\\n'):\n"
                            "        m = re.search(pattern, line)\n"
                            "        if m:\n"
                            "            status = m.group('status')\n"
                            "            stats[status] += 1\n"
                            "            if status.startswith('5'):  # 5xx 에러\n"
                            "                errors.append({\n"
                            "                    'ip': m.group('ip'),\n"
                            "                    'path': m.group('path'),\n"
                            "                    'status': status,\n"
                            "                })\n\n"
                            "    return dict(stats), errors\n\n\n"
                            "# 예제 로그\n"
                            "sample_log = \"\"\"\n"
                            "192.168.1.1 - - [15/Jan/2024] \"GET /index.html HTTP/1.1\" 200 1234\n"
                            "10.0.0.5 - - [15/Jan/2024] \"POST /api/login HTTP/1.1\" 200 567\n"
                            "172.16.0.3 - - [15/Jan/2024] \"GET /missing HTTP/1.1\" 404 89\n"
                            "192.168.1.2 - - [15/Jan/2024] \"GET /api/data HTTP/1.1\" 500 45\n"
                            "\"\"\"\n\n"
                            "stats, errors = parse_access_log(sample_log)\n"
                            "print('상태 코드 통계:', stats)\n"
                            "# {'200': 2, '404': 1, '500': 1}\n"
                            "print('5xx 에러 목록:', errors)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "정규표현식 플래그(flag)도 활용하면 더 강력합니다:\n"
                            "- `re.IGNORECASE` (또는 `re.I`): 대소문자 무시\n"
                            "- `re.MULTILINE` (또는 `re.M`): ^와 $가 각 줄의 시작/끝에 매칭\n"
                            "- `re.DOTALL` (또는 `re.S`): `.`이 줄바꿈도 포함\n\n"
                            "예: `re.findall(r'error', log, re.IGNORECASE)` — "
                            "ERROR, Error, error 모두 찾음"
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "regex101.com 사이트를 활용하세요. 패턴을 실시간으로 테스트하고 각 부분의 의미를 시각적으로 확인할 수 있습니다.",
            "원시 문자열 r''을 항상 사용하세요. 백슬래시 이스케이프 문제를 예방합니다.",
            "패턴이 복잡해지면 `re.VERBOSE` 플래그를 쓰고 주석을 달아 가독성을 높이세요.",
            "HTML 파싱에는 정규표현식보다 BeautifulSoup이 훨씬 안정적입니다. 적절한 도구를 선택하세요.",
            "프로덕션 코드에서 반복 사용되는 패턴은 모듈 수준에서 `re.compile()`로 미리 컴파일해 두세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 re.match()와 re.search()의 차이를 올바르게 설명한 것은?",
                "choices": [
                    "A) match는 패턴을 전체 문자열과 비교하고, search는 부분 매칭을 허용한다.",
                    "B) match는 문자열의 시작 부분에서만 찾고, search는 전체에서 찾는다.",
                    "C) match는 모든 매치를 반환하고, search는 첫 번째만 반환한다.",
                    "D) 두 함수는 동일하며 성능만 다르다.",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": r"패턴 r'\d{3}-\d{4}'가 매칭하는 것은?",
                "choices": [
                    "A) 777-777777",
                    "B) 123-4567",
                    "C) 12-3456",
                    "D) 1234-567",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "문자열에서 'YYYY-MM-DD' 형식의 날짜를 모두 찾아 리스트로 반환하는 "
                    "함수 `extract_dates(text)`를 작성하세요. "
                    "예: '보고서 날짜: 2024-01-15, 제출일: 2024-03-20' → "
                    "['2024-01-15', '2024-03-20']"
                ),
                "hint": r"r'\d{4}-\d{2}-\d{2}' 패턴과 re.findall()을 사용하세요.",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "주민등록번호 형식(XXXXXX-XXXXXXX)을 마스킹하는 함수 "
                    "`mask_id(text)`를 작성하세요. "
                    "뒷자리 7자리를 '*'로 대체합니다. "
                    "예: '홍길동 900101-1234567' → '홍길동 900101-*******'"
                ),
                "hint": r"r'(\d{6})-\d{7}' 패턴과 re.sub()를 사용하고, 그룹 참조 r'\1-*******'로 치환하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "로그 문자열 리스트에서 'ERROR' 레벨 로그만 추출하는 "
                    "함수 `filter_errors(logs)`를 작성하세요. "
                    "로그 형식: '[LEVEL] 메시지'. "
                    "대소문자를 구분하지 않아야 합니다."
                ),
                "hint": r"r'^\[ERROR\]' 패턴과 re.IGNORECASE 플래그, re.match()를 사용하세요.",
            },
        ],
        "challenge": {
            "question": (
                "텍스트에서 URL을 모두 추출하여 도메인별로 그룹화하는 함수 "
                "`group_urls_by_domain(text)`를 작성하세요. "
                "반환 형태는 딕셔너리: {도메인: [URL 리스트]}. "
                "예를 들어 'https://news.naver.com/abc', 'http://sports.naver.com/xyz', "
                "'https://google.com/search' 가 있다면 "
                "{'naver.com': ['https://news.naver.com/abc', 'http://sports.naver.com/xyz'], "
                "'google.com': ['https://google.com/search']} 를 반환합니다."
            ),
            "hint": (
                "URL 패턴: r'https?://[\\w.-]+/\\S*'. "
                "도메인 추출에는 네임드 그룹 또는 별도 패턴 적용. "
                "최상위 도메인(naver.com, google.com) 기준으로 그룹화하려면 "
                "마지막 두 파트(domain.tld)를 추출하세요. "
                "collections.defaultdict(list)를 활용하면 편리합니다."
            ),
        },
        "summary": [
            "정규표현식은 텍스트 패턴을 기술하는 미니 언어로, Python의 re 모듈로 사용한다.",
            "주요 함수: search()(전체 검색), match()(시작 검색), findall()(전체 수집), sub()(치환).",
            "메타문자 `.`, `*`, `+`, `?`, `{n,m}`, `[]`, `|`, `^`, `$`로 다양한 패턴을 표현한다.",
            "특수 시퀀스: \\d(숫자), \\w(단어 문자), \\s(공백), \\b(단어 경계) — 대문자는 반대 의미.",
            "그룹 `()`: 매치 내 특정 부분만 추출. 네임드 그룹 `(?P<name>...)`으로 이름을 붙일 수 있다.",
            "탐욕적 매칭(기본)은 최대한 많이 소비. `*?`, `+?`처럼 `?`를 추가하면 비탐욕적으로 전환된다.",
        ],
    }
