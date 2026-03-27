"""
부록 B: 자주 하는 실수 Top 20
초보자가 가장 많이 빠지는 함정을 유형별로 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 B: 자주 하는 실수 Top 20",
        "sections": [
            # ── 섹션 1: 문법 실수 ──
            {
                "title": "B.1 문법 실수",
                "content": [
                    (
                        "Python이 코드를 실행하기도 전에 "
                        "SyntaxError로 멈추게 만드는 실수들입니다. "
                        "에러 메시지를 잘 읽으면 대부분 바로 고칠 수 있습니다."
                    ),
                    "**실수 1: 들여쓰기 오류**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (IndentationError)\n"
                            "if True:\n"
                            "print('안녕')  # 들여쓰기가 없음!\n"
                            "\n"
                            "# 올바른 코드\n"
                            "if True:\n"
                            "    print('안녕')  # 4칸 들여쓰기"
                        ),
                    },
                    (
                        "Python은 중괄호 대신 **들여쓰기**로 코드 블록을 구분합니다. "
                        "탭과 스페이스를 섞지 말고, 항상 **스페이스 4칸**을 사용하세요. "
                        "대부분의 편집기에서 Tab 키를 누르면 자동으로 스페이스 4칸이 입력됩니다."
                    ),
                    "**실수 2: 콜론(:) 빼먹기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (SyntaxError)\n"
                            "if score >= 90\n"
                            "    print('A등급')\n"
                            "\n"
                            "# 올바른 코드\n"
                            "if score >= 90:       # 콜론 필수!\n"
                            "    print('A등급')"
                        ),
                    },
                    (
                        "if, elif, else, for, while, def, class 뒤에는 "
                        "반드시 콜론(:)이 와야 합니다. "
                        "'블록을 시작한다'는 표시입니다."
                    ),
                    "**실수 3: 괄호 불일치**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (SyntaxError)\n"
                            'print("결과:", (1 + 2)\n'
                            "\n"
                            "# 올바른 코드\n"
                            'print("결과:", (1 + 2))'
                        ),
                    },
                    (
                        "여는 괄호 (, [, { 의 수와 닫는 괄호 ), ], } 의 수가 "
                        "반드시 일치해야 합니다. "
                        "에러 위치가 다른 줄을 가리킬 수 있으므로, "
                        "에러가 나면 바로 윗줄의 괄호부터 확인하세요."
                    ),
                    "**실수 4: = 와 == 혼동**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (의도치 않은 동작 또는 SyntaxError)\n"
                            "if x = 10:    # 대입 연산자를 조건에 사용!\n"
                            "    print(x)\n"
                            "\n"
                            "# 올바른 코드\n"
                            "if x == 10:   # 비교 연산자\n"
                            "    print(x)"
                        ),
                    },
                    (
                        "`=`는 '값을 넣어라(대입)', "
                        "`==`는 '같은지 비교해라(비교)'입니다. "
                        "조건문에서는 항상 `==`를 사용해야 합니다."
                    ),
                    "**실수 5: 잘못된 변수명**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (SyntaxError / NameError)\n"
                            "2nd_place = '은메달'    # 숫자로 시작 불가\n"
                            "my-name = '철수'        # 하이픈 사용 불가\n"
                            "class = 'A반'           # 키워드 사용 불가\n"
                            "\n"
                            "# 올바른 코드\n"
                            "second_place = '은메달'  # 문자로 시작, 밑줄 사용\n"
                            "my_name = '철수'         # 밑줄로 단어 연결\n"
                            "class_name = 'A반'       # 키워드 피하기"
                        ),
                    },
                    (
                        "변수명 규칙: 문자 또는 밑줄(_)로 시작, "
                        "문자/숫자/밑줄만 사용 가능, "
                        "Python 키워드는 사용 불가."
                    ),
                ],
            },
            # ── 섹션 2: 타입 실수 ──
            {
                "title": "B.2 타입 실수",
                "content": [
                    (
                        "Python은 타입을 자동으로 처리하지만, "
                        "그래서 오히려 타입 관련 실수를 놓치기 쉽습니다."
                    ),
                    "**실수 6: 문자열 + 숫자 연산**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (TypeError)\n"
                            "age = input('나이: ')    # '25' (문자열!)\n"
                            "next_year = age + 1      # 문자열 + 숫자 = 에러!\n"
                            "\n"
                            "# 올바른 코드\n"
                            "age = int(input('나이: '))  # 25 (정수로 변환)\n"
                            "next_year = age + 1         # 26"
                        ),
                    },
                    (
                        "input()은 **항상 문자열**을 반환합니다. "
                        "숫자로 쓰려면 반드시 int() 또는 float()로 변환해야 합니다."
                    ),
                    "**실수 7: 가변 기본 인자 (Mutable Default Argument)**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (의도치 않은 공유)\n"
                            "def add_item(item, items=[]):\n"
                            "    items.append(item)\n"
                            "    return items\n"
                            "\n"
                            "print(add_item('a'))  # ['a']\n"
                            "print(add_item('b'))  # ['a', 'b'] ← 이전 호출의 것이 남아있음!\n"
                            "\n"
                            "# 올바른 코드\n"
                            "def add_item(item, items=None):\n"
                            "    if items is None:\n"
                            "        items = []\n"
                            "    items.append(item)\n"
                            "    return items\n"
                            "\n"
                            "print(add_item('a'))  # ['a']\n"
                            "print(add_item('b'))  # ['b'] ← 독립적!"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "리스트, 딕셔너리 같은 가변(mutable) 객체를 "
                            "함수의 기본 인자로 사용하면, "
                            "모든 호출이 같은 객체를 공유합니다. "
                            "기본값으로는 None을 쓰고 함수 안에서 새로 만드세요."
                        ),
                    },
                    "**실수 8: 정수 나눗셈 착각**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 주의: / 는 항상 float 반환\n"
                            "result = 10 / 3    # 3.3333... (float)\n"
                            "result = 10 / 2    # 5.0 (float!  5가 아님)\n"
                            "\n"
                            "# 정수 나눗셈을 원하면 // 사용\n"
                            "result = 10 // 3   # 3 (int)\n"
                            "result = 10 // 2   # 5 (int)"
                        ),
                    },
                    (
                        "Python 3에서 `/`는 항상 float을 반환합니다. "
                        "정수 결과가 필요하면 `//`(몫 연산)을 사용하세요."
                    ),
                    "**실수 9: None 비교**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (동작하지만 권장하지 않음)\n"
                            "if result == None:\n"
                            "    print('없음')\n"
                            "\n"
                            "# 올바른 코드\n"
                            "if result is None:    # is 로 비교!\n"
                            "    print('없음')"
                        ),
                    },
                    (
                        "None은 특별한 싱글턴 객체이므로 "
                        "`==` 대신 `is`로 비교하는 것이 Python의 관례입니다. "
                        "`is not None`도 마찬가지입니다."
                    ),
                ],
            },
            # ── 섹션 3: 논리 실수 ──
            {
                "title": "B.3 논리 실수",
                "content": [
                    (
                        "문법은 맞지만 프로그램이 의도대로 동작하지 않는 실수입니다. "
                        "에러 메시지가 나지 않아 찾기가 더 어렵습니다."
                    ),
                    "**실수 10: 무한 루프**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (무한 루프!)\n"
                            "count = 0\n"
                            "while count < 5:\n"
                            "    print(count)\n"
                            "    # count += 1 을 빼먹음! → 영원히 0 출력\n"
                            "\n"
                            "# 올바른 코드\n"
                            "count = 0\n"
                            "while count < 5:\n"
                            "    print(count)\n"
                            "    count += 1    # 반드시 종료 조건에 다가가야 함"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "while 루프를 쓸 때 항상 자문하세요: "
                            "'이 루프가 끝나는 조건에 도달할 수 있는가?' "
                            "무한 루프에 빠지면 Ctrl+C로 강제 종료할 수 있습니다."
                        ),
                    },
                    "**실수 11: Off-by-One 에러**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (1~10까지 출력하려는데...)\n"
                            "for i in range(10):\n"
                            "    print(i)      # 0부터 9까지 출력됨\n"
                            "\n"
                            "# 올바른 코드\n"
                            "for i in range(1, 11):  # 시작=1, 끝=11(미포함)\n"
                            "    print(i)            # 1부터 10까지 출력"
                        ),
                    },
                    (
                        "range(n)은 0부터 n-1까지입니다. "
                        "'하나 차이'로 의도한 범위를 벗어나는 실수를 "
                        "Off-by-One 에러라고 합니다. "
                        "경계값을 항상 확인하세요."
                    ),
                    "**실수 12: 빈 컬렉션 체크**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 불필요하게 복잡한 코드\n"
                            "if len(my_list) == 0:\n"
                            "    print('비어있음')\n"
                            "\n"
                            "if len(my_list) > 0:\n"
                            "    print('데이터 있음')\n"
                            "\n"
                            "# Python다운 코드 (Pythonic)\n"
                            "if not my_list:       # 빈 리스트는 False\n"
                            "    print('비어있음')\n"
                            "\n"
                            "if my_list:           # 데이터가 있으면 True\n"
                            "    print('데이터 있음')"
                        ),
                    },
                    (
                        "빈 리스트 `[]`, 빈 문자열 `''`, 빈 딕셔너리 `{}`, "
                        "숫자 `0`, `None`은 모두 불리언으로 `False`입니다. "
                        "이를 활용하면 더 깔끔한 코드를 쓸 수 있습니다."
                    ),
                    "**실수 13: 얕은 복사 함정**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (같은 리스트를 가리킴!)\n"
                            "original = [1, 2, 3]\n"
                            "copy = original         # 복사가 아니라 같은 객체!\n"
                            "copy.append(4)\n"
                            "print(original)          # [1, 2, 3, 4] ← 원본도 변경됨!\n"
                            "\n"
                            "# 올바른 코드\n"
                            "original = [1, 2, 3]\n"
                            "copy = original.copy()   # 또는 original[:] 또는 list(original)\n"
                            "copy.append(4)\n"
                            "print(original)          # [1, 2, 3] ← 원본 유지!"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "변수 대입(=)은 '복사'가 아니라 '같은 객체를 가리킨다'는 뜻입니다. "
                            "독립적인 복사본이 필요하면 .copy(), [:], "
                            "또는 copy 모듈의 deepcopy()를 사용하세요."
                        ),
                    },
                    "**실수 14: 스코프 혼동**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (UnboundLocalError)\n"
                            "count = 0\n"
                            "\n"
                            "def increment():\n"
                            "    count += 1    # 전역 변수를 직접 수정할 수 없음!\n"
                            "    return count\n"
                            "\n"
                            "# 올바른 코드 (방법 1: 매개변수 사용 — 권장)\n"
                            "def increment(count):\n"
                            "    return count + 1\n"
                            "\n"
                            "count = 0\n"
                            "count = increment(count)  # 1"
                        ),
                    },
                    (
                        "함수 안에서 전역 변수를 읽기만 하는 것은 가능하지만, "
                        "수정하려면 `global` 키워드가 필요합니다. "
                        "하지만 global은 코드를 복잡하게 만드므로, "
                        "매개변수와 반환값을 사용하는 것이 훨씬 좋은 방법입니다."
                    ),
                ],
            },
            # ── 섹션 4: 습관 실수 ──
            {
                "title": "B.4 습관 실수",
                "content": [
                    (
                        "코드는 동작하지만 나쁜 습관으로 인해 "
                        "나중에 더 큰 문제를 만드는 실수들입니다."
                    ),
                    "**실수 15: 변수 이름 대충 짓기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 나쁜 코드 (아무도 이해 못함)\n"
                            "a = 50000\n"
                            "b = 12\n"
                            "c = a * b\n"
                            "\n"
                            "# 좋은 코드 (이름만 봐도 이해됨)\n"
                            "monthly_salary = 50000\n"
                            "months = 12\n"
                            "annual_salary = monthly_salary * months"
                        ),
                    },
                    (
                        "변수 이름은 '미래의 나'를 위한 메모입니다. "
                        "6개월 뒤에 코드를 다시 볼 때 `a`, `b`, `c`로는 "
                        "아무것도 알 수 없습니다. "
                        "길더라도 의미 있는 이름을 쓰세요."
                    ),
                    "**실수 16: print 디버깅만 하기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 초보자의 디버깅 (비효율적)\n"
                            "def calculate(data):\n"
                            "    print('여기 옴')           # 디버깅 print 1\n"
                            "    print('data:', data)       # 디버깅 print 2\n"
                            "    result = process(data)\n"
                            "    print('result:', result)   # 디버깅 print 3\n"
                            "    return result\n"
                            "\n"
                            "# 더 나은 방법: breakpoint() 사용 (Python 3.7+)\n"
                            "def calculate(data):\n"
                            "    breakpoint()   # 여기서 멈추고 대화식 디버깅\n"
                            "    result = process(data)\n"
                            "    return result"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "breakpoint()를 넣으면 그 줄에서 프로그램이 멈추고 "
                            "pdb(Python Debugger)가 실행됩니다. "
                            "변수 값을 확인하고, 한 줄씩 실행하며, "
                            "문제를 정확히 추적할 수 있습니다."
                        ),
                    },
                    "**실수 17: 주석 안 쓰기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 나쁜 코드 (왜 이렇게 하는지 알 수 없음)\n"
                            "if age >= 19:\n"
                            "    allow_access()\n"
                            "\n"
                            "# 좋은 코드 (이유를 설명)\n"
                            "# 한국 법률상 성인 기준: 만 19세 이상\n"
                            "if age >= 19:\n"
                            "    allow_access()"
                        ),
                    },
                    (
                        "주석은 '왜(why)' 이 코드가 필요한지를 적는 것입니다. "
                        "'무엇을(what)' 하는지는 코드 자체로 알 수 있어야 합니다. "
                        "매직 넘버(19 같은 특별한 의미의 숫자)에는 반드시 주석을 달거나 "
                        "상수로 이름을 붙이세요."
                    ),
                    "**실수 18: 테스트 안 하기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 이 함수를 작성한 후...\n"
                            "def calculate_discount(price, rate):\n"
                            "    return price * (1 - rate / 100)\n"
                            "\n"
                            "# 반드시 간단한 테스트를 해보세요!\n"
                            "# 10000원에 10% 할인 → 9000원이어야 함\n"
                            "assert calculate_discount(10000, 10) == 9000.0\n"
                            "\n"
                            "# 경계값도 테스트\n"
                            "assert calculate_discount(10000, 0) == 10000.0   # 0% 할인\n"
                            "assert calculate_discount(10000, 100) == 0.0     # 100% 할인\n"
                            "print('모든 테스트 통과!')"
                        ),
                    },
                    (
                        "함수를 만들었으면 직접 호출해서 결과를 확인하세요. "
                        "assert 문으로 예상 결과와 비교하는 습관을 들이면 "
                        "버그를 일찍 발견할 수 있습니다."
                    ),
                    "**실수 19: 에러 무시하기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 매우 나쁜 코드 (에러를 삼켜버림)\n"
                            "try:\n"
                            "    result = int(user_input)\n"
                            "except:\n"
                            "    pass          # 아무것도 안 함 → 문제 원인 파악 불가\n"
                            "\n"
                            "# 올바른 코드 (에러 종류를 명시하고 처리)\n"
                            "try:\n"
                            "    result = int(user_input)\n"
                            "except ValueError:\n"
                            '    print("숫자를 입력해주세요.")\n'
                            "    result = 0    # 기본값 설정"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "except: pass (맨손 except + 무시)는 "
                            "Python 코드에서 가장 위험한 패턴 중 하나입니다. "
                            "모든 에러를 삼켜버려서 버그를 찾을 수 없게 만듭니다. "
                            "반드시 구체적인 예외 타입을 명시하고 적절히 처리하세요."
                        ),
                    },
                    "**실수 20: 반복문 안에서 리스트 수정하기**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 잘못된 코드 (순회 중 삭제 → 요소 건너뜀)\n"
                            "numbers = [1, 2, 3, 4, 5]\n"
                            "for num in numbers:\n"
                            "    if num % 2 == 0:\n"
                            "        numbers.remove(num)   # 위험!\n"
                            "print(numbers)  # [1, 3, 5] 가 아닌 예상 밖의 결과\n"
                            "\n"
                            "# 올바른 코드 (새 리스트를 만들기)\n"
                            "numbers = [1, 2, 3, 4, 5]\n"
                            "odd_numbers = [num for num in numbers if num % 2 != 0]\n"
                            "print(odd_numbers)  # [1, 3, 5]"
                        ),
                    },
                    (
                        "for 루프로 순회 중인 리스트를 수정하면 "
                        "인덱스가 어긋나면서 요소를 건너뛸 수 있습니다. "
                        "리스트 컴프리헨션으로 새 리스트를 만드는 것이 안전합니다."
                    ),
                    {
                        "type": "note",
                        "text": (
                            "이 20가지 실수는 모든 초보자가 한 번쯤 겪는 것들입니다. "
                            "실수 자체를 두려워하지 마세요. "
                            "중요한 것은 같은 실수를 반복하지 않도록 "
                            "'왜 틀렸는지'를 이해하는 것입니다."
                        ),
                    },
                ],
            },
        ],
    }
