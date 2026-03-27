"""Chapter 7: 문자열 심화 — 텍스트 마스터하기"""


def get_chapter():
    return {
        "number": 7,
        "title": "문자열 심화",
        "subtitle": "텍스트 마스터하기",
        "big_picture": (
            "프로그래밍에서 다루는 데이터의 대부분은 텍스트입니다. "
            "로그 분석, 데이터 전처리, 사용자 입력 검증 등 "
            "거의 모든 작업에서 문자열을 능숙하게 다루는 능력이 필요합니다. "
            "이 장에서는 문자열의 본질부터 정규표현식까지 깊이 있게 다룹니다."
        ),
        "sections": [
            # ── 섹션 1: 문자열의 본질 ──────────────────────
            {
                "title": "문자열의 본질",
                "content": [
                    "Python의 문자열(`str`)은 **불변(immutable) 시퀀스**입니다. "
                    "한 번 만들어지면 내부의 글자를 바꿀 수 없으며, "
                    "수정하면 항상 새로운 문자열이 만들어집니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "문자열은 돌에 새긴 글자와 같습니다. "
                            "한 글자를 고치고 싶으면 돌을 깎을 수 없으니, "
                            "새 돌에 처음부터 다시 새겨야 합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 문자열은 시퀀스 — 인덱싱과 반복 가능\n"
                            "인사 = '안녕하세요'\n"
                            "print(인사[0])    # '안'\n"
                            "print(인사[-1])   # '요'\n"
                            "print(len(인사))  # 5\n\n"
                            "# 글자 하나씩 순회\n"
                            "for 글자 in 인사:\n"
                            "    print(글자, end=' ')  # 안 녕 하 세 요"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 문자열은 불변 — 수정 불가\n"
                            "텍스트 = 'Hello'\n"
                            "# 텍스트[0] = 'h'  # TypeError 발생!\n\n"
                            "# 새 문자열을 만들어야 합니다\n"
                            "새_텍스트 = 'h' + 텍스트[1:]\n"
                            "print(새_텍스트)  # 'hello'"
                        ),
                    },
                    {"type": "heading", "text": "유니코드 기초"},
                    "Python 3의 문자열은 유니코드(Unicode)를 기본으로 사용합니다. "
                    "한글, 이모지, 일본어 등 전 세계 문자를 자연스럽게 처리할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 유니코드 — 모든 문자를 다룰 수 있습니다\n"
                            "한글 = '파이썬'\n"
                            "일본어 = 'パイソン'\n"
                            "이모지 = '🐍🎉'\n\n"
                            "# 유니코드 코드포인트 확인\n"
                            "print(ord('가'))    # 44032\n"
                            "print(chr(44032))   # '가'"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python 3에서 문자열은 유니코드 문자의 나열이고, "
                            "바이트열(bytes)과는 다릅니다. "
                            "파일이나 네트워크에서는 바이트로 변환(인코딩)이 필요합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: f-string 포매팅 ──────────────────
            {
                "title": "f-string 포매팅",
                "content": [
                    "f-string은 Python 3.6에서 도입된 문자열 포매팅 방법으로, "
                    "가장 직관적이고 빠릅니다. 문자열 앞에 `f`를 붙이고 "
                    "중괄호 `{}` 안에 변수나 표현식을 넣습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "f-string은 빈칸 채우기 시험지와 같습니다. "
                            "'나의 이름은 ___입니다'에서 빈칸에 답을 쓰듯, "
                            "중괄호 자리에 값이 자동으로 채워집니다."
                        ),
                    },
                    {"type": "heading", "text": "기본 사용법"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 f-string\n"
                            "이름 = '김철수'\n"
                            "나이 = 20\n"
                            "print(f'이름: {이름}, 나이: {나이}세')\n"
                            "# 출력: 이름: 김철수, 나이: 20세\n\n"
                            "# 표현식도 가능\n"
                            "print(f'내년 나이: {나이 + 1}세')\n"
                            "print(f'이름 길이: {len(이름)}글자')"
                        ),
                    },
                    {"type": "heading", "text": "정렬과 채움"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 정렬: < 왼쪽, > 오른쪽, ^ 가운데\n"
                            "항목 = '사과'\n"
                            "print(f'|{항목:<10}|')   # |사과        |\n"
                            "print(f'|{항목:>10}|')   # |        사과|\n"
                            "print(f'|{항목:^10}|')   # |    사과    |\n\n"
                            "# 채움 문자 지정\n"
                            "print(f'|{항목:*^10}|')  # |****사과****|"
                        ),
                    },
                    {"type": "heading", "text": "숫자 포매팅"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 소수점 자릿수\n"
                            "파이 = 3.141592653589793\n"
                            "print(f'파이 = {파이:.2f}')     # 파이 = 3.14\n"
                            "print(f'파이 = {파이:.4f}')     # 파이 = 3.1416\n\n"
                            "# 천 단위 구분\n"
                            "가격 = 1234567\n"
                            "print(f'가격: {가격:,}원')       # 가격: 1,234,567원\n\n"
                            "# 퍼센트\n"
                            "비율 = 0.856\n"
                            "print(f'정확도: {비율:.1%}')    # 정확도: 85.6%"
                        ),
                    },
                    {"type": "heading", "text": "디버깅용 f-string (Python 3.8+)"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 변수명=값 형태로 출력 (디버깅에 유용)\n"
                            "x = 42\n"
                            "이름 = '철수'\n"
                            "print(f'{x=}')      # x=42\n"
                            "print(f'{이름=}')    # 이름='철수'\n"
                            "print(f'{x * 2=}')  # x * 2=84"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "f\"{변수=}\" 문법은 디버깅할 때 print 문 작성 시간을 "
                            "크게 줄여줍니다. 변수명과 값이 함께 나와서 "
                            "어떤 값인지 바로 알 수 있습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["포맷 코드", "의미", "예시"],
                        "rows": [
                            [".2f", "소수점 둘째 자리", "3.14"],
                            [",", "천 단위 쉼표", "1,234,567"],
                            [".1%", "퍼센트 (소수 1자리)", "85.6%"],
                            ["<10", "왼쪽 정렬 (10칸)", "사과      "],
                            [">10", "오른쪽 정렬 (10칸)", "      사과"],
                            ["^10", "가운데 정렬 (10칸)", "    사과    "],
                        ],
                    },
                ],
            },
            # ── 섹션 3: 문자열 메서드 총정리 ────────────
            {
                "title": "문자열 메서드 총정리",
                "content": [
                    "Python 문자열은 수십 가지 내장 메서드를 제공합니다. "
                    "모두 외울 필요는 없고, 카테고리별로 주요 메서드를 기억해 두세요.",
                    {"type": "heading", "text": "검색/탐색 메서드"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "텍스트 = 'Hello, Python World!'\n\n"
                            "# 찾기\n"
                            "print(텍스트.find('Python'))      # 7 (시작 인덱스)\n"
                            "print(텍스트.find('Java'))        # -1 (없으면 -1)\n"
                            "print(텍스트.count('l'))          # 3 (등장 횟수)\n\n"
                            "# 시작/끝 확인\n"
                            "print(텍스트.startswith('Hello'))  # True\n"
                            "print(텍스트.endswith('!'))        # True"
                        ),
                    },
                    {"type": "heading", "text": "변환 메서드"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "텍스트 = '  Hello, World!  '\n\n"
                            "# 대소문자 변환\n"
                            "print(텍스트.upper())    # '  HELLO, WORLD!  '\n"
                            "print(텍스트.lower())    # '  hello, world!  '\n"
                            "print('hello'.capitalize())  # 'Hello'\n"
                            "print('hello world'.title())  # 'Hello World'\n\n"
                            "# 공백 제거\n"
                            "print(텍스트.strip())    # 'Hello, World!'  (양쪽)\n"
                            "print(텍스트.lstrip())   # 'Hello, World!  '  (왼쪽)\n"
                            "print(텍스트.rstrip())   # '  Hello, World!'  (오른쪽)"
                        ),
                    },
                    {"type": "heading", "text": "분리/결합 메서드"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# split: 문자열 → 리스트\n"
                            "csv_행 = '이름,나이,전공'\n"
                            "항목들 = csv_행.split(',')  # ['이름', '나이', '전공']\n\n"
                            "# join: 리스트 → 문자열\n"
                            "단어들 = ['Python', 'is', 'fun']\n"
                            "문장 = ' '.join(단어들)   # 'Python is fun'\n"
                            "경로 = '/'.join(['home', 'user', 'docs'])  # 'home/user/docs'\n\n"
                            "# replace: 치환\n"
                            "원본 = '나는 Java를 좋아한다'\n"
                            "수정 = 원본.replace('Java', 'Python')\n"
                            "print(수정)  # '나는 Python를 좋아한다'"
                        ),
                    },
                    {"type": "heading", "text": "판별 메서드"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 문자열 내용 판별\n"
                            "print('12345'.isdigit())    # True (숫자만?)\n"
                            "print('abc'.isalpha())      # True (문자만?)\n"
                            "print('abc123'.isalnum())   # True (문자+숫자만?)\n"
                            "print('   '.isspace())      # True (공백만?)\n"
                            "print('Hello'.isupper())    # False\n"
                            "print('HELLO'.isupper())    # True"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["카테고리", "메서드", "설명"],
                        "rows": [
                            ["검색", "find(s)", "s의 시작 인덱스 (-1 if 없음)"],
                            ["검색", "count(s)", "s의 등장 횟수"],
                            ["검색", "startswith(s)", "s로 시작하는지 (bool)"],
                            ["검색", "endswith(s)", "s로 끝나는지 (bool)"],
                            ["변환", "upper() / lower()", "대문자/소문자 변환"],
                            ["변환", "strip()", "양쪽 공백 제거"],
                            ["변환", "replace(a, b)", "a를 b로 치환"],
                            ["분리", "split(sep)", "sep 기준으로 분리 → 리스트"],
                            ["결합", "join(리스트)", "리스트를 문자열로 결합"],
                            ["판별", "isdigit()", "숫자로만 이루어졌는지"],
                            ["판별", "isalpha()", "문자로만 이루어졌는지"],
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            "문자열 메서드는 항상 새 문자열을 반환합니다. "
                            "원본은 변하지 않으므로, 결과를 변수에 저장해야 합니다. "
                            "텍스트.upper()를 호출해도 텍스트 자체는 바뀌지 않습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 슬라이싱 마스터 ──────────────────
            {
                "title": "슬라이싱 마스터",
                "content": [
                    "슬라이싱은 시퀀스(문자열, 리스트 등)의 일부를 잘라내는 강력한 기능입니다. "
                    "`[start:stop:step]` 세 가지 값으로 세밀하게 제어할 수 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "슬라이싱은 줄자로 천을 자르는 것과 같습니다. "
                            "시작 지점, 끝 지점, 간격을 정하면 "
                            "원하는 부분만 정확히 잘라낼 수 있습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 슬라이싱: [시작:끝]\n"
                            "텍스트 = 'ABCDEFGHIJ'\n"
                            "#         0123456789\n\n"
                            "print(텍스트[2:5])    # 'CDE'  (2번부터 4번까지)\n"
                            "print(텍스트[:4])     # 'ABCD' (처음부터 3번까지)\n"
                            "print(텍스트[6:])     # 'GHIJ' (6번부터 끝까지)\n"
                            "print(텍스트[:])      # 'ABCDEFGHIJ' (전체 복사)"
                        ),
                    },
                    {"type": "heading", "text": "step 활용"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "텍스트 = 'ABCDEFGHIJ'\n\n"
                            "# step: 간격 지정\n"
                            "print(텍스트[::2])    # 'ACEGI'  (2칸씩 건너뛰기)\n"
                            "print(텍스트[1::2])   # 'BDFHJ'  (1번부터 2칸씩)\n\n"
                            "# 역순\n"
                            "print(텍스트[::-1])   # 'JIHGFEDCBA'  (뒤집기)\n"
                            "print(텍스트[7:2:-1]) # 'HGFED'  (7번부터 3번까지 역순)"
                        ),
                    },
                    {"type": "heading", "text": "실용적인 슬라이싱 패턴"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 회문(팰린드롬) 검사\n"
                            "단어 = '토마토'\n"
                            "print(단어 == 단어[::-1])  # True (뒤집어도 같다)\n\n"
                            "# 파일 확장자 추출\n"
                            "파일명 = 'report_2024.pdf'\n"
                            "확장자 = 파일명[파일명.rfind('.'):]\n"
                            "print(확장자)  # '.pdf'\n\n"
                            "# 문자열 복사 (새 객체 생성)\n"
                            "원본 = 'Hello'\n"
                            "복사본 = 원본[:]"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["양수 인덱스", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        "rows": [
                            ["문자", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
                            ["음수 인덱스", "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "슬라이싱에서 끝(stop) 인덱스의 요소는 포함되지 않습니다. "
                            "텍스트[2:5]는 인덱스 2, 3, 4만 포함합니다. "
                            "이것은 range()와 같은 규칙입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 인코딩 기초 ──────────────────────
            {
                "title": "인코딩 기초",
                "content": [
                    "컴퓨터는 문자를 숫자로 저장합니다. "
                    "문자를 숫자로 바꾸는 규칙을 **인코딩(encoding)**이라고 하며, "
                    "가장 널리 쓰이는 것이 **UTF-8**입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "인코딩은 암호표와 같습니다. "
                            "같은 글자라도 암호표(인코딩)가 다르면 "
                            "다른 숫자로 변환됩니다. "
                            "보내는 쪽과 받는 쪽이 같은 암호표를 써야 합니다."
                        ),
                    },
                    {"type": "heading", "text": "ASCII와 UTF-8"},
                    {
                        "type": "bullet_list",
                        "items": [
                            "ASCII: 영문자, 숫자, 기호 128개만 표현 (1바이트)",
                            "UTF-8: 전 세계 모든 문자 표현 가능 (1~4바이트)",
                            "UTF-8은 ASCII와 하위 호환 (영문은 1바이트 동일)",
                            "한글 1글자 = UTF-8에서 3바이트",
                        ],
                    },
                    {"type": "heading", "text": "encode와 decode"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 문자열 → 바이트 (인코딩)\n"
                            "텍스트 = '안녕'\n"
                            "바이트 = 텍스트.encode('utf-8')\n"
                            "print(바이트)        # b'\\xec\\x95\\x88\\xeb\\x85\\x95'\n"
                            "print(len(바이트))   # 6 (한글 2글자 × 3바이트)\n\n"
                            "# 바이트 → 문자열 (디코딩)\n"
                            "복원 = 바이트.decode('utf-8')\n"
                            "print(복원)          # '안녕'\n\n"
                            "# 영문은 1바이트\n"
                            "print(len('AB'.encode('utf-8')))  # 2"
                        ),
                    },
                    {"type": "heading", "text": "한글 처리 시 주의점"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 문자 수와 바이트 수는 다릅니다\n"
                            "텍스트 = '파이썬 Python'\n"
                            "print(len(텍스트))                    # 10 (문자 수)\n"
                            "print(len(텍스트.encode('utf-8')))    # 16 (바이트 수)\n"
                            "# 한글 3자 × 3바이트 + 공백 1바이트 + 영문 6자 × 1바이트 = 16\n\n"
                            "# 잘못된 인코딩으로 열면 깨집니다\n"
                            "try:\n"
                            "    '한글'.encode('utf-8').decode('ascii')\n"
                            "except UnicodeDecodeError as e:\n"
                            "    print(f'인코딩 오류: {e}')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "파일을 읽고 쓸 때 인코딩을 명시하세요. "
                            "open('파일.txt', encoding='utf-8')처럼 "
                            "항상 encoding 인자를 지정하는 습관을 들이세요."
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "MLOps에서 데이터 전처리 시 인코딩 문제는 빈번합니다. "
                            "CSV 파일이 깨져 보인다면 십중팔구 인코딩 문제입니다. "
                            "'utf-8', 'cp949'(한국 윈도우), 'euc-kr' 순서로 시도해 보세요."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 정규표현식 맛보기 ────────────────
            {
                "title": "정규표현식 맛보기",
                "content": [
                    "정규표현식(Regular Expression, regex)은 "
                    "문자열에서 특정 패턴을 찾는 강력한 도구입니다. "
                    "Python에서는 `re` 모듈로 사용합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "정규표현식은 금속탐지기와 같습니다. "
                            "해변(텍스트) 위를 훑으면서 "
                            "특정 패턴(금속)에 해당하는 부분만 "
                            "찾아냅니다."
                        ),
                    },
                    {"type": "heading", "text": "re 모듈 기본 함수"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "텍스트 = '전화번호는 010-1234-5678이고 이메일은 test@email.com입니다'\n\n"
                            "# re.search(): 처음 매칭되는 것 찾기\n"
                            "결과 = re.search(r'\\d{3}-\\d{4}-\\d{4}', 텍스트)\n"
                            "if 결과:\n"
                            "    print(f'전화번호: {결과.group()}')  # 010-1234-5678\n\n"
                            "# re.findall(): 매칭되는 것 모두 찾기\n"
                            "숫자들 = re.findall(r'\\d+', 텍스트)\n"
                            "print(숫자들)  # ['010', '1234', '5678']\n\n"
                            "# re.sub(): 패턴 치환\n"
                            "가려진 = re.sub(r'\\d', '*', 텍스트)\n"
                            "print(가려진)  # 전화번호는 ***-****-****이고 ..."
                        ),
                    },
                    {"type": "heading", "text": "자주 쓰는 패턴 기호"},
                    {
                        "type": "table",
                        "headers": ["기호", "의미", "예시"],
                        "rows": [
                            ["\\d", "숫자 한 개", "'3', '7'"],
                            ["\\w", "영문자/숫자/밑줄", "'a', '3', '_'"],
                            ["\\s", "공백 문자", "' ', '\\t', '\\n'"],
                            [".", "아무 문자 한 개", "'a', '1', '!'"],
                            ["+", "1개 이상 반복", "\\d+ → '123'"],
                            ["*", "0개 이상 반복", "\\d* → '' 또는 '123'"],
                            ["{n}", "정확히 n번", "\\d{3} → '010'"],
                            ["{n,m}", "n~m번", "\\d{2,4} → '12'~'1234'"],
                            ["[ ]", "문자 클래스", "[aeiou] → 모음"],
                            ["^", "문자열 시작", "^Hello"],
                            ["$", "문자열 끝", "world$"],
                        ],
                    },
                    {"type": "heading", "text": "실용 패턴 예제"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n\n"
                            "# 패턴 1: 이메일 찾기\n"
                            "텍스트 = '연락처: user@example.com 또는 admin@test.co.kr'\n"
                            "이메일들 = re.findall(r'[\\w.+-]+@[\\w-]+\\.[\\w.]+', 텍스트)\n"
                            "print(이메일들)  # ['user@example.com', 'admin@test.co.kr']\n\n"
                            "# 패턴 2: 전화번호 찾기\n"
                            "텍스트2 = '집: 02-123-4567, 핸드폰: 010-9876-5432'\n"
                            "전화번호들 = re.findall(r'\\d{2,3}-\\d{3,4}-\\d{4}', 텍스트2)\n"
                            "print(전화번호들)  # ['02-123-4567', '010-9876-5432']\n\n"
                            "# 패턴 3: 한글만 추출\n"
                            "혼합 = 'Hello 안녕 World 세계'\n"
                            "한글만 = re.findall(r'[가-힣]+', 혼합)\n"
                            "print(한글만)  # ['안녕', '세계']"
                        ),
                    },
                    {"type": "heading", "text": "실습: 시저 암호"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 시저 암호: 각 글자를 일정 칸수만큼 밀어서 암호화\n"
                            "def 시저_암호화(텍스트, 이동칸):\n"
                            "    \"\"\"영문 소문자를 이동칸만큼 밀어서 암호화합니다.\"\"\"\n"
                            "    결과 = []\n"
                            "    for 글자 in 텍스트:\n"
                            "        if 'a' <= 글자 <= 'z':\n"
                            "            # ord()로 숫자 변환 → 이동 → chr()로 문자 복원\n"
                            "            새_번호 = (ord(글자) - ord('a') + 이동칸) % 26\n"
                            "            결과.append(chr(새_번호 + ord('a')))\n"
                            "        elif 'A' <= 글자 <= 'Z':\n"
                            "            새_번호 = (ord(글자) - ord('A') + 이동칸) % 26\n"
                            "            결과.append(chr(새_번호 + ord('A')))\n"
                            "        else:\n"
                            "            결과.append(글자)  # 영문이 아니면 그대로\n"
                            "    return ''.join(결과)\n\n\n"
                            "def 시저_복호화(암호문, 이동칸):\n"
                            "    \"\"\"암호문을 이동칸만큼 되돌려 복호화합니다.\"\"\"\n"
                            "    return 시저_암호화(암호문, -이동칸)\n\n\n"
                            "# 테스트\n"
                            "원문 = 'Hello Python'\n"
                            "암호문 = 시저_암호화(원문, 3)\n"
                            "print(f'원문:   {원문}')     # Hello Python\n"
                            "print(f'암호문: {암호문}')   # Khoor Sbwkrq\n"
                            "print(f'복호문: {시저_복호화(암호문, 3)}')  # Hello Python"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "정규표현식은 처음에 어려울 수 있습니다. "
                            "이 단계에서는 기본 기호를 익히고, "
                            "필요할 때 참고표를 보면서 쓰면 충분합니다. "
                            "연습할수록 자연스러워집니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "문자열 결합이 많을 때는 + 대신 join()을 쓰세요. "
            "성능이 훨씬 좋습니다.",
            "f-string은 가장 읽기 쉬운 포매팅 방법입니다. "
            "format()이나 % 대신 f-string을 쓰는 습관을 들이세요.",
            "사용자 입력은 항상 strip()으로 양쪽 공백을 제거한 뒤 처리하세요.",
            "파일을 열 때 encoding='utf-8'을 명시하는 것이 좋은 습관입니다.",
            "정규표현식 패턴 앞에 r을 붙여 원시 문자열(raw string)로 쓰세요. "
            "역슬래시(\\) 문제를 방지합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "Python 문자열에 대한 설명으로 올바른 것은?",
                "choices": [
                    "A) 문자열은 변경 가능(mutable)하다",
                    "B) 문자열은 불변(immutable) 시퀀스이다",
                    "C) 문자열에 인덱싱을 사용할 수 없다",
                    "D) 문자열 메서드는 원본을 직접 수정한다",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "f'{3.14159:.2f}'의 출력 결과는?",
                "choices": [
                    "A) 3.14159",
                    "B) 3.14",
                    "C) 3.1",
                    "D) 3",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "사용자로부터 이름을 입력받아 "
                    "앞뒤 공백을 제거하고, 첫 글자만 대문자로 바꿔 출력하세요. "
                    "(예: '  john doe  ' → 'John Doe')"
                ),
                "hint": "strip()과 title() 메서드를 조합하세요.",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "주어진 문자열이 회문(팰린드롬)인지 확인하는 함수를 작성하세요. "
                    "공백과 대소문자는 무시합니다. "
                    "(예: 'Race Car' → True)"
                ),
                "hint": (
                    "lower()와 replace()로 전처리한 뒤, "
                    "슬라이싱 [::-1]으로 뒤집어 비교하세요."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "텍스트에서 모든 이메일 주소를 찾아 "
                    "리스트로 반환하는 함수를 정규표현식으로 작성하세요."
                ),
                "hint": "re.findall()과 적절한 이메일 패턴을 사용하세요.",
            },
        ],
        "challenge": {
            "question": (
                "시저 암호를 확장하여, "
                "한글(가~힣)도 암호화할 수 있는 버전을 만드세요. "
                "한글 유니코드 범위(44032~55203)를 활용하고, "
                "암호화/복호화가 정확히 동작하는지 테스트하세요."
            ),
            "hint": (
                "ord('가')는 44032, 한글 음절은 총 11172개(55203-44032+1)입니다. "
                "영문과 같은 원리로 범위 안에서 순환시키세요."
            ),
        },
        "summary": [
            "Python 문자열은 불변(immutable) 시퀀스이며, "
            "수정하면 항상 새 문자열이 만들어집니다.",
            "f-string은 가장 직관적이고 빠른 포매팅 방법입니다. "
            "정렬, 소수점, 천 단위 등 다양한 서식을 지원합니다.",
            "문자열 메서드는 검색, 변환, 분리/결합, 판별 네 카테고리로 분류됩니다.",
            "슬라이싱 [start:stop:step]으로 문자열의 일부를 "
            "자유자재로 잘라낼 수 있습니다.",
            "UTF-8은 전 세계 문자를 표현하는 표준 인코딩이며, "
            "한글 1글자는 3바이트입니다.",
            "정규표현식(re 모듈)은 패턴 기반 문자열 검색에 강력한 도구이며, "
            "\\d, \\w, +, * 등의 기호를 사용합니다.",
            "문자열 결합 시 + 대신 join()을, "
            "파일 처리 시 encoding='utf-8'을 명시하는 것이 좋은 습관입니다.",
        ],
    }
