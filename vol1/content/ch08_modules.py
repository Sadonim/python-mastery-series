"""Chapter 8: 모듈과 패키지 — 코드를 조직하는 기술"""


def get_chapter():
    return {
        "number": 8,
        "title": "모듈과 패키지",
        "subtitle": "코드를 조직하는 기술",
        "big_picture": (
            "코드가 길어지면 하나의 파일에 모든 것을 담기 어렵습니다. "
            "모듈과 패키지를 사용하면 코드를 기능별로 분리하고, "
            "다른 사람이 만든 코드를 가져다 쓸 수 있습니다. "
            "이것은 혼자 모든 부품을 만드는 대신 전문 업체의 부품을 조립하는 것과 같습니다."
        ),
        "sections": [
            # ── 섹션 1: import의 동작 원리 ──────────────
            {
                "title": "import의 동작 원리",
                "content": [
                    "Python에서 `import`는 다른 파일(모듈)의 코드를 "
                    "현재 파일에서 사용할 수 있게 가져오는 명령입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "import는 도서관에서 책을 빌려오는 것과 같습니다. "
                            "직접 모든 내용을 외우는 대신, "
                            "필요한 책(모듈)을 빌려와서 참고합니다."
                        ),
                    },
                    {"type": "heading", "text": "import 기본 형태"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 방법 1: 모듈 전체 가져오기\n"
                            "import math\n"
                            "print(math.sqrt(16))   # 4.0\n"
                            "print(math.pi)         # 3.141592653589793\n\n"
                            "# 방법 2: 특정 기능만 가져오기\n"
                            "from math import sqrt, pi\n"
                            "print(sqrt(16))        # 4.0 (math. 없이 바로 사용)\n"
                            "print(pi)              # 3.141592653589793\n\n"
                            "# 방법 3: 별칭(alias) 사용\n"
                            "import datetime as dt\n"
                            "오늘 = dt.date.today()\n"
                            "print(오늘)  # 2026-03-27"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "from math import * 처럼 전부 가져오는 것은 피하세요. "
                            "어떤 이름이 어디서 왔는지 알 수 없어서 "
                            "코드를 읽기 어려워지고, 이름 충돌이 발생할 수 있습니다."
                        ),
                    },
                    {"type": "heading", "text": "__name__ == '__main__' 패턴"},
                    "Python 파일은 직접 실행할 수도 있고, "
                    "다른 파일에서 import할 수도 있습니다. "
                    "이 두 경우를 구분하는 패턴이 `__name__` 검사입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 계산기.py\n"
                            "def 더하기(a, b):\n"
                            "    return a + b\n\n"
                            "def 빼기(a, b):\n"
                            "    return a - b\n\n\n"
                            "# 이 부분은 직접 실행할 때만 작동합니다\n"
                            "if __name__ == '__main__':\n"
                            "    # 테스트 코드\n"
                            "    print(더하기(3, 5))  # 8\n"
                            "    print(빼기(10, 4))   # 6"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["실행 방식", "__name__ 값", "테스트 코드"],
                        "rows": [
                            ["직접 실행 (python 계산기.py)", "__main__", "실행됨"],
                            ["import로 가져올 때 (import 계산기)", "계산기 (모듈 이름)", "실행 안 됨"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "모듈을 만들 때 항상 if __name__ == '__main__': "
                            "블록 안에 테스트 코드를 넣는 습관을 들이세요. "
                            "이렇게 하면 모듈로 사용될 때 불필요한 코드가 실행되지 않습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 표준 라이브러리 맛보기 ──────────
            {
                "title": "표준 라이브러리 맛보기",
                "content": [
                    "Python은 '배터리 포함(batteries included)' 철학으로 유명합니다. "
                    "설치 없이 바로 쓸 수 있는 수백 개의 모듈이 표준 라이브러리에 포함되어 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "표준 라이브러리는 스위스 군용 칼과 같습니다. "
                            "칼(Python)을 사면 가위, 드라이버, 병따개 등 "
                            "다양한 도구가 이미 내장되어 있습니다."
                        ),
                    },
                    {"type": "heading", "text": "os / pathlib — 파일과 경로"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import os\n"
                            "from pathlib import Path\n\n"
                            "# os: 운영체제 기능\n"
                            "print(os.getcwd())              # 현재 작업 디렉토리\n"
                            "print(os.listdir('.'))           # 현재 디렉토리 파일 목록\n\n"
                            "# pathlib: 경로를 객체로 다루기 (더 현대적)\n"
                            "경로 = Path.home() / 'Documents' / 'report.txt'\n"
                            "print(경로)           # /Users/user/Documents/report.txt\n"
                            "print(경로.suffix)    # .txt\n"
                            "print(경로.stem)      # report"
                        ),
                    },
                    {"type": "heading", "text": "random — 무작위"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import random\n\n"
                            "print(random.randint(1, 10))          # 1~10 사이 랜덤 정수\n"
                            "print(random.choice(['가위', '바위', '보']))  # 랜덤 선택\n"
                            "목록 = [1, 2, 3, 4, 5]\n"
                            "random.shuffle(목록)                   # 섞기 (원본 변경)\n"
                            "print(목록)"
                        ),
                    },
                    {"type": "heading", "text": "datetime — 날짜와 시간"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from datetime import datetime, timedelta\n\n"
                            "지금 = datetime.now()\n"
                            "print(지금)                                # 2026-03-27 14:30:00.123456\n"
                            "print(지금.strftime('%Y년 %m월 %d일'))      # 2026년 03월 27일\n\n"
                            "# 날짜 연산\n"
                            "일주일_후 = 지금 + timedelta(days=7)\n"
                            "print(일주일_후.strftime('%Y-%m-%d'))       # 2026-04-03"
                        ),
                    },
                    {"type": "heading", "text": "json — 데이터 교환 형식"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n\n"
                            "# 딕셔너리 → JSON 문자열\n"
                            "데이터 = {'이름': '철수', '나이': 20, '취미': ['독서', '코딩']}\n"
                            "json_문자열 = json.dumps(데이터, ensure_ascii=False, indent=2)\n"
                            "print(json_문자열)\n\n"
                            "# JSON 문자열 → 딕셔너리\n"
                            "복원 = json.loads(json_문자열)\n"
                            "print(복원['이름'])  # 철수"
                        ),
                    },
                    {"type": "heading", "text": "math / sys"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import math\n"
                            "import sys\n\n"
                            "# math: 수학 함수\n"
                            "print(math.ceil(3.2))    # 4 (올림)\n"
                            "print(math.floor(3.8))   # 3 (내림)\n"
                            "print(math.gcd(12, 8))   # 4 (최대공약수)\n\n"
                            "# sys: 시스템 정보\n"
                            "print(sys.version)       # Python 버전\n"
                            "print(sys.platform)      # 운영체제 (darwin, linux, win32)"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["모듈", "용도", "주요 기능"],
                        "rows": [
                            ["os", "운영체제 인터페이스", "getcwd, listdir, environ"],
                            ["pathlib", "경로 처리 (객체지향)", "Path, suffix, stem"],
                            ["random", "무작위 생성", "randint, choice, shuffle"],
                            ["datetime", "날짜/시간", "now, strftime, timedelta"],
                            ["json", "JSON 처리", "dumps, loads, dump, load"],
                            ["math", "수학 함수", "sqrt, pi, ceil, floor"],
                            ["sys", "시스템 정보", "version, platform, argv"],
                        ],
                    },
                ],
            },
            # ── 섹션 3: pip와 PyPI ──────────────────────
            {
                "title": "pip와 PyPI",
                "content": [
                    "표준 라이브러리만으로 부족할 때, "
                    "전 세계 개발자가 만든 패키지를 `pip`로 설치할 수 있습니다. "
                    "이 패키지들은 **PyPI(Python Package Index)**에 등록되어 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "PyPI는 앱 스토어와 같습니다. "
                            "필요한 기능(앱)을 검색해서 pip install(다운로드)하면 "
                            "바로 사용할 수 있습니다. "
                            "50만 개 이상의 패키지가 등록되어 있습니다."
                        ),
                    },
                    {"type": "heading", "text": "pip 기본 명령어"},
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 패키지 설치\n"
                            "pip install requests\n\n"
                            "# 특정 버전 설치\n"
                            "pip install requests==2.31.0\n\n"
                            "# 최소 버전 지정\n"
                            "pip install 'requests>=2.28.0'\n\n"
                            "# 패키지 업그레이드\n"
                            "pip install --upgrade requests\n\n"
                            "# 패키지 제거\n"
                            "pip uninstall requests\n\n"
                            "# 설치된 패키지 목록\n"
                            "pip list\n\n"
                            "# 설치된 패키지를 파일로 저장\n"
                            "pip freeze > requirements.txt"
                        ),
                    },
                    {"type": "heading", "text": "requirements.txt"},
                    "프로젝트에서 필요한 패키지 목록을 `requirements.txt`에 기록합니다. "
                    "다른 사람이 같은 환경을 쉽게 재현할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "text",
                        "code": (
                            "# requirements.txt 예시\n"
                            "requests==2.31.0\n"
                            "pandas>=2.0.0\n"
                            "numpy>=1.24.0,<2.0.0\n"
                            "flask~=3.0.0"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# requirements.txt의 모든 패키지 한 번에 설치\n"
                            "pip install -r requirements.txt"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["버전 지정", "의미", "예시"],
                        "rows": [
                            ["==2.31.0", "정확히 이 버전", "고정 (배포용)"],
                            [">=2.28.0", "이 버전 이상", "최소 요구"],
                            ["<2.0.0", "이 버전 미만", "호환성 상한"],
                            ["~=3.0.0", "3.0.x 범위", "패치만 허용"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "MLOps에서 자주 쓰는 패키지: "
                            "numpy(수치 계산), pandas(데이터 분석), "
                            "scikit-learn(머신러닝), matplotlib(시각화), "
                            "requests(HTTP 통신), flask/fastapi(웹 서버)."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 가상환경 (venv) 기초 ────────────
            {
                "title": "가상환경 (venv) 기초",
                "content": [
                    "가상환경은 프로젝트마다 독립된 Python 패키지 공간을 만드는 기술입니다. "
                    "프로젝트 A는 requests 2.28, 프로젝트 B는 requests 2.31이 "
                    "필요할 때, 각각의 가상환경에서 다른 버전을 사용할 수 있습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "가상환경은 각 프로젝트의 전용 작업실과 같습니다. "
                            "작업실마다 독립된 도구 세트가 있어서, "
                            "한 작업실에서 도구를 바꿔도 다른 작업실에 영향을 주지 않습니다."
                        ),
                    },
                    {"type": "heading", "text": "왜 가상환경이 필요한가?"},
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "프로젝트 A", "sub": "requests 2.28"},
                            {"label": "가상환경 (.venv)", "color": "#03B26C"},
                            {"label": "프로젝트 B", "sub": "requests 2.31"},
                        ],
                        "note": "각 프로젝트마다 독립된 가상환경을 사용하면 패키지 충돌이 없습니다",
                    },
                    {"type": "heading", "text": "가상환경 사용법"},
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 1. 가상환경 생성 (프로젝트 폴더에서)\n"
                            "python -m venv .venv\n\n"
                            "# 2. 활성화\n"
                            "# macOS / Linux:\n"
                            "source .venv/bin/activate\n"
                            "# Windows:\n"
                            "# .venv\\Scripts\\activate\n\n"
                            "# 3. 패키지 설치 (가상환경 안에서)\n"
                            "pip install requests pandas\n\n"
                            "# 4. 작업 완료 후 비활성화\n"
                            "deactivate"
                        ),
                    },
                    {
                        "type": "numbered_list",
                        "items": [
                            "프로젝트 폴더로 이동합니다",
                            "python -m venv .venv 으로 가상환경을 생성합니다",
                            "source .venv/bin/activate 로 활성화합니다",
                            "pip install 로 필요한 패키지를 설치합니다",
                            "pip freeze > requirements.txt 로 패키지 목록을 저장합니다",
                            "작업이 끝나면 deactivate 로 비활성화합니다",
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            ".venv 폴더는 Git에 올리면 안 됩니다. "
                            ".gitignore 파일에 .venv/를 추가하세요. "
                            "대신 requirements.txt를 공유하면 "
                            "누구든 같은 환경을 재현할 수 있습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# .gitignore 에 추가할 내용\n"
                            "# echo '.venv/' >> .gitignore\n\n"
                            "# 새 환경에서 프로젝트 시작할 때\n"
                            "python -m venv .venv\n"
                            "source .venv/bin/activate\n"
                            "pip install -r requirements.txt"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "프로젝트를 시작할 때 가장 먼저 할 일: "
                            "폴더 만들기 → 가상환경 생성 → 활성화 → 패키지 설치. "
                            "이 순서를 습관으로 만드세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 나만의 모듈 만들기 ──────────────
            {
                "title": "나만의 모듈 만들기",
                "content": [
                    "Python 파일 하나가 곧 하나의 모듈입니다. "
                    "함수나 클래스를 별도 파일로 분리하면 재사용하기 쉬워집니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "모듈은 레고 블록과 같습니다. "
                            "각 블록(모듈)은 독립적인 기능을 가지고 있고, "
                            "필요한 블록을 조합해서 원하는 구조물(프로그램)을 만듭니다."
                        ),
                    },
                    {"type": "heading", "text": "파일 분리 예제"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# --- 파일: 수학_도구.py ---\n"
                            "\"\"\"기본 수학 유틸리티 모듈\"\"\"\n\n"
                            "PI = 3.141592653589793\n\n\n"
                            "def 원의_넓이(반지름):\n"
                            "    \"\"\"원의 넓이를 계산합니다.\"\"\"\n"
                            "    if 반지름 < 0:\n"
                            "        raise ValueError('반지름은 0 이상이어야 합니다')\n"
                            "    return PI * 반지름 ** 2\n\n\n"
                            "def 원의_둘레(반지름):\n"
                            "    \"\"\"원의 둘레를 계산합니다.\"\"\"\n"
                            "    if 반지름 < 0:\n"
                            "        raise ValueError('반지름은 0 이상이어야 합니다')\n"
                            "    return 2 * PI * 반지름"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# --- 파일: main.py ---\n"
                            "from 수학_도구 import 원의_넓이, 원의_둘레, PI\n\n"
                            "print(f'원주율: {PI}')\n"
                            "print(f'반지름 5인 원의 넓이: {원의_넓이(5):.2f}')\n"
                            "print(f'반지름 5인 원의 둘레: {원의_둘레(5):.2f}')"
                        ),
                    },
                    {"type": "heading", "text": "패키지 구조"},
                    "여러 모듈을 폴더로 묶으면 **패키지**가 됩니다. "
                    "폴더 안에 `__init__.py` 파일이 있으면 Python이 패키지로 인식합니다.",
                    {
                        "type": "diagram",
                        "text": (
                            "my_utils/               ← 패키지 (폴더)\n"
                            "├── __init__.py         ← 패키지 초기화 파일\n"
                            "├── 수학_도구.py         ← 모듈\n"
                            "├── 문자열_도구.py       ← 모듈\n"
                            "└── 파일_도구.py         ← 모듈"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# --- 파일: my_utils/__init__.py ---\n"
                            "# 패키지에서 바로 쓸 수 있게 주요 기능 노출\n"
                            "from .수학_도구 import 원의_넓이, 원의_둘레\n"
                            "from .문자열_도구 import 단어_세기\n\n"
                            "__version__ = '0.1.0'"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 패키지 사용하기\n"
                            "from my_utils import 원의_넓이, 단어_세기\n\n"
                            "print(원의_넓이(3))\n"
                            "print(단어_세기('안녕하세요 반갑습니다'))"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python 3.3부터 __init__.py가 없어도 "
                            "패키지로 인식되지만(namespace package), "
                            "명시적으로 넣는 것이 권장됩니다. "
                            "빈 파일이라도 괜찮습니다."
                        ),
                    },
                    {"type": "heading", "text": "실습: 미니 유틸리티 패키지"},
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# --- 파일: mini_utils/문자열.py ---\n"
                            "\"\"\"문자열 유틸리티 모듈\"\"\"\n\n\n"
                            "def 단어_세기(텍스트):\n"
                            "    \"\"\"텍스트의 단어 수를 반환합니다.\"\"\"\n"
                            "    if not 텍스트 or not 텍스트.strip():\n"
                            "        return 0\n"
                            "    return len(텍스트.split())\n\n\n"
                            "def 회문_검사(텍스트):\n"
                            "    \"\"\"텍스트가 회문인지 확인합니다.\"\"\"\n"
                            "    정리된 = 텍스트.replace(' ', '').lower()\n"
                            "    return 정리된 == 정리된[::-1]\n\n\n"
                            "def 첫글자_대문자(텍스트):\n"
                            "    \"\"\"각 단어의 첫 글자를 대문자로 바꿉니다.\"\"\"\n"
                            "    return ' '.join(\n"
                            "        단어.capitalize() for 단어 in 텍스트.split()\n"
                            "    )"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# --- 파일: mini_utils/숫자.py ---\n"
                            "\"\"\"숫자 유틸리티 모듈\"\"\"\n\n\n"
                            "def 짝수_판별(n):\n"
                            "    \"\"\"짝수이면 True를 반환합니다.\"\"\"\n"
                            "    return n % 2 == 0\n\n\n"
                            "def 범위_제한(값, 최소, 최대):\n"
                            "    \"\"\"값을 최소~최대 범위로 제한합니다.\"\"\"\n"
                            "    return max(최소, min(값, 최대))\n\n\n"
                            "def 평균(숫자들):\n"
                            "    \"\"\"숫자 리스트의 평균을 반환합니다.\"\"\"\n"
                            "    if not 숫자들:\n"
                            "        raise ValueError('빈 리스트의 평균을 구할 수 없습니다')\n"
                            "    return sum(숫자들) / len(숫자들)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# --- 파일: mini_utils/__init__.py ---\n"
                            "\"\"\"미니 유틸리티 패키지\"\"\"\n\n"
                            "from .문자열 import 단어_세기, 회문_검사, 첫글자_대문자\n"
                            "from .숫자 import 짝수_판별, 범위_제한, 평균\n\n"
                            "__version__ = '0.1.0'\n"
                            "__all__ = [\n"
                            "    '단어_세기', '회문_검사', '첫글자_대문자',\n"
                            "    '짝수_판별', '범위_제한', '평균',\n"
                            "]"
                        ),
                    },
                ],
            },
            # ── 섹션 6: 모듈 설계 원칙 ──────────────────
            {
                "title": "모듈 설계 원칙",
                "content": [
                    "모듈을 잘 나누면 코드를 이해하기 쉽고, "
                    "수정할 때 영향 범위가 줄어들며, 재사용성이 높아집니다.",
                    {"type": "heading", "text": "원칙 1: 단일 책임"},
                    "하나의 모듈은 하나의 주제만 담당해야 합니다.",
                    {
                        "type": "bullet_list",
                        "items": [
                            "수학_도구.py → 수학 관련 함수만",
                            "파일_도구.py → 파일 입출력 관련 함수만",
                            "검증_도구.py → 입력 검증 관련 함수만",
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 나쁜 예: 한 모듈에 여러 책임\n"
                            "# utils.py 안에 수학, 문자열, 파일, 검증 함수가 뒤섞임\n\n"
                            "# 좋은 예: 주제별 분리\n"
                            "# math_utils.py   → 수학 함수\n"
                            "# string_utils.py → 문자열 함수\n"
                            "# file_utils.py   → 파일 함수\n"
                            "# validators.py   → 검증 함수"
                        ),
                    },
                    {"type": "heading", "text": "원칙 2: 순환 import 피하기"},
                    "모듈 A가 B를 import하고, B가 다시 A를 import하면 "
                    "순환 참조가 발생합니다. 이를 피해야 합니다.",
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "모듈 A"},
                            {"label": "모듈 C (공통)", "color": "#03B26C"},
                            {"label": "모듈 B"},
                        ],
                        "note": "순환 import를 피하려면 공통 부분을 별도 모듈로 분리합니다",
                    },
                    {
                        "type": "warning",
                        "text": (
                            "순환 import가 발생하면 ImportError가 나거나, "
                            "None 값을 참조하는 버그가 생길 수 있습니다. "
                            "공통으로 쓰이는 부분을 별도 모듈로 분리하세요."
                        ),
                    },
                    {"type": "heading", "text": "원칙 3: 네이밍 컨벤션"},
                    {
                        "type": "table",
                        "headers": ["대상", "규칙", "예시"],
                        "rows": [
                            ["모듈/패키지", "소문자, 밑줄", "my_module, utils"],
                            ["함수/변수", "소문자, 밑줄 (snake_case)", "calculate_area"],
                            ["클래스", "대문자 시작 (PascalCase)", "StudentInfo"],
                            ["상수", "전부 대문자, 밑줄", "MAX_RETRY, PI"],
                            ["비공개", "밑줄 시작", "_internal_func"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 네이밍 예시\n"
                            "MAX_RETRY = 3             # 상수\n"
                            "DEFAULT_TIMEOUT = 30      # 상수\n\n\n"
                            "def calculate_average(numbers):  # 함수: snake_case\n"
                            "    \"\"\"숫자 리스트의 평균을 계산합니다.\"\"\"\n"
                            "    return sum(numbers) / len(numbers)\n\n\n"
                            "def _validate_input(value):      # 비공개 함수: 밑줄 시작\n"
                            "    \"\"\"내부 검증용 함수 (외부 사용 비권장).\"\"\"\n"
                            "    return value is not None"
                        ),
                    },
                    {"type": "heading", "text": "모듈 설계 체크리스트"},
                    {
                        "type": "numbered_list",
                        "items": [
                            "모듈 이름이 내용을 잘 설명하는가?",
                            "한 모듈이 하나의 주제만 다루는가?",
                            "순환 import가 없는가?",
                            "공개 함수와 비공개 함수가 구분되어 있는가?",
                            "모듈 docstring이 작성되어 있는가?",
                            "상수는 대문자로, 함수는 snake_case로 되어 있는가?",
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "코드를 작성할 때 '이 파일이 200줄을 넘는가?'를 "
                            "자주 확인하세요. 넘긴다면 분리할 시점입니다. "
                            "작은 모듈 여러 개가 큰 모듈 하나보다 항상 낫습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "import 문은 파일 맨 위에 모아두세요. "
            "표준 라이브러리 → 서드파티 → 내 모듈 순서로 그룹핑합니다.",
            "from module import * 는 사용하지 마세요. "
            "이름 충돌과 가독성 문제가 생깁니다.",
            "프로젝트를 시작하면 가장 먼저 가상환경을 만드세요. "
            "시스템 Python을 오염시키지 않는 좋은 습관입니다.",
            "requirements.txt는 항상 최신 상태로 유지하세요. "
            "패키지를 추가하거나 제거할 때마다 갱신합니다.",
            "모듈 이름에 하이픈(-)을 쓰지 마세요. "
            "Python에서 import할 수 없습니다. 밑줄(_)을 사용하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 import 방법으로 올바르지 않은 것은?",
                "choices": [
                    "A) import math",
                    "B) from math import sqrt",
                    "C) import math as m",
                    "D) import math.sqrt",
                ],
                "answer": "D",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "가상환경이 필요한 이유로 가장 적절한 것은?"
                ),
                "choices": [
                    "A) Python 실행 속도를 높이기 위해",
                    "B) 프로젝트별 패키지 버전을 독립적으로 관리하기 위해",
                    "C) 코드를 암호화하기 위해",
                    "D) 인터넷 없이 코딩하기 위해",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "if __name__ == '__main__':의 역할은?"
                ),
                "choices": [
                    "A) 파일을 읽기 전용으로 만든다",
                    "B) 해당 파일이 직접 실행될 때만 블록 안의 코드를 실행한다",
                    "C) 모듈을 다른 파일에서 import할 수 없게 한다",
                    "D) Python 버전을 확인한다",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "random 모듈을 사용하여 1~45 사이의 "
                    "중복 없는 숫자 6개를 뽑아 오름차순으로 출력하는 "
                    "로또 번호 생성기를 만드세요."
                ),
                "hint": "random.sample()을 사용하면 중복 없이 뽑을 수 있습니다.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "현재 날짜를 'YYYY년 MM월 DD일 (요일)' 형식으로 출력하는 "
                    "프로그램을 datetime 모듈로 작성하세요. "
                    "요일은 한글로 출력합니다."
                ),
                "hint": (
                    "datetime.now()과 strftime()을 사용하세요. "
                    "weekday()는 0(월)~6(일)을 반환합니다."
                ),
            },
        ],
        "challenge": {
            "question": (
                "나만의 미니 유틸리티 패키지를 만드세요. "
                "패키지 이름은 my_tools이고, "
                "string_tools.py(문자열 함수 3개 이상)와 "
                "math_tools.py(수학 함수 3개 이상)를 포함합니다. "
                "__init__.py에서 주요 함수를 공개하고, "
                "별도의 test_my_tools.py에서 모든 함수를 테스트하세요."
            ),
            "hint": (
                "각 함수에 docstring을 작성하고, "
                "잘못된 입력에 대한 에러 처리도 포함하세요. "
                "__init__.py에서 __all__ 리스트를 정의하면 "
                "공개 API를 명확히 할 수 있습니다."
            ),
        },
        "summary": [
            "import로 다른 모듈의 코드를 가져와 쓸 수 있으며, "
            "import, from...import, as 세 가지 형태가 있습니다.",
            "if __name__ == '__main__': 패턴으로 "
            "직접 실행과 import를 구분합니다.",
            "Python 표준 라이브러리는 os, random, datetime, json, math 등 "
            "다양한 모듈을 기본 제공합니다.",
            "pip는 PyPI에서 외부 패키지를 설치하는 도구이며, "
            "requirements.txt로 의존성을 관리합니다.",
            "가상환경(venv)은 프로젝트별 독립 패키지 환경을 만들어 "
            "버전 충돌을 방지합니다.",
            "Python 파일 하나가 모듈이고, "
            "__init__.py를 포함한 폴더가 패키지입니다.",
            "모듈 설계 시 단일 책임, 순환 import 방지, "
            "네이밍 컨벤션 준수가 핵심 원칙입니다.",
            "import 문은 파일 상단에 표준→서드파티→내 모듈 순서로 "
            "그룹핑하는 것이 관례입니다.",
        ],
    }
