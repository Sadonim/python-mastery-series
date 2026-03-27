"""Chapter 2: 상속과 다형성 - 코드 재사용과 유연한 설계의 핵심."""


def get_chapter():
    """챕터 2의 전체 콘텐츠를 딕셔너리로 반환한다."""
    return {
        "number": 2,
        "title": "상속과 다형성",
        "subtitle": "코드 재사용과 유연한 설계의 핵심",
        "big_picture": (
            "클래스를 배웠다면 이제 클래스들 사이의 '관계'를 다룰 차례입니다. "
            "상속(Inheritance)은 기존 클래스의 속성과 메서드를 물려받아 "
            "새 클래스를 만드는 기법으로, 코드 중복을 획기적으로 줄여줍니다. "
            "다형성(Polymorphism)은 '같은 이름의 메서드가 객체 종류에 따라 다르게 동작'하는 것으로, "
            "유연하고 확장 가능한 코드를 만드는 핵심 원리입니다. "
            "실용 예제로는 도형 클래스 계층(Shape → Circle, Rectangle, Triangle)을 구현합니다."
        ),
        "sections": [
            _section_inheritance_concept(),
            _section_parent_child_class(),
            _section_super(),
            _section_method_overriding(),
            _section_polymorphism(),
            _section_multiple_inheritance(),
            _section_isinstance_issubclass(),
        ],
        "practical_tips": [
            "상속을 쓰기 전에 'IS-A 관계'인지 확인하세요. '원(Circle)은 도형(Shape)이다' ✓, '자동차(Car)는 엔진(Engine)이다' ✗ (이 경우 합성(composition)이 더 적합).",
            "자식 클래스에서 `__init__`을 재정의할 때는 `super().__init__()`을 잊지 마세요. 부모의 초기화가 누락되면 예상치 못한 버그가 생깁니다.",
            "다중 상속은 강력하지만 복잡합니다. MRO를 이해하지 못한 채 사용하면 찾기 어려운 버그가 생깁니다. 가능하면 단일 상속을 먼저 시도하세요.",
            "`isinstance()` 확인을 남발하면 다형성의 장점이 사라집니다. 타입에 따라 분기하는 코드 대신 메서드 오버라이딩으로 해결하는 것이 OOP 답습니다.",
            "추상 메서드(abstract method)가 필요하다면 `abc` 모듈의 `ABC`와 `@abstractmethod`를 활용하세요. 자식 클래스가 반드시 구현해야 하는 메서드를 강제할 수 있습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "상속에서 `super()`를 사용하는 주된 목적은?",
                "choices": [
                    "A) 자식 클래스의 메서드를 부모 클래스에서 호출하기 위해",
                    "B) 부모 클래스의 메서드나 생성자를 자식 클래스에서 호출하기 위해",
                    "C) 클래스 변수를 초기화하기 위해",
                    "D) 정적 메서드를 호출하기 위해",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "다형성(Polymorphism)의 개념을 가장 잘 설명한 것은?",
                "choices": [
                    "A) 하나의 클래스가 여러 클래스를 동시에 상속받는 것",
                    "B) 같은 이름의 메서드가 객체 종류에 따라 다른 방식으로 동작하는 것",
                    "C) 클래스의 내부 데이터를 숨기는 것",
                    "D) 자식 클래스가 부모 클래스의 변수를 공유하는 것",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "Python에서 MRO(Method Resolution Order)란 무엇인가?",
                "choices": [
                    "A) 메서드를 알파벳 순서로 정렬하는 규칙",
                    "B) 다중 상속 시 메서드를 어느 클래스에서 찾을지 결정하는 순서",
                    "C) 정적 메서드와 클래스 메서드를 구분하는 방법",
                    "D) 인스턴스 메서드의 실행 속도를 결정하는 알고리즘",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "`Animal` 기본 클래스와 `Dog`, `Cat` 자식 클래스를 작성하세요.\n"
                    "- Animal: 속성(name, age), 메서드 speak() → '동물이 소리를 냅니다' 출력\n"
                    "- Dog: speak() 오버라이딩 → '{name}: 왈왈!' 출력\n"
                    "- Cat: speak() 오버라이딩 → '{name}: 야옹~' 출력\n"
                    "animals = [Dog('뽀삐', 3), Cat('나비', 2), Dog('초코', 5)]\n"
                    "for animal in animals:\n"
                    "    animal.speak()  # 각자의 speak() 호출 — 다형성 시연"
                ),
                "hint": "자식 클래스의 `__init__`에서 `super().__init__(name, age)`를 호출하고, speak() 메서드를 각 클래스에서 재정의하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "도형 계층 구조를 작성하세요.\n"
                    "- Shape 기본 클래스: name 속성, area() → 0 반환, describe() → '도형: {name}, 넓이: {area()}' 출력\n"
                    "- Circle(Shape): radius 속성, area() 오버라이딩 (π * r²)\n"
                    "- Rectangle(Shape): width, height 속성, area() 오버라이딩 (w * h)\n"
                    "shapes = [Circle(5), Rectangle(3, 4)]\n"
                    "for s in shapes:\n"
                    "    s.describe()  # 각 도형의 넓이 출력"
                ),
                "hint": "`import math`로 `math.pi`를 사용하세요. describe()는 Shape 클래스에 한 번만 정의하면 자식 클래스에서 area()를 오버라이딩했을 때 자동으로 올바른 값이 사용됩니다.",
            },
        ],
        "challenge": {
            "question": (
                "'직원 관리 시스템'을 만들어보세요.\n"
                "Employee 기본 클래스: 속성(name, employee_id, base_salary), "
                "메서드(calculate_pay() → base_salary 반환, get_info() 출력)\n"
                "FullTimeEmployee(Employee): 보너스 비율 속성, calculate_pay() 오버라이딩 (base_salary * (1 + bonus_rate))\n"
                "PartTimeEmployee(Employee): 시급과 근무 시간 속성, calculate_pay() 오버라이딩 (hourly_rate * hours_worked)\n"
                "Intern(PartTimeEmployee): 수련 기간 속성, get_info() 오버라이딩 (인턴 표시 추가)\n"
                "직원 리스트에서 모든 직원의 급여 합산 및 직원별 정보 출력"
            ),
            "hint": (
                "calculate_pay()를 다형성으로 설계하면 직원 리스트를 순회하며 "
                "타입을 확인하지 않고도 `sum(emp.calculate_pay() for emp in employees)`처럼 "
                "한 줄로 급여 합산이 가능합니다."
            ),
        },
        "summary": [
            "상속은 기존 클래스(부모)의 속성과 메서드를 새 클래스(자식)가 물려받아 코드 중복을 줄이는 기법이다.",
            "자식 클래스는 `class Child(Parent):` 형식으로 정의하며, `super()`로 부모의 메서드/생성자를 호출한다.",
            "메서드 오버라이딩: 자식 클래스에서 부모 메서드를 같은 이름으로 재정의하면 자식 버전이 실행된다.",
            "다형성: 같은 인터페이스(메서드 이름)를 공유하는 여러 객체를 동일한 방식으로 다룰 수 있다.",
            "다중 상속 시 MRO(C3 선형화 알고리즘)에 따라 메서드를 탐색하며, `클래스.__mro__`로 순서를 확인할 수 있다.",
            "`isinstance(obj, Class)`는 객체가 해당 클래스(또는 자식 클래스)의 인스턴스인지 확인하고, `issubclass(Child, Parent)`는 클래스 관계를 확인한다.",
        ],
    }


