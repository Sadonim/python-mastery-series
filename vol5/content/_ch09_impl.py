"""
Ch09 프로젝트 — 구현 세부 섹션 (FastAPI, Docker, 모니터링, 마무리 + 연습문제)
ch09_project.py에서 임포트하여 사용한다.
"""


def _section_fastapi() -> dict:
    """9.5 4단계: FastAPI 서빙 API 구축"""
    return {
        "title": "9.5 4단계: FastAPI 서빙 API 구축",
        "content": [
            (
                "Model Registry에 등록된 모델을 FastAPI로 서빙합니다. "
                "앱 시작 시 모델을 메모리에 로드하고, /predict 엔드포인트에서 "
                "JSON 입력을 받아 예측 결과를 반환합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/app/schema.py — Pydantic 요청/응답 스키마\n"
                    "from pydantic import BaseModel, Field\n"
                    "\n"
                    "\n"
                    "class PredictRequest(BaseModel):\n"
                    '    """예측 요청 스키마 — Iris 피처 4개를 입력받는다."""\n'
                    "    features: list[float] = Field(\n"
                    "        ...,\n"
                    "        min_length=4,\n"
                    "        max_length=4,\n"
                    "        description='[꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비] (cm)',\n"
                    "    )\n"
                    "\n"
                    "\n"
                    "class PredictResponse(BaseModel):\n"
                    '    """예측 응답 스키마"""\n'
                    "    predicted_class: int\n"
                    "    predicted_label: str\n"
                    "    probabilities: dict[str, float] | None = None\n"
                    "    model_version: str\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/app/predictor.py — MLflow 모델 로드 & 예측 로직\n"
                    "import mlflow.pyfunc\n"
                    "import numpy as np\n"
                    "from src.register import REGISTRY_MODEL_NAME\n"
                    "\n"
                    "\n"
                    "class ModelPredictor:\n"
                    '    """MLflow Registry에서 모델을 로드하고 예측을 수행한다."""\n'
                    "\n"
                    "    TARGET_NAMES = ['setosa', 'versicolor', 'virginica']  # Iris 기준\n"
                    "\n"
                    "    def __init__(self) -> None:\n"
                    "        self._model = None\n"
                    "        self._version = 'unknown'\n"
                    "\n"
                    "    def load(self) -> None:\n"
                    '        """Production 모델을 로드한다. 앱 시작 시 1회 호출."""\n'
                    "        model_uri = f'models:/{REGISTRY_MODEL_NAME}@production'\n"
                    "        self._model = mlflow.pyfunc.load_model(model_uri)\n"
                    "        self._version = REGISTRY_MODEL_NAME\n"
                    "        print(f'모델 로드 완료: {model_uri}')\n"
                    "\n"
                    "    def predict(self, features: list[float]) -> dict:\n"
                    '        """피처 리스트를 받아 예측 결과를 반환한다."""\n'
                    "        if self._model is None:\n"
                    "            raise RuntimeError('모델이 로드되지 않았습니다. load()를 먼저 호출하세요.')\n"
                    "        X = np.array([features])\n"
                    "        predicted_class = int(self._model.predict(X)[0])\n"
                    "        return {\n"
                    "            'predicted_class': predicted_class,\n"
                    "            'predicted_label': self.TARGET_NAMES[predicted_class],\n"
                    "            'model_version': self._version,\n"
                    "        }\n"
                    "\n"
                    "\n"
                    "# 앱 전역에서 공유하는 싱글턴 예측기\n"
                    "predictor = ModelPredictor()\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/app/main.py — FastAPI 앱\n"
                    "from contextlib import asynccontextmanager\n"
                    "from fastapi import FastAPI, HTTPException\n"
                    "from src.app.schema import PredictRequest, PredictResponse\n"
                    "from src.app.predictor import predictor\n"
                    "import logging\n"
                    "import time\n"
                    "\n"
                    "logger = logging.getLogger(__name__)\n"
                    "logging.basicConfig(level=logging.INFO)\n"
                    "\n"
                    "\n"
                    "@asynccontextmanager\n"
                    "async def lifespan(app: FastAPI):\n"
                    '    """앱 시작 시 모델 로드, 종료 시 정리."""\n'
                    "    predictor.load()\n"
                    "    yield\n"
                    "\n"
                    "\n"
                    "app = FastAPI(\n"
                    "    title='Iris 분류 ML API',\n"
                    "    description='MLflow Registry에서 로드한 모델로 Iris 품종을 예측합니다.',\n"
                    "    version='1.0.0',\n"
                    "    lifespan=lifespan,\n"
                    ")\n"
                    "\n"
                    "\n"
                    "@app.get('/health')\n"
                    "async def health_check() -> dict:\n"
                    '    """서버 상태 확인 엔드포인트"""\n'
                    "    return {'status': 'ok', 'model_loaded': predictor._model is not None}\n"
                    "\n"
                    "\n"
                    "@app.post('/predict', response_model=PredictResponse)\n"
                    "async def predict(request: PredictRequest) -> PredictResponse:\n"
                    '    """Iris 피처를 입력받아 품종을 예측한다."""\n'
                    "    start = time.time()\n"
                    "    try:\n"
                    "        result = predictor.predict(request.features)\n"
                    "        latency_ms = (time.time() - start) * 1000\n"
                    "        logger.info(\n"
                    "            f'PREDICT | features={request.features} | '\n"
                    "            f'class={result[\"predicted_label\"]} | latency={latency_ms:.1f}ms'\n"
                    "        )\n"
                    "        return PredictResponse(**result)\n"
                    "    except Exception as e:\n"
                    "        logger.error(f'예측 오류: {e}')\n"
                    "        raise HTTPException(status_code=500, detail=str(e))\n"
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 서버 실행\n"
                    "uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload\n"
                    "\n"
                    "# 예측 테스트 (Iris setosa 샘플)\n"
                    "curl -X POST http://localhost:8000/predict \\\n"
                    "     -H 'Content-Type: application/json' \\\n"
                    "     -d '{\"features\": [5.1, 3.5, 1.4, 0.2]}'\n"
                    "\n"
                    "# 응답 예시\n"
                    "# {\"predicted_class\": 0, \"predicted_label\": \"setosa\",\n"
                    "#  \"probabilities\": null, \"model_version\": \"iris-best-model\"}\n"
                ),
            },
        ],
    }


