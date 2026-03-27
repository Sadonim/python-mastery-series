"""챕터 8: 데코레이터와 컨텍스트 매니저 — 함수를 강화하고 자원을 안전하게 관리하는 기술."""


def get_chapter():
    """챕터 8 콘텐츠를 반환한다."""
    return {
        "number": 8,
        "title": "데코레이터와 컨텍스트 매니저",
        "subtitle": "함수를 강화하고 자원을 안전하게 관리하는 기술",
        "big_picture": (
            "모든 API 함수에 실행 시간 측정 코드를 추가해야 한다면, "
            "함수마다 같은 코드를 복사·붙여넣기 해야 할까요? "
            "데코레이터는 이런 반복을 없애주는 강력한 도구입니다. "
            "함수에 @데코레이터 한 줄만 붙이면 로깅, 인증 확인, 성능 측정 등 "
            "부가 기능을 원본 코드를 건드리지 않고 추가할 수 있습니다. "
            "컨텍스트 매니저는 파일, DB 연결, 네트워크 소켓 등 "
            "자원을 예외가 발생해도 반드시 안전하게 닫아주는 패턴입니다."
        ),
        "sections": [
            # ── 섹션 1: 일급 객체로서의 함수와 클로저 ──────────────
            {
                "title": "일급 객체로서의 함수와 클로저",
                "content": [
                    "데코레이터를 이해하려면 먼저 Python에서 함수가 **일급 객체(first-class object)**라는 것을 알아야 합니다. "
                    "함수를 변수에 저장하고, 다른 함수의 인자로 전달하고, 함수의 반환값으로 사용할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 함수를 변수에 할당\n"
                            "def greet(name):\n"
                            "    return f'안녕하세요, {name}님!'\n\n"
                            "say_hello = greet        # 함수 자체를 변수에 저장 (호출 X)\n"
                            "print(say_hello('김철수'))  # 안녕하세요, 김철수님!\n\n"
                            "# 함수를 인자로 전달\n"
                            "def apply(func, value):\n"
                            "    return func(value)\n\n"
                            "result = apply(greet, '이영희')\n"
                            "print(result)  # 안녕하세요, 이영희님!\n\n"
                            "# 함수를 반환값으로 사용\n"
                            "def make_multiplier(n):\n"
                            "    def multiplier(x):\n"
                            "        return x * n    # n은 바깥 함수의 변수\n"
                            "    return multiplier   # 내부 함수를 반환\n\n"
                            "double = make_multiplier(2)\n"
                            "triple = make_multiplier(3)\n"
                            "print(double(5))  # 10\n"
                            "print(triple(5))  # 15"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "클로저(Closure): 바깥 변수를 기억하는 함수",
                    },
                    "위 `make_multiplier` 예제에서 `multiplier` 함수는 바깥 함수의 변수 `n`을 "
                    "기억합니다. 이처럼 **자신이 정의된 환경의 변수를 기억하는 함수**를 클로저라고 합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def make_counter(start=0):\n"
                            "    \"\"\"독립적인 카운터 클로저를 반환한다.\"\"\"\n"
                            "    count = [start]  # 리스트로 감싸면 내부에서 수정 가능\n\n"
                            "    def counter():\n"
                            "        count[0] += 1\n"
                            "        return count[0]\n\n"
                            "    return counter\n\n"
                            "# 각 카운터는 독립적인 상태를 유지\n"
                            "counter_a = make_counter()\n"
                            "counter_b = make_counter(10)\n\n"
                            "print(counter_a())  # 1\n"
                            "print(counter_a())  # 2\n"
                            "print(counter_b())  # 11  ← 서로 독립적\n"
                            "print(counter_a())  # 3"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "클로저는 데코레이터의 핵심 메커니즘입니다. "
                            "데코레이터가 원본 함수를 감싸는 래퍼(wrapper) 함수를 반환할 때, "
                            "그 래퍼 함수가 원본 함수를 클로저로 기억하는 것입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 데코레이터 기초 ──────────────────────────────
            {
                "title": "데코레이터 기초",
                "content": [
                    "**데코레이터(decorator)**는 함수를 입력받아, "
                    "기능이 추가된 새로운 함수를 반환하는 함수입니다. "
                    "`@데코레이터` 문법은 이 과정을 간결하게 표현합니다.",
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "원본 함수 정의 (def my_func)"},
                            {"label": "@decorator 적용", "color": "#3182F6"},
                            {"label": "my_func = decorator(my_func)"},
                            {"label": "my_func() 호출 → 강화된 버전 실행", "color": "#03b26c"},
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 데코레이터를 직접 만들어보기\n"
                            "def log_call(func):\n"
                            "    \"\"\"함수 호출을 로깅하는 데코레이터.\"\"\"\n\n"
                            "    def wrapper(*args, **kwargs):  # 원본 함수의 인자를 모두 받음\n"
                            "        print(f'[호출] {func.__name__} 시작')\n"
                            "        result = func(*args, **kwargs)  # 원본 함수 실행\n"
                            "        print(f'[완료] {func.__name__} 종료')\n"
                            "        return result\n\n"
                            "    return wrapper  # 강화된 wrapper 함수를 반환\n\n\n"
                            "# @log_call 은 아래와 동일:\n"
                            "# say_hi = log_call(say_hi)\n"
                            "@log_call\n"
                            "def say_hi(name):\n"
                            "    print(f'안녕하세요, {name}님!')\n\n"
                            "say_hi('박민수')\n"
                            "# [호출] say_hi 시작\n"
                            "# 안녕하세요, 박민수님!\n"
                            "# [완료] say_hi 종료"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "functools.wraps — 원본 함수 정보 보존",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from functools import wraps\n\n"
                            "def log_call(func):\n"
                            "    @wraps(func)  # 원본 함수의 __name__, __doc__ 등을 유지\n"
                            "    def wrapper(*args, **kwargs):\n"
                            "        print(f'[호출] {func.__name__}')\n"
                            "        return func(*args, **kwargs)\n"
                            "    return wrapper\n\n"
                            "@log_call\n"
                            "def calculate(a, b):\n"
                            "    \"\"\"두 수의 합을 계산한다.\"\"\"\n"
                            "    return a + b\n\n"
                            "# @wraps 없으면: calculate.__name__ == 'wrapper'\n"
                            "# @wraps 있으면: calculate.__name__ == 'calculate' (원본 보존)\n"
                            "print(calculate.__name__)  # calculate\n"
                            "print(calculate.__doc__)   # 두 수의 합을 계산한다."
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "데코레이터를 만들 때는 항상 `@functools.wraps(func)`를 붙이세요. "
                            "이것이 없으면 디버깅, 로깅, 문서화 도구들이 wrapper 함수를 "
                            "원본 함수로 오인하여 혼란이 생깁니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 인자 있는 데코레이터와 실용 예제 ──────────────
            {
                "title": "인자 있는 데코레이터와 실용 예제",
                "content": [
                    "데코레이터 자체가 인자를 받으려면 래핑 단계가 하나 더 필요합니다. "
                    "`@decorator(인자)`는 `func = decorator(인자)(func)` 와 동일합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from functools import wraps\n"
                            "import time\n\n"
                            "# 실행 시간 측정 데코레이터 (재시도 횟수 인자)\n"
                            "def retry(max_attempts=3, delay=1.0):\n"
                            "    \"\"\"지정한 횟수만큼 재시도하는 데코레이터.\"\"\"\n"
                            "    def decorator(func):\n"
                            "        @wraps(func)\n"
                            "        def wrapper(*args, **kwargs):\n"
                            "            for attempt in range(1, max_attempts + 1):\n"
                            "                try:\n"
                            "                    return func(*args, **kwargs)\n"
                            "                except Exception as e:\n"
                            "                    if attempt == max_attempts:\n"
                            "                        raise  # 마지막 시도에서 예외 재발생\n"
                            "                    print(f'시도 {attempt} 실패: {e}. {delay}초 후 재시도...')\n"
                            "                    time.sleep(delay)\n"
                            "        return wrapper\n"
                            "    return decorator\n\n\n"
                            "@retry(max_attempts=3, delay=0.5)\n"
                            "def fetch_data(url):\n"
                            "    \"\"\"외부 API에서 데이터를 가져온다.\"\"\"\n"
                            "    # 실제로는 requests.get() 등을 사용\n"
                            "    raise ConnectionError('서버 응답 없음')  # 예시용\n\n"
                            "# try:\n"
                            "#     fetch_data('https://api.example.com/data')\n"
                            "# except ConnectionError:\n"
                            "#     print('최종 실패')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실행 시간 측정 데코레이터",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from functools import wraps\n"
                            "import time\n\n"
                            "def timer(func):\n"
                            "    \"\"\"함수 실행 시간을 측정하는 데코레이터.\"\"\"\n"
                            "    @wraps(func)\n"
                            "    def wrapper(*args, **kwargs):\n"
                            "        start = time.perf_counter()  # 고정밀 타이머\n"
                            "        result = func(*args, **kwargs)\n"
                            "        elapsed = time.perf_counter() - start\n"
                            "        print(f'[{func.__name__}] 실행 시간: {elapsed:.4f}초')\n"
                            "        return result  # 원본 반환값을 그대로 전달\n"
                            "    return wrapper\n\n\n"
                            "@timer\n"
                            "def process_data(n):\n"
                            "    \"\"\"n개의 소수를 찾는다.\"\"\"\n"
                            "    primes = []\n"
                            "    for i in range(2, n):\n"
                            "        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):\n"
                            "            primes.append(i)\n"
                            "    return primes\n\n"
                            "result = process_data(1000)\n"
                            "print(f'소수 {len(result)}개 발견')\n"
                            "# [process_data] 실행 시간: 0.0032초\n"
                            "# 소수 168개 발견"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "데코레이터는 여러 개를 중첩할 수 있습니다. "
                            "적용 순서는 아래에서 위로, 실행 순서는 위에서 아래로:\n"
                            "```\n"
                            "@timer\n"
                            "@log_call\n"
                            "def my_func(): ...\n"
                            "# 실행 순서: timer → log_call → 원본 → log_call → timer\n"
                            "```"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 내장 데코레이터 ──────────────────────────────
            {
                "title": "내장 데코레이터: @property, @staticmethod, @classmethod",
                "content": [
                    "Python은 자주 쓰이는 패턴을 위한 내장 데코레이터를 제공합니다. "
                    "클래스를 작성할 때 매우 유용하게 활용됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Soldier:\n"
                            "    \"\"\"군인 정보를 관리하는 클래스.\"\"\"\n\n"
                            "    # 클래스 변수\n"
                            "    unit = '육군 1사단'\n\n"
                            "    def __init__(self, name, service_days):\n"
                            "        self._name = name                  # 이름 (외부 직접 수정 방지)\n"
                            "        self._service_days = service_days  # 복무일수\n\n"
                            "    # @property: 메서드를 속성처럼 접근 (getter)\n"
                            "    @property\n"
                            "    def name(self):\n"
                            "        \"\"\"이름을 반환한다.\"\"\"\n"
                            "        return self._name\n\n"
                            "    @property\n"
                            "    def remaining_days(self):\n"
                            "        \"\"\"전역까지 남은 일수를 계산하여 반환한다.\"\"\"\n"
                            "        total = 18 * 30  # 약 18개월\n"
                            "        return max(0, total - self._service_days)\n\n"
                            "    # @property.setter: 속성 쓰기 제어\n"
                            "    @name.setter\n"
                            "    def name(self, new_name):\n"
                            "        if not new_name.strip():\n"
                            "            raise ValueError('이름은 빈 문자열일 수 없습니다.')\n"
                            "        self._name = new_name\n\n"
                            "    # @staticmethod: self 불필요, 클래스와 관련된 유틸 함수\n"
                            "    @staticmethod\n"
                            "    def is_valid_service_days(days):\n"
                            "        \"\"\"복무일수가 유효한지 검증한다.\"\"\"\n"
                            "        return 0 <= days <= 550\n\n"
                            "    # @classmethod: 클래스 자체를 인자로 받음, 팩토리 메서드에 활용\n"
                            "    @classmethod\n"
                            "    def from_months(cls, name, months):\n"
                            "        \"\"\"월 단위로 복무 기간을 입력받아 Soldier를 생성한다.\"\"\"\n"
                            "        return cls(name, months * 30)\n\n\n"
                            "# 사용\n"
                            "soldier = Soldier('김철수', 200)\n"
                            "print(soldier.name)            # 김철수 (메서드지만 () 없이 접근)\n"
                            "print(soldier.remaining_days)  # 340\n"
                            "soldier.name = '김철수 이병'   # setter 통해 안전하게 수정\n\n"
                            "# 정적 메서드: 인스턴스 없이 호출\n"
                            "print(Soldier.is_valid_service_days(200))  # True\n\n"
                            "# 클래스 메서드로 다른 방식으로 생성\n"
                            "s2 = Soldier.from_months('이영희', 6)\n"
                            "print(s2._service_days)  # 180"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["데코레이터", "첫 번째 인자", "용도"],
                        "rows": [
                            ["(일반 메서드)", "self (인스턴스)", "인스턴스 데이터 접근/수정"],
                            ["@property", "self (인스턴스)", "속성처럼 사용되는 getter/setter"],
                            ["@staticmethod", "없음", "클래스와 관련된 독립 유틸 함수"],
                            ["@classmethod", "cls (클래스 자체)", "팩토리 메서드, 클래스 변수 조작"],
                        ],
                    },
                ],
            },
            # ── 섹션 5: 컨텍스트 매니저 ─────────────────────────────
            {
                "title": "컨텍스트 매니저: with문과 __enter__/__exit__",
                "content": [
                    "`with` 문은 자원을 안전하게 관리하기 위한 Python의 핵심 문법입니다. "
                    "예외가 발생하더라도 자원(파일, DB 연결, 락 등)이 반드시 해제되도록 보장합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# with 없이: 예외 발생 시 파일이 닫히지 않을 수 있음\n"
                            "f = open('data.txt', 'r', encoding='utf-8')\n"
                            "try:\n"
                            "    data = f.read()\n"
                            "finally:\n"
                            "    f.close()  # 반드시 닫아야 함\n\n"
                            "# with 사용: __exit__가 자동으로 close() 호출\n"
                            "with open('data.txt', 'r', encoding='utf-8') as f:\n"
                            "    data = f.read()\n"
                            "# 블록을 벗어나면 예외 여부와 무관하게 파일이 닫힘"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "__enter__와 __exit__ 구현",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class DatabaseConnection:\n"
                            "    \"\"\"DB 연결을 컨텍스트 매니저로 관리하는 클래스.\"\"\"\n\n"
                            "    def __init__(self, host, db_name):\n"
                            "        self._host = host\n"
                            "        self._db_name = db_name\n"
                            "        self._conn = None\n\n"
                            "    def __enter__(self):\n"
                            "        \"\"\"with 블록 진입 시 호출. 연결을 열고 self를 반환.\"\"\"\n"
                            "        print(f'{self._host}/{self._db_name} 연결 중...')\n"
                            "        self._conn = {'status': 'connected'}  # 실제로는 DB 연결\n"
                            "        return self  # as 뒤의 변수에 할당됨\n\n"
                            "    def __exit__(self, exc_type, exc_val, exc_tb):\n"
                            "        \"\"\"\n"
                            "        with 블록 종료 시 호출 (예외 발생 여부 무관).\n"
                            "        exc_type: 예외 타입 (정상이면 None)\n"
                            "        False 반환 시 예외가 전파됨 (권장)\n"
                            "        \"\"\"\n"
                            "        if self._conn:\n"
                            "            print('연결 종료')\n"
                            "            self._conn = None\n"
                            "        if exc_type:\n"
                            "            print(f'예외 발생: {exc_val}')\n"
                            "        return False  # 예외를 다시 발생시킴\n\n"
                            "    def query(self, sql):\n"
                            "        \"\"\"SQL을 실행한다.\"\"\"\n"
                            "        return f'{sql} 실행 결과'\n\n\n"
                            "# 사용\n"
                            "with DatabaseConnection('localhost', 'mydb') as db:\n"
                            "    result = db.query('SELECT * FROM users')\n"
                            "    print(result)\n"
                            "# localhost/mydb 연결 중...\n"
                            "# SELECT * FROM users 실행 결과\n"
                            "# 연결 종료"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "__exit__ 메서드는 세 가지 예외 관련 인자를 받습니다:\n"
                            "- exc_type: 예외 클래스 (없으면 None)\n"
                            "- exc_val: 예외 인스턴스 (없으면 None)\n"
                            "- exc_tb: 트레이스백 (없으면 None)\n\n"
                            "True를 반환하면 예외를 '삼켜' 전파를 막습니다 (드물게 사용).\n"
                            "False(또는 None)를 반환하면 예외가 정상적으로 전파됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: contextlib과 실용 예제 ──────────────────────
            {
                "title": "contextlib.contextmanager와 실용 예제",
                "content": [
                    "`contextlib.contextmanager` 데코레이터를 사용하면 "
                    "__enter__/__exit__ 클래스 없이도 제너레이터 함수로 "
                    "컨텍스트 매니저를 간단히 만들 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from contextlib import contextmanager\n"
                            "import time\n\n"
                            "@contextmanager\n"
                            "def timer_context(label):\n"
                            "    \"\"\"코드 블록의 실행 시간을 측정하는 컨텍스트 매니저.\"\"\"\n"
                            "    start = time.perf_counter()\n"
                            "    try:\n"
                            "        yield  # with 블록이 여기서 실행됨\n"
                            "    finally:\n"
                            "        elapsed = time.perf_counter() - start\n"
                            "        print(f'[{label}] {elapsed:.4f}초')\n\n\n"
                            "# 사용\n"
                            "with timer_context('데이터 처리'):\n"
                            "    # 처리할 작업\n"
                            "    total = sum(i ** 2 for i in range(100_000))\n"
                            "    print(f'합계: {total}')\n"
                            "# 합계: 333328333350000\n"
                            "# [데이터 처리] 0.0089초"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "로깅 데코레이터 (완성 예제)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from functools import wraps\n"
                            "import logging\n"
                            "import time\n\n"
                            "logging.basicConfig(\n"
                            "    level=logging.INFO,\n"
                            "    format='%(asctime)s [%(levelname)s] %(message)s'\n"
                            ")\n"
                            "logger = logging.getLogger(__name__)\n\n\n"
                            "def log_performance(func):\n"
                            "    \"\"\"함수 호출, 인자, 실행 시간, 반환값을 로깅하는 데코레이터.\"\"\"\n"
                            "    @wraps(func)\n"
                            "    def wrapper(*args, **kwargs):\n"
                            "        logger.info(f'{func.__name__} 호출 — args={args}, kwargs={kwargs}')\n"
                            "        start = time.perf_counter()\n"
                            "        try:\n"
                            "            result = func(*args, **kwargs)\n"
                            "            elapsed = time.perf_counter() - start\n"
                            "            logger.info(f'{func.__name__} 완료 — {elapsed:.4f}초, 반환값={result!r}')\n"
                            "            return result\n"
                            "        except Exception as e:\n"
                            "            elapsed = time.perf_counter() - start\n"
                            "            logger.error(f'{func.__name__} 실패 — {elapsed:.4f}초, 오류={e}')\n"
                            "            raise  # 예외를 다시 발생시켜 호출자에게 전달\n"
                            "    return wrapper\n\n\n"
                            "@log_performance\n"
                            "def calculate_bmi(weight_kg, height_m):\n"
                            "    \"\"\"BMI(체질량지수)를 계산하여 반환한다.\"\"\"\n"
                            "    if height_m <= 0:\n"
                            "        raise ValueError('키는 0보다 커야 합니다.')\n"
                            "    bmi = weight_kg / (height_m ** 2)\n"
                            "    return round(bmi, 2)\n\n"
                            "print(calculate_bmi(70, 1.75))  # 약 22.86\n"
                            "# 로그: calculate_bmi 호출 → 완료"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "복수의 with 문 관리",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 여러 컨텍스트 매니저를 한 줄에\n"
                            "with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:\n"
                            "    for line in fin:\n"
                            "        fout.write(line.upper())\n\n"
                            "# contextlib.suppress: 특정 예외를 무시하는 컨텍스트 매니저\n"
                            "from contextlib import suppress\n\n"
                            "with suppress(FileNotFoundError):\n"
                            "    import os\n"
                            "    os.remove('temp_file.tmp')  # 파일이 없어도 예외 없이 통과\n\n"
                            "# contextlib.ExitStack: 동적으로 컨텍스트 매니저 관리\n"
                            "from contextlib import ExitStack\n\n"
                            "filenames = ['a.txt', 'b.txt', 'c.txt']\n"
                            "with ExitStack() as stack:\n"
                            "    # 파일 수가 런타임에 결정될 때 유용\n"
                            "    files = [stack.enter_context(open(f, 'w')) for f in filenames]\n"
                            "    for f in files:\n"
                            "        f.write('테스트')\n"
                            "# 블록 종료 시 모든 파일이 자동으로 닫힘"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "MLOps에서 컨텍스트 매니저의 활용:\n"
                            "- torch.no_grad(): 추론 시 그래디언트 계산 비활성화\n"
                            "- mlflow.start_run(): 실험 실행 세션 관리\n"
                            "- tf.device('/GPU:0'): 특정 장치에서 연산 실행\n"
                            "이 모두 __enter__/__exit__ 프로토콜을 구현한 컨텍스트 매니저입니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "데코레이터를 만들 때 @functools.wraps(func)를 빠뜨리지 마세요. 디버깅과 문서화 도구들이 올바르게 동작하려면 필수입니다.",
            "파일, DB 연결, 네트워크 소켓은 항상 with 문으로 열고 닫으세요. try/finally보다 간결하고 안전합니다.",
            "@contextmanager를 사용하면 클래스 없이도 컨텍스트 매니저를 빠르게 만들 수 있습니다.",
            "@property를 사용하면 내부 구현을 바꿔도 외부 인터페이스를 유지할 수 있습니다.",
            "데코레이터가 너무 복잡해지면 클래스 기반 데코레이터(`__call__` 메서드 구현)로 전환하는 것도 고려하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 @functools.wraps(func)를 데코레이터에 사용하는 이유로 올바른 것은?",
                "choices": [
                    "A) 데코레이터의 실행 속도를 높이기 위해",
                    "B) 원본 함수의 __name__, __doc__ 등 메타데이터를 wrapper 함수에 복사하기 위해",
                    "C) 데코레이터를 클래스 메서드에도 사용할 수 있게 하기 위해",
                    "D) 중첩 데코레이터를 허용하기 위해",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "컨텍스트 매니저의 __exit__ 메서드에서 True를 반환하면 어떤 일이 발생하는가?",
                "choices": [
                    "A) with 블록이 다시 실행된다.",
                    "B) 발생한 예외가 억제되어 전파되지 않는다.",
                    "C) 다음 컨텍스트 매니저로 넘어간다.",
                    "D) 프로그램이 즉시 종료된다.",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "함수 호출 횟수를 세어 출력하는 데코레이터 `count_calls`를 작성하세요. "
                    "예: @count_calls를 붙인 함수를 3번 호출하면 "
                    "'greet 함수가 3번 호출되었습니다.' 라고 출력되어야 합니다."
                ),
                "hint": "wrapper 함수 바깥에 count 변수(리스트 또는 nonlocal)를 두고 호출 시마다 증가시키세요.",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "@contextmanager를 사용하여 코드 블록 실행 전후에 "
                    "'=== 시작 ===' 과 '=== 종료 ===' 를 출력하는 "
                    "컨텍스트 매니저 `section(title)`을 작성하세요. "
                    "예: with section('데이터 처리'): → '=== 데이터 처리 시작 ===', '=== 데이터 처리 종료 ==='"
                ),
                "hint": "contextlib.contextmanager 데코레이터와 yield를 사용하세요. try/finally로 예외 시에도 종료 메시지가 출력되게 하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "Circle 클래스를 만드세요. "
                    "반지름(radius)을 @property로 구현하고, "
                    "0 이하의 값을 설정하면 ValueError를 발생시키는 setter를 추가하세요. "
                    "넓이(area)를 계산하는 @property도 추가하세요 (math.pi 사용)."
                ),
                "hint": "self._radius로 내부 저장, @radius.setter에서 유효성 검사, area property에서 math.pi * self._radius ** 2를 반환하세요.",
            },
        ],
        "challenge": {
            "question": (
                "함수 결과를 캐싱하는 `@memoize` 데코레이터를 직접 구현하세요. "
                "같은 인자로 호출될 때 이전에 계산한 결과를 딕셔너리에서 꺼내 반환합니다. "
                "재귀적인 `fibonacci(n)` 함수에 적용하여 성능 차이를 측정하세요. "
                "(참고: Python 표준 라이브러리에는 functools.lru_cache가 있지만, "
                "이 문제는 직접 구현하는 연습입니다.)"
            ),
            "hint": (
                "wrapper 바깥에 cache = {} 딕셔너리를 두세요. "
                "args를 키로 사용합니다 (args는 튜플이므로 해시 가능). "
                "kwargs가 있다면 tuple(sorted(kwargs.items()))를 키에 포함하세요. "
                "time.perf_counter()로 memoize 적용 전후의 fibonacci(35) 실행 시간을 비교하세요."
            ),
        },
        "summary": [
            "Python에서 함수는 일급 객체다. 변수에 저장하고, 인자로 전달하고, 반환값으로 사용할 수 있다.",
            "클로저는 자신이 정의된 환경의 변수를 기억하는 함수다. 데코레이터의 핵심 메커니즘이다.",
            "데코레이터는 @문법으로 함수에 부가 기능을 추가한다. 항상 @functools.wraps(func)를 함께 사용하라.",
            "인자 있는 데코레이터는 한 겹 더 감싸는 구조(decorator factory)로 구현한다.",
            "@property는 메서드를 속성처럼 사용하게 하고, @staticmethod와 @classmethod는 클래스 설계에 활용된다.",
            "컨텍스트 매니저(with 문)는 __enter__/__exit__ 또는 @contextmanager로 구현하며, 자원을 안전하게 관리한다.",
        ],
    }