def _section_inheritance_concept():
    """섹션 1: 상속의 개념과 필요성."""
    return {
        "title": "상속(Inheritance)이란? — 왜 필요한가",
        "content": [
            "상속이 없다면 비슷한 클래스를 만들 때마다 같은 코드를 반복 작성해야 합니다. 상속은 이 문제를 해결하는 핵심 도구입니다.",
            {
                "type": "analogy",
                "text": (
                    "유전(遺傳)을 생각해보세요. 자녀는 부모의 눈 색깔, 혈액형, 체형 같은 특성을 물려받습니다. "
                    "프로그래밍의 상속도 마찬가지입니다. "
                    "자식 클래스는 부모 클래스의 모든 속성과 메서드를 물려받고, "
                    "자신만의 고유한 특성을 추가하거나 부모의 특성을 변형할 수 있습니다. "
                    "군에 비유하면: 소대는 중대의 규칙을 그대로 따르면서(상속) 소대만의 특수 임무(추가 메서드)를 가집니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 상속 없이 작성한 경우 — 코드 중복이 심하다 ──\n"
                    "class Dog:\n"
                    "    def __init__(self, name: str, age: int) -> None:\n"
                    "        self.name = name  # 중복!\n"
                    "        self.age = age    # 중복!\n"
                    "\n"
                    "    def eat(self) -> str:   # 중복!\n"
                    "        return f'{self.name}이(가) 밥을 먹습니다.'\n"
                    "\n"
                    "    def sleep(self) -> str:  # 중복!\n"
                    "        return f'{self.name}이(가) 잠을 잡니다.'\n"
                    "\n"
                    "    def bark(self) -> str:   # Dog만의 메서드\n"
                    "        return '왈왈!'\n"
                    "\n"
                    "\n"
                    "class Cat:\n"
                    "    def __init__(self, name: str, age: int) -> None:\n"
                    "        self.name = name  # Dog와 완전히 동일 — 중복!\n"
                    "        self.age = age    # 중복!\n"
                    "\n"
                    "    def eat(self) -> str:    # 중복!\n"
                    "        return f'{self.name}이(가) 밥을 먹습니다.'\n"
                    "\n"
                    "    def sleep(self) -> str:  # 중복!\n"
                    "        return f'{self.name}이(가) 잠을 잡니다.'\n"
                    "\n"
                    "    def meow(self) -> str:   # Cat만의 메서드\n"
                    "        return '야옹~'"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 상속을 사용한 경우 — 공통 코드를 부모 클래스에 한 번만 작성 ──\n"
                    "class Animal:\n"
                    "    \"\"\"모든 동물의 공통 기능을 정의하는 부모 클래스.\"\"\"\n"
                    "\n"
                    "    def __init__(self, name: str, age: int) -> None:\n"
                    "        self.name = name\n"
                    "        self.age = age\n"
                    "\n"
                    "    def eat(self) -> str:\n"
                    "        return f'{self.name}이(가) 밥을 먹습니다.'\n"
                    "\n"
                    "    def sleep(self) -> str:\n"
                    "        return f'{self.name}이(가) 잠을 잡니다.'\n"
                    "\n"
                    "\n"
                    "class Dog(Animal):  # Animal을 상속 — Animal의 모든 것을 물려받음\n"
                    "    def bark(self) -> str:\n"
                    "        return '왈왈!'\n"
                    "\n"
                    "\n"
                    "class Cat(Animal):  # Animal을 상속\n"
                    "    def meow(self) -> str:\n"
                    "        return '야옹~'\n"
                    "\n"
                    "\n"
                    "dog = Dog('뽀삐', 3)\n"
                    "print(dog.eat())    # 뽀삐이(가) 밥을 먹습니다. (Animal에서 상속)\n"
                    "print(dog.sleep())  # 뽀삐이(가) 잠을 잡니다. (Animal에서 상속)\n"
                    "print(dog.bark())   # 왈왈! (Dog만의 메서드)"
                ),
            },
            {
                "type": "flow_diagram",
                "nodes": [
                    "Animal (부모/슈퍼 클래스)",
                    "├── Dog (자식/서브 클래스)",
                    "├── Cat (자식/서브 클래스)",
                    "└── Bird (자식/서브 클래스)",
                ],
                "note": "계층 구조: 부모 클래스의 공통 기능을 자식들이 공유",
            },
            {
                "type": "note",
                "text": "IS-A 관계 확인: '개는 동물이다(Dog IS-A Animal)' — 상속 적합. 'HAS-A 관계'(개는 목줄을 가진다)는 합성(Composition)이 더 적합합니다.",
            },
        ],
    }


