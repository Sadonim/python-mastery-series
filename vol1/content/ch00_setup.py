"""Chapter 0: 개발 환경 설정 - Python과의 첫 만남."""


def get_chapter():
    """챕터 0의 전체 콘텐츠를 딕셔너리로 반환한다."""
    return {
        "number": 0,
        "title": "개발 환경 설정",
        "subtitle": "Python과의 첫 만남",
        "big_picture": (
            "프로그래밍을 배우기 전에 가장 먼저 해야 할 일은 '작업 공간'을 준비하는 것입니다. "
            "목수가 연장을 정리하듯, 개발자는 언어 설치와 편집기 설정부터 시작합니다. "
            "이 챕터에서 준비한 환경은 앞으로 모든 챕터의 실습 기반이 됩니다."
        ),
        "sections": [
            _section_what_is_python(),
            _section_install_python(),
            _section_vscode_setup(),
            _section_terminal_basics(),
            _section_hello_world(),
            _section_dev_workflow(),
        ],
        "practical_tips": [
            "Python 버전이 헷갈릴 때는 항상 `python3 --version`으로 확인하세요.",
            "VS Code의 터미널(Ctrl+`)을 활용하면 편집기와 실행 환경을 한 화면에서 쓸 수 있습니다.",
            "새 프로젝트를 시작할 때마다 전용 폴더를 만들면 파일 관리가 편합니다.",
            "코드 실행이 안 될 때는 파일을 저장(Ctrl+S)했는지 먼저 확인하세요.",
            "PATH 문제가 의심되면 터미널을 완전히 껐다가 다시 열어보세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "Python 공식 웹사이트 주소로 올바른 것은?",
                "choices": [
                    "A) python.com",
                    "B) python.org",
                    "C) python.dev",
                    "D) python.io",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "Windows에서 Python 설치 시 반드시 체크해야 하는 옵션은?",
                "choices": [
                    "A) Install for all users",
                    "B) Add Python to PATH",
                    "C) Install pip",
                    "D) Download debug symbols",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "터미널에서 Python 버전을 확인하는 명령어를 입력하고, "
                    "이어서 '나의 첫 Python 프로그램'이라는 문장을 출력하는 "
                    "hello.py 파일을 만들어 실행해보세요."
                ),
                "hint": "python3 --version 으로 버전 확인, print() 함수로 문자열 출력",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "VS Code에서 새 파일 greeting.py를 만들고, "
                    "자신의 이름과 오늘 날짜를 출력하는 프로그램을 작성하세요."
                ),
                "hint": "print()를 여러 번 사용하거나, 여러 값을 쉼표로 구분할 수 있습니다.",
            },
        ],
        "challenge": {
            "question": (
                "ASCII 아트로 간단한 그림(예: 집, 나무, 로봇)을 출력하는 "
                "Python 프로그램을 작성하세요. print() 함수를 최소 5줄 이상 사용하고, "
                "VS Code에서 작성한 뒤 터미널로 실행해보세요."
            ),
            "hint": (
                "print()에 특수문자(*, /, \\, |, _, ^)를 조합하면 그림을 만들 수 있습니다. "
                "백슬래시(\\)는 \\\\로 두 번 써야 합니다."
            ),
        },
        "summary": [
            "Python은 1991년 귀도 반 로섬이 만든 범용 프로그래밍 언어로, 가독성과 생산성이 뛰어납니다.",
            "2024년 TIOBE 지수 1위를 차지하며 AI/데이터 과학 분야에서 사실상 표준 언어입니다.",
            "macOS는 Homebrew(`brew install python`), Windows는 공식 설치 파일로 Python을 설치합니다.",
            "Windows 설치 시 'Add Python to PATH' 체크박스를 반드시 선택해야 합니다.",
            "VS Code + Python 확장은 초보자부터 전문가까지 가장 널리 쓰이는 개발 환경입니다.",
            "터미널은 개발자의 기본 도구이며, 파일 탐색과 프로그램 실행에 필수적입니다.",
            "코드 작성 -> 저장 -> 실행 -> 결과 확인의 사이클을 이해하는 것이 개발의 첫걸음입니다.",
            "Hello, World! 프로그램은 환경이 정상 동작하는지 검증하는 전통적인 첫 프로그램입니다.",
        ],
    }