def _section_docker() -> dict:
    """9.6 5단계: Docker 컨테이너화 & docker-compose"""
    return {
        "title": "9.6 5단계: Docker 컨테이너화 & docker-compose",
        "content": [
            (
                "FastAPI 서버와 MLflow 서버를 각각 Docker 컨테이너로 패키징하고, "
                "docker-compose로 한 번에 실행합니다. "
                "컨테이너간 통신은 Docker 네트워크를 통해 이루어집니다."
            ),
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# Dockerfile — FastAPI + MLflow 모델 서빙\n"
                    "FROM python:3.11-slim\n"
                    "\n"
                    "WORKDIR /app\n"
                    "\n"
                    "# 의존성 설치 (레이어 캐싱 최적화)\n"
                    "COPY requirements.txt .\n"
                    "RUN pip install --no-cache-dir -r requirements.txt\n"
                    "\n"
                    "# 앱 코드 복사\n"
                    "COPY src/ ./src/\n"
                    "COPY mlruns/ ./mlruns/\n"
                    "\n"
                    "# 포트 노출 및 실행 명령\n"
                    "EXPOSE 8000\n"
                    "CMD [\"uvicorn\", \"src.app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n"
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# docker-compose.yml — FastAPI + MLflow 함께 실행\n"
                    "version: '3.9'\n"
                    "\n"
                    "services:\n"
                    "  mlflow:\n"
                    "    image: python:3.11-slim\n"
                    "    command: >\n"
                    "      bash -c 'pip install mlflow && mlflow server\n"
                    "      --host 0.0.0.0 --port 5000\n"
                    "      --backend-store-uri /mlruns\n"
                    "      --default-artifact-root /mlruns'\n"
                    "    ports:\n"
                    "      - '5000:5000'\n"
                    "    volumes:\n"
                    "      - ./mlruns:/mlruns\n"
                    "    healthcheck:\n"
                    "      test: ['CMD', 'curl', '-f', 'http://localhost:5000/health']\n"
                    "      interval: 10s\n"
                    "      retries: 5\n"
                    "\n"
                    "  api:\n"
                    "    build: .\n"
                    "    ports:\n"
                    "      - '8000:8000'\n"
                    "    environment:\n"
                    "      - MLFLOW_TRACKING_URI=http://mlflow:5000\n"
                    "    volumes:\n"
                    "      - ./mlruns:/app/mlruns\n"
                    "    depends_on:\n"
                    "      mlflow:\n"
                    "        condition: service_healthy\n"
                    "\n"
                    "networks:\n"
                    "  default:\n"
                    "    name: ml-pipeline-network\n"
                ),
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 실행 절차\n"
                    "\n"
                    "# 1. 학습 및 모델 등록 (로컬에서 먼저 실행)\n"
                    "python -m src.train\n"
                    "python -m src.register\n"
                    "\n"
                    "# 2. Docker 이미지 빌드 & 전체 스택 실행\n"
                    "docker compose up --build\n"
                    "\n"
                    "# 3. 서비스 확인\n"
                    "curl http://localhost:8000/health\n"
                    "curl http://localhost:5000/health  # MLflow 서버\n"
                    "\n"
                    "# 4. 종료\n"
                    "docker compose down\n"
                ),
            },
            {
                "type": "warning",
                "text": (
                    "mlruns/ 디렉터리를 볼륨으로 마운트해야 컨테이너 안에서 "
                    "로컬에서 학습한 모델을 참조할 수 있습니다. "
                    "볼륨 없이 빌드하면 COPY로 복사된 스냅샷만 사용되어 "
                    "모델 업데이트가 반영되지 않습니다."
                ),
            },
        ],
    }


