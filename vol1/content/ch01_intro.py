"""Chapter 1: 프로그래밍이란 무엇인가 - 컴퓨터와 대화하는 법."""


def get_chapter():
    """챕터 1의 전체 콘텐츠를 딕셔너리로 반환한다."""
    return {
        "number": 1,
        "title": "프로그래밍이란 무엇인가",
        "subtitle": "컴퓨터와 대화하는 법",
        "big_picture": (
            "프로그래밍은 컴퓨터에게 일을 시키기 위한 '명령서'를 작성하는 행위입니다. "
            "이 챕터에서는 프로그래밍의 본질을 이해하고, Python이라는 언어가 "
            "왜 여러분의 MLOps 커리어에 최적의 출발점인지 알아봅니다. "
            "코드를 작성하기 전에 '왜 프로그래밍을 배우는가'를 명확히 하는 것이 중요합니다."
        ),
        "sections": [
            _section_essence_of_programming(),
            _section_how_computers_understand(),
            _section_python_philosophy(),
            _section_language_map(),
            _section_python_for_mlops(),
            _section_what_is_good_code(),
        ],
        "practical_tips": [
            "코드를 읽는 시간이 쓰는 시간보다 훨씬 많으므로, 가독성을 항상 우선시하세요.",
            "새로운 개념을 배울 때는 반드시 직접 코드를 입력하고 실행해보세요. 눈으로만 읽는 것은 효과가 10%입니다.",
            "에러 메시지를 그대로 구글에 검색하면 대부분 Stack Overflow에서 답을 찾을 수 있습니다.",
            "하루에 30분이라도 매일 코딩하는 것이 주말에 몰아서 5시간 하는 것보다 효과적입니다.",
            "`import this`를 Python에서 실행해보세요. Python 개발자들의 철학이 담겨 있습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "프로그래밍 언어를 크게 두 가지로 분류할 때, Python은 어디에 해당하나요?",
                "choices": [
                    "A) 컴파일 언어",
                    "B) 인터프리터 언어",
                    "C) 마크업 언어",
                    "D) 쿼리 언어",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "Python의 Zen(철학)에서 가장 강조하는 가치는 무엇인가요?",
                "choices": [
                    "A) 실행 속도",
                    "B) 메모리 효율",
                    "C) 가독성(Readability)",
                    "D) 하위 호환성",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "다음 중 MLOps 파이프라인에서 Python이 담당하지 않는 영역은?",
                "choices": [
                    "A) 데이터 전처리",
                    "B) 모델 학습",
                    "C) 하드웨어 드라이버 개발",
                    "D) 모델 배포 자동화",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "Python 대화형 모드에서 `import this`를 실행하고, "
                    "출력된 내용 중 자신이 가장 마음에 드는 문장을 골라 "
                    "print()로 출력하는 프로그램을 작성하세요."
                ),
                "hint": "import this를 실행하면 The Zen of Python이 출력됩니다. 마음에 드는 구절을 print()의 따옴표 안에 넣으세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "자신만의 프로그래밍 비유를 하나 생각해내고, "
                    "그 비유를 print()로 출력하는 프로그램을 작성하세요. "
                    "예: '프로그래밍은 레고 블록 쌓기와 같다'"
                ),
                "hint": "print() 안에 자신의 비유를 문자열로 작성합니다. 여러 줄로 출력해도 좋습니다.",
            },
        ],
        "challenge": {
            "question": (
                "Python, Java, JavaScript, C 네 가지 언어로 'Hello, World!'를 출력하는 코드를 "
                "인터넷에서 찾아보고, 각 언어의 코드를 Python의 print() 함수로 출력하는 "
                "프로그램을 작성하세요. 어떤 언어의 문법이 가장 간결한지 주석으로 비교 의견을 적어보세요."
            ),
            "hint": (
                "다른 언어의 코드를 문자열로 print() 안에 넣으면 됩니다. "
                "중괄호({})나 따옴표가 포함된 코드는 이스케이프(\\)에 주의하세요."
            ),
        },
        "summary": [
            "프로그래밍은 컴퓨터에게 일을 시키기 위해 '명령의 집합'을 작성하는 행위입니다.",
            "알고리즘은 문제를 해결하기 위한 단계별 절차이며, 이를 코드로 옮기는 것이 프로그래밍입니다.",
            "인터프리터 언어(Python)는 코드를 한 줄씩 즉시 실행하고, 컴파일 언어(C/Java)는 전체를 먼저 기계어로 번역합니다.",
            "Python의 핵심 철학은 '가독성이 중요하다(Readability counts)'입니다.",
            "Python은 AI/ML 생태계의 사실상 표준 언어로, MLOps 커리어에 필수입니다.",
            "TensorFlow, PyTorch, scikit-learn 등 핵심 ML 라이브러리가 모두 Python 기반입니다.",
            "좋은 코드란 다른 사람(그리고 미래의 나)이 쉽게 읽고 이해할 수 있는 코드입니다.",
            "프로그래밍 언어마다 강점이 다르므로, 목적에 맞는 언어를 선택하는 것이 중요합니다.",
        ],
    }


