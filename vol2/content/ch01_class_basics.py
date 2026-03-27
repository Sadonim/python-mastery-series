"""Chapter 1: 클래스와 객체 - 설계도로 세상을 구조화하다."""


def get_chapter():
    """챕터 1의 전체 콘텐츠를 딕셔너리로 반환한다."""
    return {
        "number": 1,
        "title": "클래스와 객체",
        "subtitle": "설계도로 세상을 구조화하다",
        "big_picture": (
            "지금까지는 함수와 변수로 코드를 조각조각 작성했습니다. "
            "하지만 현실 세계의 복잡한 문제를 다루려면 '데이터'와 '동작'을 묶어 하나의 단위로 "
            "관리하는 방법이 필요합니다. 객체지향 프로그래밍(OOP)은 그 해답입니다. "
            "이 챕터에서는 클래스(class)라는 설계도로 객체(object)를 만들고, "
            "`__init__`, `self`, 인스턴스 변수, 클래스 변수, 메서드를 배웁니다. "
            "실용 예제로는 은행 계좌 클래스와 학생 성적 관리 시스템을 만들어봅니다."
        ),
        "sections": [
            _section_oop_concept(),
            _section_class_definition(),
            _section_init_and_self(),
            _section_variables(),
            _section_methods(),
            _section_access_control(),
            _section_practical_examples(),
        ],
        "practical_tips": [
            "클래스를 설계할 때는 '이 객체가 무엇을 알고(속성), 무엇을 할 수 있는가(메서드)'를 먼저 생각하세요.",
            "`__init__` 안에서 모든 인스턴스 변수를 선언하세요. 나중에 추가하면 코드를 읽기 어려워집니다.",
            "클래스 이름은 반드시 CamelCase(대문자 시작)로, 인스턴스 변수/메서드는 소문자_언더스코어로 작성하세요.",
            "단일 책임 원칙(SRP): 하나의 클래스는 하나의 역할만 담당해야 합니다. 클래스가 너무 커지면 분리를 고려하세요.",
            "실습 팁: 먼저 종이에 '속성 목록'과 '메서드 목록'을 그린 뒤 코드로 옮기면 훨씬 빠르게 설계할 수 있습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 클래스(class)와 객체(object)의 관계를 가장 잘 설명한 것은?",
                "choices": [
                    "A) 클래스는 실제 데이터이고, 객체는 그 설계도다",
                    "B) 클래스는 설계도(틀)이고, 객체는 그 설계도로 만든 실체다",
                    "C) 클래스와 객체는 완전히 같은 개념이다",
                    "D) 클래스는 함수의 다른 이름이다",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "`self` 매개변수에 대한 올바른 설명은?",
                "choices": [
                    "A) 클래스 자신(클래스 전체)을 가리키는 특별한 키워드다",
                    "B) 메서드를 호출한 인스턴스(객체) 자신을 가리키는 관례적 이름이다",
                    "C) `self`는 Python이 자동으로 제공하므로 매개변수 목록에 쓰지 않아도 된다",
                    "D) `self`는 항상 첫 번째 인수로 직접 값을 전달해야 한다",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "인스턴스 변수와 클래스 변수의 차이로 올바른 것은?",
                "choices": [
                    "A) 인스턴스 변수는 모든 객체가 공유하고, 클래스 변수는 객체마다 다르다",
                    "B) 인스턴스 변수는 객체마다 독립적이고, 클래스 변수는 모든 객체가 공유한다",
                    "C) 둘 다 동일하게 모든 객체가 공유한다",
                    "D) 인스턴스 변수는 `__init__` 밖에서만 선언할 수 있다",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "`Car` 클래스를 작성하세요.\n"
                    "- 속성: brand(제조사), model(모델명), speed(현재 속도, 초기값 0)\n"
                    "- 메서드:\n"
                    "  - accelerate(amount): speed를 amount만큼 증가 (최대 200)\n"
                    "  - brake(amount): speed를 amount만큼 감소 (최소 0)\n"
                    "  - get_info(): '제조사 모델 - 현재 속도: Nkm/h' 형식으로 출력\n"
                    "car = Car('현대', '소나타')\n"
                    "car.accelerate(80)\n"
                    "car.get_info()  # '현대 소나타 - 현재 속도: 80km/h'"
                ),
                "hint": "speed가 0 미만이거나 200 초과가 되지 않도록 min(), max()나 if문을 활용하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "`Rectangle` 클래스를 작성하세요.\n"
                    "- 클래스 변수 `count`로 생성된 사각형 총 개수를 추적\n"
                    "- 속성: width(가로), height(세로)\n"
                    "- 메서드: area()(넓이), perimeter()(둘레), __str__()(문자열 표현)\n"
                    "- 인스턴스 생성 시마다 count가 1 증가\n"
                    "r1 = Rectangle(3, 4)\n"
                    "r2 = Rectangle(5, 6)\n"
                    "print(Rectangle.count)  # 2"
                ),
                "hint": "`__init__` 안에서 `Rectangle.count += 1`로 클래스 변수를 증가시키세요.",
            },
        ],
        "challenge": {
            "question": (
                "간단한 '도서관 관리 시스템'을 만들어보세요.\n"
                "`Book` 클래스: 속성(제목, 저자, ISBN, 대출 여부), 메서드(대출, 반납, 정보 출력)\n"
                "`Library` 클래스: 속성(도서 목록), 메서드(도서 추가, ISBN으로 검색, 대출 가능 목록 출력)\n"
                "최소 3권의 책을 추가하고, 대출/반납 시나리오를 실행해보세요."
            ),
            "hint": (
                "Library 클래스의 도서 목록은 리스트로 관리하고, "
                "검색 시 for 반복문으로 ISBN을 비교하세요. "
                "대출 여부는 Book 객체의 불리언 속성으로 관리합니다."
            ),
        },
        "summary": [
            "OOP는 '데이터(속성)'와 '동작(메서드)'을 클래스라는 설계도로 묶어 관리하는 프로그래밍 패러다임이다.",
            "클래스는 설계도, 객체(인스턴스)는 설계도로 만든 실체다. 하나의 클래스로 여러 객체를 만들 수 있다.",
            "`__init__`은 객체가 생성될 때 자동으로 호출되는 생성자 메서드이며, `self`는 호출된 인스턴스 자신을 가리킨다.",
            "인스턴스 변수는 각 객체마다 독립적인 값을 가지고, 클래스 변수는 모든 객체가 공유한다.",
            "메서드 종류: 인스턴스 메서드(self), 클래스 메서드(@classmethod, cls), 정적 메서드(@staticmethod).",
            "_변수는 내부 사용 관례, __변수는 이름 맹글링(name mangling)으로 외부 접근을 어렵게 만든다.",
        ],
    }