# ─────────────────────────────────────────────
# 섹션 헬퍼 함수
# ─────────────────────────────────────────────


def _section_what_is_python():
    """Python이란? 섹션."""
    return {
        "title": "Python이란?",
        "content": [
            (
                "Python은 1991년 네덜란드의 프로그래머 **귀도 반 로섬(Guido van Rossum)**이 "
                "만든 범용 프로그래밍 언어입니다. 이름은 영국의 코미디 그룹 "
                "'몬티 파이선(Monty Python)'에서 따왔습니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "프로그래밍 언어를 외국어에 비유하면, Python은 '영어'와 같습니다. "
                    "배우기 쉽고, 전 세계에서 가장 많이 쓰이며, 어디서든 통합니다."
                ),
            },
            (
                "Python은 2024년 **TIOBE 프로그래밍 언어 인기 지수**에서 1위를 차지했습니다. "
                "웹 개발, 데이터 과학, 인공지능, 자동화, 시스템 관리 등 거의 모든 분야에서 "
                "활발하게 사용되고 있습니다."
            ),
            {"type": "heading", "text": "Python의 핵심 특징"},
            {
                "type": "table",
                "headers": ["특징", "설명"],
                "rows": [
                    ["읽기 쉬운 문법", "영어 문장처럼 자연스러운 코드 구조"],
                    ["인터프리터 언어", "코드를 한 줄씩 바로 실행할 수 있음"],
                    ["동적 타이핑", "변수의 자료형을 미리 선언하지 않아도 됨"],
                    ["풍부한 라이브러리", "수십만 개의 패키지가 PyPI에 등록되어 있음"],
                    ["크로스 플랫폼", "Windows, macOS, Linux 어디서든 동작"],
                    ["무료 & 오픈소스", "누구나 무료로 사용하고 코드를 볼 수 있음"],
                ],
            },
            {"type": "heading", "text": "Python이 인기 있는 이유"},
            {
                "type": "bullet_list",
                "items": [
                    "**낮은 진입 장벽**: 다른 언어에 비해 문법이 간결하여 초보자도 빠르게 배울 수 있습니다.",
                    "**AI/ML 생태계**: TensorFlow, PyTorch, scikit-learn 등 핵심 라이브러리가 모두 Python 기반입니다.",
                    "**거대한 커뮤니티**: Stack Overflow, GitHub 등에서 질문하면 빠르게 답변을 얻을 수 있습니다.",
                    "**기업 채택**: Google, Netflix, Instagram, Spotify 등 글로벌 기업이 Python을 핵심 기술로 사용합니다.",
                    "**MLOps 표준**: 모델 학습부터 배포, 모니터링까지 전 과정에서 Python이 사용됩니다.",
                ],
            },
            {
                "type": "note",
                "text": (
                    "이 교재에서는 Python 3.12 버전을 기준으로 설명합니다. "
                    "Python 2는 2020년 공식 지원이 종료되었으므로 반드시 Python 3을 사용하세요."
                ),
            },
        ],
    }


