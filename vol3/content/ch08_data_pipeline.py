"""챕터 8: 데이터 파이프라인 구축 — 수집부터 저장까지 자동화하는 법."""


def get_chapter():
    """챕터 8 콘텐츠를 반환한다."""
    return {
        "number": 8,
        "title": "데이터 파이프라인 구축",
        "subtitle": "수집부터 저장까지 자동화하는 법",
        "big_picture": (
            "데이터를 한 번만 수집하는 것으로는 충분하지 않습니다. "
            "실제 데이터 분석 프로젝트는 수집 → 정제 → 저장 → 분석의 흐름이 "
            "반복적으로 실행되어야 합니다. "
            "이 흐름을 파이프라인이라고 부릅니다. "
            "이 챕터에서는 ETL 개념부터 pandas 전처리, 데이터 품질 검증, "
            "CSV/JSON/SQLite 저장, 그리고 자동화 기초까지 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: ETL 개념과 파이프라인 설계 ──────────────
            {
                "title": "ETL 개념과 데이터 파이프라인 설계",
                "content": [
                    "ETL은 Extract(추출) → Transform(변환) → Load(적재)의 약자로, "
                    "데이터 엔지니어링의 핵심 패턴입니다. "
                    "각 단계를 명확히 분리하면 유지보수와 디버깅이 쉬워집니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "ETL은 음식 재료 처리와 같습니다. "
                            "Extract는 시장에서 재료 구입(API, 스크래핑, 파일 읽기), "
                            "Transform은 재료 손질·조리(정제, 변환, 집계), "
                            "Load는 그릇에 담아 냉장고에 저장(CSV, DB, JSON)입니다. "
                            "각 단계가 명확히 분리되어야 중간에 문제가 생겨도 해당 단계만 고칠 수 있습니다."
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "title": "ETL 데이터 파이프라인 흐름",
                        "steps": [
                            "Extract: 데이터 수집 (API / 웹 스크래핑 / 파일 읽기)",
                            "Validate: 원본 데이터 품질 검증 (필수 필드, 타입 체크)",
                            "Transform: 정제 및 변환 (결측값 처리, 형 변환, 집계)",
                            "Validate: 변환 결과 품질 검증 (범위, 일관성 확인)",
                            "Load: 저장 (CSV / JSON / SQLite / 데이터베이스)",
                            "Report: 결과 리포트 생성 및 로그 기록",
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["ETL 단계", "주요 작업", "Python 도구"],
                        "rows": [
                            ["Extract", "API 호출, 파일 읽기, 스크래핑", "requests, BeautifulSoup, pandas"],
                            ["Transform", "결측값 처리, 형 변환, 정규화, 집계", "pandas, numpy"],
                            ["Load", "파일/DB 저장, 리포트 생성", "pandas, sqlite3, json"],
                            ["Validate", "타입·범위·필수값 검증", "assert, pandas, pydantic"],
                            ["Orchestrate", "단계 연결, 로깅, 오류 처리", "logging, 함수 합성"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 파이프라인 설계 패턴: 각 단계를 독립 함수로 분리\n"
                            "import logging\n\n\n"
                            "logging.basicConfig(\n"
                            "    level=logging.INFO,\n"
                            "    format='%(asctime)s [%(levelname)s] %(message)s',\n"
                            ")\n"
                            "logger = logging.getLogger(__name__)\n\n\n"
                            "def run_pipeline(config):\n"
                            "    \"\"\"ETL 파이프라인을 실행한다.\"\"\"\n"
                            "    logger.info('파이프라인 시작')\n\n"
                            "    # 1단계: 추출\n"
                            "    raw_data = extract(config['source'])\n"
                            "    logger.info(f'추출 완료: {len(raw_data)}건')\n\n"
                            "    # 2단계: 변환\n"
                            "    clean_data = transform(raw_data)\n"
                            "    logger.info(f'변환 완료: {len(clean_data)}건')\n\n"
                            "    # 3단계: 적재\n"
                            "    load(clean_data, config['output'])\n"
                            "    logger.info(f'저장 완료: {config[\"output\"]}')\n\n"
                            "    return clean_data\n\n\n"
                            "# 각 단계는 단일 책임 원칙에 따라 분리\n"
                            "def extract(source): ...\n"
                            "def transform(data): ...\n"
                            "def load(data, output): ..."
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "파이프라인의 각 단계를 독립된 함수로 분리하면 "
                            "단위 테스트가 쉬워지고, "
                            "특정 단계에서 오류 발생 시 해당 단계만 수정할 수 있습니다. "
                            "함수는 50줄 이내, 한 가지 역할만 담당하도록 설계하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 2: pandas 전처리 파이프라인 ─────────────────
            {
                "title": "pandas 전처리 파이프라인: pipe와 메서드 체이닝",
                "content": [
                    "pandas는 데이터 변환을 연쇄적으로 적용하는 "
                    "메서드 체이닝(method chaining)과 pipe() 패턴을 지원합니다. "
                    "이를 활용하면 전처리 과정을 읽기 쉽고 재사용 가능하게 작성할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "# 샘플 데이터: 날씨 관측 데이터\n"
                            "raw = pd.DataFrame({\n"
                            "    'date': ['2026-03-01', '2026-03-02', None, '2026-03-04'],\n"
                            "    'temp': [5.2, None, 8.1, 9.9],\n"
                            "    'humidity': [60, 75, 200, 55],  # 200은 잘못된 값\n"
                            "    'city': ['  서울  ', '부산', '인천', '서울'],\n"
                            "})\n\n\n"
                            "# 일반적인 방식 (단계별 변수 할당) — 읽기 어려움\n"
                            "df1 = raw.dropna(subset=['date'])\n"
                            "df2 = df1.copy()\n"
                            "df2['city'] = df2['city'].str.strip()\n"
                            "df3 = df2.fillna({'temp': df2['temp'].median()})\n"
                            "df4 = df3[df3['humidity'] <= 100]\n\n\n"
                            "# 메서드 체이닝 방식 — 흐름이 명확\n"
                            "clean = (\n"
                            "    raw\n"
                            "    .dropna(subset=['date'])          # 날짜 없는 행 제거\n"
                            "    .assign(city=lambda df: df['city'].str.strip())  # 공백 제거\n"
                            "    .assign(temp=lambda df: df['temp'].fillna(df['temp'].median()))\n"
                            "    .query('humidity <= 100')         # 유효하지 않은 습도 제거\n"
                            "    .reset_index(drop=True)           # 인덱스 초기화\n"
                            ")\n"
                            "print(clean)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "# pipe(): 커스텀 함수를 체이닝에 포함\n"
                            "def drop_duplicates_by(df, subset):\n"
                            "    \"\"\"지정된 열 기준으로 중복 행을 제거한다.\"\"\"\n"
                            "    before = len(df)\n"
                            "    result = df.drop_duplicates(subset=subset)\n"
                            "    dropped = before - len(result)\n"
                            "    if dropped:\n"
                            "        print(f'중복 제거: {dropped}건')\n"
                            "    return result\n\n\n"
                            "def normalize_columns(df):\n"
                            "    \"\"\"컬럼명을 소문자 스네이크케이스로 정규화한다.\"\"\"\n"
                            "    df = df.copy()\n"
                            "    df.columns = (\n"
                            "        df.columns\n"
                            "        .str.strip()\n"
                            "        .str.lower()\n"
                            "        .str.replace(' ', '_', regex=False)\n"
                            "    )\n"
                            "    return df\n\n\n"
                            "# pipe()로 커스텀 함수를 체인에 포함\n"
                            "raw = pd.DataFrame({\n"
                            "    'Date': ['2026-03-01', '2026-03-01', '2026-03-03'],\n"
                            "    'City Name': ['서울', '서울', '부산'],\n"
                            "    'Temp C': [5.2, 5.2, 8.1],\n"
                            "})\n\n"
                            "clean = (\n"
                            "    raw\n"
                            "    .pipe(normalize_columns)              # 컬럼명 정규화\n"
                            "    .pipe(drop_duplicates_by, subset=['date', 'city_name'])\n"
                            "    .rename(columns={'temp_c': 'temp'})\n"
                            ")\n"
                            "print(clean.columns.tolist())  # ['date', 'city_name', 'temp']"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "assign()은 기존 DataFrame을 변경하지 않고 새 열을 추가한 "
                            "새 DataFrame을 반환합니다. "
                            "메서드 체이닝에서 원본 데이터를 보존하는 핵심 메서드입니다. "
                            "lambda df:를 사용하면 이전 단계의 결과를 참조할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 데이터 품질 검증 ──────────────────────────
            {
                "title": "데이터 품질 검증",
                "content": [
                    "데이터 파이프라인에서 품질 검증은 오류가 조용히 전파되는 것을 방지합니다. "
                    "추출 직후와 변환 후 두 번 검증하는 것이 좋습니다.",
                    {
                        "type": "table",
                        "headers": ["검증 항목", "확인 내용", "pandas/Python 방법"],
                        "rows": [
                            ["스키마 검증", "필수 컬럼 존재 여부", "assert set(cols) <= set(df.columns)"],
                            ["타입 검증", "데이터 타입 일치", "df['col'].dtype"],
                            ["결측값 검증", "허용 범위 내 결측값", "df.isnull().sum()"],
                            ["범위 검증", "값이 유효 범위 내", "assert df['temp'].between(-50, 60).all()"],
                            ["중복 검증", "키 열의 고유성", "assert not df.duplicated(subset=key).any()"],
                            ["행 수 검증", "최소 행 수 확보", "assert len(df) >= min_rows"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "class DataValidator:\n"
                            "    \"\"\"DataFrame 데이터 품질을 검증하는 클래스.\"\"\"\n\n"
                            "    def __init__(self, df, name='DataFrame'):\n"
                            "        self._df = df\n"
                            "        self._name = name\n"
                            "        self._errors = []\n\n"
                            "    def has_columns(self, *cols):\n"
                            "        \"\"\"필수 컬럼이 모두 존재하는지 확인한다.\"\"\"\n"
                            "        missing = [c for c in cols if c not in self._df.columns]\n"
                            "        if missing:\n"
                            "            self._errors.append(f'필수 컬럼 없음: {missing}')\n"
                            "        return self\n\n"
                            "    def no_nulls(self, *cols):\n"
                            "        \"\"\"지정된 컬럼에 결측값이 없는지 확인한다.\"\"\"\n"
                            "        for col in cols:\n"
                            "            if col in self._df.columns:\n"
                            "                null_count = self._df[col].isnull().sum()\n"
                            "                if null_count:\n"
                            "                    self._errors.append(\n"
                            "                        f'{col}: 결측값 {null_count}건'\n"
                            "                    )\n"
                            "        return self\n\n"
                            "    def in_range(self, col, min_val, max_val):\n"
                            "        \"\"\"값이 유효 범위 내에 있는지 확인한다.\"\"\"\n"
                            "        if col in self._df.columns:\n"
                            "            out = (~self._df[col].between(min_val, max_val)).sum()\n"
                            "            if out:\n"
                            "                self._errors.append(\n"
                            "                    f'{col}: 범위 초과 {out}건 ({min_val}~{max_val})'\n"
                            "                )\n"
                            "        return self\n\n"
                            "    def min_rows(self, count):\n"
                            "        \"\"\"최소 행 수를 충족하는지 확인한다.\"\"\"\n"
                            "        if len(self._df) < count:\n"
                            "            self._errors.append(\n"
                            "                f'행 수 부족: {len(self._df)} < {count}'\n"
                            "            )\n"
                            "        return self\n\n"
                            "    def validate(self, strict=True):\n"
                            "        \"\"\"검증 결과를 반환하고, strict=True이면 예외를 발생시킨다.\"\"\"\n"
                            "        if self._errors:\n"
                            "            msg = f'{self._name} 검증 실패:\\n  ' + '\\n  '.join(self._errors)\n"
                            "            if strict:\n"
                            "                raise ValueError(msg)\n"
                            "            print(f'[경고] {msg}')\n"
                            "        return len(self._errors) == 0"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "# DataValidator 사용 예\n"
                            "df = pd.DataFrame({\n"
                            "    'date': ['2026-03-01', '2026-03-02', '2026-03-03'],\n"
                            "    'temp': [5.2, 8.1, 9.9],\n"
                            "    'humidity': [60, 75, 55],\n"
                            "})\n\n"
                            "# 체이닝으로 여러 검증을 한번에 실행\n"
                            "DataValidator(df, '날씨 데이터') \\\n"
                            "    .has_columns('date', 'temp', 'humidity') \\\n"
                            "    .no_nulls('date', 'temp') \\\n"
                            "    .in_range('temp', -50, 60) \\\n"
                            "    .in_range('humidity', 0, 100) \\\n"
                            "    .min_rows(1) \\\n"
                            "    .validate(strict=True)  # 오류 있으면 ValueError 발생\n\n"
                            "print('검증 통과!')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "데이터 검증을 생략하면 잘못된 데이터가 파이프라인을 타고 내려가 "
                            "분석 결과를 조용히 왜곡합니다. "
                            "특히 외부 API나 웹 스크래핑으로 수집한 데이터는 "
                            "언제든 형식이 바뀔 수 있으므로 반드시 검증하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: CSV/JSON/SQLite로 결과 저장 ──────────────
            {
                "title": "CSV, JSON, SQLite로 결과 저장",
                "content": [
                    "파이프라인의 최종 단계는 처리된 데이터를 적절한 형식으로 저장하는 것입니다. "
                    "용도에 따라 CSV, JSON, SQLite를 선택합니다.",
                    {
                        "type": "table",
                        "headers": ["형식", "장점", "단점", "적합한 용도"],
                        "rows": [
                            ["CSV", "범용 호환, 엑셀에서 열기 쉬움", "중첩 구조 표현 어려움", "표 형태 데이터, 공유"],
                            ["JSON", "중첩 구조, 사람이 읽기 쉬움", "대용량 느림", "설정, API 응답, 중첩 데이터"],
                            ["SQLite", "쿼리 가능, 관계형 데이터", "설정 필요, 동시 쓰기 제한", "누적 데이터, 조회 필요 시"],
                            ["Parquet", "압축률 높음, 고성능", "바이너리, 전용 도구 필요", "대용량 분석 데이터"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n"
                            "import sqlite3\n"
                            "from pathlib import Path\n"
                            "import pandas as pd\n\n\n"
                            "def save_results(df, base_path):\n"
                            "    \"\"\"분석 결과를 CSV, JSON, SQLite 세 가지 형식으로 저장한다.\"\"\"\n"
                            "    base = Path(base_path)\n"
                            "    base.mkdir(parents=True, exist_ok=True)\n\n"
                            "    # CSV 저장\n"
                            "    csv_path = base / 'data.csv'\n"
                            "    df.to_csv(csv_path, index=False, encoding='utf-8-sig')\n"
                            "    print(f'CSV 저장: {csv_path}')\n\n"
                            "    # JSON 저장 (레코드 형식)\n"
                            "    json_path = base / 'data.json'\n"
                            "    records = df.to_dict(orient='records')\n"
                            "    with open(json_path, 'w', encoding='utf-8') as f:\n"
                            "        json.dump(records, f, ensure_ascii=False, indent=2)\n"
                            "    print(f'JSON 저장: {json_path}')\n\n"
                            "    # SQLite 저장\n"
                            "    db_path = base / 'data.db'\n"
                            "    with sqlite3.connect(db_path) as conn:\n"
                            "        df.to_sql(\n"
                            "            'weather',\n"
                            "            conn,\n"
                            "            if_exists='replace',  # 기존 테이블 교체\n"
                            "            index=False,\n"
                            "        )\n"
                            "    print(f'SQLite 저장: {db_path}')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import sqlite3\n"
                            "import pandas as pd\n\n\n"
                            "def query_sqlite(db_path, sql, params=None):\n"
                            "    \"\"\"SQLite DB에 쿼리를 실행하고 DataFrame으로 반환한다.\"\"\"\n"
                            "    with sqlite3.connect(db_path) as conn:\n"
                            "        return pd.read_sql_query(sql, conn, params=params)\n\n\n"
                            "def append_to_sqlite(df, db_path, table_name):\n"
                            "    \"\"\"기존 SQLite 테이블에 데이터를 추가한다.\"\"\"\n"
                            "    with sqlite3.connect(db_path) as conn:\n"
                            "        df.to_sql(\n"
                            "            table_name,\n"
                            "            conn,\n"
                            "            if_exists='append',  # 기존 데이터 유지, 추가만\n"
                            "            index=False,\n"
                            "        )\n\n\n"
                            "# 사용 예\n"
                            "# df_result = query_sqlite(\n"
                            "#     'output/data.db',\n"
                            "#     'SELECT city, AVG(temp) as avg_temp FROM weather GROUP BY city',\n"
                            "# )\n"
                            "# print(df_result)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "SQLite는 별도 서버 설치 없이 파일 하나로 동작하는 "
                            "경량 관계형 데이터베이스입니다. "
                            "매일 수집한 데이터를 if_exists='append'로 누적하고, "
                            "SQL로 기간 조회나 집계를 하면 CSV보다 훨씬 편리합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 자동화 기초와 스케줄링 ───────────────────
            {
                "title": "자동화 기초: 스크립트 작성과 스케줄링",
                "content": [
                    "파이프라인을 매번 수동으로 실행하는 것은 비효율적입니다. "
                    "스크립트를 명령줄에서 실행 가능하게 만들고, "
                    "운영체제의 스케줄러로 정기 실행을 설정합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# run_pipeline.py — 명령줄에서 직접 실행 가능한 스크립트\n"
                            "import argparse\n"
                            "import logging\n"
                            "import sys\n"
                            "from datetime import datetime\n"
                            "from pathlib import Path\n\n\n"
                            "logging.basicConfig(\n"
                            "    level=logging.INFO,\n"
                            "    format='%(asctime)s [%(levelname)s] %(message)s',\n"
                            "    handlers=[\n"
                            "        logging.StreamHandler(sys.stdout),\n"
                            "        logging.FileHandler('pipeline.log', encoding='utf-8'),\n"
                            "    ],\n"
                            ")\n"
                            "logger = logging.getLogger(__name__)\n\n\n"
                            "def parse_args():\n"
                            "    \"\"\"명령줄 인수를 파싱한다.\"\"\"\n"
                            "    parser = argparse.ArgumentParser(description='날씨 데이터 파이프라인')\n"
                            "    parser.add_argument(\n"
                            "        '--city', default='Seoul', help='수집할 도시 (기본: Seoul)'\n"
                            "    )\n"
                            "    parser.add_argument(\n"
                            "        '--output', default='output', help='저장 경로 (기본: output/)'\n"
                            "    )\n"
                            "    return parser.parse_args()\n\n\n"
                            "def main():\n"
                            "    \"\"\"파이프라인 진입점.\"\"\"\n"
                            "    args = parse_args()\n"
                            "    today = datetime.now().strftime('%Y-%m-%d')\n"
                            "    output_dir = Path(args.output) / today\n\n"
                            "    logger.info(f'시작: 도시={args.city}, 출력={output_dir}')\n\n"
                            "    try:\n"
                            "        # 여기서 실제 파이프라인 함수 호출\n"
                            "        # raw = extract(args.city)\n"
                            "        # clean = transform(raw)\n"
                            "        # save_results(clean, output_dir)\n"
                            "        logger.info('완료')\n"
                            "    except Exception as e:\n"
                            "        logger.error(f'파이프라인 실패: {e}', exc_info=True)\n"
                            "        sys.exit(1)  # 오류 시 비정상 종료 코드 반환\n\n\n"
                            "if __name__ == '__main__':\n"
                            "    main()\n\n"
                            "# 실행 방법:\n"
                            "# python run_pipeline.py\n"
                            "# python run_pipeline.py --city Busan --output /data/output"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["스케줄러", "운영체제", "설정 방법", "예시"],
                        "rows": [
                            ["cron", "macOS / Linux", "crontab -e 편집", "0 8 * * * python /path/run.py"],
                            ["작업 스케줄러", "Windows", "GUI 또는 schtasks", "매일 오전 8시 실행"],
                            ["GitHub Actions", "클라우드", ".github/workflows/*.yml", "schedule: cron 문법 동일"],
                            ["APScheduler", "Python 라이브러리", "pip install apscheduler", "코드 내에서 스케줄 정의"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# cron 설정 예시 (macOS / Linux)\n"
                            "# crontab -e 로 편집기 열기\n\n"
                            "# 형식: 분 시 일 월 요일 명령\n"
                            "# 매일 오전 8시 실행\n"
                            "# 0 8 * * * /usr/bin/python3 /home/user/pipeline/run_pipeline.py\n\n"
                            "# 매 시간 실행\n"
                            "# 0 * * * * /usr/bin/python3 /home/user/pipeline/run_pipeline.py\n\n"
                            "# 매주 월요일 오전 9시 실행\n"
                            "# 0 9 * * 1 /usr/bin/python3 /home/user/pipeline/run_pipeline.py\n\n\n"
                            "# Python 내에서 스케줄링: schedule 라이브러리\n"
                            "# pip install schedule\n"
                            "# import schedule, time\n\n"
                            "# def job():\n"
                            "#     print('파이프라인 실행 중...')\n"
                            "#     main()\n\n"
                            "# schedule.every().day.at('08:00').do(job)\n\n"
                            "# while True:\n"
                            "#     schedule.run_pending()\n"
                            "#     time.sleep(60)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "스크립트에 `if __name__ == '__main__':` 블록을 반드시 추가하세요. "
                            "이 블록이 없으면 다른 모듈에서 import할 때 의도치 않게 실행됩니다. "
                            "또한 `sys.exit(1)`로 오류 시 비정상 종료 코드를 반환하면 "
                            "cron이나 CI/CD에서 실패를 감지할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 ─────────────────────────────────
            {
                "title": "실용 예제: 날씨 데이터 수집 → 분석 → 리포트 자동화",
                "content": [
                    "지금까지 배운 ETL, 검증, 저장, 자동화를 하나로 합쳐 "
                    "완전한 날씨 데이터 파이프라인을 구축합니다.",
                    {
                        "type": "heading",
                        "text": "전체 파이프라인 구현",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n"
                            "import sqlite3\n"
                            "import logging\n"
                            "from datetime import datetime\n"
                            "from pathlib import Path\n"
                            "import pandas as pd\n\n\n"
                            "logger = logging.getLogger(__name__)\n\n\n"
                            "# ── Extract ──────────────────────────────────────\n"
                            "def extract_weather_mock(cities):\n"
                            "    \"\"\"Mock 날씨 데이터를 반환한다 (실제 API 대체).\"\"\"\n"
                            "    import random\n"
                            "    records = []\n"
                            "    for city in cities:\n"
                            "        records.append({\n"
                            "            'city': city,\n"
                            "            'date': datetime.now().strftime('%Y-%m-%d'),\n"
                            "            'temp': round(random.uniform(-5, 35), 1),\n"
                            "            'humidity': random.randint(30, 95),\n"
                            "            'description': random.choice(['맑음', '흐림', '비', '눈']),\n"
                            "        })\n"
                            "    return records\n\n\n"
                            "# ── Transform ────────────────────────────────────\n"
                            "def transform_weather(records):\n"
                            "    \"\"\"날씨 원본 데이터를 정제하고 분석 컬럼을 추가한다.\"\"\"\n"
                            "    df = pd.DataFrame(records)\n\n"
                            "    clean = (\n"
                            "        df\n"
                            "        .dropna(subset=['city', 'date', 'temp'])\n"
                            "        .assign(\n"
                            "            date=lambda d: pd.to_datetime(d['date']),\n"
                            "            temp_category=lambda d: pd.cut(\n"
                            "                d['temp'],\n"
                            "                bins=[-float('inf'), 0, 10, 20, float('inf')],\n"
                            "                labels=['매우 추움', '추움', '서늘함', '따뜻함'],\n"
                            "            ),\n"
                            "        )\n"
                            "        .query('humidity.between(0, 100)')\n"
                            "        .reset_index(drop=True)\n"
                            "    )\n"
                            "    return clean"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n"
                            "import sqlite3\n"
                            "from pathlib import Path\n"
                            "import pandas as pd\n\n\n"
                            "# ── Load & Report ─────────────────────────────────\n"
                            "def load_and_report(df, output_dir):\n"
                            "    \"\"\"데이터를 저장하고 요약 리포트를 생성한다.\"\"\"\n"
                            "    out = Path(output_dir)\n"
                            "    out.mkdir(parents=True, exist_ok=True)\n\n"
                            "    # CSV 저장\n"
                            "    df.to_csv(out / 'weather.csv', index=False, encoding='utf-8-sig')\n\n"
                            "    # SQLite 누적 저장\n"
                            "    with sqlite3.connect(out / 'weather.db') as conn:\n"
                            "        df.to_sql('weather', conn, if_exists='append', index=False)\n\n"
                            "    # 요약 통계 리포트 생성\n"
                            "    report = {\n"
                            "        'generated_at': pd.Timestamp.now().isoformat(),\n"
                            "        'record_count': len(df),\n"
                            "        'cities': df['city'].tolist(),\n"
                            "        'temp_stats': {\n"
                            "            'mean': round(df['temp'].mean(), 1),\n"
                            "            'min': df['temp'].min(),\n"
                            "            'max': df['temp'].max(),\n"
                            "        },\n"
                            "        'humidity_mean': round(df['humidity'].mean(), 1),\n"
                            "        'description_counts': (\n"
                            "            df['description'].value_counts().to_dict()\n"
                            "        ),\n"
                            "    }\n\n"
                            "    report_path = out / 'report.json'\n"
                            "    with open(report_path, 'w', encoding='utf-8') as f:\n"
                            "        json.dump(report, f, ensure_ascii=False, indent=2)\n\n"
                            "    print(f'리포트 생성: {report_path}')\n"
                            "    print(f'  수집 도시: {report[\"cities\"]}')\n"
                            "    print(f'  평균 기온: {report[\"temp_stats\"][\"mean\"]}°C')\n"
                            "    return report\n\n\n"
                            "# ── 전체 파이프라인 실행 ───────────────────────────\n"
                            "if __name__ == '__main__':\n"
                            "    logging.basicConfig(level=logging.INFO)\n"
                            "    cities = ['서울', '부산', '인천', '대구', '광주']\n"
                            "    raw = extract_weather_mock(cities)\n"
                            "    clean = transform_weather(raw)\n"
                            "    load_and_report(clean, 'output/weather')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "파이프라인을 날짜별 디렉토리(output/2026-03-27/)에 저장하면 "
                            "과거 데이터를 보존하면서 최신 데이터를 관리할 수 있습니다. "
                            "SQLite의 if_exists='append'를 활용하면 "
                            "매일 실행할 때마다 데이터가 누적되어 장기 트렌드 분석이 가능합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "ETL 각 단계(Extract/Transform/Load)를 독립 함수로 분리하면 테스트와 디버깅이 쉬워집니다.",
            "데이터 검증은 추출 직후와 변환 후 두 번 실시하여 오류의 조기 발견을 보장하세요.",
            "pandas 메서드 체이닝과 pipe()를 활용하면 전처리 흐름을 읽기 쉽게 표현할 수 있습니다.",
            "SQLite의 if_exists='append'로 매일 데이터를 누적하면 장기 트렌드 분석이 가능합니다.",
            "스크립트에 argparse로 명령줄 인수를 추가하면 cron 등 외부 스케줄러와 쉽게 연동됩니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "ETL에서 'T'(Transform)에 해당하는 작업이 아닌 것은?",
                "choices": [
                    "A) 결측값을 중앙값으로 채우기",
                    "B) API에서 JSON 데이터 가져오기",
                    "C) 문자열 날짜를 datetime 타입으로 변환",
                    "D) 유효하지 않은 범위의 값 제거",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "pandas 메서드 체이닝에서 원본 DataFrame을 변경하지 않고 새 열을 추가하는 메서드는?",
                "choices": [
                    "A) df.add_column()",
                    "B) df.insert()",
                    "C) df.assign()",
                    "D) df.append()",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "SQLite에 데이터를 저장할 때 기존 테이블을 유지하면서 새 데이터를 추가하는 if_exists 옵션은?",
                "choices": [
                    "A) if_exists='replace'",
                    "B) if_exists='update'",
                    "C) if_exists='append'",
                    "D) if_exists='insert'",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "다음 DataFrame에서 메서드 체이닝을 사용하여 "
                    "1) 결측값이 있는 행 제거, "
                    "2) 'name' 컬럼 앞뒤 공백 제거, "
                    "3) 'score'가 0~100 범위인 행만 유지, "
                    "4) 인덱스 초기화를 순서대로 수행하는 코드를 작성하세요."
                ),
                "hint": (
                    "dropna(), assign(name=lambda df: df['name'].str.strip()), "
                    "query('score.between(0, 100)'), reset_index(drop=True)를 "
                    "괄호로 감싸 체이닝하세요."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "리스트 형태의 딕셔너리 데이터를 받아 "
                    "CSV와 JSON 두 형식으로 저장하는 함수 "
                    "`save_dual(records, base_path)`를 작성하세요. "
                    "CSV는 'data.csv', JSON은 'data.json'으로 저장해야 합니다."
                ),
                "hint": (
                    "pd.DataFrame(records).to_csv(path, index=False, encoding='utf-8-sig')와 "
                    "json.dump(records, f, ensure_ascii=False, indent=2)를 사용하세요. "
                    "Path(base_path).mkdir(parents=True, exist_ok=True)로 디렉토리를 먼저 생성하세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "챕터 6의 API 수집과 챕터 7의 스크래핑을 결합한 완전한 ETL 파이프라인을 구축하세요. "
                "수집 대상: books.toscrape.com에서 도서 정보 (제목, 가격, 평점) 2페이지 이상. "
                "변환 단계: "
                "1) 가격 문자열을 숫자로 변환, "
                "2) 평점을 숫자(1~5)로 변환, "
                "3) 가격 범위 검증 (0~1000 사이), "
                "4) 결측값 제거. "
                "저장 단계: CSV, JSON, SQLite 모두 저장. "
                "리포트: 총 도서 수, 평균 가격, 평점별 도서 수, "
                "가장 비싼 도서 TOP 5를 report.json에 포함. "
                "파이프라인은 run_books_pipeline.py로 명령줄에서 실행 가능해야 합니다."
            ),
            "hint": (
                "scrape → validate(raw) → transform → validate(clean) → save → report 순으로 진행합니다. "
                "가격 변환: float(price.replace('Â£', '').replace('£', '').strip()), "
                "df.nlargest(5, 'price')[['title', 'price']]로 TOP 5를 추출하세요."
            ),
        },
        "summary": [
            "ETL(Extract-Transform-Load)은 데이터 파이프라인의 핵심 패턴으로, 각 단계를 독립 함수로 분리해 설계한다.",
            "pandas 메서드 체이닝과 pipe()를 활용하면 전처리 흐름을 읽기 쉽고 불변적으로 작성할 수 있다.",
            "DataValidator 패턴으로 추출 후와 변환 후 두 번 검증하여 데이터 품질을 보장한다.",
            "CSV는 공유와 호환, JSON은 중첩 데이터, SQLite는 누적 저장과 SQL 쿼리가 필요할 때 선택한다.",
            "argparse로 명령줄 인수를 지원하고 if __name__ == '__main__': 블록을 작성하면 cron 자동화가 쉽다.",
            "logging 모듈로 파이프라인 실행 로그를 파일에 기록하면 문제 발생 시 추적이 가능하다.",
        ],
    }