def _section_oop_concept():
    """섹션 1: 객체지향 프로그래밍이란?"""
    return {
        "title": "객체지향 프로그래밍(OOP)이란?",
        "content": [
            "프로그래밍 세계에는 두 가지 큰 흐름이 있습니다. 하나는 '절차적 프로그래밍', 다른 하나는 '객체지향 프로그래밍'입니다.",
            {
                "type": "table",
                "headers": ["구분", "절차적 프로그래밍", "객체지향 프로그래밍(OOP)"],
                "rows": [
                    ["핵심 단위", "함수 (function)", "객체 (object)"],
                    ["데이터 관리", "데이터와 함수가 분리됨", "데이터와 메서드가 하나로 묶임"],
                    ["코드 재사용", "함수 호출", "상속(inheritance)"],
                    ["비유", "요리 레시피 (단계별 순서)", "요리사 (자신만의 도구와 기술 보유)"],
                    ["적합한 경우", "간단한 스크립트, 순서가 명확한 작업", "복잡한 시스템, 협업 프로젝트"],
                ],
            },
            {
                "type": "analogy",
                "text": (
                    "절차적 프로그래밍은 군대의 '작전 명령서'와 같습니다. 1번 → 2번 → 3번 순서대로 실행합니다. "
                    "반면 OOP는 '부대 편성표'와 같습니다. 각 부대(객체)가 자신만의 역할(메서드)과 장비(속성)를 가지고, "
                    "지휘관(코드)은 각 부대에게 임무를 맡깁니다. "
                    "복잡한 작전(프로그램)일수록 OOP 방식이 관리하기 훨씬 쉽습니다."
                ),
            },
            {
                "type": "flow_diagram",
                "nodes": [
                    "현실 세계의 '사물' 관찰",
                    "→ 공통 속성 추출 (이름, 나이 등)",
                    "→ 공통 동작 추출 (걷다, 말하다 등)",
                    "→ 클래스(설계도) 정의",
                    "→ 객체(인스턴스) 생성",
                    "→ 객체끼리 메시지를 주고받으며 문제 해결",
                ],
                "note": "OOP의 핵심: 현실 세계를 코드로 모델링하는 과정",
            },
            "OOP의 4대 원칙: **캡슐화(Encapsulation)**, **상속(Inheritance)**, **다형성(Polymorphism)**, **추상화(Abstraction)**. Vol.2에서 하나씩 배워나갑니다.",
            {
                "type": "note",
                "text": "OOP가 항상 옳은 것은 아닙니다. 간단한 스크립트나 데이터 처리에는 함수형 프로그래밍이 더 간결합니다. 상황에 맞는 도구를 선택하는 것이 중요합니다.",
            },
        ],
    }