def _section_monitoring() -> dict:
    """9.7 6단계: 모니터링 지표 추가"""
    return {
        "title": "9.7 6단계: 모니터링 지표 추가",
        "content": [
            (
                "모델을 배포한 뒤에는 예측 결과와 입력 분포를 지속적으로 모니터링해야 합니다. "
                "간단한 구조화 로그로 응답 시간, 예측 분포, 입력 통계를 기록하고, "
                "Evidently AI를 이용한 데이터 드리프트 감지 패턴도 확인합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/app/monitor.py — 예측 로그 기록 & 드리프트 감지 준비\n"
                    "import json\n"
                    "import logging\n"
                    "import time\n"
                    "from collections import defaultdict\n"
                    "from dataclasses import dataclass, field, asdict\n"
                    "from datetime import datetime\n"
                    "\n"
                    "logger = logging.getLogger('ml_monitor')\n"
                    "\n"
                    "\n"
                    "@dataclass\n"
                    "class PredictionLog:\n"
                    '    """단일 예측 이벤트 로그 레코드"""\n'
                    "    timestamp: str\n"
                    "    features: list[float]\n"
                    "    predicted_class: int\n"
                    "    predicted_label: str\n"
                    "    latency_ms: float\n"
                    "    model_version: str\n"
                    "\n"
                    "\n"
                    "class PredictionMonitor:\n"
                    '    """예측 로그를 수집하고 기본 통계를 제공한다."""\n'
                    "\n"
                    "    def __init__(self) -> None:\n"
                    "        self._logs: list[PredictionLog] = []\n"
                    "        self._class_counts: dict[str, int] = defaultdict(int)\n"
                    "\n"
                    "    def record(\n"
                    "        self,\n"
                    "        features: list[float],\n"
                    "        predicted_class: int,\n"
                    "        predicted_label: str,\n"
                    "        latency_ms: float,\n"
                    "        model_version: str,\n"
                    "    ) -> None:\n"
                    '        """예측 결과를 로그에 기록한다."""\n'
                    "        log = PredictionLog(\n"
                    "            timestamp=datetime.utcnow().isoformat(),\n"
                    "            features=list(features),  # 불변 복사본 저장\n"
                    "            predicted_class=predicted_class,\n"
                    "            predicted_label=predicted_label,\n"
                    "            latency_ms=latency_ms,\n"
                    "            model_version=model_version,\n"
                    "        )\n"
                    "        self._logs.append(log)\n"
                    "        self._class_counts[predicted_label] += 1\n"
                    "\n"
                    "        # 구조화 JSON 로그 출력 (로그 수집 시스템과 연동 가능)\n"
                    "        logger.info(json.dumps(asdict(log)))\n"
                    "\n"
                    "    def get_stats(self) -> dict:\n"
                    '        """수집된 로그의 요약 통계를 반환한다."""\n'
                    "        if not self._logs:\n"
                    "            return {'total_predictions': 0}\n"
                    "\n"
                    "        latencies = [log.latency_ms for log in self._logs]\n"
                    "        return {\n"
                    "            'total_predictions': len(self._logs),\n"
                    "            'avg_latency_ms': sum(latencies) / len(latencies),\n"
                    "            'max_latency_ms': max(latencies),\n"
                    "            'class_distribution': dict(self._class_counts),\n"
                    "        }\n"
                    "\n"
                    "\n"
                    "# 앱 전역 모니터 싱글턴\n"
                    "monitor = PredictionMonitor()\n"
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/app/main.py 수정 — /metrics 엔드포인트 추가\n"
                    "from src.app.monitor import monitor\n"
                    "\n"
                    "\n"
                    "@app.post('/predict', response_model=PredictResponse)\n"
                    "async def predict(request: PredictRequest) -> PredictResponse:\n"
                    "    start = time.time()\n"
                    "    result = predictor.predict(request.features)\n"
                    "    latency_ms = (time.time() - start) * 1000\n"
                    "\n"
                    "    # 모니터링 기록\n"
                    "    monitor.record(\n"
                    "        features=request.features,\n"
                    "        predicted_class=result['predicted_class'],\n"
                    "        predicted_label=result['predicted_label'],\n"
                    "        latency_ms=latency_ms,\n"
                    "        model_version=result['model_version'],\n"
                    "    )\n"
                    "    return PredictResponse(**result)\n"
                    "\n"
                    "\n"
                    "@app.get('/metrics')\n"
                    "async def get_metrics() -> dict:\n"
                    '    """수집된 예측 통계를 반환한다."""\n'
                    "    return monitor.get_stats()\n"
                ),
            },
            {
                "type": "table",
                "headers": ["모니터링 항목", "수집 방법", "경보 기준 예시", "대응"],
                "rows": [
                    ["응답 지연시간", "time.time() 측정", "평균 500ms 초과", "모델 경량화 또는 스케일 아웃"],
                    ["예측 분포 변화", "클래스별 카운트 추적", "특정 클래스 비율 2배 증가", "데이터 드리프트 점검"],
                    ["입력 피처 분포", "Evidently AI", "PSI 0.2 초과", "모델 재학습 검토"],
                    ["오류율", "exception 카운트", "5% 초과", "버그 수정 또는 롤백"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "실무에서는 Prometheus + Grafana로 지표를 시각화합니다. "
                    "prometheus-fastapi-instrumentator 라이브러리를 설치하면 "
                    "FastAPI 앱에 /metrics 엔드포인트가 자동으로 추가되어 "
                    "Prometheus가 수집할 수 있는 형식으로 지표를 제공합니다."
                ),
            },
        ],
    }