def _section_install_python():
    """Python 3.12 설치 섹션."""
    return {
        "title": "Python 3.12 설치",
        "content": [
            (
                "Python을 사용하려면 먼저 컴퓨터에 설치해야 합니다. "
                "운영체제에 따라 설치 방법이 다르므로 자신의 환경에 맞는 방법을 따라주세요."
            ),
            {"type": "heading", "text": "macOS에서 설치하기"},
            (
                "macOS에는 Python이 기본 설치되어 있을 수 있지만, 시스템용 Python이므로 "
                "개발용으로 별도 설치하는 것을 권장합니다. 두 가지 방법이 있습니다."
            ),
            {"type": "heading", "text": "방법 1: 공식 설치 파일 (추천)"},
            {
                "type": "numbered_list",
                "items": [
                    "웹 브라우저에서 https://python.org 에 접속합니다.",
                    "상단 메뉴의 Downloads > macOS를 클릭합니다.",
                    "최신 Python 3.12.x 버전의 macOS installer를 다운로드합니다.",
                    "다운로드한 .pkg 파일을 더블클릭하여 설치를 진행합니다.",
                    "설치 완료 후 터미널을 열고 버전을 확인합니다.",
                ],
            },
            {
                "type": "code",
                "language": "bash",
                "code": "# macOS 터미널에서 Python 버전 확인\npython3 --version\n# 출력 예: Python 3.12.x",
            },
            {"type": "heading", "text": "방법 2: Homebrew 사용"},
            (
                "Homebrew는 macOS의 패키지 관리자로, 터미널에서 간편하게 소프트웨어를 "
                "설치할 수 있게 해줍니다."
            ),
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# Homebrew가 없다면 먼저 설치\n"
                    '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"\n\n'
                    "# Python 설치\n"
                    "brew install python@3.12\n\n"
                    "# 버전 확인\n"
                    "python3 --version"
                ),
            },
            {"type": "heading", "text": "Windows에서 설치하기"},
            {
                "type": "numbered_list",
                "items": [
                    "https://python.org 에 접속합니다.",
                    "Downloads > Windows를 클릭합니다.",
                    "최신 Python 3.12.x 버전의 Windows installer (64-bit)를 다운로드합니다.",
                    "다운로드한 파일을 실행합니다.",
                    "**반드시 'Add python.exe to PATH' 체크박스를 선택합니다!**",
                    "'Install Now'를 클릭하여 설치합니다.",
                ],
            },
            {
                "type": "warning",
                "text": (
                    "Windows 설치 시 'Add python.exe to PATH' 체크를 빠뜨리면 "
                    "터미널에서 python 명령을 인식하지 못합니다. "
                    "이 경우 Python을 제거 후 다시 설치하거나, 환경 변수를 수동으로 추가해야 합니다."
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# Windows PowerShell에서 확인\n"
                    "python --version\n"
                    "# 출력 예: Python 3.12.x\n\n"
                    "# pip(패키지 관리자)도 함께 확인\n"
                    "pip --version"
                ),
            },
            {
                "type": "note",
                "text": (
                    "macOS/Linux에서는 `python3`, Windows에서는 `python`으로 실행하는 것이 일반적입니다. "
                    "이 교재에서는 `python3`을 기준으로 설명하지만, Windows 사용자는 `python`으로 대체하세요."
                ),
            },
            {"type": "heading", "text": "설치 확인 체크리스트"},
            {
                "type": "table",
                "headers": ["항목", "확인 명령어", "정상 결과"],
                "rows": [
                    ["Python 버전", "python3 --version", "Python 3.12.x"],
                    ["pip 버전", "pip3 --version", "pip 24.x.x"],
                    ["대화형 모드", "python3 (엔터)", ">>> 프롬프트 표시"],
                    ["종료", "exit() 또는 Ctrl+D", "터미널로 복귀"],
                ],
            },
        ],
    }