def _section_class_definition():
    """섹션 2: 클래스 정의와 인스턴스 생성."""
    return {
        "title": "클래스 정의와 인스턴스 생성",
        "content": [
            "`class` 키워드로 클래스를 정의하고, 클래스 이름 뒤에 괄호를 붙여 인스턴스(객체)를 생성합니다.",
            {
                "type": "analogy",
                "text": (
                    "클래스는 '붕어빵 틀'이고, 인스턴스는 '붕어빵'입니다. "
                    "틀 하나로 수백 개의 붕어빵을 만들 수 있듯이, "
                    "클래스 하나로 수백 개의 객체를 만들 수 있습니다. "
                    "각 붕어빵은 같은 모양(구조)이지만 서로 다른 재료(데이터)를 가질 수 있습니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 가장 간단한 클래스 ──\n"
                    "class Dog:\n"
                    "    \"\"\"개를 표현하는 클래스.\"\"\"\n"
                    "    pass  # 아직 아무것도 없는 빈 클래스\n"
                    "\n"
                    "\n"
                    "# 인스턴스(객체) 생성 — 클래스 이름()으로 호출\n"
                    "dog1 = Dog()  # Dog 클래스의 인스턴스\n"
                    "dog2 = Dog()  # 또 다른 Dog 인스턴스\n"
                    "\n"
                    "print(type(dog1))        # <class '__main__.Dog'>\n"
                    "print(isinstance(dog1, Dog))  # True\n"
                    "print(dog1 is dog2)      # False — 서로 다른 객체!"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 속성을 동적으로 추가하는 방법 (비권장) ──\n"
                    "# 이해를 위한 예시일 뿐, 실제로는 __init__에서 선언해야 합니다\n"
                    "class Dog:\n"
                    "    pass\n"
                    "\n"
                    "\n"
                    "dog1 = Dog()\n"
                    "dog1.name = '뽀삐'     # 동적으로 속성 추가 (비권장)\n"
                    "dog1.breed = '진돗개'\n"
                    "print(dog1.name)       # 뽀삐\n"
                    "\n"
                    "dog2 = Dog()\n"
                    "# dog2.name 접근 시 AttributeError 발생!\n"
                    "# → __init__에서 모든 속성을 미리 선언해야 하는 이유"
                ),
            },
            {
                "type": "warning",
                "text": "클래스 이름은 반드시 대문자로 시작하는 CamelCase를 사용하세요. `dog`나 `my_dog`처럼 소문자로 시작하면 PEP 8 위반입니다.",
            },
        ],
    }