# ─────────────────────────────────────────────
# 섹션 헬퍼 함수
# ─────────────────────────────────────────────


def _section_essence_of_programming():
    """프로그래밍의 본질 섹션."""
    return {
        "title": "프로그래밍의 본질",
        "content": [
            (
                "프로그래밍이란 무엇일까요? 한마디로 정의하면, "
                "**컴퓨터에게 일을 시키기 위해 명령을 작성하는 행위**입니다. "
                "컴퓨터는 스스로 생각하지 못합니다. 사람이 정확한 명령을 내려야만 동작합니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "프로그래밍은 '요리 레시피'를 작성하는 것과 같습니다. "
                    "요리사가 레시피 없이 요리할 수 있듯이 컴퓨터도 프로그램 없이 스스로 판단할 수 없습니다. "
                    "레시피에 '소금 약간'이라고 쓰면 사람은 적당량을 추측하지만, "
                    "컴퓨터에게는 '소금 2g을 넣어라'처럼 정확하게 알려줘야 합니다."
                ),
            },
            {"type": "heading", "text": "프로그램의 세 가지 구성 요소"},
            {
                "type": "table",
                "headers": ["요소", "설명", "요리 비유"],
                "rows": [
                    ["입력(Input)", "프로그램이 받아들이는 데이터", "재료 (밀가루, 달걀, 설탕)"],
                    ["처리(Process)", "데이터를 가공하는 논리", "조리 과정 (반죽, 굽기)"],
                    ["출력(Output)", "처리 결과를 보여줌", "완성된 요리 (케이크)"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 프로그램의 기본 구조: 입력 -> 처리 -> 출력\n\n"
                    "# 입력: 사용자로부터 이름을 받음\n"
                    'name = input("이름을 입력하세요: ")\n\n'
                    "# 처리: 인사 메시지를 조합\n"
                    'greeting = "안녕하세요, " + name + "님!"\n\n'
                    "# 출력: 결과를 화면에 표시\n"
                    "print(greeting)"
                ),
            },
            {"type": "heading", "text": "알고리즘이란?"},
            (
                "**알고리즘(Algorithm)**은 문제를 해결하기 위한 **단계별 절차**입니다. "
                "프로그래밍은 이 알고리즘을 컴퓨터가 이해할 수 있는 언어로 옮기는 작업입니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 알고리즘 예시: 라면 끓이기\n"
                    "# 1단계: 물 550ml를 냄비에 넣는다\n"
                    "# 2단계: 물이 끓을 때까지 기다린다\n"
                    "# 3단계: 면과 스프를 넣는다\n"
                    "# 4단계: 4분 30초 동안 끓인다\n"
                    "# 5단계: 불을 끄고 그릇에 담는다\n\n"
                    "# 이것을 Python '느낌'으로 표현하면:\n"
                    'print("1. 물 550ml를 냄비에 넣습니다")\n'
                    'print("2. 물이 끓을 때까지 기다립니다")\n'
                    'print("3. 면과 스프를 넣습니다")\n'
                    'print("4. 4분 30초 동안 끓입니다")\n'
                    'print("5. 불을 끄고 그릇에 담습니다")'
                ),
            },
            {
                "type": "note",
                "text": (
                    "프로그래밍의 핵심은 '컴퓨터 언어를 외우는 것'이 아니라, "
                    "'문제를 논리적으로 분해하고 해결 절차를 설계하는 능력'입니다. "
                    "이 능력을 **컴퓨팅 사고력(Computational Thinking)**이라고 합니다."
                ),
            },
        ],
    }