def _section_vscode_setup():
    """VS Code 설정 섹션."""
    return {
        "title": "VS Code 설정",
        "content": [
            (
                "**Visual Studio Code(VS Code)**는 Microsoft가 만든 무료 코드 편집기입니다. "
                "가볍고 빠르면서도 강력한 기능을 갖추고 있어 전 세계 개발자들이 가장 많이 사용합니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "코드 편집기는 '작가의 워드프로세서'와 같습니다. "
                    "메모장으로도 글을 쓸 수 있지만, 맞춤법 검사와 자동 완성이 있는 "
                    "워드프로세서가 훨씬 효율적인 것처럼, VS Code는 개발자를 위한 "
                    "똑똑한 편집 도구입니다."
                ),
            },
            {"type": "heading", "text": "VS Code 설치"},
            {
                "type": "numbered_list",
                "items": [
                    "https://code.visualstudio.com 에 접속합니다.",
                    "자신의 운영체제에 맞는 버전을 다운로드합니다.",
                    "설치 파일을 실행하고 기본 옵션으로 설치합니다.",
                    "설치 완료 후 VS Code를 실행합니다.",
                ],
            },
            {"type": "heading", "text": "필수 확장(Extension) 설치"},
            (
                "VS Code의 진정한 힘은 확장(Extension)에 있습니다. "
                "왼쪽 사이드바의 네모 아이콘(Extensions)을 클릭하여 아래 확장을 설치하세요."
            ),
            {
                "type": "table",
                "headers": ["확장 이름", "제작자", "용도"],
                "rows": [
                    ["Python", "Microsoft", "Python 문법 강조, 디버깅, 린팅 (필수)"],
                    ["Pylance", "Microsoft", "빠른 자동 완성과 타입 체크 (필수)"],
                    ["Korean Language Pack", "Microsoft", "VS Code 한국어 메뉴"],
                    ["indent-rainbow", "oderwat", "들여쓰기를 색상으로 구분"],
                    ["Error Lens", "Alexander", "에러를 코드 옆에 바로 표시"],
                    ["Material Icon Theme", "Philipp Kief", "파일 아이콘을 보기 좋게 변경"],
                ],
            },
            {"type": "heading", "text": "기본 설정 추천"},
            (
                "VS Code 설정은 `Ctrl+,` (macOS: `Cmd+,`)으로 열 수 있습니다. "
                "아래 설정을 JSON으로 추가하면 Python 개발에 편리합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# settings.json에 추가할 설정 (참고용)\n"
                    "# {\n"
                    '#     "editor.fontSize": 14,\n'
                    '#     "editor.tabSize": 4,\n'
                    '#     "editor.formatOnSave": true,\n'
                    '#     "python.defaultInterpreterPath": "python3",\n'
                    '#     "files.autoSave": "afterDelay"\n'
                    "# }"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "VS Code 하단 상태바의 Python 버전을 클릭하면 사용할 Python 인터프리터를 "
                    "선택할 수 있습니다. 여러 버전이 설치된 경우 올바른 버전이 선택되었는지 확인하세요."
                ),
            },
        ],
    }


