"""
Chapter 9: 미니 프로젝트 — 서울시 공공데이터 분석
requests, Pandas, Matplotlib/Seaborn을 종합하여 실전 데이터 분석 파이프라인을 완성한다.
"""


def get_chapter():
    return {
        "number": 9,
        "title": "미니 프로젝트 — 서울시 공공데이터 분석",
        "subtitle": "Vol.3에서 배운 모든 것을 하나의 파이프라인으로",
        "big_picture": (
            "Chapter 1~8에서 배운 NumPy, Pandas, Matplotlib, Seaborn, 통계 기초를 "
            "하나의 완결된 파이프라인에 녹여냅니다. "
            "서울시 공공데이터 API에서 실시간으로 데이터를 수집하고, "
            "Pandas로 정제·분석한 뒤, Seaborn으로 시각화하여 "
            "CSV 파일과 분석 리포트로 저장합니다. "
            "'수집 → 정제 → 분석 → 시각화 → 저장'의 전체 흐름을 직접 만들어 봅니다."
        ),
        "sections": [
            # ── 섹션 1: 프로젝트 소개 & 요구사항 분석 ──
            {
                "title": "9.1 프로젝트 소개 & 요구사항 분석",
                "content": [
                    (
                        "이번 프로젝트는 **서울시 공공데이터 분석 파이프라인**입니다. "
                        "서울시 열린데이터광장(data.seoul.go.kr)에서 "
                        "서울시 공공자전거(따릉이) 대여 현황 데이터를 수집하고, "
                        "시간대별·지역별 이용 패턴을 분석하여 인사이트를 도출합니다."
                    ),
                    {
                        "type": "analogy",
                        "text": (
                            "데이터 분석 파이프라인은 제조업의 생산라인과 같습니다. "
                            "원자재(원본 데이터)가 컨베이어 벨트를 따라 이동하며 "
                            "세척(정제), 가공(분석), 포장(시각화), 출하(저장) 단계를 거칩니다. "
                            "각 단계의 품질이 최종 결과물의 품질을 결정합니다."
                        ),
                    },
                    {
                        "type": "flow_diagram",
                        "title": "프로젝트 전체 구조 — 데이터 분석 파이프라인",
                        "steps": [
                            "1단계: 데이터 수집 — requests로 서울 열린데이터 API 호출",
                            "2단계: 데이터 정제 — Pandas로 결측값 처리 · 타입 변환",
                            "3단계: 탐색적 분석 — 통계 요약 · 시간대별 · 지역별 집계",
                            "4단계: 시각화 — Matplotlib/Seaborn으로 차트 생성",
                            "5단계: 결과 저장 — CSV 출력 · 텍스트 리포트 작성",
                        ],
                    },
                    "**프로젝트 요구사항:**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "서울시 공공 API에서 JSON 데이터를 수집하고 오류를 처리한다",
                            "Pandas DataFrame으로 변환하고 결측값·이상값을 정제한다",
                            "시간대별·구별 이용 현황을 집계하고 통계 요약을 출력한다",
                            "막대 그래프, 히트맵, 산점도 3종 차트를 PNG로 저장한다",
                            "분석 결과를 CSV와 텍스트 리포트(.txt)로 저장한다",
                            "모든 단계를 함수로 분리하여 파이프라인 형태로 구성한다",
                        ],
                    },
                    "**사용하는 라이브러리 & 역할:**",
                    {
                        "type": "table",
                        "headers": ["라이브러리", "역할", "주요 함수/객체", "챕터"],
                        "rows": [
                            ["requests", "HTTP API 호출", "get(), json()", "Ch9(신규)"],
                            ["pandas", "데이터 정제·분석", "DataFrame, groupby, agg", "Ch4-5"],
                            ["numpy", "수치 계산", "array, mean, std", "Ch1-2"],
                            ["matplotlib", "기본 시각화", "pyplot, savefig", "Ch6"],
                            ["seaborn", "고급 시각화", "heatmap, barplot", "Ch7"],
                            ["pathlib", "파일 경로 관리", "Path, mkdir", "Vol.2 Ch5"],
                            ["json", "JSON 파싱", "loads, dumps", "내장"],
                            ["datetime", "날짜·시간 처리", "now, strftime", "내장"],
                        ],
                    },
                ],
            },
            # ── 섹션 2: 데이터 수집 — API 호출 ──
            {
                "title": "9.2 데이터 수집 — 공공 API 호출",
                "content": [
                    (
                        "서울시 열린데이터광장은 REST API로 데이터를 제공합니다. "
                        "requests 라이브러리로 API를 호출하고, "
                        "응답 JSON을 Python 딕셔너리로 파싱합니다. "
                        "네트워크 오류와 API 오류를 모두 처리하는 견고한 코드를 작성합니다."
                    ),
                    {
                        "type": "tip",
                        "text": (
                            "서울시 열린데이터광장(data.seoul.go.kr)에서 무료 API 키를 발급받으세요. "
                            "회원가입 후 '인증키 신청'에서 즉시 발급됩니다. "
                            "API 키는 .env 파일이나 환경변수에 저장하고 코드에 직접 쓰지 마세요."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# collector.py — 데이터 수집 모듈\n"
                            "import os\n"
                            "import time\n"
                            "import requests\n"
                            "from typing import Optional\n"
                            "\n"
                            "\n"
                            "# API 설정 상수\n"
                            "BASE_URL = 'http://openapi.seoul.go.kr:8088'\n"
                            "SERVICE_NAME = 'bikeList'  # 따릉이 대여소 목록\n"
                            "DATA_TYPE = 'json'\n"
                            "PAGE_SIZE = 1000\n"
                            "\n"
                            "\n"
                            "def fetch_bike_data(\n"
                            "    api_key: str,\n"
                            "    start: int = 1,\n"
                            "    end: int = PAGE_SIZE,\n"
                            "    timeout: int = 10,\n"
                            ") -> Optional[dict]:\n"
                            '    """서울시 따릉이 대여소 데이터를 API로 수집한다.\n\n'
                            "    Args:\n"
                            "        api_key: 서울 열린데이터광장 인증키\n"
                            "        start: 시작 인덱스 (1부터)\n"
                            "        end: 끝 인덱스\n"
                            "        timeout: 요청 제한 시간(초)\n\n"
                            "    Returns:\n"
                            "        성공 시 API 응답 딕셔너리, 실패 시 None\n"
                            '    """\n'
                            "    url = f'{BASE_URL}/{api_key}/{DATA_TYPE}/{SERVICE_NAME}/{start}/{end}'\n"
                            "\n"
                            "    try:\n"
                            "        response = requests.get(url, timeout=timeout)\n"
                            "        response.raise_for_status()  # 4xx/5xx → HTTPError\n"
                            "        return response.json()\n"
                            "\n"
                            "    except requests.exceptions.ConnectionError:\n"
                            "        print('[오류] 네트워크 연결 실패. 인터넷 연결을 확인하세요.')\n"
                            "    except requests.exceptions.Timeout:\n"
                            "        print(f'[오류] 요청 시간 초과 ({timeout}초). 나중에 다시 시도하세요.')\n"
                            "    except requests.exceptions.HTTPError as e:\n"
                            "        print(f'[오류] HTTP 오류: {e}')\n"
                            "    except requests.exceptions.JSONDecodeError:\n"
                            "        print('[오류] 응답 데이터를 JSON으로 파싱할 수 없습니다.')\n"
                            "\n"
                            "    return None\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def collect_all_data(api_key: str) -> list[dict]:\n"
                            '    """전체 데이터를 페이지별로 나눠 수집한다 (페이지네이션)."""\n'
                            "    all_rows: list[dict] = []\n"
                            "    start = 1\n"
                            "\n"
                            "    while True:\n"
                            "        end = start + PAGE_SIZE - 1\n"
                            "        print(f'  수집 중: {start} ~ {end}번째 데이터...')\n"
                            "\n"
                            "        raw = fetch_bike_data(api_key, start, end)\n"
                            "        if raw is None:\n"
                            "            print('[중단] 데이터 수집 실패.')\n"
                            "            break\n"
                            "\n"
                            "        # API 응답 구조: {'bikeList': {'RESULT': {...}, 'row': [...]}}\n"
                            "        service_data = raw.get(SERVICE_NAME, {})\n"
                            "        result = service_data.get('RESULT', {})\n"
                            "\n"
                            "        if result.get('CODE') != 'INFO-000':\n"
                            "            print(f'[API 오류] {result.get(\"MESSAGE\", \"알 수 없는 오류\")}')\n"
                            "            break\n"
                            "\n"
                            "        rows = service_data.get('row', [])\n"
                            "        if not rows:\n"
                            "            break  # 더 이상 데이터 없음\n"
                            "\n"
                            "        all_rows.extend(rows)\n"
                            "\n"
                            "        if len(rows) < PAGE_SIZE:\n"
                            "            break  # 마지막 페이지\n"
                            "\n"
                            "        start = end + 1\n"
                            "        time.sleep(0.3)  # API 서버 부하 방지\n"
                            "\n"
                            "    print(f'수집 완료: 총 {len(all_rows)}개 레코드')\n"
                            "    return all_rows\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "API 키는 반드시 환경변수로 관리하세요. "
                            "os.environ.get('SEOUL_API_KEY') 또는 "
                            "python-dotenv 라이브러리로 .env 파일에서 불러옵니다. "
                            "코드에 API 키를 직접 작성하면 GitHub 업로드 시 보안 사고가 발생합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 데이터 정제 — Pandas ──
            {
                "title": "9.3 데이터 정제 — Pandas로 깨끗하게",
                "content": [
                    (
                        "수집된 원본 데이터에는 결측값, 잘못된 타입, 불필요한 컬럼 등이 포함됩니다. "
                        "Pandas로 DataFrame을 만들고, "
                        "분석에 적합한 형태로 정제하는 과정을 단계별로 살펴봅니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# cleaner.py — 데이터 정제 모듈\n"
                            "import pandas as pd\n"
                            "import numpy as np\n"
                            "\n"
                            "\n"
                            "# 사용할 컬럼 정의 (원본 → 한글 이름)\n"
                            "COLUMN_MAP = {\n"
                            "    'RENT_ID': '대여소_ID',\n"
                            "    'RENT_NM': '대여소명',\n"
                            "    'STTN_ADDR': '주소',\n"
                            "    'LEND_CNT': '대여_건수',\n"
                            "    'RTRN_CNT': '반납_건수',\n"
                            "    'PARKNG_CNT': '거치대_수',\n"
                            "    'HOLD_CNT': '보유_자전거',\n"
                            "    'LEND_POSBL_STTS': '대여_가능_여부',\n"
                            "}\n"
                            "\n"
                            "\n"
                            "def raw_to_dataframe(rows: list[dict]) -> pd.DataFrame:\n"
                            '    """수집된 원본 레코드를 DataFrame으로 변환한다."""\n'
                            "    if not rows:\n"
                            "        raise ValueError('변환할 데이터가 없습니다.')\n"
                            "\n"
                            "    df = pd.DataFrame(rows)\n"
                            "    print(f'원본 shape: {df.shape}')\n"
                            "    return df\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:\n"
                            '    """DataFrame을 정제하여 분석용으로 변환한다."""\n'
                            "    # 1. 필요한 컬럼만 선택 & 이름 변경\n"
                            "    available = [c for c in COLUMN_MAP if c in df.columns]\n"
                            "    df = df[available].rename(columns=COLUMN_MAP)\n"
                            "\n"
                            "    # 2. 수치형 컬럼 타입 변환 (문자열 → 정수)\n"
                            "    numeric_cols = ['대여_건수', '반납_건수', '거치대_수', '보유_자전거']\n"
                            "    for col in numeric_cols:\n"
                            "        if col in df.columns:\n"
                            "            df[col] = pd.to_numeric(df[col], errors='coerce')\n"
                            "\n"
                            "    # 3. 결측값 처리\n"
                            "    missing_before = df.isnull().sum().sum()\n"
                            "    df[numeric_cols] = df[numeric_cols].fillna(0).astype(int)\n"
                            "    df['대여소명'] = df['대여소명'].fillna('알 수 없음')\n"
                            "    df['주소'] = df['주소'].fillna('')\n"
                            "    print(f'결측값 처리: {missing_before}개 → 0개')\n"
                            "\n"
                            "    # 4. 주소에서 구(區) 추출 — '서울특별시 강남구 ...' → '강남구'\n"
                            "    df['구'] = (\n"
                            "        df['주소']\n"
                            "        .str.extract(r'(\\S+구)', expand=False)\n"
                            "        .fillna('기타')\n"
                            "    )\n"
                            "\n"
                            "    # 5. 이상값 제거 — 대여 건수 음수는 불가\n"
                            "    outlier_mask = (df['대여_건수'] < 0) | (df['반납_건수'] < 0)\n"
                            "    if outlier_mask.sum() > 0:\n"
                            "        print(f'이상값 제거: {outlier_mask.sum()}행')\n"
                            "        df = df[~outlier_mask].copy()\n"
                            "\n"
                            "    # 6. 중복 대여소 제거\n"
                            "    before = len(df)\n"
                            "    df = df.drop_duplicates(subset=['대여소_ID']).reset_index(drop=True)\n"
                            "    print(f'중복 제거: {before - len(df)}행 삭제')\n"
                            "\n"
                            "    print(f'정제 완료 shape: {df.shape}')\n"
                            "    return df\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "정제 전에 항상 df.info()와 df.describe()로 데이터를 먼저 탐색하세요. "
                            "컬럼별 타입과 결측값 수를 파악해야 어떻게 정제할지 결정할 수 있습니다. "
                            "정제 코드를 작성하기 전 탐색에 충분한 시간을 투자하는 것이 좋습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 탐색적 분석 ──
            {
                "title": "9.4 탐색적 분석 — 인사이트 발굴",
                "content": [
                    (
                        "정제된 데이터에서 의미 있는 패턴을 찾아냅니다. "
                        "구별 대여 현황, 대여소 규모별 이용률, "
                        "거치대 수 대비 대여 건수 관계를 분석합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# analyzer.py — 분석 모듈\n"
                            "import pandas as pd\n"
                            "import numpy as np\n"
                            "\n"
                            "\n"
                            "def summarize(df: pd.DataFrame) -> dict:\n"
                            '    """데이터 전체 통계 요약을 반환한다."""\n'
                            "    return {\n"
                            "        '총_대여소_수': len(df),\n"
                            "        '총_대여_건수': int(df['대여_건수'].sum()),\n"
                            "        '총_반납_건수': int(df['반납_건수'].sum()),\n"
                            "        '평균_대여_건수': round(df['대여_건수'].mean(), 1),\n"
                            "        '중앙값_대여_건수': float(df['대여_건수'].median()),\n"
                            "        '표준편차_대여_건수': round(df['대여_건수'].std(), 1),\n"
                            "        '대여_건수_상위_1pct_기준': int(df['대여_건수'].quantile(0.99)),\n"
                            "        '활성_구_수': df['구'].nunique(),\n"
                            "    }\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def analyze_by_district(df: pd.DataFrame) -> pd.DataFrame:\n"
                            '    """구별 대여 현황을 집계한다."""\n'
                            "    district = (\n"
                            "        df.groupby('구')\n"
                            "        .agg(\n"
                            "            대여소_수=('대여소_ID', 'count'),\n"
                            "            총_대여=('대여_건수', 'sum'),\n"
                            "            총_반납=('반납_건수', 'sum'),\n"
                            "            평균_대여=('대여_건수', 'mean'),\n"
                            "            총_거치대=('거치대_수', 'sum'),\n"
                            "        )\n"
                            "        .round(1)\n"
                            "        .sort_values('총_대여', ascending=False)\n"
                            "        .reset_index()\n"
                            "    )\n"
                            "\n"
                            "    # 이용률 = 총 대여 / 총 거치대 (0 나눗셈 방지)\n"
                            "    district['이용률'] = np.where(\n"
                            "        district['총_거치대'] > 0,\n"
                            "        (district['총_대여'] / district['총_거치대']).round(2),\n"
                            "        0.0,\n"
                            "    )\n"
                            "    return district\n"
                            "\n"
                            "\n"
                            "def top_stations(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:\n"
                            '    """대여 건수 상위 N개 대여소를 반환한다."""\n'
                            "    return (\n"
                            "        df[['대여소명', '구', '대여_건수', '반납_건수', '거치대_수']]\n"
                            "        .nlargest(n, '대여_건수')\n"
                            "        .reset_index(drop=True)\n"
                            "    )\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def analyze_capacity_vs_usage(df: pd.DataFrame) -> pd.DataFrame:\n"
                            '    """거치대 규모별 이용 현황을 분석한다."""\n'
                            "    # 거치대 수 기준으로 대여소를 3등분\n"
                            "    df = df.copy()\n"
                            "    df['규모'] = pd.qcut(\n"
                            "        df['거치대_수'],\n"
                            "        q=3,\n"
                            "        labels=['소형(하위 33%)', '중형(중간 33%)', '대형(상위 33%)'],\n"
                            "        duplicates='drop',\n"
                            "    )\n"
                            "\n"
                            "    result = (\n"
                            "        df.groupby('규모', observed=True)\n"
                            "        .agg(\n"
                            "            대여소_수=('대여소_ID', 'count'),\n"
                            "            평균_거치대=('거치대_수', 'mean'),\n"
                            "            평균_대여=('대여_건수', 'mean'),\n"
                            "        )\n"
                            "        .round(1)\n"
                            "        .reset_index()\n"
                            "    )\n"
                            "    return result\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "분석 결과를 함수로 분리하면 두 가지 이점이 있습니다. "
                            "첫째, 각 분석을 독립적으로 테스트할 수 있습니다. "
                            "둘째, 데이터가 바뀌어도 함수를 재사용할 수 있습니다. "
                            "분석 로직은 파이프라인에서 재사용 가능한 부품이 되어야 합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 시각화 ──
            {
                "title": "9.5 시각화 — Matplotlib & Seaborn으로 차트 만들기",
                "content": [
                    (
                        "분석 결과를 3종류의 차트로 표현합니다. "
                        "구별 대여 현황 막대그래프, 구별 이용률 히트맵, "
                        "거치대 수 대비 대여 건수 산점도를 PNG 파일로 저장합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# visualizer.py — 시각화 모듈\n"
                            "import matplotlib.pyplot as plt\n"
                            "import matplotlib.ticker as mticker\n"
                            "import seaborn as sns\n"
                            "import pandas as pd\n"
                            "from pathlib import Path\n"
                            "\n"
                            "\n"
                            "# 한글 폰트 설정 (macOS: AppleGothic, Windows: Malgun Gothic)\n"
                            "import platform\n"
                            "\n"
                            "if platform.system() == 'Darwin':      # macOS\n"
                            "    plt.rcParams['font.family'] = 'AppleGothic'\n"
                            "elif platform.system() == 'Windows':\n"
                            "    plt.rcParams['font.family'] = 'Malgun Gothic'\n"
                            "else:                                   # Linux (Colab 등)\n"
                            "    plt.rcParams['font.family'] = 'NanumGothic'\n"
                            "\n"
                            "plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지\n"
                            "\n"
                            "# 스타일 설정\n"
                            "sns.set_theme(style='whitegrid', palette='muted')\n"
                            "OUTPUT_DIR = Path('output')\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def plot_district_bar(\n"
                            "    district_df: pd.DataFrame,\n"
                            "    top_n: int = 15,\n"
                            ") -> Path:\n"
                            '    """구별 총 대여 건수 가로 막대 차트를 생성하고 저장한다."""\n'
                            "    OUTPUT_DIR.mkdir(exist_ok=True)\n"
                            "    df = district_df.nlargest(top_n, '총_대여')\n"
                            "\n"
                            "    fig, ax = plt.subplots(figsize=(10, 6))\n"
                            "    bars = ax.barh(\n"
                            "        df['구'],\n"
                            "        df['총_대여'],\n"
                            "        color=sns.color_palette('Blues_r', top_n),\n"
                            "    )\n"
                            "\n"
                            "    # 막대 끝에 수치 표시\n"
                            "    for bar, val in zip(bars, df['총_대여']):\n"
                            "        ax.text(\n"
                            "            bar.get_width() + max(df['총_대여']) * 0.01,\n"
                            "            bar.get_y() + bar.get_height() / 2,\n"
                            "            f'{val:,}',\n"
                            "            va='center', fontsize=9,\n"
                            "        )\n"
                            "\n"
                            "    ax.set_title(f'서울시 자치구별 따릉이 총 대여 건수 (상위 {top_n}개 구)',\n"
                            "                 fontsize=13, fontweight='bold', pad=12)\n"
                            "    ax.set_xlabel('대여 건수')\n"
                            "    ax.xaxis.set_major_formatter(mticker.FuncFormatter(\n"
                            "        lambda x, _: f'{x:,.0f}'\n"
                            "    ))\n"
                            "    ax.invert_yaxis()\n"
                            "    plt.tight_layout()\n"
                            "\n"
                            "    save_path = OUTPUT_DIR / 'chart_district_bar.png'\n"
                            "    fig.savefig(save_path, dpi=150, bbox_inches='tight')\n"
                            "    plt.close(fig)\n"
                            "    print(f'저장: {save_path}')\n"
                            "    return save_path\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def plot_usage_heatmap(district_df: pd.DataFrame) -> Path:\n"
                            '    """구별 이용률을 히트맵으로 시각화한다."""\n'
                            "    OUTPUT_DIR.mkdir(exist_ok=True)\n"
                            "\n"
                            "    # 히트맵 입력: 1행 × N열 매트릭스\n"
                            "    df_sorted = district_df.sort_values('이용률', ascending=False)\n"
                            "    heat_data = df_sorted[['구', '이용률']].set_index('구').T\n"
                            "\n"
                            "    fig, ax = plt.subplots(figsize=(14, 3))\n"
                            "    sns.heatmap(\n"
                            "        heat_data,\n"
                            "        annot=True, fmt='.2f',\n"
                            "        cmap='YlOrRd',\n"
                            "        linewidths=0.5,\n"
                            "        ax=ax,\n"
                            "        cbar_kws={'label': '이용률 (대여/거치대)'},\n"
                            "    )\n"
                            "    ax.set_title('서울시 자치구별 따릉이 이용률 히트맵',\n"
                            "                 fontsize=13, fontweight='bold', pad=12)\n"
                            "    ax.set_ylabel('')\n"
                            "    plt.xticks(rotation=45, ha='right', fontsize=8)\n"
                            "    plt.tight_layout()\n"
                            "\n"
                            "    save_path = OUTPUT_DIR / 'chart_usage_heatmap.png'\n"
                            "    fig.savefig(save_path, dpi=150, bbox_inches='tight')\n"
                            "    plt.close(fig)\n"
                            "    print(f'저장: {save_path}')\n"
                            "    return save_path\n"
                            "\n"
                            "\n"
                            "def plot_capacity_scatter(df: pd.DataFrame) -> Path:\n"
                            '    """거치대 수 대비 대여 건수 산점도를 생성한다."""\n'
                            "    OUTPUT_DIR.mkdir(exist_ok=True)\n"
                            "\n"
                            "    fig, ax = plt.subplots(figsize=(9, 6))\n"
                            "    sns.scatterplot(\n"
                            "        data=df,\n"
                            "        x='거치대_수', y='대여_건수',\n"
                            "        hue='구', alpha=0.6,\n"
                            "        ax=ax,\n"
                            "        legend=False,\n"
                            "    )\n"
                            "\n"
                            "    # 추세선 (회귀선)\n"
                            "    sns.regplot(\n"
                            "        data=df, x='거치대_수', y='대여_건수',\n"
                            "        scatter=False, color='red', line_kws={'linewidth': 1.5},\n"
                            "        ax=ax,\n"
                            "    )\n"
                            "\n"
                            "    ax.set_title('거치대 수 vs 대여 건수 (산점도 + 추세선)',\n"
                            "                 fontsize=13, fontweight='bold', pad=12)\n"
                            "    ax.set_xlabel('거치대 수 (개)')\n"
                            "    ax.set_ylabel('대여 건수')\n"
                            "    plt.tight_layout()\n"
                            "\n"
                            "    save_path = OUTPUT_DIR / 'chart_capacity_scatter.png'\n"
                            "    fig.savefig(save_path, dpi=150, bbox_inches='tight')\n"
                            "    plt.close(fig)\n"
                            "    print(f'저장: {save_path}')\n"
                            "    return save_path\n"
                        ),
                    },
                ],
            },
            # ── 섹션 6: 결과 저장 & 파이프라인 조립 ──
            {
                "title": "9.6 결과 저장 & 파이프라인 완성",
                "content": [
                    (
                        "분석 결과를 CSV 파일로 저장하고, "
                        "핵심 인사이트를 담은 텍스트 리포트를 생성합니다. "
                        "마지막으로 모든 단계를 하나의 메인 함수로 연결하여 "
                        "완성된 파이프라인을 실행합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# reporter.py — 결과 저장 모듈\n"
                            "import pandas as pd\n"
                            "from pathlib import Path\n"
                            "from datetime import datetime\n"
                            "\n"
                            "\n"
                            "OUTPUT_DIR = Path('output')\n"
                            "\n"
                            "\n"
                            "def save_csv(df: pd.DataFrame, filename: str) -> Path:\n"
                            '    """DataFrame을 CSV로 저장한다 (UTF-8 BOM — Excel 호환)."""\n'
                            "    OUTPUT_DIR.mkdir(exist_ok=True)\n"
                            "    path = OUTPUT_DIR / filename\n"
                            "    df.to_csv(path, index=False, encoding='utf-8-sig')\n"
                            "    print(f'CSV 저장: {path} ({len(df)}행)')\n"
                            "    return path\n"
                            "\n"
                            "\n"
                            "def write_report(\n"
                            "    summary: dict,\n"
                            "    district_df: pd.DataFrame,\n"
                            "    top_stations_df: pd.DataFrame,\n"
                            ") -> Path:\n"
                            '    """텍스트 분석 리포트를 작성하고 저장한다."""\n'
                            "    OUTPUT_DIR.mkdir(exist_ok=True)\n"
                            "    path = OUTPUT_DIR / 'analysis_report.txt'\n"
                            "\n"
                            "    lines = [\n"
                            "        '=' * 60,\n"
                            "        '  서울시 따릉이 대여 현황 분석 리포트',\n"
                            "        f'  생성 일시: {datetime.now().strftime(\"%Y-%m-%d %H:%M\")}',\n"
                            "        '=' * 60,\n"
                            "        '',\n"
                            "        '[1] 전체 요약',\n"
                            "        '-' * 40,\n"
                            "    ]\n"
                            "\n"
                            "    for key, value in summary.items():\n"
                            "        lines.append(f'  {key}: {value:,}' if isinstance(value, int)\n"
                            "                     else f'  {key}: {value}')\n"
                            "\n"
                            "    lines += [\n"
                            "        '',\n"
                            "        '[2] 대여 건수 상위 5개 구',\n"
                            "        '-' * 40,\n"
                            "    ]\n"
                            "    top5 = district_df.head(5)\n"
                            "    for _, row in top5.iterrows():\n"
                            "        lines.append(\n"
                            "            f'  {row[\"구\"]:6s}  대여: {int(row[\"총_대여\"]):>8,}건  '\n"
                            "            f'이용률: {row[\"이용률\"]:.2f}'\n"
                            "        )\n"
                            "\n"
                            "    lines += [\n"
                            "        '',\n"
                            "        '[3] 대여 건수 상위 10개 대여소',\n"
                            "        '-' * 40,\n"
                            "    ]\n"
                            "    for i, row in top_stations_df.iterrows():\n"
                            "        lines.append(\n"
                            "            f'  {i+1:2d}. {row[\"대여소명\"][:20]:20s}  '\n"
                            "            f'({row[\"구\"]})  {int(row[\"대여_건수\"]):,}건'\n"
                            "        )\n"
                            "\n"
                            "    lines += ['', '=' * 60]\n"
                            "\n"
                            "    path.write_text('\\n'.join(lines), encoding='utf-8')\n"
                            "    print(f'리포트 저장: {path}')\n"
                            "    return path\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# main.py — 파이프라인 진입점\n"
                            "import os\n"
                            "from collector import collect_all_data\n"
                            "from cleaner import raw_to_dataframe, clean_dataframe\n"
                            "from analyzer import summarize, analyze_by_district, top_stations\n"
                            "from visualizer import plot_district_bar, plot_usage_heatmap, plot_capacity_scatter\n"
                            "from reporter import save_csv, write_report\n"
                            "\n"
                            "\n"
                            "def run_pipeline() -> None:\n"
                            '    """서울시 따릉이 데이터 분석 파이프라인을 실행한다."""\n'
                            "    print('\\n[1/5] 데이터 수집 시작...')\n"
                            "    api_key = os.environ.get('SEOUL_API_KEY', '')\n"
                            "    if not api_key:\n"
                            "        raise EnvironmentError(\n"
                            "            'SEOUL_API_KEY 환경변수가 설정되지 않았습니다.\\n'\n"
                            "            '터미널에서: export SEOUL_API_KEY=발급받은키'\n"
                            "        )\n"
                            "\n"
                            "    rows = collect_all_data(api_key)\n"
                            "    print('\\n[2/5] 데이터 정제 중...')\n"
                            "    df_raw = raw_to_dataframe(rows)\n"
                            "    df = clean_dataframe(df_raw)\n"
                            "    print('\\n[3/5] 데이터 분석 중...')\n"
                            "    summary = summarize(df)\n"
                            "    district_df = analyze_by_district(df)\n"
                            "    top10 = top_stations(df, n=10)\n"
                            "    for k, v in summary.items():\n"
                            "        print(f'  {k}: {v}')\n"
                            "    print('\\n[4/5] 시각화 중...')\n"
                            "    plot_district_bar(district_df)\n"
                            "    plot_usage_heatmap(district_df)\n"
                            "    plot_capacity_scatter(df)\n"
                            "    print('\\n[5/5] 결과 저장 중...')\n"
                            "    save_csv(df, 'bike_stations_clean.csv')\n"
                            "    save_csv(district_df, 'bike_by_district.csv')\n"
                            "    write_report(summary, district_df, top10)\n"
                            "    print('\\n파이프라인 완료! output/ 폴더를 확인하세요.')\n"
                            "\n"
                            "\n"
                            "if __name__ == '__main__':\n"
                            "    run_pipeline()\n"
                        ),
                    },
                    "**프로젝트 파일 구조:**",
                    {
                        "type": "table",
                        "headers": ["파일", "역할", "주요 함수"],
                        "rows": [
                            ["collector.py", "API 데이터 수집", "fetch_bike_data, collect_all_data"],
                            ["cleaner.py", "데이터 정제", "raw_to_dataframe, clean_dataframe"],
                            ["analyzer.py", "통계 분석", "summarize, analyze_by_district, top_stations"],
                            ["visualizer.py", "차트 생성", "plot_district_bar, plot_usage_heatmap, plot_capacity_scatter"],
                            ["reporter.py", "결과 저장", "save_csv, write_report"],
                            ["main.py", "파이프라인 조립", "run_pipeline"],
                            ["output/", "생성 파일 저장 폴더", "CSV 3종 + PNG 3종 + 리포트"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "실제 API가 없을 때는 테스트용 샘플 데이터를 만들어 파이프라인을 테스트하세요. "
                            "collector.py에 load_sample_data() 함수를 추가하고, "
                            "main.py에서 API 호출 대신 샘플 데이터를 사용하면 "
                            "오프라인에서도 전체 파이프라인을 검증할 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "파이프라인 각 단계를 독립 함수로 만들면 문제가 생겼을 때 어느 단계인지 바로 알 수 있습니다.",
            "데이터 정제는 분석보다 더 많은 시간이 걸립니다. 현업에서는 전체 작업 시간의 60~80%가 정제에 사용됩니다.",
            "차트 저장 후 plt.close(fig)를 반드시 호출하세요. 닫지 않으면 메모리 누수 및 차트 요소 혼합 문제가 생깁니다.",
            "API 호출에는 항상 timeout을 설정하세요. 미설정 시 서버 무응답으로 프로그램이 무한 대기 상태에 빠집니다.",
            "CSV 저장 시 encoding='utf-8-sig'를 사용해야 Windows Excel에서 한글이 깨지지 않습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "title": "오프라인 샘플 데이터 생성기",
                "description": (
                    "API 없이도 파이프라인을 실행할 수 있도록 "
                    "collector.py에 generate_sample_data(n=200) 함수를 작성하세요. "
                    "서울 25개 구, 임의의 대여소명, 0~500 범위의 대여 건수를 가진 "
                    "DataFrame을 반환합니다."
                ),
                "hint": "numpy.random.randint()와 random.choice()를 사용하면 됩니다. 구 목록은 리스트 상수로 정의하세요.",
            },
            {
                "number": 2,
                "title": "분석 함수 단위 테스트",
                "description": (
                    "analyzer.py의 summarize()와 analyze_by_district() 함수에 대한 "
                    "pytest 단위 테스트를 test_analyzer.py 파일에 작성하세요. "
                    "최소 5개 행으로 구성된 테스트용 DataFrame을 fixture로 만들어 사용합니다."
                ),
                "hint": "@pytest.fixture로 sample_df를 만들고, summarize(sample_df)['총_대여소_수'] == 5임을 검증하세요.",
            },
            {
                "number": 3,
                "title": "시간대별 대여 분포 분석",
                "description": (
                    "서울 열린데이터광장의 '공공자전거 시간대별 대여정보' API를 추가로 수집하여 "
                    "시간대별(0시~23시) 대여 건수 분포를 분석하고, 라인 차트로 시각화하세요."
                ),
                "hint": "0~23시 x축, 대여 건수 y축으로 sns.lineplot을 사용하세요.",
            },
            {
                "number": 4,
                "title": "리포트를 HTML로 변환",
                "description": (
                    "reporter.py에 write_html_report() 함수를 추가하세요. "
                    "기존 텍스트 리포트 내용을 HTML 테이블로 변환하고, "
                    "PNG 차트 이미지를 <img> 태그로 삽입합니다."
                ),
                "hint": "district_df.to_html(classes='table', index=False)를 사용하면 DataFrame을 HTML 테이블로 변환할 수 있습니다.",
            },
            {
                "number": 5,
                "title": "이상값 탐지 함수",
                "description": (
                    "cleaner.py에 detect_outliers(df, column, method='iqr') 함수를 추가하세요. "
                    "IQR 방법(Q1 - 1.5*IQR 미만 또는 Q3 + 1.5*IQR 초과)으로 "
                    "이상값 행의 인덱스와 해당 값을 반환합니다."
                ),
                "hint": "Q1 = df[column].quantile(0.25), Q3 = df[column].quantile(0.75), IQR = Q3 - Q1",
            },
        ],
        "challenge": {
            "question": (
                "파이프라인을 **자동 스케줄러**로 확장하세요. "
                "schedule 라이브러리를 사용하여 매일 오전 9시에 run_pipeline()이 자동 실행되도록 하고, "
                "실행 결과(성공/실패, 수집 레코드 수, 소요 시간)를 날짜별 로그 파일에 기록하세요. "
                "실패 시 smtplib으로 오류 내용을 이메일로 발송하는 알림 기능도 추가하세요."
            ),
            "hint": (
                "schedule.every().day.at('09:00').do(run_pipeline)으로 스케줄 등록, "
                "logging.FileHandler로 날짜별 로그 저장, "
                "smtplib.SMTP_SSL로 이메일 발송 — API 키와 비밀번호는 환경변수로 관리하세요."
            ),
        },
        "summary": [
            "공공 API 호출은 requests.get()으로 수행하며, 연결 오류·타임아웃·HTTP 오류를 모두 처리해야 합니다.",
            "데이터 정제(컬럼 선택, 타입 변환, 결측값 처리, 이상값 제거, 중복 제거)는 분석 품질의 핵심입니다.",
            "groupby().agg()로 구별·규모별 집계를 효율적으로 수행하고, 파생 변수(이용률)를 추가합니다.",
            "한글 폰트 설정과 plt.rcParams로 환경별 폰트를 설정하고, 각 차트를 PNG로 저장합니다.",
            "파이프라인은 수집→정제→분석→시각화→저장 순서로 함수를 연결하며, main.py가 전체를 조립합니다.",
        ],
    }
