"""
부록 A: Python 매직 메서드 총정리
클래스에서 사용할 수 있는 특수 메서드(__dunder__)를 한눈에 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 A: Python 매직 메서드 총정리",
        "sections": [
            # ── 섹션 1: 매직 메서드란? ──
            {
                "title": "A.1 매직 메서드란?",
                "content": [
                    (
                        "매직 메서드(magic method)는 이름 앞뒤에 밑줄 두 개(__)가 붙은 특수 메서드입니다. "
                        "'던더(dunder) 메서드'라고도 부릅니다(double underscore의 줄임말). "
                        "Python이 특정 연산자나 내장함수를 만나면 자동으로 호출하는 메서드로, "
                        "클래스에 Python 내장 타입과 같은 자연스러운 동작을 부여합니다."
                    ),
                    {
                        "type": "analogy",
                        "text": (
                            "매직 메서드는 클래스와 Python 사이의 '계약서'와 같습니다. "
                            "__add__를 정의하면 + 연산자가 동작하고, "
                            "__len__을 정의하면 len() 함수가 동작합니다. "
                            "list, dict, str 같은 내장 타입도 모두 이 계약을 지킵니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 매직 메서드 없이 클래스를 만들면\n"
                            "class Point:\n"
                            "    def __init__(self, x, y):\n"
                            "        self.x = x\n"
                            "        self.y = y\n"
                            "\n"
                            "p1 = Point(1, 2)\n"
                            "p2 = Point(3, 4)\n"
                            "print(p1)        # <__main__.Point object at 0x...> — 불친절한 출력\n"
                            "# p1 + p2       # TypeError: unsupported operand type\n"
                            "# len(p1)       # TypeError: object of type 'Point' has no len()\n"
                            "\n"
                            "# 매직 메서드를 추가하면\n"
                            "class Point:\n"
                            "    def __init__(self, x, y):\n"
                            "        self.x = x\n"
                            "        self.y = y\n"
                            "    def __str__(self):\n"
                            "        return f'Point({self.x}, {self.y})'  # 친절한 출력\n"
                            "    def __add__(self, other):\n"
                            "        return Point(self.x + other.x, self.y + other.y)\n"
                            "\n"
                            "p1, p2 = Point(1, 2), Point(3, 4)\n"
                            "print(p1)        # Point(1, 2)\n"
                            "print(p1 + p2)   # Point(4, 6)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "매직 메서드를 직접 호출하지 마세요. "
                            "p1.__add__(p2) 대신 p1 + p2를 쓰세요. "
                            "직접 호출은 가독성을 해치고, 연산자 오버로딩의 의도에 맞지 않습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 생성/소멸 메서드 ──
            {
                "title": "A.2 생성 & 소멸: __init__, __new__, __del__",
                "content": [
                    {
                        "type": "table",
                        "headers": ["메서드", "호출 시점", "주요 용도"],
                        "rows": [
                            ["__new__(cls, ...)", "인스턴스 생성 직전", "싱글톤 패턴, 불변 타입 서브클래스"],
                            ["__init__(self, ...)", "인스턴스 생성 직후", "속성 초기화 (가장 많이 사용)"],
                            ["__del__(self)", "인스턴스 소멸 직전", "리소스 해제 (파일, DB 연결 등)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class DatabaseConnection:\n"
                            "    def __init__(self, host: str, port: int):\n"
                            "        self.host = host\n"
                            "        self.port = port\n"
                            "        self._connected = False\n"
                            "        print(f'연결 준비: {host}:{port}')\n"
                            "\n"
                            "    def connect(self):\n"
                            "        self._connected = True\n"
                            "        print('DB 연결됨')\n"
                            "\n"
                            "    def __del__(self):\n"
                            "        # 가비지 컬렉터가 객체를 제거할 때 자동 호출\n"
                            "        if self._connected:\n"
                            "            print(f'{self.host} 연결 종료')\n"
                            "\n"
                            "# __new__ 활용: 싱글톤 패턴 (부록 B에서 자세히)\n"
                            "class SingletonMeta(type):\n"
                            "    _instances = {}\n"
                            "    def __call__(cls, *args, **kwargs):\n"
                            "        if cls not in cls._instances:\n"
                            "            cls._instances[cls] = super().__call__(*args, **kwargs)\n"
                            "        return cls._instances[cls]\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "__del__은 정확한 호출 시점이 보장되지 않습니다. "
                            "리소스 해제는 __del__ 대신 컨텍스트 매니저(__enter__/__exit__)를 사용하세요. "
                            "with 문이 훨씬 안전하고 예측 가능합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 문자열 표현 메서드 ──
            {
                "title": "A.3 문자열 표현: __str__, __repr__, __format__",
                "content": [
                    {
                        "type": "table",
                        "headers": ["메서드", "호출하는 함수", "목적"],
                        "rows": [
                            ["__str__(self)", "str(obj), print(obj)", "사용자 친화적 출력"],
                            ["__repr__(self)", "repr(obj), 대화형 셸", "개발자용 디버깅 출력"],
                            ["__format__(self, spec)", "format(obj, spec), f-string", "형식 지정 출력"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Money:\n"
                            "    def __init__(self, amount: int, currency: str = 'KRW'):\n"
                            "        self.amount = amount\n"
                            "        self.currency = currency\n"
                            "\n"
                            "    def __str__(self) -> str:\n"
                            "        # 사용자에게 보여주는 형식\n"
                            "        return f'{self.amount:,}{self.currency}'\n"
                            "\n"
                            "    def __repr__(self) -> str:\n"
                            "        # 개발자가 보는 형식 — eval()로 복원 가능한 형태가 이상적\n"
                            "        return f'Money(amount={self.amount}, currency={self.currency!r})'\n"
                            "\n"
                            "    def __format__(self, spec: str) -> str:\n"
                            "        # f'{m:+}' 처럼 사용자 정의 형식 지정자 지원\n"
                            "        if spec == '+':\n"
                            "            return f'+{self.amount:,}{self.currency}'\n"
                            "        return str(self)\n"
                            "\n"
                            "m = Money(50000)\n"
                            "print(m)          # 50,000KRW      (__str__)\n"
                            "print(repr(m))    # Money(amount=50000, currency='KRW')  (__repr__)\n"
                            "print(f'{m:+}')   # +50,000KRW     (__format__)\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "__repr__는 __str__가 없을 때 폴백으로도 사용됩니다. "
                            "최소한 __repr__만이라도 구현하는 것이 좋은 습관입니다. "
                            "규칙: __repr__은 'ClassName(인자들)' 형식으로 작성하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 비교 연산자 메서드 ──
            {
                "title": "A.4 비교 연산자: __eq__, __lt__, __le__, __gt__, __ge__, __ne__",
                "content": [
                    {
                        "type": "table",
                        "headers": ["메서드", "연산자", "의미"],
                        "rows": [
                            ["__eq__(self, other)", "==", "같음"],
                            ["__ne__(self, other)", "!=", "다름 (__eq__ 반전이 기본)"],
                            ["__lt__(self, other)", "<", "미만"],
                            ["__le__(self, other)", "<=", "이하"],
                            ["__gt__(self, other)", ">", "초과"],
                            ["__ge__(self, other)", ">=", "이상"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from functools import total_ordering\n"
                            "\n"
                            "@total_ordering  # __eq__와 하나만 정의하면 나머지를 자동 생성\n"
                            "class Temperature:\n"
                            "    def __init__(self, celsius: float):\n"
                            "        self.celsius = celsius\n"
                            "\n"
                            "    def __eq__(self, other: object) -> bool:\n"
                            "        if not isinstance(other, Temperature):\n"
                            "            return NotImplemented\n"
                            "        return self.celsius == other.celsius\n"
                            "\n"
                            "    def __lt__(self, other: 'Temperature') -> bool:\n"
                            "        if not isinstance(other, Temperature):\n"
                            "            return NotImplemented\n"
                            "        return self.celsius < other.celsius\n"
                            "\n"
                            "    # @total_ordering 덕분에 <=, >, >= 는 자동 정의됨\n"
                            "\n"
                            "t1 = Temperature(20)\n"
                            "t2 = Temperature(30)\n"
                            "print(t1 < t2)   # True\n"
                            "print(t1 >= t2)  # False  (자동 생성)\n"
                            "print(sorted([t2, t1]))  # [Temperature(20), Temperature(30)]\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "@functools.total_ordering 데코레이터를 사용하면 "
                            "__eq__와 __lt__ 두 개만 정의해도 나머지 4개 비교 연산자가 자동 생성됩니다. "
                            "sorted()나 min()/max()를 클래스에 사용하려면 반드시 비교 메서드를 구현하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 산술 연산자 메서드 ──
            {
                "title": "A.5 산술 연산자: __add__, __sub__, __mul__ 외",
                "content": [
                    {
                        "type": "table",
                        "headers": ["메서드", "연산자", "반영 메서드 (우항)"],
                        "rows": [
                            ["__add__(self, other)", "+", "__radd__"],
                            ["__sub__(self, other)", "-", "__rsub__"],
                            ["__mul__(self, other)", "*", "__rmul__"],
                            ["__truediv__(self, other)", "/", "__rtruediv__"],
                            ["__floordiv__(self, other)", "//", "__rfloordiv__"],
                            ["__mod__(self, other)", "%", "__rmod__"],
                            ["__pow__(self, other)", "**", "__rpow__"],
                            ["__neg__(self)", "단항 -", "(없음)"],
                            ["__abs__(self)", "abs()", "(없음)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Vector:\n"
                            "    def __init__(self, x: float, y: float):\n"
                            "        self.x = x\n"
                            "        self.y = y\n"
                            "\n"
                            "    def __add__(self, other: 'Vector') -> 'Vector':\n"
                            "        return Vector(self.x + other.x, self.y + other.y)\n"
                            "\n"
                            "    def __sub__(self, other: 'Vector') -> 'Vector':\n"
                            "        return Vector(self.x - other.x, self.y - other.y)\n"
                            "\n"
                            "    def __mul__(self, scalar: float) -> 'Vector':\n"
                            "        # Vector * 숫자\n"
                            "        return Vector(self.x * scalar, self.y * scalar)\n"
                            "\n"
                            "    def __rmul__(self, scalar: float) -> 'Vector':\n"
                            "        # 숫자 * Vector  (3 * v 형태 지원)\n"
                            "        return self.__mul__(scalar)\n"
                            "\n"
                            "    def __neg__(self) -> 'Vector':\n"
                            "        return Vector(-self.x, -self.y)\n"
                            "\n"
                            "    def __abs__(self) -> float:\n"
                            "        return (self.x ** 2 + self.y ** 2) ** 0.5\n"
                            "\n"
                            "    def __str__(self) -> str:\n"
                            "        return f'Vector({self.x}, {self.y})'\n"
                            "\n"
                            "v1, v2 = Vector(1, 2), Vector(3, 4)\n"
                            "print(v1 + v2)   # Vector(4, 6)\n"
                            "print(3 * v1)    # Vector(3, 6)  (__rmul__ 사용)\n"
                            "print(abs(v2))   # 5.0\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "반영 메서드(r-메서드)는 좌항이 해당 연산을 지원하지 않을 때 우항에서 시도됩니다. "
                            "예를 들어 3 * v에서 int는 Vector를 모르므로, "
                            "Python이 v.__rmul__(3)을 자동 호출합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 컬렉션 메서드 ──
            {
                "title": "A.6 컬렉션: __len__, __getitem__, __setitem__, __delitem__, __contains__, __iter__",
                "content": [
                    {
                        "type": "table",
                        "headers": ["메서드", "호출하는 연산/함수", "의미"],
                        "rows": [
                            ["__len__(self)", "len(obj)", "길이 반환"],
                            ["__getitem__(self, key)", "obj[key]", "인덱스/키로 조회"],
                            ["__setitem__(self, key, val)", "obj[key] = val", "인덱스/키로 저장"],
                            ["__delitem__(self, key)", "del obj[key]", "인덱스/키로 삭제"],
                            ["__contains__(self, item)", "item in obj", "포함 여부 확인"],
                            ["__iter__(self)", "for x in obj, iter(obj)", "이터레이터 반환"],
                            ["__next__(self)", "next(obj)", "다음 값 반환"],
                            ["__reversed__(self)", "reversed(obj)", "역순 이터레이터"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class Playlist:\n"
                            '    """음악 재생목록 — 컬렉션 매직 메서드 시연"""\n'
                            "\n"
                            "    def __init__(self, name: str):\n"
                            "        self.name = name\n"
                            "        self._songs: list[str] = []\n"
                            "\n"
                            "    def add(self, song: str) -> None:\n"
                            "        self._songs.append(song)\n"
                            "\n"
                            "    def __len__(self) -> int:\n"
                            "        return len(self._songs)\n"
                            "\n"
                            "    def __getitem__(self, index: int) -> str:\n"
                            "        return self._songs[index]  # 슬라이싱도 자동 지원\n"
                            "\n"
                            "    def __setitem__(self, index: int, song: str) -> None:\n"
                            "        self._songs[index] = song\n"
                            "\n"
                            "    def __delitem__(self, index: int) -> None:\n"
                            "        del self._songs[index]\n"
                            "\n"
                            "    def __contains__(self, song: str) -> bool:\n"
                            "        return song in self._songs\n"
                            "\n"
                            "    def __iter__(self):\n"
                            "        return iter(self._songs)  # 리스트의 이터레이터 위임\n"
                            "\n"
                            "pl = Playlist('내 플리')\n"
                            "pl.add('봄날')\n"
                            "pl.add('Dynamite')\n"
                            "print(len(pl))          # 2\n"
                            "print(pl[0])            # 봄날\n"
                            "print('봄날' in pl)      # True\n"
                            "for song in pl:         # __iter__ 사용\n"
                            "    print(f'  - {song}')\n"
                        ),
                    },
                ],
            },
            # ── 섹션 7: 호출·컨텍스트·속성 메서드 ──
            {
                "title": "A.7 호출, 컨텍스트, 속성 접근",
                "content": [
                    {
                        "type": "table",
                        "headers": ["메서드", "호출 시점", "주요 용도"],
                        "rows": [
                            ["__call__(self, ...)", "obj(...)", "인스턴스를 함수처럼 사용"],
                            ["__enter__(self)", "with obj as x:", "컨텍스트 진입"],
                            ["__exit__(self, exc_t, exc_v, tb)", "with 블록 종료", "리소스 해제"],
                            ["__getattr__(self, name)", "존재하지 않는 속성 접근", "동적 속성 처리"],
                            ["__setattr__(self, name, value)", "obj.attr = val", "속성 설정 가로채기"],
                            ["__delattr__(self, name)", "del obj.attr", "속성 삭제 가로채기"],
                            ["__getattribute__(self, name)", "모든 속성 접근", "속성 접근 완전 제어 (주의)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# __call__: 인스턴스를 함수처럼 사용\n"
                            "class Multiplier:\n"
                            "    def __init__(self, factor: float):\n"
                            "        self.factor = factor\n"
                            "\n"
                            "    def __call__(self, value: float) -> float:\n"
                            "        return value * self.factor\n"
                            "\n"
                            "double = Multiplier(2)\n"
                            "triple = Multiplier(3)\n"
                            "print(double(5))   # 10\n"
                            "print(triple(5))   # 15\n"
                            "# 함수처럼 전달 가능\n"
                            "results = list(map(double, [1, 2, 3]))  # [2, 4, 6]\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# __enter__ / __exit__: 컨텍스트 매니저\n"
                            "class Timer:\n"
                            '    """코드 블록 실행 시간 측정"""\n'
                            "    import time\n"
                            "\n"
                            "    def __enter__(self):\n"
                            "        import time\n"
                            "        self._start = time.time()\n"
                            "        return self  # as 절에 전달되는 값\n"
                            "\n"
                            "    def __exit__(self, exc_type, exc_val, tb):\n"
                            "        import time\n"
                            "        self.elapsed = time.time() - self._start\n"
                            "        print(f'경과 시간: {self.elapsed:.4f}초')\n"
                            "        return False  # 예외를 재발생시킴 (True이면 예외 억제)\n"
                            "\n"
                            "with Timer() as t:\n"
                            "    total = sum(range(1_000_000))\n"
                            "# 경과 시간: 0.0234초\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# __getattr__: 존재하지 않는 속성 접근 처리\n"
                            "class FlexibleConfig:\n"
                            '    """없는 설정 키를 None 대신 기본값으로 반환"""\n'
                            "\n"
                            "    def __init__(self, **settings):\n"
                            "        self._data = settings\n"
                            "\n"
                            "    def __getattr__(self, name: str):\n"
                            "        # __getattr__는 일반 속성 조회가 실패했을 때만 호출됨\n"
                            "        return self._data.get(name)  # 없으면 None 반환\n"
                            "\n"
                            "config = FlexibleConfig(debug=True, max_retry=3)\n"
                            "print(config.debug)       # True\n"
                            "print(config.max_retry)   # 3\n"
                            "print(config.timeout)     # None (없는 키도 오류 없이 처리)\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "__getattribute__는 모든 속성 접근에서 호출됩니다. "
                            "잘못 오버라이드하면 무한 재귀에 빠질 수 있으므로, "
                            "특별한 이유가 없다면 __getattr__만 사용하세요. "
                            "__getattr__는 일반 조회가 실패했을 때만 호출되어 훨씬 안전합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 8: 매직 메서드 전체 요약표 ──
            {
                "title": "A.8 전체 요약표",
                "content": [
                    "**카테고리별 매직 메서드 한눈에 보기:**",
                    {
                        "type": "table",
                        "headers": ["카테고리", "메서드", "연산/함수"],
                        "rows": [
                            ["생성/소멸", "__new__, __init__, __del__", "객체 생성·소멸 시"],
                            ["문자열 표현", "__str__, __repr__, __format__", "str(), repr(), format()"],
                            ["비교", "__eq__, __ne__, __lt__, __le__, __gt__, __ge__", "==, !=, <, <=, >, >="],
                            ["산술", "__add__, __sub__, __mul__, __truediv__", "+, -, *, /"],
                            ["산술(계속)", "__floordiv__, __mod__, __pow__, __neg__", "//, %, **, 단항-"],
                            ["컬렉션", "__len__, __getitem__, __setitem__", "len(), obj[k], obj[k]=v"],
                            ["컬렉션(계속)", "__delitem__, __contains__, __iter__", "del obj[k], in, for"],
                            ["호출", "__call__", "obj(...)"],
                            ["컨텍스트", "__enter__, __exit__", "with 문"],
                            ["속성", "__getattr__, __setattr__, __delattr__", ".attr 접근/설정/삭제"],
                            ["해시", "__hash__", "hash(), dict 키, set 원소"],
                            ["불리언", "__bool__", "bool(), if 조건"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# __hash__와 __bool__ 예제\n"
                            "class Point:\n"
                            "    def __init__(self, x: float, y: float):\n"
                            "        self.x = x\n"
                            "        self.y = y\n"
                            "\n"
                            "    def __hash__(self) -> int:\n"
                            "        # set이나 dict 키로 사용하려면 필수\n"
                            "        # __eq__를 정의하면 __hash__는 None이 되므로 직접 정의 필요\n"
                            "        return hash((self.x, self.y))\n"
                            "\n"
                            "    def __bool__(self) -> bool:\n"
                            "        # 원점(0, 0)이면 False, 아니면 True\n"
                            "        return bool(self.x or self.y)\n"
                            "\n"
                            "p = Point(0, 0)\n"
                            "print(bool(p))      # False — 원점\n"
                            "p2 = Point(1, 0)\n"
                            "print(bool(p2))     # True\n"
                            "visited = {p, p2}   # set 사용 가능 (__hash__ 덕분)\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "__eq__를 정의하면 Python은 __hash__를 자동으로 None으로 설정합니다 "
                            "(해시 불일치 방지). set이나 dict 키로 사용하려면 __hash__도 함께 정의하세요. "
                            "불변 속성만으로 해시를 계산하는 것이 원칙입니다."
                        ),
                    },
                ],
            },
        ],
    }
