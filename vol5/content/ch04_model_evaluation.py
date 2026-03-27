"""챕터 4: 모델 평가 & 튜닝 — 좋은 모델을 올바르게 측정하기."""


def get_chapter():
    """챕터 4 콘텐츠를 반환한다."""
    return {
        "number": 4,
        "title": "모델 평가 & 튜닝",
        "subtitle": "좋은 모델을 올바르게 측정하고 개선하기",
        "big_picture": (
            "모델을 만들었다면 이제 '얼마나 잘 동작하는가'를 측정해야 합니다. "
            "단순히 정확도(Accuracy) 하나만 보면 오해할 수 있습니다. "
            "의료 진단처럼 거짓 음성(False Negative)이 치명적인 경우, "
            "정확도 98%인 모델이 실제로는 쓸모없을 수 있습니다. "
            "이 챕터에서는 상황에 맞는 평가 지표를 선택하는 법, "
            "교차 검증으로 모델의 진짜 성능을 측정하는 법, "
            "그리고 GridSearchCV로 최적 하이퍼파라미터를 자동으로 찾는 법을 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: 분류 평가 지표 ──────────────────────────────
            {
                "title": "분류 평가 지표 — 정확도만으로는 부족하다",
                "content": [
                    "분류 모델의 성능을 제대로 이해하려면 혼동 행렬(Confusion Matrix)부터 시작해야 합니다. "
                    "혼동 행렬은 모델의 예측이 실제와 어떻게 일치하거나 어긋나는지를 4가지 경우로 나눠 보여줍니다.",
                    {
                        "type": "table",
                        "headers": ["구분", "예측: Positive", "예측: Negative"],
                        "rows": [
                            ["실제: Positive", "TP (True Positive, 올바른 양성)", "FN (False Negative, 놓친 양성)"],
                            ["실제: Negative", "FP (False Positive, 잘못된 양성)", "TN (True Negative, 올바른 음성)"],
                        ],
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "군 의무실에서 독감 양성/음성을 판단한다고 생각해보세요. "
                            "TP: 독감인 사람을 양성 판정 (정확히 잡음). "
                            "FN: 독감인 사람을 음성 판정 (놓침 — 위험!). "
                            "FP: 독감 아닌 사람을 양성 판정 (과잉 격리). "
                            "TN: 독감 아닌 사람을 음성 판정 (정확히 통과)."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.datasets import load_breast_cancer\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.metrics import (\n"
                            "    accuracy_score, precision_score, recall_score,\n"
                            "    f1_score, confusion_matrix, classification_report,\n"
                            ")\n\n\n"
                            "cancer = load_breast_cancer()\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    cancer.data, cancer.target,\n"
                            "    test_size=0.2, random_state=42, stratify=cancer.target\n"
                            ")\n\n"
                            "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n"
                            "rf.fit(X_train, y_train)\n"
                            "y_pred = rf.predict(X_test)\n\n"
                            "# ── 주요 분류 지표 ────────────────────────────────────\n"
                            "print(f'정확도(Accuracy):  {accuracy_score(y_test, y_pred):.4f}')\n"
                            "print(f'정밀도(Precision): {precision_score(y_test, y_pred):.4f}')\n"
                            "print(f'재현율(Recall):    {recall_score(y_test, y_pred):.4f}')\n"
                            "print(f'F1-Score:         {f1_score(y_test, y_pred):.4f}')\n\n"
                            "# ── 혼동 행렬 ────────────────────────────────────────\n"
                            "cm = confusion_matrix(y_test, y_pred)\n"
                            "print(f'\\n혼동 행렬:\\n{cm}')\n\n"
                            "# ── 클래스별 상세 리포트 ──────────────────────────────\n"
                            "print('\\n분류 리포트:')\n"
                            "print(classification_report(\n"
                            "    y_test, y_pred,\n"
                            "    target_names=cancer.target_names,\n"
                            "))"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["지표", "수식", "의미", "언제 중요한가"],
                        "rows": [
                            ["Accuracy", "(TP+TN) / 전체", "전체 정답 비율", "클래스 균형일 때"],
                            ["Precision", "TP / (TP+FP)", "양성 예측 중 실제 양성 비율", "FP를 줄여야 할 때 (스팸 필터)"],
                            ["Recall", "TP / (TP+FN)", "실제 양성 중 탐지 비율", "FN을 줄여야 할 때 (질병 진단)"],
                            ["F1-Score", "2*(P*R)/(P+R)", "Precision과 Recall의 조화 평균", "불균형 데이터, 둘 다 중요할 때"],
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            "클래스 불균형 데이터(예: 정상 99%, 이상 1%)에서 "
                            "정확도만 보면 항상 '정상'이라고 예측하는 모델이 99% 정확도를 가집니다. "
                            "이런 상황에서는 반드시 Precision, Recall, F1을 함께 확인하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 회귀 평가 지표 ──────────────────────────────
            {
                "title": "회귀 평가 지표 — 예측 오차를 숫자로",
                "content": [
                    "회귀 문제는 연속적인 숫자를 예측합니다. "
                    "분류처럼 맞고 틀리는 개념이 없으므로 "
                    "예측값과 실제값의 차이(오차)를 측정합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.datasets import fetch_california_housing\n"
                            "from sklearn.ensemble import RandomForestRegressor\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.metrics import (\n"
                            "    mean_squared_error, mean_absolute_error, r2_score\n"
                            ")\n"
                            "import numpy as np\n\n\n"
                            "housing = fetch_california_housing()\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    housing.data, housing.target,\n"
                            "    test_size=0.2, random_state=42\n"
                            ")\n\n"
                            "rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)\n"
                            "rf_reg.fit(X_train, y_train)\n"
                            "y_pred = rf_reg.predict(X_test)\n\n"
                            "# ── 회귀 지표 계산 ────────────────────────────────────\n"
                            "mse  = mean_squared_error(y_test, y_pred)\n"
                            "rmse = np.sqrt(mse)  # sklearn 1.4+: mean_squared_error(..., squared=False)\n"
                            "mae  = mean_absolute_error(y_test, y_pred)\n"
                            "r2   = r2_score(y_test, y_pred)\n\n"
                            "print(f'MSE  (평균 제곱 오차):    {mse:.4f}')\n"
                            "print(f'RMSE (평균 제곱근 오차):  {rmse:.4f}')\n"
                            "print(f'MAE  (평균 절대 오차):    {mae:.4f}')\n"
                            "print(f'R²   (결정 계수):         {r2:.4f}')\n"
                            "# R² = 1이면 완벽한 예측, 0이면 평균 예측과 동일, 음수면 최악"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["지표", "수식", "단위", "특징"],
                        "rows": [
                            ["MSE", "평균((예측-실제)²)", "원본 단위²", "큰 오차에 민감 (이상치 영향 큼)"],
                            ["RMSE", "MSE의 제곱근", "원본 단위", "해석 쉬움, 이상치 민감"],
                            ["MAE", "평균(|예측-실제|)", "원본 단위", "이상치에 강건, 해석 직관적"],
                            ["R²", "1 - SS_res/SS_tot", "없음 (0~1)", "설명력 비율, 1에 가까울수록 좋음"],
                        ],
                    },
                ],
            },
            # ── 섹션 3: 교차 검증 ─────────────────────────────────
            {
                "title": "교차 검증 — 모델의 진짜 성능 측정",
                "content": [
                    "훈련/테스트를 한 번만 분할하면 분할 방식에 따라 결과가 크게 달라질 수 있습니다. "
                    "교차 검증(Cross-Validation)은 데이터를 여러 번 다르게 분할해 "
                    "모델의 평균 성능과 안정성을 측정합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "시험을 한 번만 보면 운이 좋거나 나쁠 수 있습니다. "
                            "5회 시험을 보고 평균을 내면 진짜 실력을 알 수 있습니다. "
                            "K-Fold 교차 검증도 마찬가지로 K번 다른 조합으로 훈련/검증을 반복합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.model_selection import (\n"
                            "    cross_val_score, KFold, StratifiedKFold\n"
                            ")\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "import numpy as np\n\n\n"
                            "cancer = load_breast_cancer()\n"
                            "X, y = cancer.data, cancer.target\n\n"
                            "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n\n"
                            "# ── 가장 간단한 교차 검증 ────────────────────────────\n"
                            "# cv=5: 5-Fold, scoring: 평가 지표\n"
                            "scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')\n"
                            "print(f'5-Fold CV 정확도: {scores}')\n"
                            "print(f'평균: {scores.mean():.4f} ± {scores.std():.4f}')\n\n"
                            "# ── StratifiedKFold: 클래스 비율 유지 (분류 문제 권장) ──\n"
                            "skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n"
                            "scores_strat = cross_val_score(\n"
                            "    rf, X, y, cv=skf, scoring='f1'\n"
                            ")\n"
                            "print(f'\\nStratified 5-Fold F1: {scores_strat}')\n"
                            "print(f'평균 F1: {scores_strat.mean():.4f} ± {scores_strat.std():.4f}')\n\n"
                            "# ── KFold: 클래스 비율 무관 (회귀 문제에 사용) ──────────\n"
                            "kf = KFold(n_splits=5, shuffle=True, random_state=42)\n"
                            "scores_kf = cross_val_score(rf, X, y, cv=kf, scoring='accuracy')\n"
                            "print(f'\\nKFold 정확도 평균: {scores_kf.mean():.4f}')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["방법", "클래스 비율 유지", "권장 상황"],
                        "rows": [
                            ["KFold", "아니오", "회귀 문제, 균형 데이터"],
                            ["StratifiedKFold", "예", "분류 문제 (특히 불균형 데이터)"],
                            ["cross_val_score(cv=N)", "분류 시 자동 Stratified", "빠른 평가 시 편리"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "교차 검증 점수의 표준편차(std)도 중요합니다. "
                            "평균이 높아도 std가 크면 모델이 불안정하다는 신호입니다. "
                            "MLOps에서는 평균 성능뿐 아니라 일관성(낮은 분산)도 중요합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 하이퍼파라미터 튜닝 ─────────────────────────
            {
                "title": "하이퍼파라미터 튜닝 — GridSearchCV와 RandomizedSearchCV",
                "content": [
                    "하이퍼파라미터(max_depth, n_estimators, C 등)는 학습 전에 사람이 설정하는 값입니다. "
                    "최적값을 찾기 위해 여러 조합을 체계적으로 시도해봐야 합니다.",
                    {
                        "type": "flow_diagram",
                        "title": "모델 선택 파이프라인",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "원본 데이터", "sub": "raw features"},
                            {"label": "전처리", "sub": "스케일링·인코딩"},
                            {"label": "학습", "sub": "모델 피팅"},
                            {"label": "교차 검증", "sub": "K-Fold 평가"},
                            {"label": "하이퍼파라미터 튜닝", "sub": "Grid/Random Search"},
                            {"label": "최종 모델", "sub": "테스트셋 평가"},
                        ],
                        "note": (
                            "튜닝 단계에서 테스트셋은 절대 사용하지 않습니다. "
                            "최종 평가 시 딱 한 번만 사용해야 공정한 평가가 됩니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.model_selection import GridSearchCV, RandomizedSearchCV\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "import numpy as np\n\n\n"
                            "cancer = load_breast_cancer()\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    cancer.data, cancer.target, test_size=0.2, random_state=42\n"
                            ")\n\n"
                            "# ── GridSearchCV: 모든 조합 탐색 ────────────────────\n"
                            "param_grid = {\n"
                            "    'n_estimators': [50, 100, 200],\n"
                            "    'max_depth': [3, 5, 10, None],\n"
                            "    'min_samples_leaf': [1, 2, 4],\n"
                            "}  # 총 3 x 4 x 3 = 36가지 조합 x 5-Fold = 180번 학습\n\n"
                            "grid_search = GridSearchCV(\n"
                            "    RandomForestClassifier(random_state=42),\n"
                            "    param_grid,\n"
                            "    cv=5,\n"
                            "    scoring='f1',\n"
                            "    n_jobs=-1,     # 병렬 처리\n"
                            "    verbose=1,     # 진행 상황 출력\n"
                            ")\n"
                            "grid_search.fit(X_train, y_train)\n\n"
                            "print(f'최적 파라미터: {grid_search.best_params_}')\n"
                            "print(f'최고 CV F1:   {grid_search.best_score_:.4f}')\n"
                            "best_model = grid_search.best_estimator_\n"
                            "print(f'테스트 정확도: {best_model.score(X_test, y_test):.4f}')"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── RandomizedSearchCV: 랜덤 샘플링 (대규모 탐색 공간에 유리) ──\n"
                            "from scipy.stats import randint, uniform\n\n"
                            "param_dist = {\n"
                            "    'n_estimators': randint(50, 500),       # 50~499 정수 무작위\n"
                            "    'max_depth': randint(3, 20),            # 3~19 정수 무작위\n"
                            "    'min_samples_leaf': randint(1, 10),     # 1~9 정수 무작위\n"
                            "    'max_features': uniform(0.3, 0.7),      # 0.3~1.0 실수 무작위\n"
                            "}\n\n"
                            "random_search = RandomizedSearchCV(\n"
                            "    RandomForestClassifier(random_state=42),\n"
                            "    param_dist,\n"
                            "    n_iter=50,     # 50가지 조합만 시도 (GridSearch보다 훨씬 빠름)\n"
                            "    cv=5,\n"
                            "    scoring='f1',\n"
                            "    n_jobs=-1,\n"
                            "    random_state=42,\n"
                            ")\n"
                            "random_search.fit(X_train, y_train)\n\n"
                            "print(f'최적 파라미터: {random_search.best_params_}')\n"
                            "print(f'최고 CV F1:   {random_search.best_score_:.4f}')\n"
                            "print(f'테스트 정확도: {random_search.best_estimator_.score(X_test, y_test):.4f}')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["방법", "탐색 방식", "장점", "단점", "권장 상황"],
                        "rows": [
                            ["GridSearchCV", "모든 조합 전수 탐색", "최적값 보장", "느림, 조합 폭발", "파라미터 수 적을 때 (3개 이하)"],
                            ["RandomizedSearchCV", "n_iter개 무작위 탐색", "빠름, 넓은 공간 탐색", "최적값 미보장", "파라미터 수 많을 때 (4개 이상)"],
                        ],
                    },
                ],
            },
            # ── 섹션 5: 학습 곡선과 검증 곡선 ──────────────────────
            {
                "title": "학습 곡선과 검증 곡선 — 과적합/과소적합 진단",
                "content": [
                    "모델이 잘 학습되고 있는지 시각적으로 진단하는 두 가지 도구입니다. "
                    "학습 곡선은 데이터 크기에 따른 성능 변화를, "
                    "검증 곡선은 하이퍼파라미터 값에 따른 성능 변화를 보여줍니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.model_selection import learning_curve, validation_curve\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "import numpy as np\n\n\n"
                            "cancer = load_breast_cancer()\n"
                            "X, y = cancer.data, cancer.target\n"
                            "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n\n"
                            "# ── 학습 곡선 ─────────────────────────────────────────\n"
                            "train_sizes, train_scores, val_scores = learning_curve(\n"
                            "    rf, X, y,\n"
                            "    train_sizes=np.linspace(0.1, 1.0, 10),  # 10~100% 데이터\n"
                            "    cv=5,\n"
                            "    scoring='accuracy',\n"
                            "    n_jobs=-1,\n"
                            ")\n\n"
                            "# 각 데이터 크기별 평균 ± 표준편차\n"
                            "train_mean = train_scores.mean(axis=1)\n"
                            "val_mean   = val_scores.mean(axis=1)\n\n"
                            "print('학습 곡선 (데이터 크기별 성능):')\n"
                            "for size, tr, va in zip(train_sizes, train_mean, val_mean):\n"
                            "    print(f'  데이터 {size:4d}개 — 훈련: {tr:.4f}, 검증: {va:.4f}')\n\n"
                            "# ── 검증 곡선 ─────────────────────────────────────────\n"
                            "param_range = [1, 3, 5, 10, 20, None]  # max_depth 범위\n"
                            "train_vc, val_vc = validation_curve(\n"
                            "    RandomForestClassifier(n_estimators=100, random_state=42),\n"
                            "    X, y,\n"
                            "    param_name='max_depth',\n"
                            "    param_range=param_range,\n"
                            "    cv=5,\n"
                            "    scoring='accuracy',\n"
                            ")\n\n"
                            "print('\\n검증 곡선 (max_depth별 성능):')\n"
                            "for depth, tr, va in zip(\n"
                            "    param_range, train_vc.mean(axis=1), val_vc.mean(axis=1)\n"
                            "):\n"
                            "    print(f'  max_depth={str(depth):4s} — 훈련: {tr:.4f}, 검증: {va:.4f}')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["증상", "훈련 점수", "검증 점수", "진단", "처방"],
                        "rows": [
                            ["과소적합", "낮음", "낮음", "모델이 너무 단순", "복잡도 높임 (depth 증가, 특성 추가)"],
                            ["과적합", "높음", "낮음", "모델이 너무 복잡", "규제 강화, 데이터 추가, 단순화"],
                            ["적절한 학습", "높음", "높음", "일반화 성공", "유지 또는 미세 튜닝"],
                        ],
                    },
                ],
            },
            # ── 섹션 6: ROC 곡선과 AUC ──────────────────────────────
            {
                "title": "ROC 곡선과 AUC — 임계값에 독립적인 평가",
                "content": [
                    "분류 모델은 내부적으로 확률을 계산한 뒤 임계값(보통 0.5)으로 클래스를 결정합니다. "
                    "ROC 곡선은 임계값을 바꾸면서 True Positive Rate(재현율)와 "
                    "False Positive Rate의 균형을 시각화합니다. "
                    "AUC(Area Under Curve)는 이 곡선 아래 면적으로 "
                    "임계값에 무관한 단일 성능 지표를 제공합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from sklearn.metrics import roc_curve, roc_auc_score\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.datasets import load_breast_cancer\n"
                            "from sklearn.model_selection import train_test_split\n\n\n"
                            "cancer = load_breast_cancer()\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    cancer.data, cancer.target, test_size=0.2, random_state=42\n"
                            ")\n\n"
                            "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n"
                            "rf.fit(X_train, y_train)\n\n"
                            "# 확률 예측 (0.5 임계값 이전의 원시 확률)\n"
                            "y_proba = rf.predict_proba(X_test)[:, 1]  # Positive 클래스 확률\n\n"
                            "# ── ROC 커브 데이터 계산 ─────────────────────────────\n"
                            "fpr, tpr, thresholds = roc_curve(y_test, y_proba)\n"
                            "auc = roc_auc_score(y_test, y_proba)\n\n"
                            "print(f'AUC: {auc:.4f}')\n"
                            "print(f'  AUC = 1.0 → 완벽한 분류기')\n"
                            "print(f'  AUC = 0.5 → 무작위 추측과 동일')\n"
                            "print(f'  AUC = 0.0 → 완전히 반대로 예측')\n\n"
                            "# 여러 임계값에서의 성능 샘플 출력\n"
                            "print('\\n임계값별 FPR / TPR (샘플):')\n"
                            "step = max(1, len(thresholds) // 5)\n"
                            "for thresh, fp, tp in zip(\n"
                            "    thresholds[::step], fpr[::step], tpr[::step]\n"
                            "):\n"
                            "    print(f'  임계값={thresh:.2f}: FPR={fp:.4f}, TPR={tp:.4f}')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["AUC 범위", "해석", "실무 의미"],
                        "rows": [
                            ["0.9 ~ 1.0", "매우 우수", "운영 환경에 배포 고려"],
                            ["0.8 ~ 0.9", "우수", "대부분의 실무 요구사항 충족"],
                            ["0.7 ~ 0.8", "보통", "추가 개선(특성 공학, 튜닝) 필요"],
                            ["0.5 ~ 0.7", "미흡", "모델 구조나 특성 재검토 필요"],
                            ["0.5 이하", "최악", "레이블이 반전됐을 가능성 확인"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "MLOps에서 AUC는 모델 배포 결정 지표로 자주 사용됩니다. "
                            "임계값은 배포 후 비즈니스 요구에 맞게 조정할 수 있습니다. "
                            "예: 의료 시스템에서는 FN(놓친 양성)을 줄이기 위해 "
                            "임계값을 0.5보다 낮게(0.3~0.4) 설정하는 경우가 많습니다."
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
                        "MLOps 모델 배포 결정 체크리스트: "
                        "1) 교차 검증 평균 성능이 기준선(baseline)을 넘는가? "
                        "2) 훈련/검증 점수 차이가 합리적인가 (과적합 없음)? "
                        "3) AUC가 0.8 이상인가? "
                        "4) 비즈니스에서 중요한 클래스의 Recall이 충분한가?"
                    ),
                },
                {
                    "type": "tip",
                    "text": (
                        "GridSearchCV의 best_estimator_는 전체 훈련 데이터로 재학습된 모델입니다. "
                        "이 모델을 바로 테스트셋 평가와 운영 배포에 사용하세요. "
                        "best_score_는 교차 검증 점수이므로 테스트셋 결과와 다를 수 있습니다."
                    ),
                },
                {
                    "type": "warning",
                    "text": (
                        "데이터 누수(Data Leakage) 주의: "
                        "전처리(스케일링, 인코딩)를 교차 검증 루프 밖에서 수행하면 "
                        "테스트 데이터 정보가 훈련에 흘러들어 성능이 낙관적으로 측정됩니다. "
                        "반드시 Pipeline을 사용해 전처리와 모델을 묶으세요 (Ch.5 참조)."
                    ),
                },
            ],
        },
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "독감 환자를 조기 진단하는 모델에서 "
                    "가장 중요하게 높여야 할 지표는 무엇인가? "
                    "(독감인데 음성 판정 = 치명적)"
                ),
                "choices": [
                    "A) Precision (정밀도)",
                    "B) Recall (재현율)",
                    "C) Accuracy (정확도)",
                    "D) Specificity (특이도)",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "StratifiedKFold와 KFold의 핵심 차이점은 무엇인가?",
                "choices": [
                    "A) StratifiedKFold가 더 많은 Fold를 사용한다",
                    "B) StratifiedKFold는 각 Fold에서 클래스 비율을 원본과 동일하게 유지한다",
                    "C) KFold는 분류 문제에만 사용 가능하다",
                    "D) StratifiedKFold는 회귀 문제에 권장된다",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "학습 곡선에서 훈련 점수는 0.98이고 검증 점수는 0.72일 때 "
                    "이 모델은 어떤 상태인지 설명하고 해결 방법을 서술하시오."
                ),
                "answer": (
                    "과적합(Overfitting) 상태입니다. "
                    "모델이 훈련 데이터를 암기해 새 데이터에 일반화하지 못합니다. "
                    "해결 방법: max_depth 감소, min_samples_leaf 증가 등 규제 강화, "
                    "훈련 데이터 추가, 중요도 낮은 특성 제거 등."
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "load_wine() 데이터셋으로 DecisionTreeClassifier를 학습하고 "
                    "5-Fold StratifiedKFold 교차 검증으로 accuracy와 f1_macro 점수를 출력하시오. "
                    "(random_state=42, shuffle=True)"
                ),
                "hint": (
                    "cross_val_score에 cv=skf를 전달합니다. "
                    "f1_macro는 scoring='f1_macro'로 지정합니다 (다중 분류 시 사용)."
                ),
                "answer": (
                    "from sklearn.datasets import load_wine\n"
                    "from sklearn.tree import DecisionTreeClassifier\n"
                    "from sklearn.model_selection import cross_val_score, StratifiedKFold\n"
                    "import numpy as np\n\n"
                    "wine = load_wine()\n"
                    "dt = DecisionTreeClassifier(random_state=42)\n"
                    "skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n\n"
                    "acc = cross_val_score(dt, wine.data, wine.target, cv=skf, scoring='accuracy')\n"
                    "f1  = cross_val_score(dt, wine.data, wine.target, cv=skf, scoring='f1_macro')\n\n"
                    "print(f'Accuracy: {acc.mean():.4f} +- {acc.std():.4f}')\n"
                    "print(f'F1 Macro: {f1.mean():.4f} +- {f1.std():.4f}')"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "load_breast_cancer()로 RandomForestClassifier를 GridSearchCV로 튜닝하시오. "
                    "탐색 파라미터: n_estimators=[50, 100], max_depth=[5, 10, None]. "
                    "cv=5, scoring='recall', n_jobs=-1. "
                    "최적 파라미터와 최고 recall, 테스트셋 accuracy를 출력하시오."
                ),
                "hint": (
                    "grid_search.best_params_, grid_search.best_score_, "
                    "grid_search.best_estimator_.score(X_test, y_test)를 활용합니다."
                ),
                "answer": (
                    "from sklearn.datasets import load_breast_cancer\n"
                    "from sklearn.ensemble import RandomForestClassifier\n"
                    "from sklearn.model_selection import GridSearchCV, train_test_split\n\n"
                    "cancer = load_breast_cancer()\n"
                    "X_train, X_test, y_train, y_test = train_test_split(\n"
                    "    cancer.data, cancer.target, test_size=0.2, random_state=42\n"
                    ")\n\n"
                    "param_grid = {\n"
                    "    'n_estimators': [50, 100],\n"
                    "    'max_depth': [5, 10, None],\n"
                    "}\n"
                    "gs = GridSearchCV(\n"
                    "    RandomForestClassifier(random_state=42),\n"
                    "    param_grid, cv=5, scoring='recall', n_jobs=-1\n"
                    ")\n"
                    "gs.fit(X_train, y_train)\n\n"
                    "print('최적 파라미터:', gs.best_params_)\n"
                    "print(f'최고 Recall: {gs.best_score_:.4f}')\n"
                    "print(f'테스트 Accuracy: {gs.best_estimator_.score(X_test, y_test):.4f}')"
                ),
            },
        ],
        "challenge": {
            "question": (
                "완전한 모델 평가 파이프라인을 구축하세요. "
                "1) load_breast_cancer()로 데이터 로드, train 70% / test 30% 분할 "
                "2) RandomForestClassifier를 RandomizedSearchCV로 튜닝 "
                "   (n_estimators: 50~300 정수, max_depth: 3~15 정수, n_iter=20, cv=5, scoring='f1') "
                "3) 최적 모델로 테스트셋 평가: accuracy, precision, recall, f1, AUC 출력 "
                "4) confusion_matrix 출력 "
                "5) 학습 곡선 데이터를 계산해 '데이터 10% vs 100%'에서의 훈련/검증 점수 비교 출력 "
                "모든 결과를 가독성 있게 섹션별로 출력하세요."
            ),
            "hint": (
                "RandomizedSearchCV에 scipy.stats.randint를 활용하세요. "
                "AUC는 roc_auc_score(y_test, best_model.predict_proba(X_test)[:, 1])로 계산합니다. "
                "learning_curve의 train_sizes=[0.1, 1.0]으로 두 지점만 비교하면 간결합니다."
            ),
        },
        "summary": [
            "혼동 행렬의 TP/FP/FN/TN을 이해하면 Precision, Recall, F1 지표의 의미를 파악할 수 있다.",
            "클래스 불균형 데이터에서는 Accuracy 대신 F1-Score와 AUC를 주요 지표로 사용해야 한다.",
            "MSE/RMSE/MAE/R²는 회귀 모델의 오차를 다양한 관점에서 측정하는 지표다.",
            "StratifiedKFold 교차 검증은 클래스 비율을 유지하면서 모델의 평균 성능과 안정성을 측정한다.",
            "GridSearchCV는 모든 조합을 탐색하고 RandomizedSearchCV는 랜덤 샘플링으로 빠르게 탐색한다.",
            "학습 곡선과 검증 곡선으로 과적합/과소적합을 진단하고 처방 방향을 결정한다.",
            "AUC는 임계값에 독립적인 분류 성능 지표로 MLOps 배포 결정 기준으로 널리 사용된다.",
        ],
    }