def _section_wrapup() -> dict:
    """9.8 프로젝트 마무리 & 확장 방향"""
    return {
        "title": "9.8 프로젝트 마무리 & 확장 방향",
        "content": [
            "축하합니다! 엔드투엔드 ML 파이프라인을 완성했습니다. 지금까지 만든 것을 정리해 봅시다.",
            {
                "type": "table",
                "headers": ["단계", "구현 내용", "핵심 도구", "상태"],
                "rows": [
                    ["1. 데이터", "EDA + 전처리 Pipeline", "pandas, scikit-learn", "완료"],
                    ["2. 학습", "다중 모델 학습 + 실험 로깅", "MLflow Tracking", "완료"],
                    ["3. Registry", "최적 모델 등록 + Production 전환", "MLflow Registry", "완료"],
                    ["4. 서빙", "/predict API 구축", "FastAPI, Pydantic", "완료"],
                    ["5. 배포", "컨테이너화 + 멀티 서비스", "Docker, docker-compose", "완료"],
                    ["6. 모니터링", "지연시간 + 예측 분포 로깅", "구조화 로그, /metrics", "완료"],
                ],
            },
            "**다음 단계로 도전할 수 있는 확장 방향:**",
            {
                "type": "bullet_list",
                "items": [
                    "CI/CD 자동화: GitHub Actions로 코드 푸시 시 자동 학습 → 등록 → 배포",
                    "피처 스토어: Feast 또는 Hopsworks로 피처를 중앙 관리",
                    "A/B 테스트: 두 모델을 동시에 배포하고 트래픽을 분할하여 성능 비교",
                    "배치 예측: Airflow DAG으로 정기적으로 대량 데이터 예측",
                    "딥러닝 모델 적용: PyTorch 모델을 MLflow로 관리하고 ONNX로 최적화",
                ],
            },
        ],
    }


