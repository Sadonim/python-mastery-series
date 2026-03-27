"""Chapter 0: 복습 & 심화 준비 - Vol.1 핵심 정리와 Vol.2 미리보기."""


def get_chapter():
    """챕터 0의 전체 콘텐츠를 딕셔너리로 반환한다."""
    return {
        "number": 0,
        "title": "복습 & 심화 준비",
        "subtitle": "Vol.1 핵심 정리와 Vol.2 미리보기",
        "big_picture": (
            "Vol.2를 시작하기 전에 Vol.1에서 배운 핵심 개념들을 빠르게 점검합니다. "
            "변수, 자료형, 제어문, 함수, 자료구조의 핵심을 10분 안에 복습하고, "
            "Vol.2에서 다룰 객체지향 프로그래밍(OOP), 예외처리, 파일 입출력, "
            "정규식, 이터레이터, 데코레이터의 전체 그림을 미리 살펴봅니다. "
            "또한 Python 3.12+ 환경 점검과 PEP 8 코딩 스타일도 함께 익힙니다."
        ),
        "sections": [
            _section_vol1_quick_review(),
            _section_vol2_preview(),
            _section_dev_environment(),
            _section_pep8_style(),
            _section_docstring(),
        ],
        "practical_tips": [
            "복습할 때는 책을 닫고 백지에 직접 코드를 써보세요. 기억 인출 훈련이 단순 재독보다 3배 효과적입니다.",
            "VS Code에서 `Ctrl+Shift+P` → 'Format Document'를 습관화하면 PEP 8을 자동으로 지킬 수 있습니다.",
            "Python 3.12는 오류 메시지가 훨씬 친절해졌습니다. 에러를 만나면 당황하지 말고 메시지를 천천히 읽으세요.",
            "`python --version`과 `pip list`로 환경을 먼저 확인하는 것이 모든 문제 해결의 첫걸음입니다.",
            "docstring은 '미래의 나'에게 보내는 편지입니다. 6개월 후에도 이해할 수 있게 작성하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 Python 리스트(list)와 튜플(tuple)의 가장 큰 차이점은 무엇인가요?",
                "choices": [
                    "A) 리스트는 숫자만, 튜플은 문자열만 저장할 수 있다",
                    "B) 리스트는 변경 가능(mutable), 튜플은 변경 불가능(immutable)하다",
                    "C) 리스트는 순서가 없고, 튜플은 순서가 있다",
                    "D) 리스트는 중복을 허용하지 않고, 튜플은 허용한다",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "PEP 8에 따른 올바른 함수 이름 작성 방식은 무엇인가요?",
                "choices": [
                    "A) calculateUserAge()",
                    "B) CalculateUserAge()",
                    "C) calculate_user_age()",
                    "D) CALCULATE_USER_AGE()",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "다음 중 Vol.2에서 새롭게 배울 개념이 아닌 것은?",
                "choices": [
                    "A) 클래스와 객체 (OOP)",
                    "B) 데코레이터 (decorator)",
                    "C) for 반복문",
                    "D) 이터레이터 (iterator)",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "다음 요구사항을 만족하는 함수 `summarize_scores`를 작성하세요.\n"
                    "- 정수 점수 리스트를 입력받아 딕셔너리를 반환한다\n"
                    "- 반환 딕셔너리: {'최고': 최댓값, '최저': 최솟값, '평균': 평균값(소수점 1자리)}\n"
                    "예시: summarize_scores([80, 90, 70]) → {'최고': 90, '최저': 70, '평균': 80.0}"
                ),
                "hint": "max(), min(), sum(), len(), round() 내장 함수를 활용하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "아래 코드에서 PEP 8 위반 사항을 모두 찾아 수정하세요.\n"
                    "def calc(x,y):\n"
                    "  z=x+y\n"
                    "  return z\n"
                    "Result=calc(3,5)\n"
                    "print(Result)"
                ),
                "hint": "들여쓰기(4칸), 공백(연산자 양옆), 변수명(소문자_언더스코어), 함수명 규칙을 확인하세요.",
            },
        ],
        "challenge": {
            "question": (
                "Vol.1에서 배운 개념 5가지(변수, 리스트, 딕셔너리, 함수, 반복문)를 모두 활용하여 "
                "'단어 빈도수 분석기'를 만들어보세요. 사용자로부터 문장을 입력받아 "
                "각 단어가 몇 번 등장하는지 딕셔너리로 반환하고, "
                "가장 많이 등장한 단어 Top 3를 출력하는 프로그램을 작성하세요."
            ),
            "hint": (
                "문자열의 .split()으로 단어를 분리하고, 딕셔너리로 빈도를 세어보세요. "
                "정렬은 sorted(dict.items(), key=lambda x: x[1], reverse=True)를 활용하면 됩니다."
            ),
        },
        "summary": [
            "Vol.1 핵심: 변수/자료형, 제어문(if/for/while), 함수, 리스트/딕셔너리/집합은 Python의 기초 골격이다.",
            "Vol.2 로드맵: OOP(클래스·상속) → 예외처리 → 파일 I/O → 정규식 → 이터레이터/제너레이터 → 데코레이터 순으로 진행한다.",
            "개발 환경: Python 3.12+와 VS Code(Pylance, autopep8 확장) 설치를 확인한다.",
            "PEP 8: 들여쓰기 4칸, 소문자_언더스코어 변수/함수명, 클래스는 CamelCase, 상수는 UPPER_CASE.",
            "docstring: 모든 함수·클래스에 목적, 인수, 반환값을 간결하게 문서화하는 습관을 들인다.",
            "좋은 코드는 '한 번 쓰고 백 번 읽는 코드'다. 가독성이 곧 생산성이다.",
        ],
    }


