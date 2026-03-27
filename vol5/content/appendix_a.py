"""
부록 A: Scikit-learn 치트시트
알고리즘 선택 가이드, 전처리 도구, 평가 지표, 하이퍼파라미터, Pipeline 패턴을 한눈에 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 A: Scikit-learn 치트시트",
        "sections": [
            _section_algorithm_guide(),
            _section_preprocessing(),
            _section_metrics(),
            _section_hyperparams(),
            _section_pipeline_patterns(),
        ],
    }


def _section_algorithm_guide() -> dict:
    return {
        "title": "A.1 알고리즘 선택 가이드",
        "content": [
            (
                "어떤 알고리즘을 선택할지는 데이터의 크기, 유형, 목적에 따라 달라집니다. "
                "아래 표는 상황별 추천 알고리즘과 scikit-learn 클래스를 정리한 것입니다. "
                "'먼저 단순한 모델부터 시도하고, 성능 부족 시 복잡한 모델로 전환한다'는 원칙을 따르세요."
            ),
            {
                "type": "heading",
                "text": "분류 (Classification)",
            },
            {
                "type": "table",
                "headers": ["상황", "추천 알고리즘", "scikit-learn 클래스", "특징"],
                "rows": [
                    ["빠른 베이스라인", "로지스틱 회귀", "LogisticRegression", "선형, 해석 용이, 빠름"],
                    ["피처 중요도 필요", "랜덤 포레스트", "RandomForestClassifier", "앙상블, 과적합 강건"],
                    ["고성능 & 대용량", "그래디언트 부스팅", "GradientBoostingClassifier", "느린 학습, 높은 정확도"],
                    ["텍스트/희소 데이터", "나이브 베이즈", "MultinomialNB", "확률 기반, 매우 빠름"],
                    ["비선형 경계", "SVM", "SVC(kernel='rbf')", "소규모 고차원에 적합"],
                    ["이웃 기반", "K-최근접 이웃", "KNeighborsClassifier", "직관적, 대용량에 느림"],
                ],
            },
            {
                "type": "heading",
                "text": "회귀 (Regression)",
            },
            {
                "type": "table",
                "headers": ["상황", "추천 알고리즘", "scikit-learn 클래스", "특징"],
                "rows": [
                    ["기본 회귀", "선형 회귀", "LinearRegression", "단순, 다중공선성 주의"],
                    ["규제 필요 (L2)", "릿지 회귀", "Ridge", "가중치 축소, 안정적"],
                    ["피처 선택 필요", "라쏘 회귀", "Lasso", "희소 해 생성, 자동 피처 선택"],
                    ["비선형 패턴", "랜덤 포레스트 회귀", "RandomForestRegressor", "앙상블, 이상치 강건"],
                    ["고성능", "그래디언트 부스팅 회귀", "GradientBoostingRegressor", "XGBoost와 유사한 성능"],
                ],
            },
            {
                "type": "heading",
                "text": "군집화 (Clustering)",
            },
            {
                "type": "table",
                "headers": ["상황", "추천 알고리즘", "scikit-learn 클래스", "특징"],
                "rows": [
                    ["군집 수 알 때", "K-Means", "KMeans", "빠름, 구형 군집 가정"],
                    ["군집 수 모를 때", "DBSCAN", "DBSCAN", "노이즈 처리, 비구형 가능"],
                    ["계층적 분석", "계층적 군집화", "AgglomerativeClustering", "덴드로그램 시각화"],
                ],
            },
            {
                "type": "flow_diagram",
                "title": "알고리즘 선택 결정 흐름",
                "direction": "vertical",
                "nodes": [
                    {"label": "레이블 있음?", "sub": "지도/비지도 선택"},
                    {"label": "예/지도학습", "sub": "목표: 분류 또는 회귀"},
                    {"label": "아니오/비지도", "sub": "목표: 군집 또는 차원 축소"},
                    {"label": "샘플 수 확인", "sub": "1만 미만: SVM/KNN 가능"},
                    {"label": "베이스라인 먼저", "sub": "LogReg / LinearReg"},
                    {"label": "성능 부족 시", "sub": "앙상블 모델로 업그레이드"},
                ],
                "note": "항상 단순한 모델부터 시작하세요. 복잡한 모델은 해석력이 낮고 과적합 위험이 높습니다.",
            },
        ],
    }


def _section_preprocessing() -> dict:
    return {
        "title": "A.2 전처리 도구 비교",
        "content": [
            "올바른 전처리는 모델 성능에 직결됩니다. 아래 표로 상황에 맞는 도구를 선택하세요.",
            {
                "type": "heading",
                "text": "스케일러 (Scaler)",
            },
            {
                "type": "table",
                "headers": ["클래스", "변환 방식", "적합한 상황", "주의사항"],
                "rows": [
                    ["StandardScaler", "평균 0, 표준편차 1로 변환", "정규분포에 가까운 데이터, SVM/선형 모델", "이상치에 민감"],
                    ["MinMaxScaler", "[0, 1] 범위로 변환", "이미지 픽셀, 신경망 입력", "이상치가 범위를 왜곡"],
                    ["RobustScaler", "중앙값과 IQR 기반 변환", "이상치 많은 데이터", "정규분포 가정 없음"],
                    ["Normalizer", "각 샘플을 단위 벡터로 정규화", "텍스트, 코사인 유사도", "피처가 아닌 샘플 단위"],
                ],
            },
            {
                "type": "heading",
                "text": "인코더 (Encoder)",
            },
            {
                "type": "table",
                "headers": ["클래스", "변환 방식", "적합한 상황", "주의사항"],
                "rows": [
                    ["LabelEncoder", "문자열 -> 정수 (0, 1, 2...)", "타겟 레이블", "순서 없는 피처에는 부적합"],
                    ["OrdinalEncoder", "범주형 -> 정수 (순서 있음)", "저/중/고 같은 순서형 변수", "순서 의미 없으면 부적합"],
                    ["OneHotEncoder", "범주형 -> 이진 벡터", "순서 없는 명목형 변수", "카디널리티 높으면 차원 폭발"],
                    ["TargetEncoder", "범주별 타겟 평균으로 인코딩", "고카디널리티 범주형", "타겟 누출 주의, CV 필요"],
                ],
            },
            {
                "type": "heading",
                "text": "결측값 처리 (Imputer)",
            },
            {
                "type": "table",
                "headers": ["클래스", "대체 전략", "적합한 상황"],
                "rows": [
                    ["SimpleImputer(strategy='mean')", "평균값으로 대체", "연속형 변수, 결측이 무작위"],
                    ["SimpleImputer(strategy='median')", "중앙값으로 대체", "이상치 있는 연속형 변수"],
                    ["SimpleImputer(strategy='most_frequent')", "최빈값으로 대체", "범주형 변수"],
                    ["KNNImputer", "K개 이웃의 평균으로 대체", "결측 패턴이 복잡할 때"],
                    ["IterativeImputer", "다른 피처로 결측값 예측", "결측이 다른 피처와 연관"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 수치형 + 범주형 피처를 각각 전처리하는 ColumnTransformer 예시\n"
                    "from sklearn.compose import ColumnTransformer\n"
                    "from sklearn.pipeline import Pipeline\n"
                    "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n"
                    "from sklearn.impute import SimpleImputer\n"
                    "\n"
                    "numeric_features = ['age', 'income', 'score']\n"
                    "categorical_features = ['gender', 'region']\n"
                    "\n"
                    "# 수치형 파이프라인: 결측값 처리 -> 표준화\n"
                    "numeric_pipeline = Pipeline([\n"
                    "    ('imputer', SimpleImputer(strategy='median')),\n"
                    "    ('scaler', StandardScaler()),\n"
                    "])\n"
                    "\n"
                    "# 범주형 파이프라인: 결측값 처리 -> 원-핫 인코딩\n"
                    "categorical_pipeline = Pipeline([\n"
                    "    ('imputer', SimpleImputer(strategy='most_frequent')),\n"
                    "    ('encoder', OneHotEncoder(handle_unknown='ignore')),\n"
                    "])\n"
                    "\n"
                    "# 전처리기 조합\n"
                    "preprocessor = ColumnTransformer([\n"
                    "    ('num', numeric_pipeline, numeric_features),\n"
                    "    ('cat', categorical_pipeline, categorical_features),\n"
                    "])\n"
                ),
            },
        ],
    }


def _section_metrics() -> dict:
    return {
        "title": "A.3 평가 지표 요약",
        "content": [
            "목적에 맞는 평가 지표를 선택해야 모델의 실제 성능을 올바르게 측정할 수 있습니다.",
            {
                "type": "heading",
                "text": "분류 지표",
            },
            {
                "type": "table",
                "headers": ["지표", "계산 방식", "언제 사용", "sklearn 함수"],
                "rows": [
                    ["Accuracy", "정답 / 전체", "클래스 균형일 때", "accuracy_score"],
                    ["Precision", "TP / (TP + FP)", "FP를 줄이고 싶을 때 (스팸 필터)", "precision_score"],
                    ["Recall", "TP / (TP + FN)", "FN을 줄이고 싶을 때 (암 진단)", "recall_score"],
                    ["F1-Score", "Precision과 Recall의 조화 평균", "불균형 데이터, 균형 중요", "f1_score"],
                    ["ROC-AUC", "ROC 곡선 아래 면적", "이진 분류, 임계값 무관", "roc_auc_score"],
                    ["Confusion Matrix", "실제/예측 클래스별 분포 행렬", "오분류 패턴 분석", "confusion_matrix"],
                ],
            },
            {
                "type": "heading",
                "text": "회귀 지표",
            },
            {
                "type": "table",
                "headers": ["지표", "계산 방식", "특징", "sklearn 함수"],
                "rows": [
                    ["MAE", "오차 절댓값의 평균", "이상치에 강건, 직관적", "mean_absolute_error"],
                    ["MSE", "오차 제곱의 평균", "큰 오차에 페널티, 미분 가능", "mean_squared_error"],
                    ["RMSE", "MSE의 제곱근", "원래 단위와 동일, 해석 용이", "mean_squared_error(squared=False)"],
                    ["R2-Score", "1 - (잔차 제곱합 / 전체 분산)", "1에 가까울수록 좋음, 음수 가능", "r2_score"],
                    ["MAPE", "절대 백분율 오차의 평균", "비율로 해석, 0값 주의", "mean_absolute_percentage_error"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "클래스 불균형 데이터(예: 사기 탐지)에서는 Accuracy보다 "
                    "F1-Score 또는 ROC-AUC를 사용하세요. "
                    "99% 음성 데이터에서 무조건 '음성' 예측만 해도 Accuracy 99%가 나오지만, "
                    "이 모델은 사기 탐지에 전혀 쓸모가 없습니다."
                ),
            },
        ],
    }


def _section_hyperparams() -> dict:
    return {
        "title": "A.4 주요 하이퍼파라미터",
        "content": [
            "각 모델의 핵심 하이퍼파라미터와 권장 탐색 범위입니다. GridSearchCV 또는 RandomizedSearchCV와 함께 사용하세요.",
            {
                "type": "table",
                "headers": ["모델", "주요 파라미터", "기본값", "탐색 범위 예시"],
                "rows": [
                    ["RandomForestClassifier", "n_estimators", "100", "[50, 100, 200, 300]"],
                    ["RandomForestClassifier", "max_depth", "None", "[3, 5, 10, None]"],
                    ["RandomForestClassifier", "min_samples_split", "2", "[2, 5, 10]"],
                    ["GradientBoostingClassifier", "n_estimators", "100", "[100, 200, 500]"],
                    ["GradientBoostingClassifier", "learning_rate", "0.1", "[0.01, 0.05, 0.1, 0.2]"],
                    ["GradientBoostingClassifier", "max_depth", "3", "[3, 5, 7]"],
                    ["SVC", "C", "1.0", "[0.1, 1, 10, 100]"],
                    ["SVC", "kernel", "'rbf'", "['linear', 'rbf', 'poly']"],
                    ["SVC", "gamma", "'scale'", "['scale', 'auto', 0.1, 0.01]"],
                    ["LogisticRegression", "C", "1.0", "[0.01, 0.1, 1, 10]"],
                    ["LogisticRegression", "solver", "'lbfgs'", "['lbfgs', 'saga']"],
                    ["KNeighborsClassifier", "n_neighbors", "5", "[3, 5, 7, 11, 15]"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# GridSearchCV로 최적 하이퍼파라미터 탐색\n"
                    "from sklearn.model_selection import GridSearchCV, RandomizedSearchCV\n"
                    "from sklearn.ensemble import RandomForestClassifier\n"
                    "\n"
                    "param_grid = {\n"
                    "    'n_estimators': [100, 200],\n"
                    "    'max_depth': [None, 5, 10],\n"
                    "    'min_samples_split': [2, 5],\n"
                    "}\n"
                    "\n"
                    "# GridSearchCV: 모든 조합 탐색 (느림, 정확)\n"
                    "grid_search = GridSearchCV(\n"
                    "    RandomForestClassifier(random_state=42),\n"
                    "    param_grid,\n"
                    "    cv=5,               # 5-Fold 교차검증\n"
                    "    scoring='f1_weighted',\n"
                    "    n_jobs=-1,          # 모든 CPU 코어 사용\n"
                    "    verbose=1,\n"
                    ")\n"
                    "grid_search.fit(X_train, y_train)\n"
                    "print(f'최적 파라미터: {grid_search.best_params_}')\n"
                    "print(f'최적 F1: {grid_search.best_score_:.4f}')\n"
                    "\n"
                    "# RandomizedSearchCV: 랜덤 샘플링 (빠름, 대규모 탐색)\n"
                    "from scipy.stats import randint\n"
                    "param_dist = {\n"
                    "    'n_estimators': randint(50, 500),\n"
                    "    'max_depth': [None, 3, 5, 10, 20],\n"
                    "}\n"
                    "random_search = RandomizedSearchCV(\n"
                    "    RandomForestClassifier(random_state=42),\n"
                    "    param_dist,\n"
                    "    n_iter=20,          # 20개 조합만 탐색\n"
                    "    cv=5,\n"
                    "    scoring='f1_weighted',\n"
                    "    random_state=42,\n"
                    ")\n"
                ),
            },
        ],
    }


def _section_pipeline_patterns() -> dict:
    return {
        "title": "A.5 Pipeline 구성 패턴",
        "content": [
            (
                "사이킷런 Pipeline은 전처리와 모델을 하나로 묶어 "
                "데이터 누출(leakage)을 방지하고 재현성을 보장합니다. "
                "Pipeline 내부에서 fit()은 학습 데이터에만 적용되고, "
                "transform()은 학습/테스트 데이터 모두에 일관되게 적용됩니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 패턴 1: 기본 Pipeline (전처리 + 모델)\n"
                    "from sklearn.pipeline import Pipeline\n"
                    "from sklearn.preprocessing import StandardScaler\n"
                    "from sklearn.svm import SVC\n"
                    "\n"
                    "pipe = Pipeline([\n"
                    "    ('scaler', StandardScaler()),\n"
                    "    ('classifier', SVC()),\n"
                    "])\n"
                    "pipe.fit(X_train, y_train)\n"
                    "score = pipe.score(X_test, y_test)\n"
                    "\n"
                    "# 패턴 2: Pipeline + GridSearchCV (하이퍼파라미터 탐색)\n"
                    "param_grid = {\n"
                    "    'classifier__C': [0.1, 1, 10],       # 'step이름__파라미터' 형식\n"
                    "    'classifier__kernel': ['linear', 'rbf'],\n"
                    "}\n"
                    "grid = GridSearchCV(pipe, param_grid, cv=5)\n"
                    "grid.fit(X_train, y_train)\n"
                    "\n"
                    "# 패턴 3: Pipeline + cross_val_score\n"
                    "from sklearn.model_selection import cross_val_score\n"
                    "scores = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')\n"
                    "print(f'CV Accuracy: {scores.mean():.4f} +/- {scores.std():.4f}')\n"
                    "\n"
                    "# 패턴 4: Pipeline 저장 & 로드\n"
                    "import joblib\n"
                    "joblib.dump(pipe, 'model_pipeline.pkl')   # 저장\n"
                    "loaded_pipe = joblib.load('model_pipeline.pkl')  # 로드\n"
                    "predictions = loaded_pipe.predict(X_new)\n"
                ),
            },
            {
                "type": "warning",
                "text": (
                    "StandardScaler를 Pipeline 밖에서 fit하면 데이터 누출이 발생합니다. "
                    "scaler.fit(X_train) 후 X_test에도 transform을 적용하면 "
                    "테스트 데이터의 통계(평균, 표준편차)가 학습에 간접적으로 영향을 줍니다. "
                    "항상 Pipeline 안에 넣어 교차검증 시 fold마다 독립적으로 fit되게 하세요."
                ),
            },
            {
                "type": "tip",
                "text": (
                    "set_output(transform='pandas') API(scikit-learn 1.2+)를 사용하면 "
                    "Pipeline 중간 단계 출력이 DataFrame으로 반환되어 "
                    "피처 이름을 유지한 채 디버깅할 수 있습니다."
                ),
            },
        ],
    }
