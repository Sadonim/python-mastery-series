"""
Ch 2: Scikit-learn 기초
Python Mastery Series Vol.5 — ML & MLOps
"""


def get_chapter():
    return {
        "number": 2,
        "title": "Scikit-learn 기초",
        "subtitle": "fit, predict, score — 일관된 API로 ML 마스터하기",
        "big_picture": (
            "scikit-learn은 파이썬 머신러닝의 표준 라이브러리입니다. "
            "100개가 넘는 알고리즘이 있지만 모두 동일한 API(fit, predict, transform)를 따릅니다. "
            "이 챕터에서는 scikit-learn의 철학을 이해하고, "
            "선형 회귀, 로지스틱 회귀, KNN 세 가지 알고리즘을 직접 실습합니다. "
            "또한 train_test_split과 StandardScaler로 데이터 전처리의 기초를 다집니다."
        ),
        "sections": [
            {
                "title": "Scikit-learn API 철학",
                "content": [
                    "scikit-learn의 가장 큰 강점은 '일관성'입니다. "
                    "어떤 알고리즘을 사용하든 동일한 3단계 패턴으로 동작합니다. "
                    "이 패턴을 한 번 익히면 새로운 알고리즘도 빠르게 사용할 수 있습니다.",
                    {
                        "type": "flow_diagram",
                        "title": "Scikit-learn 3단계 API",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "1. fit()", "sub": "데이터로 모델 학습"},
                            {"label": "2. predict()", "sub": "새 데이터 예측"},
                            {"label": "3. score()", "sub": "성능 평가"},
                        ],
                        "note": "전처리기(Scaler, Encoder)는 fit() + transform()을 사용합니다.",
                    },
                    {
                        "type": "heading",
                        "text": "Estimator API 3가지 역할",
                    },
                    {
                        "type": "table",
                        "headers": ["메서드", "역할", "사용 대상", "반환값"],
                        "rows": [
                            [
                                "fit(X, y)",
                                "훈련 데이터로 모델 학습",
                                "모든 Estimator",
                                "self (메서드 체이닝 가능)",
                            ],
                            [
                                "predict(X)",
                                "새 입력에 대한 예측값 생성",
                                "Predictor (모델)",
                                "예측 배열 (y_pred)",
                            ],
                            [
                                "transform(X)",
                                "데이터 변환 (스케일링, 인코딩 등)",
                                "Transformer (전처리기)",
                                "변환된 X",
                            ],
                            [
                                "fit_transform(X)",
                                "학습 + 변환을 한 번에",
                                "Transformer",
                                "변환된 X",
                            ],
                            [
                                "score(X, y)",
                                "모델 성능 점수 반환",
                                "모든 Estimator",
                                "R2 (회귀) 또는 정확도 (분류)",
                            ],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# scikit-learn API 패턴 — 모든 알고리즘에 동일하게 적용\n"
                            "from sklearn.linear_model import LinearRegression\n"
                            "from sklearn.tree import DecisionTreeClassifier\n"
                            "from sklearn.preprocessing import StandardScaler\n"
                            "import numpy as np\n"
                            "\n"
                            "# === 회귀 모델 패턴 ===\n"
                            "X_train = np.array([[1], [2], [3], [4], [5]])\n"
                            "y_train = np.array([2.1, 4.0, 5.9, 8.1, 10.2])\n"
                            "X_test = np.array([[6], [7]])\n"
                            "\n"
                            "model = LinearRegression()   # 1. 모델 인스턴스 생성\n"
                            "model.fit(X_train, y_train)  # 2. 학습 (X와 y 필요)\n"
                            "y_pred = model.predict(X_test)  # 3. 예측\n"
                            "score = model.score(X_test, np.array([12.0, 14.1]))  # 4. 평가\n"
                            "print(f'예측값: {y_pred}')  # [12.08 14.06]\n"
                            "print(f'R2 점수: {score:.4f}')  # 1.0에 가까울수록 좋음\n"
                            "\n"
                            "# === 전처리기 패턴 ===\n"
                            "scaler = StandardScaler()           # 1. 스케일러 생성\n"
                            "X_scaled = scaler.fit_transform(X_train)  # 2. 학습 + 변환 (훈련 데이터만!)\n"
                            "X_test_scaled = scaler.transform(X_test)  # 3. 변환 (테스트는 transform만!)\n"
                            "# 핵심: 테스트 데이터에 fit()을 다시 호출하면 안 됩니다!"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "전처리기(StandardScaler 등)는 항상 훈련 데이터로만 fit()을 호출하세요. "
                            "테스트 데이터에 fit()을 호출하면 테스트 데이터의 통계(평균, 표준편차)가 "
                            "모델에 누수되어 성능이 부풀려집니다. "
                            "테스트 데이터는 항상 transform()만 사용합니다."
                        ),
                    },
                ],
            },
            {
                "title": "데이터셋 로드 — Scikit-learn 내장 데이터",
                "content": [
                    "scikit-learn은 연습용 데이터셋을 내장하고 있습니다. "
                    "실제 데이터를 수집하기 전에 이 데이터셋으로 알고리즘을 빠르게 실험할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# scikit-learn 내장 데이터셋 로드\n"
                            "from sklearn.datasets import (\n"
                            "    load_iris,          # 붓꽃 분류 (3클래스, 150샘플)\n"
                            "    load_breast_cancer, # 유방암 분류 (2클래스, 569샘플)\n"
                            "    load_diabetes,      # 당뇨병 회귀 (442샘플)\n"
                            "    fetch_california_housing,  # 캘리포니아 집값 회귀\n"
                            "    make_classification,  # 분류용 가상 데이터 생성\n"
                            "    make_regression,      # 회귀용 가상 데이터 생성\n"
                            ")\n"
                            "import pandas as pd\n"
                            "\n"
                            "# Iris 데이터셋 로드 및 탐색\n"
                            "iris = load_iris()\n"
                            "\n"
                            "print('=== Iris 데이터셋 정보 ===')\n"
                            "print(f'특성 이름: {iris.feature_names}')\n"
                            "print(f'클래스 이름: {iris.target_names}')\n"
                            "print(f'X 형태: {iris.data.shape}')    # (150, 4)\n"
                            "print(f'y 형태: {iris.target.shape}')  # (150,)\n"
                            "print(f'클래스 분포: {dict(zip(*[iris.target_names, [\n"
                            "    sum(iris.target == i) for i in range(3)]]))}')\n"
                            "\n"
                            "# DataFrame으로 변환하면 탐색이 편리\n"
                            "df = pd.DataFrame(\n"
                            "    iris.data,\n"
                            "    columns=iris.feature_names\n"
                            ")\n"
                            "df['target'] = iris.target\n"
                            "df['species'] = df['target'].map(\n"
                            "    {i: name for i, name in enumerate(iris.target_names)}\n"
                            ")\n"
                            "print('\\n처음 5개 행:')\n"
                            "print(df.head())\n"
                            "print('\\n기본 통계:')\n"
                            "print(df.describe().round(2))"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["데이터셋", "함수", "샘플 수", "특성 수", "문제 유형", "학습 목적"],
                        "rows": [
                            ["Iris 붓꽃", "load_iris()", "150", "4", "3클래스 분류", "기초 분류 입문"],
                            ["Breast Cancer", "load_breast_cancer()", "569", "30", "2클래스 분류", "이진 분류"],
                            ["Diabetes", "load_diabetes()", "442", "10", "회귀", "기초 회귀 입문"],
                            ["California Housing", "fetch_california_housing()", "20640", "8", "회귀", "실제 규모 회귀"],
                            ["make_classification", "make_classification()", "사용자 지정", "사용자 지정", "분류", "통제된 실험"],
                        ],
                    },
                ],
            },
            {
                "title": "선형 회귀 — LinearRegression 실습",
                "content": [
                    "선형 회귀는 가장 단순한 회귀 알고리즘입니다. "
                    "특성과 목표 변수 사이의 선형 관계를 학습합니다. "
                    "'기준선(baseline)' 모델로 항상 먼저 시도해보세요.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 선형 회귀 실습 — 당뇨병 진행 예측\n"
                            "from sklearn.datasets import load_diabetes\n"
                            "from sklearn.linear_model import LinearRegression\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.preprocessing import StandardScaler\n"
                            "from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error\n"
                            "import numpy as np\n"
                            "\n"
                            "# 1. 데이터 로드\n"
                            "diabetes = load_diabetes()\n"
                            "X, y = diabetes.data, diabetes.target\n"
                            "print(f'데이터 형태: X={X.shape}, y={y.shape}')\n"
                            "print(f'목표 변수 범위: {y.min():.0f} ~ {y.max():.0f}')\n"
                            "\n"
                            "# 2. Train/Test Split\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42\n"
                            ")\n"
                            "\n"
                            "# 3. 특성 표준화 (선형 회귀는 스케일에 민감)\n"
                            "scaler = StandardScaler()\n"
                            "X_train_scaled = scaler.fit_transform(X_train)  # 학습 + 변환\n"
                            "X_test_scaled = scaler.transform(X_test)         # 변환만\n"
                            "\n"
                            "# 4. 모델 학습\n"
                            "model = LinearRegression()\n"
                            "model.fit(X_train_scaled, y_train)\n"
                            "\n"
                            "# 5. 예측 및 평가\n"
                            "y_pred = model.predict(X_test_scaled)\n"
                            "\n"
                            "mse = mean_squared_error(y_test, y_pred)\n"
                            "rmse = np.sqrt(mse)\n"
                            "mae = mean_absolute_error(y_test, y_pred)\n"
                            "r2 = r2_score(y_test, y_pred)\n"
                            "\n"
                            "print(f'\\n=== 선형 회귀 평가 결과 ===')\n"
                            "print(f'RMSE: {rmse:.2f}  (낮을수록 좋음)')\n"
                            "print(f'MAE:  {mae:.2f}   (낮을수록 좋음)')\n"
                            "print(f'R2:   {r2:.4f}  (1.0에 가까울수록 좋음)')\n"
                            "\n"
                            "# 6. 모델 파라미터 해석\n"
                            "print(f'\\n절편 (bias): {model.intercept_:.2f}')\n"
                            "print('특성별 계수 (coefficient):')\n"
                            "for name, coef in zip(diabetes.feature_names, model.coef_):\n"
                            "    print(f'  {name:8s}: {coef:+.4f}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "회귀 평가 지표 정리",
                    },
                    {
                        "type": "table",
                        "headers": ["지표", "수식 (설명)", "범위", "해석"],
                        "rows": [
                            [
                                "MSE",
                                "평균 제곱 오차 (오차 제곱의 평균)",
                                "0 이상",
                                "낮을수록 좋음. 큰 오차에 민감",
                            ],
                            [
                                "RMSE",
                                "MSE의 제곱근 (원래 단위로 해석 가능)",
                                "0 이상",
                                "낮을수록 좋음. MSE보다 직관적",
                            ],
                            [
                                "MAE",
                                "평균 절대 오차 (오차 절댓값의 평균)",
                                "0 이상",
                                "낮을수록 좋음. 이상치에 강인",
                            ],
                            [
                                "R2",
                                "결정계수 (모델이 분산을 설명하는 비율)",
                                "0 ~ 1 (음수 가능)",
                                "1.0이 완벽, 0.0은 평균값 예측 수준",
                            ],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "R2 점수가 0.5 이상이면 선형 회귀가 어느 정도 설명력이 있다고 볼 수 있습니다. "
                            "현업에서는 R2 0.7 이상을 목표로 하는 경우가 많지만, "
                            "도메인에 따라 기준이 다릅니다. "
                            "항상 도메인 전문가와 함께 적절한 성능 기준을 정하세요."
                        ),
                    },
                ],
            },
            {
                "title": "로지스틱 회귀 — 분류 실습",
                "content": [
                    "이름에 '회귀'가 붙지만 분류 알고리즘입니다. "
                    "선형 회귀의 출력을 시그모이드 함수로 변환해 0~1 확률로 만들고, "
                    "임계값(보통 0.5)으로 클래스를 결정합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 로지스틱 회귀 실습 — Iris 꽃 분류\n"
                            "from sklearn.datasets import load_iris\n"
                            "from sklearn.linear_model import LogisticRegression\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.preprocessing import StandardScaler\n"
                            "from sklearn.metrics import (\n"
                            "    accuracy_score, classification_report, confusion_matrix\n"
                            ")\n"
                            "\n"
                            "# 1. 데이터 준비\n"
                            "iris = load_iris()\n"
                            "X, y = iris.data, iris.target\n"
                            "\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42, stratify=y\n"
                            "    # stratify=y: 클래스 비율을 유지하며 분할\n"
                            ")\n"
                            "\n"
                            "# 2. 표준화\n"
                            "scaler = StandardScaler()\n"
                            "X_train_scaled = scaler.fit_transform(X_train)\n"
                            "X_test_scaled = scaler.transform(X_test)\n"
                            "\n"
                            "# 3. 로지스틱 회귀 학습\n"
                            "# max_iter: 최대 반복 횟수 (수렴 보장을 위해 충분히 설정)\n"
                            "clf = LogisticRegression(max_iter=200, random_state=42)\n"
                            "clf.fit(X_train_scaled, y_train)\n"
                            "\n"
                            "# 4. 예측\n"
                            "y_pred = clf.predict(X_test_scaled)\n"
                            "\n"
                            "# 확률값도 확인 가능 (각 클래스에 속할 확률)\n"
                            "y_proba = clf.predict_proba(X_test_scaled)\n"
                            "print('첫 번째 샘플 클래스별 확률:')\n"
                            "for cls, prob in zip(iris.target_names, y_proba[0]):\n"
                            "    print(f'  {cls}: {prob:.4f}')\n"
                            "\n"
                            "# 5. 분류 평가\n"
                            "accuracy = accuracy_score(y_test, y_pred)\n"
                            "print(f'\\n정확도 (Accuracy): {accuracy:.4f}')\n"
                            "\n"
                            "# 분류 리포트: Precision, Recall, F1-Score\n"
                            "print('\\n분류 리포트:')\n"
                            "print(classification_report(y_test, y_pred, target_names=iris.target_names))\n"
                            "\n"
                            "# 혼동 행렬 (Confusion Matrix)\n"
                            "print('혼동 행렬:')\n"
                            "print(confusion_matrix(y_test, y_pred))"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "분류 평가 지표 정리",
                    },
                    {
                        "type": "table",
                        "headers": ["지표", "설명", "중요한 상황"],
                        "rows": [
                            [
                                "Accuracy (정확도)",
                                "전체 중 올바르게 분류한 비율",
                                "클래스 불균형이 없을 때",
                            ],
                            [
                                "Precision (정밀도)",
                                "양성으로 예측한 것 중 실제 양성 비율",
                                "False Positive를 줄여야 할 때 (스팸 필터)",
                            ],
                            [
                                "Recall (재현율)",
                                "실제 양성 중 양성으로 예측한 비율",
                                "False Negative를 줄여야 할 때 (암 진단)",
                            ],
                            [
                                "F1-Score",
                                "Precision과 Recall의 조화 평균",
                                "두 지표의 균형이 필요할 때",
                            ],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "불균형 데이터(클래스 비율이 치우친 경우)에서 Accuracy는 속임수가 됩니다. "
                            "예를 들어 양성:음성 = 1:99인 데이터에서 무조건 '음성'으로 예측해도 "
                            "Accuracy 99%가 나옵니다. 이런 경우 F1-Score 또는 AUC-ROC를 사용하세요."
                        ),
                    },
                ],
            },
            {
                "title": "KNN — K-최근접 이웃 분류 실습",
                "content": [
                    "KNN은 '비슷한 것끼리 같은 클래스'라는 직관에 기반한 알고리즘입니다. "
                    "학습 과정이 없고(Lazy Learner), 예측 시 전체 훈련 데이터를 검색합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "새로운 병사가 전입했을 때 '이 병사는 어떤 특기를 맡으면 좋을까?'를 "
                            "판단하는 상황을 생각해보세요. "
                            "가장 비슷한 능력치의 병사 5명(K=5)을 찾아서, "
                            "그 5명 중 가장 많은 특기로 새 병사에게 배정합니다. "
                            "이것이 KNN의 작동 원리입니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# KNN 분류 실습 및 K값 최적화\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "from sklearn.neighbors import KNeighborsClassifier\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.preprocessing import StandardScaler\n"
                            "from sklearn.metrics import accuracy_score\n"
                            "import numpy as np\n"
                            "\n"
                            "# 1. 유방암 데이터셋 (이진 분류: 악성/양성)\n"
                            "cancer = load_breast_cancer()\n"
                            "X, y = cancer.data, cancer.target\n"
                            "print(f'클래스: {cancer.target_names}')  # ['malignant' 'benign']\n"
                            "print(f'클래스 분포: 악성={sum(y==0)}, 양성={sum(y==1)}')\n"
                            "\n"
                            "# 2. 분할 및 표준화 (KNN은 거리 기반 → 스케일 중요!)\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42, stratify=y\n"
                            ")\n"
                            "scaler = StandardScaler()\n"
                            "X_train_scaled = scaler.fit_transform(X_train)\n"
                            "X_test_scaled = scaler.transform(X_test)\n"
                            "\n"
                            "# 3. K값에 따른 성능 변화 확인\n"
                            "print('\\nK값별 테스트 정확도:')\n"
                            "k_scores = {}\n"
                            "for k in [1, 3, 5, 7, 9, 11, 15]:\n"
                            "    knn = KNeighborsClassifier(n_neighbors=k)\n"
                            "    knn.fit(X_train_scaled, y_train)\n"
                            "    acc = accuracy_score(y_test, knn.predict(X_test_scaled))\n"
                            "    k_scores[k] = acc\n"
                            "    print(f'  K={k:2d}: {acc:.4f}')\n"
                            "\n"
                            "# 4. 최적 K값으로 최종 모델\n"
                            "best_k = max(k_scores, key=k_scores.get)\n"
                            "print(f'\\n최적 K값: {best_k} (정확도: {k_scores[best_k]:.4f})')\n"
                            "\n"
                            "best_knn = KNeighborsClassifier(n_neighbors=best_k)\n"
                            "best_knn.fit(X_train_scaled, y_train)\n"
                            "\n"
                            "# 5. 새 샘플 예측\n"
                            "new_sample = X_test_scaled[[0]]  # 첫 번째 테스트 샘플\n"
                            "prediction = best_knn.predict(new_sample)\n"
                            "proba = best_knn.predict_proba(new_sample)\n"
                            "print(f'\\n예측 결과: {cancer.target_names[prediction[0]]}')\n"
                            "print(f'확률: 악성={proba[0][0]:.3f}, 양성={proba[0][1]:.3f}')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["K값", "특징", "편향-분산"],
                        "rows": [
                            ["K=1", "훈련 데이터에 완벽히 맞춤, 노이즈에 민감", "낮은 편향, 높은 분산 (과적합 위험)"],
                            ["K=작은 값", "경계선이 복잡하고 유연", "낮은 편향, 높은 분산"],
                            ["K=적절한 값", "일반화 성능이 좋음", "균형 잡힌 편향-분산"],
                            ["K=큰 값", "경계선이 단순하고 매끄러움", "높은 편향, 낮은 분산 (과소적합 위험)"],
                        ],
                    },
                ],
            },
            {
                "title": "Train/Test Split과 StandardScaler 심화",
                "content": [
                    "지금까지 사용한 두 가지 핵심 도구를 더 깊이 이해합니다.",
                    {
                        "type": "heading",
                        "text": "StandardScaler — 왜 필요한가?",
                    },
                    "거리 기반 알고리즘(KNN, SVM)이나 경사 하강법 기반 알고리즘(선형/로지스틱 회귀)은 "
                    "특성의 스케일에 민감합니다. 표준화는 이를 해결합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# StandardScaler 동작 원리 이해\n"
                            "import numpy as np\n"
                            "from sklearn.preprocessing import StandardScaler, MinMaxScaler\n"
                            "\n"
                            "# 스케일이 다른 특성 예시\n"
                            "X = np.array([\n"
                            "    [175, 70, 22],   # 키(cm), 몸무게(kg), 나이\n"
                            "    [160, 50, 25],\n"
                            "    [185, 90, 30],\n"
                            "    [170, 65, 28],\n"
                            "])\n"
                            "\n"
                            "print('원본 데이터:')\n"
                            "print(X)\n"
                            "print(f'평균: {X.mean(axis=0).round(1)}')\n"
                            "print(f'표준편차: {X.std(axis=0).round(1)}')\n"
                            "\n"
                            "# StandardScaler: 평균=0, 표준편차=1로 변환\n"
                            "# 공식: (x - 평균) / 표준편차\n"
                            "std_scaler = StandardScaler()\n"
                            "X_std = std_scaler.fit_transform(X)\n"
                            "print('\\nStandardScaler 변환 후:')\n"
                            "print(X_std.round(3))\n"
                            "print(f'변환 후 평균 (거의 0): {X_std.mean(axis=0).round(3)}')\n"
                            "print(f'변환 후 표준편차 (거의 1): {X_std.std(axis=0).round(3)}')\n"
                            "\n"
                            "# MinMaxScaler: 0~1 범위로 변환 (이상치에 민감)\n"
                            "minmax_scaler = MinMaxScaler()\n"
                            "X_minmax = minmax_scaler.fit_transform(X)\n"
                            "print('\\nMinMaxScaler 변환 후 (0~1 범위):')\n"
                            "print(X_minmax.round(3))"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "올바른 전처리 순서",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 올바른 전처리 순서 — 핵심 패턴\n"
                            "from sklearn.datasets import load_iris\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.preprocessing import StandardScaler\n"
                            "from sklearn.linear_model import LogisticRegression\n"
                            "\n"
                            "X, y = load_iris(return_X_y=True)  # return_X_y=True 편의 옵션\n"
                            "\n"
                            "# 1단계: 먼저 분할\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42\n"
                            ")\n"
                            "\n"
                            "# 2단계: 훈련 데이터로만 스케일러 학습 (fit)\n"
                            "scaler = StandardScaler()\n"
                            "X_train_scaled = scaler.fit_transform(X_train)  # fit + transform\n"
                            "\n"
                            "# 3단계: 테스트 데이터는 변환만 (fit 없이!)\n"
                            "X_test_scaled = scaler.transform(X_test)  # transform only\n"
                            "\n"
                            "# 4단계: 스케일된 데이터로 모델 학습\n"
                            "clf = LogisticRegression(max_iter=200)\n"
                            "clf.fit(X_train_scaled, y_train)\n"
                            "\n"
                            "# 5단계: 스케일된 테스트 데이터로 평가\n"
                            "print(f'테스트 정확도: {clf.score(X_test_scaled, y_test):.4f}')\n"
                            "\n"
                            "# 주의: 실전에서는 Pipeline으로 자동화 (Ch.7에서 학습)\n"
                            "# from sklearn.pipeline import Pipeline\n"
                            "# pipe = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression())])"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Ch.7에서 배울 Pipeline을 사용하면 스케일러와 모델을 묶어서 "
                            "fit/predict를 한 번에 처리할 수 있습니다. "
                            "전처리 순서 실수를 자동으로 방지해주므로 실전에서는 Pipeline 사용을 권장합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "새로운 ML 프로젝트를 시작할 때 scikit-learn의 알고리즘 선택 가이드 차트를 참고하세요. "
            "sklearn.org에서 'Choosing the right estimator'를 검색하면 문제 유형별 알고리즘 지도가 있습니다.",
            "StandardScaler는 대부분의 알고리즘에 무난하게 사용됩니다. "
            "이상치가 많은 데이터에는 RobustScaler, 0~1 범위가 필요하면 MinMaxScaler를 고려하세요.",
            "KNN은 대용량 데이터에서 매우 느립니다 (예측 시 전체 훈련 데이터 검색). "
            "10만 개 이상의 데이터에서는 RandomForest나 XGBoost를 우선 고려하세요.",
            "classification_report()는 Precision, Recall, F1을 한 번에 보여줍니다. "
            "모든 분류 프로젝트에서 accuracy 하나만 보지 말고 전체 리포트를 확인하세요.",
            "random_state=42는 관례적으로 사용하는 시드 값입니다. "
            "어떤 값이든 고정된 값을 쓰면 되지만, 42는 ML 커뮤니티에서 사실상 표준입니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "StandardScaler를 사용할 때 테스트 데이터에 대해 올바른 처리는?",
                "choices": [
                    "scaler.fit_transform(X_test) — 테스트 데이터로 다시 학습 후 변환",
                    "scaler.fit(X_test) — 테스트 데이터로 스케일러 재학습",
                    "scaler.transform(X_test) — 훈련 데이터로 학습된 스케일러로 변환만",
                    "새로운 StandardScaler()로 테스트 데이터를 따로 처리",
                ],
                "answer": "3번",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "KNN 알고리즘에서 K값이 너무 크면 어떤 문제가 생기나?",
                "choices": [
                    "과적합 (훈련 데이터를 완벽히 외움)",
                    "과소적합 (너무 단순한 경계선)",
                    "데이터 누수 (Data Leakage)",
                    "차원의 저주 (Curse of Dimensionality)",
                ],
                "answer": "2번",
            },
            {
                "number": 3,
                "type": "code",
                "question": (
                    "load_iris() 데이터셋으로 로지스틱 회귀 모델을 만드세요.\n"
                    "train_test_split (test_size=0.3, random_state=0), StandardScaler 적용 후\n"
                    "테스트 정확도를 출력하세요."
                ),
                "hint": (
                    "load_iris → train_test_split → StandardScaler.fit_transform(X_train) "
                    "→ StandardScaler.transform(X_test) → LogisticRegression().fit() → score()"
                ),
                "answer": (
                    "from sklearn.datasets import load_iris\n"
                    "from sklearn.model_selection import train_test_split\n"
                    "from sklearn.preprocessing import StandardScaler\n"
                    "from sklearn.linear_model import LogisticRegression\n"
                    "\n"
                    "X, y = load_iris(return_X_y=True)\n"
                    "X_train, X_test, y_train, y_test = train_test_split(\n"
                    "    X, y, test_size=0.3, random_state=0\n"
                    ")\n"
                    "scaler = StandardScaler()\n"
                    "X_train_s = scaler.fit_transform(X_train)\n"
                    "X_test_s = scaler.transform(X_test)\n"
                    "clf = LogisticRegression(max_iter=200)\n"
                    "clf.fit(X_train_s, y_train)\n"
                    "print(f'정확도: {clf.score(X_test_s, y_test):.4f}')"
                ),
            },
            {
                "number": 4,
                "type": "short_answer",
                "question": (
                    "분류 문제에서 클래스 불균형(예: 양성 5%, 음성 95%)이 있을 때 "
                    "Accuracy 대신 어떤 평가 지표를 사용해야 하며, 그 이유는 무엇인가?"
                ),
                "answer": (
                    "F1-Score (또는 AUC-ROC, Precision/Recall)을 사용합니다. "
                    "불균형 데이터에서 무조건 다수 클래스를 예측해도 Accuracy가 높게 나오므로, "
                    "소수 클래스에 대한 Precision과 Recall을 균형 있게 측정하는 F1-Score가 적합합니다."
                ),
            },
            {
                "number": 5,
                "type": "multiple_choice",
                "question": (
                    "scikit-learn에서 train_test_split의 stratify=y 파라미터를 설정하는 이유는?"
                ),
                "choices": [
                    "훈련 데이터와 테스트 데이터의 크기를 동일하게 맞추기 위해",
                    "훈련/테스트 분할 후에도 각 클래스의 비율이 원본과 동일하게 유지되도록",
                    "특성(Feature)의 분포를 표준화하기 위해",
                    "무작위성을 제거해서 항상 같은 결과를 얻기 위해",
                ],
                "answer": "2번",
            },
        ],
        "challenge": {
            "question": (
                "세 가지 분류기(LogisticRegression, KNeighborsClassifier, 결정 트리)를 "
                "동일한 데이터셋으로 비교하는 벤치마크 스크립트를 작성하세요.\n\n"
                "요구사항:\n"
                "① load_breast_cancer() 데이터셋 사용 (이진 분류)\n"
                "② train_test_split (test_size=0.2, random_state=42, stratify=y)\n"
                "③ StandardScaler로 표준화\n"
                "④ 세 모델을 각각 학습하고 Accuracy, F1-Score를 출력\n"
                "⑤ 결과를 표로 정리해서 출력 (모델명 | Accuracy | F1-Score)\n"
                "⑥ 어떤 모델이 이 데이터셋에 가장 적합한지 한 줄로 코멘트 추가"
            ),
            "hint": (
                "from sklearn.tree import DecisionTreeClassifier,\n"
                "from sklearn.metrics import accuracy_score, f1_score 를 import 합니다.\n"
                "세 모델을 리스트에 담아 for 루프로 학습/평가하면 깔끔합니다: \n"
                "models = [('LR', LogisticRegression()), ('KNN', KNeighborsClassifier()), ('DT', DecisionTreeClassifier())]\n"
                "f1_score에는 average='binary'를 지정하세요."
            ),
        },
        "summary": [
            "scikit-learn의 모든 알고리즘은 fit(학습) → predict(예측) → score(평가) 3단계 API를 따릅니다.",
            "전처리기(StandardScaler)는 훈련 데이터로만 fit()하고, 테스트 데이터는 transform()만 적용합니다.",
            "LinearRegression은 연속값 예측(회귀), LogisticRegression은 카테고리 분류에 사용합니다.",
            "KNN은 K값이 작으면 과적합, 크면 과소적합이 발생하며 거리 기반이므로 표준화가 필수입니다.",
            "분류 평가는 Accuracy 하나만 보지 말고 classification_report()로 Precision/Recall/F1을 함께 확인하세요.",
            "Ch.7의 Pipeline으로 표준화 + 모델 학습을 묶으면 데이터 누수를 자동으로 방지할 수 있습니다.",
        ],
    }
