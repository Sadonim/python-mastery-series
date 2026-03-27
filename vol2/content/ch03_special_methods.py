"""챕터 3: 특수 메서드와 연산자 오버로딩 — 파이썬스러운 클래스 만들기."""


def get_chapter():
    """챕터 3 콘텐츠를 반환한다."""
    return {
        "number": 3,
        "title": "특수 메서드와 연산자 오버로딩",
        "subtitle": "파이썬스러운 클래스 만들기",
        "big_picture": (
            "Python에서 `len(obj)`, `obj + other`, `obj[0]` 같은 표현이 "
            "동작하는 비밀은 '특수 메서드(Special Methods)'에 있습니다. "
            "앞뒤를 밑줄 두 개로 감싼 `__dunder__` 메서드를 클래스에 구현하면 "
            "내가 만든 객체가 Python 내장 타입처럼 자연스럽게 동작합니다. "
            "이것이 '파이썬스러운(Pythonic)' 코드를 만드는 핵심 기술입니다."
        ),
        "sections": [
            # ── 섹션 1: 특수 메서드란 무엇인가 ──────────────────
            {
                "title": "특수 메서드란 무엇인가",
                "content": [
                    "특수 메서드(special methods)는 Python 인터프리터가 "
                    "특정 연산자나 내장 함수를 만났을 때 자동으로 호출하는 메서드입니다. "
                    "앞뒤에 밑줄 두 개(`__`)가 붙어 있어 '던더(dunder) 메서드'라고도 합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "특수 메서드는 계약서의 빈칸과 같습니다. "
                            "Python이라는 회사에서 '`+` 연산자를 지원하고 싶으면 "
                            "`__add__` 메서드를 구현하세요'라고 규격을 정해뒀습니다. "
                            "그 빈칸을 채우면 Python 생태계의 모든 연산과 매끄럽게 연동됩니다."
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "Python 코드: a + b"},
                            {"label": "인터프리터가 __add__ 탐색", "color": "#3182F6"},
                            {"label": "__add__(self, other) 실행"},
                            {"label": "결과 반환"},
                        ],
                    },
                    "특수 메서드는 절대로 직접 호출하지 않습니다. "
                    "`a.__add__(b)` 대신 `a + b`를 쓰세요. "
                    "Python이 적절한 특수 메서드를 자동으로 찾아 호출합니다.",
                    {
                        "type": "table",
                        "headers": ["카테고리", "특수 메서드", "대응하는 연산/함수"],
                        "rows": [
                            ["문자열 표현", "__str__", "str(obj), print(obj)"],
                            ["문자열 표현", "__repr__", "repr(obj), 대화형 셸 출력"],
                            ["비교", "__eq__", "obj == other"],
                            ["비교", "__lt__", "obj < other"],
                            ["비교", "__le__", "obj <= other"],
                            ["산술", "__add__", "obj + other"],
                            ["산술", "__sub__", "obj - other"],
                            ["산술", "__mul__", "obj * other"],
                            ["컬렉션", "__len__", "len(obj)"],
                            ["컬렉션", "__getitem__", "obj[key]"],
                            ["컬렉션", "__contains__", "item in obj"],
                            ["호출", "__call__", "obj(args)"],
                            ["초기화", "__init__", "MyClass(args)"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python의 내장 타입도 모두 특수 메서드로 구현되어 있습니다. "
                            "`1 + 2`는 내부적으로 `int.__add__(1, 2)`를 호출합니다. "
                            "여러분의 클래스도 같은 방식으로 동작하게 만들 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 문자열 표현 __str__ vs __repr__ ──────────
            {
                "title": "문자열 표현: __str__ vs __repr__",
                "content": [
                    "객체를 문자열로 표현하는 방법은 두 가지입니다. "
                    "`__str__`은 사람이 읽기 좋은 형태, "
                    "`__repr__`은 개발자가 디버깅할 때 쓰는 공식적인 표현입니다.",
                    {
                        "type": "table",
                        "headers": ["메서드", "호출 방법", "목적", "원칙"],
                        "rows": [
                            ["__str__", "str(obj), print(obj)", "사용자용 출력", "읽기 쉽게"],
                            ["__repr__", "repr(obj), 대화형 셸", "개발자용 디버깅", "eval()로 복원 가능하게"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Point:\n"
                            "    \"\"\"2차원 좌표를 나타내는 클래스.\"\"\"\n\n"
                            "    def __init__(self, x, y):\n"
                            "        self.x = x\n"
                            "        self.y = y\n\n"
                            "    def __str__(self):\n"
                            "        \"\"\"사람이 읽기 좋은 문자열 반환.\"\"\"\n"
                            "        return f'({self.x}, {self.y})'\n\n"
                            "    def __repr__(self):\n"
                            "        \"\"\"개발자용 공식 표현 반환.\"\"\"\n"
                            "        return f'Point(x={self.x}, y={self.y})'\n\n\n"
                            "p = Point(3, 4)\n"
                            "print(p)           # (3, 4)         ← __str__ 사용\n"
                            "print(repr(p))     # Point(x=3, y=4) ← __repr__ 사용\n"
                            "print(str(p))      # (3, 4)\n\n"
                            "# 리스트 안에서는 __repr__이 사용됨\n"
                            "points = [Point(1, 2), Point(3, 4)]\n"
                            "print(points)      # [Point(x=1, y=2), Point(x=3, y=4)]"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "__repr__만 구현해도 __str__이 없을 때 자동으로 대체됩니다. "
                            "최소한 __repr__은 항상 구현하세요. "
                            "규칙: __repr__에서는 `MyClass(field=value)` 형태를 권장합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Temperature:\n"
                            "    \"\"\"섭씨 온도를 나타내는 클래스.\"\"\"\n\n"
                            "    def __init__(self, celsius):\n"
                            "        self.celsius = celsius\n\n"
                            "    def __repr__(self):\n"
                            "        return f'Temperature({self.celsius})'\n\n"
                            "    def __str__(self):\n"
                            "        return f'{self.celsius}°C'\n\n\n"
                            "t = Temperature(36.5)\n"
                            "print(f'체온: {t}')    # 체온: 36.5°C\n"
                            "print(repr(t))         # Temperature(36.5)"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 비교 연산자 오버로딩 ─────────────────────
            {
                "title": "비교 연산자 오버로딩",
                "content": [
                    "클래스에 비교 연산자를 구현하면 `sorted()`, `min()`, `max()` 같은 "
                    "Python 내장 기능을 바로 사용할 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["연산자", "메서드", "의미"],
                        "rows": [
                            ["==", "__eq__(self, other)", "같다"],
                            ["!=", "__ne__(self, other)", "다르다 (__eq__ 반대로 자동 생성)"],
                            ["<", "__lt__(self, other)", "작다"],
                            ["<=", "__le__(self, other)", "작거나 같다"],
                            [">", "__gt__(self, other)", "크다"],
                            [">=", "__ge__(self, other)", "크거나 같다"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Student:\n"
                            "    \"\"\"학생을 나타내는 클래스 — 점수 기준 비교.\"\"\"\n\n"
                            "    def __init__(self, name, score):\n"
                            "        self.name = name\n"
                            "        self.score = score\n\n"
                            "    def __repr__(self):\n"
                            "        return f'Student({self.name!r}, {self.score})'\n\n"
                            "    def __eq__(self, other):\n"
                            "        \"\"\"점수가 같으면 동일한 등수로 본다.\"\"\"\n"
                            "        if not isinstance(other, Student):\n"
                            "            return NotImplemented\n"
                            "        return self.score == other.score\n\n"
                            "    def __lt__(self, other):\n"
                            "        \"\"\"점수가 낮으면 순위가 낮다.\"\"\"\n"
                            "        if not isinstance(other, Student):\n"
                            "            return NotImplemented\n"
                            "        return self.score < other.score\n\n\n"
                            "students = [\n"
                            "    Student('김철수', 88),\n"
                            "    Student('이영희', 95),\n"
                            "    Student('박민수', 72),\n"
                            "]\n\n"
                            "# sorted()가 __lt__를 자동으로 사용\n"
                            "sorted_students = sorted(students)\n"
                            "for s in sorted_students:\n"
                            "    print(f'{s.name}: {s.score}점')\n"
                            "# 박민수: 72점\n"
                            "# 김철수: 88점\n"
                            "# 이영희: 95점\n\n"
                            "print(max(students))  # Student('이영희', 95)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "`NotImplemented`를 반환하면 Python이 피연산자를 뒤집어 "
                            "다시 시도합니다. `return False`와 다르니 주의하세요. "
                            "타입이 다를 때는 반드시 `NotImplemented`를 반환하세요."
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "`functools.total_ordering` 데코레이터를 사용하면 "
                            "__eq__와 __lt__만 구현해도 나머지 4가지를 자동으로 생성합니다. "
                            "반복 작업을 줄이는 실용적인 방법입니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from functools import total_ordering\n\n\n"
                            "@total_ordering\n"
                            "class Score:\n"
                            "    \"\"\"점수 클래스 — total_ordering으로 모든 비교 연산 지원.\"\"\"\n\n"
                            "    def __init__(self, value):\n"
                            "        self.value = value\n\n"
                            "    def __eq__(self, other):\n"
                            "        return self.value == other.value\n\n"
                            "    def __lt__(self, other):\n"
                            "        return self.value < other.value\n\n\n"
                            "a, b = Score(80), Score(90)\n"
                            "print(a < b)    # True  ← __lt__\n"
                            "print(a > b)    # False ← total_ordering이 자동 생성\n"
                            "print(a <= b)   # True  ← total_ordering이 자동 생성"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 산술 연산자 오버로딩 ─────────────────────
            {
                "title": "산술 연산자 오버로딩",
                "content": [
                    "수학적 개념을 클래스로 표현할 때 산술 연산자를 구현하면 "
                    "코드가 훨씬 직관적이 됩니다. "
                    "대표적인 예가 벡터(Vector) 클래스입니다.",
                    {
                        "type": "table",
                        "headers": ["연산자", "메서드", "예시"],
                        "rows": [
                            ["+", "__add__(self, other)", "v1 + v2"],
                            ["-", "__sub__(self, other)", "v1 - v2"],
                            ["*", "__mul__(self, other)", "v1 * 3"],
                            ["*", "__rmul__(self, other)", "3 * v1 (역순)"],
                            ["/", "__truediv__(self, other)", "v1 / 2"],
                            ["-x (단항)", "__neg__(self)", "-v1"],
                            ["abs()", "__abs__(self)", "abs(v1)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import math\n\n\n"
                            "class Vector:\n"
                            "    \"\"\"2차원 벡터 클래스.\"\"\"\n\n"
                            "    def __init__(self, x, y):\n"
                            "        self.x = x\n"
                            "        self.y = y\n\n"
                            "    def __repr__(self):\n"
                            "        return f'Vector({self.x}, {self.y})'\n\n"
                            "    def __str__(self):\n"
                            "        return f'<{self.x}, {self.y}>'\n\n"
                            "    def __add__(self, other):\n"
                            "        \"\"\"벡터 덧셈 — 새 Vector를 반환한다 (불변).\"\"\"\n"
                            "        return Vector(self.x + other.x, self.y + other.y)\n\n"
                            "    def __sub__(self, other):\n"
                            "        \"\"\"벡터 뺄셈.\"\"\"\n"
                            "        return Vector(self.x - other.x, self.y - other.y)\n\n"
                            "    def __mul__(self, scalar):\n"
                            "        \"\"\"스칼라 곱셈.\"\"\"\n"
                            "        return Vector(self.x * scalar, self.y * scalar)\n\n"
                            "    def __rmul__(self, scalar):\n"
                            "        \"\"\"역순 스칼라 곱셈: 3 * v 형태 지원.\"\"\"\n"
                            "        return self.__mul__(scalar)\n\n"
                            "    def __neg__(self):\n"
                            "        \"\"\"벡터 부정 (방향 반전).\"\"\"\n"
                            "        return Vector(-self.x, -self.y)\n\n"
                            "    def __abs__(self):\n"
                            "        \"\"\"벡터 크기(magnitude) 반환.\"\"\"\n"
                            "        return math.sqrt(self.x ** 2 + self.y ** 2)\n\n"
                            "    def __eq__(self, other):\n"
                            "        return isinstance(other, Vector) and self.x == other.x and self.y == other.y\n\n\n"
                            "v1 = Vector(3, 4)\n"
                            "v2 = Vector(1, 2)\n\n"
                            "print(v1 + v2)      # <4, 6>\n"
                            "print(v1 - v2)      # <2, 2>\n"
                            "print(v1 * 2)       # <6, 8>\n"
                            "print(3 * v1)       # <9, 12>  ← __rmul__ 덕분\n"
                            "print(-v1)          # <-3, -4>\n"
                            "print(abs(v1))      # 5.0       ← 3-4-5 직각삼각형\n"
                            "print(v1 == Vector(3, 4))  # True"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "산술 연산자는 반드시 '새 객체'를 반환해야 합니다. "
                            "`self.x += other.x` 처럼 self를 수정하면 안 됩니다. "
                            "불변성을 지키는 것이 버그를 예방하는 핵심입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 컬렉션 프로토콜 ──────────────────────────
            {
                "title": "컬렉션 프로토콜: __len__, __getitem__, __contains__",
                "content": [
                    "클래스에 컬렉션 특수 메서드를 구현하면 "
                    "`len()`, 인덱싱(`[]`), `in` 연산자를 사용할 수 있습니다. "
                    "심지어 `for` 루프도 동작합니다.",
                    {
                        "type": "table",
                        "headers": ["메서드", "대응 문법", "설명"],
                        "rows": [
                            ["__len__(self)", "len(obj)", "길이 반환 (정수)"],
                            ["__getitem__(self, key)", "obj[key]", "항목 접근"],
                            ["__setitem__(self, key, val)", "obj[key] = val", "항목 설정"],
                            ["__delitem__(self, key)", "del obj[key]", "항목 삭제"],
                            ["__contains__(self, item)", "item in obj", "포함 여부"],
                            ["__iter__(self)", "for x in obj", "반복자 반환"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Squad:\n"
                            "    \"\"\"분대원 목록을 관리하는 클래스.\"\"\"\n\n"
                            "    def __init__(self, name):\n"
                            "        self.name = name\n"
                            "        self._members = []  # 내부 리스트 (외부 노출 금지)\n\n"
                            "    def add(self, member):\n"
                            "        \"\"\"분대원을 추가한다.\"\"\"\n"
                            "        self._members = self._members + [member]  # 불변: 새 리스트\n\n"
                            "    def __len__(self):\n"
                            "        \"\"\"분대 인원수를 반환한다.\"\"\"\n"
                            "        return len(self._members)\n\n"
                            "    def __getitem__(self, index):\n"
                            "        \"\"\"인덱스로 분대원에 접근한다.\"\"\"\n"
                            "        return self._members[index]\n\n"
                            "    def __contains__(self, member):\n"
                            "        \"\"\"분대원 여부를 확인한다.\"\"\"\n"
                            "        return member in self._members\n\n"
                            "    def __repr__(self):\n"
                            "        return f'Squad({self.name!r}, {self._members})'\n\n\n"
                            "squad = Squad('1분대')\n"
                            "squad.add('김병장')\n"
                            "squad.add('이상병')\n"
                            "squad.add('박일병')\n\n"
                            "print(len(squad))          # 3\n"
                            "print(squad[0])            # 김병장\n"
                            "print(squad[-1])           # 박일병\n"
                            "print('이상병' in squad)   # True\n"
                            "print('최이병' in squad)   # False\n\n"
                            "# __getitem__이 있으면 for 루프 자동 지원\n"
                            "for member in squad:\n"
                            "    print(f'  - {member}')"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "__getitem__을 구현하면 별도의 __iter__ 없이도 "
                            "for 루프가 동작합니다. Python이 index 0, 1, 2, ... 로 "
                            "자동 반복하다 IndexError가 발생하면 루프를 종료합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: __call__ 과 실전 예제 ────────────────────
            {
                "title": "__call__ — 호출 가능한 객체와 실전 예제",
                "content": [
                    "`__call__`을 구현하면 객체를 함수처럼 `obj(args)` 형태로 호출할 수 있습니다. "
                    "상태를 가진 함수가 필요할 때 매우 유용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Multiplier:\n"
                            "    \"\"\"특정 값을 곱하는 호출 가능 객체.\"\"\"\n\n"
                            "    def __init__(self, factor):\n"
                            "        self.factor = factor\n\n"
                            "    def __call__(self, value):\n"
                            "        \"\"\"객체를 함수처럼 호출하면 factor를 곱한다.\"\"\"\n"
                            "        return value * self.factor\n\n"
                            "    def __repr__(self):\n"
                            "        return f'Multiplier({self.factor})'\n\n\n"
                            "double = Multiplier(2)\n"
                            "triple = Multiplier(3)\n\n"
                            "print(double(5))   # 10\n"
                            "print(triple(5))   # 15\n\n"
                            "# 리스트에 적용\n"
                            "numbers = [1, 2, 3, 4, 5]\n"
                            "doubled = list(map(double, numbers))\n"
                            "print(doubled)     # [2, 4, 6, 8, 10]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "종합 예제: Money 클래스",
                    },
                    "지금까지 배운 특수 메서드를 모두 활용한 현실적인 예제입니다. "
                    "화폐 연산은 부동소수점 오류를 피하기 위해 정수(원 단위)로 처리합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Money:\n"
                            "    \"\"\"원화 금액을 나타내는 불변 클래스.\"\"\"\n\n"
                            "    def __init__(self, amount):\n"
                            "        if amount < 0:\n"
                            "            raise ValueError(f'금액은 0 이상이어야 합니다: {amount}')\n"
                            "        self._amount = int(amount)  # 원 단위 정수\n\n"
                            "    @property\n"
                            "    def amount(self):\n"
                            "        return self._amount\n\n"
                            "    def __repr__(self):\n"
                            "        return f'Money({self._amount})'\n\n"
                            "    def __str__(self):\n"
                            "        return f'{self._amount:,}원'\n\n"
                            "    def __add__(self, other):\n"
                            "        \"\"\"두 금액을 더한 새 Money를 반환한다.\"\"\"\n"
                            "        if not isinstance(other, Money):\n"
                            "            return NotImplemented\n"
                            "        return Money(self._amount + other._amount)\n\n"
                            "    def __sub__(self, other):\n"
                            "        \"\"\"두 금액을 뺀 새 Money를 반환한다.\"\"\"\n"
                            "        if not isinstance(other, Money):\n"
                            "            return NotImplemented\n"
                            "        return Money(self._amount - other._amount)\n\n"
                            "    def __mul__(self, multiplier):\n"
                            "        \"\"\"금액에 배수를 곱한 새 Money를 반환한다.\"\"\"\n"
                            "        return Money(self._amount * multiplier)\n\n"
                            "    def __eq__(self, other):\n"
                            "        if not isinstance(other, Money):\n"
                            "            return NotImplemented\n"
                            "        return self._amount == other._amount\n\n"
                            "    def __lt__(self, other):\n"
                            "        if not isinstance(other, Money):\n"
                            "            return NotImplemented\n"
                            "        return self._amount < other._amount\n\n\n"
                            "price = Money(15000)\n"
                            "discount = Money(3000)\n\n"
                            "final = price - discount\n"
                            "print(f'최종 가격: {final}')     # 최종 가격: 12,000원\n\n"
                            "total = final * 3\n"
                            "print(f'3개 구매: {total}')      # 3개 구매: 36,000원\n\n"
                            "cart = [Money(10000), Money(25000), Money(5000)]\n"
                            "cart_total = sum(cart, Money(0))  # sum은 0에서 시작하므로 초기값 필요\n"
                            "print(f'장바구니 합계: {cart_total}')  # 40,000원\n\n"
                            "print(sorted(cart))  # [Money(5000), Money(10000), Money(25000)]"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "특수 메서드를 구현할 때 '새 객체를 반환한다'는 원칙을 항상 지키세요. "
                            "Money 클래스처럼 self를 수정하지 않고 "
                            "매번 새 인스턴스를 만들어 반환하는 것이 안전합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "__repr__은 반드시 구현하세요. 디버깅 시 객체 내용을 즉시 확인할 수 있습니다.",
            "산술·비교 연산자는 항상 새 객체를 반환하고 self를 수정하지 마세요.",
            "타입 불일치 시 NotImplemented를 반환하면 Python이 역방향 연산을 자동 시도합니다.",
            "functools.total_ordering으로 __eq__와 __lt__만 정의해도 6가지 비교가 모두 동작합니다.",
            "__call__로 상태를 가진 함수 객체를 만들 수 있어 콜백·팩토리 패턴에 유용합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "`print(obj)` 호출 시 Python이 가장 먼저 사용하는 특수 메서드는?"
                ),
                "choices": [
                    "A) __repr__",
                    "B) __str__",
                    "C) __format__",
                    "D) __print__",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "다음 중 `3 * v` 형태(숫자가 왼쪽)를 지원하기 위해 "
                    "Vector 클래스에 구현해야 하는 메서드는?"
                ),
                "choices": [
                    "A) __mul__",
                    "B) __lmul__",
                    "C) __rmul__",
                    "D) __imul__",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "타입이 다른 객체와 비교할 때 `__eq__`에서 반환해야 하는 값은?"
                ),
                "choices": [
                    "A) False",
                    "B) None",
                    "C) NotImplemented",
                    "D) TypeError를 발생시킨다",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "Rectangle 클래스를 만드세요. "
                    "width와 height를 받고, __str__은 '3 x 4 사각형', "
                    "__repr__은 'Rectangle(3, 4)' 형태로 반환합니다. "
                    "또한 넓이가 큰 사각형이 '>` 비교에서 크도록 __lt__를 구현하세요."
                ),
                "hint": "넓이는 width * height입니다. __lt__에서 self.area() < other.area()를 비교하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "카운터 클래스 Counter를 만드세요. "
                    "내부에 정수 값을 가지며, __call__로 호출할 때마다 "
                    "값이 1씩 증가하고 현재 값을 반환합니다. "
                    "len(counter)는 현재 카운트를 반환합니다."
                ),
                "hint": "__call__에서 self._count += 1 후 반환, __len__은 self._count를 반환합니다.",
            },
        ],
        "challenge": {
            "question": (
                "Matrix 클래스를 구현하세요 (2x2 행렬). "
                "초기화: `Matrix([[1,2],[3,4]])`. "
                "__str__은 행렬을 보기 좋게 출력, "
                "__add__는 행렬 덧셈, __mul__은 행렬 곱셈을 지원합니다. "
                "__getitem__으로 `m[0][1]` 형태의 접근도 가능하게 하세요. "
                "모든 연산은 새 Matrix를 반환해야 합니다."
            ),
            "hint": (
                "내부에 2x2 리스트를 저장합니다. "
                "행렬 곱셈은 (result[i][j] = sum(row_i * col_j)). "
                "__getitem__은 self._data[index]를 반환하면 됩니다."
            ),
        },
        "summary": [
            "특수 메서드(__dunder__)는 Python이 연산자와 내장 함수를 처리할 때 자동으로 호출한다.",
            "__str__은 사람용, __repr__은 개발자용 문자열 표현이다. __repr__은 항상 구현하자.",
            "비교 연산자(__eq__, __lt__ 등)를 구현하면 sorted(), min(), max()가 자동으로 동작한다.",
            "산술 연산자는 항상 새 객체를 반환해야 한다 (불변성 원칙).",
            "__len__, __getitem__, __contains__를 구현하면 컬렉션처럼 동작하는 클래스를 만들 수 있다.",
            "__call__을 구현하면 객체를 함수처럼 호출할 수 있어 상태 있는 콜백에 유용하다.",
        ],
    }
