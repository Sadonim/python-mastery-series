"""Chapter 2: 변수와 자료형 - 데이터에 이름 붙이기."""


def get_chapter():
    """챕터 2의 전체 콘텐츠를 딕셔너리로 반환한다."""
    return {
        "number": 2,
        "title": "변수와 자료형",
        "subtitle": "데이터에 이름 붙이기",
        "big_picture": (
            "프로그램은 데이터를 다루는 도구이고, 변수는 그 데이터를 담는 그릇입니다. "
            "이 챕터에서는 Python의 핵심 자료형(숫자, 문자열, 불리언, None)을 배우고, "
            "데이터를 저장하고 변환하는 방법을 익힙니다. "
            "변수와 자료형은 이후 모든 챕터의 기초이므로 확실히 이해해야 합니다."
        ),
        "sections": [
            _section_what_is_variable(),
            _section_numbers(),
            _section_strings(),
            _section_booleans(),
            _section_none(),
            _section_type_conversion(),
        ],
        "practical_tips": [
            "변수명은 영어 소문자와 밑줄 조합(`snake_case`)을 사용하세요. `myVar` 대신 `my_var`.",
            "숫자를 문자열과 연결할 때는 반드시 `str()`로 변환하세요: `'나이: ' + str(age)`.",
            "`type()` 함수는 디버깅의 첫 번째 도구입니다. 값이 예상과 다르게 동작하면 타입부터 확인하세요.",
            "f-string은 Python 3.6+에서 사용 가능하며, 문자열 포매팅 중 가장 읽기 쉬운 방식입니다.",
            "0, 빈 문자열(''), None은 모두 `False`로 평가됩니다. 이를 'falsy 값'이라고 합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "Python에서 변수 이름으로 사용할 수 없는 것은?",
                "choices": [
                    "A) my_name",
                    "B) _count",
                    "C) 2nd_place",
                    "D) student_age",
                ],
                "answer": "C",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "`type(3.14)`의 결과는 무엇인가요?",
                "choices": [
                    "A) <class 'int'>",
                    "B) <class 'float'>",
                    "C) <class 'str'>",
                    "D) <class 'number'>",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "`'Python' * 3`의 결과는?",
                "choices": [
                    "A) 에러 발생",
                    "B) 'Python 3'",
                    "C) 'PythonPythonPython'",
                    "D) 9",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "자신의 이름, 나이, 키(cm)를 각각 변수에 저장하고, "
                    "f-string을 사용하여 '저는 [이름]이고, [나이]살이며, "
                    "키는 [키]cm입니다.'를 출력하는 프로그램을 작성하세요."
                ),
                "hint": "name = '홍길동', age = 20, height = 175.5 처럼 변수를 선언하고 f'...' 안에 {변수명}을 넣으세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "사용자로부터 input()으로 두 숫자를 입력받아 "
                    "덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 출력하는 "
                    "간단한 계산기를 만들어보세요."
                ),
                "hint": "input()은 항상 문자열을 반환합니다. int() 또는 float()로 변환해야 산술 연산이 가능합니다.",
            },
        ],
        "challenge": {
            "question": (
                "BMI(체질량지수) 계산기를 만드세요. "
                "사용자로부터 키(cm)와 몸무게(kg)를 입력받아 "
                "BMI를 계산하고(BMI = 몸무게 / (키(m))^2), "
                "결과에 따라 '저체중/정상/과체중/비만' 중 하나를 출력하세요. "
                "(조건문은 아직 배우지 않았으므로, 계산 결과와 기준표만 함께 출력해도 됩니다.)"
            ),
            "hint": (
                "키를 cm에서 m로 변환하려면 100으로 나누세요. "
                "거듭제곱은 ** 연산자를 사용합니다. round()로 소수점을 정리할 수 있습니다."
            ),
        },
        "summary": [
            "변수는 데이터를 저장하는 이름표이며, `=` 기호로 값을 할당합니다.",
            "변수 이름은 소문자+밑줄(snake_case)을 사용하고, 숫자로 시작하거나 예약어를 쓸 수 없습니다.",
            "Python의 기본 자료형: int(정수), float(실수), str(문자열), bool(참/거짓), NoneType(없음).",
            "정수(int)는 크기 제한이 없고, 실수(float)는 부동소수점 방식으로 근사값을 저장합니다.",
            "문자열은 작은따옴표나 큰따옴표로 감싸며, `+`로 연결, `*`로 반복할 수 있습니다.",
            "f-string(`f'...'`)을 사용하면 문자열 안에 변수를 직접 삽입할 수 있습니다.",
            "bool은 True/False 두 값만 가지며, 조건 판단의 기초입니다.",
            "None은 '값이 없음'을 명시적으로 나타내는 특별한 값입니다.",
            "`type()` 함수로 자료형을 확인하고, `int()`, `float()`, `str()` 등으로 형변환할 수 있습니다.",
        ],
    }


