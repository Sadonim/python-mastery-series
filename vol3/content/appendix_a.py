"""
부록 A: Pandas 치트시트
데이터 분석에서 가장 자주 쓰는 Pandas 명령어를 한눈에 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 A: Pandas 치트시트",
        "sections": [
            # ── 섹션 1: DataFrame 생성 & 기본 조회 ──
            {
                "title": "A.1 DataFrame 생성 & 기본 조회",
                "content": [
                    (
                        "DataFrame을 만드는 방법과 데이터를 처음 탐색할 때 "
                        "사용하는 핵심 명령어를 정리합니다."
                    ),
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "예시"],
                        "rows": [
                            ["pd.DataFrame(dict)", "딕셔너리로 생성", "pd.DataFrame({'a': [1,2], 'b': [3,4]})"],
                            ["pd.read_csv(path)", "CSV 파일 읽기", "pd.read_csv('data.csv', encoding='utf-8-sig')"],
                            ["pd.read_excel(path)", "엑셀 파일 읽기", "pd.read_excel('data.xlsx', sheet_name=0)"],
                            ["pd.read_json(path)", "JSON 파일 읽기", "pd.read_json('data.json')"],
                            ["df.shape", "행 × 열 수 반환", "(1000, 12)"],
                            ["df.dtypes", "컬럼별 데이터 타입", "name: object, age: int64"],
                            ["df.info()", "전체 구조 요약 출력", "결측값 수, 메모리 사용량 포함"],
                            ["df.describe()", "수치형 통계 요약", "count, mean, std, min, max"],
                            ["df.head(n)", "처음 n행 (기본 5)", "df.head(10)"],
                            ["df.tail(n)", "마지막 n행", "df.tail(3)"],
                            ["df.sample(n)", "무작위 n행 추출", "df.sample(5, random_state=42)"],
                            ["df.columns", "컬럼 이름 목록", "Index(['이름', '나이', ...])"],
                            ["df.index", "인덱스 정보", "RangeIndex(start=0, stop=1000, step=1)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "\n"
                            "# 딕셔너리로 DataFrame 생성\n"
                            "df = pd.DataFrame({\n"
                            "    '이름': ['김민준', '이서연', '박지호'],\n"
                            "    '나이': [28, 35, 22],\n"
                            "    '점수': [88.5, 92.0, 75.5],\n"
                            "})\n"
                            "\n"
                            "print(df.shape)      # (3, 3)\n"
                            "print(df.dtypes)\n"
                            "# 이름     object\n"
                            "# 나이      int64\n"
                            "# 점수    float64\n"
                            "\n"
                            "# CSV 읽기 — 자주 쓰는 옵션\n"
                            "df2 = pd.read_csv(\n"
                            "    'sales.csv',\n"
                            "    encoding='utf-8-sig',   # Windows Excel BOM 처리\n"
                            "    parse_dates=['날짜'],    # 날짜 컬럼 자동 변환\n"
                            "    index_col=None,          # 인덱스 컬럼 지정 안 함\n"
                            ")\n"
                        ),
                    },
                ],
            },
            # ── 섹션 2: 데이터 선택 & 필터링 ──
            {
                "title": "A.2 데이터 선택 & 필터링",
                "content": [
                    (
                        "원하는 행·열을 선택하고 조건으로 필터링하는 명령어입니다. "
                        "loc(라벨 기반)과 iloc(위치 기반)의 차이를 명확히 구분하세요."
                    ),
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "예시"],
                        "rows": [
                            ["df['컬럼']", "단일 컬럼 (Series 반환)", "df['이름']"],
                            ["df[['A', 'B']]", "다중 컬럼 선택", "df[['이름', '점수']]"],
                            ["df.loc[행, 열]", "라벨로 선택", "df.loc[0, '이름']"],
                            ["df.iloc[행, 열]", "정수 위치로 선택", "df.iloc[0:3, 1:3]"],
                            ["df[조건]", "불리언 인덱싱", "df[df['나이'] >= 30]"],
                            ["df.query('조건')", "문자열 조건 필터링", "df.query('나이 >= 30 and 점수 > 80')"],
                            ["df.isin(값_목록)", "목록 포함 여부", "df[df['지역'].isin(['서울', '부산'])]"],
                            ["df.between(a, b)", "범위 필터링", "df[df['점수'].between(80, 100)]"],
                            ["df.str.contains(패턴)", "문자열 포함 여부", "df[df['이름'].str.contains('김')]"],
                            ["df.nlargest(n, col)", "상위 n행", "df.nlargest(5, '점수')"],
                            ["df.nsmallest(n, col)", "하위 n행", "df.nsmallest(3, '나이')"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 조건 조합 — & (and), | (or), ~ (not)\n"
                            "# 각 조건을 반드시 괄호로 감싸야 합니다\n"
                            "mask = (df['나이'] >= 25) & (df['점수'] >= 85)\n"
                            "result = df[mask]\n"
                            "\n"
                            "# query() — 가독성이 좋고 변수 참조도 가능\n"
                            "threshold = 85\n"
                            "result2 = df.query('나이 >= 25 and 점수 >= @threshold')\n"
                            "\n"
                            "# loc으로 행 + 열 동시 선택\n"
                            "subset = df.loc[df['점수'] >= 80, ['이름', '점수']]\n"
                            "\n"
                            "# 복수 조건 isin\n"
                            "vip = df[df['등급'].isin(['VIP', 'GOLD'])]\n"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 집계 & 변환 ──
            {
                "title": "A.3 집계 & 변환",
                "content": [
                    (
                        "groupby와 집계 함수로 데이터를 요약하고, "
                        "apply·map·assign으로 새 컬럼을 생성하거나 값을 변환합니다."
                    ),
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "예시"],
                        "rows": [
                            ["df.groupby('키').agg(...)", "그룹별 집계", "df.groupby('구').agg({'대여':['sum','mean']})"],
                            ["df.groupby('키').size()", "그룹별 행 수", "df.groupby('등급').size()"],
                            ["df.pivot_table(...)", "피벗 테이블", "pd.pivot_table(df, values='매출', index='월', columns='지역')"],
                            ["df['열'].value_counts()", "빈도 집계", "df['등급'].value_counts()"],
                            ["df.sort_values('열')", "값 기준 정렬", "df.sort_values('점수', ascending=False)"],
                            ["df.assign(새열=식)", "새 컬럼 추가 (불변)", "df.assign(합계=df['A']+df['B'])"],
                            ["df['열'].apply(함수)", "함수 적용 (행/열)", "df['점수'].apply(lambda x: '합격' if x>=60 else '불합격')"],
                            ["df['열'].map(딕셔너리)", "값 매핑", "df['등급'].map({'A':4.0,'B':3.0})"],
                            ["df.rename(columns={...})", "컬럼명 변경", "df.rename(columns={'old':'new'})"],
                            ["pd.cut(s, bins)", "구간 분할", "pd.cut(df['나이'], bins=[0,20,40,60])"],
                            ["pd.qcut(s, q)", "분위수 분할", "pd.qcut(df['점수'], q=4, labels=['하','중하','중상','상'])"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# groupby + agg 다중 집계\n"
                            "result = (\n"
                            "    df.groupby('지역')\n"
                            "    .agg(\n"
                            "        고객수=('고객ID', 'count'),\n"
                            "        총매출=('매출', 'sum'),\n"
                            "        평균매출=('매출', 'mean'),\n"
                            "    )\n"
                            "    .round(1)\n"
                            "    .sort_values('총매출', ascending=False)\n"
                            "    .reset_index()\n"
                            ")\n"
                            "\n"
                            "# assign으로 파생 컬럼 추가 (원본 불변)\n"
                            "df2 = df.assign(\n"
                            "    세금=df['매출'] * 0.1,\n"
                            "    순매출=df['매출'] * 0.9,\n"
                            ")\n"
                            "\n"
                            "# 구간 분할\n"
                            "df2 = df.assign(\n"
                            "    나이대=pd.cut(\n"
                            "        df['나이'],\n"
                            "        bins=[0, 20, 30, 40, 60, 100],\n"
                            "        labels=['10대', '20대', '30대', '40대', '50대+'],\n"
                            "    )\n"
                            ")\n"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 결측치 & 타입 변환 ──
            {
                "title": "A.4 결측치 처리 & 타입 변환",
                "content": [
                    (
                        "실제 데이터에는 항상 결측값(NaN)이 존재합니다. "
                        "결측값을 탐지하고 채우거나 제거하는 방법과 "
                        "컬럼 타입을 변환하는 명령어를 정리합니다."
                    ),
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "예시"],
                        "rows": [
                            ["df.isnull()", "결측값 여부 (True/False)", "df.isnull().sum() — 컬럼별 결측 수"],
                            ["df.notnull()", "비결측값 여부", "df[df['이름'].notnull()]"],
                            ["df.dropna()", "결측행 제거", "df.dropna(subset=['이름', '나이'])"],
                            ["df.fillna(값)", "결측값 채우기", "df['점수'].fillna(df['점수'].mean())"],
                            ["df.fillna(method='ffill')", "앞 값으로 채우기", "시계열 데이터에 유용"],
                            ["df.fillna(method='bfill')", "뒤 값으로 채우기", "시계열 데이터에 유용"],
                            ["pd.to_numeric(s, errors=)", "수치형으로 변환", "pd.to_numeric(df['값'], errors='coerce')"],
                            ["pd.to_datetime(s)", "날짜형으로 변환", "pd.to_datetime(df['날짜'])"],
                            ["df.astype(타입)", "타입 강제 변환", "df['나이'].astype(int)"],
                            ["df['열'].str.strip()", "문자열 공백 제거", "df['이름'].str.strip()"],
                            ["df.drop_duplicates()", "중복행 제거", "df.drop_duplicates(subset=['이름'])"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 결측값 현황 파악\n"
                            "missing = df.isnull().sum()\n"
                            "missing_pct = (missing / len(df) * 100).round(1)\n"
                            "print(pd.DataFrame({'결측수': missing, '결측률(%)': missing_pct}))\n"
                            "\n"
                            "# 전략별 처리\n"
                            "df2 = (\n"
                            "    df\n"
                            "    .assign(\n"
                            "        점수=df['점수'].fillna(df['점수'].median()),   # 중앙값 대체\n"
                            "        지역=df['지역'].fillna('미입력'),               # 기본값 대체\n"
                            "    )\n"
                            "    .dropna(subset=['이름'])                            # 이름 없는 행 제거\n"
                            ")\n"
                            "\n"
                            "# 수치형 변환 — 변환 불가 값은 NaN으로\n"
                            "df2['매출'] = pd.to_numeric(df2['매출'], errors='coerce')\n"
                            "\n"
                            "# 날짜 변환 후 파생 컬럼 추출\n"
                            "df2['날짜'] = pd.to_datetime(df2['날짜'])\n"
                            "df2 = df2.assign(\n"
                            "    연도=df2['날짜'].dt.year,\n"
                            "    월=df2['날짜'].dt.month,\n"
                            "    요일=df2['날짜'].dt.day_name(),\n"
                            ")\n"
                        ),
                    },
                ],
            },
            # ── 섹션 5: 저장 & 시각화 명령어 ──
            {
                "title": "A.5 저장 & 시각화 명령어",
                "content": [
                    (
                        "분석이 끝난 DataFrame을 파일로 저장하거나 "
                        "Pandas 내장 플롯 기능으로 빠르게 시각화하는 명령어입니다."
                    ),
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "주요 옵션"],
                        "rows": [
                            ["df.to_csv(path)", "CSV로 저장", "index=False, encoding='utf-8-sig'"],
                            ["df.to_excel(path)", "엑셀로 저장", "sheet_name='Sheet1', index=False"],
                            ["df.to_json(path)", "JSON으로 저장", "orient='records', force_ascii=False"],
                            ["df.plot(kind='bar')", "막대 그래프", "color, figsize, title"],
                            ["df.plot(kind='line')", "선 그래프", "marker='o', linewidth=2"],
                            ["df.plot(kind='scatter')", "산점도", "x='컬럼', y='컬럼'"],
                            ["df.plot(kind='hist')", "히스토그램", "bins=20, edgecolor='white'"],
                            ["df.plot(kind='box')", "박스플롯", "vert=True, patch_artist=True"],
                            ["df['열'].plot(kind='pie')", "파이 차트", "autopct='%1.1f%%'"],
                            ["df.corr()", "상관계수 행렬", "numeric_only=True"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import matplotlib.pyplot as plt\n"
                            "\n"
                            "# CSV 저장 (Excel 호환 인코딩)\n"
                            "df.to_csv('result.csv', index=False, encoding='utf-8-sig')\n"
                            "\n"
                            "# 엑셀 저장 — 여러 시트\n"
                            "with pd.ExcelWriter('report.xlsx') as writer:\n"
                            "    df.to_excel(writer, sheet_name='원본', index=False)\n"
                            "    district_df.to_excel(writer, sheet_name='구별집계', index=False)\n"
                            "\n"
                            "# Pandas 내장 플롯 — 빠른 탐색용\n"
                            "ax = (\n"
                            "    df.groupby('지역')['매출']\n"
                            "    .sum()\n"
                            "    .sort_values(ascending=False)\n"
                            "    .plot(kind='bar', figsize=(10, 5), title='지역별 매출')\n"
                            ")\n"
                            "plt.tight_layout()\n"
                            "plt.savefig('sales_by_region.png', dpi=150)\n"
                            "plt.close()\n"
                            "\n"
                            "# 상관계수 히트맵\n"
                            "import seaborn as sns\n"
                            "corr = df.select_dtypes('number').corr()\n"
                            "sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')\n"
                            "plt.tight_layout()\n"
                            "plt.savefig('correlation.png', dpi=150)\n"
                            "plt.close()\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Pandas 내장 plot은 빠른 탐색에는 좋지만, "
                            "발표용·보고서용 차트는 Matplotlib/Seaborn을 직접 사용하세요. "
                            "내장 plot의 반환값은 Axes 객체이므로 "
                            "ax.set_title(), ax.set_xlabel() 등으로 세부 조정이 가능합니다."
                        ),
                    },
                ],
            },
        ],
    }