EXERCISES = [
    {
        "id": 1,
        "type": "code",
        "question": (
            "Wine 데이터셋으로 전환하여 전체 파이프라인을 재실행하세요. "
            "load_dataset('wine')을 사용하고, EXPERIMENT_NAME을 'wine-classification'으로 변경합니다. "
            "어떤 모델이 가장 높은 accuracy를 달성하는지 확인하세요."
        ),
        "hint": "피처 수가 Iris(4개) → Wine(13개)로 늘어납니다. train.py의 EXPERIMENT_NAME 상수와 eda.py의 load_dataset 호출만 변경하면 됩니다.",
        "answer": (
            "# src/train.py 상단 수정\n"
            "EXPERIMENT_NAME = 'wine-classification'\n"
            "\n"
            "# 실행\n"
            "# python -m src.train  (dataset_name='wine' 인자 전달)\n"
            "# run_experiments('wine') 호출 시 자동으로 Wine 데이터 사용\n"
            "\n"
            "# schema.py 수정: features 길이 4 -> 13\n"
            "features: list[float] = Field(..., min_length=13, max_length=13)\n"
        ),
    },
    {
        "id": 2,
        "type": "code",
        "question": (
            "/predict 엔드포인트에 입력 검증을 강화하세요. "
            "피처 값이 음수이거나 100을 초과하면 422 오류를 반환해야 합니다. "
            "Pydantic Field의 ge(이상), le(이하) 제약을 활용하세요."
        ),
        "hint": "Field(ge=0, le=100)을 features의 각 원소에 적용하려면 Annotated 타입 또는 validator를 사용합니다.",
        "answer": (
            "from pydantic import BaseModel, Field, field_validator\n"
            "from typing import Annotated\n"
            "\n"
            "FeatureValue = Annotated[float, Field(ge=0.0, le=100.0)]\n"
            "\n"
            "class PredictRequest(BaseModel):\n"
            "    features: list[FeatureValue] = Field(\n"
            "        ..., min_length=4, max_length=4\n"
            "    )\n"
        ),
    },
    {
        "id": 3,
        "type": "short_answer",
        "question": (
            "MLflow Model Registry에서 'Staging'과 'Production' 단계의 차이점은 무엇인가요? "
            "실무에서 두 단계를 어떻게 활용하면 좋을지 설명하세요."
        ),
        "answer": (
            "Staging은 통합 테스트, A/B 테스트, 성능 검증을 위한 준비 단계입니다. "
            "Production은 실서비스에 투입된 상태로, API 서버가 이 모델을 로드합니다. "
            "실무 패턴: (1) 새 모델 학습 후 Staging 등록 → "
            "(2) 통합 테스트 통과 시 Production 전환 → "
            "(3) 이전 Production은 Archived로 보존. "
            "이 흐름으로 롤백이 언제든 가능합니다."
        ),
    },
]

CHALLENGE = {
    "title": "도전 과제: GitHub Actions로 CI/CD 파이프라인 구성",
    "description": (
        ".github/workflows/ml-pipeline.yml을 작성하여 "
        "main 브랜치에 푸시할 때마다 자동으로 모델을 재학습하고 API를 재배포하는 "
        "CI/CD 파이프라인을 구성하세요."
    ),
    "requirements": [
        "on: push: branches: [main] 트리거 설정",
        "python -m src.train 실행 후 accuracy가 0.90 미만이면 실패 처리",
        "python -m src.register 실행으로 최적 모델 자동 등록",
        "docker compose up --build -d 로 서비스 재시작",
        "curl http://localhost:8000/health 로 배포 확인",
    ],
    "hint": (
        "jobs.train.outputs를 활용하면 학습 단계의 accuracy를 다음 단계로 전달할 수 있습니다. "
        "mlflow run 결과를 파싱하거나 별도 JSON 파일로 지표를 저장한 뒤 읽어오세요."
    ),
}

SUMMARY = {
    "title": "Chapter 9 요약 — 엔드투엔드 ML 파이프라인",
    "points": [
        "EDA → Pipeline 구성 → MLflow 실험 → Registry → FastAPI → Docker → Monitor 6단계 완성",
        "MLflow Tracking으로 하이퍼파라미터, 지표, 모델을 체계적으로 관리한다",
        "Model Registry의 Production alias로 API 서버와 모델을 느슨하게 결합한다",
        "FastAPI lifespan으로 앱 시작 시 모델을 1회 로드하여 예측 지연을 최소화한다",
        "Docker Compose로 MLflow 서버와 API 서버를 함께 실행하고 헬스체크로 순서를 보장한다",
        "구조화 로그와 /metrics 엔드포인트로 서빙 후 모니터링 기반을 마련한다",
    ],
}