# ─────────────────────────────────────────────
# 섹션 헬퍼 함수
# ─────────────────────────────────────────────


def _section_what_is_variable():
    """변수란 무엇인가 섹션."""
    return {
        "title": "변수란 무엇인가",
        "content": [
            (
                "프로그래밍에서 **변수(Variable)**란 데이터를 저장하는 공간에 붙인 이름입니다. "
                "변수를 사용하면 데이터를 기억하고, 나중에 다시 사용할 수 있습니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "변수는 '이름표가 붙은 상자'와 같습니다. "
                    "'과일 상자'라는 이름표가 붙은 상자에 사과를 넣으면, "
                    "나중에 '과일 상자'라고 말하는 것만으로 사과를 꺼낼 수 있습니다. "
                    "상자에 새 과일(배)을 넣으면, 같은 이름으로 배를 꺼낼 수 있습니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 변수에 값 할당하기\n"
                    'name = "홍길동"       # 문자열을 name 변수에 저장\n'
                    "age = 20              # 정수를 age 변수에 저장\n"
                    "height = 175.5        # 실수를 height 변수에 저장\n"
                    "is_student = True     # 불리언을 is_student 변수에 저장\n\n"
                    "# 변수에 저장된 값 사용하기\n"
                    "print(name)           # 출력: 홍길동\n"
                    "print(age)            # 출력: 20\n"
                    "print(height)         # 출력: 175.5"
                ),
            },
            {"type": "heading", "text": "변수의 동작 원리: 메모리 주소"},
            (
                "컴퓨터 내부에서 변수는 실제로 **메모리(RAM)의 특정 위치**를 가리킵니다. "
                "`name = '홍길동'`이라고 쓰면, Python은 메모리 어딘가에 '홍길동'을 저장하고, "
                "`name`이라는 이름표를 그 위치에 붙입니다."
            ),
            {
                "type": "diagram",
                "text": (
                    "  변수 이름          메모리\n"
                    "  ─────────     ─────────────────\n"
                    '  name    ────> │ "홍길동"       │  주소: 0x7f3a...\n'
                    "  ─────────     ─────────────────\n"
                    "  age     ────> │ 20             │  주소: 0x7f3b...\n"
                    "  ─────────     ─────────────────\n"
                    "  height  ────> │ 175.5          │  주소: 0x7f3c...\n"
                    "  ─────────     ─────────────────"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# id() 함수로 메모리 주소를 확인할 수 있습니다\n"
                    "x = 42\n"
                    "print(id(x))   # 예: 4375145680 (실행할 때마다 다를 수 있음)\n\n"
                    "# 변수의 값을 바꾸면 새로운 메모리 주소를 가리킵니다\n"
                    "x = 100\n"
                    "print(id(x))   # 다른 주소가 출력됩니다"
                ),
            },
            {"type": "heading", "text": "변수 이름 규칙"},
            {
                "type": "table",
                "headers": ["규칙", "올바른 예", "잘못된 예"],
                "rows": [
                    ["영문자, 숫자, 밑줄(_) 사용 가능", "user_name, count1", "user-name, count!"],
                    ["숫자로 시작할 수 없음", "name2, _temp", "2name, 1st_item"],
                    ["대소문자를 구분함", "Name과 name은 다른 변수", "—"],
                    ["예약어 사용 불가", "my_class, is_true", "class, True, for"],
                    ["관례: snake_case 사용", "user_age, total_count", "userAge, TotalCount"],
                ],
            },
            {"type": "heading", "text": "Python 예약어 목록"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# Python의 예약어(키워드) 확인하기\n"
                    "import keyword\n"
                    "print(keyword.kwlist)\n\n"
                    "# 주요 예약어:\n"
                    "# False, True, None, and, or, not, if, else, elif,\n"
                    "# for, while, break, continue, def, return, class,\n"
                    "# import, from, try, except, finally, with, as, ..."
                ),
            },
            {
                "type": "warning",
                "text": (
                    "Python에서 변수는 '값을 담는 상자'보다는 '값에 붙이는 이름표'에 가깝습니다. "
                    "`x = 10`은 10이라는 값 객체에 x라는 이름을 붙이는 것입니다. "
                    "이 개념은 나중에 '가변 객체'와 '불변 객체'를 배울 때 중요해집니다."
                ),
            },
        ],
    }