def _section_parent_child_class():
    """섹션 2: 부모/자식 클래스."""
    return {
        "title": "부모 클래스와 자식 클래스",
        "content": [
            "부모 클래스(parent/super class)는 공통 기능을 정의하고, 자식 클래스(child/sub class)는 이를 물려받아 확장합니다.",
            {
                "type": "table",
                "headers": ["용어", "다른 이름", "설명"],
                "rows": [
                    ["부모 클래스", "슈퍼 클래스, 베이스 클래스", "공통 기능을 정의하는 상위 클래스"],
                    ["자식 클래스", "서브 클래스, 파생 클래스", "부모를 상속받아 확장하는 하위 클래스"],
                    ["상속", "inheritance, 확장", "부모의 속성/메서드를 자식이 물려받는 것"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 기본 상속 문법 ──\n"
                    "class Vehicle:  # 부모 클래스\n"
                    "    \"\"\"모든 운송수단의 공통 기능.\"\"\"\n"
                    "\n"
                    "    def __init__(self, brand: str, speed: int) -> None:\n"
                    "        self.brand = brand\n"
                    "        self.speed = speed      # 최고 속도 (km/h)\n"
                    "        self.current_speed = 0  # 현재 속도\n"
                    "\n"
                    "    def accelerate(self, amount: int) -> None:\n"
                    "        \"\"\"속도를 높인다.\"\"\"\n"
                    "        self.current_speed = min(self.current_speed + amount, self.speed)\n"
                    "        print(f'현재 속도: {self.current_speed}km/h')\n"
                    "\n"
                    "    def stop(self) -> None:\n"
                    "        \"\"\"정지한다.\"\"\"\n"
                    "        self.current_speed = 0\n"
                    "        print('정지했습니다.')\n"
                    "\n"
                    "    def __str__(self) -> str:\n"
                    "        return f'{self.brand} (최고속도: {self.speed}km/h)'\n"
                    "\n"
                    "\n"
                    "class Car(Vehicle):  # Vehicle을 상속\n"
                    "    \"\"\"자동차 — Vehicle의 모든 기능 + 자동차 고유 기능.\"\"\"\n"
                    "\n"
                    "    def __init__(self, brand: str, speed: int, doors: int) -> None:\n"
                    "        # 부모의 __init__ 호출 (다음 섹션에서 자세히)\n"
                    "        super().__init__(brand, speed)\n"
                    "        self.doors = doors  # Car만의 속성\n"
                    "\n"
                    "    def honk(self) -> str:\n"
                    "        \"\"\"경적을 울린다 — Car만의 메서드.\"\"\"\n"
                    "        return f'{self.brand}: 빵빵!'\n"
                    "\n"
                    "\n"
                    "class Motorcycle(Vehicle):  # Vehicle을 상속\n"
                    "    \"\"\"오토바이.\"\"\"\n"
                    "\n"
                    "    def wheelie(self) -> str:\n"
                    "        \"\"\"앞바퀴를 들어 올린다 — Motorcycle만의 메서드.\"\"\"\n"
                    "        if self.current_speed > 30:\n"
                    "            return '윌리 성공!'\n"
                    "        return '속도가 부족합니다.'\n"
                    "\n"
                    "\n"
                    "car = Car('현대', 200, 4)\n"
                    "car.accelerate(80)    # Vehicle에서 상속한 메서드\n"
                    "print(car.honk())     # Car만의 메서드\n"
                    "print(car)            # Vehicle의 __str__ 상속: 현대 (최고속도: 200km/h)"
                ),
            },
            {
                "type": "tip",
                "text": "`dir(인스턴스)`를 실행하면 해당 객체가 가진 모든 속성과 메서드(상속된 것 포함) 목록을 볼 수 있습니다. `vars(인스턴스)`는 인스턴스 변수 딕셔너리만 보여줍니다.",
            },
        ],
    }


def _section_super():
    """섹션 3: super() 사용법."""
    return {
        "title": "`super()` — 부모에게 위임하기",
        "content": [
            "`super()`는 부모 클래스를 참조하는 프록시 객체를 반환합니다. 주로 자식 클래스에서 부모의 `__init__`이나 오버라이딩한 메서드를 호출할 때 사용합니다.",
            {
                "type": "analogy",
                "text": (
                    "군대에서 자대 배치 시 인사 절차를 생각해보세요. "
                    "신임 장교는 부대 고유 절차를 추가하기 전에 반드시 상급부대 표준 절차(부모 절차)를 먼저 완료해야 합니다. "
                    "`super().__init__()`이 바로 그 역할입니다. "
                    "부모의 초기화를 먼저 완료하고, 그 위에 자식만의 초기화를 추가합니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "class Person:\n"
                    "    \"\"\"사람을 표현하는 기본 클래스.\"\"\"\n"
                    "\n"
                    "    def __init__(self, name: str, age: int) -> None:\n"
                    "        self.name = name\n"
                    "        self.age = age\n"
                    "        print(f'Person.__init__ 호출됨: {name}')\n"
                    "\n"
                    "    def introduce(self) -> str:\n"
                    "        return f'안녕하세요, 저는 {self.name}이고 {self.age}살입니다.'\n"
                    "\n"
                    "\n"
                    "class Student(Person):\n"
                    "    \"\"\"학생 — Person을 상속.\"\"\"\n"
                    "\n"
                    "    def __init__(self, name: str, age: int, major: str) -> None:\n"
                    "        # 1. 부모의 __init__을 먼저 호출 (name, age 초기화)\n"
                    "        super().__init__(name, age)\n"
                    "        # 2. 자식만의 속성 추가\n"
                    "        self.major = major\n"
                    "        print(f'Student.__init__ 호출됨: 전공={major}')\n"
                    "\n"
                    "    def introduce(self) -> str:\n"
                    "        # 부모의 introduce() 결과를 재사용\n"
                    "        base = super().introduce()\n"
                    "        return f'{base} 전공은 {self.major}입니다.'\n"
                    "\n"
                    "\n"
                    "class GraduateStudent(Student):\n"
                    "    \"\"\"대학원생 — Student를 상속 (2단계 상속).\"\"\"\n"
                    "\n"
                    "    def __init__(self, name: str, age: int, major: str, thesis: str) -> None:\n"
                    "        super().__init__(name, age, major)  # Student.__init__ 호출\n"
                    "        self.thesis = thesis\n"
                    "\n"
                    "    def introduce(self) -> str:\n"
                    "        base = super().introduce()  # Student.introduce() 호출\n"
                    "        return f'{base} 논문 주제: {self.thesis}'\n"
                    "\n"
                    "\n"
                    "# 실행\n"
                    "gs = GraduateStudent('홍길동', 28, '컴퓨터공학', 'Python ML 최적화')\n"
                    "# 출력 순서:\n"
                    "# Person.__init__ 호출됨: 홍길동\n"
                    "# Student.__init__ 호출됨: 전공=컴퓨터공학\n"
                    "print(gs.introduce())"
                ),
            },
            {
                "type": "warning",
                "text": "자식 클래스에서 `__init__`을 정의할 때 `super().__init__()`을 호출하지 않으면 부모의 인스턴스 변수가 초기화되지 않습니다. 부모 메서드를 호출하면 `AttributeError`가 발생할 수 있습니다.",
            },
            {
                "type": "note",
                "text": "Python 2에서는 `super(ClassName, self).__init__()`처럼 써야 했지만, Python 3에서는 `super().__init__()`만 써도 됩니다. Python 3을 사용한다면 인수 없는 형식을 항상 사용하세요.",
            },
        ],
    }


def _section_method_overriding():
    """섹션 4: 메서드 오버라이딩."""
    return {
        "title": "메서드 오버라이딩 — 부모의 행동을 바꾸다",
        "content": [
            "자식 클래스에서 부모 클래스와 **같은 이름**의 메서드를 정의하면, 자식 버전이 부모 버전을 덮어씁니다. 이를 메서드 오버라이딩(Method Overriding)이라 합니다.",
            {
                "type": "flow_diagram",
                "nodes": [
                    "dog.speak() 호출",
                    "→ Python이 Dog 클래스에서 speak() 탐색",
                    "→ Dog에 speak() 있음 → Dog.speak() 실행",
                    "만약 Dog에 없다면 → Animal.speak() 실행 (상속)",
                ],
                "note": "메서드 탐색 순서: 자식 클래스 → 부모 클래스",
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "import math\n"
                    "\n"
                    "\n"
                    "class Shape:\n"
                    "    \"\"\"모든 도형의 기본 클래스.\"\"\"\n"
                    "\n"
                    "    def __init__(self, name: str) -> None:\n"
                    "        self.name = name\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        \"\"\"넓이를 반환한다 (자식 클래스에서 오버라이딩 필요).\"\"\"\n"
                    "        return 0.0\n"
                    "\n"
                    "    def perimeter(self) -> float:\n"
                    "        \"\"\"둘레를 반환한다 (자식 클래스에서 오버라이딩 필요).\"\"\"\n"
                    "        return 0.0\n"
                    "\n"
                    "    def describe(self) -> str:\n"
                    "        \"\"\"도형 정보를 반환한다 — 오버라이딩 없이 공통으로 사용.\"\"\"\n"
                    "        return (\n"
                    "            f'[{self.name}] '\n"
                    "            f'넓이: {self.area():.2f}, '\n"
                    "            f'둘레: {self.perimeter():.2f}'\n"
                    "        )\n"
                    "\n"
                    "\n"
                    "class Circle(Shape):\n"
                    "    \"\"\"원.\"\"\"\n"
                    "\n"
                    "    def __init__(self, radius: float) -> None:\n"
                    "        super().__init__('원')\n"
                    "        self.radius = radius\n"
                    "\n"
                    "    def area(self) -> float:       # Shape.area() 오버라이딩\n"
                    "        return math.pi * self.radius ** 2\n"
                    "\n"
                    "    def perimeter(self) -> float:  # Shape.perimeter() 오버라이딩\n"
                    "        return 2 * math.pi * self.radius\n"
                    "\n"
                    "\n"
                    "class Rectangle(Shape):\n"
                    "    \"\"\"직사각형.\"\"\"\n"
                    "\n"
                    "    def __init__(self, width: float, height: float) -> None:\n"
                    "        super().__init__('직사각형')\n"
                    "        self.width = width\n"
                    "        self.height = height\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return self.width * self.height\n"
                    "\n"
                    "    def perimeter(self) -> float:\n"
                    "        return 2 * (self.width + self.height)\n"
                    "\n"
                    "\n"
                    "class Triangle(Shape):\n"
                    "    \"\"\"삼각형.\"\"\"\n"
                    "\n"
                    "    def __init__(self, base: float, height: float, sides: tuple) -> None:\n"
                    "        super().__init__('삼각형')\n"
                    "        self.base = base\n"
                    "        self.height = height\n"
                    "        self.sides = sides  # (변1, 변2, 변3)\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return 0.5 * self.base * self.height\n"
                    "\n"
                    "    def perimeter(self) -> float:\n"
                    "        return sum(self.sides)\n"
                    "\n"
                    "\n"
                    "# 사용 예시\n"
                    "shapes = [\n"
                    "    Circle(5),\n"
                    "    Rectangle(4, 6),\n"
                    "    Triangle(3, 4, (3, 4, 5)),\n"
                    "]\n"
                    "\n"
                    "for shape in shapes:\n"
                    "    print(shape.describe())\n"
                    "# [원] 넓이: 78.54, 둘레: 31.42\n"
                    "# [직사각형] 넓이: 24.00, 둘레: 20.00\n"
                    "# [삼각형] 넓이: 6.00, 둘레: 12.00"
                ),
            },
            {
                "type": "tip",
                "text": "오버라이딩할 때 부모의 기존 동작을 완전히 대체할 수도 있고, `super().method_name()`으로 부모 동작을 먼저 실행한 뒤 추가 동작을 붙일 수도 있습니다. 상황에 맞게 선택하세요.",
            },
        ],
    }


