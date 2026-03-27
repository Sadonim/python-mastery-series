"""
Chapter 9: 미니 프로젝트 — 엔드투엔드 ML 파이프라인
Iris/Wine 분류기를 MLflow로 실험 관리하고, FastAPI로 서빙한 뒤
Docker 컨테이너로 배포하는 완전한 MLOps 파이프라인을 구축한다.

섹션 4~6 및 연습문제는 _ch09_impl.py에 분리 정의되어 있다.
"""
from content._ch09_impl import (
    CHALLENGE,
    EXERCISES,
    SUMMARY,
    _section_fastapi,
    _section_docker,
    _section_monitoring,
    _section_wrapup,
)


def get_chapter():
    return {
        "number": 9,
        "title": "미니 프로젝트 — 엔드투엔드 ML 파이프라인",
        "subtitle": "Data → Train → MLflow → FastAPI → Docker → Monitor",
        "big_picture": (
            "Ch 1~8에서 배운 사이킷런, MLflow, FastAPI, Docker를 하나의 완결된 프로젝트에 통합합니다. "
            "Iris/Wine 데이터셋 분류기를 예시로 '데이터 탐색 → 모델 학습 → 실험 추적 → "
            "모델 레지스트리 → API 서빙 → 컨테이너화 → 모니터링' 전 과정을 직접 경험합니다. "
            "각 단계가 다음 단계의 입력이 되는 실전 MLOps 사고방식을 익히는 것이 핵심입니다."
        ),
        "sections": [
            _section_overview(),
            _section_eda(),
            _section_training(),
            _section_registry(),
            _section_fastapi(),
            _section_docker(),
            _section_monitoring(),
            _section_wrapup(),
        ],
        "exercises": EXERCISES,
        "challenge": CHALLENGE,
        "summary": SUMMARY,
    }


def _section_overview() -> dict:
    """9.1 프로젝트 개요 & 전체 아키텍처"""
    return {
        "title": "9.1 프로젝트 개요 & 전체 아키텍처",
        "content": [
            (
                "이번 프로젝트는 **엔드투엔드 ML 파이프라인**입니다. "
                "공개 데이터셋(Iris 또는 Wine)으로 분류 모델을 학습하고, "
                "MLflow로 실험을 추적한 뒤 최적 모델을 Model Registry에 등록합니다. "
                "등록된 모델을 FastAPI로 서빙하고, Docker로 컨테이너화하여 배포합니다. "
                "마지막으로 예측 지연시간과 입력 분포 변화를 모니터링합니다."
            ),
            {
                "type": "flow_diagram",
                "title": "엔드투엔드 ML 파이프라인 — 전체 아키텍처",
                "direction": "horizontal",
                "nodes": [
                    {"label": "1. 데이터", "sub": "EDA / 전처리 / Pipeline"},
                    {"label": "2. 학습", "sub": "RandomForest / SVM / MLflow 로깅"},
                    {"label": "3. Registry", "sub": "최적 모델 등록 / Staging"},
                    {"label": "4. FastAPI", "sub": "/predict 엔드포인트"},
                    {"label": "5. Docker", "sub": "Dockerfile / docker-compose"},
                    {"label": "6. Monitor", "sub": "지연시간 / 드리프트 감지"},
                ],
                "note": "각 단계는 독립적으로 실행 가능하며, MLflow가 학습~서빙을 연결하는 허브 역할을 합니다.",
            },
            "**프로젝트 요구사항:**",
            {
                "type": "numbered_list",
                "items": [
                    "Iris 또는 Wine 데이터셋으로 2개 이상의 모델을 학습하고 MLflow에 로깅한다",
                    "MLflow Model Registry에 최적 모델을 'Production' 단계로 등록한다",
                    "FastAPI로 /predict 엔드포인트를 구축하여 JSON 입력을 받아 예측 결과를 반환한다",
                    "Dockerfile + docker-compose.yml로 FastAPI 서버와 MLflow 서버를 함께 실행한다",
                    "응답 시간, 예측 결과, 입력 피처 분포를 로그로 기록한다",
                ],
            },
            "**프로젝트 디렉터리 구조:**",
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "ml-pipeline/\n"
                    "├── data/                  # 데이터셋 (자동 다운로드)\n"
                    "├── notebooks/             # EDA 노트북 (선택)\n"
                    "├── src/\n"
                    "│   ├── train.py           # 모델 학습 & MLflow 로깅\n"
                    "│   ├── register.py        # 최적 모델 Registry 등록\n"
                    "│   ├── app/\n"
                    "│   │   ├── main.py        # FastAPI 앱\n"
                    "│   │   ├── schema.py      # Pydantic 스키마\n"
                    "│   │   └── predictor.py   # MLflow 모델 로드 & 예측\n"
                    "├── Dockerfile\n"
                    "├── docker-compose.yml\n"
                    "├── requirements.txt\n"
                    "└── mlruns/                # MLflow 실험 데이터 (자동 생성)\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "MLflow 서버를 별도로 실행하지 않아도 됩니다. "
                    "기본 설정(mlflow.set_tracking_uri('mlruns'))은 로컬 파일 시스템에 기록하므로 "
                    "설치 후 즉시 시작할 수 있습니다."
                ),
            },
        ],
    }