def _section_numbers():
    """숫자형: int, float 섹션."""
    return {
        "title": "숫자형: int, float",
        "content": [
            (
                "Python에서 숫자는 크게 **정수(int)**와 **실수(float)** 두 가지로 나뉩니다. "
                "프로그래밍에서 가장 자주 사용하는 자료형이므로 정확히 이해해야 합니다."
            ),
            {"type": "heading", "text": "정수(int) - 소수점이 없는 수"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 정수 예시\n"
                    "positive = 42           # 양의 정수\n"
                    "negative = -17          # 음의 정수\n"
                    "zero = 0                # 영\n"
                    "big_number = 1_000_000  # 밑줄로 자릿수 구분 (가독성 향상)\n\n"
                    "print(type(positive))   # <class 'int'>\n"
                    "print(big_number)       # 1000000 (밑줄은 출력되지 않음)"
                ),
            },
            {
                "type": "note",
                "text": (
                    "Python의 int는 크기 제한이 없습니다. "
                    "C나 Java에서는 정수가 너무 크면 '오버플로우'가 발생하지만, "
                    "Python은 메모리가 허용하는 한 아무리 큰 수도 다룰 수 있습니다."
                ),
            },
            {"type": "heading", "text": "실수(float) - 소수점이 있는 수"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 실수 예시\n"
                    "pi = 3.14159           # 원주율\n"
                    "temperature = -5.3     # 영하 온도\n"
                    "tiny = 0.001           # 작은 소수\n"
                    "scientific = 2.5e6     # 과학적 표기법: 2,500,000.0\n\n"
                    "print(type(pi))        # <class 'float'>\n"
                    "print(scientific)      # 2500000.0"
                ),
            },
            {
                "type": "warning",
                "text": (
                    "실수(float)는 부동소수점 방식으로 저장되므로 미세한 오차가 발생할 수 있습니다. "
                    "예: `0.1 + 0.2`의 결과는 `0.30000000000000004`입니다. "
                    "이는 Python뿐 아니라 거의 모든 프로그래밍 언어에서 발생하는 현상입니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 부동소수점 오차 확인\n"
                    "print(0.1 + 0.2)           # 0.30000000000000004\n"
                    "print(0.1 + 0.2 == 0.3)    # False (주의!)\n\n"
                    "# 정확한 비교가 필요하면 round() 사용\n"
                    "print(round(0.1 + 0.2, 1))        # 0.3\n"
                    "print(round(0.1 + 0.2, 1) == 0.3) # True"
                ),
            },
            {"type": "heading", "text": "산술 연산자"},
            {
                "type": "table",
                "headers": ["연산자", "의미", "예시", "결과"],
                "rows": [
                    ["+", "덧셈", "7 + 3", "10"],
                    ["-", "뺄셈", "7 - 3", "4"],
                    ["*", "곱셈", "7 * 3", "21"],
                    ["/", "나눗셈 (실수)", "7 / 3", "2.3333..."],
                    ["//", "나눗셈 (정수, 몫)", "7 // 3", "2"],
                    ["%", "나머지", "7 % 3", "1"],
                    ["**", "거듭제곱", "2 ** 10", "1024"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 산술 연산 실습\n"
                    "a = 17\n"
                    "b = 5\n\n"
                    "print(f'{a} + {b} = {a + b}')    # 17 + 5 = 22\n"
                    "print(f'{a} - {b} = {a - b}')    # 17 - 5 = 12\n"
                    "print(f'{a} * {b} = {a * b}')    # 17 * 5 = 85\n"
                    "print(f'{a} / {b} = {a / b}')    # 17 / 5 = 3.4\n"
                    "print(f'{a} // {b} = {a // b}')  # 17 // 5 = 3 (몫)\n"
                    "print(f'{a} % {b} = {a % b}')    # 17 % 5 = 2 (나머지)\n"
                    "print(f'{a} ** {b} = {a ** b}')   # 17 ** 5 = 1419857"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "나눗셈 `/`의 결과는 항상 float입니다. "
                    "정수 결과가 필요하면 `//`를 사용하세요. "
                    "예: `10 / 2`는 `5.0`(float), `10 // 2`는 `5`(int)."
                ),
            },
        ],
    }