def _section_terminal_basics():
    """터미널 기초 섹션."""
    return {
        "title": "터미널 기초",
        "content": [
            (
                "**터미널(Terminal)**은 텍스트 명령어로 컴퓨터를 조작하는 도구입니다. "
                "마우스 클릭 대신 키보드로 명령을 입력하여 파일을 관리하고 프로그램을 실행합니다."
            ),
            {
                "type": "analogy",
                "text": (
                    "터미널은 '음성 비서'와 비슷합니다. "
                    "GUI(그래픽 사용자 인터페이스)가 아이콘을 클릭하는 방식이라면, "
                    "터미널은 '이 폴더 열어줘', '이 파일 실행해줘'라고 텍스트로 지시하는 방식입니다."
                ),
            },
            {"type": "heading", "text": "터미널 열기"},
            {
                "type": "table",
                "headers": ["운영체제", "방법"],
                "rows": [
                    ["macOS", "Spotlight(Cmd+Space)에서 'Terminal' 검색 또는 응용 프로그램 > 유틸리티 > 터미널"],
                    ["Windows", "시작 메뉴에서 'PowerShell' 검색 또는 Win+R > powershell 입력"],
                    ["VS Code", "Ctrl+` (백틱) 또는 상단 메뉴 > 터미널 > 새 터미널"],
                ],
            },
            {"type": "heading", "text": "필수 터미널 명령어"},
            {
                "type": "table",
                "headers": ["명령어", "macOS/Linux", "Windows PowerShell", "설명"],
                "rows": [
                    ["현재 위치 확인", "pwd", "pwd 또는 Get-Location", "지금 어느 폴더에 있는지 표시"],
                    ["폴더 내용 보기", "ls", "ls 또는 dir", "현재 폴더의 파일/폴더 목록"],
                    ["폴더 이동", "cd 폴더명", "cd 폴더명", "지정한 폴더로 이동"],
                    ["상위 폴더로 이동", "cd ..", "cd ..", "한 단계 위 폴더로 이동"],
                    ["폴더 만들기", "mkdir 폴더명", "mkdir 폴더명", "새 폴더 생성"],
                    ["파일 삭제", "rm 파일명", "Remove-Item 파일명", "파일 삭제 (주의!)"],
                    ["화면 지우기", "clear", "cls 또는 clear", "터미널 화면 정리"],
                ],
            },
            {"type": "heading", "text": "터미널 실습"},
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 1. 현재 위치 확인\n"
                    "pwd\n\n"
                    "# 2. 바탕화면으로 이동\n"
                    "cd ~/Desktop\n\n"
                    "# 3. 실습 폴더 만들기\n"
                    "mkdir python_practice\n\n"
                    "# 4. 실습 폴더로 이동\n"
                    "cd python_practice\n\n"
                    "# 5. 폴더 내용 확인 (아직 비어있음)\n"
                    "ls"
                ),
            },
            {
                "type": "warning",
                "text": (
                    "rm 명령어로 삭제한 파일은 휴지통에 들어가지 않고 바로 삭제됩니다. "
                    "중요한 파일은 절대 rm으로 삭제하지 마세요."
                ),
            },
            {
                "type": "tip",
                "text": (
                    "터미널에서 Tab 키를 누르면 파일명이나 폴더명이 자동 완성됩니다. "
                    "긴 이름을 일일이 타이핑할 필요가 없으니 적극 활용하세요."
                ),
            },
        ],
    }


def _section_hello_world():
    """첫 번째 프로그램: Hello, World! 섹션."""
    return {
        "title": "첫 번째 프로그램: Hello, World!",
        "content": [
            (
                "모든 프로그래밍 언어 학습은 'Hello, World!'로 시작합니다. "
                "이 전통은 1978년 브라이언 커니핸의 C 프로그래밍 교재에서 시작되었습니다. "
                "단순한 프로그램이지만, 환경이 정상적으로 설정되었는지 확인하는 중요한 의미가 있습니다."
            ),
            {"type": "heading", "text": "프로그램 작성하기"},
            {
                "type": "numbered_list",
                "items": [
                    "VS Code를 열고, 앞에서 만든 python_practice 폴더를 엽니다 (파일 > 폴더 열기).",
                    "새 파일을 만듭니다 (Ctrl+N 또는 Cmd+N).",
                    "아래 코드를 입력합니다.",
                    "파일을 hello.py로 저장합니다 (Ctrl+S 또는 Cmd+S).",
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# hello.py - 나의 첫 번째 Python 프로그램\n"
                    'print("Hello, World!")\n'
                    'print("안녕하세요, Python!")\n'
                    'print("프로그래밍의 세계에 오신 것을 환영합니다!")'
                ),
            },
            {"type": "heading", "text": "프로그램 실행하기"},
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 터미널에서 실행\n"
                    "python3 hello.py\n\n"
                    "# 실행 결과:\n"
                    "# Hello, World!\n"
                    "# 안녕하세요, Python!\n"
                    "# 프로그래밍의 세계에 오신 것을 환영합니다!"
                ),
            },
            (
                "축하합니다! 방금 여러분의 첫 Python 프로그램을 실행했습니다. "
                "`print()` 함수는 괄호 안의 내용을 화면에 출력하는 역할을 합니다."
            ),
            {"type": "heading", "text": "대화형 모드(REPL) 체험하기"},
            (
                "Python에는 코드를 한 줄씩 즉시 실행할 수 있는 **대화형 모드**가 있습니다. "
                "REPL(Read-Eval-Print Loop)이라고도 부릅니다."
            ),
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 대화형 모드 시작\n"
                    "python3\n\n"
                    '>>> print("대화형 모드에서 안녕!")\n'
                    "대화형 모드에서 안녕!\n"
                    ">>> 1 + 1\n"
                    "2\n"
                    '>>> "Python" * 3\n'
                    "'PythonPythonPython'\n"
                    ">>> exit()  # 대화형 모드 종료"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "REPL은 코드 조각을 빠르게 테스트할 때 유용합니다. "
                    "하지만 본격적인 프로그램은 .py 파일에 작성하세요."
                ),
            },
        ],
    }


