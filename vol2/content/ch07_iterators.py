"""챕터 7: 이터레이터와 제너레이터 — 메모리를 아끼며 데이터를 처리하는 기술."""


def get_chapter():
    """챕터 7 콘텐츠를 반환한다."""
    return {
        "number": 7,
        "title": "이터레이터와 제너레이터",
        "subtitle": "메모리를 아끼며 데이터를 처리하는 기술",
        "big_picture": (
            "100만 줄짜리 로그 파일을 처리해야 한다면 어떻게 할까요? "
            "전체를 메모리에 올리면 수 GB가 필요할 수 있습니다. "
            "이터레이터와 제너레이터는 '필요할 때 한 번에 하나씩'이라는 원칙으로 "
            "이 문제를 해결합니다. "
            "Python의 for 루프, 리스트 컴프리헨션, 내장 함수들이 모두 "
            "이 메커니즘 위에서 동작하고 있습니다. "
            "MLOps 파이프라인에서 대용량 데이터를 다룰 때 꼭 필요한 핵심 개념입니다."
        ),
        "sections": [
            # ── 섹션 1: 이터러블과 이터레이터 ───────────────────────
            {
                "title": "이터러블 vs 이터레이터",
                "content": [
                    "Python에서 `for` 루프로 순회할 수 있는 모든 객체를 "
                    "**이터러블(Iterable)**이라고 합니다. "
                    "리스트, 튜플, 문자열, 딕셔너리, 파일 객체가 모두 이터러블입니다.",
                    {
                        "type": "table",
                        "headers": ["개념", "설명", "예시"],
                        "rows": [
                            ["이터러블 (Iterable)", "순회 가능한 객체. iter()를 호출할 수 있다.", "list, tuple, str, dict, set, range"],
                            ["이터레이터 (Iterator)", "다음 값을 하나씩 꺼낼 수 있는 객체. next()를 호출할 수 있다.", "iter(list), 파일 객체, 제너레이터"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "iter()와 next()로 동작 이해하기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 리스트는 이터러블이지만 이터레이터는 아님\n"
                            "numbers = [1, 2, 3]\n\n"
                            "# iter()로 이터레이터를 만든다\n"
                            "iterator = iter(numbers)\n"
                            "print(type(iterator))  # <class 'list_iterator'>\n\n"
                            "# next()로 값을 하나씩 꺼낸다\n"
                            "print(next(iterator))  # 1\n"
                            "print(next(iterator))  # 2\n"
                            "print(next(iterator))  # 3\n"
                            "# print(next(iterator))  # StopIteration 예외 발생!\n\n"
                            "# for 루프는 내부적으로 이 과정을 자동으로 처리함\n"
                            "# for x in numbers: ← 내부에서 iter() → next() → StopIteration 처리"
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "for x in iterable"},
                            {"label": "iter(iterable) 호출 → iterator 생성", "color": "#3182F6"},
                            {"label": "next(iterator) 호출 → 값 반환"},
                            {"label": "StopIteration 발생 → 루프 종료", "color": "#f04452"},
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "이터레이터는 이터러블이기도 합니다. "
                            "`iter(이터레이터)`를 호출하면 자기 자신을 반환합니다. "
                            "반면 이터러블은 이터레이터가 아닐 수 있습니다 — "
                            "리스트에 직접 `next()`를 호출하면 TypeError가 발생합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 커스텀 이터레이터 ───────────────────────────
            {
                "title": "커스텀 이터레이터 만들기",
                "content": [
                    "클래스에 `__iter__()`와 `__next__()` 메서드를 구현하면 "
                    "직접 이터레이터를 만들 수 있습니다. "
                    "이것이 바로 **이터레이터 프로토콜**입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class CountDown:\n"
                            "    \"\"\"숫자를 n에서 1까지 하나씩 반환하는 이터레이터.\"\"\"\n\n"
                            "    def __init__(self, start):\n"
                            "        self._current = start  # 현재 값 (변경 가능 상태)\n\n"
                            "    def __iter__(self):\n"
                            "        \"\"\"이터레이터 자신을 반환한다.\"\"\"\n"
                            "        return self\n\n"
                            "    def __next__(self):\n"
                            "        \"\"\"다음 값을 반환하거나 StopIteration을 발생시킨다.\"\"\"\n"
                            "        if self._current <= 0:\n"
                            "            raise StopIteration  # 순회 종료 신호\n"
                            "        value = self._current\n"
                            "        self._current -= 1\n"
                            "        return value\n\n\n"
                            "# 사용\n"
                            "for n in CountDown(5):\n"
                            "    print(n, end=' ')  # 5 4 3 2 1\n\n"
                            "# 리스트로 변환도 가능\n"
                            "print(list(CountDown(3)))  # [3, 2, 1]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "이터레이터의 한계: 한 번만 순회 가능",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 이터레이터는 소모성 — 한 번 다 쓰면 재사용 불가\n"
                            "counter = CountDown(3)\n\n"
                            "print(list(counter))  # [3, 2, 1]\n"
                            "print(list(counter))  # [] ← 이미 소진됨!\n\n"
                            "# 이터러블(클래스)은 여러 번 순회 가능\n"
                            "# __iter__에서 새 이터레이터를 반환하도록 설계\n"
                            "class NumberRange:\n"
                            "    \"\"\"여러 번 순회 가능한 이터러블 클래스.\"\"\"\n\n"
                            "    def __init__(self, start, end):\n"
                            "        self._start = start\n"
                            "        self._end = end\n\n"
                            "    def __iter__(self):\n"
                            "        \"\"\"매번 새 이터레이터를 반환한다.\"\"\"\n"
                            "        current = self._start\n"
                            "        while current <= self._end:\n"
                            "            yield current  # 제너레이터로 구현 (다음 섹션에서 설명)\n"
                            "            current += 1\n\n"
                            "nums = NumberRange(1, 3)\n"
                            "print(list(nums))  # [1, 2, 3]\n"
                            "print(list(nums))  # [1, 2, 3] ← 다시 순회 가능!"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "이터레이터를 직접 클래스로 구현하는 것은 복잡합니다. "
                            "Python에서는 대부분의 경우 다음 섹션에서 배울 "
                            "제너레이터로 훨씬 간단하게 같은 결과를 얻을 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 제너레이터 함수 ──────────────────────────────
            {
                "title": "제너레이터 함수: yield 키워드",
                "content": [
                    "**제너레이터(generator)**는 이터레이터를 아주 간단하게 만드는 방법입니다. "
                    "일반 함수에서 `return` 대신 `yield`를 사용하면 제너레이터 함수가 됩니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "제너레이터는 주문할 때마다 한 잔씩 만드는 바리스타와 같습니다. "
                            "일반 함수(return)가 커피 100잔을 미리 다 만들어 테이블에 올려두는 것이라면, "
                            "제너레이터(yield)는 손님이 '다음 잔 주세요'라고 요청할 때마다 "
                            "그 자리에서 한 잔씩 만들어 냅니다. "
                            "100잔을 보관할 공간이 필요 없고, 요청받을 때까지 일하지도 않습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 일반 함수: 모든 결과를 리스트로 만들어 한꺼번에 반환\n"
                            "def make_squares_list(n):\n"
                            "    result = []\n"
                            "    for i in range(n):\n"
                            "        result.append(i ** 2)\n"
                            "    return result  # n개 요소를 메모리에 모두 저장\n\n"
                            "# 제너레이터 함수: yield로 값을 하나씩 생산\n"
                            "def make_squares_gen(n):\n"
                            "    for i in range(n):\n"
                            "        yield i ** 2  # 여기서 실행이 '일시 중단'됨\n\n"
                            "# 사용법은 동일\n"
                            "for sq in make_squares_gen(5):\n"
                            "    print(sq, end=' ')  # 0 1 4 9 16\n\n"
                            "print(type(make_squares_gen(5)))  # <class 'generator'>"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "yield의 동작 원리",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def step_by_step():\n"
                            "    \"\"\"yield의 실행 흐름을 보여주는 예제.\"\"\"\n"
                            "    print('① 시작')       # next() 첫 호출 시 실행\n"
                            "    yield 10              # 10 반환, 실행 일시 중단\n"
                            "    print('② 재개')       # next() 두 번째 호출 시 재개\n"
                            "    yield 20\n"
                            "    print('③ 마지막')     # next() 세 번째 호출 시 재개\n"
                            "    yield 30\n"
                            "    print('④ 종료')       # StopIteration 발생 전 실행\n\n"
                            "gen = step_by_step()\n"
                            "print(next(gen))  # ① 시작 → 10\n"
                            "print(next(gen))  # ② 재개 → 20\n"
                            "print(next(gen))  # ③ 마지막 → 30\n"
                            "# next(gen)      # ④ 종료 → StopIteration"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실용 예제: 피보나치 제너레이터",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def fibonacci():\n"
                            "    \"\"\"무한 피보나치 수열을 생성하는 제너레이터.\"\"\"\n"
                            "    a, b = 0, 1\n"
                            "    while True:      # 무한 루프 — 메모리 걱정 없음!\n"
                            "        yield a\n"
                            "        a, b = b, a + b\n\n"
                            "# 처음 10개만 출력\n"
                            "gen = fibonacci()\n"
                            "first_ten = [next(gen) for _ in range(10)]\n"
                            "print(first_ten)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n\n"
                            "# 100 미만의 피보나치 수 출력\n"
                            "for fib in fibonacci():\n"
                            "    if fib >= 100:\n"
                            "        break\n"
                            "    print(fib, end=' ')  # 0 1 1 2 3 5 8 13 21 34 55 89"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "무한 제너레이터에서 `list(fibonacci())`를 호출하면 "
                            "메모리가 모두 소진되어 프로그램이 멈춥니다. "
                            "무한 제너레이터는 반드시 `break` 조건이나 `islice()`로 개수를 제한해야 합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 제너레이터 표현식 ───────────────────────────
            {
                "title": "제너레이터 표현식",
                "content": [
                    "리스트 컴프리헨션 `[...]`의 괄호를 `(...)`로 바꾸면 "
                    "**제너레이터 표현식**이 됩니다. "
                    "문법은 거의 동일하지만, 메모리를 훨씬 적게 사용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 리스트 컴프리헨션: 전체를 메모리에 올림\n"
                            "squares_list = [x ** 2 for x in range(1_000_000)]\n"
                            "# 약 8MB 메모리 사용\n\n"
                            "# 제너레이터 표현식: 필요할 때 하나씩 생성\n"
                            "squares_gen = (x ** 2 for x in range(1_000_000))\n"
                            "# 수백 바이트만 사용! 실제 값은 아직 계산되지 않음\n\n"
                            "import sys\n"
                            "print(sys.getsizeof(squares_list))  # ~8 MB\n"
                            "print(sys.getsizeof(squares_gen))   # ~120 bytes"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "내장 함수와 함께 사용",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# sum(), max(), min() 등 내장 함수는 제너레이터를 직접 받음\n"
                            "total = sum(x ** 2 for x in range(1000))  # 괄호 하나 절약\n"
                            "print(total)  # 332833500\n\n"
                            "# 조건부 필터링\n"
                            "even_squares = list(x ** 2 for x in range(10) if x % 2 == 0)\n"
                            "print(even_squares)  # [0, 4, 16, 36, 64]\n\n"
                            "# 파일 처리 (대용량 파일에서 특정 줄만 처리)\n"
                            "# error_lines = sum(1 for line in open('app.log') if 'ERROR' in line)\n"
                            "# — 파일 전체를 메모리에 올리지 않고 줄 수 계산 가능"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["구분", "리스트 컴프리헨션 [...]", "제너레이터 표현식 (...)"],
                        "rows": [
                            ["메모리", "전체를 즉시 생성", "필요할 때 하나씩 생성"],
                            ["재사용", "여러 번 순회 가능", "한 번 소진 후 재사용 불가"],
                            ["속도(첫 접근)", "느림 (모두 계산)", "빠름 (계산 미룸)"],
                            ["용도", "크기가 작고 여러 번 사용", "대용량 데이터, 일회성 처리"],
                        ],
                    },
                ],
            },
            # ── 섹션 5: itertools 모듈 ───────────────────────────────
            {
                "title": "itertools 모듈",
                "content": [
                    "`itertools`는 이터레이터를 다루는 강력한 함수들을 모아 놓은 표준 라이브러리입니다. "
                    "효율적인 루프 처리와 조합 생성에 자주 활용됩니다.",
                    {
                        "type": "table",
                        "headers": ["함수", "설명", "예시 결과"],
                        "rows": [
                            ["count(start, step)", "무한 카운터", "count(1, 2) → 1, 3, 5, 7 ..."],
                            ["cycle(iterable)", "무한 순환", "cycle([A,B]) → A, B, A, B ..."],
                            ["repeat(elem, n)", "n번 반복", "repeat(7, 3) → 7, 7, 7"],
                            ["chain(*iterables)", "여러 이터러블 연결", "chain([1,2],[3,4]) → 1,2,3,4"],
                            ["islice(it, n)", "n개만 잘라냄", "islice(count(), 5) → 0,1,2,3,4"],
                            ["product(*its)", "데카르트 곱", "product([1,2],[A,B]) → (1,A),(1,B),(2,A),(2,B)"],
                            ["combinations(it, r)", "조합", "combinations([1,2,3], 2) → (1,2),(1,3),(2,3)"],
                            ["permutations(it, r)", "순열", "permutations([1,2,3], 2) → (1,2),(1,3),..."],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "자주 쓰이는 itertools 활용",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import itertools\n\n"
                            "# chain: 여러 리스트를 하나처럼 순회\n"
                            "week1 = ['월', '화', '수']\n"
                            "week2 = ['목', '금', '토', '일']\n"
                            "all_days = list(itertools.chain(week1, week2))\n"
                            "print(all_days)  # ['월', '화', '수', '목', '금', '토', '일']\n\n"
                            "# islice: 무한 제너레이터에서 필요한 개수만 추출\n"
                            "from itertools import islice\n"
                            "first_5_fibs = list(islice(fibonacci(), 5))  # 앞서 정의한 fibonacci()\n"
                            "print(first_5_fibs)  # [0, 1, 1, 2, 3]\n\n"
                            "# product: 시험 번호 조합 생성\n"
                            "subjects = ['국어', '수학']\n"
                            "difficulties = ['A형', 'B형']\n"
                            "combos = list(itertools.product(subjects, difficulties))\n"
                            "print(combos)\n"
                            "# [('국어', 'A형'), ('국어', 'B형'), ('수학', 'A형'), ('수학', 'B형')]"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import itertools\n\n"
                            "# groupby: 연속된 같은 값끼리 묶기 (정렬 후 사용해야 함)\n"
                            "soldiers = [\n"
                            "    {'name': '김철수', 'rank': '이병'},\n"
                            "    {'name': '이영희', 'rank': '일병'},\n"
                            "    {'name': '박민수', 'rank': '이병'},\n"
                            "    {'name': '정수진', 'rank': '일병'},\n"
                            "]\n\n"
                            "# 계급별로 그룹화 (먼저 정렬)\n"
                            "sorted_soldiers = sorted(soldiers, key=lambda s: s['rank'])\n"
                            "for rank, group in itertools.groupby(sorted_soldiers, key=lambda s: s['rank']):\n"
                            "    names = [s['name'] for s in group]\n"
                            "    print(f'{rank}: {names}')\n"
                            "# 이병: ['김철수', '박민수']\n"
                            "# 일병: ['이영희', '정수진']"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "`itertools.groupby()`는 연속된 같은 키끼리만 묶습니다. "
                            "반드시 같은 키 기준으로 먼저 `sorted()`를 적용한 뒤 사용하세요. "
                            "정렬하지 않으면 예상과 다른 결과가 나옵니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 — 대용량 파일 처리 ──────────────────
            {
                "title": "실용 예제: 대용량 로그 파일 처리",
                "content": [
                    "제너레이터의 가장 강력한 활용 분야는 대용량 파일 처리입니다. "
                    "GB 단위의 로그 파일도 메모리에 올리지 않고 처리할 수 있습니다.",
                    {
                        "type": "heading",
                        "text": "메모리 사용량 비교",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 나쁜 방법: 전체 파일을 메모리에 올림\n"
                            "def count_errors_bad(filepath):\n"
                            "    \"\"\"파일 전체를 메모리에 올린 후 ERROR 수를 센다.\"\"\"\n"
                            "    with open(filepath, 'r', encoding='utf-8') as f:\n"
                            "        lines = f.readlines()  # 100만 줄 → 수백 MB 메모리!\n"
                            "    return sum(1 for line in lines if 'ERROR' in line)\n\n\n"
                            "# 좋은 방법: 제너레이터로 한 줄씩 처리\n"
                            "def count_errors_good(filepath):\n"
                            "    \"\"\"파일을 한 줄씩 읽으며 ERROR 수를 센다.\"\"\"\n"
                            "    with open(filepath, 'r', encoding='utf-8') as f:\n"
                            "        # 파일 객체 자체가 이터레이터 (한 줄씩 생성)\n"
                            "        return sum(1 for line in f if 'ERROR' in line)\n"
                            "    # 어느 시점에도 파일 전체가 메모리에 올라가지 않음"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "제너레이터 파이프라인",
                    },
                    "제너레이터를 연결하면 데이터 처리 파이프라인을 구성할 수 있습니다. "
                    "각 단계가 필요한 만큼만 데이터를 처리하므로 매우 효율적입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def read_log_lines(filepath):\n"
                            "    \"\"\"로그 파일에서 줄을 하나씩 생성한다.\"\"\"\n"
                            "    with open(filepath, 'r', encoding='utf-8') as f:\n"
                            "        for line in f:\n"
                            "            yield line.strip()\n\n\n"
                            "def filter_errors(lines):\n"
                            "    \"\"\"ERROR 레벨 로그만 통과시킨다.\"\"\"\n"
                            "    for line in lines:\n"
                            "        if 'ERROR' in line:\n"
                            "            yield line\n\n\n"
                            "def parse_log_entry(lines):\n"
                            "    \"\"\"로그 줄을 딕셔너리로 파싱한다.\"\"\"\n"
                            "    import re\n"
                            "    pattern = r'(?P<timestamp>[\\d-]+ [\\d:]+) (?P<level>\\w+): (?P<message>.+)'\n"
                            "    for line in lines:\n"
                            "        m = re.match(pattern, line)\n"
                            "        if m:\n"
                            "            yield m.groupdict()\n\n\n"
                            "# 파이프라인 구성 — 각 단계가 필요할 때만 동작\n"
                            "def process_log_pipeline(filepath):\n"
                            "    \"\"\"로그 파일을 파이프라인으로 처리한다.\"\"\"\n"
                            "    lines = read_log_lines(filepath)    # 단계 1: 읽기\n"
                            "    errors = filter_errors(lines)       # 단계 2: 필터\n"
                            "    entries = parse_log_entry(errors)   # 단계 3: 파싱\n"
                            "    return entries  # 이 시점에 실제 처리는 시작되지 않음!\n\n\n"
                            "# 실제 처리는 여기서 시작 (가상 파일 경로)\n"
                            "# for entry in process_log_pipeline('app.log'):\n"
                            "#     print(entry['timestamp'], entry['message'])"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "이 파이프라인 패턴은 MLOps에서 데이터 전처리 파이프라인과 구조가 동일합니다. "
                            "pandas의 method chaining, scikit-learn의 Pipeline, "
                            "Apache Spark의 DataFrame 변환 모두 이 아이디어를 기반으로 합니다. "
                            "제너레이터를 이해하면 대용량 ML 데이터셋 처리 코드를 자연스럽게 작성할 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "대용량 파일(수백 MB 이상)은 readlines() 대신 for 루프로 직접 순회하세요. 파일 객체는 이터레이터입니다.",
            "한 번만 사용할 데이터는 리스트 대신 제너레이터 표현식을 사용해 메모리를 절약하세요.",
            "무한 제너레이터를 사용할 때는 항상 itertools.islice()나 break 조건을 함께 준비하세요.",
            "sum(), any(), all(), max(), min() 등 내장 함수는 제너레이터를 직접 받으므로 list()로 변환하지 않아도 됩니다.",
            "yield from 문법을 사용하면 다른 이터러블의 모든 항목을 간단히 위임할 수 있습니다: `yield from range(10)`.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 이터레이터(Iterator)의 특징으로 올바른 것은?",
                "choices": [
                    "A) 여러 번 순회할 수 있다.",
                    "B) __iter__()와 __next__() 메서드를 모두 가진다.",
                    "C) 모든 값을 메모리에 저장한다.",
                    "D) list와 동일한 타입이다.",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "리스트 컴프리헨션 대신 제너레이터 표현식을 사용해야 하는 경우는?",
                "choices": [
                    "A) 같은 데이터를 여러 번 순회할 때",
                    "B) 결과를 인덱스로 접근해야 할 때",
                    "C) 수백만 개의 요소를 한 번만 처리할 때",
                    "D) 정렬이 필요할 때",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "1부터 n까지 홀수만 하나씩 생성하는 제너레이터 함수 "
                    "`odd_numbers(n)`을 작성하세요. "
                    "예: odd_numbers(10) → 1, 3, 5, 7, 9"
                ),
                "hint": "for 루프와 if 조건, yield를 조합하세요. 또는 range(1, n+1, 2)를 활용하세요.",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "문자열 리스트를 받아 길이가 5 이상인 단어만 대문자로 변환해 "
                    "반환하는 제너레이터 표현식을 작성하세요. "
                    "예: ['cat', 'elephant', 'dog', 'python'] → 'ELEPHANT', 'PYTHON'"
                ),
                "hint": "제너레이터 표현식 (word.upper() for word in words if len(word) >= 5) 을 활용하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "itertools.chain을 사용하여 여러 개의 숫자 리스트를 하나로 합친 후 "
                    "전체 합계를 구하는 함수 `total_sum(*lists)`를 작성하세요. "
                    "예: total_sum([1,2], [3,4], [5]) → 15"
                ),
                "hint": "itertools.chain(*lists)로 연결하고 sum()으로 합산하세요.",
            },
        ],
        "challenge": {
            "question": (
                "대용량 CSV 파일을 처리하는 제너레이터 파이프라인을 구성하세요. "
                "파일의 각 줄을 딕셔너리로 파싱하는 `parse_csv(filepath)` 제너레이터, "
                "특정 컬럼의 값이 조건을 만족하는 행만 통과시키는 `filter_rows(rows, column, threshold)` 제너레이터, "
                "특정 컬럼 값만 추출하는 `extract_column(rows, column)` 제너레이터를 각각 작성하고 "
                "파이프라인으로 연결하여 '점수가 80 이상인 학생의 이름 목록'을 출력하는 코드를 완성하세요. "
                "(실제 파일 없이 테스트용 문자열 데이터로 검증하세요.)"
            ),
            "hint": (
                "parse_csv에서 첫 줄을 헤더로 파싱하고 나머지를 딕셔너리로 yield하세요. "
                "io.StringIO를 사용하면 실제 파일 없이 문자열을 파일처럼 읽을 수 있습니다. "
                "각 제너레이터 함수가 이전 단계의 이터레이터를 인자로 받도록 설계하세요."
            ),
        },
        "summary": [
            "이터러블은 순회 가능한 객체이고, 이터레이터는 next()로 값을 하나씩 꺼내는 객체다.",
            "이터레이터 프로토콜: __iter__()는 자신을 반환하고, __next__()는 다음 값 또는 StopIteration을 반환한다.",
            "제너레이터 함수는 yield를 사용하며, 호출 시 값을 즉시 반환하지 않고 이터레이터를 생성한다.",
            "yield는 실행을 일시 중단하고 값을 반환한다. 다음 next() 호출 시 중단된 곳부터 재개된다.",
            "제너레이터 표현식 (...)은 리스트 컴프리헨션 [...]과 달리 값을 즉시 계산하지 않아 메모리 효율적이다.",
            "itertools 모듈(chain, islice, product, groupby 등)은 이터레이터 처리를 위한 강력한 도구를 제공한다.",
        ],
    }