def _section_strings():
    """문자열: str 섹션."""
    return {
        "title": "문자열: str",
        "content": [
            (
                "**문자열(string, str)**은 텍스트 데이터를 나타내는 자료형입니다. "
                "프로그래밍에서 이름, 주소, 메시지 등 텍스트를 다룰 때 사용합니다. "
                "Python에서 문자열은 작은따옴표(`'...'`) 또는 큰따옴표(`\"...\"`)"
                "로 감싸서 만듭니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 문자열 생성하기\n"
                    "name = '홍길동'              # 작은따옴표\n"
                    'greeting = "안녕하세요!"      # 큰따옴표\n'
                    "empty = ''                    # 빈 문자열\n\n"
                    "# 따옴표 안에 따옴표 넣기\n"
                    "quote1 = \"그가 '안녕'이라고 말했다\"     # 큰따옴표 안에 작은따옴표\n"
                    "quote2 = '그가 \"안녕\"이라고 말했다'     # 작은따옴표 안에 큰따옴표\n\n"
                    "print(type(name))   # <class 'str'>"
                ),
            },
            {"type": "heading", "text": "이스케이프 문자"},
            (
                "문자열 안에서 특수한 동작을 하는 문자를 **이스케이프 문자**라고 합니다. "
                "백슬래시(`\\`)와 함께 사용합니다."
            ),
            {
                "type": "table",
                "headers": ["이스케이프", "의미", "예시 출력"],
                "rows": [
                    ["\\n", "줄바꿈 (새 줄)", "첫째 줄(줄바꿈)둘째 줄"],
                    ["\\t", "탭 (들여쓰기)", "이름(탭)나이"],
                    ["\\'", "작은따옴표", "It's"],
                    ['\\\"', "큰따옴표", 'He said "Hi"'],
                    ["\\\\", "백슬래시 자체", "C:\\Users\\..."],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 이스케이프 문자 사용 예시\n"
                    'print("첫째 줄\\n둘째 줄")\n'
                    "# 출력:\n"
                    "# 첫째 줄\n"
                    "# 둘째 줄\n\n"
                    'print("이름\\t나이\\t도시")\n'
                    'print("홍길동\\t20\\t서울")\n'
                    "# 출력:\n"
                    "# 이름    나이    도시\n"
                    "# 홍길동  20      서울"
                ),
            },
            {"type": "heading", "text": "문자열 연산"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 문자열 연결 (+)\n"
                    "first = '홍'\n"
                    "last = '길동'\n"
                    "full_name = first + last\n"
                    "print(full_name)        # 홍길동\n\n"
                    "# 문자열 반복 (*)\n"
                    "line = '-' * 30\n"
                    "print(line)             # ------------------------------\n\n"
                    "# 문자열 길이 (len)\n"
                    "message = '안녕하세요'\n"
                    "print(len(message))     # 5"
                ),
            },
            {"type": "heading", "text": "f-string (문자열 포매팅)"},
            (
                "Python 3.6부터 도입된 **f-string**은 문자열 안에 변수를 "
                "직접 삽입하는 가장 편리한 방법입니다. 문자열 앞에 `f`를 붙이고, "
                "중괄호 `{}`안에 변수명이나 표현식을 넣습니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# f-string 기본 사용법\n"
                    "name = '김파이'\n"
                    "age = 22\n"
                    "gpa = 3.87\n\n"
                    "# 변수 삽입\n"
                    "print(f'이름: {name}, 나이: {age}세')\n"
                    "# 출력: 이름: 김파이, 나이: 22세\n\n"
                    "# 표현식 삽입 (계산도 가능)\n"
                    "print(f'{name}님은 내년에 {age + 1}세입니다')\n"
                    "# 출력: 김파이님은 내년에 23세입니다\n\n"
                    "# 소수점 자릿수 지정\n"
                    "print(f'학점: {gpa:.1f}')\n"
                    "# 출력: 학점: 3.9"
                ),
            },
            {
                "type": "note",
                "text": (
                    "f-string 이전에는 `%` 연산자나 `.format()` 메서드를 사용했습니다. "
                    "기존 코드에서 이 방식을 볼 수 있지만, "
                    "새 코드를 작성할 때는 f-string을 권장합니다."
                ),
            },
            {"type": "heading", "text": "여러 줄 문자열"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    '# 삼중 따옴표로 여러 줄 문자열 작성\n'
                    'poem = """\n'
                    "산에는 꽃이 피네\n"
                    "꽃이 피네\n"
                    "갈 봄 여름 없이\n"
                    "꽃이 피네\n"
                    '"""\n'
                    "print(poem)"
                ),
            },
        ],
    }