def _section_eda() -> dict:
    """9.2 1단계: 데이터 탐색 및 전처리"""
    return {
        "title": "9.2 1단계: 데이터 탐색 및 전처리",
        "content": [
            (
                "좋은 모델의 출발점은 데이터를 이해하는 것입니다. "
                "EDA(탐색적 데이터 분석)로 결측값, 피처 분포, 클래스 불균형을 확인하고, "
                "사이킷런 Pipeline으로 전처리를 모델과 묶어 재사용성을 높입니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/eda.py — 데이터 탐색 및 전처리 Pipeline 구성\n"
                    "import pandas as pd\n"
                    "import numpy as np\n"
                    "from sklearn.datasets import load_iris, load_wine\n"
                    "from sklearn.model_selection import train_test_split\n"
                    "from sklearn.pipeline import Pipeline\n"
                    "from sklearn.preprocessing import StandardScaler\n"
                    "from sklearn.impute import SimpleImputer\n"
                    "\n"
                    "\n"
                    "def load_dataset(name: str = 'iris') -> tuple:\n"
                    '    """데이터셋을 로드하고 DataFrame으로 반환한다."""\n'
                    "    loaders = {'iris': load_iris, 'wine': load_wine}\n"
                    "    if name not in loaders:\n"
                    "        raise ValueError(f'지원하지 않는 데이터셋: {name}. 선택: {list(loaders)}')\n"
                    "\n"
                    "    dataset = loaders[name]()\n"
                    "    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)\n"
                    "    df['target'] = dataset.target\n"
                    "    df['target_name'] = [dataset.target_names[t] for t in dataset.target]\n"
                    "    return df, dataset.target_names.tolist()\n"
                    "\n"
                    "\n"
                    "def explore_dataset(df: pd.DataFrame) -> dict:\n"
                    '    """기본 EDA 정보를 반환한다."""\n'
                    "    return {\n"
                    "        'shape': df.shape,\n"
                    "        'dtypes': df.dtypes.to_dict(),\n"
                    "        'missing': df.isnull().sum().to_dict(),\n"
                    "        'class_distribution': df['target'].value_counts().to_dict(),\n"
                    "        'describe': df.describe().to_dict(),\n"
                    "    }\n"
                    "\n"
                    "\n"
                    "def build_preprocessor() -> Pipeline:\n"
                    '    """결측값 처리 + 표준화 Pipeline을 반환한다."""\n'
                    "    return Pipeline([\n"
                    "        ('imputer', SimpleImputer(strategy='mean')),  # 결측값 → 평균\n"
                    "        ('scaler', StandardScaler()),                 # 표준화\n"
                    "    ])\n"
                    "\n"
                    "\n"
                    "def split_data(\n"
                    "    df: pd.DataFrame,\n"
                    "    test_size: float = 0.2,\n"
                    "    random_state: int = 42,\n"
                    ") -> tuple:\n"
                    '    """피처/타겟 분리 후 학습/검증 데이터로 분할한다."""\n'
                    "    feature_cols = [c for c in df.columns if c not in ('target', 'target_name')]\n"
                    "    X = df[feature_cols].values\n"
                    "    y = df['target'].values\n"
                    "    return train_test_split(X, y, test_size=test_size, random_state=random_state,\n"
                    "                            stratify=y)\n"
                    "\n"
                    "\n"
                    "if __name__ == '__main__':\n"
                    "    df, target_names = load_dataset('iris')\n"
                    "    info = explore_dataset(df)\n"
                    "    print(f'데이터 크기: {info[\"shape\"]}')\n"
                    "    print(f'결측값: {info[\"missing\"]}')\n"
                    "    print(f'클래스 분포: {info[\"class_distribution\"]}')\n"
                ),
            },
            {
                "type": "note",
                "text": (
                    "사이킷런 Pipeline은 전처리와 모델을 하나의 객체로 묶습니다. "
                    "덕분에 학습 시 fit()을 한 번만 호출하면 전처리와 모델 학습이 순서대로 실행되고, "
                    "예측 시 transform()과 predict()가 자동으로 연결됩니다."
                ),
            },
        ],
    }