def _section_polymorphism():
    """섹션 5: 다형성."""
    return {
        "title": "다형성(Polymorphism) — 같은 인터페이스, 다른 동작",
        "content": [
            "다형성은 '여러 형태'라는 뜻으로, 같은 메서드 이름으로 다른 타입의 객체를 동일하게 다룰 수 있는 능력입니다.",
            {
                "type": "analogy",
                "text": (
                    "리모컨의 '전원 버튼'을 생각해보세요. "
                    "TV 리모컨의 전원 버튼, 에어컨 리모컨의 전원 버튼, 오디오 리모컨의 전원 버튼은 "
                    "모두 '전원을 켜고 끄는 동작'이지만 각 기기마다 내부 동작은 다릅니다. "
                    "사용자는 '전원 버튼'만 알면 어떤 기기든 조작할 수 있습니다. "
                    "이것이 다형성의 힘입니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 다형성 시연 ── 앞 섹션의 Shape 계층 활용\n"
                    "import math\n"
                    "\n"
                    "\n"
                    "class Shape:\n"
                    "    def area(self) -> float:\n"
                    "        return 0.0\n"
                    "\n"
                    "\n"
                    "class Circle(Shape):\n"
                    "    def __init__(self, radius: float) -> None:\n"
                    "        self.radius = radius\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return math.pi * self.radius ** 2\n"
                    "\n"
                    "\n"
                    "class Rectangle(Shape):\n"
                    "    def __init__(self, width: float, height: float) -> None:\n"
                    "        self.width = width\n"
                    "        self.height = height\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return self.width * self.height\n"
                    "\n"
                    "\n"
                    "class Triangle(Shape):\n"
                    "    def __init__(self, base: float, height: float) -> None:\n"
                    "        self.base = base\n"
                    "        self.height = height\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return 0.5 * self.base * self.height\n"
                    "\n"
                    "\n"
                    "# 다형성: 타입을 몰라도 area()를 동일하게 호출 가능\n"
                    "shapes: list = [\n"
                    "    Circle(5),\n"
                    "    Rectangle(3, 4),\n"
                    "    Triangle(6, 8),\n"
                    "    Circle(2),\n"
                    "]\n"
                    "\n"
                    "# 모든 도형의 총 넓이 계산 — 타입 확인 없이!\n"
                    "total_area = sum(shape.area() for shape in shapes)\n"
                    "print(f'모든 도형의 총 넓이: {total_area:.2f}')\n"
                    "\n"
                    "# 가장 넓은 도형 찾기 — max()의 key로 다형성 활용\n"
                    "largest = max(shapes, key=lambda s: s.area())\n"
                    "print(f'가장 넓은 도형: {type(largest).__name__}, 넓이: {largest.area():.2f}')"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 덕 타이핑(Duck Typing) — Python의 다형성 ──\n"
                    "# 'speak() 메서드만 있으면 어떤 객체든 OK' — 상속 없이도 다형성 가능!\n"
                    "\n"
                    "class Dog:\n"
                    "    def speak(self) -> str:\n"
                    "        return '왈왈!'\n"
                    "\n"
                    "\n"
                    "class Cat:\n"
                    "    def speak(self) -> str:\n"
                    "        return '야옹~'\n"
                    "\n"
                    "\n"
                    "class Robot:  # Animal과 무관하지만 speak()가 있음\n"
                    "    def speak(self) -> str:\n"
                    "        return '삐빅~ 안녕하세요.'\n"
                    "\n"
                    "\n"
                    "# Dog, Cat, Robot은 서로 무관하지만 모두 speak()를 가짐\n"
                    "speakers = [Dog(), Cat(), Robot()]\n"
                    "for speaker in speakers:\n"
                    "    print(speaker.speak())  # 각자의 speak() 호출\n"
                    "\n"
                    "# '오리처럼 걷고 오리처럼 꽥꽥거리면, 그것은 오리다'\n"
                    "# — 타입이 아닌 동작(인터페이스)으로 판단하는 Python 철학"
                ),
            },
            {
                "type": "note",
                "text": "Python은 '덕 타이핑(Duck Typing)' 언어입니다. 객체의 타입보다 '어떤 메서드를 가지고 있는가'를 중시합니다. 상속 없이도 같은 인터페이스(메서드 이름)만 있으면 다형성이 적용됩니다.",
            },
        ],
    }