def _section_booleans():
    """불리언: bool 섹션."""
    return {
        "title": "불리언: bool",
        "content": [
            (
                "**불리언(bool)**은 **참(True)** 또는 **거짓(False)** "
                "두 가지 값만 가지는 자료형입니다. "
                "이름은 논리학을 창시한 수학자 조지 불(George Boole)에서 유래합니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "불리언은 '전등 스위치'와 같습니다. "
                    "켜짐(True) 또는 꺼짐(False), 두 상태만 존재합니다. "
                    "'약간 켜짐' 같은 중간 상태는 없습니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 불리언 변수\n"
                    "is_student = True\n"
                    "has_license = False\n\n"
                    "print(type(is_student))   # <class 'bool'>\n"
                    "print(is_student)         # True"
                ),
            },
            {"type": "heading", "text": "비교 연산자"},
            (
                "비교 연산자는 두 값을 비교하여 불리언(True/False)을 반환합니다. "
                "나중에 배울 `if` 조건문의 핵심 재료입니다."
            ),
            {
                "type": "table",
                "headers": ["연산자", "의미", "예시", "결과"],
                "rows": [
                    ["==", "같다", "5 == 5", "True"],
                    ["!=", "같지 않다", "5 != 3", "True"],
                    [">", "크다", "5 > 3", "True"],
                    ["<", "작다", "5 < 3", "False"],
                    [">=", "크거나 같다", "5 >= 5", "True"],
                    ["<=", "작거나 같다", "3 <= 5", "True"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 비교 연산 실습\n"
                    "age = 20\n\n"
                    "print(age > 18)      # True  (20은 18보다 크다)\n"
                    "print(age == 20)     # True  (20은 20과 같다)\n"
                    "print(age < 15)      # False (20은 15보다 작지 않다)\n"
                    "print(age != 20)     # False (20은 20과 같으므로 '같지 않다'는 거짓)\n\n"
                    '# 문자열도 비교 가능\n'
                    'print("apple" == "apple")    # True\n'
                    'print("apple" == "Apple")    # False (대소문자 구분!)'
                ),
            },
            {
                "type": "warning",
                "text": (
                    "`=`와 `==`를 혼동하지 마세요! "
                    "`=`는 '값을 할당'하는 연산자이고, `==`는 '같은지 비교'하는 연산자입니다. "
                    "`x = 5`는 x에 5를 저장, `x == 5`는 x가 5인지 확인합니다."
                ),
            },
            {"type": "heading", "text": "논리 연산자"},
            {
                "type": "table",
                "headers": ["연산자", "의미", "예시", "결과"],
                "rows": [
                    ["and", "둘 다 참이면 True", "True and True", "True"],
                    ["or", "하나라도 참이면 True", "False or True", "True"],
                    ["not", "반대로 뒤집기", "not True", "False"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 논리 연산 실습\n"
                    "age = 20\n"
                    "has_id = True\n\n"
                    "# and: 둘 다 충족해야 True\n"
                    "can_enter = (age >= 18) and has_id\n"
                    "print(f'입장 가능: {can_enter}')     # True\n\n"
                    "# or: 하나만 충족해도 True\n"
                    "is_vip = False\n"
                    "is_member = True\n"
                    "gets_discount = is_vip or is_member\n"
                    "print(f'할인 적용: {gets_discount}')  # True\n\n"
                    "# not: 반전\n"
                    "is_closed = False\n"
                    "is_open = not is_closed\n"
                    "print(f'영업 중: {is_open}')          # True"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "Python에서는 `0`, `0.0`, `''`(빈 문자열), `[]`(빈 리스트), `None`이 "
                    "모두 `False`로 평가됩니다. 이를 'falsy 값'이라고 합니다. "
                    "그 외의 값은 모두 'truthy'입니다."
                ),
            },
        ],
    }


def _section_none():
    """None 타입 섹션."""
    return {
        "title": "None 타입",
        "content": [
            (
                "**None**은 '값이 없음'을 나타내는 Python의 특별한 값입니다. "
                "다른 언어에서는 `null`, `nil` 등으로 불리며, "
                "Python에서는 `NoneType`이라는 고유한 타입을 가집니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "None은 '빈 접시'와 같습니다. "
                    "접시에 음식이 없다(None)는 것은 접시 자체가 없는 것(존재하지 않음)과 다릅니다. "
                    "'0'은 숫자 0이라는 값이 있는 것이고, '빈 문자열'은 길이가 0인 문자열이 있는 것이지만, "
                    "None은 정말로 '아무 값도 없음'을 의미합니다."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# None 사용 예시\n"
                    "result = None          # 아직 결과가 정해지지 않음\n"
                    "print(result)          # None\n"
                    "print(type(result))    # <class 'NoneType'>"
                ),
            },
            {"type": "heading", "text": "None은 언제 사용하나요?"},
            {
                "type": "table",
                "headers": ["상황", "설명", "예시"],
                "rows": [
                    [
                        "초기값 미정",
                        "값을 나중에 할당할 변수의 자리 표시",
                        "user_input = None",
                    ],
                    [
                        "함수 반환값 없음",
                        "함수가 명시적 반환값 없이 끝남",
                        "print()의 반환값",
                    ],
                    [
                        "선택적 데이터",
                        "값이 있을 수도, 없을 수도 있는 경우",
                        "middle_name = None",
                    ],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# None 비교는 is 연산자를 사용합니다\n"
                    "value = None\n\n"
                    "# 올바른 비교 방법 (is 사용)\n"
                    "if value is None:\n"
                    "    print('값이 없습니다')\n\n"
                    "# 잘못된 비교 방법 (== 사용) - 동작은 하지만 권장하지 않음\n"
                    "if value == None:\n"
                    "    print('이 방법은 권장하지 않습니다')"
                ),
            },
            {"type": "heading", "text": "None과 다른 'falsy' 값의 차이"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# None, 0, 빈 문자열은 모두 다른 값입니다\n"
                    "print(None == 0)       # False\n"
                    "print(None == '')      # False\n"
                    "print(None == False)   # False\n\n"
                    "# 하지만 모두 bool()로 변환하면 False입니다\n"
                    "print(bool(None))      # False\n"
                    "print(bool(0))         # False\n"
                    "print(bool(''))        # False"
                ),
            },
            {
                "type": "note",
                "text": (
                    "None을 `==`로 비교하지 말고, `is`로 비교하세요. "
                    "`value is None`이 Python의 공식 권장 방식(PEP 8)입니다. "
                    "`is`는 두 값이 동일한 객체인지 확인하는 연산자입니다."
                ),
            },
        ],
    }