def _section_how_computers_understand():
    """컴퓨터가 코드를 이해하는 방법 섹션."""
    return {
        "title": "컴퓨터가 코드를 이해하는 방법",
        "content": [
            (
                "우리가 작성하는 코드는 영어나 한글 같은 '사람의 언어'에 가깝습니다. "
                "하지만 컴퓨터는 실제로 0과 1(이진수)만 이해합니다. "
                "그렇다면 컴퓨터는 어떻게 우리의 코드를 실행할 수 있는 걸까요?"
            ),
            {
                "type": "flow_diagram",
                "nodes": [
                    {"label": "소스 코드", "sub": "print('Hello')"},
                    {"label": "인터프리터", "sub": "중간 번역 단계"},
                    {"label": "기계어", "sub": "0101 1010..."},
                ],
                "title": "소스 코드가 실행되기까지",
            },
            {"type": "heading", "text": "컴파일 방식 vs 인터프리터 방식"},
            (
                "프로그래밍 언어가 기계어로 번역되는 방식은 크게 두 가지가 있습니다. "
                "이 차이를 이해하면 Python의 특성을 더 잘 파악할 수 있습니다."
            ),
            {
                "type": "table",
                "headers": ["구분", "컴파일 방식", "인터프리터 방식"],
                "rows": [
                    ["번역 시점", "실행 전에 전체를 한 번에 번역", "실행하면서 한 줄씩 번역"],
                    ["실행 속도", "빠름 (이미 번역 완료)", "상대적으로 느림"],
                    ["개발 속도", "느림 (컴파일 대기 시간)", "빠름 (바로 실행 확인)"],
                    ["에러 발견", "컴파일 시 전체 에러 표시", "실행 중 해당 줄에서 에러 표시"],
                    ["대표 언어", "C, C++, Go, Rust", "Python, JavaScript, Ruby"],
                ],
            },
            {
                "type": "analogy",
                "text": (
                    "컴파일 방식은 '번역된 책'과 같습니다. 전체를 미리 번역해두면 읽는 속도가 빠릅니다. "
                    "인터프리터 방식은 '동시통역'과 같습니다. 한 문장씩 바로 통역하므로 "
                    "전체 번역을 기다릴 필요가 없지만, 통역 시간이 추가됩니다."
                ),
            },
            {"type": "heading", "text": "Python의 실행 과정"},
            {
                "type": "numbered_list",
                "items": [
                    "개발자가 .py 파일에 소스 코드를 작성합니다.",
                    "python3 명령으로 실행하면 Python 인터프리터(CPython)가 시작됩니다.",
                    "인터프리터가 소스 코드를 **바이트코드(.pyc)**로 변환합니다.",
                    "바이트코드를 **Python 가상 머신(PVM)**이 실행합니다.",
                    "결과가 화면에 출력됩니다.",
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 이 코드가 실행되는 과정을 관찰해봅시다\n"
                    'print("1번 줄: 인터프리터가 이 줄을 읽고 실행합니다")\n'
                    'print("2번 줄: 그 다음 이 줄을 읽고 실행합니다")\n'
                    'print("3번 줄: 위에서 아래로 순서대로 실행됩니다")\n'
                    "# 인터프리터는 위에서 아래로, 한 줄씩 실행합니다"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "Python이 인터프리터 언어라서 '느리다'는 말을 들을 수 있습니다. "
                    "하지만 대부분의 응용 프로그램에서 개발 속도의 이점이 실행 속도의 차이보다 큽니다. "
                    "성능이 정말 중요한 부분은 C로 작성된 라이브러리(NumPy 등)를 활용합니다."
                ),
            },
        ],
    }