def _section_multiple_inheritance():
    """섹션 6: 다중 상속과 MRO."""
    return {
        "title": "다중 상속과 MRO — 두 부모를 가질 때",
        "content": [
            "Python은 하나의 클래스가 여러 부모 클래스를 동시에 상속받는 **다중 상속**을 지원합니다. 강력하지만 주의해서 사용해야 합니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 다중 상속 기본 예시 ──\n"
                    "class Flyable:\n"
                    "    \"\"\"날 수 있는 능력.\"\"\"\n"
                    "\n"
                    "    def fly(self) -> str:\n"
                    "        return '하늘을 날고 있습니다!'\n"
                    "\n"
                    "\n"
                    "class Swimmable:\n"
                    "    \"\"\"수영할 수 있는 능력.\"\"\"\n"
                    "\n"
                    "    def swim(self) -> str:\n"
                    "        return '물속을 헤엄치고 있습니다!'\n"
                    "\n"
                    "\n"
                    "class Duck(Flyable, Swimmable):  # 두 클래스를 동시에 상속\n"
                    "    \"\"\"오리 — 날 수도 있고 수영도 할 수 있음.\"\"\"\n"
                    "\n"
                    "    def quack(self) -> str:\n"
                    "        return '꽥꽥!'\n"
                    "\n"
                    "\n"
                    "duck = Duck()\n"
                    "print(duck.fly())    # 하늘을 날고 있습니다!\n"
                    "print(duck.swim())   # 물속을 헤엄치고 있습니다!\n"
                    "print(duck.quack())  # 꽥꽥!"
                ),
            },
            "**MRO(Method Resolution Order)**: 다중 상속 시 같은 이름의 메서드가 여러 부모에 있을 때, Python이 어느 클래스의 메서드를 먼저 실행할지 결정하는 순서입니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 다이아몬드 문제와 MRO ──\n"
                    "#\n"
                    "#       A\n"
                    "#      / \\\n"
                    "#     B   C\n"
                    "#      \\ /\n"
                    "#       D\n"
                    "\n"
                    "class A:\n"
                    "    def hello(self) -> str:\n"
                    "        return 'A에서 안녕!'\n"
                    "\n"
                    "\n"
                    "class B(A):\n"
                    "    def hello(self) -> str:\n"
                    "        return 'B에서 안녕!'\n"
                    "\n"
                    "\n"
                    "class C(A):\n"
                    "    def hello(self) -> str:\n"
                    "        return 'C에서 안녕!'\n"
                    "\n"
                    "\n"
                    "class D(B, C):  # B, C 순서로 상속\n"
                    "    pass\n"
                    "\n"
                    "\n"
                    "d = D()\n"
                    "print(d.hello())   # B에서 안녕! — B가 C보다 먼저 탐색\n"
                    "\n"
                    "# MRO 확인 — C3 선형화 알고리즘 결과\n"
                    "print(D.__mro__)\n"
                    "# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)\n"
                    "\n"
                    "# 더 읽기 좋게 출력\n"
                    "for cls in D.__mro__:\n"
                    "    print(cls.__name__, end=' → ')"
                ),
            },
            {
                "type": "table",
                "headers": ["MRO 탐색 순서", "설명"],
                "rows": [
                    ["1. D 자신", "D에 hello()가 있으면 바로 실행"],
                    ["2. B (첫 번째 부모)", "D에 없으면 B에서 탐색"],
                    ["3. C (두 번째 부모)", "B에도 없으면 C에서 탐색"],
                    ["4. A (공통 조상)", "C에도 없으면 A에서 탐색"],
                    ["5. object (최상위)", "모든 Python 클래스의 뿌리"],
                ],
            },
            {
                "type": "warning",
                "text": "다중 상속은 코드를 복잡하게 만들 수 있습니다. Python에서는 믹스인(Mixin) 패턴으로 다중 상속을 안전하게 사용합니다. 믹스인은 독립적으로 사용하지 않고, 기능 추가 목적으로만 상속하는 작은 클래스입니다.",
            },
        ],
    }


