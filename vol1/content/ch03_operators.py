"""챕터 3: 연산자 — 데이터를 다루는 도구."""


def get_chapter():
    """챕터 3 콘텐츠를 반환한다."""
    return {
        "number": 3,
        "title": "연산자",
        "subtitle": "데이터를 다루는 도구",
        "big_picture": (
            "프로그래밍에서 연산자는 데이터를 가공하는 핵심 도구입니다. "
            "덧셈·뺄셈 같은 기본 계산부터 크기 비교, 논리 판단까지 "
            "모든 프로그램은 연산자 위에서 동작합니다. "
            "이 장에서는 Python이 제공하는 다양한 연산자를 익히고, "
            "실전에서 올바르게 조합하는 방법을 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: 산술 연산자 ──────────────────────────
            {
                "title": "산술 연산자",
                "content": [
                    "산술 연산자는 숫자를 계산할 때 사용합니다. "
                    "수학 시간에 배운 사칙연산을 Python에서 그대로 쓸 수 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "산술 연산자는 계산기의 버튼과 같습니다. "
                            "계산기에서 +, -, ×, ÷ 버튼을 누르듯 "
                            "Python에서도 +, -, *, / 기호로 계산합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["연산자", "이름", "예시", "결과"],
                        "rows": [
                            ["+", "덧셈", "7 + 3", "10"],
                            ["-", "뺄셈", "7 - 3", "4"],
                            ["*", "곱셈", "7 * 3", "21"],
                            ["/", "나눗셈", "7 / 3", "2.3333..."],
                            ["//", "몫(정수 나눗셈)", "7 // 3", "2"],
                            ["%", "나머지", "7 % 3", "1"],
                            ["**", "거듭제곱", "2 ** 10", "1024"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 산술 연산\n"
                            "a = 15\n"
                            "b = 4\n\n"
                            "print(a + b)   # 19  — 덧셈\n"
                            "print(a - b)   # 11  — 뺄셈\n"
                            "print(a * b)   # 60  — 곱셈\n"
                            "print(a / b)   # 3.75 — 나눗셈 (항상 float)\n"
                            "print(a // b)  # 3   — 몫\n"
                            "print(a % b)   # 3   — 나머지\n"
                            "print(b ** 3)  # 64  — 4의 세제곱"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "나눗셈의 두 얼굴: / 와 //",
                    },
                    (
                        "Python에서 `/`는 **항상** 실수(float)를 반환합니다. "
                        "정수 결과가 필요하면 `//`를 사용하세요."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# / 는 항상 float 반환\n"
                            "print(10 / 2)   # 5.0  (정수가 아니라 실수!)\n"
                            "print(10 // 2)  # 5    (정수 몫)\n\n"
                            "# 음수 몫은 '내림' 방향\n"
                            "print(-7 // 2)  # -4  (수학적 내림: -3.5 → -4)"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "0으로 나누면 `ZeroDivisionError`가 발생합니다. "
                            "사용자 입력을 나눗셈에 쓸 때는 반드시 0 여부를 검사하세요."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 0으로 나누기 — 에러 발생\n"
                            "# print(10 / 0)  # ZeroDivisionError!\n\n"
                            "# 안전한 나눗셈 패턴\n"
                            "divisor = int(input('나눌 수를 입력하세요: '))\n"
                            "if divisor != 0:\n"
                            "    print(100 / divisor)\n"
                            "else:\n"
                            "    print('0으로 나눌 수 없습니다.')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "`%` 연산자로 짝수·홀수를 판별할 수 있습니다. "
                            "`num % 2 == 0`이면 짝수, 아니면 홀수입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 비교 연산자 ──────────────────────────
            {
                "title": "비교 연산자",
                "content": [
                    "비교 연산자는 두 값을 비교하여 **True** 또는 **False**를 반환합니다. "
                    "조건문(if)과 반복문(while)의 핵심 재료입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "비교 연산자는 저울과 같습니다. "
                            "저울 양쪽에 값을 올려놓고 어느 쪽이 무거운지, "
                            "같은지를 판단하는 것이죠."
                        ),
                    },
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
                            "# 비교 연산자 기본 사용\n"
                            "score = 85\n\n"
                            "print(score == 100)  # False — 같은가?\n"
                            "print(score != 0)    # True  — 다른가?\n"
                            "print(score >= 60)   # True  — 합격?\n"
                            "print(score < 90)    # True  — A 미만?"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "연쇄 비교 (Chained Comparison)",
                    },
                    "Python은 수학처럼 비교를 연결할 수 있습니다. "
                    "다른 언어에서는 지원하지 않는 Python만의 장점입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 연쇄 비교 — 범위 검사에 유용\n"
                            "age = 25\n\n"
                            "# 일반적인 방법\n"
                            "print(18 <= age and age < 65)  # True\n\n"
                            "# Python 연쇄 비교 (더 읽기 좋음)\n"
                            "print(18 <= age < 65)          # True\n\n"
                            "# 여러 값 동시 비교도 가능\n"
                            "x = 5\n"
                            "print(1 < x < 10)    # True — x가 1~10 사이인가?\n"
                            "print(1 < x < 3)     # False"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "`=`는 대입 연산자이고, `==`가 비교 연산자입니다. "
                            "초보자가 가장 자주 실수하는 부분이니 꼭 구별하세요!"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "실수(float) 비교 시 부동소수점 오차에 주의하세요. "
                            "`0.1 + 0.2 == 0.3`은 **False**입니다. "
                            "실수 비교는 `abs(a - b) < 1e-9` 패턴을 사용합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 부동소수점 비교 주의\n"
                            "print(0.1 + 0.2 == 0.3)  # False!\n"
                            "print(0.1 + 0.2)         # 0.30000000000000004\n\n"
                            "# 안전한 실수 비교\n"
                            "result = 0.1 + 0.2\n"
                            "print(abs(result - 0.3) < 1e-9)  # True"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 논리 연산자 ──────────────────────────
            {
                "title": "논리 연산자",
                "content": [
                    "논리 연산자는 여러 조건을 **조합**할 때 사용합니다. "
                    "`and`, `or`, `not` 세 가지가 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "논리 연산자는 면접관의 판단 기준과 같습니다. "
                            "'성적이 좋고(and) 면접도 통과' — 둘 다 만족해야 합격. "
                            "'추천서가 있거나(or) 경력이 있다' — 하나만 있으면 통과. "
                            "'결격 사유가 없다(not)' — 조건을 뒤집습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["연산자", "의미", "True가 되려면"],
                        "rows": [
                            ["and", "그리고", "양쪽 모두 True"],
                            ["or", "또는", "하나 이상 True"],
                            ["not", "부정", "피연산자가 False"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "진리표 (Truth Table)",
                    },
                    {
                        "type": "table",
                        "headers": ["A", "B", "A and B", "A or B", "not A"],
                        "rows": [
                            ["True", "True", "True", "True", "False"],
                            ["True", "False", "False", "True", "False"],
                            ["False", "True", "False", "True", "True"],
                            ["False", "False", "False", "False", "True"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 논리 연산자 실전 예시\n"
                            "age = 20\n"
                            "has_id = True\n"
                            "is_vip = False\n\n"
                            "# and — 둘 다 만족해야 입장\n"
                            "can_enter = age >= 19 and has_id\n"
                            "print(can_enter)  # True\n\n"
                            "# or — 하나만 만족하면 할인\n"
                            "gets_discount = age < 18 or is_vip\n"
                            "print(gets_discount)  # False\n\n"
                            "# not — 조건 반전\n"
                            "is_minor = not (age >= 19)\n"
                            "print(is_minor)  # False"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "단축 평가 (Short-Circuit Evaluation)",
                    },
                    (
                        "Python은 결과가 확정되면 나머지 조건을 평가하지 않습니다. "
                        "이를 **단축 평가**라 하며, 에러를 미리 방지하는 패턴에 활용합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 단축 평가 활용\n"
                            "# and: 앞이 False면 뒤는 실행 안 함\n"
                            "x = 0\n"
                            "result = x != 0 and 10 / x  # 0이면 나눗셈 실행 안 함\n"
                            "print(result)  # False (에러 없음!)\n\n"
                            "# or: 앞이 True면 뒤는 실행 안 함\n"
                            "name = '' or '이름 없음'\n"
                            "print(name)  # '이름 없음' (빈 문자열은 False)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python에서 `0`, `''`, `[]`, `None`은 "
                            "논리적으로 **False**로 취급됩니다 (Falsy 값). "
                            "이 특성을 활용하면 코드를 간결하게 작성할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 할당 연산자 ──────────────────────────
            {
                "title": "할당 연산자",
                "content": [
                    "할당 연산자는 변수에 값을 저장하는 연산자입니다. "
                    "기본 `=` 외에도 산술과 결합한 **복합 할당 연산자**가 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "복합 할당 연산자는 '약어'와 같습니다. "
                            "'score = score + 10'을 'score += 10'으로 "
                            "줄여 쓰는 것이죠. 뜻은 같지만 더 간결합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["연산자", "예시", "동일한 표현"],
                        "rows": [
                            ["=", "x = 5", "—"],
                            ["+=", "x += 3", "x = x + 3"],
                            ["-=", "x -= 2", "x = x - 2"],
                            ["*=", "x *= 4", "x = x * 4"],
                            ["/=", "x /= 2", "x = x / 2"],
                            ["//=", "x //= 3", "x = x // 3"],
                            ["%=", "x %= 7", "x = x % 7"],
                            ["**=", "x **= 2", "x = x ** 2"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 복합 할당 연산자 실전 예시\n"
                            "total = 0\n\n"
                            "# 물건 가격 누적\n"
                            "total += 15000  # 커피\n"
                            "total += 4500   # 빵\n"
                            "total += 2000   # 물\n"
                            "print(f'총합: {total}원')  # 총합: 21500원\n\n"
                            "# 할인 적용 (10%)\n"
                            "total *= 0.9\n"
                            "print(f'할인 후: {total:.0f}원')  # 할인 후: 19350원"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 카운터 패턴 — 프로그래밍에서 매우 자주 사용\n"
                            "count = 0\n"
                            "count += 1  # 1 증가\n"
                            "count += 1  # 또 1 증가\n"
                            "print(count)  # 2\n\n"
                            "# 참고: Python에는 ++ 연산자가 없습니다!\n"
                            "# count++  ← 이건 에러!\n"
                            "# count += 1 을 사용하세요."
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "복합 할당 연산자는 코드를 짧게 만들 뿐 아니라 "
                            "의도를 명확히 드러냅니다. '값을 누적한다'는 뜻이 "
                            "`+= `에 담겨 있죠."
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "Python은 C/Java와 달리 `++`, `--` 연산자가 "
                            "없습니다. 반드시 `+= 1`, `-= 1`을 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 비트 연산자 ──────────────────────────
            {
                "title": "비트 연산자",
                "content": [
                    "비트 연산자는 정수를 **이진수(비트)** 단위로 처리합니다. "
                    "초보 단계에서 자주 쓰지는 않지만, 시스템 프로그래밍이나 "
                    "최적화에서 중요한 역할을 합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "비트 연산은 전등 스위치 여러 개를 한꺼번에 "
                            "조작하는 것과 같습니다. 각 스위치(비트)가 "
                            "켜짐(1) 또는 꺼짐(0) 상태이고, "
                            "AND/OR/XOR로 한꺼번에 제어합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["연산자", "이름", "설명"],
                        "rows": [
                            ["&", "AND", "양쪽 비트 모두 1이면 1"],
                            ["|", "OR", "한쪽이라도 1이면 1"],
                            ["^", "XOR", "서로 다르면 1"],
                            ["~", "NOT", "비트 반전"],
                            ["<<", "왼쪽 시프트", "비트를 왼쪽으로 이동"],
                            [">>", "오른쪽 시프트", "비트를 오른쪽으로 이동"],
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["값", "비트 표현", "AND (&)", "OR (|)", "XOR (^)"],
                        "rows": [
                            ["5", "0 1 0 1", "", "", ""],
                            ["3", "0 0 1 1", "", "", ""],
                            ["결과", "", "0 0 0 1 (=1)", "0 1 1 1 (=7)", "0 1 1 0 (=6)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 비트 연산 기본\n"
                            "a = 5   # 이진수: 0101\n"
                            "b = 3   # 이진수: 0011\n\n"
                            "print(a & b)   # 1  (0001) — AND\n"
                            "print(a | b)   # 7  (0111) — OR\n"
                            "print(a ^ b)   # 6  (0110) — XOR\n"
                            "print(a << 1)  # 10 (1010) — 왼쪽 시프트\n"
                            "print(a >> 1)  # 2  (0010) — 오른쪽 시프트"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실무 예시: 권한 관리에서의 비트 연산",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 파일 권한 관리 (리눅스 스타일)\n"
                            "READ = 0b100    # 4 — 읽기 권한\n"
                            "WRITE = 0b010   # 2 — 쓰기 권한\n"
                            "EXECUTE = 0b001 # 1 — 실행 권한\n\n"
                            "# 권한 조합 (OR로 합치기)\n"
                            "my_permission = READ | WRITE  # 6 (읽기 + 쓰기)\n\n"
                            "# 권한 확인 (AND로 검사)\n"
                            "can_read = bool(my_permission & READ)    # True\n"
                            "can_execute = bool(my_permission & EXECUTE)  # False\n\n"
                            "print(f'읽기 가능: {can_read}')      # True\n"
                            "print(f'실행 가능: {can_execute}')    # False"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "비트 연산자는 당장 외우지 않아도 됩니다. "
                            "'이런 게 있다' 정도만 기억하고, 필요할 때 찾아보세요. "
                            "나중에 네트워크, 암호화, 시스템 프로그래밍에서 만나게 됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 연산자 우선순위 ──────────────────────
            {
                "title": "연산자 우선순위",
                "content": [
                    "여러 연산자가 한 줄에 섞여 있을 때, "
                    "Python은 정해진 **우선순위**에 따라 계산합니다. "
                    "수학에서 '곱셈을 먼저' 하는 것과 같은 원리입니다.",
                    {
                        "type": "table",
                        "headers": ["우선순위", "연산자", "설명"],
                        "rows": [
                            ["1 (높음)", "**", "거듭제곱"],
                            ["2", "+x, -x, ~x", "단항 연산자"],
                            ["3", "*, /, //, %", "곱셈류"],
                            ["4", "+, -", "덧셈류"],
                            ["5", "<<, >>", "시프트"],
                            ["6", "&", "비트 AND"],
                            ["7", "^", "비트 XOR"],
                            ["8", "|", "비트 OR"],
                            ["9", "==, !=, >, <, >=, <=", "비교"],
                            ["10", "not", "논리 NOT"],
                            ["11", "and", "논리 AND"],
                            ["12 (낮음)", "or", "논리 OR"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 우선순위에 따른 계산 순서\n"
                            "result = 2 + 3 * 4     # 14 (곱셈 먼저)\n"
                            "result = (2 + 3) * 4   # 20 (괄호 먼저)\n\n"
                            "# 거듭제곱은 곱셈보다 높음\n"
                            "result = 2 * 3 ** 2    # 18 (3**2=9, 2*9=18)\n"
                            "result = (2 * 3) ** 2  # 36 (6**2=36)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "헷갈리는 예시들",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 헷갈리기 쉬운 우선순위\n\n"
                            "# 1) not과 비교 연산자\n"
                            "print(not 3 > 5)      # True  → not (3 > 5) → not False\n"
                            "print(not True == False)  # True\n"
                            "# → (not True) == False? 아니면 not (True == False)?\n"
                            "# → not (True == False) → not False → True\n\n"
                            "# 2) and와 or의 우선순위\n"
                            "print(True or False and False)  # True\n"
                            "# → True or (False and False) → True or False → True\n"
                            "# and가 or보다 먼저 계산됩니다!"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "우선순위를 외우느라 시간 쓰지 마세요. "
                            "**괄호를 적극적으로 사용**하면 의도가 명확해지고 "
                            "실수도 줄어듭니다. `(a + b) * c`처럼 쓰세요."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실습: BMI 계산기",
                    },
                    "배운 연산자를 종합하여 BMI(체질량지수) 계산기를 만들어 봅시다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# BMI 계산기\n"
                            "# BMI = 체중(kg) / 키(m)의 제곱\n\n"
                            "weight = float(input('체중(kg)을 입력하세요: '))\n"
                            "height_cm = float(input('키(cm)를 입력하세요: '))\n\n"
                            "# cm를 m로 변환\n"
                            "height_m = height_cm / 100\n\n"
                            "# BMI 계산 (** 연산자 사용)\n"
                            "bmi = weight / (height_m ** 2)\n\n"
                            "# 결과 출력 (소수점 1자리)\n"
                            "print(f'BMI: {bmi:.1f}')\n\n"
                            "# 판정 (비교 + 논리 연산자 사용)\n"
                            "if bmi < 18.5:\n"
                            "    print('판정: 저체중')\n"
                            "elif 18.5 <= bmi < 23.0:\n"
                            "    print('판정: 정상')\n"
                            "elif 23.0 <= bmi < 25.0:\n"
                            "    print('판정: 과체중')\n"
                            "else:\n"
                            "    print('판정: 비만')"
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "입력: 체중, 키"},
                            {"label": "cm → m 변환", "sub": "/ 100"},
                            {"label": "BMI 계산", "sub": "/ **"},
                            {"label": "판정", "sub": "비교 + 논리 연산자"},
                        ],
                    },
                ],
            },
        ],
        "practical_tips": [
            "나눗셈 전에 항상 0 여부를 확인하세요.",
            "실수(float) 비교는 `==` 대신 `abs(a - b) < 오차` 패턴을 사용하세요.",
            "복잡한 수식에는 괄호를 적극 사용하여 우선순위를 명확히 하세요.",
            "단축 평가를 활용하면 불필요한 계산과 에러를 방지할 수 있습니다.",
            "`%` 연산자는 짝홀수 판별, 순환 인덱스 등 다양하게 활용됩니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 `7 // 2`의 결과는?",
                "choices": ["A) 3.5", "B) 3", "C) 4", "D) 3.0"],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "`True or False and False`의 결과는?",
                "choices": ["A) True", "B) False", "C) 에러", "D) None"],
                "answer": "A",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "`not 3 > 5`의 결과는?",
                "choices": ["A) True", "B) False", "C) 3", "D) 에러"],
                "answer": "A",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "사용자로부터 초(seconds)를 입력받아 "
                    "'X시간 Y분 Z초'로 변환하여 출력하는 프로그램을 작성하세요. "
                    "(// 와 % 연산자를 사용하세요)"
                ),
                "hint": "시간 = seconds // 3600, 남은 초에서 분 = 나머지 // 60",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "세 과목 점수를 입력받아 평균을 계산하고, "
                    "평균이 60점 이상이면서 모든 과목이 40점 이상이면 '합격', "
                    "아니면 '불합격'을 출력하는 프로그램을 작성하세요."
                ),
                "hint": "and 연산자로 여러 조건을 결합하세요.",
            },
        ],
        "challenge": {
            "question": (
                "사용자로부터 연도를 입력받아 윤년인지 판별하는 프로그램을 작성하세요. "
                "윤년 조건: (4의 배수이면서 100의 배수가 아니거나) 또는 (400의 배수). "
                "% 연산자와 논리 연산자를 활용하세요."
            ),
            "hint": (
                "year % 4 == 0 and year % 100 != 0 or year % 400 == 0 "
                "— 여기서 괄호를 어디에 넣어야 할지 생각해 보세요."
            ),
        },
        "summary": [
            "산술 연산자: +, -, *, /, //(몫), %(나머지), **(거듭제곱)",
            "`/`는 항상 float를 반환하고, `//`는 정수 몫을 반환한다.",
            "비교 연산자(==, !=, >, < 등)는 True/False를 반환한다.",
            "Python은 `1 < x < 10` 같은 연쇄 비교를 지원한다.",
            "논리 연산자: and(모두 참), or(하나 이상 참), not(반전)",
            "단축 평가를 활용하면 불필요한 연산과 에러를 방지할 수 있다.",
            "복합 할당 연산자(+=, -= 등)로 코드를 간결하게 작성한다.",
            "연산자 우선순위가 헷갈리면 괄호를 사용하여 명확히 한다.",
        ],
    }
