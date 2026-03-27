"""챕터 3: Scikit-learn 심화 — 트리·앙상블·SVM·비지도학습."""


def get_chapter():
    """챕터 3 콘텐츠를 반환한다."""
    return {
        "number": 3,
        "title": "Scikit-learn 심화",
        "subtitle": "트리·앙상블·SVM과 비지도학습 마스터하기",
        "big_picture": (
            "Vol.5 Ch.2에서 선형 모델과 scikit-learn의 기본 API를 익혔습니다. "
            "이제 한 단계 올라가 더 강력한 알고리즘들을 배울 차례입니다. "
            "결정 트리는 '스무고개'처럼 데이터를 분류하고, "
            "랜덤 포레스트는 수백 개의 트리가 투표해 더 정확한 답을 냅니다. "
            "SVM은 데이터를 가장 넓게 나누는 경계를 찾으며, "
            "K-Means와 PCA는 레이블 없이 데이터의 패턴을 발견합니다. "
            "이 알고리즘들을 언제, 왜 쓰는지 이해하면 "
            "실무에서 올바른 도구를 선택할 수 있습니다."
        ),
        "sections": [
            # ── 섹션 1: 결정 트리 ─────────────────────────────────
            {
                "title": "결정 트리 — 스무고개로 분류하기",
                "content": [
                    "결정 트리(Decision Tree)는 스무고개 게임처럼 동작합니다. "
                    "각 노드에서 특성 하나를 기준으로 데이터를 두 그룹으로 나누고, "
                    "이를 반복해 최종 분류에 도달합니다. "
                    "직관적이고 시각화가 쉬워 비전문가에게 결과를 설명할 때 특히 유용합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "결정 트리는 군 의무실에서 환자를 분류하는 과정과 같습니다. "
                            "'체온이 38도 이상인가?' → 예: '기침이 있는가?' → 예: 독감 의심. "
                            "각 질문이 하나의 노드이고, 마지막 답이 리프 노드(분류 결과)입니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "분할 기준 — 불순도를 줄이는 방향으로",
                    },
                    "결정 트리는 '불순도'를 최소화하는 방향으로 분할 기준을 선택합니다. "
                    "분류 문제에서는 지니 불순도(Gini Impurity)와 정보 이득(Information Gain)이 주로 사용됩니다.",
                    {
                        "type": "table",
                        "headers": ["기준", "파라미터 값", "특징", "권장 상황"],
                        "rows": [
                            ["지니 불순도", "criterion='gini'", "계산 빠름 (기본값)", "대부분의 분류 문제"],
                            ["정보 이득", "criterion='entropy'", "정보 이론 기반, 약간 느림", "균형 잡힌 트리 선호 시"],
                            ["분산 감소", "criterion='squared_error'", "회귀 트리에 사용", "연속값 예측 문제"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.tree import DecisionTreeClassifier, export_text\n"
                            "from sklearn.datasets import load_iris\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.metrics import accuracy_score\n\n\n"
                            "# 붓꽃 데이터셋 로드 (150개 샘플, 4개 특성, 3개 클래스)\n"
                            "iris = load_iris()\n"
                            "X, y = iris.data, iris.target\n\n"
                            "# 훈련/테스트 분할 (80:20)\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42, stratify=y\n"
                            ")\n\n"
                            "# ── 깊이 제한 없는 트리 (과적합 위험) ───────────────\n"
                            "dt_full = DecisionTreeClassifier(random_state=42)\n"
                            "dt_full.fit(X_train, y_train)\n"
                            "print(f'깊이 제한 없음 - 깊이: {dt_full.get_depth()}')\n"
                            "print(f'훈련 정확도: {dt_full.score(X_train, y_train):.4f}')  # 1.0000 (과적합)\n"
                            "print(f'테스트 정확도: {dt_full.score(X_test, y_test):.4f}')\n\n"
                            "# ── 깊이 제한으로 일반화 성능 향상 ─────────────────\n"
                            "dt_limited = DecisionTreeClassifier(\n"
                            "    max_depth=3,          # 최대 깊이 3으로 제한\n"
                            "    min_samples_split=5,  # 분할 최소 샘플 수\n"
                            "    min_samples_leaf=2,   # 리프 노드 최소 샘플 수\n"
                            "    criterion='gini',     # 분할 기준 (기본값)\n"
                            "    random_state=42,\n"
                            ")\n"
                            "dt_limited.fit(X_train, y_train)\n"
                            "print(f'\\n깊이 3 제한 - 깊이: {dt_limited.get_depth()}')\n"
                            "print(f'훈련 정확도: {dt_limited.score(X_train, y_train):.4f}')\n"
                            "print(f'테스트 정확도: {dt_limited.score(X_test, y_test):.4f}')\n\n"
                            "# 트리 구조를 텍스트로 출력\n"
                            "tree_rules = export_text(dt_limited, feature_names=iris.feature_names)\n"
                            "print('\\n트리 구조:')\n"
                            "print(tree_rules)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "max_depth는 결정 트리의 가장 중요한 하이퍼파라미터입니다. "
                            "너무 깊으면 과적합(훈련 정확도 높고 테스트 낮음), "
                            "너무 얕으면 과소적합(둘 다 낮음)이 발생합니다. "
                            "보통 3~10 사이에서 교차 검증으로 최적값을 찾습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 랜덤 포레스트 ───────────────────────────────
            {
                "title": "랜덤 포레스트 — 앙상블로 더 강하게",
                "content": [
                    "랜덤 포레스트(Random Forest)는 수백 개의 결정 트리를 만들고 "
                    "각 트리의 예측을 다수결(분류) 또는 평균(회귀)으로 합쳐 최종 예측을 냅니다. "
                    "단일 트리보다 훨씬 강건하고 과적합에 강합니다.",
                    {
                        "type": "flow_diagram",
                        "title": "앙상블 학습 — 여러 모델의 집단 지성",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "훈련 데이터", "sub": "원본 데이터셋"},
                            {"label": "부트스트랩 샘플링", "sub": "중복 허용 재추출 x N"},
                            {"label": "트리 1~N 학습", "sub": "각각 랜덤 특성 사용"},
                            {"label": "예측 결과 수집", "sub": "N개 트리의 예측"},
                            {"label": "투표/평균", "sub": "다수결 또는 평균"},
                            {"label": "최종 예측", "sub": "앙상블 결과"},
                        ],
                        "note": (
                            "각 트리는 서로 다른 데이터 샘플과 특성 부분집합을 사용해 "
                            "'다양성'을 확보합니다. 다양한 트리들의 오류가 서로 상쇄됩니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "import numpy as np\n\n\n"
                            "# 유방암 분류 데이터셋 (569 샘플, 30 특성, 2 클래스)\n"
                            "cancer = load_breast_cancer()\n"
                            "X, y = cancer.data, cancer.target\n\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42, stratify=y\n"
                            ")\n\n"
                            "# ── 랜덤 포레스트 학습 ───────────────────────────────\n"
                            "rf = RandomForestClassifier(\n"
                            "    n_estimators=200,      # 트리 개수 (많을수록 안정적, 느림)\n"
                            "    max_depth=10,          # 개별 트리 최대 깊이\n"
                            "    max_features='sqrt',   # 분할 시 고려할 특성 수 (sqrt(30) ≈ 5)\n"
                            "    min_samples_leaf=2,    # 리프 노드 최소 샘플\n"
                            "    n_jobs=-1,             # 모든 CPU 코어 사용\n"
                            "    random_state=42,\n"
                            ")\n"
                            "rf.fit(X_train, y_train)\n\n"
                            "print(f'훈련 정확도: {rf.score(X_train, y_train):.4f}')\n"
                            "print(f'테스트 정확도: {rf.score(X_test, y_test):.4f}')\n\n"
                            "# ── 특성 중요도 확인 ─────────────────────────────────\n"
                            "# 어떤 특성이 예측에 가장 큰 영향을 미치는가?\n"
                            "importances = rf.feature_importances_\n"
                            "indices = np.argsort(importances)[::-1]  # 중요도 내림차순 정렬\n\n"
                            "print('\\n상위 5개 중요 특성:')\n"
                            "for rank, idx in enumerate(indices[:5], start=1):\n"
                            "    feature_name = cancer.feature_names[idx]\n"
                            "    importance = importances[idx]\n"
                            "    print(f'  {rank}. {feature_name}: {importance:.4f}')\n\n"
                            "# 출력 예시:\n"
                            "#   1. worst perimeter: 0.1432\n"
                            "#   2. worst concave points: 0.1318\n"
                            "#   3. mean concave points: 0.1102"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["파라미터", "기본값", "설명", "튜닝 방향"],
                        "rows": [
                            ["n_estimators", "100", "트리 개수", "많을수록 좋음 (100~500), 느려짐"],
                            ["max_depth", "None", "트리 최대 깊이", "과적합 방지 위해 제한 (5~20)"],
                            ["max_features", "'sqrt'", "분할 시 고려 특성 수", "분류: sqrt, 회귀: 1.0"],
                            ["min_samples_leaf", "1", "리프 노드 최소 샘플", "2~10으로 늘리면 과적합 감소"],
                            ["n_jobs", "1", "병렬 처리 CPU 수", "-1로 모든 코어 사용"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "특성 중요도(feature_importances_)는 MLOps에서 매우 중요합니다. "
                            "모델이 어떤 특성에 의존하는지 알면 "
                            "불필요한 특성을 제거해 모델을 경량화하고, "
                            "데이터 드리프트(특성 분포 변화) 모니터링 포인트를 정할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: SVM ────────────────────────────────────────
            {
                "title": "SVM — 최적의 경계선 찾기",
                "content": [
                    "서포트 벡터 머신(SVM, Support Vector Machine)은 "
                    "두 클래스를 가장 넓게 구분하는 결정 경계(초평면)를 찾습니다. "
                    "경계에서 가장 가까운 데이터 포인트들이 '서포트 벡터'이며, "
                    "이 간격(마진)을 최대화하는 것이 SVM의 핵심 목표입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "두 군부대 사이에 비무장지대(DMZ)를 설정한다고 생각해보세요. "
                            "SVM은 두 부대 사이의 DMZ 폭을 최대로 넓히는 경계선을 찾습니다. "
                            "경계에 가장 가까운 군인들(서포트 벡터)이 DMZ 폭을 결정합니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "커널 트릭 — 비선형 문제를 선형으로",
                    },
                    "현실 데이터는 직선으로 구분되지 않는 경우가 많습니다. "
                    "커널 함수는 데이터를 더 높은 차원으로 투영해 선형 분리 가능하게 만듭니다. "
                    "실제로는 고차원 변환 없이 수학적 트릭으로 효율적으로 계산합니다.",
                    {
                        "type": "table",
                        "headers": ["커널", "kernel 파라미터", "수식 특징", "적합한 데이터"],
                        "rows": [
                            ["선형", "kernel='linear'", "내적 (점곱)", "선형 분리 가능, 고차원 희소 데이터"],
                            ["RBF (가우시안)", "kernel='rbf'", "가우시안 함수 (기본값)", "비선형, 중간 규모 데이터"],
                            ["다항식", "kernel='poly'", "다항식 함수", "특성 간 상호작용 중요 시"],
                            ["시그모이드", "kernel='sigmoid'", "tanh 함수", "신경망 모방 (잘 안 씀)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.svm import SVC\n"
                            "from sklearn.datasets import make_classification\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.preprocessing import StandardScaler\n\n\n"
                            "# 비선형 분류 데이터 생성\n"
                            "X, y = make_classification(\n"
                            "    n_samples=1000,\n"
                            "    n_features=20,\n"
                            "    n_informative=10,\n"
                            "    random_state=42,\n"
                            ")\n\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42\n"
                            ")\n\n"
                            "# !! SVM은 스케일에 민감 → 반드시 정규화 필요 !!\n"
                            "scaler = StandardScaler()\n"
                            "X_train_scaled = scaler.fit_transform(X_train)\n"
                            "X_test_scaled = scaler.transform(X_test)  # fit 없이 transform만!\n\n"
                            "# ── RBF 커널 SVM ─────────────────────────────────────\n"
                            "svm_rbf = SVC(\n"
                            "    kernel='rbf',   # 기본 커널 (비선형)\n"
                            "    C=1.0,          # 규제 강도 (작을수록 마진 넓고 오분류 허용)\n"
                            "    gamma='scale',  # RBF 커널 폭 ('scale'=1/(n_features*X.var()))\n"
                            "    probability=True,  # predict_proba 사용 가능 (느려짐)\n"
                            "    random_state=42,\n"
                            ")\n"
                            "svm_rbf.fit(X_train_scaled, y_train)\n\n"
                            "print(f'RBF SVM 테스트 정확도: {svm_rbf.score(X_test_scaled, y_test):.4f}')\n"
                            "print(f'서포트 벡터 수: {svm_rbf.n_support_}')  # 클래스별 서포트 벡터 수\n\n"
                            "# ── 선형 커널 SVM (대용량 데이터에는 LinearSVC가 더 빠름) ──\n"
                            "svm_linear = SVC(kernel='linear', C=0.1)\n"
                            "svm_linear.fit(X_train_scaled, y_train)\n"
                            "print(f'선형 SVM 테스트 정확도: {svm_linear.score(X_test_scaled, y_test):.4f}')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "SVM은 반드시 특성 스케일링 후 사용하세요. "
                            "스케일링 없이 사용하면 큰 값을 가진 특성이 결정 경계를 지배합니다. "
                            "또한 샘플 수가 10만 개 이상이면 학습 속도가 매우 느려집니다. "
                            "대용량 데이터에는 SGDClassifier(loss='hinge')를 대신 사용하세요."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["하이퍼파라미터", "역할", "작은 값 효과", "큰 값 효과"],
                        "rows": [
                            ["C", "규제 강도 역수", "넓은 마진, 오분류 허용 (과소적합 위험)", "좁은 마진, 오분류 감소 (과적합 위험)"],
                            ["gamma (RBF)", "커널 폭", "부드러운 경계 (underfitting)", "복잡한 경계 (overfitting)"],
                        ],
                    },
                ],
            },
            # ── 섹션 4: K-Means 클러스터링 ─────────────────────────
            {
                "title": "K-Means 클러스터링 — 레이블 없이 그룹 찾기",
                "content": [
                    "지금까지는 모두 '지도학습'이었습니다. 레이블(정답)이 있는 데이터로 모델을 훈련했죠. "
                    "비지도학습은 레이블 없이 데이터 자체의 패턴을 찾습니다. "
                    "K-Means는 데이터를 K개의 클러스터로 나누는 가장 기본적인 군집화 알고리즘입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "신병들을 체력 수준에 따라 A/B/C 분대로 나눈다고 생각해보세요. "
                            "정답이 없는 상태에서 비슷한 사람끼리 묶는 것, 이게 클러스터링입니다. "
                            "K-Means는 각 분대의 '대표 위치(중심점)'를 찾아가는 과정을 반복합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.cluster import KMeans\n"
                            "from sklearn.datasets import make_blobs\n"
                            "from sklearn.metrics import silhouette_score\n"
                            "import numpy as np\n\n\n"
                            "# 클러스터링 테스트용 데이터 생성 (실제로는 레이블 y를 사용하지 않음)\n"
                            "X, y_true = make_blobs(\n"
                            "    n_samples=500, centers=4, cluster_std=0.8, random_state=42\n"
                            ")\n\n"
                            "# ── K-Means 클러스터링 ──────────────────────────────\n"
                            "kmeans = KMeans(\n"
                            "    n_clusters=4,    # 클러스터 개수 (사전에 지정 필요)\n"
                            "    n_init=10,       # 초기 중심점 시도 횟수 (최선 선택)\n"
                            "    max_iter=300,    # 최대 반복 횟수\n"
                            "    random_state=42,\n"
                            ")\n"
                            "kmeans.fit(X)\n\n"
                            "# 각 샘플의 클러스터 번호\n"
                            "labels = kmeans.labels_  # shape: (500,)\n"
                            "print(f'클러스터 분포: {np.bincount(labels)}')\n"
                            "# 클러스터 중심점\n"
                            "centers = kmeans.cluster_centers_  # shape: (4, 2)\n"
                            "print(f'이너셔(inertia): {kmeans.inertia_:.2f}')  # 낮을수록 조밀\n\n"
                            "# ── 최적 K 찾기: 실루엣 점수 ─────────────────────────\n"
                            "# 실루엣 점수: -1~1, 1에 가까울수록 클러스터가 잘 분리됨\n"
                            "scores = []\n"
                            "k_range = range(2, 8)\n"
                            "for k in k_range:\n"
                            "    km = KMeans(n_clusters=k, n_init=10, random_state=42)\n"
                            "    labels_k = km.fit_predict(X)\n"
                            "    score = silhouette_score(X, labels_k)\n"
                            "    scores.append(score)\n"
                            "    print(f'K={k}: 실루엣={score:.4f}')\n\n"
                            "best_k = k_range[np.argmax(scores)]\n"
                            "print(f'\\n최적 K: {best_k}')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "K-Means는 클러스터 수 K를 미리 지정해야 합니다. "
                            "엘보우 방법(inertia 꺾이는 지점)이나 "
                            "실루엣 분석으로 최적 K를 탐색하세요. "
                            "또한 이상치에 민감하므로 전처리 단계에서 이상치를 제거하거나 "
                            "DBSCAN 같은 밀도 기반 알고리즘을 검토하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: PCA 차원 축소 ───────────────────────────────
            {
                "title": "PCA — 핵심만 남기고 압축하기",
                "content": [
                    "주성분 분석(PCA, Principal Component Analysis)은 "
                    "고차원 데이터를 정보 손실을 최소화하면서 저차원으로 압축합니다. "
                    "데이터의 분산이 가장 큰 방향을 '주성분'으로 선택합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "30개 특성을 가진 군인 데이터를 2D 그래프로 그리려면 어떻게 할까요? "
                            "PCA는 30차원 데이터를 가장 중요한 2개 방향으로 '그림자를 투영'합니다. "
                            "원본 정보의 90%를 담은 채로 2D로 볼 수 있게 되는 것이죠."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.decomposition import PCA\n"
                            "from sklearn.preprocessing import StandardScaler\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "import numpy as np\n\n\n"
                            "# 유방암 데이터 (30개 특성)\n"
                            "cancer = load_breast_cancer()\n"
                            "X = cancer.data\n\n"
                            "# !! PCA 전에 반드시 스케일링 !!\n"
                            "scaler = StandardScaler()\n"
                            "X_scaled = scaler.fit_transform(X)\n\n"
                            "# ── 주성분 개수를 분산 비율로 결정 ───────────────────\n"
                            "pca_full = PCA()  # 모든 주성분 계산\n"
                            "pca_full.fit(X_scaled)\n\n"
                            "# 각 주성분이 설명하는 분산 비율\n"
                            "explained = pca_full.explained_variance_ratio_\n"
                            "cumulative = np.cumsum(explained)\n\n"
                            "print('주성분별 누적 설명 분산 비율:')\n"
                            "for i, (exp, cum) in enumerate(zip(explained[:10], cumulative[:10]), 1):\n"
                            "    print(f'  PC{i:2d}: {exp:.4f} (누적: {cum:.4f})')\n\n"
                            "# 95% 분산을 유지하는 주성분 수 찾기\n"
                            "n_components_95 = np.argmax(cumulative >= 0.95) + 1\n"
                            "print(f'\\n95% 분산 유지에 필요한 주성분 수: {n_components_95} / {X.shape[1]}')\n\n"
                            "# ── 10개 주성분으로 차원 축소 ─────────────────────────\n"
                            "pca = PCA(n_components=10)\n"
                            "X_reduced = pca.fit_transform(X_scaled)\n\n"
                            "print(f'\\n원본 형태: {X_scaled.shape}')  # (569, 30)\n"
                            "print(f'축소 형태: {X_reduced.shape}')    # (569, 10)\n"
                            "print(f'설명된 분산: {pca.explained_variance_ratio_.sum():.4f}')\n\n"
                            "# ── PCA 후 분류 모델 학습 ────────────────────────────\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.linear_model import LogisticRegression\n\n"
                            "X_train_r, X_test_r, y_train, y_test = train_test_split(\n"
                            "    X_reduced, cancer.target, test_size=0.2, random_state=42\n"
                            ")\n"
                            "lr = LogisticRegression(max_iter=1000)\n"
                            "lr.fit(X_train_r, y_train)\n"
                            "print(f'PCA 후 로지스틱 회귀 정확도: {lr.score(X_test_r, y_test):.4f}')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "PCA의 주요 사용 목적은 3가지입니다. "
                            "1) 시각화: 고차원 데이터를 2~3D로 축소해 눈으로 확인. "
                            "2) 노이즈 제거: 분산이 작은 주성분(노이즈일 가능성 높음)을 제거. "
                            "3) 계산 속도 향상: 특성 수를 줄여 모델 학습 시간 단축. "
                            "해석 가능성이 중요하면 원본 특성 선택법(SelectKBest 등)을 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 알고리즘 선택 가이드 ────────────────────────
            {
                "title": "알고리즘 선택 가이드 — 언제 무엇을?",
                "content": [
                    "scikit-learn에는 수십 가지 알고리즘이 있습니다. "
                    "데이터의 특성과 문제 유형에 따라 시작점을 정하면 "
                    "불필요한 시행착오를 줄일 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["상황", "추천 알고리즘", "이유"],
                        "rows": [
                            ["소규모 데이터 (1천 이하), 분류", "SVC (RBF)", "정확도 높음, 결정 경계 유연"],
                            ["중소규모 데이터, 분류/회귀", "RandomForest", "기본 성능 좋음, 특성 중요도 제공"],
                            ["해석이 중요한 분류", "DecisionTree (max_depth 제한)", "시각화·설명 용이"],
                            ["대규모 데이터, 선형 관계", "LogisticRegression / LinearSVC", "빠름, 해석 가능"],
                            ["비지도: 그룹 나누기", "KMeans (K 사전 지정 가능할 때)", "빠름, 직관적"],
                            ["비지도: 이상 탐지 / 모양 불규칙", "DBSCAN", "K 불필요, 노이즈 처리"],
                            ["차원 축소 (시각화)", "PCA", "선형 변환, 빠름"],
                            ["차원 축소 (비선형 구조 보존)", "t-SNE / UMAP", "시각화 전용 (느림)"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "실무 팁: 항상 LogisticRegression이나 RandomForest부터 시작하세요. "
                            "이 두 알고리즘은 대부분의 문제에서 합리적인 기준선(baseline)을 제공합니다. "
                            "그 이후 데이터 크기, 정확도 요구사항, 해석 필요성에 따라 알고리즘을 변경합니다."
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
                        "MLOps 파이프라인에서 알고리즘 선택은 '최고 정확도'보다 "
                        "'비즈니스 요구사항에 맞는 적절한 정확도'가 중요합니다. "
                        "RandomForest는 튜닝 없이도 좋은 성능을 보여 빠른 프로토타이핑에 이상적입니다."
                    ),
                },
                {
                    "type": "tip",
                    "text": (
                        "특성 중요도를 항상 기록하세요. "
                        "모델이 어떤 특성에 의존하는지 알면 "
                        "운영 환경에서 데이터 파이프라인 문제를 빠르게 진단할 수 있습니다. "
                        "예: '특성 X의 중요도가 갑자기 급락 → 데이터 수집 오류 가능성'."
                    ),
                },
                {
                    "type": "warning",
                    "text": (
                        "SVM을 대용량 데이터(10만 샘플 이상)에 사용하면 "
                        "학습 시간이 O(n^2~n^3)으로 기하급수적으로 증가합니다. "
                        "이 경우 LinearSVC나 SGDClassifier를 사용하세요."
                    ),
                },
            ],
        },
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "결정 트리에서 max_depth를 제한하는 주된 이유는 무엇인가?",
                "choices": [
                    "A) 학습 속도를 높이기 위해",
                    "B) 과적합(Overfitting)을 방지하고 일반화 성능을 높이기 위해",
                    "C) 특성 중요도를 더 정확히 계산하기 위해",
                    "D) 트리 시각화를 편리하게 하기 위해",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "랜덤 포레스트가 단일 결정 트리보다 일반적으로 성능이 좋은 핵심 이유는?",
                "choices": [
                    "A) 더 깊은 트리를 사용하기 때문",
                    "B) 모든 특성을 동시에 고려하기 때문",
                    "C) 다양한 트리들의 예측을 앙상블해 개별 오류를 상쇄하기 때문",
                    "D) 스케일링이 필요 없기 때문",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "SVM에서 하이퍼파라미터 C의 역할을 설명하고, "
                    "C를 너무 크게 설정하면 어떤 문제가 발생할 수 있는지 서술하시오."
                ),
                "answer": (
                    "C는 규제 강도의 역수로, 마진 폭과 오분류 허용 수준을 조절합니다. "
                    "C가 너무 크면 마진이 좁아지고 훈련 데이터의 오분류를 최소화하려 해 "
                    "과적합(Overfitting)이 발생합니다. "
                    "훈련 정확도는 높지만 테스트 정확도가 낮아집니다."
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "load_wine() 데이터셋으로 RandomForestClassifier를 학습하고 "
                    "상위 3개 중요 특성을 출력하는 코드를 작성하시오. "
                    "(train_test_split 80:20, n_estimators=100, random_state=42)"
                ),
                "hint": (
                    "rf.feature_importances_로 중요도 배열을 얻고, "
                    "np.argsort(importances)[::-1][:3]으로 상위 3개 인덱스를 구합니다. "
                    "wine.feature_names로 특성 이름을 확인하세요."
                ),
                "answer": (
                    "from sklearn.datasets import load_wine\n"
                    "from sklearn.ensemble import RandomForestClassifier\n"
                    "from sklearn.model_selection import train_test_split\n"
                    "import numpy as np\n\n"
                    "wine = load_wine()\n"
                    "X_train, X_test, y_train, y_test = train_test_split(\n"
                    "    wine.data, wine.target, test_size=0.2, random_state=42\n"
                    ")\n"
                    "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n"
                    "rf.fit(X_train, y_train)\n\n"
                    "importances = rf.feature_importances_\n"
                    "top3 = np.argsort(importances)[::-1][:3]\n"
                    "for rank, idx in enumerate(top3, 1):\n"
                    "    print(f'{rank}. {wine.feature_names[idx]}: {importances[idx]:.4f}')"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "make_blobs(n_samples=300, centers=3, random_state=42)으로 데이터를 생성하고 "
                    "K=3으로 KMeans 클러스터링을 수행한 뒤, "
                    "각 클러스터의 샘플 수와 실루엣 점수를 출력하는 코드를 작성하시오."
                ),
                "hint": (
                    "kmeans.labels_로 클러스터 번호 배열을 얻고, "
                    "np.bincount(labels)로 클러스터별 샘플 수를 구합니다. "
                    "silhouette_score(X, labels)로 실루엣 점수를 계산합니다."
                ),
                "answer": (
                    "from sklearn.cluster import KMeans\n"
                    "from sklearn.datasets import make_blobs\n"
                    "from sklearn.metrics import silhouette_score\n"
                    "import numpy as np\n\n"
                    "X, _ = make_blobs(n_samples=300, centers=3, random_state=42)\n"
                    "kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)\n"
                    "labels = kmeans.fit_predict(X)\n\n"
                    "print('클러스터별 샘플 수:', np.bincount(labels))\n"
                    "score = silhouette_score(X, labels)\n"
                    "print(f'실루엣 점수: {score:.4f}')"
                ),
            },
        ],
        "challenge": {
            "question": (
                "군 훈련병 데이터를 분석하는 분류 시스템을 구축하세요. "
                "1) make_classification(n_samples=1000, n_features=15, n_informative=8, "
                "n_classes=3, random_state=42)으로 데이터 생성 "
                "2) DecisionTree, RandomForest, SVM(RBF) 세 모델을 학습 (train 70%, test 30%) "
                "3) 세 모델의 테스트 정확도를 비교 출력 "
                "4) RandomForest의 상위 5개 특성 중요도를 출력 "
                "5) PCA(n_components=5)로 차원 축소 후 RandomForest 정확도가 어떻게 변하는지 비교 "
                "힌트: SVM에는 StandardScaler 적용 필수. "
                "각 단계별 결과를 가독성 있게 출력하세요."
            ),
            "hint": (
                "파이프라인처럼 단계별로 작성하세요. "
                "SVM용 스케일러는 X_train에 fit_transform, X_test에는 transform만. "
                "PCA도 마찬가지로 훈련 데이터로만 fit 후 테스트 데이터에 transform. "
                "세 모델의 결과를 딕셔너리에 모아 한 번에 출력하면 깔끔합니다."
            ),
        },
        "summary": [
            "결정 트리는 분할 기준(지니/엔트로피)으로 데이터를 재귀적으로 나누며, max_depth 제한이 과적합 방지의 핵심이다.",
            "랜덤 포레스트는 부트스트랩 샘플링 + 랜덤 특성 선택으로 다양한 트리를 만들고 앙상블해 단일 트리보다 강건하다.",
            "feature_importances_는 MLOps에서 특성 모니터링과 경량화에 활용되는 중요한 정보다.",
            "SVM은 마진을 최대화하는 결정 경계를 찾으며, 커널 트릭으로 비선형 문제를 처리한다. 반드시 스케일링 후 사용.",
            "K-Means는 비지도학습으로 K개 클러스터로 데이터를 군집화하며, 실루엣 점수로 최적 K를 탐색한다.",
            "PCA는 분산을 최대한 보존하며 고차원 데이터를 저차원으로 압축한다. 스케일링 후 적용해야 한다.",
            "알고리즘 선택은 데이터 규모·문제 유형·해석 필요성에 따라 결정하며, RandomForest가 좋은 출발점이다.",
        ],
    }
