"""챕터 7: 모델 서빙 — 학습된 모델을 API로 제공하는 방법."""


def get_chapter():
    """챕터 7 콘텐츠를 반환한다."""
    return {
        "number": 7,
        "title": "모델 서빙",
        "subtitle": "학습된 모델을 REST API로 세상에 내보내기",
        "big_picture": (
            "아무리 좋은 모델을 만들어도 다른 사람이 사용할 수 없다면 의미가 없습니다. "
            "모델 서빙(Model Serving)은 학습된 모델을 HTTP API로 감싸서 "
            "웹 앱, 모바일 앱, 다른 서비스가 예측을 요청할 수 있게 하는 과정입니다. "
            "이 챕터에서는 모델을 저장하는 방법부터 "
            "FastAPI로 예측 API를 구축하고 Docker로 컨테이너화하는 "
            "실무 배포 흐름 전체를 다룹니다."
        ),
        "sections": [
            # ── 섹션 1: 모델 서빙이란? ───────────────────────────
            {
                "title": "모델 서빙이란?",
                "content": [
                    "모델 서빙은 학습된 ML 모델에 HTTP 요청을 보내면 "
                    "예측 결과를 JSON으로 반환하는 시스템을 만드는 것입니다. "
                    "실시간 예측과 배치 예측, 두 가지 방식이 있습니다.",
                    {
                        "type": "table",
                        "headers": ["방식", "설명", "사용 사례", "지연 시간"],
                        "rows": [
                            ["실시간 예측\n(Online Serving)", "요청 즉시 단건 예측", "스팸 필터, 추천 시스템", "밀리초 단위"],
                            ["배치 예측\n(Batch Serving)", "대량 데이터를 일괄 예측", "리포트 생성, 정기 점수 산출", "분~시간 단위"],
                            ["스트리밍 예측\n(Streaming)", "데이터 흐름에 실시간 예측", "사기 탐지, IoT 분석", "밀리초 단위"],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "모델 서빙 아키텍처",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "클라이언트", "sub": "앱/서비스"},
                            {"label": "HTTP 요청", "sub": "JSON 입력"},
                            {"label": "FastAPI 서버", "sub": "입력 검증"},
                            {"label": "모델 로드", "sub": "pkl/MLflow"},
                            {"label": "predict()", "sub": "추론 실행"},
                            {"label": "JSON 응답", "sub": "예측 결과"},
                        ],
                        "note": "모델은 서버 시작 시 메모리에 한 번 로드하고, 요청마다 predict()만 호출합니다.",
                    },
                ],
            },
            # ── 섹션 2: pickle/joblib로 모델 저장 ─────────────────
            {
                "title": "모델 저장: pickle과 joblib",
                "content": [
                    "학습된 모델을 파일로 저장해야 서빙 시 다시 불러올 수 있습니다. "
                    "pickle은 Python 표준 라이브러리이고, "
                    "joblib은 NumPy 배열이 포함된 사이킷런 모델에 더 효율적입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pickle\n"
                            "import joblib\n"
                            "from sklearn.ensemble import RandomForestClassifier\n"
                            "from sklearn.datasets import load_iris\n"
                            "from sklearn.model_selection import train_test_split\n\n"
                            "# 모델 학습\n"
                            "X, y = load_iris(return_X_y=True)\n"
                            "X_train, X_test, y_train, y_test = train_test_split(\n"
                            "    X, y, test_size=0.2, random_state=42\n"
                            ")\n"
                            "model = RandomForestClassifier(n_estimators=100, random_state=42)\n"
                            "model.fit(X_train, y_train)\n\n"
                            "# ── pickle로 저장 / 로드 ───────────────────────────\n"
                            "with open(\"model.pkl\", \"wb\") as f:\n"
                            "    pickle.dump(model, f)\n\n"
                            "with open(\"model.pkl\", \"rb\") as f:\n"
                            "    loaded_model = pickle.load(f)\n\n"
                            "# ── joblib로 저장 / 로드 (사이킷런 권장) ──────────\n"
                            "joblib.dump(model, \"model.joblib\")\n"
                            "loaded_model = joblib.load(\"model.joblib\")\n\n"
                            "print(f\"로드 확인: {loaded_model.predict(X_test[:3])}\")\n\n"
                            "# ── 전처리 파이프라인 함께 저장 ───────────────────\n"
                            "from sklearn.pipeline import Pipeline\n"
                            "from sklearn.preprocessing import StandardScaler\n\n"
                            "pipeline = Pipeline([\n"
                            "    (\"scaler\", StandardScaler()),\n"
                            "    (\"clf\", RandomForestClassifier(random_state=42)),\n"
                            "])\n"
                            "pipeline.fit(X_train, y_train)\n"
                            "joblib.dump(pipeline, \"pipeline.joblib\")  # 전처리+모델 통째로 저장"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "pickle 파일은 Python 버전과 라이브러리 버전에 의존합니다. "
                            "모델을 저장할 때 Python 버전, scikit-learn 버전을 "
                            "requirements.txt에 반드시 함께 기록하세요. "
                            "버전이 다른 환경에서 로드하면 오류가 발생할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: FastAPI로 서빙 API 구축 ───────────────────
            {
                "title": "FastAPI로 ML 모델 서빙 API 구축",
                "content": [
                    "FastAPI는 Python에서 고성능 API를 빠르게 만들 수 있는 프레임워크입니다. "
                    "자동 문서화, 타입 검증, 비동기 지원이 특징입니다. "
                    "ML 서빙 API를 만들 때 가장 많이 사용되는 선택지입니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "pip install fastapi uvicorn pydantic\n\n"
                            "# 실행\n"
                            "uvicorn main:app --reload --host 0.0.0.0 --port 8000"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# main.py — FastAPI 모델 서빙 API\n"
                            "import joblib\n"
                            "import numpy as np\n"
                            "from fastapi import FastAPI, HTTPException\n"
                            "from pydantic import BaseModel, Field\n"
                            "from contextlib import asynccontextmanager\n"
                            "from typing import List\n\n"
                            "# ── 요청/응답 스키마 (Pydantic 입력 검증) ────────\n"
                            "class IrisFeatures(BaseModel):\n"
                            "    \"\"\"붓꽃 분류 예측 요청 스키마.\"\"\"\n"
                            "    sepal_length: float = Field(..., gt=0, le=20, description=\"꽃받침 길이 (cm)\")\n"
                            "    sepal_width:  float = Field(..., gt=0, le=20, description=\"꽃받침 너비 (cm)\")\n"
                            "    petal_length: float = Field(..., gt=0, le=20, description=\"꽃잎 길이 (cm)\")\n"
                            "    petal_width:  float = Field(..., gt=0, le=20, description=\"꽃잎 너비 (cm)\")\n\n"
                            "    model_config = {\"json_schema_extra\": {\n"
                            "        \"example\": {\n"
                            "            \"sepal_length\": 5.1, \"sepal_width\": 3.5,\n"
                            "            \"petal_length\": 1.4, \"petal_width\": 0.2,\n"
                            "        }\n"
                            "    }}\n\n\n"
                            "class PredictionResponse(BaseModel):\n"
                            "    \"\"\"예측 응답 스키마.\"\"\"\n"
                            "    predicted_class: int\n"
                            "    class_name: str\n"
                            "    probabilities: List[float]\n\n\n"
                            "# ── 모델을 앱 시작 시 한 번만 로드 ──────────────\n"
                            "model_store: dict = {}  # 전역 모델 저장소 (불변 참조)\n"
                            "CLASS_NAMES = [\"setosa\", \"versicolor\", \"virginica\"]\n\n\n"
                            "@asynccontextmanager\n"
                            "async def lifespan(app: FastAPI):\n"
                            "    \"\"\"앱 시작/종료 이벤트 처리: 모델 로드.\"\"\"\n"
                            "    # 시작 시 모델 로드 (요청마다 로드하면 느림)\n"
                            "    model_store[\"model\"] = joblib.load(\"model.joblib\")\n"
                            "    print(\"모델 로드 완료\")\n"
                            "    yield\n"
                            "    model_store.clear()  # 종료 시 정리\n\n\n"
                            "app = FastAPI(\n"
                            "    title=\"Iris Classifier API\",\n"
                            "    description=\"붓꽃 품종 분류 ML 서빙 API\",\n"
                            "    version=\"1.0.0\",\n"
                            "    lifespan=lifespan,\n"
                            ")\n\n\n"
                            "@app.get(\"/health\")\n"
                            "async def health_check():\n"
                            "    \"\"\"서버 상태 확인 엔드포인트.\"\"\"\n"
                            "    return {\"status\": \"ok\", \"model_loaded\": \"model\" in model_store}\n\n\n"
                            "@app.post(\"/predict\", response_model=PredictionResponse)\n"
                            "async def predict(features: IrisFeatures):\n"
                            "    \"\"\"단건 예측 엔드포인트.\"\"\"\n"
                            "    if \"model\" not in model_store:\n"
                            "        raise HTTPException(status_code=503, detail=\"모델이 로드되지 않았습니다\")\n\n"
                            "    model = model_store[\"model\"]\n"
                            "    input_data = np.array([[  # 입력을 2D 배열로 변환\n"
                            "        features.sepal_length, features.sepal_width,\n"
                            "        features.petal_length, features.petal_width,\n"
                            "    ]])\n\n"
                            "    predicted_class = int(model.predict(input_data)[0])\n"
                            "    probabilities = model.predict_proba(input_data)[0].tolist()\n\n"
                            "    return PredictionResponse(\n"
                            "        predicted_class=predicted_class,\n"
                            "        class_name=CLASS_NAMES[predicted_class],\n"
                            "        probabilities=probabilities,\n"
                            "    )"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "FastAPI는 http://localhost:8000/docs 에서 "
                            "자동 생성된 Swagger UI를 제공합니다. "
                            "브라우저에서 직접 API를 테스트할 수 있어 "
                            "개발과 디버깅에 매우 유용합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 배치 예측 ──────────────────────────────────
            {
                "title": "배치 예측 엔드포인트",
                "content": [
                    "배치 예측은 여러 샘플을 한 번의 요청으로 처리합니다. "
                    "단건 예측보다 처리량(throughput)이 높고 "
                    "네트워크 오버헤드를 줄일 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# main.py에 배치 예측 엔드포인트 추가\n"
                            "from typing import List\n\n"
                            "class BatchRequest(BaseModel):\n"
                            "    \"\"\"배치 예측 요청 스키마.\"\"\"\n"
                            "    instances: List[IrisFeatures]\n\n\n"
                            "class BatchResponse(BaseModel):\n"
                            "    \"\"\"배치 예측 응답 스키마.\"\"\"\n"
                            "    predictions: List[PredictionResponse]\n"
                            "    total_count: int\n\n\n"
                            "@app.post(\"/predict/batch\", response_model=BatchResponse)\n"
                            "async def predict_batch(batch: BatchRequest):\n"
                            "    \"\"\"배치 예측 엔드포인트 (최대 100건).\"\"\"\n"
                            "    if len(batch.instances) > 100:\n"
                            "        raise HTTPException(\n"
                            "            status_code=400,\n"
                            "            detail=\"배치 크기는 100을 초과할 수 없습니다\",\n"
                            "        )\n\n"
                            "    if \"model\" not in model_store:\n"
                            "        raise HTTPException(status_code=503, detail=\"모델 미로드\")\n\n"
                            "    model = model_store[\"model\"]\n\n"
                            "    # 2D 배열로 일괄 변환\n"
                            "    input_array = np.array([\n"
                            "        [f.sepal_length, f.sepal_width, f.petal_length, f.petal_width]\n"
                            "        for f in batch.instances\n"
                            "    ])\n\n"
                            "    predicted_classes = model.predict(input_array)\n"
                            "    all_probas = model.predict_proba(input_array)\n\n"
                            "    predictions = [\n"
                            "        PredictionResponse(\n"
                            "            predicted_class=int(cls),\n"
                            "            class_name=CLASS_NAMES[int(cls)],\n"
                            "            probabilities=probas.tolist(),\n"
                            "        )\n"
                            "        for cls, probas in zip(predicted_classes, all_probas)\n"
                            "    ]\n\n"
                            "    return BatchResponse(\n"
                            "        predictions=predictions,\n"
                            "        total_count=len(predictions),\n"
                            "    )"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# curl로 단건 예측 테스트\n"
                            "curl -X POST http://localhost:8000/predict \\\n"
                            "  -H 'Content-Type: application/json' \\\n"
                            "  -d '{\"sepal_length\": 5.1, \"sepal_width\": 3.5,\n"
                            "       \"petal_length\": 1.4, \"petal_width\": 0.2}'\n\n"
                            "# 예상 응답\n"
                            "# {\"predicted_class\": 0, \"class_name\": \"setosa\",\n"
                            "#  \"probabilities\": [0.97, 0.02, 0.01]}"
                        ),
                    },
                ],
            },
            # ── 섹션 5: Docker 컨테이너화 ─────────────────────────
            {
                "title": "Docker로 모델 서빙 컨테이너화",
                "content": [
                    "FastAPI 서빙 서버를 Docker 이미지로 만들면 "
                    "클라우드나 온프레미스 어디서든 동일하게 실행할 수 있습니다. "
                    "모델 파일도 이미지에 포함하거나, 볼륨으로 마운트할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# 프로젝트 디렉토리 구조\n"
                            "# iris-serving/\n"
                            "#   main.py           - FastAPI 앱\n"
                            "#   model.joblib      - 학습된 모델\n"
                            "#   requirements.txt  - 의존성\n"
                            "#   Dockerfile        - 이미지 정의\n"
                            "#   .dockerignore     - 제외 파일 목록"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Dockerfile\n"
                            "FROM python:3.11-slim\n\n"
                            "WORKDIR /app\n\n"
                            "# 의존성 먼저 설치 (레이어 캐시 최적화)\n"
                            "COPY requirements.txt .\n"
                            "RUN pip install --no-cache-dir -r requirements.txt\n\n"
                            "# 앱 코드와 모델 파일 복사\n"
                            "COPY main.py .\n"
                            "COPY model.joblib .\n\n"
                            "# 포트 노출\n"
                            "EXPOSE 8000\n\n"
                            "# 헬스체크 (컨테이너 상태 자동 확인)\n"
                            "HEALTHCHECK --interval=30s --timeout=10s --retries=3 \\\n"
                            "  CMD curl -f http://localhost:8000/health || exit 1\n\n"
                            "# 서버 시작\n"
                            "CMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# .dockerignore\n"
                            "# __pycache__/\n"
                            "# *.pyc\n"
                            "# .env\n"
                            "# .git/\n\n"
                            "# requirements.txt 예시\n"
                            "# fastapi==0.110.0\n"
                            "# uvicorn==0.27.0\n"
                            "# scikit-learn==1.4.0\n"
                            "# pydantic==2.6.0\n"
                            "# numpy==1.26.0\n\n"
                            "# 이미지 빌드\n"
                            "docker build -t iris-serving:1.0 .\n\n"
                            "# 컨테이너 실행\n"
                            "docker run -d -p 8000:8000 --name iris-api iris-serving:1.0\n\n"
                            "# 상태 확인\n"
                            "docker ps\n"
                            "curl http://localhost:8000/health\n\n"
                            "# 로그 확인\n"
                            "docker logs iris-api -f"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "모델 파일이 크다면(수백 MB 이상) 이미지에 포함하지 말고 "
                            "S3, GCS 등 외부 스토리지에서 시작 시 다운로드하거나 "
                            "볼륨으로 마운트하는 방식을 사용하세요. "
                            "이미지 크기를 줄여 배포 속도를 높일 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: MLflow serve ───────────────────────────────
            {
                "title": "MLflow serve: 빠른 모델 서빙",
                "content": [
                    "MLflow에 등록된 모델은 별도의 코드 없이 "
                    "mlflow models serve 명령 하나로 REST API를 실행할 수 있습니다. "
                    "빠른 프로토타이핑과 테스트에 유용합니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# MLflow 로컬 실행 서버에서 모델 서빙\n"
                            "# (mlflow ui가 localhost:5000에서 실행 중이어야 함)\n"
                            "mlflow models serve \\\n"
                            "  -m \"models:/IrisClassifier/Production\" \\\n"
                            "  --port 5001 \\\n"
                            "  --env-manager conda\n\n"
                            "# conda 없이 로컬 Python 환경 사용\n"
                            "mlflow models serve \\\n"
                            "  -m \"runs:/RUN_ID/model\" \\\n"
                            "  --port 5001 \\\n"
                            "  --env-manager local\n\n"
                            "# 예측 요청 (MLflow 서빙 포맷: instances 키)\n"
                            "curl http://localhost:5001/invocations \\\n"
                            "  -H 'Content-Type: application/json' \\\n"
                            "  -d '{\"instances\": [[5.1, 3.5, 1.4, 0.2]]}'"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["방식", "장점", "단점", "추천 상황"],
                        "rows": [
                            ["FastAPI 직접 구현", "완전한 커스터마이징, 로직 추가 가능", "코드 작성 필요", "운영 환경"],
                            ["MLflow serve", "코드 없이 즉시 서빙", "커스텀 로직 추가 어려움", "빠른 프로토타이핑"],
                            ["Docker + FastAPI", "이식성 최고, 어디서든 실행", "빌드 시간 필요", "팀 협업·클라우드 배포"],
                        ],
                    },
                ],
            },
        ],
        "practical_tips": [
            "모델을 서버 시작 시 한 번만 로드하고 전역 변수에 저장하세요. 요청마다 로드하면 응답이 수십 배 느려집니다.",
            "Pydantic의 Field(gt=0, le=100)로 입력값 범위를 검증하면 비정상 입력이 모델에 도달하기 전에 차단됩니다.",
            "/health 엔드포인트를 항상 구현하세요. Docker HEALTHCHECK, 쿠버네티스 liveness probe가 이를 활용합니다.",
            "응답에 model_version, prediction_id 등을 포함하면 나중에 예측 결과를 추적하고 디버깅하기 쉬워집니다.",
            "전처리 파이프라인(StandardScaler 등)은 모델과 함께 하나의 Pipeline으로 저장하면 서빙 코드가 단순해집니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "FastAPI 서빙 서버에서 모델 로드의 올바른 위치는?"
                ),
                "choices": [
                    "A) 각 요청 핸들러 함수 안에서 매번 로드",
                    "B) 앱 시작 시 lifespan 컨텍스트에서 한 번만 로드",
                    "C) 모델이 필요할 때마다 동적으로 로드",
                    "D) 별도의 스레드에서 주기적으로 로드",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "사이킷런 모델 저장에 joblib이 pickle보다 권장되는 이유는?"
                ),
                "choices": [
                    "A) joblib 파일이 항상 더 작다",
                    "B) joblib은 NumPy 배열이 많은 사이킷런 모델에 더 효율적이다",
                    "C) joblib은 모든 프로그래밍 언어에서 읽을 수 있다",
                    "D) joblib은 pickle보다 보안이 강하다",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "Pydantic의 Field(..., gt=0, le=20)에서 '...'(Ellipsis)의 의미는?"
                ),
                "choices": [
                    "A) 기본값이 None임을 의미",
                    "B) 필드가 필수(required)임을 의미",
                    "C) 값이 0에서 20 사이의 중간값임을 의미",
                    "D) 해당 필드를 무시함을 의미",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "FastAPI 앱에서 숫자 두 개(a, b: float)를 받아 "
                    "두 숫자의 합(sum)과 곱(product)을 JSON으로 반환하는 "
                    "POST /calculate 엔드포인트를 Pydantic 스키마와 함께 작성하세요."
                ),
                "hint": (
                    "class CalcRequest(BaseModel): a: float, b: float | "
                    "class CalcResponse(BaseModel): sum: float, product: float | "
                    "@app.post('/calculate', response_model=CalcResponse)"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "학습된 사이킷런 모델을 model.joblib으로 저장하고, "
                    "이를 Docker 이미지로 패키징하는 Dockerfile을 작성하세요. "
                    "베이스 이미지는 python:3.11-slim, 포트는 8000, "
                    "시작 명령은 uvicorn main:app입니다."
                ),
                "hint": (
                    "FROM python:3.11-slim → WORKDIR /app → "
                    "COPY requirements.txt . → RUN pip install ... → "
                    "COPY main.py . → COPY model.joblib . → "
                    "EXPOSE 8000 → CMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                ),
            },
        ],
        "challenge": {
            "question": (
                "챕터 6의 MLflow 실험에서 Production 모델을 로드하여 "
                "완전한 모델 서빙 API를 구축하세요. 요구사항: "
                "1) MLflow Model Registry의 Production 스테이지 모델을 로드합니다. "
                "2) /predict (단건), /predict/batch (배치), /health 엔드포인트를 구현합니다. "
                "3) Pydantic으로 입력값을 검증하고 유효하지 않은 입력에 422 에러를 반환합니다. "
                "4) Dockerfile을 작성하여 이미지를 빌드하고 "
                "docker run으로 실행합니다. "
                "5) curl 또는 Python requests로 세 엔드포인트를 테스트하고 "
                "응답을 확인합니다."
            ),
            "hint": (
                "mlflow.sklearn.load_model('models:/모델명/Production')으로 모델을 로드합니다. "
                "Dockerfile에서 MLFLOW_TRACKING_URI 환경 변수를 설정하거나 "
                "모델을 미리 export(mlflow.sklearn.save_model)하여 파일로 포함시킵니다. "
                "lifespan 컨텍스트에서 모델을 로드하면 앱 시작 시 한 번만 로드됩니다."
            ),
        },
        "summary": [
            "모델 서빙은 학습된 모델을 HTTP API로 감싸 다른 서비스가 예측을 요청할 수 있게 하는 과정이다.",
            "joblib.dump/load로 사이킷런 모델을 파일로 저장하고, 전처리 파이프라인도 함께 저장하는 것이 좋다.",
            "FastAPI + Pydantic으로 입력 검증, 자동 문서화, 타입 안전성을 갖춘 ML 서빙 API를 빠르게 구축할 수 있다.",
            "모델은 앱 시작 시 lifespan에서 한 번만 로드하고 전역 저장소에 보관해야 응답 속도를 보장할 수 있다.",
            "Dockerfile로 서빙 서버를 컨테이너화하면 어떤 환경에서도 동일하게 실행 가능한 이식성을 확보한다.",
            "mlflow models serve 명령으로 코드 없이 MLflow 모델을 즉시 REST API로 서빙할 수 있다.",
        ],
    }
