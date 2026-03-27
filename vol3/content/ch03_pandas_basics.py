"""챕터 3: Pandas 기초 — Series와 DataFrame으로 데이터 다루기."""


def get_chapter():
    """챕터 3 콘텐츠를 반환한다."""
    return {
        "number": 3,
        "title": "Pandas 기초",
        "subtitle": "Series와 DataFrame으로 데이터 다루기",
        "big_picture": (
            "데이터 분석의 세계에서 Pandas는 가장 강력한 도구입니다. "
            "엑셀처럼 행과 열로 구성된 표 형식의 데이터를 Python에서 "
            "자유자재로 다룰 수 있게 해줍니다. "
            "이 장에서는 Pandas의 핵심 자료구조인 Series와 DataFrame을 이해하고, "
            "데이터를 불러오고 탐색하고 선택하는 기본기를 익힙니다. "
            "이 기초가 탄탄해야 이후 심화 분석도 수월해집니다."
        ),
        "sections": [
            # ── 섹션 1: Series와 DataFrame 이해 ──────────────────
            {
                "title": "Series와 DataFrame 이해",
                "content": [
                    "Pandas는 두 가지 핵심 자료구조를 중심으로 동작합니다. "
                    "1차원인 **Series**와 2차원인 **DataFrame**입니다. "
                    "이 둘의 관계와 특징을 먼저 이해하면 나머지가 훨씬 쉬워집니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "Series는 엑셀의 '열 한 개'와 같습니다. "
                            "인덱스(행 번호)와 값으로 이루어진 1차원 배열이죠. "
                            "DataFrame은 그 Series 여러 개를 나란히 붙인 '전체 스프레드시트'입니다. "
                            "즉, DataFrame은 Series의 컬렉션이라고 볼 수 있습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["자료구조", "차원", "구성 요소", "비유"],
                        "rows": [
                            ["Series", "1차원", "인덱스 + 값", "엑셀의 열 하나"],
                            ["DataFrame", "2차원", "인덱스 + 컬럼 + 값", "엑셀 전체 시트"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "# ── Series 기초 ──────────────────────────────────\n"
                            "# 리스트에서 Series 생성\n"
                            "scores = pd.Series([85, 92, 78, 96, 88])\n"
                            "print(scores)\n"
                            "# 0    85\n"
                            "# 1    92\n"
                            "# 2    78\n"
                            "# 3    96\n"
                            "# 4    88\n"
                            "# dtype: int64\n\n"
                            "# 인덱스를 직접 지정\n"
                            "named_scores = pd.Series(\n"
                            "    [85, 92, 78, 96, 88],\n"
                            "    index=['김철수', '이영희', '박민수', '정수진', '최동욱'],\n"
                            ")\n"
                            "print(named_scores['이영희'])  # 92\n\n"
                            "# 딕셔너리에서 Series 생성\n"
                            "fruit_prices = pd.Series({'사과': 2000, '바나나': 1500, '포도': 3500})\n"
                            "print(fruit_prices)\n"
                            "# 사과     2000\n"
                            "# 바나나    1500\n"
                            "# 포도     3500\n"
                            "# dtype: int64"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── DataFrame 기초 ───────────────────────────────\n"
                            "# DataFrame의 각 컬럼은 Series\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김철수', '이영희', '박민수'],\n"
                            "    '국어': [85, 92, 78],\n"
                            "    '수학': [90, 88, 95],\n"
                            "    '영어': [80, 95, 70],\n"
                            "})\n"
                            "print(df)\n"
                            "#     이름  국어  수학  영어\n"
                            "# 0  김철수  85   90   80\n"
                            "# 1  이영희  92   88   95\n"
                            "# 2  박민수  78   95   70\n\n"
                            "# 컬럼 하나를 꺼내면 Series\n"
                            "print(type(df['국어']))  # <class 'pandas.core.series.Series'>\n"
                            "print(df['국어'])\n"
                            "# 0    85\n"
                            "# 1    92\n"
                            "# 2    78\n"
                            "# Name: 국어, dtype: int64"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Pandas는 관습적으로 `import pandas as pd`로 가져옵니다. "
                            "이 별칭은 전 세계 데이터 과학자가 공통으로 사용하는 표준입니다. "
                            "마찬가지로 NumPy는 `import numpy as np`가 표준입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: DataFrame 생성 ─────────────────────────────
            {
                "title": "DataFrame 생성: 딕셔너리, CSV, Excel에서 불러오기",
                "content": [
                    "실무에서 데이터는 대부분 파일로 주어집니다. "
                    "CSV, Excel 파일을 불러오는 방법과 "
                    "직접 DataFrame을 만드는 방법을 모두 익혀야 합니다.",
                    {
                        "type": "table",
                        "headers": ["생성 방법", "함수/방법", "주요 사용 사례"],
                        "rows": [
                            ["딕셔너리", "pd.DataFrame(dict)", "코드 내 데이터 정의"],
                            ["CSV 파일", "pd.read_csv(파일경로)", "가장 일반적인 데이터 형식"],
                            ["Excel 파일", "pd.read_excel(파일경로)", "업무용 스프레드시트"],
                            ["리스트의 리스트", "pd.DataFrame(리스트, columns=)", "행 단위 데이터"],
                            ["NumPy 배열", "pd.DataFrame(배열, columns=)", "수치 계산 결과"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "# ── 방법 1: 딕셔너리에서 생성 ────────────────────\n"
                            "students = pd.DataFrame({\n"
                            "    '학번': ['2024001', '2024002', '2024003', '2024004'],\n"
                            "    '이름': ['김민준', '이서연', '박지호', '최수아'],\n"
                            "    '학년': [1, 2, 1, 3],\n"
                            "    '평점': [3.8, 4.2, 3.5, 4.0],\n"
                            "})\n"
                            "print(students)\n\n"
                            "# ── 방법 2: 리스트의 리스트에서 생성 ─────────────\n"
                            "data = [\n"
                            "    ['2024001', '김민준', 1, 3.8],\n"
                            "    ['2024002', '이서연', 2, 4.2],\n"
                            "    ['2024003', '박지호', 1, 3.5],\n"
                            "]\n"
                            "df = pd.DataFrame(data, columns=['학번', '이름', '학년', '평점'])\n"
                            "print(df)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── CSV 파일 불러오기 ────────────────────────────\n"
                            "# 기본 사용법\n"
                            "df = pd.read_csv('students.csv')\n\n"
                            "# 인코딩 지정 (한글 파일에서 필수)\n"
                            "df = pd.read_csv('students.csv', encoding='utf-8')\n"
                            "df = pd.read_csv('students.csv', encoding='cp949')  # Windows 한글\n\n"
                            "# 특정 컬럼을 인덱스로 지정\n"
                            "df = pd.read_csv('students.csv', index_col='학번')\n\n"
                            "# 첫 N행만 불러오기 (대용량 파일 미리보기)\n"
                            "df = pd.read_csv('students.csv', nrows=100)\n\n"
                            "# 구분자가 탭인 TSV 파일\n"
                            "df = pd.read_csv('data.tsv', sep='\\t')\n\n"
                            "# ── Excel 파일 불러오기 ──────────────────────────\n"
                            "df = pd.read_excel('students.xlsx')\n\n"
                            "# 특정 시트 지정\n"
                            "df = pd.read_excel('report.xlsx', sheet_name='1월')\n\n"
                            "# 여러 시트를 한 번에 (딕셔너리로 반환)\n"
                            "sheets = pd.read_excel('report.xlsx', sheet_name=None)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "CSV 파일을 읽을 때 한글이 깨진다면 "
                            "`encoding='utf-8-sig'`를 먼저 시도해보세요. "
                            "BOM(바이트 순서 표시)이 포함된 파일은 'utf-8-sig'로 읽어야 합니다. "
                            "그래도 안 된다면 'cp949'를 시도하세요."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── DataFrame을 파일로 저장 ──────────────────────\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연'],\n"
                            "    '점수': [85, 92],\n"
                            "})\n\n"
                            "# CSV로 저장 (인덱스 제외가 일반적)\n"
                            "df.to_csv('output.csv', index=False, encoding='utf-8-sig')\n\n"
                            "# Excel로 저장\n"
                            "df.to_excel('output.xlsx', index=False, sheet_name='결과')"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 데이터 탐색 ────────────────────────────────
            {
                "title": "데이터 탐색: head, tail, info, describe, shape",
                "content": [
                    "새로운 데이터를 받았을 때 가장 먼저 해야 할 일은 "
                    "'이 데이터가 어떻게 생겼는가?'를 파악하는 것입니다. "
                    "Pandas는 이를 위한 편리한 메서드를 제공합니다.",
                    {
                        "type": "table",
                        "headers": ["메서드/속성", "반환값", "용도"],
                        "rows": [
                            ["df.head(n)", "처음 n행 (기본 5)", "데이터 미리보기"],
                            ["df.tail(n)", "마지막 n행 (기본 5)", "데이터 끝부분 확인"],
                            ["df.info()", "컬럼 정보 출력", "타입, 결측치 파악"],
                            ["df.describe()", "통계 요약 DataFrame", "수치형 통계 요약"],
                            ["df.shape", "(행수, 열수) 튜플", "크기 확인"],
                            ["df.columns", "컬럼명 배열", "컬럼 목록"],
                            ["df.index", "인덱스 객체", "인덱스 확인"],
                            ["df.dtypes", "컬럼별 타입", "데이터 타입 확인"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "# 예제 데이터 생성\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호', '최수아', '정하늘',\n"
                            "             '윤도현', '임지수', '강준혁'],\n"
                            "    '학년': [1, 2, 1, 3, 2, 1, 3, 2],\n"
                            "    '국어': [85, 92, 78, 96, 88, 72, 91, 83],\n"
                            "    '수학': [90, 88, 95, 82, 79, 98, 76, 87],\n"
                            "    '영어': [80, 95, 70, 88, 92, 75, 85, 91],\n"
                            "})\n\n"
                            "# 처음 3행 확인\n"
                            "print(df.head(3))\n\n"
                            "# 마지막 2행 확인\n"
                            "print(df.tail(2))\n\n"
                            "# 데이터 크기\n"
                            "print(df.shape)    # (8, 5)\n"
                            "print(f'행: {df.shape[0]}, 열: {df.shape[1]}')\n\n"
                            "# 컬럼 목록\n"
                            "print(df.columns.tolist())\n"
                            "# ['이름', '학년', '국어', '수학', '영어']"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── df.info() — 가장 중요한 탐색 메서드 ─────────\n"
                            "df.info()\n"
                            "# <class 'pandas.core.frame.DataFrame'>\n"
                            "# RangeIndex: 8 entries, 0 to 7\n"
                            "# Data columns (total 5 columns):\n"
                            "#  #   Column  Non-Null Count  Dtype\n"
                            "# ---  ------  --------------  -----\n"
                            "#  0   이름      8 non-null      object\n"
                            "#  1   학년      8 non-null      int64\n"
                            "#  2   국어      8 non-null      int64\n"
                            "#  3   수학      8 non-null      int64\n"
                            "#  4   영어      8 non-null      int64\n"
                            "# dtypes: int64(4), object(1)\n"
                            "# memory usage: 448.0+ bytes\n\n"
                            "# ── df.describe() — 수치형 통계 요약 ────────────\n"
                            "print(df.describe())\n"
                            "#        학년        국어        수학        영어\n"
                            "# count  8.000000  8.000000  8.000000  8.000000\n"
                            "# mean   1.875000  85.625000  86.875000  84.500000\n"
                            "# std    0.834523   7.780...   7.308...   8.689...\n"
                            "# min    1.000000  72.000000  76.000000  70.000000\n"
                            "# 25%    1.000000  81.250000  80.500000  78.750000\n"
                            "# 50%    2.000000  85.500000  87.500000  85.000000\n"
                            "# 75%    2.750000  91.250000  92.250000  91.750000\n"
                            "# max    3.000000  96.000000  98.000000  95.000000"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "`df.info()`는 데이터를 처음 받았을 때 반드시 실행해야 할 명령입니다. "
                            "컬럼별 데이터 타입(Dtype)과 결측치(Null) 개수를 한눈에 파악할 수 있습니다. "
                            "특히 숫자처럼 보이는 컬럼이 'object' 타입인 경우 전처리가 필요하다는 신호입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 컬럼/행 선택 ──────────────────────────────
            {
                "title": "컬럼/행 선택: df['col'], df.loc[], df.iloc[]",
                "content": [
                    "DataFrame에서 원하는 데이터를 꺼내는 방법은 여러 가지입니다. "
                    "컬럼 선택, 레이블 기반 선택(loc), 위치 기반 선택(iloc)을 "
                    "상황에 맞게 사용하는 것이 핵심입니다.",
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "데이터 선택"},
                            {"label": "컬럼 선택: df['col']", "color": "#3182F6"},
                            {"label": "레이블 기반: df.loc[]", "color": "#3182F6"},
                            {"label": "위치 기반: df.iloc[]", "color": "#3182F6"},
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호', '최수아', '정하늘'],\n"
                            "    '학년': [1, 2, 1, 3, 2],\n"
                            "    '국어': [85, 92, 78, 96, 88],\n"
                            "    '수학': [90, 88, 95, 82, 79],\n"
                            "}, index=['s001', 's002', 's003', 's004', 's005'])\n\n"
                            "# ── 컬럼 선택 ─────────────────────────────────\n"
                            "# 단일 컬럼 → Series 반환\n"
                            "print(df['국어'])\n\n"
                            "# 여러 컬럼 → DataFrame 반환 (리스트로 전달)\n"
                            "print(df[['이름', '국어', '수학']])\n\n"
                            "# 점 표기법 (컬럼명에 공백/특수문자가 없을 때만 사용)\n"
                            "print(df.국어)  # df['국어']와 동일"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── df.loc[] — 레이블(인덱스/컬럼명) 기반 선택 ──\n"
                            "# loc[행 레이블, 컬럼 레이블]\n\n"
                            "# 단일 행 선택\n"
                            "print(df.loc['s001'])          # s001 행 전체 (Series)\n\n"
                            "# 단일 값 선택\n"
                            "print(df.loc['s001', '국어'])  # 85\n\n"
                            "# 여러 행 선택\n"
                            "print(df.loc[['s001', 's003']])\n\n"
                            "# 슬라이싱 (끝 포함!)\n"
                            "print(df.loc['s001':'s003'])   # s001, s002, s003\n\n"
                            "# 행 슬라이싱 + 특정 컬럼\n"
                            "print(df.loc['s001':'s003', ['이름', '국어']])\n\n"
                            "# 모든 행, 특정 컬럼들\n"
                            "print(df.loc[:, ['국어', '수학']])"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── df.iloc[] — 정수 위치(0부터 시작) 기반 선택 ─\n"
                            "# iloc[행 번호, 열 번호]\n\n"
                            "# 첫 번째 행\n"
                            "print(df.iloc[0])         # 0번 행 (s001)\n\n"
                            "# 특정 위치의 값\n"
                            "print(df.iloc[0, 2])      # 0행 2열 → 85 (국어)\n\n"
                            "# 슬라이싱 (끝 미포함! Python 표준)\n"
                            "print(df.iloc[0:3])       # 0, 1, 2행 (s001, s002, s003)\n\n"
                            "# 마지막 2행\n"
                            "print(df.iloc[-2:])       # s004, s005\n\n"
                            "# 행 슬라이싱 + 열 슬라이싱\n"
                            "print(df.iloc[0:3, 1:3])  # 0-2행, 1-2열"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["구분", "loc[]", "iloc[]"],
                        "rows": [
                            ["기준", "레이블(이름)", "정수 위치(0부터)"],
                            ["슬라이싱 끝", "포함", "미포함 (Python 방식)"],
                            ["사용 예", "df.loc['a':'c']", "df.iloc[0:3]"],
                            ["장점", "인덱스가 문자열일 때 직관적", "항상 번호로 접근 가능"],
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            "loc과 iloc의 슬라이싱 차이를 꼭 기억하세요. "
                            "loc는 끝 레이블을 포함하지만, iloc는 끝 인덱스를 포함하지 않습니다. "
                            "이 차이를 모르면 예상치 못한 결과가 나올 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 조건 필터링과 정렬 ──────────────────────────
            {
                "title": "조건 필터링과 정렬: boolean indexing, sort_values",
                "content": [
                    "데이터에서 조건에 맞는 행만 뽑아내는 **필터링**과 "
                    "원하는 기준으로 행을 나열하는 **정렬**은 "
                    "데이터 분석에서 가장 자주 사용하는 작업입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호', '최수아', '정하늘',\n"
                            "             '윤도현', '임지수', '강준혁'],\n"
                            "    '학년': [1, 2, 1, 3, 2, 1, 3, 2],\n"
                            "    '국어': [85, 92, 78, 96, 88, 72, 91, 83],\n"
                            "    '수학': [90, 88, 95, 82, 79, 98, 76, 87],\n"
                            "    '영어': [80, 95, 70, 88, 92, 75, 85, 91],\n"
                            "})\n\n"
                            "# ── boolean indexing ────────────────────────────\n"
                            "# 조건식은 True/False Series를 반환\n"
                            "mask = df['국어'] >= 90\n"
                            "print(mask)\n"
                            "# 0    False\n"
                            "# 1     True\n"
                            "# 2    False ...\n\n"
                            "# 마스크를 인덱서로 사용\n"
                            "high_korean = df[df['국어'] >= 90]\n"
                            "print(high_korean)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 여러 조건 결합 ──────────────────────────────\n"
                            "# 주의: Python의 and/or 대신 &/| 를 사용\n"
                            "# 각 조건에 반드시 괄호를 씌워야 합니다\n\n"
                            "# 국어 90 이상 AND 수학 90 이상\n"
                            "both_high = df[(df['국어'] >= 90) & (df['수학'] >= 90)]\n"
                            "print(both_high[['이름', '국어', '수학']])\n\n"
                            "# 1학년 OR 3학년\n"
                            "yr1_or_3 = df[(df['학년'] == 1) | (df['학년'] == 3)]\n"
                            "print(yr1_or_3[['이름', '학년']])\n\n"
                            "# isin으로 목록 필터링 (OR의 깔끔한 대안)\n"
                            "yr1_or_3 = df[df['학년'].isin([1, 3])]\n\n"
                            "# NOT 조건 (~)\n"
                            "not_yr2 = df[~(df['학년'] == 2)]\n"
                            "print(not_yr2[['이름', '학년']])"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 정렬: sort_values ───────────────────────────\n"
                            "# 국어 점수 오름차순\n"
                            "df_sorted = df.sort_values('국어')\n"
                            "print(df_sorted[['이름', '국어']].head())\n\n"
                            "# 국어 점수 내림차순\n"
                            "df_sorted = df.sort_values('국어', ascending=False)\n"
                            "print(df_sorted[['이름', '국어']].head())\n\n"
                            "# 여러 컬럼 기준 정렬 (학년 오름차순, 같은 학년이면 국어 내림차순)\n"
                            "df_sorted = df.sort_values(['학년', '국어'], ascending=[True, False])\n"
                            "print(df_sorted[['이름', '학년', '국어']])\n\n"
                            "# ── 인덱스 기준 정렬: sort_index ─────────────────\n"
                            "df_by_index = df.sort_index()\n"
                            "df_by_index = df.sort_index(ascending=False)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "필터링과 정렬 모두 원본 DataFrame을 수정하지 않고 새 DataFrame을 반환합니다. "
                            "결과를 보존하려면 변수에 저장하세요: `df_sorted = df.sort_values('국어')`. "
                            "원본을 직접 바꾸려면 `inplace=True`를 추가하지만, "
                            "불변성 원칙상 새 변수에 저장하는 방식을 권장합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 — 학생 성적 데이터 분석 ────────────
            {
                "title": "실용 예제: 학생 성적 데이터 분석",
                "content": [
                    "지금까지 배운 내용을 종합하여 "
                    "학생 성적 데이터를 실전처럼 분석해봅니다. "
                    "데이터 생성 → 탐색 → 선택 → 필터링 → 정렬까지 "
                    "전체 흐름을 경험해보세요.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "# ── 1단계: 데이터 준비 ─────────────────────────\n"
                            "성적표 = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호', '최수아', '정하늘',\n"
                            "             '윤도현', '임지수', '강준혁', '한소희', '오성민'],\n"
                            "    '학년': [1, 2, 1, 3, 2, 1, 3, 2, 1, 3],\n"
                            "    '반': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],\n"
                            "    '국어': [85, 92, 78, 96, 88, 72, 91, 83, 79, 95],\n"
                            "    '수학': [90, 88, 95, 82, 79, 98, 76, 87, 84, 91],\n"
                            "    '영어': [80, 95, 70, 88, 92, 75, 85, 91, 77, 89],\n"
                            "})\n\n"
                            "# ── 2단계: 기본 탐색 ────────────────────────────\n"
                            "print('=== 데이터 기본 정보 ===')\n"
                            "print(f'학생 수: {len(성적표)}명')\n"
                            "print(f'컬럼: {성적표.columns.tolist()}')\n"
                            "print(성적표.describe())"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 3단계: 과목별 평균 점수 계산 ─────────────────\n"
                            "과목_평균 = 성적표[['국어', '수학', '영어']].mean()\n"
                            "print('\\n=== 과목별 평균 ===')\n"
                            "for 과목, 평균 in 과목_평균.items():\n"
                            "    print(f'{과목}: {평균:.1f}점')\n\n"
                            "# ── 4단계: 총점과 평균 컬럼 추가 ─────────────────\n"
                            "성적표 = pd.DataFrame(성적표)  # 새 DataFrame으로 작업\n"
                            "성적표['총점'] = 성적표['국어'] + 성적표['수학'] + 성적표['영어']\n"
                            "성적표['평균'] = 성적표['총점'] / 3\n\n"
                            "# ── 5단계: 우수 학생 필터링 (세 과목 모두 85점 이상) ─\n"
                            "우수학생 = 성적표[\n"
                            "    (성적표['국어'] >= 85)\n"
                            "    & (성적표['수학'] >= 85)\n"
                            "    & (성적표['영어'] >= 85)\n"
                            "]\n"
                            "print('\\n=== 우수 학생 (전 과목 85점 이상) ===')\n"
                            "print(우수학생[['이름', '학년', '국어', '수학', '영어', '평균']])"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 6단계: 성적 순위 산출 ─────────────────────────\n"
                            "성적표_정렬 = 성적표.sort_values('총점', ascending=False)\n"
                            "성적표_정렬 = pd.DataFrame(성적표_정렬)  # 새 객체\n"
                            "성적표_정렬['순위'] = range(1, len(성적표_정렬) + 1)\n\n"
                            "print('\\n=== 성적 순위표 ===')\n"
                            "print(성적표_정렬[['순위', '이름', '총점', '평균']].to_string(index=False))\n\n"
                            "# ── 7단계: 학년별 평균 (groupby 미리보기) ────────\n"
                            "학년별_평균 = 성적표.groupby('학년')[['국어', '수학', '영어']].mean()\n"
                            "print('\\n=== 학년별 과목 평균 ===')\n"
                            "print(학년별_평균.round(1))"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "실무에서는 데이터에 한글 컬럼명을 사용하는 경우가 많습니다. "
                            "Pandas는 UTF-8 문자열을 컬럼명으로 완벽하게 지원합니다. "
                            "다만 `df.학년` 같은 점 표기법은 한글 컬럼에서도 동작하지만, "
                            "가독성을 위해 `df['학년']` 방식을 일관되게 사용하는 것을 권장합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "새 데이터를 받으면 head(), info(), describe()를 순서대로 실행하여 전체 구조를 파악하세요.",
            "loc는 레이블 기반(끝 포함), iloc는 위치 기반(끝 미포함)임을 항상 기억하세요.",
            "boolean indexing에서 여러 조건을 결합할 때 and/or 대신 &/|를 사용하고, 각 조건을 괄호로 감싸세요.",
            "sort_values()는 원본을 수정하지 않습니다. 결과를 저장할 변수를 명시적으로 지정하세요.",
            "한글 CSV 파일은 인코딩 문제가 자주 발생합니다. utf-8-sig → cp949 순으로 시도해보세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "다음 중 DataFrame의 특정 컬럼을 선택했을 때 반환되는 타입은?"
                ),
                "choices": [
                    "A) DataFrame",
                    "B) Series",
                    "C) list",
                    "D) numpy.ndarray",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "df.loc['a':'c']와 df.iloc[0:3]의 차이점으로 옳은 것은?"
                ),
                "choices": [
                    "A) loc는 끝을 포함하고, iloc는 끝을 포함하지 않는다",
                    "B) iloc는 끝을 포함하고, loc는 끝을 포함하지 않는다",
                    "C) 둘 다 끝을 포함한다",
                    "D) 둘 다 끝을 포함하지 않는다",
                ],
                "answer": "A",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "df[df['점수'] >= 90]에서 사용된 기법의 이름은?"
                ),
                "choices": [
                    "A) 위치 인덱싱 (positional indexing)",
                    "B) 레이블 인덱싱 (label indexing)",
                    "C) 불리언 인덱싱 (boolean indexing)",
                    "D) 팬시 인덱싱 (fancy indexing)",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "다음 조건을 모두 만족하는 코드를 작성하세요. "
                    "1) 이름, 나이, 급여 컬럼이 있는 DataFrame 생성 (5명 이상). "
                    "2) 급여가 4000만원 이상인 직원만 필터링. "
                    "3) 결과를 급여 내림차순으로 정렬하여 출력."
                ),
                "hint": "df[df['급여'] >= 4000].sort_values('급여', ascending=False)",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "CSV 파일을 읽어서 shape, info(), describe()를 출력하고, "
                    "특정 숫자 컬럼에서 상위 10% 이상인 행만 필터링하는 코드를 작성하세요. "
                    "(파일이 없다면 pd.DataFrame으로 직접 데이터를 만드세요)"
                ),
                "hint": "상위 10%: df[df['컬럼'] >= df['컬럼'].quantile(0.9)]",
            },
        ],
        "challenge": {
            "question": (
                "학생 성적 데이터를 분석하는 종합 보고서를 만드세요. "
                "① 전체 학생 수, 과목 수, 기본 통계 출력. "
                "② 각 학생의 총점, 평균, 등급(A/B/C/D/F) 컬럼 추가. "
                "   (90+: A, 80-89: B, 70-79: C, 60-69: D, 60미만: F) "
                "③ 등급별 학생 수 집계. "
                "④ 최고점 학생과 최저점 학생의 정보 출력. "
                "모든 연산은 새 DataFrame을 생성하고 원본을 수정하지 마세요."
            ),
            "hint": (
                "등급 부여: pd.cut() 또는 np.where()를 활용하거나 "
                "apply(lambda x: 'A' if x >= 90 else ...)를 사용하세요. "
                "등급별 집계: df['등급'].value_counts(). "
                "최고점: df.loc[df['총점'].idxmax()]"
            ),
        },
        "summary": [
            "Pandas의 핵심 자료구조는 1차원 Series와 2차원 DataFrame이며, DataFrame은 Series의 컬렉션이다.",
            "DataFrame은 딕셔너리, CSV, Excel 등 다양한 방법으로 생성하고 불러올 수 있다.",
            "head(), tail(), info(), describe(), shape로 데이터의 기본 구조와 통계를 빠르게 파악한다.",
            "컬럼 선택은 df['col'], 다중 선택은 df[['col1', 'col2']] 형태로 한다.",
            "loc[]는 레이블 기반(끝 포함), iloc[]는 위치 기반(끝 미포함) 인덱싱이다.",
            "boolean indexing으로 조건에 맞는 행을 필터링하며, 여러 조건은 &/|로 결합한다.",
        ],
    }
