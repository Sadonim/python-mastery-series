"""챕터 5: 파일 입출력 — 데이터를 영구적으로 저장하는 법."""


def get_chapter():
    """챕터 5 콘텐츠를 반환한다."""
    return {
        "number": 5,
        "title": "파일 입출력",
        "subtitle": "데이터를 영구적으로 저장하는 법",
        "big_picture": (
            "프로그램이 종료되면 메모리의 모든 데이터는 사라집니다. "
            "데이터를 영구적으로 보존하려면 파일에 저장해야 합니다. "
            "Python은 텍스트 파일, CSV, JSON 등 다양한 형식을 "
            "간결하고 안전하게 다루는 도구를 내장하고 있습니다. "
            "파일 입출력은 설정 저장, 로그 기록, 데이터 분석의 첫걸음입니다."
        ),
        "sections": [
            # ── 섹션 1: open() 함수와 파일 모드 ─────────────────
            {
                "title": "open() 함수와 파일 모드",
                "content": [
                    "파일을 다루는 모든 작업은 `open()` 함수로 시작합니다. "
                    "어떤 목적으로 파일을 열지는 '모드' 문자열로 지정합니다.",
                    {
                        "type": "table",
                        "headers": ["모드", "의미", "파일 없으면", "기존 내용"],
                        "rows": [
                            ["r", "읽기 (기본값)", "FileNotFoundError", "유지"],
                            ["w", "쓰기", "새로 생성", "덮어씀 (삭제)"],
                            ["a", "추가 쓰기", "새로 생성", "유지, 끝에 추가"],
                            ["x", "배타적 생성", "새로 생성", "이미 있으면 FileExistsError"],
                            ["r+", "읽기+쓰기", "FileNotFoundError", "유지"],
                            ["rb", "이진 읽기", "FileNotFoundError", "유지"],
                            ["wb", "이진 쓰기", "새로 생성", "덮어씀"],
                        ],
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "파일 모드는 도서관 열람 규칙과 같습니다. "
                            "r은 '열람만 가능', w는 '새 노트로 교체', "
                            "a는 '기존 노트 뒤에 이어 쓰기', "
                            "rb/wb는 '일반 글이 아닌 이미지나 음원 파일 전용' 입니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 open/close 패턴 (권장하지 않음)\n"
                            "f = open('hello.txt', 'w', encoding='utf-8')\n"
                            "f.write('안녕하세요!\\n')\n"
                            "f.close()  # 반드시 닫아야 함 — 실수로 빠뜨리기 쉬움\n\n"
                            "# with 문을 사용한 패턴 (권장)\n"
                            "with open('hello.txt', 'w', encoding='utf-8') as f:\n"
                            "    f.write('안녕하세요!\\n')  # 블록 종료 시 자동으로 close()"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "파일을 열고 닫지 않으면 데이터가 디스크에 기록되지 않거나 "
                            "다른 프로그램이 파일에 접근하지 못할 수 있습니다. "
                            "항상 `with` 문을 사용하여 자동으로 닫히도록 하세요."
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "한글 텍스트 파일을 다룰 때는 항상 `encoding='utf-8'`을 명시하세요. "
                            "Windows에서는 기본 인코딩이 cp949(EUC-KR)라 오류가 발생할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 텍스트 파일 읽기/쓰기 ──────────────────
            {
                "title": "텍스트 파일 읽기와 쓰기",
                "content": [
                    "파일 객체는 내용을 읽는 세 가지 주요 메서드를 제공합니다. "
                    "상황에 따라 적절한 메서드를 선택하세요.",
                    {
                        "type": "table",
                        "headers": ["메서드", "반환값", "주요 사용 상황"],
                        "rows": [
                            ["read()", "파일 전체를 하나의 문자열로", "작은 파일 전체 읽기"],
                            ["readline()", "한 줄 문자열 (\\n 포함)", "한 줄씩 처리할 때"],
                            ["readlines()", "모든 줄의 리스트", "줄을 리스트로 다룰 때"],
                            ["for line in f:", "줄 단위 이터레이션", "대용량 파일 (메모리 효율)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 파일 쓰기\n"
                            "lines = [\n"
                            "    '이름,나이,직책\\n',\n"
                            "    '김철수,25,일병\\n',\n"
                            "    '이영희,23,이병\\n',\n"
                            "    '박민수,27,병장\\n',\n"
                            "]\n\n"
                            "with open('personnel.txt', 'w', encoding='utf-8') as f:\n"
                            "    f.writelines(lines)  # 리스트의 각 항목을 순서대로 씀\n\n\n"
                            "# 방법 1: read() — 전체를 한 문자열로\n"
                            "with open('personnel.txt', encoding='utf-8') as f:\n"
                            "    content = f.read()\n"
                            "print(content)\n\n"
                            "# 방법 2: readlines() — 줄 목록 반환\n"
                            "with open('personnel.txt', encoding='utf-8') as f:\n"
                            "    all_lines = f.readlines()\n"
                            "print(all_lines[0])  # '이름,나이,직책\\n'\n\n"
                            "# 방법 3: for 루프 — 가장 권장 (메모리 효율적)\n"
                            "with open('personnel.txt', encoding='utf-8') as f:\n"
                            "    for line in f:\n"
                            "        print(line.strip())  # strip()으로 \\n 제거"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 파일 추가(append) — 기존 내용 유지\n"
                            "with open('log.txt', 'a', encoding='utf-8') as f:\n"
                            "    f.write('2026-03-27 09:00 — 훈련 시작\\n')\n"
                            "    f.write('2026-03-27 17:00 — 훈련 종료\\n')\n\n"
                            "# 여러 줄 한번에 쓰기\n"
                            "with open('report.txt', 'w', encoding='utf-8') as f:\n"
                            "    f.write('=== 주간 보고서 ===\\n')\n"
                            "    f.write(f'작성일: 2026-03-27\\n')\n"
                            "    f.write(f'내용: 정상 완료\\n')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "대용량 파일을 처리할 때는 `read()`나 `readlines()`로 "
                            "전체를 메모리에 올리지 말고, `for line in f:` 방식을 사용하세요. "
                            "수 GB 파일도 메모리 부담 없이 처리할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: CSV 파일 다루기 ──────────────────────────
            {
                "title": "CSV 파일 다루기",
                "content": [
                    "CSV(Comma-Separated Values)는 스프레드시트 데이터를 저장하는 "
                    "가장 널리 쓰이는 형식입니다. "
                    "Python의 `csv` 모듈은 쉼표, 따옴표, 개행이 섞인 복잡한 CSV를 "
                    "안전하게 처리합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "CSV는 엑셀의 간소화 버전입니다. "
                            "서식(색, 폰트)은 없지만 데이터 자체는 완벽히 저장됩니다. "
                            "거의 모든 프로그램과 언어가 읽을 수 있어 "
                            "데이터 교환의 표준 형식으로 쓰입니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import csv\n\n\n"
                            "# CSV 파일 쓰기\n"
                            "soldiers = [\n"
                            "    ['이름', '계급', '점수'],\n"
                            "    ['김철수', '병장', 92],\n"
                            "    ['이영희', '상병', 88],\n"
                            "    ['박민수', '일병', 75],\n"
                            "]\n\n"
                            "with open('soldiers.csv', 'w', newline='', encoding='utf-8-sig') as f:\n"
                            "    # utf-8-sig: 엑셀에서 한글 깨짐 방지\n"
                            "    writer = csv.writer(f)\n"
                            "    writer.writerows(soldiers)  # 여러 행 한번에 쓰기\n\n\n"
                            "# CSV 파일 읽기\n"
                            "with open('soldiers.csv', encoding='utf-8-sig') as f:\n"
                            "    reader = csv.reader(f)\n"
                            "    header = next(reader)  # 첫 줄(헤더) 별도 처리\n"
                            "    print(f'헤더: {header}')\n"
                            "    for row in reader:\n"
                            "        name, rank, score = row\n"
                            "        print(f'{name} ({rank}): {score}점')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import csv\n\n\n"
                            "# DictWriter / DictReader — 딕셔너리 방식 (더 편리)\n"
                            "records = [\n"
                            "    {'이름': '김철수', '계급': '병장', '점수': 92},\n"
                            "    {'이름': '이영희', '계급': '상병', '점수': 88},\n"
                            "]\n\n"
                            "fieldnames = ['이름', '계급', '점수']\n\n"
                            "with open('soldiers_dict.csv', 'w', newline='', encoding='utf-8-sig') as f:\n"
                            "    writer = csv.DictWriter(f, fieldnames=fieldnames)\n"
                            "    writer.writeheader()   # 헤더 자동 작성\n"
                            "    writer.writerows(records)\n\n\n"
                            "# DictReader: 각 행이 딕셔너리로 반환됨\n"
                            "with open('soldiers_dict.csv', encoding='utf-8-sig') as f:\n"
                            "    reader = csv.DictReader(f)\n"
                            "    for row in reader:\n"
                            "        print(f\"{row['이름']}: {row['점수']}점\")"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "CSV 쓰기 시 `newline=''`을 지정해야 합니다. "
                            "지정하지 않으면 Windows에서 빈 줄이 중간에 삽입됩니다. "
                            "또한 한글 파일을 엑셀에서 열 때는 `utf-8-sig` 인코딩을 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: JSON 파일 다루기 ─────────────────────────
            {
                "title": "JSON 파일 다루기",
                "content": [
                    "JSON(JavaScript Object Notation)은 웹 API와 설정 파일에 가장 많이 쓰이는 "
                    "데이터 교환 형식입니다. "
                    "Python의 딕셔너리, 리스트와 구조가 거의 동일해 변환이 매우 자연스럽습니다.",
                    {
                        "type": "table",
                        "headers": ["Python 타입", "JSON 타입", "예시"],
                        "rows": [
                            ["dict", "object", '{"name": "철수"}'],
                            ["list", "array", "[1, 2, 3]"],
                            ["str", "string", '"안녕하세요"'],
                            ["int / float", "number", "42 / 3.14"],
                            ["True / False", "true / false", "true"],
                            ["None", "null", "null"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n\n\n"
                            "# Python 객체 → JSON 파일 저장 (직렬화)\n"
                            "config = {\n"
                            "    'server': {\n"
                            "        'host': 'localhost',\n"
                            "        'port': 8080,\n"
                            "    },\n"
                            "    'debug': True,\n"
                            "    'allowed_users': ['admin', '철수', '영희'],\n"
                            "    'max_connections': 100,\n"
                            "}\n\n"
                            "with open('config.json', 'w', encoding='utf-8') as f:\n"
                            "    json.dump(config, f, ensure_ascii=False, indent=4)\n"
                            "    # ensure_ascii=False: 한글을 \\uXXXX 대신 그대로 저장\n"
                            "    # indent=4: 들여쓰기 4칸으로 읽기 좋게 저장\n\n\n"
                            "# JSON 파일 → Python 객체 로드 (역직렬화)\n"
                            "with open('config.json', encoding='utf-8') as f:\n"
                            "    loaded = json.load(f)\n\n"
                            "print(loaded['server']['host'])     # localhost\n"
                            "print(loaded['allowed_users'][0])   # admin\n"
                            "print(type(loaded['debug']))         # <class 'bool'>"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n\n\n"
                            "# 문자열과 JSON 간 변환 (파일 없이)\n"
                            "data = {'이름': '김철수', '점수': 95}\n\n"
                            "json_str = json.dumps(data, ensure_ascii=False)\n"
                            "print(json_str)      # {\"이름\": \"김철수\", \"점수\": 95}\n\n"
                            "recovered = json.loads(json_str)\n"
                            "print(recovered['점수'])  # 95\n\n\n"
                            "# JSON 읽기 오류 처리\n"
                            "def load_json_safe(filepath):\n"
                            "    \"\"\"JSON 파일을 안전하게 읽는다.\"\"\"\n"
                            "    try:\n"
                            "        with open(filepath, encoding='utf-8') as f:\n"
                            "            return json.load(f)\n"
                            "    except FileNotFoundError:\n"
                            "        print(f'파일 없음: {filepath}')\n"
                            "        return {}\n"
                            "    except json.JSONDecodeError as e:\n"
                            "        print(f'JSON 형식 오류: {e}')\n"
                            "        return {}"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "설정 파일은 JSON으로 저장하면 사람이 읽고 수정하기 쉽습니다. "
                            "`indent=4`와 `ensure_ascii=False`를 항상 함께 사용하세요. "
                            "민감한 설정(비밀번호, API 키)은 JSON에 직접 쓰지 말고 "
                            "환경변수나 별도의 비밀 관리 도구를 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 파일 경로 다루기 ─────────────────────────
            {
                "title": "파일 경로 다루기: os.path와 pathlib",
                "content": [
                    "파일 경로를 문자열로 직접 다루면 운영체제마다 구분자가 달라 문제가 생깁니다. "
                    "Python은 경로를 안전하게 다루는 두 가지 방법을 제공합니다.",
                    {
                        "type": "table",
                        "headers": ["방법", "설명", "스타일"],
                        "rows": [
                            ["os.path", "함수 기반, Python 2부터 존재", "전통적"],
                            ["pathlib.Path", "객체 기반, Python 3.4+, 직관적", "현대적 (권장)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from pathlib import Path\n\n\n"
                            "# 경로 생성\n"
                            "base = Path('data')              # 상대 경로\n"
                            "home = Path.home()               # 홈 디렉토리\n"
                            "config = home / 'config.json'   # / 연산자로 경로 합치기\n\n"
                            "print(config)  # /Users/sadonim/config.json (OS에 맞게 자동)\n\n"
                            "# 경로 정보 추출\n"
                            "p = Path('/data/reports/2026/report.csv')\n"
                            "print(p.name)        # report.csv\n"
                            "print(p.stem)        # report\n"
                            "print(p.suffix)      # .csv\n"
                            "print(p.parent)      # /data/reports/2026\n"
                            "print(p.parts)       # ('/', 'data', 'reports', '2026', 'report.csv')\n\n"
                            "# 존재 여부·타입 확인\n"
                            "print(p.exists())    # True/False\n"
                            "print(p.is_file())   # 파일 여부\n"
                            "print(p.is_dir())    # 디렉토리 여부"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from pathlib import Path\n\n\n"
                            "# 디렉토리 생성\n"
                            "output_dir = Path('output') / '2026'\n"
                            "output_dir.mkdir(parents=True, exist_ok=True)\n"
                            "# parents=True: 중간 디렉토리도 생성\n"
                            "# exist_ok=True: 이미 있어도 오류 없음\n\n"
                            "# 디렉토리 내 파일 목록\n"
                            "data_dir = Path('data')\n"
                            "if data_dir.exists():\n"
                            "    csv_files = list(data_dir.glob('*.csv'))  # CSV만\n"
                            "    all_files = list(data_dir.rglob('*'))     # 재귀 탐색\n"
                            "    print(f'CSV 파일 수: {len(csv_files)}')\n\n"
                            "# pathlib으로 파일 직접 읽기/쓰기\n"
                            "config_path = Path('settings.txt')\n"
                            "config_path.write_text('host=localhost\\nport=8080', encoding='utf-8')\n"
                            "content = config_path.read_text(encoding='utf-8')\n"
                            "print(content)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "경로 구분자를 직접 쓰지 마세요. "
                            "Windows는 `\\`, macOS/Linux는 `/`를 사용합니다. "
                            "`Path` 객체와 `/` 연산자를 쓰면 운영체제가 알아서 처리합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 인코딩과 실용 예제 ───────────────────────
            {
                "title": "인코딩 이슈와 실용 예제",
                "content": [
                    "한글 파일을 다룰 때 인코딩 문제는 흔한 함정입니다. "
                    "원리를 이해하면 쉽게 해결할 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["인코딩", "특징", "사용 상황"],
                        "rows": [
                            ["UTF-8", "전 세계 표준, 한글 3바이트", "신규 파일, 웹, macOS/Linux"],
                            ["UTF-8-SIG", "UTF-8 + BOM 시그니처", "엑셀에서 한글 CSV 열 때"],
                            ["EUC-KR (cp949)", "한글 전용, 2바이트", "오래된 한국 시스템 파일"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 인코딩 오류 처리 패턴\n"
                            "def read_text_safe(filepath):\n"
                            "    \"\"\"인코딩을 자동 감지하며 파일을 읽는다.\"\"\"\n"
                            "    encodings = ['utf-8', 'utf-8-sig', 'euc-kr', 'cp949']\n"
                            "    for encoding in encodings:\n"
                            "        try:\n"
                            "            with open(filepath, encoding=encoding) as f:\n"
                            "                content = f.read()\n"
                            "                print(f'인코딩 성공: {encoding}')\n"
                            "                return content\n"
                            "        except UnicodeDecodeError:\n"
                            "            continue  # 다음 인코딩 시도\n"
                            "    raise ValueError(f'알 수 없는 인코딩: {filepath}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실용 예제 1: 설정 파일 로더",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n"
                            "from pathlib import Path\n\n\n"
                            "class ConfigLoader:\n"
                            "    \"\"\"JSON 설정 파일을 로드하고 관리하는 클래스.\"\"\"\n\n"
                            "    def __init__(self, filepath, defaults=None):\n"
                            "        self._path = Path(filepath)\n"
                            "        self._defaults = defaults or {}\n"
                            "        self._config = self._load()\n\n"
                            "    def _load(self):\n"
                            "        \"\"\"파일에서 설정을 로드한다. 없으면 기본값 사용.\"\"\"\n"
                            "        if not self._path.exists():\n"
                            "            print(f'설정 파일 없음. 기본값 사용: {self._path}')\n"
                            "            return dict(self._defaults)\n"
                            "        try:\n"
                            "            with open(self._path, encoding='utf-8') as f:\n"
                            "                loaded = json.load(f)\n"
                            "                # 기본값과 병합 (기본값은 새 키에만 적용)\n"
                            "                return {**self._defaults, **loaded}\n"
                            "        except json.JSONDecodeError as e:\n"
                            "            print(f'설정 파일 형식 오류: {e}')\n"
                            "            return dict(self._defaults)\n\n"
                            "    def get(self, key, default=None):\n"
                            "        \"\"\"설정값을 가져온다.\"\"\"\n"
                            "        return self._config.get(key, default)\n\n"
                            "    def save(self):\n"
                            "        \"\"\"현재 설정을 파일에 저장한다.\"\"\"\n"
                            "        self._path.parent.mkdir(parents=True, exist_ok=True)\n"
                            "        with open(self._path, 'w', encoding='utf-8') as f:\n"
                            "            json.dump(self._config, f, ensure_ascii=False, indent=4)\n\n\n"
                            "# 사용 예\n"
                            "defaults = {'host': 'localhost', 'port': 8080, 'debug': False}\n"
                            "cfg = ConfigLoader('app_config.json', defaults=defaults)\n"
                            "print(cfg.get('host'))    # localhost\n"
                            "print(cfg.get('port'))    # 8080"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실용 예제 2: 로그 파일 분석기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from pathlib import Path\n"
                            "from collections import Counter\n\n\n"
                            "def analyze_log(log_path):\n"
                            "    \"\"\"로그 파일을 분석하여 통계를 반환한다.\"\"\"\n"
                            "    path = Path(log_path)\n"
                            "    if not path.exists():\n"
                            "        raise FileNotFoundError(f'로그 파일 없음: {log_path}')\n\n"
                            "    level_counts = Counter()\n"
                            "    error_lines = []\n"
                            "    total_lines = 0\n\n"
                            "    with open(path, encoding='utf-8') as f:\n"
                            "        for line in f:  # 대용량도 한 줄씩 처리\n"
                            "            line = line.strip()\n"
                            "            if not line:\n"
                            "                continue\n"
                            "            total_lines += 1\n\n"
                            "            # 로그 레벨 추출 (예: [ERROR], [WARNING], [INFO])\n"
                            "            for level in ('ERROR', 'WARNING', 'INFO', 'DEBUG'):\n"
                            "                if f'[{level}]' in line:\n"
                            "                    level_counts[level] += 1\n"
                            "                    if level == 'ERROR':\n"
                            "                        error_lines.append(line)\n"
                            "                    break\n\n"
                            "    return {\n"
                            "        'total': total_lines,\n"
                            "        'counts': dict(level_counts),\n"
                            "        'errors': error_lines,\n"
                            "    }\n\n\n"
                            "# 사용 예\n"
                            "# result = analyze_log('server.log')\n"
                            "# print(f'총 {result[\"total\"]}줄, 오류 {result[\"counts\"].get(\"ERROR\", 0)}건')\n"
                            "# for err in result['errors']:\n"
                            "#     print(f'  {err}')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "대용량 로그 파일(수 GB)을 처리할 때는 "
                            "`for line in f:` 방식을 사용하세요. "
                            "`readlines()`는 전체를 메모리에 올려 시스템이 멈출 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "파일 작업은 항상 with 문을 사용하세요. 예외가 발생해도 파일이 자동으로 닫힙니다.",
            "한글 텍스트 파일에는 encoding='utf-8'을 항상 명시하세요.",
            "경로는 문자열 대신 pathlib.Path를 사용하면 운영체제에 독립적입니다.",
            "파일이 존재하는지 먼저 확인하거나 try-except FileNotFoundError로 처리하세요.",
            "CSV를 엑셀에서 열 때 한글 깨짐을 막으려면 encoding='utf-8-sig'를 사용하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "기존 파일의 내용을 유지하면서 끝에 새 내용을 추가하는 파일 모드는?"
                ),
                "choices": [
                    "A) r",
                    "B) w",
                    "C) a",
                    "D) x",
                ],
                "answer": "C",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "대용량 파일을 메모리 효율적으로 처리하는 가장 좋은 방법은?",
                "choices": [
                    "A) f.read()로 전체를 한번에 읽는다",
                    "B) f.readlines()로 모든 줄을 리스트로 읽는다",
                    "C) for line in f: 로 한 줄씩 처리한다",
                    "D) f.readline()을 수동으로 반복 호출한다",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "pathlib.Path에서 경로를 합칠 때 사용하는 연산자는?",
                "choices": [
                    "A) +",
                    "B) //",
                    "C) /",
                    "D) os.join()",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "텍스트 파일의 각 줄에서 단어 수를 세어 "
                    "{'총 줄 수': N, '총 단어 수': M} 형태의 딕셔너리를 반환하는 "
                    "함수 `count_words(filepath)`를 작성하세요."
                ),
                "hint": (
                    "with open(filepath, encoding='utf-8') as f: 후 "
                    "for line in f: 로 각 줄을 처리합니다. "
                    "line.split()의 길이가 단어 수입니다."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "학생 딕셔너리 리스트를 CSV 파일로 저장하고 "
                    "다시 읽어오는 두 함수를 작성하세요. "
                    "save_students(students, filepath)와 "
                    "load_students(filepath) → list[dict]"
                ),
                "hint": (
                    "csv.DictWriter와 csv.DictReader를 사용합니다. "
                    "fieldnames는 첫 번째 딕셔너리의 키로 결정하세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "간단한 메모장 프로그램을 파일 입출력으로 구현하세요. "
                "메모는 JSON 파일('notes.json')에 리스트로 저장됩니다. "
                "기능: 1) 메모 추가 (내용 입력 후 저장), "
                "2) 전체 메모 보기 (번호 포함), "
                "3) 메모 삭제 (번호로 선택), "
                "4) 종료. "
                "프로그램을 재시작해도 이전 메모가 유지되어야 합니다."
            ),
            "hint": (
                "시작 시 notes.json을 load하고 (없으면 빈 리스트), "
                "추가/삭제 후 매번 json.dump로 저장합니다. "
                "삭제 시 인덱스 범위 초과를 try-except IndexError로 처리하세요."
            ),
        },
        "summary": [
            "open()으로 파일을 열고 with 문으로 감싸면 예외 시에도 자동으로 닫힌다.",
            "파일 모드: r(읽기), w(덮어쓰기), a(추가), rb/wb(이진)를 목적에 맞게 선택한다.",
            "대용량 파일은 for line in f: 방식으로 한 줄씩 처리해 메모리를 절약한다.",
            "csv 모듈의 DictWriter/DictReader로 딕셔너리 형태로 CSV를 쉽게 다룬다.",
            "json 모듈의 dump/load로 Python 객체를 JSON 파일로 저장하고 복원한다.",
            "pathlib.Path는 운영체제에 독립적인 경로 처리를 제공하며 현대적 방법으로 권장된다.",
        ],
    }