def _section_vol1_quick_review():
    """섹션 1: Vol.1 핵심 내용 빠르게 복습."""
    return {
        "title": "Vol.1 핵심 10분 복습",
        "content": [
            "Vol.1에서 배운 내용을 빠르게 훑어봅니다. 잘 기억나지 않는 부분이 있다면 체크해두고, 나중에 Vol.1 해당 챕터를 다시 살펴보세요.",
            {
                "type": "flow_diagram",
                "nodes": [
                    "변수 & 자료형",
                    "→ 제어문 (if/for/while)",
                    "→ 함수 (def)",
                    "→ 자료구조 (list/dict/set/tuple)",
                    "→ 문자열 & 모듈",
                    "→ Vol.2 심화 시작!",
                ],
                "note": "Vol.1 학습 경로 — 각 단계는 다음 단계의 기반이 됩니다",
            },
            "**변수와 자료형**: Python의 변수는 '이름표'입니다. 같은 이름표를 다른 값에 붙일 수 있으며, 자료형(int, float, str, bool)은 자동으로 결정됩니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 변수와 자료형 복습 ──\n"
                    "name = '홍길동'          # str (문자열)\n"
                    "age = 25                 # int (정수)\n"
                    "height = 175.5           # float (실수)\n"
                    "is_student = True        # bool (논리값)\n"
                    "\n"
                    "# 자료형 확인\n"
                    "print(type(name))        # <class 'str'>\n"
                    "print(type(age))         # <class 'int'>\n"
                    "\n"
                    "# f-string으로 깔끔하게 출력\n"
                    "print(f'{name}은 {age}살이고 키는 {height}cm입니다.')"
                ),
            },
            "**제어문**: `if`로 조건을 분기하고, `for`로 반복하며, `while`로 조건이 참인 동안 반복합니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 제어문 복습 ──\n"
                    "scores = [85, 92, 78, 95, 60]\n"
                    "\n"
                    "# for 반복 + if 조건\n"
                    "for score in scores:\n"
                    "    if score >= 90:\n"
                    "        print(f'{score}점: A학점')\n"
                    "    elif score >= 80:\n"
                    "        print(f'{score}점: B학점')\n"
                    "    else:\n"
                    "        print(f'{score}점: 재시험 대상')\n"
                    "\n"
                    "# 리스트 컴프리헨션 (한 줄로 필터링)\n"
                    "pass_scores = [s for s in scores if s >= 80]\n"
                    "print(f'합격 점수: {pass_scores}')  # [85, 92, 95]"
                ),
            },
            "**함수**: 반복되는 작업을 묶어 이름을 붙인 코드 블록입니다. 매개변수와 반환값으로 데이터를 주고받습니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 함수 복습 ──\n"
                    "def calculate_bmi(weight: float, height_cm: float) -> float:\n"
                    "    \"\"\"BMI(체질량지수)를 계산한다.\n"
                    "\n"
                    "    Args:\n"
                    "        weight: 체중 (kg)\n"
                    "        height_cm: 키 (cm)\n"
                    "\n"
                    "    Returns:\n"
                    "        BMI 값 (소수점 1자리)\n"
                    "    \"\"\"\n"
                    "    height_m = height_cm / 100  # cm → m 변환\n"
                    "    bmi = weight / (height_m ** 2)\n"
                    "    return round(bmi, 1)\n"
                    "\n"
                    "print(calculate_bmi(70, 175))  # 22.9"
                ),
            },
            "**자료구조**: 리스트(순서 있음, 변경 가능), 튜플(순서 있음, 변경 불가), 딕셔너리(키-값 쌍), 집합(중복 없음).",
            {
                "type": "table",
                "headers": ["자료구조", "생성", "특징", "대표 메서드"],
                "rows": [
                    ["list", "[1, 2, 3]", "순서 O, 중복 O, 변경 O", "append, pop, sort"],
                    ["tuple", "(1, 2, 3)", "순서 O, 중복 O, 변경 X", "count, index"],
                    ["dict", "{'a': 1}", "키-값 쌍, 순서 O(3.7+)", "get, keys, values, items"],
                    ["set", "{1, 2, 3}", "순서 X, 중복 X, 변경 O", "add, remove, union, intersection"],
                ],
            },
            {
                "type": "note",
                "text": "이 중 하나라도 잘 기억나지 않는다면, Vol.1 해당 챕터를 10분만 복습하고 오세요. 기초가 흔들리면 심화 학습이 어렵습니다.",
            },
        ],
    }


