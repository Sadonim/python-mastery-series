"""
Ch 0: 복습 & 데이터 분석 준비
Python Mastery Series Vol.3 — 데이터 분석
"""


def get_chapter():
    return {
        "number": 0,
        "title": "복습 & 데이터 분석 준비",
        "subtitle": "Vol.2 핵심 정리와 데이터 분석 환경 구축",
        "big_picture": (
            "Vol.3를 시작하기 전에 Vol.2에서 배운 핵심 개념들을 빠르게 복습하고, "
            "데이터 분석이 무엇인지, 왜 Python이 데이터 분석의 표준 언어가 되었는지 이해합니다. "
            "그리고 앞으로 사용할 핵심 패키지들을 설치하고 Jupyter Notebook 환경을 준비합니다."
        ),
        "sections": [
            {
                "title": "Vol.2 핵심 복습",
                "content": [
                    "Vol.3를 시작하기 전에 Vol.2에서 다뤘던 핵심 개념들을 빠르게 정리해봅시다. "
                    "특히 클래스, 파일 입출력, 이터레이터는 데이터 분석 코드를 작성할 때 매우 자주 등장합니다.",
                    {
                        "type": "heading",
                        "text": "OOP (객체지향 프로그래밍)",
                    },
                    "클래스는 데이터와 그 데이터를 다루는 함수를 하나로 묶는 설계도입니다. "
                    "데이터 분석에서는 데이터를 처리하는 파이프라인을 클래스로 설계할 때 자주 사용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.2 복습 — 클래스 기본 구조\n"
                            "class DataProcessor:\n"
                            "    \"\"\"데이터 처리기 예시\"\"\"\n"
                            "\n"
                            "    def __init__(self, name: str):\n"
                            "        self.name = name\n"
                            "        self._data = []  # private 속성\n"
                            "\n"
                            "    def load(self, data: list):\n"
                            "        \"\"\"데이터 로드\"\"\"\n"
                            "        self._data = data\n"
                            "        return self  # 메서드 체이닝\n"
                            "\n"
                            "    def process(self):\n"
                            "        \"\"\"데이터 처리 (서브클래스에서 오버라이드)\"\"\"\n"
                            "        return self._data\n"
                            "\n"
                            "    def __repr__(self):\n"
                            "        return f\"DataProcessor(name='{self.name}', items={len(self._data)})\"\n"
                            "\n"
                            "# 사용\n"
                            "processor = DataProcessor('판매 데이터')\n"
                            "processor.load([10, 20, 30, 40, 50])\n"
                            "print(processor)  # DataProcessor(name='판매 데이터', items=5)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "파일 입출력 (File I/O)",
                    },
                    "데이터 분석의 시작은 항상 데이터를 읽어오는 것입니다. "
                    "CSV, JSON 파일을 직접 다루는 것은 pandas를 쓰기 전에도, 쓴 후에도 여전히 중요합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.2 복습 — 파일 입출력\n"
                            "import csv\n"
                            "import json\n"
                            "\n"
                            "# CSV 읽기\n"
                            "with open('sales.csv', 'r', encoding='utf-8') as f:\n"
                            "    reader = csv.DictReader(f)\n"
                            "    rows = list(reader)\n"
                            "print(f'총 {len(rows)}행 로드')  # 예: 총 100행 로드\n"
                            "\n"
                            "# JSON 읽기\n"
                            "with open('config.json', 'r', encoding='utf-8') as f:\n"
                            "    config = json.load(f)\n"
                            "\n"
                            "# JSON 쓰기\n"
                            "result = {'총합': 1500, '평균': 75.0}\n"
                            "with open('result.json', 'w', encoding='utf-8') as f:\n"
                            "    json.dump(result, f, ensure_ascii=False, indent=2)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "이터레이터와 제너레이터",
                    },
                    "대용량 데이터를 처리할 때 제너레이터는 메모리를 절약하는 핵심 도구입니다. "
                    "파일에서 수백만 줄을 읽을 때 한 번에 메모리에 올리지 않아도 됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.2 복습 — 제너레이터\n"
                            "def read_large_csv(filepath: str):\n"
                            "    \"\"\"대용량 CSV를 한 줄씩 읽는 제너레이터\"\"\"\n"
                            "    with open(filepath, 'r', encoding='utf-8') as f:\n"
                            "        reader = csv.DictReader(f)\n"
                            "        for row in reader:\n"
                            "            yield row  # 한 행씩 반환\n"
                            "\n"
                            "# 메모리에 전체 파일을 올리지 않고 처리\n"
                            "for row in read_large_csv('big_data.csv'):\n"
                            "    # 한 번에 한 행씩 처리\n"
                            "    process_row(row)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Vol.2 내용이 잘 기억나지 않아도 괜찮습니다. "
                            "Vol.3를 진행하면서 필요한 시점에 자연스럽게 복습하게 됩니다. "
                            "다만 클래스 개념과 with 문 사용법은 미리 확인해두세요."
                        ),
                    },
                ],
            },
            {
                "title": "데이터 분석이란? 그리고 MLOps에서의 역할",
                "content": [
                    "데이터 분석은 원시 데이터(raw data)에서 의미 있는 정보를 추출하는 과정입니다. "
                    "단순히 숫자를 계산하는 것이 아니라, 비즈니스 문제를 데이터로 해석하고 "
                    "그 결과를 의사결정에 활용하는 전체 프로세스를 말합니다.",
                    {
                        "type": "flow_diagram",
                        "steps": [
                            "데이터 수집 (CSV, API, DB)",
                            "데이터 정제 (결측값, 이상값 처리)",
                            "탐색적 분석 (EDA — 패턴 발견)",
                            "시각화 (그래프, 차트)",
                            "인사이트 도출 및 보고",
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "데이터 분석 vs 머신러닝 vs MLOps",
                    },
                    {
                        "type": "table",
                        "headers": ["단계", "역할", "주요 도구"],
                        "rows": [
                            ["데이터 분석", "데이터 이해, 패턴 발견, 보고서 작성", "NumPy, Pandas, Matplotlib"],
                            ["머신러닝", "예측 모델 학습 및 평가", "scikit-learn, PyTorch, TensorFlow"],
                            ["MLOps", "모델 배포, 모니터링, 자동화 파이프라인", "MLflow, Airflow, Docker, FastAPI"],
                        ],
                    },
                    "Vol.3는 데이터 분석 단계에 집중합니다. "
                    "좋은 데이터 분석가는 머신러닝 엔지니어와 협업할 때 '데이터의 문지기' 역할을 합니다. "
                    "모델의 입력 데이터 품질을 보장하고, 모델 결과를 해석 가능하게 만드는 것이 핵심입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "데이터 분석을 요리에 비유하면: 데이터 수집은 재료 구입, "
                            "데이터 정제는 재료 손질, EDA는 재료 맛보기, "
                            "시각화는 플레이팅, 인사이트 도출은 손님에게 요리 설명하기입니다. "
                            "아무리 좋은 레시피(머신러닝 모델)도 재료 손질이 잘못되면 맛없는 요리가 됩니다."
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python이 데이터 분석의 표준 언어가 된 이유: "
                            "① 배우기 쉬운 문법, ② 풍부한 데이터 분석 생태계(NumPy/Pandas/Matplotlib), "
                            "③ 머신러닝 라이브러리와의 완벽한 연동, ④ Jupyter Notebook 환경. "
                            "R도 강력하지만, Python은 웹 개발, 자동화, API까지 하나의 언어로 처리할 수 있습니다."
                        ),
                    },
                ],
            },
            {
                "title": "필수 패키지 설치",
                "content": [
                    "Vol.3에서 사용할 핵심 패키지들을 설치합니다. "
                    "각 패키지가 어떤 역할을 하는지 이해하고 설치해봅시다.",
                    {
                        "type": "table",
                        "headers": ["패키지", "버전 (권장)", "역할"],
                        "rows": [
                            ["numpy", "≥ 1.24", "수치 연산, 다차원 배열 처리"],
                            ["pandas", "≥ 2.0", "데이터프레임 — 표 형식 데이터 처리"],
                            ["matplotlib", "≥ 3.7", "기본 시각화 (그래프, 차트)"],
                            ["seaborn", "≥ 0.12", "통계 시각화 (matplotlib 기반)"],
                            ["requests", "≥ 2.31", "HTTP 요청 — API, 웹 스크래핑"],
                            ["jupyter", "≥ 1.0", "Notebook 환경"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 가상환경 생성 (권장)\n"
                            "python3 -m venv venv\n"
                            "source venv/bin/activate  # macOS/Linux\n"
                            "# venv\\Scripts\\activate  # Windows\n"
                            "\n"
                            "# 필수 패키지 일괄 설치\n"
                            "pip install numpy pandas matplotlib seaborn requests jupyter\n"
                            "\n"
                            "# 설치 확인\n"
                            "python3 -c \"import numpy as np; print('NumPy', np.__version__)\"\n"
                            "python3 -c \"import pandas as pd; print('Pandas', pd.__version__)\"\n"
                            "python3 -c \"import matplotlib; print('Matplotlib', matplotlib.__version__)\""
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "requirements.txt로 환경 재현하기",
                    },
                    "팀 협업이나 배포 환경에서는 패키지 버전을 고정하는 것이 중요합니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 현재 설치된 패키지 목록 저장\n"
                            "pip freeze > requirements.txt\n"
                            "\n"
                            "# 다른 환경에서 동일하게 설치\n"
                            "pip install -r requirements.txt"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "시스템 Python에 직접 패키지를 설치하지 마세요. "
                            "프로젝트마다 가상환경(venv)을 만들어 독립적인 패키지 환경을 유지하세요. "
                            "나중에 패키지 버전 충돌로 인한 예상치 못한 오류를 방지할 수 있습니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 설치 검증 스크립트 — 이 코드가 오류 없이 실행되면 준비 완료!\n"
                            "import numpy as np\n"
                            "import pandas as pd\n"
                            "import matplotlib\n"
                            "import requests\n"
                            "\n"
                            "packages = {\n"
                            "    'numpy': np.__version__,\n"
                            "    'pandas': pd.__version__,\n"
                            "    'matplotlib': matplotlib.__version__,\n"
                            "    'requests': requests.__version__,\n"
                            "}\n"
                            "\n"
                            "for pkg, ver in packages.items():\n"
                            "    print(f'✓ {pkg:12s} {ver}')"
                        ),
                    },
                ],
            },
            {
                "title": "Jupyter Notebook 소개 및 설치",
                "content": [
                    "Jupyter Notebook은 코드, 텍스트, 시각화를 하나의 문서에 담을 수 있는 대화형 개발 환경입니다. "
                    "데이터 과학자들이 가장 많이 사용하는 도구 중 하나로, "
                    "코드를 셀 단위로 실행하고 결과를 즉시 확인할 수 있습니다.",
                    {
                        "type": "heading",
                        "text": "Jupyter Notebook vs JupyterLab vs VS Code Notebook",
                    },
                    {
                        "type": "table",
                        "headers": ["환경", "특징", "추천 대상"],
                        "rows": [
                            ["Jupyter Notebook", "가장 전통적, 단순한 인터페이스", "입문자, 빠른 실험"],
                            ["JupyterLab", "파일 탐색기 + 여러 Notebook 동시 작업", "중급 이상, 프로젝트 작업"],
                            ["VS Code Notebook", "에디터와 통합, 확장기능 활용 가능", "개발자 친화적"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Jupyter 설치 및 실행\n"
                            "pip install jupyter jupyterlab\n"
                            "\n"
                            "# Jupyter Notebook 실행 (브라우저 자동 열림)\n"
                            "jupyter notebook\n"
                            "\n"
                            "# JupyterLab 실행 (더 강력한 인터페이스)\n"
                            "jupyter lab\n"
                            "\n"
                            "# 특정 포트로 실행\n"
                            "jupyter notebook --port 8888"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "핵심 단축키",
                    },
                    {
                        "type": "table",
                        "headers": ["단축키", "동작", "모드"],
                        "rows": [
                            ["Shift + Enter", "셀 실행 후 다음 셀로 이동", "편집/명령"],
                            ["Ctrl + Enter", "셀 실행 (커서 유지)", "편집/명령"],
                            ["A", "위에 새 셀 추가", "명령 모드"],
                            ["B", "아래에 새 셀 추가", "명령 모드"],
                            ["DD", "셀 삭제", "명령 모드"],
                            ["M", "Markdown 셀로 변환", "명령 모드"],
                            ["Y", "Code 셀로 변환", "명령 모드"],
                            ["Esc", "편집 모드 → 명령 모드", "편집 모드"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Jupyter에서 ?를 붙이면 도움말을 볼 수 있습니다. "
                            "예: np.array? 또는 np.array?? (소스코드까지 확인). "
                            "Tab 키로 자동완성도 지원하니 적극 활용하세요."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Jupyter Magic Commands — 특별한 기능들\n"
                            "\n"
                            "# 실행 시간 측정\n"
                            "%time sum(range(1000000))\n"
                            "# CPU times: user 35.2 ms\n"
                            "\n"
                            "# 여러 번 실행해서 평균 시간 측정\n"
                            "%timeit sum(range(1000000))\n"
                            "# 35.1 ms ± 1.2 ms per loop\n"
                            "\n"
                            "# matplotlib 그래프를 Notebook 안에 표시\n"
                            "%matplotlib inline\n"
                            "\n"
                            "# 현재 디렉터리의 파일 목록\n"
                            "%ls\n"
                            "\n"
                            "# 변수 목록 확인\n"
                            "%who"
                        ),
                    },
                ],
            },
            {
                "title": "Vol.3 학습 로드맵",
                "content": [
                    "앞으로 배울 내용의 전체 구조를 먼저 파악해두면 각 챕터의 위치를 이해하는 데 도움이 됩니다.",
                    {
                        "type": "flow_diagram",
                        "steps": [
                            "Ch 1-2: NumPy — 수치 배열 연산의 기초",
                            "Ch 3-4: Pandas — 표 형식 데이터 자유자재로 다루기",
                            "Ch 5: Matplotlib / Seaborn — 데이터 시각화",
                            "Ch 6: requests — 외부 API로 실제 데이터 수집",
                            "Ch 7: BeautifulSoup — 웹 스크래핑",
                            "Ch 8: 데이터 파이프라인 — 수집→정제→분석→저장 자동화",
                            "Ch 9: 종합 프로젝트 — 실제 데이터로 EDA 보고서 작성",
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "각 챕터는 독립적으로 읽을 수 있지만, Ch 1-2(NumPy)를 이해해야 "
                            "Ch 3-4(Pandas)가 쉬워집니다. NumPy는 Pandas의 기반 엔진이기 때문입니다. "
                            "순서대로 학습하는 것을 강력히 권장합니다."
                        ),
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "각 챕터에는 실습 예제와 연습문제가 포함되어 있습니다.",
                            "코드를 직접 실행해보는 것이 가장 효과적인 학습 방법입니다.",
                            "Jupyter Notebook에서 각 코드 블록을 실행하며 결과를 확인하세요.",
                            "챕터 끝의 도전 과제는 실제 데이터를 사용한 응용 문제입니다.",
                        ],
                    },
                ],
            },
        ],
        "practical_tips": [
            "가상환경(venv)은 항상 프로젝트별로 생성하세요. 패키지 버전 충돌의 99%를 예방합니다.",
            "Jupyter Notebook에서 셀 실행 순서가 결과에 영향을 줍니다. "
            "Kernel → Restart & Run All로 항상 처음부터 실행해서 검증하세요.",
            "pip install 전에 pip install --upgrade pip으로 pip를 최신 버전으로 유지하세요.",
            "코드에 주석을 적극적으로 달아두세요. 데이터 분석 코드는 나중에 보면 "
            "무슨 의도였는지 기억이 잘 나지 않습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "Python이 데이터 분석의 표준 언어로 자리잡게 된 가장 큰 이유로 적절하지 않은 것은?",
                "choices": [
                    "NumPy, Pandas 등 강력한 데이터 분석 생태계",
                    "배우기 쉬운 문법",
                    "컴파일 언어보다 빠른 실행 속도",
                    "머신러닝 라이브러리와의 완벽한 연동",
                ],
                "answer": 2,
                "explanation": (
                    "Python은 인터프리터 언어로 C/C++ 같은 컴파일 언어보다 기본 실행 속도는 느립니다. "
                    "그러나 NumPy는 내부적으로 C로 구현되어 있어, NumPy 연산은 빠릅니다. "
                    "Python의 강점은 '속도'가 아닌 '생산성'과 '생태계'입니다."
                ),
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "Jupyter Notebook에서 현재 셀을 실행하고 커서를 그 셀에 유지하는 단축키는?",
                "choices": [
                    "Shift + Enter",
                    "Ctrl + Enter",
                    "Alt + Enter",
                    "Tab + Enter",
                ],
                "answer": 1,
                "explanation": (
                    "Ctrl + Enter는 셀을 실행하되 커서가 현재 셀에 머뭅니다. "
                    "Shift + Enter는 실행 후 다음 셀로 이동하고, "
                    "Alt + Enter는 실행 후 아래에 새 셀을 추가합니다."
                ),
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "아래 조건에 맞는 설치 검증 스크립트를 작성하세요.\n"
                    "조건:\n"
                    "① numpy, pandas, matplotlib 세 패키지를 import\n"
                    "② 각 패키지의 버전을 출력 (예: numpy: 1.24.0)\n"
                    "③ 모든 패키지가 정상 import되면 '환경 설정 완료!' 출력\n"
                    "④ ImportError 발생 시 어떤 패키지가 없는지 알려주는 에러 메시지 출력"
                ),
                "answer_code": (
                    "import sys\n"
                    "\n"
                    "required = ['numpy', 'pandas', 'matplotlib']\n"
                    "all_ok = True\n"
                    "\n"
                    "for pkg in required:\n"
                    "    try:\n"
                    "        module = __import__(pkg)\n"
                    "        print(f'{pkg}: {module.__version__}')\n"
                    "    except ImportError:\n"
                    "        print(f'오류: {pkg} 패키지가 설치되지 않았습니다.')\n"
                    "        print(f'  설치 명령: pip install {pkg}')\n"
                    "        all_ok = False\n"
                    "\n"
                    "if all_ok:\n"
                    "    print('\\n환경 설정 완료!')\n"
                    "else:\n"
                    "    print('\\n위 패키지를 설치한 후 다시 실행하세요.')\n"
                    "    sys.exit(1)"
                ),
            },
            {
                "number": 4,
                "type": "multiple_choice",
                "question": "데이터 분석 파이프라인의 일반적인 순서로 가장 올바른 것은?",
                "choices": [
                    "시각화 → 수집 → 정제 → 인사이트 도출",
                    "수집 → 정제 → 탐색적 분석(EDA) → 시각화 → 인사이트 도출",
                    "정제 → 수집 → 시각화 → 탐색적 분석(EDA)",
                    "수집 → 시각화 → 정제 → 인사이트 도출",
                ],
                "answer": 1,
                "explanation": (
                    "데이터 분석은 데이터 수집부터 시작합니다. "
                    "수집한 원시 데이터를 정제(결측값, 이상값 처리)하고, "
                    "탐색적 분석(EDA)으로 패턴을 발견한 후, "
                    "시각화로 이해를 돕고, 최종적으로 인사이트를 도출합니다."
                ),
            },
        ],
        "challenge": {
            "question": (
                "다음 상황을 해결하는 Python 스크립트를 작성하세요.\n\n"
                "상황: 팀 동료가 data_analysis 프로젝트를 GitHub에서 클론받았는데 "
                "패키지가 설치되어 있지 않아 실행이 안 된다고 합니다.\n\n"
                "① setup.py 또는 requirements.txt 없이, "
                "스크립트 실행 시 자동으로 필요한 패키지(numpy, pandas, matplotlib, requests)가 "
                "설치되어 있는지 확인하고\n"
                "② 없으면 pip를 사용해 자동 설치하는\n"
                "check_env.py 스크립트를 작성하세요.\n\n"
                "힌트: subprocess 모듈과 importlib를 활용하세요."
            ),
            "hint": (
                "importlib.util.find_spec('패키지명')으로 패키지 존재 여부를 확인하고, "
                "subprocess.check_call([sys.executable, '-m', 'pip', 'install', '패키지명'])으로 "
                "현재 Python 환경에 패키지를 설치할 수 있습니다."
            ),
        },
        "summary": [
            "Vol.2 핵심 개념(OOP, 파일 I/O, 제너레이터)은 데이터 분석 코드에서 자주 활용됩니다.",
            "데이터 분석은 수집→정제→EDA→시각화→인사이트 순서로 진행되는 파이프라인입니다.",
            "Python이 데이터 분석 표준 언어인 이유는 풍부한 생태계와 머신러닝 연동성 때문입니다.",
            "가상환경(venv)은 프로젝트마다 별도로 만들어 패키지 충돌을 방지해야 합니다.",
            "Jupyter Notebook은 코드 실행 결과를 즉시 확인하며 탐색적 분석을 하기에 최적입니다.",
        ],
    }