def _section_python_philosophy():
    """Python의 철학 섹션."""
    return {
        "title": "Python의 철학",
        "content": [
            (
                "모든 프로그래밍 언어에는 설계 철학이 있습니다. "
                "Python의 철학은 **'import this'**라는 특별한 명령으로 확인할 수 있습니다. "
                "이를 **The Zen of Python (파이썬의 선)**이라고 부릅니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 터미널에서 python3을 실행한 후 입력해보세요\n"
                    "import this\n\n"
                    "# The Zen of Python이 출력됩니다"
                ),
            },
            {"type": "heading", "text": "초보자가 알아야 할 핵심 원칙"},
            {
                "type": "table",
                "headers": ["원칙 (영어)", "의미 (한국어)", "실천 방법"],
                "rows": [
                    [
                        "Beautiful is better than ugly",
                        "아름다운 것이 추한 것보다 낫다",
                        "코드를 보기 좋게 정리하세요",
                    ],
                    [
                        "Explicit is better than implicit",
                        "명시적인 것이 암묵적인 것보다 낫다",
                        "코드의 의도를 분명히 드러내세요",
                    ],
                    [
                        "Simple is better than complex",
                        "단순한 것이 복잡한 것보다 낫다",
                        "가능한 한 간단하게 작성하세요",
                    ],
                    [
                        "Readability counts",
                        "가독성이 중요하다",
                        "다른 사람이 읽기 쉬운 코드를 쓰세요",
                    ],
                    [
                        "Errors should never pass silently",
                        "에러는 조용히 넘어가면 안 된다",
                        "에러를 무시하지 말고 처리하세요",
                    ],
                ],
            },
            (
                "이 원칙들은 단순한 구호가 아닙니다. "
                "Python 커뮤니티의 코드 리뷰, 라이브러리 설계, 언어 업데이트에 "
                "실제로 반영되는 핵심 가치입니다."
            ),
            {"type": "heading", "text": "Python 스타일 가이드: PEP 8"},
            (
                "**PEP 8**은 Python의 공식 코딩 스타일 가이드입니다. "
                "전 세계 Python 개발자들이 이 규칙을 따르므로, "
                "처음부터 좋은 습관을 들이는 것이 중요합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# PEP 8을 따르는 좋은 코드\n"
                    "user_name = '홍길동'\n"
                    "user_age = 20\n"
                    "print(user_name, '님은', user_age, '살입니다')\n\n"
                    "# PEP 8을 따르지 않는 나쁜 코드\n"
                    "UserName='홍길동'\n"
                    "userage=20\n"
                    "print(UserName,'님은',userage,'살입니다')"
                ),
            },
            {
                "type": "bullet_list",
                "items": [
                    "변수명은 소문자와 밑줄(`snake_case`)을 사용합니다: `user_name`",
                    "연산자 앞뒤에 공백을 넣습니다: `x = 1 + 2`",
                    "들여쓰기는 공백 4칸을 사용합니다 (탭이 아님)",
                    "한 줄의 최대 길이는 79자를 권장합니다",
                    "주석은 `#` 뒤에 공백 한 칸을 넣습니다: `# 이것은 주석입니다`",
                ],
            },
            {
                "type": "note",
                "text": (
                    "PEP 8을 처음부터 완벽하게 외울 필요는 없습니다. "
                    "VS Code의 Python 확장이 스타일 위반을 자동으로 알려주므로, "
                    "코딩하면서 자연스럽게 익히면 됩니다."
                ),
            },
        ],
    }


def _section_language_map():
    """프로그래밍 언어 지도 섹션."""
    return {
        "title": "프로그래밍 언어 지도",
        "content": [
            (
                "세상에는 수백 가지 프로그래밍 언어가 있습니다. "
                "각 언어에는 고유한 강점과 적합한 분야가 있으며, "
                "'최고의 언어'는 존재하지 않습니다. '목적에 맞는 언어'가 있을 뿐입니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "프로그래밍 언어는 '도구'와 같습니다. "
                    "망치는 못을 박는 데 최고이지만, 나사를 조이려면 드라이버가 필요합니다. "
                    "마찬가지로 웹 개발에는 JavaScript가, 시스템 프로그래밍에는 C/Rust가, "
                    "데이터 과학에는 Python이 적합합니다."
                ),
            },
            {"type": "heading", "text": "주요 프로그래밍 언어 비교"},
            {
                "type": "table",
                "headers": ["언어", "탄생", "주요 분야", "난이도", "특징"],
                "rows": [
                    ["Python", "1991", "AI/ML, 데이터, 자동화, 웹", "쉬움", "가독성, 생산성 최고"],
                    ["JavaScript", "1995", "웹 프론트엔드, 서버(Node.js)", "보통", "브라우저에서 유일하게 동작"],
                    ["Java", "1995", "기업 서버, Android 앱", "보통", "한 번 작성하면 어디서든 실행"],
                    ["C", "1972", "시스템 프로그래밍, 임베디드", "어려움", "하드웨어에 가까운 저수준 제어"],
                    ["C++", "1985", "게임 엔진, 고성능 시스템", "어려움", "C의 확장, 객체지향 지원"],
                    ["Go", "2009", "서버, 클라우드 인프라", "보통", "간결함, 동시성 처리에 강점"],
                    ["Rust", "2015", "시스템, 웹 어셈블리", "어려움", "메모리 안전성, 성능 최고"],
                ],
            },
            {"type": "heading", "text": "Hello, World! 비교"},
            (
                "같은 동작을 하는 프로그램이 언어마다 얼마나 다른지 비교해보겠습니다. "
                "Python의 간결함을 직접 느낄 수 있습니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    '# Python - 1줄이면 충분합니다\nprint("Hello, World!")'
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# Java - 같은 출력을 위해 5줄이 필요합니다 (참고용)\n"
                    "# public class Hello {\n"
                    "#     public static void main(String[] args) {\n"
                    '#         System.out.println("Hello, World!");\n'
                    "#     }\n"
                    "# }"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# C - 전처리기 지시문과 main 함수가 필요합니다 (참고용)\n"
                    "# #include <stdio.h>\n"
                    "# int main() {\n"
                    '#     printf("Hello, World!\\n");\n'
                    "#     return 0;\n"
                    "# }"
                ),
            },
            {
                "type": "note",
                "text": (
                    "Python으로 시작해서 프로그래밍의 기본 개념을 익힌 뒤, "
                    "필요에 따라 다른 언어를 배우는 것을 권장합니다. "
                    "프로그래밍의 핵심 개념(변수, 조건문, 반복문 등)은 모든 언어에서 공통입니다."
                ),
            },
        ],
    }