def _section_training() -> dict:
    """9.3 2단계: 모델 학습 & MLflow 실험 로깅"""
    return {
        "title": "9.3 2단계: 모델 학습 & MLflow 실험 로깅",
        "content": [
            (
                "여러 모델을 학습하고 MLflow에 하이퍼파라미터, 지표, 모델 파일을 기록합니다. "
                "각 실험은 Run으로 관리되며, MLflow UI에서 결과를 비교할 수 있습니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/train.py — 모델 학습 & MLflow 실험 로깅\n"
                    "import mlflow\n"
                    "import mlflow.sklearn\n"
                    "import numpy as np\n"
                    "from sklearn.ensemble import RandomForestClassifier\n"
                    "from sklearn.svm import SVC\n"
                    "from sklearn.metrics import accuracy_score, f1_score, classification_report\n"
                    "from sklearn.pipeline import Pipeline\n"
                    "from src.eda import load_dataset, build_preprocessor, split_data\n"
                    "\n"
                    "\n"
                    "# MLflow 실험 이름 설정\n"
                    "EXPERIMENT_NAME = 'iris-classification'\n"
                    "\n"
                    "\n"
                    "def train_model(\n"
                    "    model_name: str,\n"
                    "    model,\n"
                    "    X_train: np.ndarray,\n"
                    "    X_test: np.ndarray,\n"
                    "    y_train: np.ndarray,\n"
                    "    y_test: np.ndarray,\n"
                    ") -> dict:\n"
                    '    """단일 모델을 학습하고 MLflow에 로깅한다."""\n'
                    "    preprocessor = build_preprocessor()\n"
                    "    pipeline = Pipeline([\n"
                    "        ('preprocessor', preprocessor),\n"
                    "        ('classifier', model),\n"
                    "    ])\n"
                    "\n"
                    "    with mlflow.start_run(run_name=model_name) as run:\n"
                    "        # 모델 파라미터 로깅\n"
                    "        mlflow.log_params(model.get_params())\n"
                    "        mlflow.log_param('model_type', model_name)\n"
                    "\n"
                    "        # 학습\n"
                    "        pipeline.fit(X_train, y_train)\n"
                    "        y_pred = pipeline.predict(X_test)\n"
                    "\n"
                    "        # 지표 계산 & 로깅\n"
                    "        acc = accuracy_score(y_test, y_pred)\n"
                    "        f1 = f1_score(y_test, y_pred, average='weighted')\n"
                    "        mlflow.log_metric('accuracy', acc)\n"
                    "        mlflow.log_metric('f1_weighted', f1)\n"
                    "\n"
                    "        # 모델 아티팩트 저장\n"
                    "        mlflow.sklearn.log_model(\n"
                    "            pipeline,\n"
                    "            artifact_path='model',\n"
                    "            registered_model_name=f'{EXPERIMENT_NAME}-{model_name}',\n"
                    "        )\n"
                    "\n"
                    "        print(f'[{model_name}] accuracy={acc:.4f}, f1={f1:.4f}')\n"
                    "        return {\n"
                    "            'run_id': run.info.run_id,\n"
                    "            'model_name': model_name,\n"
                    "            'accuracy': acc,\n"
                    "            'f1': f1,\n"
                    "        }\n"
                    "\n"
                    "\n"
                    "def run_experiments(dataset_name: str = 'iris') -> list[dict]:\n"
                    '    """여러 모델을 실험하고 결과를 반환한다."""\n'
                    "    mlflow.set_experiment(EXPERIMENT_NAME)\n"
                    "\n"
                    "    df, _ = load_dataset(dataset_name)\n"
                    "    X_train, X_test, y_train, y_test = split_data(df)\n"
                    "\n"
                    "    # 비교할 모델 목록\n"
                    "    candidates = [\n"
                    "        ('RandomForest', RandomForestClassifier(n_estimators=100, random_state=42)),\n"
                    "        ('SVM-RBF', SVC(kernel='rbf', C=1.0, random_state=42)),\n"
                    "        ('SVM-Linear', SVC(kernel='linear', C=0.5, random_state=42)),\n"
                    "    ]\n"
                    "\n"
                    "    results = []\n"
                    "    for name, model in candidates:\n"
                    "        result = train_model(name, model, X_train, X_test, y_train, y_test)\n"
                    "        results.append(result)\n"
                    "\n"
                    "    return results\n"
                    "\n"
                    "\n"
                    "if __name__ == '__main__':\n"
                    "    results = run_experiments('iris')\n"
                    "    best = max(results, key=lambda r: r['accuracy'])\n"
                    "    print(f'\\n최고 모델: {best[\"model_name\"]} (accuracy={best[\"accuracy\"]:.4f})')\n"
                    "    print('MLflow UI: mlflow ui --host 0.0.0.0 --port 5000')\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "mlflow ui 명령으로 브라우저에서 실험 결과를 비교할 수 있습니다. "
                    "Experiments 탭에서 실행별 지표를 표로 보거나, "
                    "차트로 하이퍼파라미터와 지표의 관계를 시각화할 수 있습니다."
                ),
            },
        ],
    }