def _section_init_and_self():
    """섹션 3: __init__ 생성자와 self."""
    return {
        "title": "`__init__` 생성자와 `self`",
        "content": [
            "`__init__`은 객체가 생성될 때 자동으로 호출되는 특수 메서드(매직 메서드)입니다. 객체의 초기 상태를 설정하는 역할을 합니다.",
            {
                "type": "flow_diagram",
                "nodes": [
                    "Dog('뽀삐', 3) 호출",
                    "→ Python이 새 Dog 객체 메모리 할당",
                    "→ __init__(self, '뽀삐', 3) 자동 호출",
                    "→ self.name = '뽀삐' 저장",
                    "→ self.age = 3 저장",
                    "→ 초기화된 객체 반환",
                ],
                "note": "__init__ 호출 과정: 객체 생성 → 초기화 메서드 자동 실행",
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class Dog:\n"
                    "    \"\"\"개를 표현하는 클래스.\"\"\"\n"
                    "\n"
                    "    def __init__(self, name: str, breed: str, age: int) -> None:\n"
                    "        \"\"\"Dog 인스턴스를 초기화한다.\n"
                    "\n"
                    "        Args:\n"
                    "            name: 개의 이름\n"
                    "            breed: 견종\n"
                    "            age: 나이 (년)\n"
                    "        \"\"\"\n"
                    "        # self.속성명 = 값 으로 인스턴스 변수 선언\n"
                    "        self.name = name    # '뽀삐'\n"
                    "        self.breed = breed  # '진돗개'\n"
                    "        self.age = age      # 3\n"
                    "\n"
                    "    def bark(self) -> str:\n"
                    "        \"\"\"짖는 소리를 반환한다.\"\"\"\n"
                    "        return f'{self.name}: 왈왈!'\n"
                    "\n"
                    "\n"
                    "# 인스턴스 생성 — __init__의 self를 제외한 인수만 전달\n"
                    "dog1 = Dog('뽀삐', '진돗개', 3)\n"
                    "dog2 = Dog('초코', '푸들', 1)\n"
                    "\n"
                    "print(dog1.name)    # 뽀삐\n"
                    "print(dog2.breed)   # 푸들\n"
                    "print(dog1.bark())  # 뽀삐: 왈왈!"
                ),
            },
            "`self`는 메서드를 호출한 인스턴스 자기 자신을 가리킵니다. `dog1.bark()`를 호출하면 `bark(self)` 안의 `self`는 `dog1`입니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# self가 무엇인지 직접 확인해보기\n"
                    "class Cat:\n"
                    "    def __init__(self, name: str) -> None:\n"
                    "        self.name = name\n"
                    "\n"
                    "    def who_am_i(self) -> None:\n"
                    "        \"\"\"self가 어떤 객체를 가리키는지 출력한다.\"\"\"\n"
                    "        print(f'self는 {self}')          # <__main__.Cat object at 0x...>\n"
                    "        print(f'내 이름은 {self.name}')   # 내 이름은 나비\n"
                    "\n"
                    "\n"
                    "cat1 = Cat('나비')\n"
                    "cat1.who_am_i()  # self = cat1 객체 자신\n"
                    "\n"
                    "cat2 = Cat('미야')\n"
                    "cat2.who_am_i()  # self = cat2 객체 자신"
                ),
            },
            {
                "type": "note",
                "text": "`self`는 Python의 관례적 이름입니다. 기술적으로는 다른 이름을 써도 되지만 (예: `this`), 절대 변경하지 마세요. 모든 파이써니스타(Pythonista)가 `self`를 기대합니다.",
            },
        ],
    }