def _section_isinstance_issubclass():
    """섹션 7: isinstance()와 issubclass()."""
    return {
        "title": "`isinstance()`와 `issubclass()` — 타입 확인",
        "content": [
            "객체의 타입이나 클래스 간 관계를 확인해야 할 때 `isinstance()`와 `issubclass()`를 사용합니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "import math\n"
                    "\n"
                    "\n"
                    "class Shape:\n"
                    "    pass\n"
                    "\n"
                    "\n"
                    "class Circle(Shape):\n"
                    "    def __init__(self, radius: float) -> None:\n"
                    "        self.radius = radius\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return math.pi * self.radius ** 2\n"
                    "\n"
                    "\n"
                    "class Rectangle(Shape):\n"
                    "    def __init__(self, width: float, height: float) -> None:\n"
                    "        self.width = width\n"
                    "        self.height = height\n"
                    "\n"
                    "    def area(self) -> float:\n"
                    "        return self.width * self.height\n"
                    "\n"
                    "\n"
                    "c = Circle(5)\n"
                    "r = Rectangle(3, 4)\n"
                    "\n"
                    "# isinstance(객체, 클래스): 객체가 클래스의 인스턴스인지 확인\n"
                    "print(isinstance(c, Circle))    # True\n"
                    "print(isinstance(c, Shape))     # True — 부모 클래스도 True!\n"
                    "print(isinstance(c, Rectangle)) # False\n"
                    "print(isinstance(c, (Circle, Rectangle)))  # True — 여러 타입 동시 확인\n"
                    "\n"
                    "# issubclass(자식클래스, 부모클래스): 클래스 간 상속 관계 확인\n"
                    "print(issubclass(Circle, Shape))     # True\n"
                    "print(issubclass(Rectangle, Shape))  # True\n"
                    "print(issubclass(Circle, Rectangle)) # False\n"
                    "\n"
                    "# type() vs isinstance() 차이\n"
                    "print(type(c) == Circle)    # True (정확한 타입 일치만)\n"
                    "print(type(c) == Shape)     # False (부모 클래스는 False)\n"
                    "print(isinstance(c, Shape)) # True  (상속 관계도 True)"
                ),
            },
            {
                "type": "tip",
                "text": "타입 검사보다는 다형성을 우선 활용하세요. `isinstance()`로 타입을 일일이 확인하는 코드는 새로운 자식 클래스를 추가할 때마다 수정이 필요합니다. 메서드 오버라이딩으로 해결할 수 있다면 그 방법이 더 확장성 있는 설계입니다.",
            },
            {
                "type": "bullet_list",
                "items": [
                    "`isinstance(obj, Class)`: 런타임에 객체 타입 확인, 상속 관계도 True 반환",
                    "`issubclass(Child, Parent)`: 두 클래스 간 상속 관계 확인",
                    "`type(obj) == Class`: 정확한 타입 일치만 확인 (상속 관계 무시)",
                    "`obj.__class__.__name__`: 클래스 이름을 문자열로 반환",
                    "`클래스.__mro__`: 해당 클래스의 메서드 탐색 순서(MRO) 확인",
                ],
            },
        ],
    }
