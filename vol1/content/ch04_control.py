"""챕터 4: 제어문 — 프로그램의 흐름을 다스리다."""


def get_chapter():
    """챕터 4 콘텐츠를 반환한다."""
    return {
        "number": 4,
        "title": "제어문",
        "subtitle": "프로그램의 흐름을 다스리다",
        "big_picture": (
            "지금까지 작성한 코드는 위에서 아래로 한 줄씩 실행되었습니다. "
            "하지만 현실의 프로그램은 조건에 따라 다른 동작을 하고, "
            "같은 작업을 반복해야 합니다. "
            "제어문은 프로그램의 실행 흐름을 '분기'하고 '반복'하는 도구이며, "
            "이것이 프로그래밍의 진짜 힘입니다."
        ),
        "sections": [
            # ── 섹션 1: 조건문 if/elif/else ──────────────────
            {
                "title": "조건문 if / elif / else",
                "content": [
                    "조건문은 **조건이 참인지 거짓인지**에 따라 "
                    "실행할 코드를 선택하는 구문입니다. "
                    "모든 프로그래밍 언어의 핵심 구조입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "조건문은 갈림길의 이정표와 같습니다. "
                            "'비가 오면 우산을 챙기고, 아니면 그냥 나간다.' "
                            "이 판단 과정이 바로 if/else입니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# if 기본 구조\n"
                            "temperature = 35\n\n"
                            "if temperature >= 30:\n"
                            "    print('폭염 주의보!')  # 조건이 True면 실행\n"
                            "    print('물을 충분히 마시세요.')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "들여쓰기: Python의 생명줄",
                    },
                    (
                        "Python은 중괄호 `{}` 대신 **들여쓰기(indentation)**로 "
                        "코드 블록을 구분합니다. "
                        "들여쓰기가 잘못되면 프로그램이 작동하지 않습니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 올바른 들여쓰기 (공백 4칸 권장)\n"
                            "score = 85\n\n"
                            "if score >= 90:\n"
                            "    grade = 'A'\n"
                            "    print('우수합니다!')\n"
                            "elif score >= 80:\n"
                            "    grade = 'B'\n"
                            "    print('잘했습니다!')\n"
                            "elif score >= 70:\n"
                            "    grade = 'C'\n"
                            "    print('보통입니다.')\n"
                            "else:\n"
                            "    grade = 'F'\n"
                            "    print('분발하세요.')\n\n"
                            "print(f'학점: {grade}')  # 들여쓰기 없음 → 항상 실행"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "탭(Tab)과 공백(Space)을 섞어 쓰면 "
                            "`IndentationError`가 발생합니다. "
                            "공백 4칸을 표준으로 통일하세요. "
                            "대부분의 편집기에서 Tab 키를 누르면 자동으로 "
                            "공백 4칸이 입력되도록 설정할 수 있습니다."
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "if 조건1?"},
                            {"label": "elif 조건2?"},
                            {"label": "else"},
                        ],
                        "arrow_labels": ["False", "False"],
                        "note": "True이면 해당 블록을 실행하고 나머지는 건너뜁니다",
                    },
                    {
                        "type": "heading",
                        "text": "중첩 조건문",
                    },
                    "조건문 안에 또 다른 조건문을 넣을 수 있습니다. "
                    "하지만 3단계 이상 중첩하면 읽기 어려워집니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 중첩 조건문 예시 — 놀이기구 탑승 여부\n"
                            "age = 12\n"
                            "height = 140\n\n"
                            "if age >= 10:\n"
                            "    if height >= 130:\n"
                            "        print('탑승 가능합니다!')\n"
                            "    else:\n"
                            "        print('키가 130cm 이상이어야 합니다.')\n"
                            "else:\n"
                            "    print('10세 이상만 탑승 가능합니다.')\n\n"
                            "# 더 나은 방법: and로 합치기\n"
                            "if age >= 10 and height >= 130:\n"
                            "    print('탑승 가능합니다!')\n"
                            "else:\n"
                            "    print('조건을 충족하지 못합니다.')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "중첩이 깊어지면 `and`/`or`로 조건을 합치거나, "
                            "조기 반환(early return) 패턴을 사용하세요. "
                            "가독성이 크게 향상됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 삼항 연산자 ──────────────────────────
            {
                "title": "삼항 연산자 (조건 표현식)",
                "content": [
                    "간단한 if/else를 **한 줄**로 쓸 수 있는 문법입니다. "
                    "변수에 값을 조건부로 대입할 때 유용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 문법: 값1 if 조건 else 값2\n\n"
                            "age = 20\n\n"
                            "# 일반 if/else\n"
                            "if age >= 19:\n"
                            "    status = '성인'\n"
                            "else:\n"
                            "    status = '미성년자'\n\n"
                            "# 삼항 연산자로 같은 코드\n"
                            "status = '성인' if age >= 19 else '미성년자'\n"
                            "print(status)  # 성인"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 실전 활용 예시\n\n"
                            "# 1) 절댓값 구하기\n"
                            "num = -7\n"
                            "absolute = num if num >= 0 else -num\n"
                            "print(absolute)  # 7\n\n"
                            "# 2) 짝홀수 판별\n"
                            "n = 13\n"
                            "parity = '짝수' if n % 2 == 0 else '홀수'\n"
                            "print(parity)  # 홀수\n\n"
                            "# 3) 최솟값 구하기\n"
                            "a, b = 10, 25\n"
                            "smaller = a if a < b else b\n"
                            "print(smaller)  # 10"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "삼항 연산자를 중첩하면 읽기 어려워집니다. "
                            "`a if x else b if y else c` 같은 코드는 피하고, "
                            "복잡한 조건은 일반 if/elif/else를 사용하세요."
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "삼항 연산자는 '표현식(expression)'이므로 "
                            "f-string이나 함수 인자 안에서도 사용할 수 있습니다. "
                            "예: `print(f'{\"합격\" if score >= 60 else \"불합격\"}')`"
                        ),
                    },
                ],
            },
            # ── 섹션 3: for 반복문 ───────────────────────────
            {
                "title": "for 반복문",
                "content": [
                    "for문은 **정해진 횟수**만큼 또는 **시퀀스의 각 요소**를 "
                    "순회하며 반복합니다. Python에서 가장 많이 쓰는 반복문입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "for문은 출석 부르기와 같습니다. "
                            "명단에 있는 학생을 첫 번째부터 마지막까지 "
                            "한 명씩 이름을 불러가며 확인하는 것이죠."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 for문 — 시퀀스 순회\n"
                            "fruits = ['사과', '바나나', '딸기', '포도']\n\n"
                            "for fruit in fruits:\n"
                            "    print(f'{fruit}을(를) 먹겠습니다!')\n\n"
                            "# 출력:\n"
                            "# 사과을(를) 먹겠습니다!\n"
                            "# 바나나을(를) 먹겠습니다!\n"
                            "# 딸기을(를) 먹겠습니다!\n"
                            "# 포도을(를) 먹겠습니다!"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "range() 함수",
                    },
                    "`range()`는 숫자 시퀀스를 생성합니다. "
                    "반복 횟수를 지정할 때 필수적입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# range() 사용법\n\n"
                            "# range(끝) — 0부터 끝-1까지\n"
                            "for i in range(5):\n"
                            "    print(i, end=' ')  # 0 1 2 3 4\n"
                            "print()\n\n"
                            "# range(시작, 끝) — 시작부터 끝-1까지\n"
                            "for i in range(1, 6):\n"
                            "    print(i, end=' ')  # 1 2 3 4 5\n"
                            "print()\n\n"
                            "# range(시작, 끝, 간격)\n"
                            "for i in range(0, 10, 2):\n"
                            "    print(i, end=' ')  # 0 2 4 6 8\n"
                            "print()\n\n"
                            "# 역순 반복\n"
                            "for i in range(5, 0, -1):\n"
                            "    print(i, end=' ')  # 5 4 3 2 1"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "enumerate() — 인덱스와 값을 함께",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# enumerate()로 인덱스와 값 동시 접근\n"
                            "menu = ['김치찌개', '된장찌개', '비빔밥', '불고기']\n\n"
                            "for index, item in enumerate(menu):\n"
                            "    print(f'{index + 1}. {item}')\n\n"
                            "# 출력:\n"
                            "# 1. 김치찌개\n"
                            "# 2. 된장찌개\n"
                            "# 3. 비빔밥\n"
                            "# 4. 불고기\n\n"
                            "# start 매개변수로 시작 번호 지정\n"
                            "for num, item in enumerate(menu, start=1):\n"
                            "    print(f'{num}. {item}')  # 같은 결과"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "중첩 for문",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 구구단 출력 (중첩 for문)\n"
                            "for dan in range(2, 10):\n"
                            "    print(f'--- {dan}단 ---')\n"
                            "    for i in range(1, 10):\n"
                            "        print(f'{dan} x {i} = {dan * i}')\n"
                            "    print()  # 단 사이 빈 줄"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 별 찍기 — 직각삼각형\n"
                            "for row in range(1, 6):\n"
                            "    print('*' * row)\n\n"
                            "# 출력:\n"
                            "# *\n"
                            "# **\n"
                            "# ***\n"
                            "# ****\n"
                            "# *****"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "문자열에 `*`를 곱하면 반복됩니다. "
                            "`'*' * 5`는 `'*****'`가 됩니다. "
                            "별 찍기 문제에서 매우 유용한 기법입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: while 반복문 ─────────────────────────
            {
                "title": "while 반복문",
                "content": [
                    "while문은 **조건이 참인 동안** 계속 반복합니다. "
                    "반복 횟수가 정해지지 않은 경우에 적합합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "while문은 '신호등'과 같습니다. "
                            "'빨간불인 동안 기다린다' — "
                            "조건(빨간불)이 유지되는 한 반복(기다림)하고, "
                            "조건이 바뀌면(파란불) 빠져나옵니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 while문 — 카운트다운\n"
                            "count = 5\n\n"
                            "while count > 0:\n"
                            "    print(count)\n"
                            "    count -= 1  # 반드시 조건을 변화시켜야 함!\n\n"
                            "print('발사!')  # 5 4 3 2 1 발사!"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "while문 안에서 조건을 변화시키지 않으면 "
                            "**무한 루프**에 빠집니다. "
                            "실행 중 Ctrl+C로 강제 종료할 수 있습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 무한 루프 — 의도적으로 사용하는 경우\n"
                            "# (break와 함께 사용)\n\n"
                            "while True:\n"
                            "    user_input = input('종료하려면 q를 입력: ')\n"
                            "    if user_input == 'q':\n"
                            "        print('프로그램을 종료합니다.')\n"
                            "        break  # 루프 탈출\n"
                            "    print(f'입력값: {user_input}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "카운터 패턴과 누적 패턴",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 누적 패턴: 1부터 100까지의 합\n"
                            "total = 0\n"
                            "num = 1\n\n"
                            "while num <= 100:\n"
                            "    total += num\n"
                            "    num += 1\n\n"
                            "print(f'1~100의 합: {total}')  # 5050"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "for vs while — 언제 어떤 것을?",
                    },
                    {
                        "type": "table",
                        "headers": ["상황", "추천", "이유"],
                        "rows": [
                            [
                                "반복 횟수가 정해짐",
                                "for",
                                "range()로 명확히 표현",
                            ],
                            [
                                "리스트/문자열 순회",
                                "for",
                                "자연스러운 순회 구조",
                            ],
                            [
                                "조건 만족 시까지 반복",
                                "while",
                                "종료 조건 명확",
                            ],
                            [
                                "사용자 입력 대기",
                                "while",
                                "횟수 예측 불가",
                            ],
                        ],
                    },
                ],
            },
            # ── 섹션 5: break, continue, pass ────────────────
            {
                "title": "break, continue, pass",
                "content": [
                    "반복문 안에서 흐름을 세밀하게 제어하는 세 가지 키워드입니다.",
                    {
                        "type": "table",
                        "headers": ["키워드", "역할", "비유"],
                        "rows": [
                            ["break", "반복문 즉시 탈출", "비상구"],
                            ["continue", "현재 반복 건너뛰기", "한 문제 건너뛰기"],
                            ["pass", "아무것도 하지 않음", "빈 페이지"],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "break — 반복문 탈출",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# break: 특정 값을 찾으면 즉시 멈추기\n"
                            "numbers = [10, 25, 30, 42, 55, 60]\n\n"
                            "for num in numbers:\n"
                            "    if num == 42:\n"
                            "        print(f'{num}을 찾았습니다!')\n"
                            "        break  # 찾으면 루프 종료\n"
                            "    print(f'{num} 확인 중...')\n\n"
                            "# 출력:\n"
                            "# 10 확인 중...\n"
                            "# 25 확인 중...\n"
                            "# 30 확인 중...\n"
                            "# 42을 찾았습니다!"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "continue — 건너뛰기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# continue: 홀수만 출력 (짝수는 건너뛰기)\n"
                            "for i in range(1, 11):\n"
                            "    if i % 2 == 0:\n"
                            "        continue  # 짝수면 아래 코드 건너뜀\n"
                            "    print(i, end=' ')  # 1 3 5 7 9"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "pass — 자리 표시자",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# pass: 아직 구현하지 않은 코드의 자리 표시\n\n"
                            "for i in range(10):\n"
                            "    if i % 3 == 0:\n"
                            "        pass  # TODO: 나중에 3의 배수 처리 구현\n"
                            "    else:\n"
                            "        print(i)\n\n"
                            "# pass가 없으면 빈 블록에서 SyntaxError 발생\n"
                            "# if True:\n"
                            "#     ← 여기에 아무것도 없으면 에러!"
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "for 루프 시작"},
                            {"label": "다음 요소 가져오기"},
                            {"label": "continue?", "sub": "현재 건너뛰기"},
                            {"label": "break?", "sub": "루프 탈출"},
                            {"label": "본문 실행"},
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python의 for/while에는 `else` 절을 붙일 수 있습니다. "
                            "`break` 없이 루프가 정상 종료되었을 때만 실행됩니다. "
                            "검색 패턴에서 '찾지 못한 경우'를 처리할 때 유용합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# for-else: break 없이 끝나면 else 실행\n"
                            "target = 99\n"
                            "numbers = [10, 20, 30, 40, 50]\n\n"
                            "for num in numbers:\n"
                            "    if num == target:\n"
                            "        print(f'{target}을 찾았습니다!')\n"
                            "        break\n"
                            "else:\n"
                            "    # break가 실행되지 않았을 때 (= 못 찾았을 때)\n"
                            "    print(f'{target}을 찾지 못했습니다.')\n\n"
                            "# 출력: 99을 찾지 못했습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 제어문 실전 패턴 ─────────────────────
            {
                "title": "제어문 실전 패턴",
                "content": [
                    "지금까지 배운 제어문을 조합하여 "
                    "실무에서 자주 쓰이는 패턴을 익혀봅시다.",
                    {
                        "type": "heading",
                        "text": "패턴 1: 입력 검증 루프",
                    },
                    "사용자가 올바른 값을 입력할 때까지 반복하는 패턴입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 입력 검증 루프 — 1~100 사이의 숫자만 허용\n"
                            "while True:\n"
                            "    raw = input('점수를 입력하세요 (1~100): ')\n\n"
                            "    # 숫자인지 확인\n"
                            "    if not raw.isdigit():\n"
                            "        print('숫자만 입력해 주세요.')\n"
                            "        continue\n\n"
                            "    score = int(raw)\n\n"
                            "    # 범위 확인\n"
                            "    if 1 <= score <= 100:\n"
                            "        break  # 유효한 입력이면 탈출\n\n"
                            "    print('1에서 100 사이의 값을 입력해 주세요.')\n\n"
                            "print(f'입력된 점수: {score}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "패턴 2: 메뉴 시스템",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 간단한 메뉴 시스템\n"
                            "while True:\n"
                            "    print('\\n=== 메뉴 ===')\n"
                            "    print('1. 인사하기')\n"
                            "    print('2. 덧셈 계산')\n"
                            "    print('3. 종료')\n\n"
                            "    choice = input('선택: ')\n\n"
                            "    if choice == '1':\n"
                            "        name = input('이름을 입력하세요: ')\n"
                            "        print(f'안녕하세요, {name}님!')\n"
                            "    elif choice == '2':\n"
                            "        a = int(input('첫 번째 수: '))\n"
                            "        b = int(input('두 번째 수: '))\n"
                            "        print(f'{a} + {b} = {a + b}')\n"
                            "    elif choice == '3':\n"
                            "        print('프로그램을 종료합니다.')\n"
                            "        break\n"
                            "    else:\n"
                            "        print('잘못된 선택입니다. 다시 입력해 주세요.')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "패턴 3: 검색과 필터링",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 리스트에서 조건에 맞는 값 찾기\n"
                            "scores = [78, 92, 65, 88, 45, 97, 53, 81]\n\n"
                            "# 패턴 A: 최대값 찾기\n"
                            "max_score = scores[0]\n"
                            "for s in scores:\n"
                            "    if s > max_score:\n"
                            "        max_score = s\n"
                            "print(f'최고 점수: {max_score}')  # 97\n\n"
                            "# 패턴 B: 조건 필터링 (60점 이상만)\n"
                            "passed = []\n"
                            "for s in scores:\n"
                            "    if s >= 60:\n"
                            "        passed.append(s)\n"
                            "print(f'합격자 점수: {passed}')  # [78, 92, 65, 88, 97, 81]\n\n"
                            "# 패턴 C: 개수 세기\n"
                            "fail_count = 0\n"
                            "for s in scores:\n"
                            "    if s < 60:\n"
                            "        fail_count += 1\n"
                            "print(f'불합격자 수: {fail_count}명')  # 2명"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실습: 숫자 맞추기 게임",
                    },
                    "배운 제어문을 모두 활용한 종합 실습입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import random\n\n"
                            "# 1~100 사이의 랜덤 숫자 생성\n"
                            "answer = random.randint(1, 100)\n"
                            "attempts = 0\n"
                            "max_attempts = 7\n\n"
                            "print('=== 숫자 맞추기 게임 ===')\n"
                            "print(f'1~100 사이의 숫자를 맞추세요! (최대 {max_attempts}회)')\n\n"
                            "while attempts < max_attempts:\n"
                            "    # 입력 검증\n"
                            "    raw = input(f'\\n[{attempts + 1}/{max_attempts}] 숫자 입력: ')\n"
                            "    if not raw.isdigit():\n"
                            "        print('숫자만 입력해 주세요.')\n"
                            "        continue\n\n"
                            "    guess = int(raw)\n"
                            "    attempts += 1\n\n"
                            "    # 정답 비교\n"
                            "    if guess == answer:\n"
                            "        print(f'정답입니다! {attempts}번 만에 맞추셨습니다!')\n"
                            "        break\n"
                            "    elif guess < answer:\n"
                            "        print('더 큰 수입니다. ↑')\n"
                            "    else:\n"
                            "        print('더 작은 수입니다. ↓')\n"
                            "else:\n"
                            "    # 기회를 모두 소진한 경우\n"
                            "    print(f'\\n게임 오버! 정답은 {answer}였습니다.')"
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "랜덤 숫자 생성"},
                            {"label": "사용자 입력"},
                            {"label": "정답 비교"},
                            {"label": "성공!"},
                        ],
                        "note": "오답이면 힌트(크다/작다)를 출력하고 다시 입력받습니다",
                    },
                ],
            },
        ],
        "practical_tips": [
            "조건문에서 `==`(비교)와 `=`(대입)을 혼동하지 마세요.",
            "들여쓰기는 항상 공백 4칸으로 통일하세요.",
            "중첩이 3단계 이상이면 구조를 재설계하세요.",
            "무한 루프에는 반드시 break 탈출 조건을 넣으세요.",
            "for문은 횟수가 정해진 반복, while문은 조건 기반 반복에 적합합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 코드의 출력은?\n```\nfor i in range(3):\n    print(i)\n```",
                "choices": ["A) 1 2 3", "B) 0 1 2", "C) 0 1 2 3", "D) 1 2"],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "`while` 루프 안에서 `continue`를 만나면 어떻게 되나요?"
                ),
                "choices": [
                    "A) 루프를 완전히 빠져나간다",
                    "B) 현재 반복을 건너뛰고 조건 검사로 돌아간다",
                    "C) 다음 줄을 실행한다",
                    "D) 프로그램이 종료된다",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "1부터 100까지의 정수 중에서 3의 배수이면서 "
                    "5의 배수가 아닌 수를 모두 출력하는 프로그램을 작성하세요."
                ),
                "hint": "for + range + if 조합, % 연산자로 배수 판별",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "사용자로부터 정수를 계속 입력받아 누적 합을 계산하고, "
                    "0을 입력하면 총합과 입력 횟수를 출력하며 종료하는 "
                    "프로그램을 작성하세요."
                ),
                "hint": "while True + break 패턴, 카운터와 누적 변수 활용",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "구구단 중 사용자가 원하는 단만 출력하는 프로그램을 작성하세요. "
                    "2~9 외의 값을 입력하면 '2~9 사이의 값을 입력해 주세요'를 "
                    "출력하고 다시 입력받도록 하세요."
                ),
                "hint": "입력 검증 루프(while True) + for문 조합",
            },
        ],
        "challenge": {
            "question": (
                "가위바위보 게임을 만드세요. 컴퓨터는 random.choice로 선택하고, "
                "사용자가 '종료'를 입력할 때까지 반복합니다. "
                "각 라운드 결과와 누적 전적(승/패/무)을 출력하세요."
            ),
            "hint": (
                "while True로 게임 루프를 만들고, "
                "if/elif로 승패를 판정하세요. "
                "random.choice(['가위', '바위', '보'])로 컴퓨터 선택을 구현합니다."
            ),
        },
        "summary": [
            "if/elif/else는 조건에 따라 실행 경로를 선택한다.",
            "Python은 들여쓰기(공백 4칸)로 코드 블록을 구분한다.",
            "삼항 연산자 `x if 조건 else y`로 간단한 조건 대입을 한 줄로 작성한다.",
            "for문은 시퀀스 순회에, while문은 조건 기반 반복에 적합하다.",
            "range()는 숫자 시퀀스를, enumerate()는 인덱스+값을 생성한다.",
            "break는 루프 탈출, continue는 현재 반복 건너뛰기, pass는 빈 블록 채우기이다.",
            "입력 검증 루프(while True + break)는 실무에서 매우 자주 쓰이는 패턴이다.",
            "for-else 구문은 break 없이 루프가 끝났을 때만 else를 실행한다.",
        ],
    }
