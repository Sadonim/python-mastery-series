"""챕터 4: Pandas 심화 — 데이터 정제, 집계, 결합, 피벗."""


def get_chapter():
    """챕터 4 콘텐츠를 반환한다."""
    return {
        "number": 4,
        "title": "Pandas 심화",
        "subtitle": "데이터 정제, 집계, 결합, 피벗",
        "big_picture": (
            "현실의 데이터는 결코 깨끗하지 않습니다. "
            "결측치가 있고, 타입이 뒤섞여 있고, 여러 파일에 흩어져 있습니다. "
            "이 장에서는 지저분한 데이터를 분석 가능한 형태로 정제하고, "
            "groupby로 집계하고, merge/concat으로 데이터를 결합하며, "
            "pivot_table로 요약하는 심화 기술을 익힙니다. "
            "apply/map으로 함수를 데이터 전체에 적용하는 방법도 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: 결측치 처리 ────────────────────────────────
            {
                "title": "결측치 처리: isna, fillna, dropna",
                "content": [
                    "결측치(Missing Value)는 데이터 분석에서 피할 수 없는 현실입니다. "
                    "설문 미응답, 센서 오류, 데이터 입력 누락 등 다양한 이유로 발생합니다. "
                    "Pandas에서 결측치는 `NaN(Not a Number)` 또는 `None`으로 표현됩니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "결측치는 빈 칸이 있는 설문지와 같습니다. "
                            "빈 칸을 어떻게 처리할지는 상황에 따라 다릅니다. "
                            "제외(dropna)할 수도 있고, 특정 값으로 채울(fillna) 수도 있습니다. "
                            "어떤 방법을 선택하느냐에 따라 분석 결과가 달라지므로 신중해야 합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["메서드", "동작", "주요 파라미터"],
                        "rows": [
                            ["df.isna()", "결측치 위치를 True/False로 반환", "—"],
                            ["df.notna()", "결측치가 아닌 위치를 True로 반환", "—"],
                            ["df.isna().sum()", "컬럼별 결측치 개수", "—"],
                            ["df.dropna()", "결측치가 있는 행/열 제거", "axis, how, subset"],
                            ["df.fillna(값)", "결측치를 지정값으로 채우기", "value, method"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "# 결측치가 포함된 예제 데이터\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호', None, '정하늘'],\n"
                            "    '나이': [25, np.nan, 30, 28, np.nan],\n"
                            "    '급여': [3500, 4200, np.nan, 3800, 4000],\n"
                            "    '부서': ['개발', '마케팅', '개발', np.nan, '인사'],\n"
                            "})\n\n"
                            "# ── 결측치 확인 ─────────────────────────────────\n"
                            "print(df.isna())\n"
                            "#     이름     나이    급여     부서\n"
                            "# 0  False  False  False  False\n"
                            "# 1  False   True  False  False\n"
                            "# 2  False  False   True  False\n"
                            "# 3   True  False  False   True\n"
                            "# 4  False   True  False  False\n\n"
                            "# 컬럼별 결측치 개수\n"
                            "print(df.isna().sum())\n"
                            "# 이름    1\n"
                            "# 나이    2\n"
                            "# 급여    1\n"
                            "# 부서    1\n\n"
                            "# 결측치 비율\n"
                            "print(df.isna().mean() * 100)  # 퍼센트로 표시"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── dropna — 결측치가 있는 행 제거 ──────────────\n"
                            "# 하나라도 결측치가 있는 행 제거 (기본)\n"
                            "df_clean = df.dropna()\n"
                            "print(df_clean)\n\n"
                            "# 모든 값이 결측치인 행만 제거\n"
                            "df_any = df.dropna(how='all')\n\n"
                            "# 특정 컬럼에서만 결측치 확인 후 제거\n"
                            "df_subset = df.dropna(subset=['이름', '급여'])\n\n"
                            "# ── fillna — 결측치를 값으로 채우기 ─────────────\n"
                            "# 고정값으로 채우기\n"
                            "df_filled = df.fillna({'나이': df['나이'].mean(), '부서': '미정'})\n\n"
                            "# 앞 행의 값으로 채우기 (forward fill)\n"
                            "df_ffill = df.fillna(method='ffill')\n\n"
                            "# 뒤 행의 값으로 채우기 (backward fill)\n"
                            "df_bfill = df.fillna(method='bfill')\n\n"
                            "# 수치형은 평균, 범주형은 최빈값으로 채우기 (실무 패턴)\n"
                            "df_smart = df.copy()\n"
                            "df_smart['나이'] = df_smart['나이'].fillna(df_smart['나이'].mean())\n"
                            "df_smart['부서'] = df_smart['부서'].fillna(df_smart['부서'].mode()[0])"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "dropna()는 데이터를 잃는 대신 완전한 데이터를 확보합니다. "
                            "fillna()는 데이터를 유지하지만 채운 값이 분석에 영향을 줄 수 있습니다. "
                            "어떤 방법을 선택하든 이유를 문서화해두세요."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 데이터 타입 변환 ────────────────────────────
            {
                "title": "데이터 타입 변환: astype, pd.to_datetime, pd.to_numeric",
                "content": [
                    "데이터를 불러오면 의도와 다른 타입으로 읽히는 경우가 많습니다. "
                    "숫자가 문자열로, 날짜가 일반 텍스트로 저장될 수 있습니다. "
                    "올바른 타입으로 변환해야 계산과 분석이 정확하게 동작합니다.",
                    {
                        "type": "table",
                        "headers": ["함수/메서드", "용도", "예시"],
                        "rows": [
                            ["df['col'].astype(타입)", "명시적 타입 변환", "astype('int64')"],
                            ["pd.to_numeric(series)", "문자열 → 숫자 (오류 처리 포함)", "errors='coerce'"],
                            ["pd.to_datetime(series)", "문자열 → 날짜/시간", "format='%Y-%m-%d'"],
                            ["df['col'].astype('category')", "범주형으로 변환 (메모리 절약)", "—"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "# 타입 문제가 있는 예제 데이터\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호'],\n"
                            "    '나이': ['25', '30', '28'],        # 숫자가 문자열로\n"
                            "    '급여': ['3500만원', '4200만원', '3800만원'],  # 단위 포함\n"
                            "    '입사일': ['2020-03-15', '2019-07-22', '2021-01-10'],\n"
                            "    '평가': ['A', 'B', 'A'],\n"
                            "})\n\n"
                            "print(df.dtypes)\n"
                            "# 이름     object\n"
                            "# 나이     object  ← 숫자여야 할 컬럼이 문자열\n"
                            "# 급여     object\n"
                            "# 입사일   object  ← 날짜여야 할 컬럼이 문자열\n"
                            "# 평가     object"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── astype으로 타입 변환 ─────────────────────────\n"
                            "df_fixed = pd.DataFrame(df)  # 새 객체 생성\n\n"
                            "# 문자열 나이 → 정수\n"
                            "df_fixed['나이'] = df_fixed['나이'].astype('int64')\n\n"
                            "# 범주형으로 변환 (반복값이 많을 때 메모리 절약)\n"
                            "df_fixed['평가'] = df_fixed['평가'].astype('category')\n\n"
                            "# ── 문자열에서 숫자 추출 후 변환 ─────────────────\n"
                            "# '3500만원' → 3500 추출\n"
                            "df_fixed['급여'] = (\n"
                            "    df_fixed['급여']\n"
                            "    .str.replace('만원', '', regex=False)\n"
                            "    .astype('int64')\n"
                            ")\n\n"
                            "# ── pd.to_numeric — 오류 처리 포함 변환 ──────────\n"
                            "messy_nums = pd.Series(['1', '2', 'three', '4', None])\n"
                            "# errors='coerce': 변환 실패 시 NaN으로\n"
                            "print(pd.to_numeric(messy_nums, errors='coerce'))\n"
                            "# 0    1.0\n"
                            "# 1    2.0\n"
                            "# 2    NaN  ← 'three' 변환 실패\n"
                            "# 3    4.0\n"
                            "# 4    NaN"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── pd.to_datetime — 날짜/시간 변환 ─────────────\n"
                            "df_fixed['입사일'] = pd.to_datetime(df_fixed['입사일'])\n"
                            "print(df_fixed['입사일'].dtype)  # datetime64[ns]\n\n"
                            "# 날짜 컬럼에서 다양한 정보 추출 가능\n"
                            "df_fixed['입사_년도'] = df_fixed['입사일'].dt.year\n"
                            "df_fixed['입사_월'] = df_fixed['입사일'].dt.month\n"
                            "df_fixed['요일'] = df_fixed['입사일'].dt.day_name()\n\n"
                            "# 재직 기간 계산\n"
                            "오늘 = pd.Timestamp('today')\n"
                            "df_fixed['재직일수'] = (오늘 - df_fixed['입사일']).dt.days\n"
                            "print(df_fixed[['이름', '입사일', '재직일수']])"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "날짜 형식이 다양할 때는 `format` 파라미터를 명시하면 변환이 빠르고 정확합니다. "
                            "예: `pd.to_datetime(df['날짜'], format='%Y/%m/%d')`. "
                            "형식을 지정하지 않으면 Pandas가 자동 추론하지만 속도가 느릴 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: groupby 집계 ───────────────────────────────
            {
                "title": "groupby 집계 연산",
                "content": [
                    "groupby는 SQL의 GROUP BY와 동일한 개념입니다. "
                    "'분류 기준에 따라 데이터를 묶고, 각 그룹에 함수를 적용'하는 "
                    "강력한 분석 도구입니다.",
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "전체 DataFrame"},
                            {"label": "groupby('기준 컬럼'): 분할", "color": "#3182F6"},
                            {"label": "각 그룹에 함수 적용", "color": "#3182F6"},
                            {"label": "결과 결합 → 새 DataFrame"},
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "매출 = pd.DataFrame({\n"
                            "    '날짜': ['2024-01', '2024-01', '2024-02', '2024-02',\n"
                            "             '2024-03', '2024-03', '2024-03'],\n"
                            "    '지역': ['서울', '부산', '서울', '부산', '서울', '부산', '서울'],\n"
                            "    '제품': ['A', 'B', 'A', 'A', 'B', 'B', 'A'],\n"
                            "    '매출액': [1200, 800, 1500, 950, 1100, 700, 1300],\n"
                            "    '수량': [12, 8, 15, 9, 11, 7, 13],\n"
                            "})\n\n"
                            "# ── 기본 groupby ─────────────────────────────────\n"
                            "# 지역별 매출액 합계\n"
                            "지역별_합계 = 매출.groupby('지역')['매출액'].sum()\n"
                            "print(지역별_합계)\n"
                            "# 지역\n"
                            "# 부산    2450\n"
                            "# 서울    5100\n"
                            "# Name: 매출액, dtype: int64\n\n"
                            "# 여러 집계 함수 동시 적용\n"
                            "지역별_통계 = 매출.groupby('지역')['매출액'].agg(['sum', 'mean', 'count', 'max'])\n"
                            "print(지역별_통계)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 다중 키로 groupby ────────────────────────────\n"
                            "지역_제품별 = 매출.groupby(['지역', '제품'])['매출액'].sum()\n"
                            "print(지역_제품별)\n"
                            "# 지역  제품\n"
                            "# 부산  A     950\n"
                            "#       B    1500\n"
                            "# 서울  A    4000\n"
                            "#       B    1100\n\n"
                            "# ── 여러 컬럼에 각기 다른 집계 적용 ─────────────\n"
                            "결과 = 매출.groupby('지역').agg(\n"
                            "    매출_합계=('매출액', 'sum'),\n"
                            "    매출_평균=('매출액', 'mean'),\n"
                            "    거래_횟수=('매출액', 'count'),\n"
                            "    총_수량=('수량', 'sum'),\n"
                            ")\n"
                            "print(결과.round(0))"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── groupby + 필터링 조합 ───────────────────────\n"
                            "# 지역별 평균 매출보다 높은 거래만 필터링\n"
                            "지역_평균 = 매출.groupby('지역')['매출액'].transform('mean')\n"
                            "고성과_거래 = 매출[매출['매출액'] > 지역_평균]\n"
                            "print(고성과_거래)\n\n"
                            "# ── transform: 그룹 집계값을 원래 크기로 되돌리기 ─\n"
                            "# 각 행에 지역 평균 매출을 새 컬럼으로 추가\n"
                            "매출_copy = pd.DataFrame(매출)\n"
                            "매출_copy['지역평균'] = 매출.groupby('지역')['매출액'].transform('mean')\n"
                            "매출_copy['평균대비'] = 매출_copy['매출액'] - 매출_copy['지역평균']\n"
                            "print(매출_copy[['지역', '매출액', '지역평균', '평균대비']].round(1))"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "transform()은 groupby의 집계 결과를 원래 DataFrame과 같은 크기로 확장합니다. "
                            "agg()는 그룹 수만큼의 행을 반환하지만, "
                            "transform()은 원래 행 수를 그대로 유지하면서 그룹 집계값을 각 행에 매핑합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 데이터 결합 ────────────────────────────────
            {
                "title": "merge, join, concat으로 데이터 합치기",
                "content": [
                    "실무에서 데이터는 여러 테이블에 분산되어 있는 경우가 대부분입니다. "
                    "merge, join, concat은 분산된 데이터를 하나로 합치는 도구입니다. "
                    "SQL을 아는 분이라면 merge를 JOIN, concat을 UNION으로 생각하면 됩니다.",
                    {
                        "type": "table",
                        "headers": ["함수", "동작", "SQL 유사 기능"],
                        "rows": [
                            ["pd.merge(left, right)", "공통 키 기준 수평 결합", "JOIN"],
                            ["df.join(other)", "인덱스 기준 수평 결합", "JOIN (인덱스 기반)"],
                            ["pd.concat([df1, df2])", "수직(행) 또는 수평(열) 결합", "UNION / 옆으로 붙이기"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n\n\n"
                            "# 예제 데이터\n"
                            "직원 = pd.DataFrame({\n"
                            "    '직원ID': [101, 102, 103, 104],\n"
                            "    '이름': ['김민준', '이서연', '박지호', '최수아'],\n"
                            "    '부서ID': [10, 20, 10, 30],\n"
                            "})\n\n"
                            "부서 = pd.DataFrame({\n"
                            "    '부서ID': [10, 20, 30, 40],\n"
                            "    '부서명': ['개발', '마케팅', '인사', '재무'],\n"
                            "})\n\n"
                            "# ── INNER JOIN (기본) ─────────────────────────────\n"
                            "# 양쪽에 모두 있는 키만 포함\n"
                            "결과 = pd.merge(직원, 부서, on='부서ID')\n"
                            "print(결과)\n"
                            "#    직원ID   이름  부서ID  부서명\n"
                            "# 0     101  김민준    10   개발\n"
                            "# 1     103  박지호    10   개발\n"
                            "# 2     102  이서연    20  마케팅\n"
                            "# 3     104  최수아    30   인사"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── LEFT / RIGHT / OUTER JOIN ────────────────────\n"
                            "# LEFT: 왼쪽 DataFrame 기준, 오른쪽에 없으면 NaN\n"
                            "left_join = pd.merge(직원, 부서, on='부서ID', how='left')\n\n"
                            "# RIGHT: 오른쪽 DataFrame 기준\n"
                            "right_join = pd.merge(직원, 부서, on='부서ID', how='right')\n\n"
                            "# OUTER: 양쪽 모두 포함, 없는 쪽은 NaN\n"
                            "outer_join = pd.merge(직원, 부서, on='부서ID', how='outer')\n"
                            "print(outer_join)\n"
                            "#    직원ID   이름  부서ID  부서명\n"
                            "# 0   101.0  김민준    10   개발\n"
                            "# 1   103.0  박지호    10   개발\n"
                            "# 2   102.0  이서연    20  마케팅\n"
                            "# 3   104.0  최수아    30   인사\n"
                            "# 4     NaN   NaN    40   재무  ← 직원 없는 부서\n\n"
                            "# ── 키 이름이 다를 때 ──────────────────────────────\n"
                            "df_a = pd.DataFrame({'emp_id': [1, 2], '이름': ['김', '이']})\n"
                            "df_b = pd.DataFrame({'id': [1, 2], '직급': ['대리', '과장']})\n"
                            "결합 = pd.merge(df_a, df_b, left_on='emp_id', right_on='id')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── pd.concat — 수직 결합 (행 추가) ─────────────\n"
                            "1월_매출 = pd.DataFrame({\n"
                            "    '날짜': ['2024-01-01', '2024-01-02'],\n"
                            "    '매출': [1000, 1200],\n"
                            "})\n"
                            "2월_매출 = pd.DataFrame({\n"
                            "    '날짜': ['2024-02-01', '2024-02-02'],\n"
                            "    '매출': [1100, 900],\n"
                            "})\n\n"
                            "# 위아래로 합치기\n"
                            "전체_매출 = pd.concat([1월_매출, 2월_매출], ignore_index=True)\n"
                            "print(전체_매출)\n\n"
                            "# ── 수평 결합 (열 추가) ──────────────────────────\n"
                            "기본정보 = pd.DataFrame({'이름': ['김', '이'], '나이': [25, 30]})\n"
                            "추가정보 = pd.DataFrame({'급여': [3500, 4000], '부서': ['개발', '인사']})\n"
                            "전체 = pd.concat([기본정보, 추가정보], axis=1)\n"
                            "print(전체)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "concat에 ignore_index=True를 사용하면 인덱스를 0부터 다시 정리합니다. "
                            "수직 결합 후 인덱스가 중복되는 것을 방지하려면 항상 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: pivot_table과 apply/map ───────────────────
            {
                "title": "pivot_table 활용과 apply, map으로 함수 적용",
                "content": [
                    "pivot_table은 행/열/값을 재구성하여 요약 보고서를 만드는 도구입니다. "
                    "apply와 map은 데이터의 각 요소에 임의의 함수를 적용하는 강력한 방법입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "매출 = pd.DataFrame({\n"
                            "    '연도': [2023, 2023, 2023, 2024, 2024, 2024],\n"
                            "    '분기': ['Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3'],\n"
                            "    '지역': ['서울', '서울', '부산', '서울', '부산', '서울'],\n"
                            "    '제품': ['A', 'B', 'A', 'A', 'B', 'B'],\n"
                            "    '매출액': [1200, 800, 950, 1500, 700, 1100],\n"
                            "    '수량': [12, 8, 9, 15, 7, 11],\n"
                            "})\n\n"
                            "# ── pivot_table 기본 ──────────────────────────────\n"
                            "# 행=연도, 열=지역, 값=매출액 합계\n"
                            "pt = pd.pivot_table(\n"
                            "    매출,\n"
                            "    values='매출액',\n"
                            "    index='연도',\n"
                            "    columns='지역',\n"
                            "    aggfunc='sum',\n"
                            "    fill_value=0,       # NaN 대신 0\n"
                            ")\n"
                            "print(pt)\n"
                            "# 지역   부산  서울\n"
                            "# 연도\n"
                            "# 2023   950  2000\n"
                            "# 2024   700  2600"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 다중 집계 함수 ────────────────────────────────\n"
                            "pt_multi = pd.pivot_table(\n"
                            "    매출,\n"
                            "    values='매출액',\n"
                            "    index='연도',\n"
                            "    columns='지역',\n"
                            "    aggfunc=['sum', 'mean'],\n"
                            "    fill_value=0,\n"
                            "    margins=True,    # 합계 행/열 추가\n"
                            "    margins_name='합계',\n"
                            ")\n"
                            "print(pt_multi.round(0))"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── apply — 행/열에 함수 적용 ──────────────────\n"
                            "성적 = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호'],\n"
                            "    '국어': [85, 92, 78],\n"
                            "    '수학': [90, 88, 95],\n"
                            "    '영어': [80, 95, 70],\n"
                            "})\n\n"
                            "# 각 행에서 최댓값\n"
                            "성적_copy = pd.DataFrame(성적)\n"
                            "성적_copy['최고점수'] = 성적[['국어', '수학', '영어']].max(axis=1)\n\n"
                            "# 컬럼에 함수 적용 (axis=0: 열 방향, axis=1: 행 방향)\n"
                            "성적_copy['등급'] = 성적[['국어', '수학', '영어']].mean(axis=1).apply(\n"
                            "    lambda 평균: 'A' if 평균 >= 90 else 'B' if 평균 >= 80 else 'C'\n"
                            ")\n"
                            "print(성적_copy)\n\n"
                            "# ── map — Series의 각 요소에 함수/딕셔너리 적용 ─\n"
                            "등급_점수 = {'A': 4.5, 'B': 3.5, 'C': 2.5}\n"
                            "성적_copy['GPA'] = 성적_copy['등급'].map(등급_점수)\n"
                            "print(성적_copy[['이름', '등급', 'GPA']])"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "apply는 유연하지만 느릴 수 있습니다. "
                            "가능하면 벡터화된 Pandas 연산(+, -, mean() 등)을 먼저 사용하고, "
                            "복잡한 조건이나 커스텀 로직이 필요할 때만 apply를 사용하세요. "
                            "성능이 중요하다면 np.vectorize()나 np.select()도 검토해보세요."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 — 매출 데이터 분석 ──────────────
            {
                "title": "실용 예제: 매출 데이터 분석 (그룹별 집계, 피벗)",
                "content": [
                    "지금까지 배운 결측치 처리, 타입 변환, groupby, merge, pivot_table을 "
                    "모두 활용하여 실전 매출 데이터를 분석합니다. "
                    "이 흐름이 실무 데이터 분석의 전형적인 패턴입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "# ── 1단계: 데이터 생성 (실무에서는 CSV에서 로드) ──\n"
                            "매출_raw = pd.DataFrame({\n"
                            "    '주문일': ['2024-01-05', '2024-01-12', '2024-02-03',\n"
                            "               '2024-02-18', '2024-03-07', '2024-03-21',\n"
                            "               '2024-01-25', '2024-02-14', '2024-03-30'],\n"
                            "    '지점': ['강남', '강남', '홍대', '홍대', '강남', '홍대', '강남', '홍대', '강남'],\n"
                            "    '제품': ['노트북', '마우스', '키보드', '노트북', '마우스', '노트북',\n"
                            "             '키보드', '마우스', '노트북'],\n"
                            "    '단가': [1200000, 45000, 85000, 1200000, 45000,\n"
                            "             1200000, 85000, None, 1200000],\n"
                            "    '수량': [2, 5, 3, 1, 8, 3, 4, 6, 1],\n"
                            "})"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 2단계: 데이터 정제 ─────────────────────────\n"
                            "df = pd.DataFrame(매출_raw)  # 새 객체로 작업\n\n"
                            "# 타입 변환\n"
                            "df['주문일'] = pd.to_datetime(df['주문일'])\n"
                            "df['월'] = df['주문일'].dt.month\n"
                            "df['분기'] = df['주문일'].dt.quarter.apply(lambda q: f'Q{q}')\n\n"
                            "# 결측치 처리: 단가 NaN → 제품별 중앙값으로 채우기\n"
                            "단가_중앙값 = df.groupby('제품')['단가'].transform('median')\n"
                            "df['단가'] = df['단가'].fillna(단가_중앙값)\n\n"
                            "# 매출 계산\n"
                            "df['매출액'] = df['단가'] * df['수량']\n"
                            "print('\\n=== 정제 후 데이터 ===')\n"
                            "print(df[['주문일', '지점', '제품', '매출액']].head())"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 3단계: 지점별 / 제품별 집계 ──────────────────\n"
                            "지점별 = df.groupby('지점').agg(\n"
                            "    총매출=('매출액', 'sum'),\n"
                            "    총수량=('수량', 'sum'),\n"
                            "    거래건수=('매출액', 'count'),\n"
                            "    건당평균=('매출액', 'mean'),\n"
                            ")\n"
                            "print('\\n=== 지점별 실적 ===')\n"
                            "print(지점별.sort_values('총매출', ascending=False))\n\n"
                            "# ── 4단계: 월별 × 지점별 피벗 테이블 ─────────────\n"
                            "월별_지점 = pd.pivot_table(\n"
                            "    df,\n"
                            "    values='매출액',\n"
                            "    index='월',\n"
                            "    columns='지점',\n"
                            "    aggfunc='sum',\n"
                            "    fill_value=0,\n"
                            "    margins=True,\n"
                            "    margins_name='합계',\n"
                            ")\n"
                            "print('\\n=== 월별 × 지점별 매출 (피벗) ===')\n"
                            "print(월별_지점 / 10000, '(단위: 만원)')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 5단계: 제품 정보와 병합하여 카테고리 분석 ───\n"
                            "제품정보 = pd.DataFrame({\n"
                            "    '제품': ['노트북', '마우스', '키보드'],\n"
                            "    '카테고리': ['컴퓨터', '주변기기', '주변기기'],\n"
                            "    '마진율': [0.15, 0.35, 0.30],\n"
                            "})\n\n"
                            "df_완성 = pd.merge(df, 제품정보, on='제품', how='left')\n"
                            "df_완성['이익'] = df_완성['매출액'] * df_완성['마진율']\n\n"
                            "카테고리별 = df_완성.groupby('카테고리').agg(\n"
                            "    총매출=('매출액', 'sum'),\n"
                            "    총이익=('이익', 'sum'),\n"
                            ").assign(이익률=lambda x: (x['총이익'] / x['총매출'] * 100).round(1))\n\n"
                            "print('\\n=== 카테고리별 매출 및 이익 ===')\n"
                            "print(카테고리별.sort_values('총매출', ascending=False))"
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "결측치 처리 방법(drop vs fill)은 데이터의 맥락과 분석 목적에 따라 선택하세요. 항상 이유를 기록하세요.",
            "pd.to_numeric(errors='coerce')는 숫자가 섞인 지저분한 컬럼을 안전하게 변환하는 최선의 방법입니다.",
            "groupby + agg()에서 named aggregation (컬럼명=('원본', '함수')) 패턴을 쓰면 결과 컬럼명이 명확해집니다.",
            "merge 시 how 파라미터를 항상 명시하세요. 기본값 inner가 의도치 않은 데이터 손실을 일으킬 수 있습니다.",
            "apply(lambda)는 강력하지만 느립니다. pd.cut(), np.where(), map()으로 대체 가능한지 먼저 검토하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "df.dropna(how='all')의 동작을 올바르게 설명한 것은?"
                ),
                "choices": [
                    "A) 하나라도 결측치가 있는 행을 제거한다",
                    "B) 모든 값이 결측치인 행만 제거한다",
                    "C) 결측치가 있는 열을 제거한다",
                    "D) 결측치를 0으로 채운다",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "pd.to_numeric(series, errors='coerce')에서 "
                    "변환할 수 없는 값은 어떻게 처리되는가?"
                ),
                "choices": [
                    "A) ValueError 발생",
                    "B) 0으로 변환",
                    "C) NaN으로 변환",
                    "D) 원래 문자열 그대로 유지",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "groupby().transform('mean')과 groupby().agg('mean')의 차이점은?"
                ),
                "choices": [
                    "A) 차이 없다",
                    "B) transform은 원래 DataFrame과 같은 크기 반환, agg는 그룹 수만큼 반환",
                    "C) agg는 원래 DataFrame과 같은 크기 반환, transform은 그룹 수만큼 반환",
                    "D) transform은 합계, agg는 평균만 계산한다",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "직원 데이터(이름, 부서, 급여, 연차)를 생성하고 "
                    "① 결측치 현황을 출력하고, "
                    "② 부서별 평균 급여와 평균 연차를 구하고, "
                    "③ 각 직원의 급여가 부서 평균 대비 높은지(True/False) 컬럼을 추가하세요."
                ),
                "hint": "③은 transform('mean')으로 부서 평균을 구한 뒤 비교하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "두 개의 DataFrame(주문 테이블, 고객 테이블)을 merge로 결합하고 "
                    "고객별 총 주문금액을 구한 뒤, "
                    "피벗 테이블로 월별 × 고객등급별 주문금액 합계를 출력하세요."
                ),
                "hint": "고객등급은 주문금액 기준 apply로 분류하세요. pivot_table의 margins=True로 합계 행을 추가하세요.",
            },
        ],
        "challenge": {
            "question": (
                "공공데이터 형식의 판매 데이터를 분석하는 파이프라인을 구현하세요. "
                "① 날짜 컬럼 변환 (년, 월, 요일 추출). "
                "② 결측치를 컬럼 특성에 맞게 처리 (수치: 중앙값, 범주: 최빈값). "
                "③ 요일별, 월별 매출 집계 후 가장 매출이 높은 요일과 월 출력. "
                "④ 제품 카테고리별 매출 비중(%) 계산. "
                "⑤ 전월 대비 증감률 계산 (pct_change() 활용). "
                "모든 단계에서 원본 데이터를 수정하지 않고 새 DataFrame을 생성하세요."
            ),
            "hint": (
                "요일 추출: dt.day_name() 또는 dt.weekday. "
                "전월 대비: df.groupby('월')['매출'].sum().pct_change() * 100. "
                "비중: groupby 합계 / 전체 합계 * 100."
            ),
        },
        "summary": [
            "결측치는 isna()로 파악하고, dropna()로 제거하거나 fillna()로 채운다.",
            "astype(), pd.to_numeric(), pd.to_datetime()으로 컬럼 타입을 올바르게 변환한다.",
            "groupby + agg()로 그룹별 집계를 수행하고, named aggregation으로 결과 컬럼명을 명확히 한다.",
            "transform()은 그룹 집계값을 원래 행 수에 맞게 확장하여 조건 필터링에 유용하다.",
            "pd.merge()는 공통 키 기준으로 테이블을 결합하며, how 파라미터로 JOIN 방식을 제어한다.",
            "pd.concat()으로 행을 추가(axis=0)하거나 열을 추가(axis=1)할 수 있다.",
        ],
    }
