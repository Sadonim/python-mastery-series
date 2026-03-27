"""챕터 5: 함수 — 코드를 재사용하는 마법."""


def get_chapter():
    """챕터 5 콘텐츠를 반환한다."""
    return {
        "number": 5,
        "title": "함수",
        "subtitle": "코드를 재사용하는 마법",
        "big_picture": (
            "같은 코드를 여러 번 복사·붙여넣기 하고 있다면, "
            "함수를 만들어야 할 때입니다. "
            "함수는 코드를 이름 붙인 블록으로 묶어 "
            "언제든 호출할 수 있게 만드는 핵심 도구입니다. "
            "프로그램의 복잡도를 낮추고 유지보수를 쉽게 만드는 "
            "모든 프로그래밍의 기본 단위가 바로 함수입니다."
        ),
        "sections": [
            # ── 섹션 1: 함수란 무엇인가 ──────────────────────
            {
                "title": "함수란 무엇인가",
                "content": [
                    "함수(function)는 **특정 작업을 수행하는 코드 묶음**에 "
                    "이름을 붙인 것입니다. 한번 정의하면 몇 번이든 재사용할 수 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "함수는 자판기와 같습니다. "
                            "돈(입력)을 넣고 버튼(함수 호출)을 누르면 "
                            "음료(출력)가 나옵니다. "
                            "자판기 내부 동작을 몰라도 사용할 수 있듯이, "
                            "함수도 내부 구현을 몰라도 호출하여 결과를 받을 수 있습니다."
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "입력 (인자)"},
                            {"label": "함수 (코드 묶음)", "color": "#3182F6"},
                            {"label": "출력 (반환값)"},
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "DRY 원칙: Don't Repeat Yourself",
                    },
                    (
                        "같은 코드가 2번 이상 등장한다면, 함수로 추출하세요. "
                        "코드 중복은 버그의 근원이며, "
                        "수정 시 모든 복사본을 찾아 고쳐야 하기 때문입니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 나쁜 예: 같은 코드 반복\n"
                            "print('=' * 30)\n"
                            "print('보고서 제목')\n"
                            "print('=' * 30)\n\n"
                            "# ... 다른 코드 ...\n\n"
                            "print('=' * 30)\n"
                            "print('요약')\n"
                            "print('=' * 30)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 좋은 예: 함수로 추출\n"
                            "def print_header(title):\n"
                            "    \"\"\"제목을 꾸며서 출력한다.\"\"\"\n"
                            "    print('=' * 30)\n"
                            "    print(title)\n"
                            "    print('=' * 30)\n\n"
                            "print_header('보고서 제목')\n"
                            "# ... 다른 코드 ...\n"
                            "print_header('요약')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "함수 정의 기본 구조",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 함수 정의 기본 구조\n"
                            "def 함수이름(매개변수1, 매개변수2):\n"
                            "    \"\"\"이 함수가 무엇을 하는지 설명 (독스트링).\"\"\"\n"
                            "    # 함수 본문\n"
                            "    결과 = 매개변수1 + 매개변수2\n"
                            "    return 결과\n\n"
                            "# 함수 호출\n"
                            "값 = 함수이름(10, 20)\n"
                            "print(값)  # 30"
                        ),
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "`def` 키워드로 함수를 정의한다.",
                            "함수 이름은 소문자와 밑줄 조합 (snake_case)을 사용한다.",
                            "괄호 안에 매개변수를 나열한다 (없을 수도 있음).",
                            "콜론 `:` 뒤에 들여쓰기된 본문이 온다.",
                            "`return`으로 결과를 돌려준다 (생략하면 None 반환).",
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 매개변수가 없는 함수\n"
                            "def greet():\n"
                            "    \"\"\"인사말을 출력한다.\"\"\"\n"
                            "    print('안녕하세요! Python 세계에 오신 것을 환영합니다.')\n\n"
                            "greet()  # 함수 호출\n"
                            "greet()  # 몇 번이든 재사용 가능"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "함수를 정의만 하고 호출하지 않으면 아무 일도 일어나지 않습니다. "
                            "`def`는 '레시피를 적어두는 것'이고, "
                            "실제 요리는 함수를 호출할 때 시작됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 매개변수와 인자 ──────────────────────
            {
                "title": "매개변수와 인자",
                "content": [
                    "**매개변수(parameter)**는 함수 정의 시 괄호 안의 변수이고, "
                    "**인자(argument)**는 함수 호출 시 실제로 전달하는 값입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "택배 양식에 '받는 사람'이라는 빈칸(매개변수)이 있고, "
                            "실제로 '홍길동'이라고 적는 것(인자)과 같습니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "위치 인자 (Positional Arguments)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 위치 인자 — 순서대로 매칭\n"
                            "def introduce(name, age, city):\n"
                            "    \"\"\"자기소개 문장을 반환한다.\"\"\"\n"
                            "    return f'저는 {city}에 사는 {age}세 {name}입니다.'\n\n"
                            "# 순서대로 전달\n"
                            "msg = introduce('김철수', 25, '서울')\n"
                            "print(msg)  # 저는 서울에 사는 25세 김철수입니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "키워드 인자 (Keyword Arguments)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 키워드 인자 — 이름으로 매칭 (순서 무관)\n"
                            "msg = introduce(city='부산', name='이영희', age=30)\n"
                            "print(msg)  # 저는 부산에 사는 30세 이영희입니다.\n\n"
                            "# 위치 인자와 키워드 인자 혼합\n"
                            "msg = introduce('박민수', age=22, city='대전')\n"
                            "print(msg)  # 저는 대전에 사는 22세 박민수입니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "기본값 매개변수 (Default Parameters)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본값 — 인자를 생략하면 기본값 사용\n"
                            "def make_coffee(size='보통', sugar=1):\n"
                            "    \"\"\"커피 주문 내역을 반환한다.\"\"\"\n"
                            "    return f'{size} 사이즈, 설탕 {sugar}개'\n\n"
                            "print(make_coffee())                # 보통 사이즈, 설탕 1개\n"
                            "print(make_coffee('큰'))             # 큰 사이즈, 설탕 1개\n"
                            "print(make_coffee('작은', 0))        # 작은 사이즈, 설탕 0개\n"
                            "print(make_coffee(sugar=3))         # 보통 사이즈, 설탕 3개"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "기본값 매개변수는 반드시 일반 매개변수 뒤에 와야 합니다. "
                            "`def f(a=1, b):` 는 SyntaxError입니다. "
                            "`def f(b, a=1):` 처럼 작성하세요."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "*args와 **kwargs — 가변 인자",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# *args — 위치 인자를 튜플로 받기\n"
                            "def calculate_sum(*numbers):\n"
                            "    \"\"\"전달받은 모든 숫자의 합을 반환한다.\"\"\"\n"
                            "    total = 0\n"
                            "    for num in numbers:\n"
                            "        total += num\n"
                            "    return total\n\n"
                            "print(calculate_sum(1, 2, 3))       # 6\n"
                            "print(calculate_sum(10, 20, 30, 40))  # 100"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# **kwargs — 키워드 인자를 딕셔너리로 받기\n"
                            "def print_profile(**info):\n"
                            "    \"\"\"전달받은 모든 정보를 출력한다.\"\"\"\n"
                            "    for key, value in info.items():\n"
                            "        print(f'{key}: {value}')\n\n"
                            "print_profile(이름='김철수', 나이=25, 직업='개발자')\n"
                            "# 출력:\n"
                            "# 이름: 김철수\n"
                            "# 나이: 25\n"
                            "# 직업: 개발자"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "`*args`와 `**kwargs`의 이름은 관례일 뿐입니다. "
                            "`*values`, `**options` 등 원하는 이름을 쓸 수 있습니다. "
                            "중요한 것은 `*`(튜플)과 `**`(딕셔너리) 기호입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 반환값 ───────────────────────────────
            {
                "title": "반환값",
                "content": [
                    "함수는 `return` 키워드로 결과를 호출자에게 돌려줍니다. "
                    "return이 없거나 값 없이 쓰이면 `None`을 반환합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 반환\n"
                            "def square(n):\n"
                            "    \"\"\"n의 제곱을 반환한다.\"\"\"\n"
                            "    return n ** 2\n\n"
                            "result = square(7)\n"
                            "print(result)  # 49\n\n"
                            "# return 이후의 코드는 실행되지 않음\n"
                            "def test():\n"
                            "    return '여기까지만 실행'\n"
                            "    print('이 줄은 절대 실행되지 않습니다')  # 도달 불가"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "다중 반환값",
                    },
                    "Python은 여러 값을 한꺼번에 반환할 수 있습니다. "
                    "내부적으로는 튜플(tuple)로 묶여서 반환됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 다중 반환 — 통계 계산\n"
                            "def get_statistics(numbers):\n"
                            "    \"\"\"리스트의 합계, 개수, 평균을 반환한다.\"\"\"\n"
                            "    total = sum(numbers)\n"
                            "    count = len(numbers)\n"
                            "    average = total / count if count > 0 else 0\n"
                            "    return total, count, average\n\n"
                            "scores = [88, 92, 75, 96, 80]\n\n"
                            "# 튜플로 한꺼번에 받기\n"
                            "stats = get_statistics(scores)\n"
                            "print(stats)  # (431, 5, 86.2)\n\n"
                            "# 언패킹으로 개별 변수에 받기 (권장)\n"
                            "total, count, avg = get_statistics(scores)\n"
                            "print(f'합계: {total}, 인원: {count}, 평균: {avg:.1f}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "None 반환과 출력 함수",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# return이 없으면 None 반환\n"
                            "def say_hello(name):\n"
                            "    \"\"\"인사말을 출력한다 (반환값 없음).\"\"\"\n"
                            "    print(f'안녕하세요, {name}님!')\n\n"
                            "result = say_hello('철수')  # '안녕하세요, 철수님!' 출력\n"
                            "print(result)  # None\n\n"
                            "# 주의: print()는 '출력'이고, return은 '반환'입니다.\n"
                            "# 출력: 화면에 표시 (사람이 볼 수 있음)\n"
                            "# 반환: 값을 호출자에게 전달 (코드가 사용할 수 있음)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "함수가 계산 결과를 돌려줘야 할 때는 반드시 `return`을 쓰세요. "
                            "`print()`만 쓰면 화면에는 보이지만, "
                            "다른 코드에서 그 값을 사용할 수 없습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 스코프와 네임스페이스 ────────────────
            {
                "title": "스코프와 네임스페이스",
                "content": [
                    "**스코프(scope)**는 변수가 유효한 범위입니다. "
                    "함수 안에서 만든 변수는 함수 밖에서 사용할 수 없습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "스코프는 교실의 칠판과 같습니다. "
                            "1반 칠판에 적힌 내용은 2반에서 볼 수 없고, "
                            "각 반(함수)은 자기만의 칠판(지역 변수)을 가집니다. "
                            "교무실 칠판(전역 변수)은 모든 반에서 참조할 수 있습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 지역 변수 vs 전역 변수\n"
                            "message = '전역 메시지'  # 전역 변수\n\n"
                            "def show_message():\n"
                            "    message = '지역 메시지'  # 지역 변수 (새로 생성됨)\n"
                            "    print(f'함수 안: {message}')\n\n"
                            "show_message()       # 함수 안: 지역 메시지\n"
                            "print(f'함수 밖: {message}')  # 함수 밖: 전역 메시지"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "LEGB 규칙 — 변수 검색 순서",
                    },
                    "Python은 변수를 찾을 때 다음 순서로 검색합니다.",
                    {
                        "type": "numbered_list",
                        "items": [
                            "L (Local) — 현재 함수 내부",
                            "E (Enclosing) — 바깥 함수 (중첩 함수인 경우)",
                            "G (Global) — 모듈 전역",
                            "B (Built-in) — Python 내장 (print, len 등)",
                        ],
                    },
                    {
                        "type": "diagram",
                        "text": (
                            "  ┌─────────────────────────────┐\n"
                            "  │  B: Built-in (print, len)   │\n"
                            "  │  ┌───────────────────────┐  │\n"
                            "  │  │  G: Global (모듈 전역)  │  │\n"
                            "  │  │  ┌─────────────────┐  │  │\n"
                            "  │  │  │  E: Enclosing    │  │  │\n"
                            "  │  │  │  ┌───────────┐  │  │  │\n"
                            "  │  │  │  │  L: Local  │  │  │  │\n"
                            "  │  │  │  │  (여기부터)  │  │  │  │\n"
                            "  │  │  │  └───────────┘  │  │  │\n"
                            "  │  │  └─────────────────┘  │  │\n"
                            "  │  └───────────────────────┘  │\n"
                            "  └─────────────────────────────┘"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# LEGB 규칙 예시\n"
                            "x = '전역'          # G: Global\n\n"
                            "def outer():\n"
                            "    x = '바깥 함수'   # E: Enclosing\n\n"
                            "    def inner():\n"
                            "        x = '안쪽 함수'  # L: Local\n"
                            "        print(x)  # '안쪽 함수' (L에서 찾음)\n\n"
                            "    inner()\n"
                            "    print(x)      # '바깥 함수' (E에서 찾음)\n\n"
                            "outer()\n"
                            "print(x)          # '전역' (G에서 찾음)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "global 키워드",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# global — 함수 안에서 전역 변수를 수정할 때\n"
                            "counter = 0\n\n"
                            "def increment():\n"
                            "    global counter  # 전역 변수를 사용하겠다고 선언\n"
                            "    counter += 1\n\n"
                            "increment()\n"
                            "increment()\n"
                            "print(counter)  # 2"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "`global`은 가능하면 피하세요. "
                            "전역 변수를 함수 안에서 수정하면 "
                            "코드의 흐름을 추적하기 어려워집니다. "
                            "대신 매개변수로 값을 받고, return으로 결과를 돌려주세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: lambda 함수 ──────────────────────────
            {
                "title": "lambda 함수",
                "content": [
                    "`lambda`는 이름 없는 **한 줄짜리 함수**를 만드는 문법입니다. "
                    "간단한 변환이나 정렬 기준을 정할 때 자주 사용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 일반 함수\n"
                            "def double(x):\n"
                            "    return x * 2\n\n"
                            "# 같은 기능의 lambda\n"
                            "double_lambda = lambda x: x * 2\n\n"
                            "print(double(5))         # 10\n"
                            "print(double_lambda(5))  # 10"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "map()과 함께 사용",
                    },
                    "`map(함수, 시퀀스)`는 시퀀스의 모든 요소에 함수를 적용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# map() + lambda — 모든 요소 변환\n"
                            "prices = [1000, 2500, 800, 3200]\n\n"
                            "# 10% 할인 적용\n"
                            "discounted = list(map(lambda p: int(p * 0.9), prices))\n"
                            "print(discounted)  # [900, 2250, 720, 2880]\n\n"
                            "# 섭씨 → 화씨 변환\n"
                            "celsius = [0, 10, 20, 30, 100]\n"
                            "fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))\n"
                            "print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 212.0]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "filter()와 함께 사용",
                    },
                    "`filter(함수, 시퀀스)`는 함수가 True를 반환하는 요소만 남깁니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# filter() + lambda — 조건 필터링\n"
                            "scores = [45, 78, 92, 33, 67, 88, 55]\n\n"
                            "# 60점 이상만 필터\n"
                            "passed = list(filter(lambda s: s >= 60, scores))\n"
                            "print(passed)  # [78, 92, 67, 88]\n\n"
                            "# 짝수만 필터\n"
                            "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\n"
                            "evens = list(filter(lambda n: n % 2 == 0, numbers))\n"
                            "print(evens)  # [2, 4, 6, 8]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "정렬 기준으로 사용",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# sorted() + lambda — 정렬 기준 지정\n"
                            "students = [\n"
                            "    ('김철수', 88),\n"
                            "    ('이영희', 95),\n"
                            "    ('박민수', 72),\n"
                            "    ('정수진', 91),\n"
                            "]\n\n"
                            "# 점수 기준 오름차순 정렬\n"
                            "by_score = sorted(students, key=lambda s: s[1])\n"
                            "print(by_score)\n"
                            "# [('박민수', 72), ('김철수', 88), ('정수진', 91), ('이영희', 95)]\n\n"
                            "# 점수 기준 내림차순 정렬\n"
                            "top_first = sorted(students, key=lambda s: s[1], reverse=True)\n"
                            "print(top_first[0])  # ('이영희', 95)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "lambda는 간단한 한 줄 로직에만 사용하세요. "
                            "복잡한 로직은 일반 함수로 정의하는 것이 "
                            "읽기 좋고 디버깅하기 쉽습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 함수 설계 원칙 ───────────────────────
            {
                "title": "함수 설계 원칙",
                "content": [
                    "좋은 함수는 읽기 쉽고, 테스트하기 쉽고, 재사용하기 쉽습니다. "
                    "다음 원칙을 따르면 품질 높은 함수를 작성할 수 있습니다.",
                    {
                        "type": "heading",
                        "text": "원칙 1: 단일 책임 (한 가지 일만 하라)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 나쁜 예: 함수가 너무 많은 일을 함\n"
                            "def process_student(name, scores):\n"
                            "    \"\"\"학생 데이터를 처리하고 출력하고 파일에 저장한다.\"\"\"\n"
                            "    avg = sum(scores) / len(scores)\n"
                            "    grade = 'A' if avg >= 90 else 'B' if avg >= 80 else 'C'\n"
                            "    print(f'{name}: {avg:.1f} ({grade})')\n"
                            "    # ... 파일 저장 코드 ...\n"
                            "    return grade\n\n"
                            "# 좋은 예: 역할별로 분리\n"
                            "def calculate_average(scores):\n"
                            "    \"\"\"점수 리스트의 평균을 반환한다.\"\"\"\n"
                            "    if not scores:\n"
                            "        return 0.0\n"
                            "    return sum(scores) / len(scores)\n\n"
                            "def determine_grade(average):\n"
                            "    \"\"\"평균 점수에 따른 학점을 반환한다.\"\"\"\n"
                            "    if average >= 90:\n"
                            "        return 'A'\n"
                            "    if average >= 80:\n"
                            "        return 'B'\n"
                            "    return 'C'\n\n"
                            "def format_report(name, average, grade):\n"
                            "    \"\"\"학생 보고서 문자열을 반환한다.\"\"\"\n"
                            "    return f'{name}: {average:.1f} ({grade})'"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "원칙 2: 명확한 이름",
                    },
                    {
                        "type": "table",
                        "headers": ["나쁜 이름", "좋은 이름", "이유"],
                        "rows": [
                            ["do_stuff()", "calculate_tax()", "무엇을 하는지 명확"],
                            ["f(x)", "celsius_to_fahrenheit(temp)", "의미 전달"],
                            ["process(d)", "validate_email(address)", "동작이 구체적"],
                            ["func1()", "is_leap_year(year)", "결과 타입 예측 가능"],
                        ],
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "동사로 시작: `calculate_`, `get_`, `validate_`, `convert_`",
                            "불리언 반환 함수: `is_`, `has_`, `can_` 접두사 사용",
                            "축약어 금지: `calc_avg` 보다 `calculate_average`",
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "원칙 3: 독스트링(docstring) 작성",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def calculate_bmi(weight_kg, height_cm):\n"
                            "    \"\"\"BMI(체질량지수)를 계산하여 반환한다.\n\n"
                            "    Args:\n"
                            "        weight_kg: 체중 (킬로그램 단위, 양수)\n"
                            "        height_cm: 키 (센티미터 단위, 양수)\n\n"
                            "    Returns:\n"
                            "        BMI 값 (float)\n\n"
                            "    Raises:\n"
                            "        ValueError: 체중 또는 키가 0 이하일 때\n"
                            "    \"\"\"\n"
                            "    if weight_kg <= 0 or height_cm <= 0:\n"
                            "        raise ValueError('체중과 키는 양수여야 합니다.')\n\n"
                            "    height_m = height_cm / 100\n"
                            "    return weight_kg / (height_m ** 2)\n\n"
                            "# 독스트링 확인\n"
                            "help(calculate_bmi)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실습: 성적 관리 프로그램",
                    },
                    "배운 함수 설계 원칙을 적용한 종합 실습입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# === 성적 관리 프로그램 ===\n\n"
                            "def input_scores():\n"
                            "    \"\"\"과목별 점수를 입력받아 딕셔너리로 반환한다.\"\"\"\n"
                            "    subjects = ['국어', '영어', '수학']\n"
                            "    scores = {}\n\n"
                            "    for subject in subjects:\n"
                            "        while True:\n"
                            "            raw = input(f'{subject} 점수 (0~100): ')\n"
                            "            if raw.isdigit() and 0 <= int(raw) <= 100:\n"
                            "                scores[subject] = int(raw)\n"
                            "                break\n"
                            "            print('0~100 사이의 정수를 입력해 주세요.')\n\n"
                            "    return scores\n\n\n"
                            "def calculate_average(scores):\n"
                            "    \"\"\"점수 딕셔너리의 평균을 반환한다.\"\"\"\n"
                            "    values = list(scores.values())\n"
                            "    if not values:\n"
                            "        return 0.0\n"
                            "    return sum(values) / len(values)\n\n\n"
                            "def determine_grade(average):\n"
                            "    \"\"\"평균 점수에 따른 학점을 반환한다.\"\"\"\n"
                            "    if average >= 90:\n"
                            "        return 'A'\n"
                            "    if average >= 80:\n"
                            "        return 'B'\n"
                            "    if average >= 70:\n"
                            "        return 'C'\n"
                            "    if average >= 60:\n"
                            "        return 'D'\n"
                            "    return 'F'\n\n\n"
                            "def print_report(name, scores, average, grade):\n"
                            "    \"\"\"성적표를 출력한다.\"\"\"\n"
                            "    print(f'\\n{\"=\" * 30}')\n"
                            "    print(f'  {name}님의 성적표')\n"
                            "    print(f'{\"=\" * 30}')\n"
                            "    for subject, score in scores.items():\n"
                            "        print(f'  {subject}: {score}점')\n"
                            "    print(f'{\"-\" * 30}')\n"
                            "    print(f'  평균: {average:.1f}점')\n"
                            "    print(f'  학점: {grade}')\n"
                            "    print(f'{\"=\" * 30}')\n\n\n"
                            "# 메인 실행\n"
                            "name = input('학생 이름: ')\n"
                            "scores = input_scores()\n"
                            "avg = calculate_average(scores)\n"
                            "grade = determine_grade(avg)\n"
                            "print_report(name, scores, avg, grade)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "각 함수가 한 가지 역할만 수행하는 것에 주목하세요. "
                            "입력, 계산, 판정, 출력이 분리되어 있어서 "
                            "각각 독립적으로 테스트하고 수정할 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "함수 하나는 한 가지 일만 하도록 작성하세요 (단일 책임 원칙).",
            "함수 이름은 동사로 시작하고, 무엇을 하는지 명확히 드러내세요.",
            "print()와 return을 구분하세요. 계산 함수는 return, 출력 함수는 print.",
            "global 키워드는 가능한 피하고, 매개변수와 return을 활용하세요.",
            "독스트링을 작성하면 나중에 함수를 이해하기 훨씬 쉬워집니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 함수의 반환값이 `None`인 경우는?",
                "choices": [
                    "A) return 0",
                    "B) return False",
                    "C) return 문이 없는 함수",
                    "D) return ''",
                ],
                "answer": "C",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "LEGB 규칙에서 Python이 변수를 가장 먼저 "
                    "찾는 곳은?"
                ),
                "choices": [
                    "A) Global",
                    "B) Built-in",
                    "C) Local",
                    "D) Enclosing",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "두 수를 매개변수로 받아 큰 수를 반환하는 함수 "
                    "`get_max(a, b)`를 작성하세요. "
                    "두 수가 같으면 그 수를 반환합니다."
                ),
                "hint": "if/else 또는 삼항 연산자를 사용하세요.",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "`*args`를 사용하여 전달받은 모든 숫자 중 "
                    "짝수의 합을 반환하는 함수 `sum_even(*numbers)`를 "
                    "작성하세요."
                ),
                "hint": "for 루프에서 % 2 == 0 조건으로 필터링하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "문자열과 문자를 받아 해당 문자의 등장 횟수를 반환하는 "
                    "함수 `count_char(text, char)`를 작성하세요. "
                    "대소문자를 구분하지 않아야 합니다."
                ),
                "hint": "text.lower()로 통일한 뒤 for 루프로 비교하세요.",
            },
        ],
        "challenge": {
            "question": (
                "간단한 계산기 프로그램을 만드세요. "
                "사칙연산 각각을 함수로 정의하고 (add, subtract, multiply, divide), "
                "메뉴 시스템(while 루프)으로 사용자가 연산을 선택하도록 합니다. "
                "0으로 나누기를 처리하고, '종료'를 입력하면 프로그램을 끝내세요."
            ),
            "hint": (
                "각 연산 함수는 두 수를 받아 결과를 return합니다. "
                "divide 함수에서는 0 검사를 하여 에러 메시지를 반환하세요. "
                "메인 루프는 챕터 4의 메뉴 시스템 패턴을 참고하세요."
            ),
        },
        "summary": [
            "함수는 `def 이름(매개변수):` 로 정의하고, 호출하여 재사용한다.",
            "DRY 원칙: 같은 코드가 반복되면 함수로 추출한다.",
            "매개변수에는 위치 인자, 키워드 인자, 기본값, *args, **kwargs가 있다.",
            "`return`으로 결과를 반환하며, 여러 값을 동시에 반환할 수 있다(튜플).",
            "return이 없으면 None을 반환한다. print()와 return을 구분해야 한다.",
            "LEGB 규칙: Local → Enclosing → Global → Built-in 순서로 변수를 검색한다.",
            "lambda는 한 줄짜리 익명 함수로, map/filter/sorted와 함께 자주 쓰인다.",
            "좋은 함수는 단일 책임, 명확한 이름, 독스트링을 갖추고 있다.",
        ],
    }