def _section_dev_workflow():
    """개발 작업 흐름 이해하기 섹션."""
    return {
        "title": "개발 작업 흐름 이해하기",
        "content": [
            (
                "프로그래밍은 한 번에 완성되는 것이 아닙니다. "
                "개발자는 '코드 작성 -> 저장 -> 실행 -> 결과 확인 -> 수정'의 "
                "**반복 사이클**을 통해 프로그램을 완성합니다."
            ),
            {
                "type": "flow_diagram",
                "nodes": ["코드 작성", "저장", "실행", "결과 확인"],
                "note": "수정이 필요하면 첫 단계로 돌아가서 반복합니다",
            },
            {
                "type": "analogy",
                "text": (
                    "이 과정은 '글쓰기'와 매우 비슷합니다. "
                    "초안을 쓰고(코드 작성), 저장하고, 읽어보고(실행), "
                    "어색한 부분을 고치는(수정) 과정을 반복하여 좋은 글이 완성됩니다."
                ),
            },
            {"type": "heading", "text": "실습: 작업 흐름 체험하기"},
            {
                "type": "numbered_list",
                "items": [
                    "VS Code에서 workflow.py 파일을 만듭니다.",
                    '`print("1단계: 코드 작성 완료")`를 입력합니다.',
                    "Ctrl+S로 저장합니다.",
                    "터미널에서 `python3 workflow.py`로 실행합니다.",
                    "출력 결과를 확인합니다.",
                    '코드를 `print("1단계: 코드 작성 완료!")` 처럼 수정하고 다시 저장/실행합니다.',
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# workflow.py - 개발 작업 흐름 연습\n"
                    'print("=== 개발 작업 흐름 연습 ===")\n'
                    'print("1단계: 코드를 작성합니다")\n'
                    'print("2단계: 파일을 저장합니다 (Ctrl+S)")\n'
                    'print("3단계: 터미널에서 실행합니다")\n'
                    'print("4단계: 결과를 확인합니다")\n'
                    'print("5단계: 필요하면 수정하고 반복합니다")\n'
                    'print("==========================")'
                ),
            },
            {"type": "heading", "text": "자주 하는 실수와 해결법"},
            {
                "type": "table",
                "headers": ["증상", "원인", "해결 방법"],
                "rows": [
                    [
                        "python3: command not found",
                        "Python이 PATH에 등록되지 않음",
                        "Python 재설치 (PATH 옵션 체크)",
                    ],
                    [
                        "SyntaxError: invalid syntax",
                        "문법 오류 (괄호, 따옴표 누락 등)",
                        "에러 메시지의 줄 번호를 확인하고 수정",
                    ],
                    [
                        "FileNotFoundError",
                        "파일이 없는 위치에서 실행",
                        "cd 명령으로 파일이 있는 폴더로 이동",
                    ],
                    [
                        "저장 안 한 코드 실행",
                        "수정 후 Ctrl+S를 안 누름",
                        "저장(Ctrl+S) 후 다시 실행",
                    ],
                ],
            },
            {
                "type": "note",
                "text": (
                    "에러는 '실패'가 아니라 '피드백'입니다. "
                    "Python의 에러 메시지는 매우 친절하게 어디서 무엇이 잘못되었는지 알려줍니다. "
                    "에러를 두려워하지 말고, 메시지를 차근차근 읽는 습관을 들이세요."
                ),
            },
        ],
    }