def _section_vol2_preview():
    """섹션 2: Vol.2에서 배울 내용 미리보기."""
    return {
        "title": "Vol.2 미리보기 — 앞으로 배울 것들",
        "content": [
            "Vol.2는 Python을 '쓸 줄 아는 수준'에서 '제대로 설계할 줄 아는 수준'으로 끌어올립니다. 각 주제가 왜 필요한지 먼저 이해하면 학습 동기가 높아집니다.",
            {
                "type": "flow_diagram",
                "nodes": [
                    "Ch1: 클래스와 객체",
                    "→ Ch2: 상속과 다형성",
                    "→ Ch3: 예외처리",
                    "→ Ch4: 파일 입출력",
                    "→ Ch5: 정규식",
                    "→ Ch6: 이터레이터/제너레이터",
                    "→ Ch7: 데코레이터",
                    "→ Ch8: 종합 프로젝트",
                ],
                "note": "Vol.2 학습 경로 — 앞 챕터가 뒷 챕터의 기반이 됩니다",
            },
            {
                "type": "table",
                "headers": ["챕터", "핵심 개념", "실생활 비유", "활용 예시"],
                "rows": [
                    ["Ch1: 클래스", "class, __init__, self", "설계도 → 실제 건물", "학생 관리 시스템"],
                    ["Ch2: 상속", "inheritance, super(), MRO", "부모 → 자식 유전", "도형 계층 구조"],
                    ["Ch3: 예외처리", "try/except/finally", "안전망/보험", "파일 읽기 오류 처리"],
                    ["Ch4: 파일 I/O", "open, read, write, with", "서랍장에 데이터 보관", "성적 파일 저장/불러오기"],
                    ["Ch5: 정규식", "re 모듈, 패턴 매칭", "텍스트 속 보물 찾기", "이메일/전화번호 검증"],
                    ["Ch6: 이터레이터", "iter, next, yield", "컨베이어 벨트", "대용량 로그 처리"],
                    ["Ch7: 데코레이터", "@함수, 고차함수", "선물 포장지", "실행시간 측정, 로그"],
                ],
            },
            {
                "type": "analogy",
                "text": (
                    "Vol.1이 '단어와 문법'을 배우는 과정이었다면, Vol.2는 '문단과 에세이'를 쓰는 법을 배우는 과정입니다. "
                    "단어(변수, 함수)를 알아도 좋은 글(프로그램)을 쓰려면 구조와 흐름을 설계하는 법을 알아야 합니다. "
                    "OOP는 그 구조를 잡는 핵심 도구입니다."
                ),
            },
            {
                "type": "tip",
                "text": "각 챕터를 배울 때 '이걸 왜 쓰는가?'를 먼저 이해하세요. 군에서도 '왜 이 작전을 수행하는가'를 모르면 응용이 안 되듯, 개념의 목적을 알아야 응용할 수 있습니다.",
            },
        ],
    }