def _section_type_conversion():
    """형변환과 타입 확인 섹션."""
    return {
        "title": "형변환과 타입 확인",
        "content": [
            (
                "프로그래밍을 하다 보면 자료형을 바꿔야 하는 상황이 자주 발생합니다. "
                "예를 들어 사용자가 입력한 '숫자 문자열'을 실제 숫자로 바꾸거나, "
                "숫자를 문자열에 포함시키는 경우입니다. "
                "이를 **형변환(Type Conversion)**이라고 합니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "형변환은 '단위 변환'과 비슷합니다. "
                    "같은 길이를 cm로 표현할 수도 있고, m로 표현할 수도 있듯이, "
                    "같은 데이터를 정수로, 실수로, 문자열로 표현할 수 있습니다. "
                    "단, 의미가 맞아야 변환이 가능합니다 (문자 'abc'를 숫자로 변환할 수는 없습니다)."
                ),
            },
            {"type": "heading", "text": "type() - 자료형 확인"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# type()으로 자료형 확인하기\n"
                    "print(type(42))          # <class 'int'>\n"
                    "print(type(3.14))        # <class 'float'>\n"
                    "print(type('안녕'))      # <class 'str'>\n"
                    "print(type(True))        # <class 'bool'>\n"
                    "print(type(None))        # <class 'NoneType'>"
                ),
            },
            {"type": "heading", "text": "주요 형변환 함수"},
            {
                "type": "table",
                "headers": ["함수", "용도", "예시", "결과"],
                "rows": [
                    ["int()", "정수로 변환", "int('42')", "42"],
                    ["float()", "실수로 변환", "float('3.14')", "3.14"],
                    ["str()", "문자열로 변환", "str(100)", "'100'"],
                    ["bool()", "불리언으로 변환", "bool(1)", "True"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# --- 문자열 -> 숫자 변환 ---\n"
                    "age_str = '25'              # 문자열 '25'\n"
                    "age_num = int(age_str)       # 정수 25로 변환\n"
                    "print(age_num + 1)           # 26 (산술 연산 가능)\n\n"
                    "price_str = '19900.5'\n"
                    "price_num = float(price_str) # 실수 19900.5로 변환\n"
                    "print(price_num * 2)         # 39801.0\n\n"
                    "# --- 숫자 -> 문자열 변환 ---\n"
                    "score = 95\n"
                    "message = '점수: ' + str(score) + '점'\n"
                    "print(message)               # 점수: 95점\n\n"
                    "# --- 실수 -> 정수 변환 (소수점 이하 버림) ---\n"
                    "temperature = 36.7\n"
                    "print(int(temperature))      # 36 (반올림이 아닌 버림!)"
                ),
            },
            {
                "type": "warning",
                "text": (
                    "변환할 수 없는 값을 변환하려 하면 에러가 발생합니다. "
                    "예: `int('abc')`는 ValueError를 발생시킵니다. "
                    "사용자 입력을 변환할 때는 항상 유효한 값인지 확인하세요."
                ),
            },
            {"type": "heading", "text": "isinstance() - 타입 확인"},
            (
                "`isinstance()` 함수는 값이 특정 자료형인지 True/False로 확인합니다. "
                "`type()` 보다 유연한 확인 방법입니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# isinstance()로 타입 확인\n"
                    "age = 20\n"
                    "name = '홍길동'\n\n"
                    "print(isinstance(age, int))       # True\n"
                    "print(isinstance(name, str))      # True\n"
                    "print(isinstance(age, float))     # False\n\n"
                    "# 여러 타입 중 하나인지 확인\n"
                    "value = 3.14\n"
                    "print(isinstance(value, (int, float)))  # True (int 또는 float)"
                ),
            },
            {"type": "heading", "text": "input()과 형변환"},
            (
                "`input()` 함수로 사용자 입력을 받으면 항상 **문자열(str)**로 반환됩니다. "
                "숫자로 사용하려면 반드시 형변환이 필요합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# input()은 항상 문자열을 반환합니다\n"
                    'user_input = input("숫자를 입력하세요: ")  # 사용자가 42 입력\n'
                    "print(type(user_input))   # <class 'str'> (문자열!)\n"
                    "print(user_input + 10)    # TypeError 발생!\n\n"
                    "# 올바른 방법: 형변환 후 사용\n"
                    'user_input = input("숫자를 입력하세요: ")\n'
                    "number = int(user_input)  # 문자열 -> 정수 변환\n"
                    "print(number + 10)        # 52 (정상 동작)"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "input()과 int()를 한 줄로 합칠 수 있습니다: "
                    '`age = int(input("나이: "))`. '
                    "이 패턴은 Python에서 매우 자주 사용됩니다."
                ),
            },
            {"type": "heading", "text": "자료형 변환 요약 다이어그램"},
            {
                "type": "flow_diagram",
                "nodes": [
                    {"label": "int (정수)", "color": "#3182F6"},
                    {"label": "str (문자열)", "color": "#A234C7"},
                    {"label": "float (실수)", "color": "#03B26C"},
                ],
                "arrow_labels": ["str()", "float()"],
                "title": "자료형 변환 경로",
                "note": "역방향: int(), float(), str() 사용 | bool()은 모든 타입에서 True/False로 변환 가능",
            },
        ],
    }
