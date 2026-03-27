"""챕터 8: 모델 모니터링 & 재학습 — 운영 중인 모델의 건강을 지속적으로 관리한다."""


def get_chapter():
    """챕터 8 콘텐츠를 반환한다."""
    return {
        "number": 8,
        "title": "모델 모니터링 & 재학습",
        "subtitle": "운영 중인 모델의 건강을 지속적으로 관리한다",
        "big_picture": (
            "모델 배포는 끝이 아니라 시작입니다. "
            "현실 세계의 데이터는 시간이 지나면서 변합니다. "
            "코로나19 같은 사건이 발생하면 사용자 행동이 급변하고, "
            "훈련 데이터로 만든 모델은 더 이상 현실을 잘 표현하지 못하게 됩니다. "
            "이것이 '모델 드리프트'입니다. "
            "이 챕터에서는 드리프트를 감지하는 방법, "
            "모니터링 지표를 설계하는 법, "
            "자동 재학습 파이프라인을 구축하는 실무 방법을 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: 왜 모니터링이 필요한가 ──────────────────
            {
                "title": "왜 모니터링이 필요한가? 모델 성능 저하",
                "content": [
                    "소프트웨어는 코드를 바꾸지 않으면 동일하게 동작하지만, "
                    "ML 모델은 코드를 바꾸지 않아도 성능이 저하됩니다. "
                    "이유는 '데이터'가 바뀌기 때문입니다. "
                    "모니터링 없이는 성능 저하가 얼마나 심각한지조차 알 수 없습니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "기상 예보 모델을 여름 데이터로 학습했다면 "
                            "겨울이 되면 예측이 크게 틀릴 것입니다. "
                            "은행 사기 탐지 모델도 마찬가지입니다. "
                            "사기꾼들이 새로운 패턴을 학습하면 "
                            "6개월 전 모델은 새로운 사기 방식을 탐지하지 못합니다. "
                            "자동차 오일을 한 번도 교환하지 않으면 엔진이 망가지듯, "
                            "모델도 주기적인 점검과 교체가 필요합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["성능 저하 원인", "예시", "감지 방법"],
                        "rows": [
                            ["데이터 드리프트", "입력 특성 분포 변화 (코로나로 쇼핑 패턴 변화)", "입력 분포 모니터링"],
                            ["컨셉 드리프트", "y=f(X) 관계 자체가 변화 (금리 인상으로 주택 가격 모델 무효화)", "출력 분포 + 정확도 추적"],
                            ["데이터 품질 저하", "NULL 급증, 이상치 폭발", "데이터 프로파일링"],
                            ["업스트림 변경", "특성 계산 파이프라인 버그", "특성 통계 비교"],
                        ],
                    },
                ],
            },
            # ── 섹션 2: 드리프트 유형 ─────────────────────────────
            {
                "title": "드리프트의 종류: 데이터·모델·컨셉",
                "content": [
                    "드리프트는 세 가지 수준에서 발생합니다. "
                    "각각의 원인과 대응 방법이 다르므로 구분하여 이해해야 합니다.",
                    {
                        "type": "table",
                        "headers": ["유형", "정의", "예시", "대응"],
                        "rows": [
                            ["데이터 드리프트\n(Data Drift)",
                             "입력 특성 X의 분포 변화\n(P(X) 변화)",
                             "온도 센서 분포가 계절로 변화",
                             "입력 통계 모니터링 + 재학습"],
                            ["컨셉 드리프트\n(Concept Drift)",
                             "X와 y의 관계 자체가 변화\n(P(y|X) 변화)",
                             "경기 침체로 신용 점수와 연체율 관계 변화",
                             "라벨 수집 + 즉시 재학습"],
                            ["모델 드리프트\n(Model Drift)",
                             "실제 예측 정확도가 저하",
                             "정확도 90% -> 70%로 하락",
                             "성능 지표 모니터링 + 알림"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "컨셉 드리프트가 가장 위험합니다. "
                            "데이터 드리프트는 입력 분포만 보면 감지할 수 있지만, "
                            "컨셉 드리프트는 실제 라벨(정답)이 있어야 확인할 수 있습니다. "
                            "라벨을 얻기까지 시간이 걸리는 경우(예: 대출 연체는 수개월 후 확인) "
                            "컨셉 드리프트를 조기에 발견하기 어렵습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 모니터링 지표 설계 ────────────────────────
            {
                "title": "모니터링 지표 설계",
                "content": [
                    "무엇을 측정할지 결정하는 것이 모니터링의 핵심입니다. "
                    "너무 많은 지표는 노이즈를 만들고, "
                    "너무 적으면 중요한 변화를 놓칩니다.",
                    {
                        "type": "table",
                        "headers": ["지표 종류", "측정 대상", "도구/방법"],
                        "rows": [
                            ["서비스 지표", "응답 시간(p50/p95/p99), 에러율, 처리량", "Prometheus, Grafana"],
                            ["예측 분포", "예측 클래스 비율, 예측 점수 분포", "히스토그램, KS 검정"],
                            ["입력 분포", "각 특성의 평균·분산·분위수", "PSI, KL Divergence"],
                            ["모델 정확도", "Accuracy, F1, AUC (지연 라벨 필요)", "일별/주별 집계"],
                            ["데이터 품질", "NULL 비율, 이상치 비율", "Great Expectations"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 예측 로깅 시스템 설계\n"
                            "import json\n"
                            "import time\n"
                            "import uuid\n"
                            "from dataclasses import dataclass, asdict\n"
                            "from typing import List, Optional\n\n"
                            "@dataclass(frozen=True)\n"
                            "class PredictionLog:\n"
                            "    \"\"\"예측 로그 레코드 (불변 객체).\"\"\"\n"
                            "    prediction_id: str\n"
                            "    timestamp: float\n"
                            "    input_features: List[float]\n"
                            "    predicted_class: int\n"
                            "    probabilities: List[float]\n"
                            "    model_version: str\n"
                            "    latency_ms: float\n"
                            "    actual_label: Optional[int] = None  # 나중에 채워짐\n\n\n"
                            "def log_prediction(\n"
                            "    features: List[float],\n"
                            "    predicted_class: int,\n"
                            "    probabilities: List[float],\n"
                            "    model_version: str,\n"
                            "    latency_ms: float,\n"
                            ") -> PredictionLog:\n"
                            "    \"\"\"예측 결과를 로그로 기록한다 (새 객체 반환).\"\"\"\n"
                            "    return PredictionLog(\n"
                            "        prediction_id=str(uuid.uuid4()),\n"
                            "        timestamp=time.time(),\n"
                            "        input_features=features,\n"
                            "        predicted_class=predicted_class,\n"
                            "        probabilities=probabilities,\n"
                            "        model_version=model_version,\n"
                            "        latency_ms=latency_ms,\n"
                            "    )\n\n\n"
                            "# FastAPI 엔드포인트에서 사용\n"
                            "import time\n\n"
                            "# (이전 챕터 FastAPI 코드에 추가)\n"
                            "# @app.post('/predict')\n"
                            "# async def predict(features: IrisFeatures):\n"
                            "#     start = time.time()\n"
                            "#     ...(예측 수행)...\n"
                            "#     latency = (time.time() - start) * 1000\n"
                            "#     log = log_prediction([...], cls, probas, 'v1.0', latency)\n"
                            "#     # DB나 파일에 저장\n"
                            "#     append_to_log(log)   # 예: JSONL 파일에 추가"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 드리프트 감지 구현 ────────────────────────
            {
                "title": "Python으로 드리프트 감지 구현",
                "content": [
                    "통계적 가설 검정을 이용해 두 분포가 유의미하게 다른지 판단합니다. "
                    "PSI(Population Stability Index)와 KS 검정이 가장 널리 사용됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "from scipy import stats\n\n\n"
                            "def compute_psi(\n"
                            "    expected: np.ndarray,\n"
                            "    actual: np.ndarray,\n"
                            "    bins: int = 10,\n"
                            ") -> float:\n"
                            "    \"\"\"Population Stability Index(PSI)를 계산한다.\n\n"
                            "    PSI < 0.1  : 변화 없음\n"
                            "    PSI 0.1~0.2: 약간의 변화 (모니터링 강화)\n"
                            "    PSI > 0.2  : 유의미한 변화 (재학습 검토)\n"
                            "    \"\"\"\n"
                            "    # 기준 분포로 bin 경계를 설정\n"
                            "    breakpoints = np.percentile(\n"
                            "        expected, np.linspace(0, 100, bins + 1)\n"
                            "    )\n"
                            "    breakpoints = np.unique(breakpoints)  # 중복 제거\n\n"
                            "    # 각 구간의 비율 계산\n"
                            "    expected_pct = np.histogram(expected, bins=breakpoints)[0]\n"
                            "    actual_pct   = np.histogram(actual,   bins=breakpoints)[0]\n\n"
                            "    # 0 나눗셈 방지\n"
                            "    expected_pct = np.where(expected_pct == 0, 0.0001, expected_pct)\n"
                            "    actual_pct   = np.where(actual_pct   == 0, 0.0001, actual_pct)\n\n"
                            "    # 비율 정규화\n"
                            "    expected_pct = expected_pct / expected_pct.sum()\n"
                            "    actual_pct   = actual_pct   / actual_pct.sum()\n\n"
                            "    # PSI = sum((actual - expected) * ln(actual/expected))\n"
                            "    psi = np.sum(\n"
                            "        (actual_pct - expected_pct)\n"
                            "        * np.log(actual_pct / expected_pct)\n"
                            "    )\n"
                            "    return float(psi)\n\n\n"
                            "def ks_drift_test(\n"
                            "    reference: np.ndarray,\n"
                            "    current: np.ndarray,\n"
                            "    alpha: float = 0.05,\n"
                            ") -> dict:\n"
                            "    \"\"\"KS 검정으로 두 분포의 유의미한 차이를 검정한다.\"\"\"\n"
                            "    stat, p_value = stats.ks_2samp(reference, current)\n"
                            "    return {\n"
                            "        \"statistic\": float(stat),\n"
                            "        \"p_value\": float(p_value),\n"
                            "        \"drift_detected\": bool(p_value < alpha),\n"
                            "    }\n\n\n"
                            "# ── 사용 예시 ───────────────────────────────────────\n"
                            "# 학습 시점 데이터 (기준)\n"
                            "reference_sepal_length = np.random.normal(5.8, 0.8, 1000)\n\n"
                            "# 3개월 후 운영 데이터\n"
                            "current_sepal_length = np.random.normal(6.5, 1.2, 500)  # 분포 이동\n\n"
                            "psi_value = compute_psi(reference_sepal_length, current_sepal_length)\n"
                            "ks_result = ks_drift_test(reference_sepal_length, current_sepal_length)\n\n"
                            "print(f\"PSI: {psi_value:.4f}\")  # 0.2 이상이면 드리프트\n"
                            "print(f\"KS 검정: {ks_result}\")   # drift_detected=True면 유의미한 차이"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Evidently AI (pip install evidently) 라이브러리를 사용하면 "
                            "데이터 드리프트, 모델 성능, 데이터 품질 리포트를 "
                            "HTML로 자동 생성할 수 있습니다. "
                            "직접 PSI를 구현하는 것보다 훨씬 빠르게 모니터링 대시보드를 구축할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 재학습 파이프라인 ─────────────────────────
            {
                "title": "재학습 파이프라인: 트리거 조건과 자동화",
                "content": [
                    "드리프트가 감지되면 모델을 재학습해야 합니다. "
                    "재학습 파이프라인은 '언제 재학습할지(트리거)', "
                    "'어떻게 재학습할지(프로세스)', "
                    "'재학습된 모델을 어떻게 배포할지(배포 전략)'를 정의합니다.",
                    {
                        "type": "flow_diagram",
                        "title": "모니터링 & 재학습 루프",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "모델 서빙", "sub": "예측 API"},
                            {"label": "로그 수집", "sub": "입력/출력 기록"},
                            {"label": "드리프트 감지", "sub": "PSI/KS 검정"},
                            {"label": "알림 발송", "sub": "트리거 조건 충족"},
                            {"label": "재학습", "sub": "새 데이터 + MLflow"},
                            {"label": "검증 & 배포", "sub": "성능 비교 후 전환"},
                        ],
                        "note": "전체 루프가 자동화되면 사람의 개입 없이 모델이 스스로 업데이트됩니다.",
                    },
                    {
                        "type": "table",
                        "headers": ["트리거 방식", "조건 예시", "장단점"],
                        "rows": [
                            ["주기적 재학습", "매주 월요일 오전 2시", "예측 가능, 불필요한 재학습 가능"],
                            ["성능 기반", "정확도 80% 미만", "라벨 필요, 지연 발생 가능"],
                            ["드리프트 기반", "PSI > 0.2", "라벨 없이 조기 감지 가능"],
                            ["데이터 볼륨 기반", "신규 데이터 10만 건 누적", "단순, 품질 보장 어려움"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 자동 재학습 파이프라인 구조\n"
                            "import mlflow\n"
                            "import mlflow.sklearn\n"
                            "import numpy as np\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.metrics import accuracy_score\n\n\n"
                            "def should_retrain(\n"
                            "    reference_data: np.ndarray,\n"
                            "    current_data: np.ndarray,\n"
                            "    psi_threshold: float = 0.2,\n"
                            ") -> tuple[bool, float]:\n"
                            "    \"\"\"재학습 트리거 여부를 판단한다.\"\"\"\n"
                            "    psi = compute_psi(reference_data, current_data)\n"
                            "    return psi > psi_threshold, psi\n\n\n"
                            "def retrain_and_evaluate(\n"
                            "    X_new: np.ndarray,\n"
                            "    y_new: np.ndarray,\n"
                            "    X_val: np.ndarray,\n"
                            "    y_val: np.ndarray,\n"
                            "    min_accuracy: float = 0.85,\n"
                            ") -> tuple[bool, str]:\n"
                            "    \"\"\"새 데이터로 재학습하고 품질 검증 후 등록한다.\"\"\"\n"
                            "    mlflow.set_experiment(\"auto-retrain\")\n\n"
                            "    with mlflow.start_run(run_name=\"auto-retrain\") as run:\n"
                            "        params = {\"n_estimators\": 100, \"random_state\": 42}\n"
                            "        mlflow.log_params(params)\n"
                            "        mlflow.set_tag(\"trigger\", \"psi_drift\")\n\n"
                            "        # 새 데이터로 재학습\n"
                            "        new_model = RandomForestClassifier(**params)\n"
                            "        new_model.fit(X_new, y_new)\n\n"
                            "        # 검증 세트로 품질 확인\n"
                            "        val_acc = accuracy_score(y_val, new_model.predict(X_val))\n"
                            "        mlflow.log_metric(\"val_accuracy\", val_acc)\n\n"
                            "        if val_acc < min_accuracy:\n"
                            "            # 품질 기준 미달 — 등록하지 않음\n"
                            "            return False, run.info.run_id\n\n"
                            "        # 품질 기준 통과 — Registry에 등록\n"
                            "        mlflow.sklearn.log_model(\n"
                            "            new_model, \"model\",\n"
                            "            registered_model_name=\"ProductionModel\",\n"
                            "        )\n"
                            "        return True, run.info.run_id\n\n\n"
                            "# ── 파이프라인 실행 ──────────────────────────────────\n"
                            "# 실제로는 Airflow, Prefect, cron 등으로 스케줄링\n"
                            "def run_monitoring_pipeline(\n"
                            "    reference: np.ndarray,\n"
                            "    current: np.ndarray,\n"
                            "    X_new, y_new, X_val, y_val,\n"
                            "):\n"
                            "    \"\"\"모니터링 → 드리프트 감지 → 재학습 전체 루프.\"\"\"\n"
                            "    trigger, psi = should_retrain(reference, current)\n"
                            "    print(f\"PSI: {psi:.4f}, 재학습 필요: {trigger}\")\n\n"
                            "    if trigger:\n"
                            "        success, run_id = retrain_and_evaluate(\n"
                            "            X_new, y_new, X_val, y_val\n"
                            "        )\n"
                            "        if success:\n"
                            "            print(f\"재학습 성공 — Run ID: {run_id}\")\n"
                            "            send_alert(\"재학습 완료: 새 모델 검토 필요\")\n"
                            "        else:\n"
                            "            print(\"재학습 실패 — 품질 기준 미달\")\n"
                            "            send_alert(\"재학습 실패: 수동 검토 필요\", level=\"warning\")"
                        ),
                    },
                ],
            },
            # ── 섹션 6: 알림 시스템 ────────────────────────────────
            {
                "title": "로깅과 알림 시스템 설계",
                "content": [
                    "드리프트가 감지되거나 모델 성능이 임계값 이하로 떨어지면 "
                    "담당자에게 즉시 알림을 보내야 합니다. "
                    "Python의 logging 모듈과 Slack Webhook을 연동하는 것이 실무에서 일반적입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import logging\n"
                            "import requests\n"
                            "import os\n\n"
                            "# 구조화된 로거 설정\n"
                            "logging.basicConfig(\n"
                            "    level=logging.INFO,\n"
                            "    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n"
                            ")\n"
                            "logger = logging.getLogger(\"model_monitor\")\n\n\n"
                            "def send_alert(message: str, level: str = \"info\") -> None:\n"
                            "    \"\"\"모니터링 알림을 로그에 기록하고 Slack으로 전송한다.\"\"\"\n"
                            "    log_fn = getattr(logger, level, logger.info)\n"
                            "    log_fn(message)\n\n"
                            "    # Slack Webhook (환경 변수에서 URL 읽기)\n"
                            "    webhook_url = os.getenv(\"SLACK_WEBHOOK_URL\")\n"
                            "    if not webhook_url:\n"
                            "        return  # 설정 없으면 건너뜀\n\n"
                            "    emoji = {\"info\": \":white_check_mark:\",\n"
                            "             \"warning\": \":warning:\",\n"
                            "             \"error\": \":red_circle:\"}.get(level, \":bell:\")\n\n"
                            "    payload = {\"text\": f\"{emoji} [ML Monitor] {message}\"}\n"
                            "    try:\n"
                            "        requests.post(webhook_url, json=payload, timeout=5)\n"
                            "    except requests.RequestException as exc:\n"
                            "        logger.error(\"Slack 알림 전송 실패: %s\", exc)\n\n\n"
                            "# 사용 예시\n"
                            "send_alert(\"PSI=0.25 감지 — 재학습 시작\", level=\"warning\")\n"
                            "send_alert(\"재학습 완료 — 정확도 0.91, Production 전환 검토 요청\")"
                        ),
                    },
                ],
            },
            # ── 섹션 7: A/B 테스트 개념 ───────────────────────────
            {
                "title": "A/B 테스트: 새 모델을 안전하게 도입하는 방법",
                "content": [
                    "새 모델을 한 번에 전체 트래픽에 적용하면 위험합니다. "
                    "A/B 테스트는 트래픽의 일부를 새 모델(B)에 보내고, "
                    "나머지는 기존 모델(A)에 유지하면서 성능을 비교합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import random\n"
                            "import hashlib\n\n\n"
                            "def get_model_variant(\n"
                            "    user_id: str,\n"
                            "    traffic_to_new: float = 0.1,  # 10% 트래픽을 새 모델로\n"
                            ") -> str:\n"
                            "    \"\"\"사용자 ID를 해싱하여 일관된 A/B 그룹을 배정한다.\"\"\"\n"
                            "    # 같은 user_id는 항상 같은 그룹에 배정됨 (일관성 보장)\n"
                            "    hash_value = int(\n"
                            "        hashlib.md5(user_id.encode()).hexdigest(), 16\n"
                            "    ) % 100\n"
                            "    return \"B\" if hash_value < (traffic_to_new * 100) else \"A\"\n\n\n"
                            "# FastAPI 엔드포인트에서 A/B 적용\n"
                            "# @app.post('/predict')\n"
                            "# async def predict(request: PredictRequest, user_id: str):\n"
                            "#     variant = get_model_variant(user_id, traffic_to_new=0.1)\n"
                            "#     model = model_store[variant]  # 'A' 또는 'B'\n"
                            "#     prediction = model.predict(request.features)\n"
                            "#     # variant를 로그에 기록하여 나중에 그룹별 성능 비교\n"
                            "#     log_prediction(..., ab_variant=variant)\n"
                            "#     return {\"prediction\": prediction, \"model\": variant}\n\n"
                            "# A/B 테스트 결과 분석 (수집 후)\n"
                            "def analyze_ab_test(\n"
                            "    logs_a: list,\n"
                            "    logs_b: list,\n"
                            ") -> dict:\n"
                            "    \"\"\"두 그룹의 성능을 비교한다.\"\"\"\n"
                            "    acc_a = sum(1 for log in logs_a if log[\"correct\"]) / len(logs_a)\n"
                            "    acc_b = sum(1 for log in logs_b if log[\"correct\"]) / len(logs_b)\n"
                            "    return {\n"
                            "        \"model_a_accuracy\": acc_a,\n"
                            "        \"model_b_accuracy\": acc_b,\n"
                            "        \"improvement\": acc_b - acc_a,\n"
                            "        \"recommendation\": \"B 전체 배포\" if acc_b > acc_a + 0.01 else \"A 유지\",\n"
                            "    }"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "A/B 테스트에서는 통계적 유의성을 반드시 확인하세요. "
                            "샘플이 충분하지 않으면 우연한 차이를 진짜 개선으로 오해할 수 있습니다. "
                            "일반적으로 각 그룹에 최소 수백 건 이상의 데이터가 필요합니다. "
                            "scipy.stats.chi2_contingency나 t-test로 p-value를 계산하세요."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "학습 시점의 데이터 통계(평균, 분산, 분위수)를 반드시 저장하세요. 이것이 드리프트 감지의 '기준선(baseline)'이 됩니다.",
            "Evidently AI, WhyLogs, Arize AI 등 오픈소스 모니터링 라이브러리로 PSI/드리프트 리포트를 자동화할 수 있습니다.",
            "재학습한 모델은 바로 Production에 올리지 말고 Staging에서 검증 후 점진적으로 트래픽을 늘려가세요.",
            "모든 예측에 unique prediction_id를 부여하면 나중에 예측-결과를 매칭하여 모델 정확도를 소급 계산할 수 있습니다.",
            "응답 시간(latency) 모니터링도 중요합니다. p95 응답 시간이 갑자기 늘어나면 모델 이외의 인프라 문제일 수 있습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "컨셉 드리프트(Concept Drift)의 정확한 정의는?"
                ),
                "choices": [
                    "A) 입력 특성 X의 분포가 변화한다",
                    "B) X와 y 사이의 관계 자체(P(y|X))가 변화한다",
                    "C) 모델 파라미터가 시간이 지나 손상된다",
                    "D) 서버 응답 시간이 증가한다",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "PSI(Population Stability Index) 값이 0.25일 때 올바른 판단은?"
                ),
                "choices": [
                    "A) 변화 없음 — 별도 조치 불필요",
                    "B) 약간의 변화 — 모니터링 강화",
                    "C) 유의미한 변화 — 재학습 검토 필요",
                    "D) PSI는 0~1 범위를 벗어날 수 없어 무효한 값이다",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "A/B 테스트에서 user_id를 해싱하여 그룹을 배정하는 이유는?"
                ),
                "choices": [
                    "A) 보안 강화를 위해",
                    "B) 같은 사용자가 매 요청마다 다른 그룹에 배정되도록 하기 위해",
                    "C) 같은 사용자가 항상 같은 그룹에 배정되는 일관성을 보장하기 위해",
                    "D) 해싱이 랜덤보다 더 균등한 분포를 만들기 때문에",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "두 NumPy 배열(reference, current)을 받아 "
                    "scipy.stats.ks_2samp으로 KS 검정을 수행하고, "
                    "p_value가 0.05 미만이면 True(드리프트 감지), "
                    "아니면 False를 반환하는 함수를 작성하세요."
                ),
                "hint": (
                    "from scipy import stats → "
                    "stat, p_value = stats.ks_2samp(reference, current) → "
                    "return p_value < 0.05"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "FastAPI 서버에서 예측 결과를 로그 파일(predictions.jsonl)에 기록하는 "
                    "함수를 작성하세요. "
                    "각 줄에 prediction_id, timestamp, predicted_class, latency_ms를 "
                    "JSON으로 저장합니다."
                ),
                "hint": (
                    "import json, time, uuid → "
                    "record = {'prediction_id': str(uuid.uuid4()), 'timestamp': time.time(), ...} → "
                    "with open('predictions.jsonl', 'a') as f: f.write(json.dumps(record) + 'newline')"
                ),
            },
        ],
        "challenge": {
            "question": (
                "챕터 6~7에서 만든 MLflow + FastAPI 시스템에 모니터링을 추가하세요. "
                "요구사항: "
                "1) FastAPI /predict 엔드포인트에서 모든 예측을 JSONL 파일에 로그로 저장합니다 "
                "(prediction_id, timestamp, features, predicted_class, probabilities, latency_ms 포함). "
                "2) 학습 데이터의 각 특성 통계(평균, 표준편차, 최솟값, 최댓값)를 "
                "reference_stats.json으로 저장합니다. "
                "3) PSI 계산 함수를 구현하고, 현재 예측 로그의 입력 분포와 "
                "학습 데이터 분포를 비교합니다. "
                "4) PSI > 0.2인 특성이 있을 때 경고 메시지를 출력하는 "
                "check_drift() 함수를 만듭니다. "
                "5) 드리프트 감지 시 새 데이터로 재학습하고 "
                "MLflow에 새 Run을 기록하는 시뮬레이션을 완성합니다."
            ),
            "hint": (
                "학습 완료 후 X_train의 통계를 numpy로 계산하여 JSON으로 저장합니다. "
                "서빙 API에서 lifespan 이벤트로 reference_stats.json을 로드합니다. "
                "check_drift()는 최근 N건의 로그를 읽어 compute_psi()를 호출합니다. "
                "드리프트 감지 시 retrain_and_evaluate()를 호출하는 흐름을 main 함수로 연결합니다."
            ),
        },
        "summary": [
            "ML 모델은 코드를 바꾸지 않아도 데이터 변화로 성능이 저하된다 — 이것이 모니터링이 필수인 이유다.",
            "데이터 드리프트는 입력 분포 변화, 컨셉 드리프트는 X-y 관계 변화, 모델 드리프트는 예측 정확도 저하를 의미한다.",
            "PSI > 0.2이면 유의미한 드리프트, KS 검정 p-value < 0.05이면 두 분포가 통계적으로 유의미하게 다르다는 신호다.",
            "예측 로그에 prediction_id를 부여하고 입력/출력을 모두 기록해야 드리프트 감지와 소급 성능 분석이 가능하다.",
            "재학습 파이프라인은 트리거 조건(PSI, 정확도, 주기) → 재학습 → 품질 검증 → 배포의 4단계로 구성된다.",
            "A/B 테스트로 새 모델을 점진적으로 도입하면 전체 서비스에 미치는 영향을 최소화하며 안전하게 교체할 수 있다.",
        ],
    }
