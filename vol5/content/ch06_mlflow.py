"""챕터 6: MLflow로 실험 관리 — 모델 실험을 체계적으로 추적하고 관리한다."""


def get_chapter():
    """챕터 6 콘텐츠를 반환한다."""
    return {
        "number": 6,
        "title": "MLflow로 실험 관리",
        "subtitle": "모델 실험을 체계적으로 추적하고 관리한다",
        "big_picture": (
            "머신러닝 프로젝트에서 가장 흔한 실수는 '이 모델이 어떤 설정으로 학습된 건지'를 "
            "기억하지 못하는 것입니다. "
            "파라미터, 데이터셋 버전, 평가 지표... 실험이 늘어날수록 추적이 어려워집니다. "
            "MLflow는 이 문제를 해결하는 오픈소스 MLOps 플랫폼입니다. "
            "실험 로깅부터 모델 레지스트리, 배포 관리까지 머신러닝 생명주기 전체를 다룹니다. "
            "이 챕터에서는 MLflow Tracking으로 실험을 기록하고, "
            "Model Registry로 모델을 체계적으로 관리하는 법을 익힙니다."
        ),
        "sections": [
            # ── 섹션 1: MLOps란? ──────────────────────────────────
            {
                "title": "MLOps란? ML 시스템의 운영 과제",
                "content": [
                    "DevOps가 소프트웨어 개발과 운영을 통합한 것처럼, "
                    "MLOps는 머신러닝 개발과 운영을 통합합니다. "
                    "모델을 한 번 학습하는 것으로 끝나지 않고, "
                    "지속적으로 재학습·배포·모니터링하는 체계를 구축하는 것이 MLOps의 목표입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "일반 소프트웨어는 코드가 바뀌지 않으면 동일하게 동작합니다. "
                            "하지만 ML 모델은 데이터가 바뀌면 성능이 저하됩니다. "
                            "마치 6개월 전 날씨 예보 모델을 지금도 그대로 쓰는 것과 같습니다. "
                            "MLOps는 이런 '모델 부패(model decay)'를 자동으로 감지하고 "
                            "새로운 데이터로 재학습하는 파이프라인을 만드는 학문입니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["과제", "설명", "MLOps 해결책"],
                        "rows": [
                            ["재현성", "같은 결과를 다시 얻을 수 없음", "실험 파라미터·데이터 버전 추적"],
                            ["모델 관리", "어떤 버전이 운영 중인지 불명확", "Model Registry로 버전 관리"],
                            ["배포", "모델을 API로 서빙하기 어려움", "표준화된 모델 패키징·서빙"],
                            ["모니터링", "성능 저하를 감지 못함", "지표 모니터링·드리프트 감지"],
                            ["협업", "팀원 간 실험 공유 어려움", "중앙 집중식 실험 추적"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "MLOps 성숙도 레벨: "
                            "Level 0(수동 실험) → Level 1(ML 파이프라인 자동화) "
                            "→ Level 2(CI/CD + 자동 재학습). "
                            "대부분의 기업은 Level 0에서 시작합니다. "
                            "MLflow는 Level 0에서 Level 1로 도약하는 핵심 도구입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: MLflow 소개 ───────────────────────────────
            {
                "title": "MLflow 소개: 4가지 핵심 컴포넌트",
                "content": [
                    "MLflow는 4개의 독립적인 컴포넌트로 구성됩니다. "
                    "각 컴포넌트는 단독으로도 사용할 수 있고, "
                    "통합해서 완전한 MLOps 파이프라인을 구성할 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["컴포넌트", "역할", "주요 기능"],
                        "rows": [
                            ["MLflow Tracking", "실험 기록·비교", "파라미터, 메트릭, 아티팩트 로깅"],
                            ["MLflow Projects", "재현 가능한 실험 패키징", "환경 정의, 엔트리포인트"],
                            ["MLflow Models", "모델 패키징 표준화", "다양한 프레임워크 지원 (flavors)"],
                            ["MLflow Model Registry", "모델 버전 관리", "Staging/Production 스테이지"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# MLflow 설치\n"
                            "pip install mlflow scikit-learn pandas\n\n"
                            "# MLflow UI 실행 (기본 포트: 5000)\n"
                            "mlflow ui\n\n"
                            "# 브라우저에서 확인\n"
                            "# http://localhost:5000\n\n"
                            "# 특정 백엔드 스토리지 지정 (운영 환경)\n"
                            "# mlflow server \\\n"
                            "#   --backend-store-uri postgresql://user:pw@host/mlflow \\\n"
                            "#   --default-artifact-root s3://my-bucket/mlflow \\\n"
                            "#   --host 0.0.0.0 --port 5000"
                        ),
                    },
                ],
            },
            # ── 섹션 3: MLflow Tracking ───────────────────────────
            {
                "title": "MLflow Tracking: 실험 로깅",
                "content": [
                    "MLflow Tracking의 핵심은 Run(실행)입니다. "
                    "하나의 Run은 하나의 모델 학습 시도를 나타내며, "
                    "파라미터(hyperparameters), 메트릭(성능 지표), 아티팩트(모델 파일)를 기록합니다. "
                    "여러 Run을 Experiment(실험)로 그룹화할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import mlflow\n"
                            "import mlflow.sklearn\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.model_selection import train_test_split\n"
                            "from sklearn.metrics import accuracy_score, f1_score\n"
                            "from sklearn.datasets import load_iris\n\n"
                            "# 실험 이름 설정 (없으면 자동 생성)\n"
                            "mlflow.set_experiment(\"iris-classification\")\n\n"
                            "# 학습 데이터 준비\n"
                            "X, y = load_iris(return_X_y=True)\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42\n"
                            ")\n\n"
                            "# Run 시작: with 블록 안의 모든 로깅이 이 Run에 기록됨\n"
                            "with mlflow.start_run(run_name=\"rf-baseline\"):\n"
                            "    # ── 파라미터 로깅 ──────────────────────────\n"
                            "    params = {\n"
                            "        \"n_estimators\": 100,\n"
                            "        \"max_depth\": 5,\n"
                            "        \"random_state\": 42,\n"
                            "    }\n"
                            "    mlflow.log_params(params)  # 여러 파라미터 한 번에\n\n"
                            "    # ── 모델 학습 ──────────────────────────────\n"
                            "    model = RandomForestClassifier(**params)\n"
                            "    model.fit(X_train, y_train)\n\n"
                            "    # ── 메트릭 로깅 ────────────────────────────\n"
                            "    y_pred = model.predict(X_test)\n"
                            "    accuracy = accuracy_score(y_test, y_pred)\n"
                            "    f1 = f1_score(y_test, y_pred, average=\"weighted\")\n\n"
                            "    mlflow.log_metric(\"accuracy\", accuracy)\n"
                            "    mlflow.log_metric(\"f1_score\", f1)\n\n"
                            "    # ── 에포크별 메트릭 (학습 곡선) ────────────\n"
                            "    for epoch, score in enumerate([0.80, 0.88, 0.93, 0.95]):\n"
                            "        mlflow.log_metric(\"train_acc\", score, step=epoch)\n\n"
                            "    # ── 아티팩트 로깅 (파일 저장) ──────────────\n"
                            "    import json\n"
                            "    with open(\"feature_importance.json\", \"w\") as f:\n"
                            "        importances = dict(zip(\n"
                            "            [f\"feat_{i}\" for i in range(4)],\n"
                            "            model.feature_importances_.tolist()\n"
                            "        ))\n"
                            "        json.dump(importances, f)\n"
                            "    mlflow.log_artifact(\"feature_importance.json\")\n\n"
                            "    # ── 태그 추가 (메타정보) ────────────────────\n"
                            "    mlflow.set_tag(\"data_version\", \"v1.0\")\n"
                            "    mlflow.set_tag(\"author\", \"kim\")\n\n"
                            "    print(f\"accuracy: {accuracy:.4f}, f1: {f1:.4f}\")\n"
                            "    print(f\"Run ID: {mlflow.active_run().info.run_id}\")"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "mlflow.autolog()를 사용하면 scikit-learn, PyTorch, TensorFlow 등에서 "
                            "파라미터와 메트릭을 자동으로 기록합니다. "
                            "단 한 줄로 대부분의 로깅이 자동화됩니다. "
                            "fit() 호출 전에 mlflow.sklearn.autolog()를 추가하면 됩니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# autolog 사용 예시 — fit() 전에 한 줄 추가\n"
                            "mlflow.sklearn.autolog()  # 자동 로깅 활성화\n\n"
                            "with mlflow.start_run():\n"
                            "    model = RandomForestClassifier(n_estimators=100)\n"
                            "    model.fit(X_train, y_train)  # 파라미터·메트릭 자동 기록\n"
                            "    # 별도 log_params / log_metrics 호출 불필요\n\n"
                            "# 실행 결과를 DataFrame으로 조회\n"
                            "import mlflow\n"
                            "runs = mlflow.search_runs(\n"
                            "    experiment_names=[\"iris-classification\"],\n"
                            "    order_by=[\"metrics.accuracy DESC\"],\n"
                            ")\n"
                            "print(runs[[\"run_id\", \"params.n_estimators\", \"metrics.accuracy\"]].head())"
                        ),
                    },
                ],
            },
            # ── 섹션 4: 모델 저장과 로드 ──────────────────────────
            {
                "title": "모델 저장과 로드: log_model / load_model",
                "content": [
                    "MLflow는 모델을 '플레이버(flavor)' 개념으로 저장합니다. "
                    "sklearn, pytorch, tensorflow, pyfunc 등 다양한 프레임워크를 "
                    "통일된 인터페이스로 저장하고 로드할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import mlflow\n"
                            "import mlflow.sklearn\n"
                            "from sklearn.ensemble import RandomForestClassifier\n\n"
                            "# ── 모델 저장 ──────────────────────────────────────\n"
                            "with mlflow.start_run() as run:\n"
                            "    model = RandomForestClassifier(n_estimators=100)\n"
                            "    model.fit(X_train, y_train)\n\n"
                            "    # 모델을 아티팩트로 저장 (artifact_path: 저장 경로 이름)\n"
                            "    mlflow.sklearn.log_model(\n"
                            "        sk_model=model,\n"
                            "        artifact_path=\"model\",\n"
                            "        # 입력 예시와 서명(스키마) 자동 추론\n"
                            "        input_example=X_test[:3],\n"
                            "    )\n"
                            "    run_id = run.info.run_id\n"
                            "    print(f\"저장된 Run ID: {run_id}\")\n\n"
                            "# ── 모델 로드 ──────────────────────────────────────\n"
                            "# runs:/<run_id>/<artifact_path> 형식의 URI 사용\n"
                            "model_uri = f\"runs:/{run_id}/model\"\n"
                            "loaded_model = mlflow.sklearn.load_model(model_uri)\n\n"
                            "# 예측\n"
                            "predictions = loaded_model.predict(X_test)\n"
                            "print(f\"예측 결과: {predictions[:5]}\")\n\n"
                            "# ── pyfunc로 프레임워크 독립적 로드 ─────────────────\n"
                            "# 어떤 프레임워크 모델이든 동일한 인터페이스로 로드 가능\n"
                            "pyfunc_model = mlflow.pyfunc.load_model(model_uri)\n"
                            "pyfunc_preds = pyfunc_model.predict(X_test)\n"
                            "print(f\"pyfunc 예측: {pyfunc_preds[:5]}\")"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "MLflow 모델 저장 폴더 구조: "
                            "model/ 아래에 MLmodel(메타정보), model.pkl(모델 바이너리), "
                            "conda.yaml(환경 정보), requirements.txt 등이 생성됩니다. "
                            "이 폴더 구조 자체가 MLflow의 모델 표준 포맷(MLflow Model)입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: MLflow UI ──────────────────────────────────
            {
                "title": "MLflow UI 활용: 실험 비교와 분석",
                "content": [
                    "mlflow ui 명령으로 실행되는 웹 인터페이스는 "
                    "실험 결과를 시각적으로 비교할 수 있는 강력한 도구입니다. "
                    "여러 Run의 메트릭을 차트로 비교하고, 최적 파라미터를 찾는 데 유용합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 여러 파라미터 조합 실험 (Grid Search 로깅 예시)\n"
                            "import mlflow\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.metrics import accuracy_score\n\n"
                            "mlflow.set_experiment(\"iris-hyperparameter-search\")\n\n"
                            "# 탐색할 파라미터 공간\n"
                            "param_grid = [\n"
                            "    {\"n_estimators\": 50,  \"max_depth\": 3},\n"
                            "    {\"n_estimators\": 100, \"max_depth\": 5},\n"
                            "    {\"n_estimators\": 200, \"max_depth\": 10},\n"
                            "]\n\n"
                            "for params in param_grid:\n"
                            "    run_name = f\"rf-n{params['n_estimators']}-d{params['max_depth']}\"\n"
                            "    with mlflow.start_run(run_name=run_name):\n"
                            "        mlflow.log_params(params)\n\n"
                            "        model = RandomForestClassifier(**params, random_state=42)\n"
                            "        model.fit(X_train, y_train)\n\n"
                            "        acc = accuracy_score(y_test, model.predict(X_test))\n"
                            "        mlflow.log_metric(\"accuracy\", acc)\n"
                            "        print(f\"{run_name}: accuracy={acc:.4f}\")\n\n"
                            "# MLflow UI (http://localhost:5000) 에서\n"
                            "# 세 Run의 accuracy를 나란히 비교할 수 있습니다"
                        ),
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "Experiments 탭: 실험별 Run 목록, 메트릭 비교 테이블",
                            "Run 상세 페이지: 파라미터, 메트릭 차트, 아티팩트 파일 브라우저",
                            "Compare 기능: 여러 Run 선택 후 메트릭 비교 차트 생성",
                            "Models 탭: Model Registry에 등록된 모델 버전 관리",
                        ],
                    },
                ],
            },
            # ── 섹션 6: Model Registry ─────────────────────────────
            {
                "title": "MLflow Model Registry: 모델 생명주기 관리",
                "content": [
                    "Model Registry는 실험에서 검증된 모델을 Staging, Production 등의 "
                    "스테이지로 관리하는 중앙 저장소입니다. "
                    "어떤 모델이 현재 운영 중인지 명확하게 추적하고, "
                    "팀 전체가 동일한 모델 버전을 사용하도록 보장합니다.",
                    {
                        "type": "flow_diagram",
                        "title": "MLflow 워크플로우: 실험부터 배포까지",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "실험 설계", "sub": "파라미터 정의"},
                            {"label": "학습 & 로깅", "sub": "Tracking Server"},
                            {"label": "실험 비교", "sub": "MLflow UI"},
                            {"label": "모델 등록", "sub": "Model Registry"},
                            {"label": "스테이지 전환", "sub": "Staging → Production"},
                            {"label": "서빙", "sub": "mlflow models serve"},
                        ],
                        "note": "Model Registry를 통해 모델 버전과 배포 상태를 중앙에서 관리합니다.",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import mlflow\n"
                            "from mlflow.tracking import MlflowClient\n\n"
                            "# ── 1. 모델 레지스트리에 등록 ──────────────────────\n"
                            "# 방법 A: log_model 시 registered_model_name 지정\n"
                            "with mlflow.start_run():\n"
                            "    mlflow.sklearn.log_model(\n"
                            "        sk_model=model,\n"
                            "        artifact_path=\"model\",\n"
                            "        registered_model_name=\"IrisClassifier\",  # 자동 등록\n"
                            "    )\n\n"
                            "# 방법 B: 기존 Run에서 사후 등록\n"
                            "model_uri = f\"runs:/{run_id}/model\"\n"
                            "mlflow.register_model(model_uri, \"IrisClassifier\")\n\n"
                            "# ── 2. 스테이지 전환 (Staging → Production) ────────\n"
                            "client = MlflowClient()\n\n"
                            "# 버전 1을 Staging으로 전환\n"
                            "client.transition_model_version_stage(\n"
                            "    name=\"IrisClassifier\",\n"
                            "    version=1,\n"
                            "    stage=\"Staging\",\n"
                            "    archive_existing_versions=False,\n"
                            ")\n\n"
                            "# 검증 완료 후 Production으로 승격\n"
                            "client.transition_model_version_stage(\n"
                            "    name=\"IrisClassifier\",\n"
                            "    version=1,\n"
                            "    stage=\"Production\",\n"
                            "    archive_existing_versions=True,  # 기존 Production 아카이브\n"
                            ")\n\n"
                            "# ── 3. Production 모델 로드 ─────────────────────────\n"
                            "# 항상 최신 Production 모델을 로드\n"
                            "prod_model = mlflow.sklearn.load_model(\n"
                            "    \"models:/IrisClassifier/Production\"\n"
                            ")\n"
                            "print(\"Production 모델 로드 완료\")\n\n"
                            "# ── 4. 모델 버전 정보 조회 ──────────────────────────\n"
                            "versions = client.get_latest_versions(\n"
                            "    \"IrisClassifier\", stages=[\"Production\"]\n"
                            ")\n"
                            "for v in versions:\n"
                            "    print(f\"버전: {v.version}, 스테이지: {v.current_stage}\")\n"
                            "    print(f\"Run ID: {v.run_id}\")"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["스테이지", "의미", "전환 조건"],
                        "rows": [
                            ["None", "레지스트리에 등록만 된 상태", "등록 직후 기본 상태"],
                            ["Staging", "테스트·검증 중인 모델", "실험에서 유망한 결과 확인 후"],
                            ["Production", "실제 서비스에 사용 중인 모델", "Staging 검증 통과 후"],
                            ["Archived", "더 이상 사용하지 않는 모델", "새 버전 Production 전환 시"],
                        ],
                    },
                    {
                        "type": "warning",
                        "text": (
                            "MLflow 2.x부터는 stage 개념이 deprecated되고 "
                            "aliases(별칭) 방식으로 전환되고 있습니다. "
                            "예: client.set_registered_model_alias('IrisClassifier', 'champion', 1). "
                            "새 프로젝트에서는 aliases 방식을 사용하는 것을 권장합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "mlflow.set_tracking_uri()로 원격 MLflow 서버를 지정하면 팀 전체가 동일한 실험 결과를 공유할 수 있습니다.",
            "run_name을 의미 있게 설정하면 (예: 'rf-n100-lr0.01-v2data') UI에서 실험을 훨씬 쉽게 찾을 수 있습니다.",
            "mlflow.log_dict(), mlflow.log_figure(), mlflow.log_table() 등으로 다양한 형태의 아티팩트를 저장하세요.",
            "git commit hash를 태그로 기록하면 코드와 실험을 연결할 수 있습니다: mlflow.set_tag('git_commit', git_sha).",
            "MLflow Projects(MLproject 파일)로 실험을 패키징하면 mlflow run 명령 하나로 팀원이 동일한 환경에서 재현 가능합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "MLflow Tracking에서 하나의 모델 학습 시도를 나타내는 단위는?"
                ),
                "choices": [
                    "A) Experiment (실험)",
                    "B) Run (실행)",
                    "C) Model (모델)",
                    "D) Artifact (아티팩트)",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "MLflow Model Registry에서 실제 서비스에 사용 중인 모델 버전의 스테이지는?"
                ),
                "choices": [
                    "A) None",
                    "B) Staging",
                    "C) Production",
                    "D) Archived",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "mlflow.log_metric(\"loss\", 0.3, step=10)에서 step 파라미터의 역할은?"
                ),
                "choices": [
                    "A) 메트릭 측정 주기 (초 단위)",
                    "B) 에포크·스텝 번호로 시계열 차트를 그리기 위한 x축 값",
                    "C) 소수점 자리 수를 지정",
                    "D) 메트릭 저장 위치(파티션)를 지정",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "사이킷런 RandomForestClassifier를 학습하고 MLflow로 다음을 기록하세요: "
                    "1) n_estimators 파라미터, 2) accuracy 메트릭, 3) 모델을 'model' 경로로 저장. "
                    "실험 이름은 'my-experiment'로 설정하세요."
                ),
                "hint": (
                    "mlflow.set_experiment('my-experiment') → "
                    "with mlflow.start_run(): → "
                    "mlflow.log_param('n_estimators', 100) → "
                    "mlflow.log_metric('accuracy', acc) → "
                    "mlflow.sklearn.log_model(model, 'model')"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "run_id가 주어졌을 때, 해당 Run에서 저장된 모델을 로드하여 "
                    "테스트 데이터로 예측을 수행하는 코드를 작성하세요."
                ),
                "hint": (
                    "model_uri = f'runs:/{run_id}/model' → "
                    "mlflow.sklearn.load_model(model_uri) → "
                    "loaded_model.predict(X_test)"
                ),
            },
        ],
        "challenge": {
            "question": (
                "붓꽃(Iris) 데이터셋으로 하이퍼파라미터 탐색 실험을 MLflow로 완전히 관리하세요. "
                "요구사항: "
                "1) 'iris-search' 실험을 생성하고 RandomForest의 n_estimators(50, 100, 200), "
                "max_depth(3, 5, 10) 조합 9가지를 모두 실행합니다. "
                "2) 각 Run에 파라미터, accuracy, f1_score를 기록합니다. "
                "3) 가장 높은 accuracy를 보인 Run의 모델을 'BestIrisModel' 이름으로 "
                "Model Registry에 등록합니다. "
                "4) 등록된 모델을 Production 스테이지로 전환합니다. "
                "5) models:/BestIrisModel/Production URI로 모델을 로드하여 "
                "전체 테스트셋에 대한 정확도를 출력합니다."
            ),
            "hint": (
                "mlflow.search_runs(order_by=['metrics.accuracy DESC'])로 최고 Run을 찾습니다. "
                "mlflow.register_model(f'runs:/{best_run_id}/model', 'BestIrisModel')으로 등록하고 "
                "client.transition_model_version_stage로 Production 전환합니다."
            ),
        },
        "summary": [
            "MLOps는 ML 모델의 개발·배포·모니터링을 자동화하는 엔지니어링 관행으로, 재현성과 신뢰성을 높인다.",
            "MLflow는 Tracking, Projects, Models, Registry 4개 컴포넌트로 ML 생명주기 전체를 관리한다.",
            "with mlflow.start_run() 블록 안에서 log_param, log_metric, log_artifact로 실험을 기록한다.",
            "mlflow.sklearn.autolog()로 사이킷런 실험의 파라미터와 메트릭을 자동으로 기록할 수 있다.",
            "Model Registry로 Staging, Production 스테이지를 관리하며 운영 모델 버전을 명확하게 추적한다.",
            "모델 로드 시 models:/모델명/스테이지 URI를 사용하면 항상 해당 스테이지의 최신 모델을 가져온다.",
        ],
    }