def _section_python_for_mlops():
    """Python이 MLOps에서 중요한 이유 섹션."""
    return {
        "title": "Python이 MLOps에서 중요한 이유",
        "content": [
            (
                "**MLOps(Machine Learning Operations)**는 머신러닝 모델의 개발, 배포, 운영을 "
                "체계적으로 관리하는 분야입니다. 이 분야에서 Python은 '공용어'와 같은 역할을 합니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "MLOps에서 Python의 위치는 건축에서 '설계 도면'의 언어와 같습니다. "
                    "건축가, 시공자, 감리자 모두 도면의 기호를 읽을 수 있어야 하듯이, "
                    "데이터 과학자, ML 엔지니어, DevOps 엔지니어 모두 Python을 사용합니다."
                ),
            },
            {"type": "heading", "text": "MLOps 파이프라인과 Python"},
            {
                "type": "flow_diagram",
                "nodes": [
                    {"label": "데이터 수집", "sub": "pandas, requests"},
                    {"label": "데이터 전처리", "sub": "pandas, numpy"},
                    {"label": "모델 학습", "sub": "PyTorch, TF"},
                    {"label": "모델 평가", "sub": "scikit-learn"},
                    {"label": "모델 배포", "sub": "FastAPI, MLflow"},
                    {"label": "모니터링", "sub": "Prometheus"},
                    {"label": "재학습", "sub": "Airflow"},
                    {"label": "자동화", "sub": "GitHub Actions"},
                ],
                "title": "MLOps 파이프라인 전체 흐름",
            },
            {"type": "heading", "text": "핵심 Python 라이브러리"},
            {
                "type": "table",
                "headers": ["영역", "라이브러리", "용도"],
                "rows": [
                    ["데이터 처리", "pandas, NumPy", "표 형태 데이터 조작, 수치 계산"],
                    ["시각화", "matplotlib, seaborn", "그래프, 차트 생성"],
                    ["머신러닝", "scikit-learn", "분류, 회귀, 클러스터링 등 전통 ML"],
                    ["딥러닝", "PyTorch, TensorFlow", "신경망 모델 구축 및 학습"],
                    ["모델 배포", "FastAPI, Flask", "ML 모델을 API로 서빙"],
                    ["파이프라인", "Airflow, Kubeflow", "학습/배포 자동화"],
                    ["실험 관리", "MLflow, Weights & Biases", "실험 추적, 모델 버전 관리"],
                ],
            },
            (
                "이 교재에서 당장 이 라이브러리들을 다루지는 않습니다. "
                "하지만 Python의 기초를 탄탄히 다져두면, "
                "이후 이 도구들을 배울 때 훨씬 수월해집니다."
            ),
            {"type": "heading", "text": "MLOps 엔지니어의 Python 학습 로드맵"},
            {
                "type": "numbered_list",
                "items": [
                    "**Python 기초** (이 교재) - 변수, 조건문, 반복문, 함수, 클래스",
                    "**데이터 처리** - pandas, NumPy로 데이터 다루기",
                    "**API 개발** - FastAPI로 모델 서빙 API 만들기",
                    "**ML 기초** - scikit-learn으로 머신러닝 체험",
                    "**딥러닝** - PyTorch 또는 TensorFlow 입문",
                    "**MLOps 도구** - Docker, Airflow, MLflow 활용",
                ],
            },
            {
                "type": "tip",
                "text": (
                    "MLOps 분야에서는 Python 코딩 능력뿐만 아니라 "
                    "Linux 기본 명령어, Git, Docker도 함께 알아야 합니다. "
                    "하지만 모든 것의 출발점은 Python 기초입니다."
                ),
            },
        ],
    }


