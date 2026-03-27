"""챕터 5: 특성 공학 — 좋은 데이터가 좋은 모델을 만든다."""


def get_chapter():
    """챕터 5 콘텐츠를 반환한다."""
    return {
        "number": 5,
        "title": "특성 공학",
        "subtitle": "좋은 데이터가 좋은 모델을 만든다",
        "big_picture": (
            "머신러닝 실무자들은 모델 선택보다 데이터 준비에 훨씬 많은 시간을 씁니다. "
            "'쓰레기가 들어가면 쓰레기가 나온다(Garbage In, Garbage Out)'는 말처럼, "
            "아무리 좋은 알고리즘도 불량한 데이터로는 좋은 결과를 낼 수 없습니다. "
            "특성 공학(Feature Engineering)은 원본 데이터를 모델이 학습하기 좋은 형태로 변환하는 기술입니다. "
            "결측치 처리, 범주형 인코딩, 스케일링, 특성 선택을 배우고, "
            "scikit-learn의 Pipeline과 ColumnTransformer로 이 모든 과정을 "
            "재사용 가능한 하나의 워크플로로 묶는 방법을 익힙니다."
        ),
        "sections": [
            # ── 섹션 1: 특성 공학이란? ────────────────────────────
            {
                "title": "특성 공학이란? — 왜 중요한가",
                "content": [
                    "특성 공학은 원본 데이터로부터 모델 성능을 극대화하는 입력 특성을 만드는 과정입니다. "
                    "단순히 '데이터 청소'가 아니라 도메인 지식을 활용해 "
                    "새로운 특성을 생성하거나 기존 특성을 변환하는 창의적 작업입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "군 부사관 진급 심사를 예로 들어봅시다. "
                            "원본 데이터: 생년월일, 임관일, 훈련 점수 기록들. "
                            "특성 공학 결과: 복무 기간(현재 날짜 - 임관일), "
                            "최근 3회 훈련 평균 점수, 점수 상승 추세(기울기). "
                            "원본보다 '가공된 특성'이 진급 예측에 훨씬 유용합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["특성 공학 작업", "내용", "효과"],
                        "rows": [
                            ["결측치 처리", "빈 값을 채우거나 제거", "모델 학습 가능 상태로 정비"],
                            ["범주형 인코딩", "문자열을 숫자로 변환", "알고리즘이 처리 가능하게"],
                            ["특성 스케일링", "값의 범위를 통일", "거리 기반 알고리즘 성능 향상"],
                            ["특성 선택", "중요 특성만 선택", "차원의 저주 회피, 모델 경량화"],
                            ["특성 생성", "기존 특성 조합으로 새 특성 생성", "도메인 지식 반영"],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "전처리 파이프라인",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "원본 데이터", "sub": "결측치·문자열·다양한 스케일"},
                            {"label": "결측치 처리", "sub": "Imputer"},
                            {"label": "인코딩", "sub": "LabelEncoder / OneHotEncoder"},
                            {"label": "스케일링", "sub": "StandardScaler / MinMaxScaler"},
                            {"label": "특성 선택", "sub": "SelectKBest"},
                            {"label": "모델 학습", "sub": "fit / predict"},
                        ],
                        "note": (
                            "각 단계를 Pipeline으로 묶으면 fit/transform이 자동화되고 "
                            "데이터 누수 없이 재사용 가능한 전처리 워크플로가 완성됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 결측치 처리 ──────────────────────────────
            {
                "title": "결측치 처리 — SimpleImputer",
                "content": [
                    "실제 데이터에는 반드시 결측치(NaN)가 있습니다. "
                    "scikit-learn의 대부분 알고리즘은 결측치를 허용하지 않으므로 "
                    "먼저 처리해야 합니다. SimpleImputer는 가장 기본적인 결측치 대체 도구입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "import pandas as pd\n"
                            "from sklearn.impute import SimpleImputer\n\n\n"
                            "# 결측치가 있는 샘플 데이터 생성\n"
                            "data = pd.DataFrame({\n"
                            "    '나이':    [25, np.nan, 31, 22, np.nan, 28],\n"
                            "    '체력점수': [88, 92, np.nan, 75, 85, np.nan],\n"
                            "    '계급코드': [1, 2, np.nan, 1, 3, 2],\n"
                            "})\n\n"
                            "print('원본 데이터:')\n"
                            "print(data)\n"
                            "print(f'\\n결측치 수:\\n{data.isnull().sum()}')\n\n"
                            "# ── 전략별 Imputer 비교 ──────────────────────────────\n"
                            "strategies = {\n"
                            "    '평균(mean)':     'mean',\n"
                            "    '중앙값(median)': 'median',\n"
                            "    '최빈값(most_frequent)': 'most_frequent',\n"
                            "    '상수(constant=0)': 'constant',\n"
                            "}\n\n"
                            "for label, strategy in strategies.items():\n"
                            "    kwargs = {'fill_value': 0} if strategy == 'constant' else {}\n"
                            "    imp = SimpleImputer(strategy=strategy, **kwargs)\n"
                            "    filled = imp.fit_transform(data)\n"
                            "    print(f'\\n[{label}] 결측치 대체 후 (나이, 체력점수, 계급코드):')\n"
                            "    print(np.round(filled, 2))"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["전략", "strategy 값", "적합한 특성", "주의사항"],
                        "rows": [
                            ["평균", "mean", "연속형 수치, 정규 분포", "이상치에 민감"],
                            ["중앙값", "median", "연속형 수치, 치우친 분포", "이상치에 강건 (권장)"],
                            ["최빈값", "most_frequent", "범주형, 이진형", "연속형에는 부적합"],
                            ["상수", "constant", "도메인 의미가 있는 경우", "fill_value 직접 지정"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "결측치 자체가 정보일 수 있습니다. "
                            "예를 들어 '체력 측정 미실시' 자체가 의미 있는 패턴이라면 "
                            "'체력점수_결측' 이진 특성을 추가한 뒤 대체하는 방법을 고려하세요. "
                            "MissingIndicator 또는 pd.isnull()로 구현할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 범주형 인코딩 ────────────────────────────
            {
                "title": "범주형 인코딩 — 문자를 숫자로",
                "content": [
                    "머신러닝 모델은 숫자만 처리할 수 있습니다. "
                    "'상병', '병장', '하사' 같은 문자형 데이터는 인코딩이 필요합니다. "
                    "어떤 인코딩을 쓰느냐에 따라 모델이 데이터를 해석하는 방식이 달라집니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import numpy as np\n"
                            "from sklearn.preprocessing import (\n"
                            "    LabelEncoder, OneHotEncoder, OrdinalEncoder\n"
                            ")\n\n\n"
                            "ranks = ['일병', '상병', '병장', '상병', '일병', '병장']\n"
                            "colors = ['빨강', '파랑', '빨강', '초록', '파랑', '빨강']\n\n"
                            "# ── LabelEncoder: 정수 레이블 (대소 관계 X, 타깃 레이블 전용) ──\n"
                            "le = LabelEncoder()\n"
                            "encoded = le.fit_transform(ranks)\n"
                            "print(f'LabelEncoder 결과: {encoded}')\n"
                            "print(f'클래스 순서: {le.classes_}')  # 알파벳 순\n\n"
                            "# !! 경고: 특성에 LabelEncoder를 쓰면 모델이 숫자 크기를 순위로 오해 !!\n\n"
                            "# ── OrdinalEncoder: 순서 있는 범주형 특성 ─────────────\n"
                            "# 명시적 순서 지정 가능\n"
                            "oe = OrdinalEncoder(\n"
                            "    categories=[['이병', '일병', '상병', '병장', '하사']]\n"
                            ")\n"
                            "rank_array = np.array(ranks).reshape(-1, 1)\n"
                            "encoded_ord = oe.fit_transform(rank_array)\n"
                            "print(f'\\nOrdinalEncoder: {encoded_ord.ravel()}')\n"
                            "# 이병=0, 일병=1, 상병=2, 병장=3 으로 올바른 순서 반영\n\n"
                            "# ── OneHotEncoder: 순서 없는 범주형 특성 ──────────────\n"
                            "ohe = OneHotEncoder(sparse_output=False)  # dense 행렬로 반환\n"
                            "color_array = np.array(colors).reshape(-1, 1)\n"
                            "encoded_ohe = ohe.fit_transform(color_array)\n\n"
                            "print(f'\\nOneHotEncoder 결과 (빨강/초록/파랑 순):')\n"
                            "print(encoded_ohe)\n"
                            "print(f'특성명: {ohe.get_feature_names_out()}')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["인코더", "대상", "특성 수 변화", "언제 사용"],
                        "rows": [
                            ["LabelEncoder", "타깃(y) 레이블", "변화 없음", "분류 타깃 인코딩"],
                            ["OrdinalEncoder", "순서 있는 범주형 특성", "변화 없음", "등급·크기 순서 있을 때"],
                            ["OneHotEncoder", "순서 없는 범주형 특성", "카테고리 수만큼 증가", "색상·지역·부대명 등"],
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            "카테고리 수가 매우 많은 경우(예: 부대명 1000개) OneHotEncoder는 "
                            "특성 수를 폭발적으로 늘립니다. "
                            "이런 경우 Target Encoding이나 Binary Encoding을 검토하거나 "
                            "max_categories 파라미터로 상위 N개만 처리하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 특성 스케일링 ──────────────────────────────
            {
                "title": "특성 스케일링 — 공평한 경쟁 환경",
                "content": [
                    "키(cm)와 체중(kg), 나이(년)는 단위와 범위가 완전히 다릅니다. "
                    "KNN, SVM, 신경망 등 거리 기반 알고리즘은 값이 큰 특성에 편향됩니다. "
                    "스케일링은 모든 특성이 동등한 영향력을 갖도록 범위를 통일합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "from sklearn.preprocessing import (\n"
                            "    StandardScaler, MinMaxScaler, RobustScaler\n"
                            ")\n\n\n"
                            "# 이상치 포함 샘플 데이터 (마지막 값이 이상치)\n"
                            "data = np.array([[170, 65], [175, 70], [168, 60],\n"
                            "                 [180, 80], [165, 55], [200, 150]])  # 마지막이 이상치\n\n"
                            "# ── StandardScaler: 평균 0, 표준편차 1 ──────────────\n"
                            "ss = StandardScaler()\n"
                            "data_ss = ss.fit_transform(data)\n"
                            "print(f'StandardScaler — 평균: {data_ss.mean(axis=0).round(2)}')\n"
                            "print(f'                  표준편차: {data_ss.std(axis=0).round(2)}')\n\n"
                            "# ── MinMaxScaler: 0~1 범위로 압축 ───────────────────\n"
                            "mms = MinMaxScaler()  # feature_range=(0, 1) 기본값\n"
                            "data_mms = mms.fit_transform(data)\n"
                            "print(f'\\nMinMaxScaler — 최솟값: {data_mms.min(axis=0).round(2)}')\n"
                            "print(f'               최댓값: {data_mms.max(axis=0).round(2)}')\n\n"
                            "# ── RobustScaler: 중앙값 기준, 이상치에 강건 ───────\n"
                            "rs = RobustScaler()\n"
                            "data_rs = rs.fit_transform(data)\n"
                            "print(f'\\nRobustScaler  — 중앙값: {np.median(data_rs, axis=0).round(2)}')\n"
                            "# 이상치(200, 150)가 다른 샘플에 미치는 영향 최소화"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["스케일러", "변환 방식", "이상치 영향", "권장 상황"],
                        "rows": [
                            ["StandardScaler", "(x - 평균) / 표준편차", "민감", "정규 분포 가정, 대부분 상황"],
                            ["MinMaxScaler", "(x - min) / (max - min)", "매우 민감", "신경망 입력, 이미지 픽셀"],
                            ["RobustScaler", "(x - 중앙값) / IQR", "강건", "이상치 많은 실무 데이터"],
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            "스케일러는 훈련 데이터로만 fit 하고, "
                            "테스트 데이터에는 transform만 적용해야 합니다. "
                            "테스트 데이터로 fit_transform하면 데이터 누수가 발생해 "
                            "성능이 낙관적으로 평가됩니다. Pipeline을 사용하면 이를 자동으로 방지합니다."
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "결정 트리 계열(DecisionTree, RandomForest, XGBoost)은 "
                            "분할 기준이 절대값이 아닌 순서에만 의존하므로 스케일링이 불필요합니다. "
                            "스케일링이 필수인 알고리즘: KNN, SVM, 로지스틱 회귀, 신경망, PCA."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 특성 선택 ───────────────────────────────
            {
                "title": "특성 선택 — 덜어내는 것도 기술",
                "content": [
                    "특성이 너무 많으면 '차원의 저주'로 모델 성능이 오히려 떨어집니다. "
                    "불필요한 특성을 제거하면 모델이 단순해지고 "
                    "과적합이 줄고 학습이 빨라집니다. "
                    "특성 선택은 '어떤 특성이 타깃과 관련 있는가'를 통계적으로 측정합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.feature_selection import (\n"
                            "    SelectKBest, f_classif, mutual_info_classif, chi2\n"
                            ")\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "import numpy as np\n\n\n"
                            "cancer = load_breast_cancer()\n"
                            "X, y = cancer.data, cancer.target\n"
                            "feature_names = cancer.feature_names\n\n"
                            "# ── SelectKBest: 통계 점수 상위 K개 선택 ─────────────\n"
                            "# f_classif: ANOVA F-통계량 (연속형 특성 + 분류 타깃)\n"
                            "selector = SelectKBest(score_func=f_classif, k=10)\n"
                            "X_selected = selector.fit_transform(X, y)\n\n"
                            "print(f'원본 특성 수: {X.shape[1]}')\n"
                            "print(f'선택된 특성 수: {X_selected.shape[1]}')\n\n"
                            "# 선택된 특성 이름 확인\n"
                            "selected_mask = selector.get_support()\n"
                            "selected_names = feature_names[selected_mask]\n"
                            "scores = selector.scores_[selected_mask]\n\n"
                            "print('\\n선택된 상위 10개 특성 (F-점수 순):')\n"
                            "ranked = sorted(zip(selected_names, scores), key=lambda x: x[1], reverse=True)\n"
                            "for name, score in ranked:\n"
                            "    print(f'  {name}: {score:.2f}')\n\n"
                            "# ── 상관관계 기반 특성 선택 (pandas 활용) ──────────\n"
                            "import pandas as pd\n\n"
                            "df = pd.DataFrame(X, columns=feature_names)\n"
                            "df['target'] = y\n"
                            "corr_with_target = df.corr()['target'].abs().sort_values(ascending=False)\n\n"
                            "print('\\n타깃과 상관관계 높은 상위 5개 특성:')\n"
                            "print(corr_with_target[1:6])  # target 자신 제외"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["방법", "score_func", "특성 유형", "타깃 유형"],
                        "rows": [
                            ["F-검정", "f_classif", "연속형", "분류"],
                            ["상호 정보량", "mutual_info_classif", "연속형·범주형", "분류"],
                            ["카이제곱", "chi2", "비음수 정수 (빈도)", "분류"],
                            ["F-검정 (회귀)", "f_regression", "연속형", "회귀"],
                        ],
                    },
                ],
            },
            # ── 섹션 6: Pipeline과 ColumnTransformer ─────────────
            {
                "title": "Pipeline과 ColumnTransformer — 전처리를 하나로",
                "content": [
                    "지금까지 배운 결측치 처리, 인코딩, 스케일링, 특성 선택을 "
                    "각각 따로 적용하면 코드가 복잡해지고 데이터 누수 위험이 있습니다. "
                    "Pipeline은 이 단계들을 순서대로 연결해 "
                    "fit/transform/predict를 한 번의 호출로 처리합니다. "
                    "ColumnTransformer는 수치형과 범주형 특성에 서로 다른 전처리를 동시에 적용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "import pandas as pd\n"
                            "from sklearn.pipeline import Pipeline\n"
                            "from sklearn.compose import ColumnTransformer\n"
                            "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n"
                            "from sklearn.impute import SimpleImputer\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.model_selection import train_test_split\n\n\n"
                            "# 수치형 + 범주형이 혼합된 샘플 데이터\n"
                            "data = pd.DataFrame({\n"
                            "    '나이':    [25, np.nan, 31, 22, 28, 35, np.nan, 29],\n"
                            "    '체력점수': [88, 92, np.nan, 75, 85, 78, 90, np.nan],\n"
                            "    '계급':    ['이병', '일병', '상병', '이병', '병장', '상병', '일병', '이병'],\n"
                            "    '부대유형': ['보병', '포병', np.nan, '보병', '기갑', '보병', '포병', '기갑'],\n"
                            "    '우수자여부': [1, 0, 1, 0, 1, 0, 1, 0],  # 타깃\n"
                            "})\n\n"
                            "X = data.drop(columns='우수자여부')\n"
                            "y = data['우수자여부']\n\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.3, random_state=42\n"
                            ")\n\n"
                            "# ── 특성 그룹 정의 ─────────────────────────────────\n"
                            "numeric_features = ['나이', '체력점수']          # 수치형\n"
                            "categorical_features = ['계급', '부대유형']      # 범주형\n\n"
                            "# ── 수치형 전처리 파이프라인 ───────────────────────\n"
                            "numeric_transformer = Pipeline(steps=[\n"
                            "    ('imputer', SimpleImputer(strategy='median')),  # 결측치: 중앙값\n"
                            "    ('scaler', StandardScaler()),                    # 스케일링\n"
                            "])\n\n"
                            "# ── 범주형 전처리 파이프라인 ───────────────────────\n"
                            "categorical_transformer = Pipeline(steps=[\n"
                            "    ('imputer', SimpleImputer(strategy='most_frequent')),  # 결측치: 최빈값\n"
                            "    ('encoder', OneHotEncoder(handle_unknown='ignore')),   # 원핫 인코딩\n"
                            "])\n\n"
                            "# ── ColumnTransformer: 특성 유형별 전처리 조합 ─────\n"
                            "preprocessor = ColumnTransformer(transformers=[\n"
                            "    ('num', numeric_transformer, numeric_features),\n"
                            "    ('cat', categorical_transformer, categorical_features),\n"
                            "])\n\n"
                            "# ── 전체 파이프라인 (전처리 + 모델) ─────────────────\n"
                            "full_pipeline = Pipeline(steps=[\n"
                            "    ('preprocessor', preprocessor),\n"
                            "    ('classifier', RandomForestClassifier(n_estimators=50, random_state=42)),\n"
                            "])\n\n"
                            "# 한 번의 fit으로 전처리 + 학습이 모두 완료\n"
                            "full_pipeline.fit(X_train, y_train)\n"
                            "score = full_pipeline.score(X_test, y_test)\n"
                            "print(f'파이프라인 테스트 정확도: {score:.4f}')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── Pipeline과 GridSearchCV 결합 ─────────────────────\n"
                            "# 파이프라인 파라미터 이름: 단계명__파라미터명\n"
                            "from sklearn.model_selection import GridSearchCV\n\n"
                            "param_grid = {\n"
                            "    'classifier__n_estimators': [50, 100],\n"
                            "    'classifier__max_depth': [3, 5, None],\n"
                            "    'preprocessor__num__imputer__strategy': ['mean', 'median'],\n"
                            "}\n\n"
                            "grid_search = GridSearchCV(\n"
                            "    full_pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1\n"
                            ")\n"
                            "grid_search.fit(X_train, y_train)\n\n"
                            "print(f'최적 파라미터: {grid_search.best_params_}')\n"
                            "print(f'최고 CV 정확도: {grid_search.best_score_:.4f}')\n\n"
                            "# !! Pipeline 덕분에 전처리 파라미터도 GridSearch 대상이 됨 !!"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Pipeline의 가장 큰 장점은 '배포 단순화'입니다. "
                            "모델 파일 하나(pipeline.pkl)만 저장하면 "
                            "추론 시 전처리와 예측이 자동으로 처리됩니다. "
                            "import joblib; joblib.dump(full_pipeline, 'pipeline.pkl')으로 저장하고 "
                            "joblib.load('pipeline.pkl').predict(new_data)로 바로 예측합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": {
            "title": "실무 팁",
            "content": [
                {
                    "type": "tip",
                    "text": (
                        "MLOps 파이프라인에서 전처리 객체(Imputer, Scaler, Encoder)는 "
                        "훈련 데이터로 fit한 상태를 반드시 저장해야 합니다. "
                        "운영 환경에서 새 데이터에 동일한 파라미터로 transform해야 하기 때문입니다. "
                        "Pipeline 전체를 joblib으로 직렬화하면 이 문제가 자동 해결됩니다."
                    ),
                },
                {
                    "type": "tip",
                    "text": (
                        "특성 공학 우선순위: 결측치 처리 → 인코딩 → 스케일링 → 특성 선택 순서로 진행하세요. "
                        "특성 선택은 반드시 마지막에 수행해야 올바른 중요도를 얻습니다. "
                        "스케일링 전 선택하면 특성의 크기 차이가 선택에 영향을 줍니다."
                    ),
                },
                {
                    "type": "warning",
                    "text": (
                        "OneHotEncoder의 handle_unknown='ignore'는 필수입니다. "
                        "운영 환경에서 훈련 때 보지 못한 카테고리가 입력될 수 있습니다. "
                        "이 옵션 없이 배포하면 새 카테고리에서 모델이 오류를 냅니다."
                    ),
                },
            ],
        },
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "SimpleImputer(strategy='median')가 가장 적합한 상황은?",
                "choices": [
                    "A) 범주형 특성에 최빈값을 채워야 할 때",
                    "B) 이상치가 있는 연속형 특성에서 중앙값으로 결측치를 채울 때",
                    "C) 모든 결측치를 0으로 채워야 할 때",
                    "D) 결측치를 제거해야 할 때",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "'빨강/파랑/초록' 같이 순서가 없는 범주형 특성을 인코딩할 때 "
                    "가장 적합한 방법은?"
                ),
                "choices": [
                    "A) LabelEncoder — 정수 0, 1, 2로 변환",
                    "B) OrdinalEncoder — 순서를 명시해 변환",
                    "C) OneHotEncoder — 카테고리별 이진 열로 변환",
                    "D) StandardScaler — 표준화 후 사용",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "스케일러를 훈련 데이터로만 fit하고 테스트 데이터에는 transform만 적용해야 하는 이유를 "
                    "'데이터 누수(Data Leakage)'와 연관지어 설명하시오."
                ),
                "answer": (
                    "스케일러를 테스트 데이터로 fit하면 테스트 데이터의 평균/표준편차가 "
                    "변환 파라미터에 포함됩니다. "
                    "이는 훈련 시 미래 데이터 정보가 사용되는 '데이터 누수'로, "
                    "모델 성능이 실제보다 낙관적으로 측정됩니다. "
                    "실제 운영 환경에서는 훈련 때의 파라미터로만 변환해야 하므로 "
                    "훈련 데이터 fit 파라미터를 저장해 재사용해야 합니다."
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "다음 배열에 StandardScaler와 MinMaxScaler를 각각 적용하고 결과를 출력하시오. "
                    "data = [[1, 200], [2, 150], [3, 300], [4, 100], [5, 250]]"
                ),
                "hint": (
                    "fit_transform(data)로 변환 후 결과를 np.round(..., 4)로 출력합니다. "
                    "StandardScaler는 평균 0/표준편차 1, MinMaxScaler는 0~1 범위가 됩니다."
                ),
                "answer": (
                    "import numpy as np\n"
                    "from sklearn.preprocessing import StandardScaler, MinMaxScaler\n\n"
                    "data = [[1, 200], [2, 150], [3, 300], [4, 100], [5, 250]]\n\n"
                    "ss = StandardScaler()\n"
                    "mms = MinMaxScaler()\n\n"
                    "print('StandardScaler:')\n"
                    "print(np.round(ss.fit_transform(data), 4))\n\n"
                    "print('MinMaxScaler:')\n"
                    "print(np.round(mms.fit_transform(data), 4))"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "수치형 특성 ['age', 'score']와 범주형 특성 ['rank']가 있는 "
                    "아래 DataFrame에 ColumnTransformer를 적용하시오. "
                    "수치형: SimpleImputer(median) + StandardScaler. "
                    "범주형: SimpleImputer(most_frequent) + OneHotEncoder. "
                    "변환 결과 배열의 형태(shape)를 출력하시오.\n"
                    "data = pd.DataFrame({'age': [25, None, 30], "
                    "'score': [88, 92, None], 'rank': ['이병', None, '상병']})"
                ),
                "hint": (
                    "Pipeline으로 수치형/범주형 전처리를 각각 만들고 "
                    "ColumnTransformer에 ('이름', 파이프라인, 열목록) 형태로 등록합니다."
                ),
                "answer": (
                    "import pandas as pd\n"
                    "import numpy as np\n"
                    "from sklearn.pipeline import Pipeline\n"
                    "from sklearn.compose import ColumnTransformer\n"
                    "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n"
                    "from sklearn.impute import SimpleImputer\n\n"
                    "data = pd.DataFrame({\n"
                    "    'age': [25, None, 30],\n"
                    "    'score': [88, 92, None],\n"
                    "    'rank': ['이병', None, '상병'],\n"
                    "})\n\n"
                    "num_pipe = Pipeline([\n"
                    "    ('imp', SimpleImputer(strategy='median')),\n"
                    "    ('scl', StandardScaler()),\n"
                    "])\n"
                    "cat_pipe = Pipeline([\n"
                    "    ('imp', SimpleImputer(strategy='most_frequent')),\n"
                    "    ('enc', OneHotEncoder(handle_unknown='ignore')),\n"
                    "])\n\n"
                    "ct = ColumnTransformer([\n"
                    "    ('num', num_pipe, ['age', 'score']),\n"
                    "    ('cat', cat_pipe, ['rank']),\n"
                    "])\n\n"
                    "result = ct.fit_transform(data)\n"
                    "print('변환 결과 shape:', result.shape)"
                ),
            },
        ],
        "challenge": {
            "question": (
                "완전한 특성 공학 파이프라인을 구축하세요. "
                "아래 단계를 모두 포함해야 합니다. "
                "1) fetch_openml('titanic', version=1)로 타이타닉 데이터 로드 "
                "   (또는 make_classification으로 유사 데이터 생성) "
                "2) 수치형 특성: SimpleImputer(median) + RobustScaler "
                "3) 범주형 특성: SimpleImputer(most_frequent) + OneHotEncoder(handle_unknown='ignore') "
                "4) ColumnTransformer로 결합 후 RandomForestClassifier와 Pipeline으로 연결 "
                "5) 5-Fold StratifiedKFold 교차 검증으로 accuracy와 f1 측정 및 출력 "
                "6) GridSearchCV로 classifier__n_estimators=[50, 100]와 "
                "   classifier__max_depth=[5, None] 튜닝 후 최적 파라미터 출력 "
                "코드를 재사용 가능하도록 함수로 구성하세요 "
                "(build_pipeline, evaluate_pipeline, tune_pipeline 분리)."
            ),
            "hint": (
                "타이타닉 데이터 로드가 어려우면 "
                "make_classification(n_samples=800, n_features=15, n_informative=8, random_state=42)로 "
                "데이터를 생성하고 범주형은 pd.cut으로 수치형을 구간화해 만드세요. "
                "함수를 분리하면 테스트하기 쉽고 각 단계를 독립적으로 교체할 수 있어 MLOps에 적합합니다."
            ),
        },
        "summary": [
            "특성 공학은 원본 데이터를 모델 학습에 최적화된 형태로 변환하는 과정으로 모델 성능에 결정적 영향을 준다.",
            "SimpleImputer는 결측치를 평균/중앙값/최빈값/상수로 대체하며, 이상치가 있으면 median 전략을 권장한다.",
            "LabelEncoder는 타깃에만, OrdinalEncoder는 순서 있는 범주형 특성에, OneHotEncoder는 순서 없는 범주형 특성에 사용한다.",
            "StandardScaler는 정규 분포를, MinMaxScaler는 신경망 입력에, RobustScaler는 이상치 많은 데이터에 권장된다.",
            "스케일러/인코더는 훈련 데이터로만 fit하고 테스트 데이터에는 transform만 적용해야 데이터 누수를 방지한다.",
            "SelectKBest로 통계적으로 중요한 특성을 선택해 차원의 저주를 피하고 모델을 경량화할 수 있다.",
            "Pipeline과 ColumnTransformer는 전처리·모델을 하나로 묶어 코드 재사용성과 배포 편의성을 높인다.",
        ],
    }