def _section_dev_environment():
    """섹션 3: 개발 환경 점검."""
    return {
        "title": "개발 환경 점검",
        "content": [
            "Python 심화 학습을 위해 개발 환경을 최신 상태로 점검합니다. 환경 문제로 인한 시간 낭비를 미리 방지합니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 터미널(명령 프롬프트)에서 실행하는 환경 점검 명령어\n"
                    "\n"
                    "# 1. Python 버전 확인 (3.12 이상 권장)\n"
                    "# $ python --version\n"
                    "# Python 3.12.2\n"
                    "\n"
                    "# 2. pip 버전 확인 및 업그레이드\n"
                    "# $ pip --version\n"
                    "# $ pip install --upgrade pip\n"
                    "\n"
                    "# 3. 설치된 패키지 목록 확인\n"
                    "# $ pip list\n"
                    "\n"
                    "# 4. Python 인터프리터에서 버전 상세 확인\n"
                    "import sys\n"
                    "print(sys.version)        # 3.12.2 (main, ...) [GCC ...]\n"
                    "print(sys.version_info)   # sys.version_info(major=3, minor=12, ...)"
                ),
            },
            {
                "type": "table",
                "headers": ["VS Code 확장", "역할", "설치 방법"],
                "rows": [
                    ["Pylance", "타입 검사, 자동 완성, 인텔리센스", "Extensions → 'Pylance' 검색"],
                    ["autopep8", "PEP 8 자동 포맷팅", "Extensions → 'autopep8' 검색"],
                    ["Python (Microsoft)", "기본 Python 지원", "Extensions → 'Python' 검색"],
                    ["indent-rainbow", "들여쓰기 시각화", "Extensions → 'indent-rainbow' 검색"],
                    ["GitLens", "Git 히스토리 시각화", "Extensions → 'GitLens' 검색"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# VS Code settings.json 권장 설정\n"
                    "# (Ctrl+Shift+P → 'Open User Settings (JSON)')\n"
                    "{\n"
                    '    "editor.formatOnSave": true,\n'
                    '    "[python]": {\n'
                    '        "editor.defaultFormatter": "ms-python.autopep8"\n'
                    "    },\n"
                    '    "python.languageServer": "Pylance",\n'
                    '    "editor.rulers": [79],\n'
                    '    "editor.tabSize": 4\n'
                    "}"
                ),
            },
            {
                "type": "warning",
                "text": "Python 2.x는 2020년에 공식 지원이 종료되었습니다. `python` 명령이 Python 2를 가리킨다면 `python3`을 사용하거나 기본 Python을 3.x로 변경하세요.",
            },
            {
                "type": "tip",
                "text": "프로젝트마다 가상환경(venv)을 사용하면 패키지 충돌을 방지할 수 있습니다. `python -m venv .venv` → `.venv\\Scripts\\activate` (Windows) 또는 `source .venv/bin/activate` (Mac/Linux).",
            },
        ],
    }