def _section_what_is_good_code():
    """좋은 코드란 무엇인가 섹션."""
    return {
        "title": "좋은 코드란 무엇인가",
        "content": [
            (
                "프로그래밍을 시작하면 '작동하는 코드'를 만드는 데 집중하게 됩니다. "
                "하지만 전문 개발자의 세계에서는 '작동하는 것'만으로 충분하지 않습니다. "
                "**좋은 코드**는 지금 작동할 뿐 아니라, 미래에도 이해하고 수정하기 쉬운 코드입니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "코드는 '편지'와 같습니다. "
                    "지금 당장 내용이 전달되면 그만이지만, "
                    "나중에 다시 읽었을 때 무슨 의미인지 이해할 수 있어야 합니다. "
                    "6개월 후의 자신도 '다른 사람'이라고 생각하세요."
                ),
            },
            {"type": "heading", "text": "좋은 코드의 세 가지 기준"},
            {
                "type": "table",
                "headers": ["기준", "설명", "예시"],
                "rows": [
                    [
                        "가독성(Readability)",
                        "코드를 읽기만 해도 의도를 파악할 수 있음",
                        "변수명을 a 대신 user_age로 작성",
                    ],
                    [
                        "유지보수성(Maintainability)",
                        "나중에 수정하거나 기능을 추가하기 쉬움",
                        "한 함수가 한 가지 일만 담당",
                    ],
                    [
                        "간결함(Simplicity)",
                        "불필요한 복잡성 없이 핵심만 표현",
                        "10줄로 될 것을 30줄로 쓰지 않음",
                    ],
                ],
            },
            {"type": "heading", "text": "좋은 코드 vs 나쁜 코드 비교"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# --- 나쁜 코드: 무슨 뜻인지 알 수 없음 ---\n"
                    "a = 85000\n"
                    "b = 12\n"
                    "c = a * b\n"
                    "print(c)\n\n"
                    "# --- 좋은 코드: 의도가 명확함 ---\n"
                    "monthly_salary = 85000       # 월급 (원)\n"
                    "months = 12                  # 1년 = 12개월\n"
                    "annual_salary = monthly_salary * months  # 연봉 계산\n"
                    "print(annual_salary)         # 연봉 출력"
                ),
            },
            (
                "두 코드의 실행 결과는 동일합니다. 하지만 두 번째 코드는 "
                "변수명만 읽어도 무엇을 계산하는지 바로 알 수 있습니다. "
                "코드에 '주석'을 추가하면 이해가 더욱 쉬워집니다."
            ),
            {"type": "heading", "text": "초보자를 위한 코딩 습관"},
            {
                "type": "bullet_list",
                "items": [
                    "**의미 있는 이름 짓기**: `x` 대신 `user_count`처럼 의미를 담은 이름을 사용하세요.",
                    "**주석 달기**: 코드의 '왜(why)'를 설명하는 주석을 작성하세요.",
                    "**작게 나누기**: 한 번에 모든 것을 해결하려 하지 말고, 작은 단위로 나누세요.",
                    "**복사-붙여넣기 자제**: 같은 코드가 반복되면 나중에 함수로 묶는 방법을 배울 것입니다.",
                    "**자주 실행하기**: 코드 10줄을 작성할 때마다 실행하여 중간 결과를 확인하세요.",
                ],
            },
            {
                "type": "warning",
                "text": (
                    "처음부터 '완벽한 코드'를 작성하려고 하지 마세요. "
                    "먼저 동작하는 코드를 만들고, 그 다음 더 좋은 코드로 개선하는 것이 "
                    "올바른 순서입니다. 이를 '리팩토링(Refactoring)'이라고 합니다."
                ),
            },
        ],
    }