def _section_variables():
    """섹션 4: 인스턴스 변수와 클래스 변수."""
    return {
        "title": "인스턴스 변수와 클래스 변수",
        "content": [
            "클래스 안의 변수는 두 종류입니다. 객체마다 따로 가지는 **인스턴스 변수**와, 모든 객체가 공유하는 **클래스 변수**입니다.",
            {
                "type": "analogy",
                "text": (
                    "군인 클래스를 생각해보세요. "
                    "'이름', '계급', '군번'은 군인마다 다른 값을 가집니다 → 인스턴스 변수. "
                    "'소속 군대(대한민국 육군)' 처럼 모든 군인이 공유하는 정보는 → 클래스 변수. "
                    "인스턴스 변수는 각자의 신분증, 클래스 변수는 부대 현판이라고 생각하세요."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class Student:\n"
                    "    \"\"\"학생을 표현하는 클래스.\"\"\"\n"
                    "\n"
                    "    # 클래스 변수 — 모든 Student 인스턴스가 공유\n"
                    "    school_name: str = '파이썬 고등학교'\n"
                    "    total_students: int = 0  # 생성된 학생 총 수\n"
                    "\n"
                    "    def __init__(self, name: str, student_id: str) -> None:\n"
                    "        # 인스턴스 변수 — 각 Student 객체마다 독립적\n"
                    "        self.name = name\n"
                    "        self.student_id = student_id\n"
                    "        self.grades: list = []  # 각자의 성적 목록\n"
                    "\n"
                    "        # 학생 생성 시마다 클래스 변수 증가\n"
                    "        Student.total_students += 1\n"
                    "\n"
                    "\n"
                    "s1 = Student('홍길동', '2024001')\n"
                    "s2 = Student('김영희', '2024002')\n"
                    "\n"
                    "# 클래스 변수 접근: 클래스명 또는 인스턴스로 접근 가능\n"
                    "print(Student.school_name)    # 파이썬 고등학교\n"
                    "print(s1.school_name)         # 파이썬 고등학교 (동일)\n"
                    "print(Student.total_students) # 2\n"
                    "\n"
                    "# 인스턴스 변수는 각자 다름\n"
                    "print(s1.name)  # 홍길동\n"
                    "print(s2.name)  # 김영희"
                ),
            },
            {
                "type": "warning",
                "text": "클래스 변수를 인스턴스를 통해 '수정'하면 주의가 필요합니다. `s1.school_name = '다른 학교'`는 클래스 변수를 바꾸는 것이 아니라 s1만의 새 인스턴스 변수를 만듭니다. 클래스 변수 수정은 반드시 `클래스명.변수명 = 값` 형식으로 하세요.",
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 클래스 변수 수정 주의사항 예시\n"
                    "class Counter:\n"
                    "    count: int = 0  # 클래스 변수\n"
                    "\n"
                    "\n"
                    "c1 = Counter()\n"
                    "c2 = Counter()\n"
                    "\n"
                    "# 올바른 방법: 클래스를 통해 수정\n"
                    "Counter.count += 1\n"
                    "print(Counter.count)  # 1\n"
                    "print(c1.count)       # 1 (클래스 변수 공유)\n"
                    "print(c2.count)       # 1 (클래스 변수 공유)\n"
                    "\n"
                    "# 잘못된 방법: 인스턴스를 통해 수정 — c1만의 인스턴스 변수가 생성됨!\n"
                    "c1.count = 99\n"
                    "print(c1.count)       # 99 (c1 인스턴스 변수)\n"
                    "print(Counter.count)  # 1  (클래스 변수는 그대로)"
                ),
            },
        ],
    }