def _section_registry() -> dict:
    """9.4 3단계: 최적 모델 선택 & Registry 등록"""
    return {
        "title": "9.4 3단계: 최적 모델 선택 & Registry 등록",
        "content": [
            (
                "실험 결과 중 가장 좋은 모델을 MLflow Model Registry에 등록합니다. "
                "Registry는 모델의 생애주기(Staging → Production → Archived)를 관리하는 중앙 저장소입니다. "
                "FastAPI 서버는 'Production' 단계의 모델을 자동으로 로드합니다."
            ),
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# src/register.py — 최적 모델 선택 & Registry 등록\n"
                    "import mlflow\n"
                    "from mlflow.tracking import MlflowClient\n"
                    "from src.train import EXPERIMENT_NAME\n"
                    "\n"
                    "\n"
                    "REGISTRY_MODEL_NAME = 'iris-best-model'\n"
                    "\n"
                    "\n"
                    "def find_best_run(metric: str = 'accuracy') -> dict:\n"
                    '    """실험에서 지정 지표가 가장 높은 Run을 반환한다."""\n'
                    "    client = MlflowClient()\n"
                    "    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)\n"
                    "    if experiment is None:\n"
                    "        raise RuntimeError(f'실험을 찾을 수 없습니다: {EXPERIMENT_NAME}')\n"
                    "\n"
                    "    runs = client.search_runs(\n"
                    "        experiment_ids=[experiment.experiment_id],\n"
                    "        order_by=[f'metrics.{metric} DESC'],\n"
                    "        max_results=1,\n"
                    "    )\n"
                    "    if not runs:\n"
                    "        raise RuntimeError('학습된 Run이 없습니다. train.py를 먼저 실행하세요.')\n"
                    "\n"
                    "    best = runs[0]\n"
                    "    return {\n"
                    "        'run_id': best.info.run_id,\n"
                    "        'accuracy': best.data.metrics.get('accuracy', 0),\n"
                    "        'model_uri': f'runs:/{best.info.run_id}/model',\n"
                    "    }\n"
                    "\n"
                    "\n"
                    "def register_best_model() -> str:\n"
                    '    """최적 Run의 모델을 Registry에 등록하고 Production으로 전환한다."""\n'
                    "    best = find_best_run()\n"
                    "    print(f'최적 Run: {best[\"run_id\"]} (accuracy={best[\"accuracy\"]:.4f})')\n"
                    "\n"
                    "    # Registry에 등록\n"
                    "    model_version = mlflow.register_model(\n"
                    "        model_uri=best['model_uri'],\n"
                    "        name=REGISTRY_MODEL_NAME,\n"
                    "    )\n"
                    "\n"
                    "    # Production 단계로 전환 (MLflow 2.x+ alias 방식)\n"
                    "    client = MlflowClient()\n"
                    "    client.set_registered_model_alias(\n"
                    "        name=REGISTRY_MODEL_NAME,\n"
                    "        alias='production',\n"
                    "        version=model_version.version,\n"
                    "    )\n"
                    "\n"
                    "    print(f'등록 완료: {REGISTRY_MODEL_NAME} v{model_version.version} -> production')\n"
                    "    return f'models:/{REGISTRY_MODEL_NAME}@production'\n"
                    "\n"
                    "\n"
                    "if __name__ == '__main__':\n"
                    "    model_uri = register_best_model()\n"
                    "    print(f'서빙 URI: {model_uri}')\n"
                ),
            },
            {
                "type": "table",
                "headers": ["단계", "의미", "전환 조건", "비고"],
                "rows": [
                    ["None", "등록 직후 상태", "자동", "버전 번호만 존재"],
                    ["Staging", "검증 중", "수동 승격", "통합 테스트 환경"],
                    ["Production", "실서비스 투입", "수동 승격", "API 서버가 이 단계 로드"],
                    ["Archived", "더 이상 사용 안 함", "수동 전환", "기록 보존"],
                ],
            },
            {
                "type": "note",
                "text": (
                    "MLflow 2.x부터는 Stage 대신 Alias(별칭) 방식을 권장합니다. "
                    "'production' alias를 지정하면 models:/모델명@production 형식으로 "
                    "버전 번호 없이 항상 최신 Production 모델을 로드할 수 있습니다."
                ),
            },
        ],
    }