def _section_pep8_style():
    """섹션 4: 코딩 스타일 가이드 PEP 8."""
    return {
        "title": "PEP 8 코딩 스타일 가이드",
        "content": [
            "PEP 8은 Python 코드 작성 규칙을 정의한 공식 문서입니다. 팀 협업과 코드 품질을 위해 반드시 익혀두어야 합니다.",
            {
                "type": "analogy",
                "text": (
                    "군에서 규정된 복장 규정이 있듯이, 프로그래밍에도 코드 작성 규정이 있습니다. "
                    "복장이 통일되면 팀원을 한눈에 알아볼 수 있듯이, "
                    "PEP 8을 따르면 누가 작성한 코드든 쉽게 읽고 이해할 수 있습니다."
                ),
            },
            {
                "type": "table",
                "headers": ["항목", "규칙", "나쁜 예", "좋은 예"],
                "rows": [
                    ["들여쓰기", "공백 4칸 (탭 X)", "  x = 1 (2칸)", "    x = 1 (4칸)"],
                    ["변수/함수명", "소문자_언더스코어", "myName, MyName", "my_name"],
                    ["클래스명", "대문자로 시작 (CamelCase)", "my_class, myclass", "MyClass"],
                    ["상수", "대문자_언더스코어", "maxRetry, Max_retry", "MAX_RETRY"],
                    ["줄 길이", "최대 79자", "매우 긴 한 줄 코드...", "줄 바꿈 사용"],
                    ["공백", "연산자 양옆에 1칸", "x=1+2", "x = 1 + 2"],
                    ["빈 줄", "최상위 함수/클래스: 2줄", "붙어있는 함수들", "함수 사이 2줄 빈 줄"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── PEP 8 위반 예시 (나쁜 코드) ──\n"
                    "def CalcArea(W,H):  # 함수명은 소문자, 인수 사이 공백 필요\n"
                    "  area=W*H          # 들여쓰기 2칸, 연산자 주변 공백 없음\n"
                    "  return area\n"
                    "x=CalcArea(3,5)    # 호출 시 인수 사이 공백 없음\n"
                    "print(x)\n"
                    "\n"
                    "\n"
                    "# ── PEP 8 준수 예시 (좋은 코드) ──\n"
                    "def calculate_area(width: float, height: float) -> float:\n"
                    "    \"\"\"직사각형의 넓이를 계산한다.\"\"\"\n"
                    "    area = width * height  # 4칸 들여쓰기, 연산자 양옆 공백\n"
                    "    return area\n"
                    "\n"
                    "\n"
                    "result = calculate_area(3, 5)  # 함수 사이 빈 줄 2개\n"
                    "print(result)  # 15"
                ),
            },
            {
                "type": "note",
                "text": "autopep8 확장을 설치하고 '저장 시 자동 포맷팅'을 설정하면 대부분의 PEP 8 규칙을 자동으로 지킬 수 있습니다. 처음에는 규칙이 많아 보이지만 2주 후에는 자연스럽게 몸에 배입니다.",
            },
        ],
    }


def _section_docstring():
    """섹션 5: 타입 힌트와 docstring."""
    return {
        "title": "타입 힌트와 docstring — 자기 자신을 위한 문서",
        "content": [
            "타입 힌트(type hint)와 docstring은 코드의 '사용 설명서'입니다. 남을 위한 것이기도 하지만, 6개월 후의 자신을 위한 것이기도 합니다.",
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── 타입 힌트 기본 문법 ──\n"
                    "def greet(name: str, count: int = 1) -> str:\n"
                    "    \"\"\"인사 메시지를 반환한다.\"\"\"\n"
                    "    return f'안녕하세요, {name}!' * count\n"
                    "\n"
                    "# 타입 힌트의 장점: IDE가 자동완성과 오류를 미리 감지해줌\n"
                    "message: str = greet('홍길동', 2)\n"
                    "print(message)  # 안녕하세요, 홍길동!안녕하세요, 홍길동!"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# ── docstring 3가지 스타일 ──\n"
                    "\n"
                    "# 1. 한 줄 docstring (간단한 함수)\n"
                    "def double(x: int) -> int:\n"
                    "    \"\"\"입력값의 2배를 반환한다.\"\"\"\n"
                    "    return x * 2\n"
                    "\n"
                    "\n"
                    "# 2. Google 스타일 (Vol.2에서 사용할 형식)\n"
                    "def calculate_grade(score: int) -> str:\n"
                    "    \"\"\"점수에 따른 학점을 반환한다.\n"
                    "\n"
                    "    Args:\n"
                    "        score: 시험 점수 (0~100)\n"
                    "\n"
                    "    Returns:\n"
                    "        학점 문자열 ('A', 'B', 'C', 'D', 'F')\n"
                    "\n"
                    "    Raises:\n"
                    "        ValueError: 점수가 0~100 범위를 벗어난 경우\n"
                    "\n"
                    "    Examples:\n"
                    "        >>> calculate_grade(95)\n"
                    "        'A'\n"
                    "        >>> calculate_grade(55)\n"
                    "        'F'\n"
                    "    \"\"\"\n"
                    "    if not 0 <= score <= 100:\n"
                    "        raise ValueError(f'점수는 0~100이어야 합니다. 입력값: {score}')\n"
                    "    if score >= 90:\n"
                    "        return 'A'\n"
                    "    elif score >= 80:\n"
                    "        return 'B'\n"
                    "    elif score >= 70:\n"
                    "        return 'C'\n"
                    "    elif score >= 60:\n"
                    "        return 'D'\n"
                    "    return 'F'"
                ),
            },
            {
                "type": "tip",
                "text": "VS Code에서 함수 위에 커서를 놓으면 docstring이 팝업으로 표시됩니다. docstring을 잘 작성하면 별도 문서 없이도 코드 사용법을 바로 알 수 있습니다.",
            },
            {
                "type": "note",
                "text": "타입 힌트는 실행 시 오류를 발생시키지 않습니다(Python은 동적 타입 언어). 하지만 Pylance 같은 정적 분석 도구가 타입 오류를 미리 감지해주므로 실수를 크게 줄일 수 있습니다.",
            },
            {
                "type": "bullet_list",
                "items": [
                    "모든 함수에 docstring 작성: 목적 1줄 + Args + Returns (3줄 이상 함수)",
                    "타입 힌트: 매개변수와 반환값에 항상 표기",
                    "클래스 docstring: 클래스의 역할과 주요 속성 설명",
                    "모듈 docstring: 파일 첫 줄에 모듈 목적 작성",
                ],
            },
        ],
    }