def _section_methods():
    """섹션 5: 메서드의 종류."""
    return {
        "title": "메서드의 종류 — 인스턴스, 클래스, 정적 메서드",
        "content": [
            "Python 클래스에는 세 종류의 메서드가 있습니다. 상황에 맞는 메서드를 선택하면 코드의 의미가 명확해집니다.",
            {
                "type": "table",
                "headers": ["종류", "첫 번째 매개변수", "데코레이터", "주요 용도"],
                "rows": [
                    ["인스턴스 메서드", "self (인스턴스 자신)", "없음", "인스턴스 변수 접근/수정"],
                    ["클래스 메서드", "cls (클래스 자신)", "@classmethod", "클래스 변수 접근, 대안 생성자"],
                    ["정적 메서드", "없음", "@staticmethod", "클래스와 관련되지만 독립적인 유틸리티 함수"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class Temperature:\n"
                    "    \"\"\"온도를 표현하는 클래스.\"\"\"\n"
                    "\n"
                    "    unit: str = 'Celsius'  # 클래스 변수\n"
                    "\n"
                    "    def __init__(self, celsius: float) -> None:\n"
                    "        self.celsius = celsius  # 인스턴스 변수\n"
                    "\n"
                    "    # ── 인스턴스 메서드 ── (self로 인스턴스 데이터 접근)\n"
                    "    def to_fahrenheit(self) -> float:\n"
                    "        \"\"\"섭씨를 화씨로 변환한다.\"\"\"\n"
                    "        return self.celsius * 9 / 5 + 32\n"
                    "\n"
                    "    def describe(self) -> str:\n"
                    "        \"\"\"온도 상태를 문자열로 반환한다.\"\"\"\n"
                    "        if self.celsius >= 30:\n"
                    "            return f'{self.celsius}°C — 더운 날씨'\n"
                    "        elif self.celsius >= 10:\n"
                    "            return f'{self.celsius}°C — 적당한 날씨'\n"
                    "        return f'{self.celsius}°C — 추운 날씨'\n"
                    "\n"
                    "    # ── 클래스 메서드 ── (cls로 클래스 데이터 접근, 대안 생성자)\n"
                    "    @classmethod\n"
                    "    def from_fahrenheit(cls, fahrenheit: float) -> 'Temperature':\n"
                    "        \"\"\"화씨 온도로부터 Temperature 인스턴스를 생성한다.\"\"\"\n"
                    "        celsius = (fahrenheit - 32) * 5 / 9\n"
                    "        return cls(round(celsius, 1))  # 새 인스턴스 반환\n"
                    "\n"
                    "    @classmethod\n"
                    "    def change_unit(cls, new_unit: str) -> None:\n"
                    "        \"\"\"모든 인스턴스에서 사용할 단위를 변경한다.\"\"\"\n"
                    "        cls.unit = new_unit\n"
                    "\n"
                    "    # ── 정적 메서드 ── (self나 cls 없이 독립적으로 동작)\n"
                    "    @staticmethod\n"
                    "    def is_valid_celsius(value: float) -> bool:\n"
                    "        \"\"\"유효한 섭씨 온도 범위(-273.15 이상)인지 확인한다.\"\"\"\n"
                    "        return value >= -273.15  # 절대영도보다 낮을 수 없음\n"
                    "\n"
                    "\n"
                    "# 사용 예시\n"
                    "t1 = Temperature(25)\n"
                    "print(t1.to_fahrenheit())    # 77.0\n"
                    "print(t1.describe())         # 25°C — 적당한 날씨\n"
                    "\n"
                    "# 클래스 메서드로 화씨에서 생성\n"
                    "t2 = Temperature.from_fahrenheit(98.6)\n"
                    "print(t2.celsius)            # 37.0 (체온)\n"
                    "\n"
                    "# 정적 메서드 호출 — 인스턴스 없이도 가능\n"
                    "print(Temperature.is_valid_celsius(-300))  # False\n"
                    "print(Temperature.is_valid_celsius(100))   # True"
                ),
            },
            {
                "type": "tip",
                "text": "언제 어떤 메서드를 쓸까? — 인스턴스 변수(self.xxx)를 사용한다면 인스턴스 메서드, 클래스 변수(cls.xxx)만 사용한다면 클래스 메서드, 클래스/인스턴스 데이터가 전혀 필요 없다면 정적 메서드입니다.",
            },
        ],
    }


def _section_access_control():
    """섹션 6: 접근 제어 관례."""
    return {
        "title": "접근 제어 관례 — _내부용과 __이름 맹글링",
        "content": [
            "Python은 Java처럼 `private`, `public` 키워드가 없습니다. 대신 이름 규칙으로 접근 의도를 표현합니다.",
            {
                "type": "table",
                "headers": ["이름 패턴", "의미", "실제 접근 가능?", "예시"],
                "rows": [
                    ["name", "공개(public)", "O", "self.name"],
                    ["_name", "내부 사용(비공개 권장)", "O (하지만 하지 마세요)", "self._balance"],
                    ["__name", "이름 맹글링(강한 비공개)", "직접 접근 차단", "self.__password"],
                    ["__name__", "매직/던더 메서드", "O (Python 예약)", "__init__, __str__"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class BankAccount:\n"
                    "    \"\"\"은행 계좌 클래스 — 접근 제어 예시.\"\"\"\n"
                    "\n"
                    "    def __init__(self, owner: str, initial_balance: float) -> None:\n"
                    "        self.owner = owner              # 공개 속성\n"
                    "        self._balance = initial_balance  # 비공개 권장 (관례)\n"
                    "        self.__account_number = self._generate_account_number()\n"
                    "        # __account_number는 이름 맹글링으로 외부 접근 차단\n"
                    "\n"
                    "    def _generate_account_number(self) -> str:\n"
                    "        \"\"\"계좌번호 생성 (내부 전용 메서드).\"\"\"\n"
                    "        import random\n"
                    "        return f'110-{random.randint(100000, 999999)}-00'\n"
                    "\n"
                    "    def get_balance(self) -> float:\n"
                    "        \"\"\"잔액을 반환한다 (안전한 공개 접근 방법).\"\"\"\n"
                    "        return self._balance\n"
                    "\n"
                    "    def deposit(self, amount: float) -> None:\n"
                    "        \"\"\"입금한다.\"\"\"\n"
                    "        if amount <= 0:\n"
                    "            raise ValueError('입금액은 양수여야 합니다.')\n"
                    "        self._balance += amount\n"
                    "        print(f'{amount:,.0f}원 입금 완료. 잔액: {self._balance:,.0f}원')\n"
                    "\n"
                    "\n"
                    "account = BankAccount('홍길동', 100000)\n"
                    "\n"
                    "# 공개 속성 접근\n"
                    "print(account.owner)         # 홍길동\n"
                    "print(account.get_balance())  # 100000\n"
                    "account.deposit(50000)        # 50,000원 입금 완료. 잔액: 150,000원\n"
                    "\n"
                    "# _balance에는 접근 가능하지만 하면 안 됩니다 (관례 위반)\n"
                    "# print(account._balance)   ← 동작하지만 비권장\n"
                    "\n"
                    "# __account_number에는 직접 접근 불가\n"
                    "# print(account.__account_number)  ← AttributeError 발생!\n"
                    "# 이름 맹글링된 실제 이름으로만 접근 가능 (비권장)\n"
                    "print(account._BankAccount__account_number)  # 맹글링된 실제 이름"
                ),
            },
            {
                "type": "analogy",
                "text": (
                    "_변수는 '관계자 외 출입 금지' 표지판과 같습니다. 물리적으로 막지는 않지만 '이건 내부용이니 건드리지 마세요'라는 신호입니다. "
                    "__변수는 자물쇠를 채운 것과 같습니다. Python이 이름을 바꿔버려서 직접 접근이 어렵습니다."
                ),
            },
            {
                "type": "note",
                "text": "Python의 철학은 '어른을 믿는다'입니다. 강제로 막기보다 관례로 알려줍니다. _로 시작하는 변수는 '내가 나중에 바꿀 수 있으니 직접 사용하지 마세요'라는 개발자의 의도 표현입니다.",
            },
        ],
    }


def _section_practical_examples():
    """섹션 7: 실용 예제."""
    return {
        "title": "실용 예제 — 은행 계좌와 학생 성적 관리",
        "content": [
            "지금까지 배운 내용을 종합하여 두 가지 실용적인 클래스를 만들어봅니다.",
            "**예제 1: 은행 계좌 클래스**",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class BankAccount:\n"
                    "    \"\"\"은행 계좌를 표현하는 클래스.\"\"\"\n"
                    "\n"
                    "    # 클래스 변수: 은행명과 이자율은 모든 계좌 공통\n"
                    "    bank_name: str = '파이썬 은행'\n"
                    "    interest_rate: float = 0.03  # 연 3%\n"
                    "\n"
                    "    def __init__(self, owner: str, initial_balance: float = 0) -> None:\n"
                    "        \"\"\"계좌를 개설한다.\"\"\"\n"
                    "        self.owner = owner\n"
                    "        self._balance = initial_balance\n"
                    "        self._transaction_history: list = []  # 거래 내역\n"
                    "\n"
                    "    def deposit(self, amount: float) -> None:\n"
                    "        \"\"\"입금한다.\"\"\"\n"
                    "        if amount <= 0:\n"
                    "            print('오류: 입금액은 0보다 커야 합니다.')\n"
                    "            return\n"
                    "        self._balance += amount\n"
                    "        self._transaction_history.append(f'입금 +{amount:,.0f}원')\n"
                    "        print(f'입금 완료. 현재 잔액: {self._balance:,.0f}원')\n"
                    "\n"
                    "    def withdraw(self, amount: float) -> None:\n"
                    "        \"\"\"출금한다.\"\"\"\n"
                    "        if amount <= 0:\n"
                    "            print('오류: 출금액은 0보다 커야 합니다.')\n"
                    "            return\n"
                    "        if amount > self._balance:\n"
                    "            print(f'오류: 잔액 부족. 현재 잔액: {self._balance:,.0f}원')\n"
                    "            return\n"
                    "        self._balance -= amount\n"
                    "        self._transaction_history.append(f'출금 -{amount:,.0f}원')\n"
                    "        print(f'출금 완료. 현재 잔액: {self._balance:,.0f}원')\n"
                    "\n"
                    "    def apply_interest(self) -> None:\n"
                    "        \"\"\"연이자를 적용한다.\"\"\"\n"
                    "        interest = self._balance * BankAccount.interest_rate\n"
                    "        self._balance += interest\n"
                    "        self._transaction_history.append(f'이자 +{interest:,.0f}원')\n"
                    "\n"
                    "    def get_balance(self) -> float:\n"
                    "        \"\"\"현재 잔액을 반환한다.\"\"\"\n"
                    "        return self._balance\n"
                    "\n"
                    "    def print_statement(self) -> None:\n"
                    "        \"\"\"거래 내역을 출력한다.\"\"\"\n"
                    "        print(f'\\n[{BankAccount.bank_name}] {self.owner} 님의 거래 내역')\n"
                    "        print('-' * 40)\n"
                    "        for record in self._transaction_history:\n"
                    "            print(f'  {record}')\n"
                    "        print(f'  최종 잔액: {self._balance:,.0f}원')\n"
                    "\n"
                    "\n"
                    "# 사용 예시\n"
                    "account = BankAccount('홍길동', 500000)\n"
                    "account.deposit(200000)\n"
                    "account.withdraw(100000)\n"
                    "account.apply_interest()\n"
                    "account.print_statement()"
                ),
            },
            "**예제 2: 학생 성적 관리 클래스**",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class Student:\n"
                    "    \"\"\"학생 성적을 관리하는 클래스.\"\"\"\n"
                    "\n"
                    "    GRADE_SCALE = {  # 클래스 변수: 모든 학생 공통 기준\n"
                    "        'A': (90, 100),\n"
                    "        'B': (80, 89),\n"
                    "        'C': (70, 79),\n"
                    "        'D': (60, 69),\n"
                    "        'F': (0, 59),\n"
                    "    }\n"
                    "\n"
                    "    def __init__(self, name: str, student_id: str) -> None:\n"
                    "        \"\"\"학생 인스턴스를 초기화한다.\"\"\"\n"
                    "        self.name = name\n"
                    "        self.student_id = student_id\n"
                    "        self._scores: dict = {}  # {'과목명': 점수}\n"
                    "\n"
                    "    def add_score(self, subject: str, score: int) -> None:\n"
                    "        \"\"\"과목 점수를 추가한다.\"\"\"\n"
                    "        if not 0 <= score <= 100:\n"
                    "            print(f'오류: 점수는 0~100 범위여야 합니다. 입력값: {score}')\n"
                    "            return\n"
                    "        self._scores[subject] = score\n"
                    "\n"
                    "    def get_average(self) -> float:\n"
                    "        \"\"\"평균 점수를 반환한다.\"\"\"\n"
                    "        if not self._scores:\n"
                    "            return 0.0\n"
                    "        return round(sum(self._scores.values()) / len(self._scores), 1)\n"
                    "\n"
                    "    def get_grade(self) -> str:\n"
                    "        \"\"\"평균 점수에 따른 학점을 반환한다.\"\"\"\n"
                    "        avg = self.get_average()\n"
                    "        for grade, (low, high) in Student.GRADE_SCALE.items():\n"
                    "            if low <= avg <= high:\n"
                    "                return grade\n"
                    "        return 'F'\n"
                    "\n"
                    "    def report(self) -> None:\n"
                    "        \"\"\"성적표를 출력한다.\"\"\"\n"
                    "        print(f'\\n성적표 — {self.name} ({self.student_id})')\n"
                    "        print('-' * 30)\n"
                    "        for subject, score in self._scores.items():\n"
                    "            print(f'  {subject}: {score}점')\n"
                    "        print(f'  평균: {self.get_average()}점 ({self.get_grade()}학점)')\n"
                    "\n"
                    "\n"
                    "# 사용 예시\n"
                    "s = Student('홍길동', '2024001')\n"
                    "s.add_score('수학', 88)\n"
                    "s.add_score('영어', 92)\n"
                    "s.add_score('파이썬', 95)\n"
                    "s.report()"
                ),
            },
            {
                "type": "tip",
                "text": "클래스를 잘 설계하면 main 코드가 매우 깔끔해집니다. '어떻게 구현할까'보다 '무엇을 할 수 있어야 하나'를 먼저 생각하고 메서드 이름을 먼저 정하는 것이 좋은 설계의 출발점입니다.",
            },
        ],
    }
