"""
부록 B: MLOps 도구 생태계
MLflow, Kubeflow, Airflow, DVC 등 주요 MLOps 도구를 비교하고,
모델 서빙, 모니터링, 성숙도 모델, 추천 학습 경로를 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 B: MLOps 도구 생태계",
        "sections": [
            _section_mlops_tools(),
            _section_serving_platforms(),
            _section_monitoring_tools(),
            _section_maturity_model(),
            _section_learning_path(),
        ],
    }


def _section_mlops_tools() -> dict:
    return {
        "title": "B.1 MLOps 도구 비교",
        "content": [
            (
                "MLOps는 ML 모델의 학습, 배포, 모니터링, 재학습을 자동화하는 실천 방식입니다. "
                "다양한 오픈소스 도구가 각 단계를 지원하며, 팀 규모와 인프라에 맞는 도구를 선택해야 합니다."
            ),
            {
                "type": "table",
                "headers": ["도구", "주요 기능", "장점", "단점", "적합한 규모"],
                "rows": [
                    [
                        "MLflow",
                        "실험 추적, 모델 레지스트리, 프로젝트 패키징, 모델 서빙",
                        "설치 간단, 다양한 프레임워크 지원, UI 직관적",
                        "대규모 파이프라인 오케스트레이션 기능 약함",
                        "개인 ~ 중소팀",
                    ],
                    [
                        "Kubeflow",
                        "ML 파이프라인 오케스트레이션, Kubernetes 기반 학습/서빙",
                        "Kubernetes 네이티브, 대규모 분산 학습 지원",
                        "Kubernetes 운영 지식 필수, 설정 복잡",
                        "대규모 조직",
                    ],
                    [
                        "Apache Airflow",
                        "데이터 파이프라인 스케줄링 & 오케스트레이션",
                        "범용 워크플로우, 풍부한 Operator, 커뮤니티 대형",
                        "ML 특화 기능 없음, 스트리밍 부적합",
                        "데이터 엔지니어링 중심팀",
                    ],
                    [
                        "DVC",
                        "데이터 버전 관리, 파이프라인 정의, 실험 비교",
                        "Git과 통합, 대용량 파일 추적, 재현성 보장",
                        "실시간 실험 추적 UI 없음, 학습 곡선",
                        "연구팀, 데이터 버전 중요 프로젝트",
                    ],
                    [
                        "ZenML",
                        "ML 파이프라인 프레임워크, 스택 추상화",
                        "클라우드/로컬 포터블 파이프라인, 현대적 API",
                        "생태계 상대적으로 작음, 신생 프로젝트",
                        "중소팀, 멀티클라우드",
                    ],
                    [
                        "Prefect",
                        "데이터 워크플로우 오케스트레이션",
                        "Python 코드 그대로 워크플로우화, UI 세련됨",
                        "Airflow 대비 생태계 작음",
                        "데이터 파이프라인 팀",
                    ],
                ],
            },
            {
                "type": "flow_diagram",
                "title": "MLOps 도구 조합 예시 (소규모 팀)",
                "direction": "horizontal",
                "nodes": [
                    {"label": "데이터 버전", "sub": "DVC"},
                    {"label": "실험 추적", "sub": "MLflow Tracking"},
                    {"label": "모델 저장소", "sub": "MLflow Registry"},
                    {"label": "파이프라인", "sub": "Airflow / Prefect"},
                    {"label": "서빙", "sub": "FastAPI + Docker"},
                    {"label": "모니터링", "sub": "Evidently + Grafana"},
                ],
                "note": "단계별로 점진적으로 도입하세요. MLflow부터 시작하여 팀이 성장하면 다른 도구를 추가합니다.",
            },
            {
                "type": "tip",
                "text": (
                    "처음 MLOps를 도입한다면 MLflow 하나로 시작하세요. "
                    "실험 추적, 모델 레지스트리, 기본 서빙까지 단일 도구로 커버 가능합니다. "
                    "팀이 성장하면 DVC(데이터 버전)와 Airflow(파이프라인)를 추가하세요."
                ),
            },
        ],
    }


def _section_serving_platforms() -> dict:
    return {
        "title": "B.2 모델 서빙 플랫폼 비교",
        "content": [
            (
                "학습된 모델을 API로 서빙하는 방법은 다양합니다. "
                "프레임워크, 트래픽 규모, 팀 역량에 따라 적합한 플랫폼이 달라집니다."
            ),
            {
                "type": "table",
                "headers": ["플랫폼", "특징", "지원 프레임워크", "장점", "단점"],
                "rows": [
                    [
                        "FastAPI + MLflow",
                        "직접 구현, 완전한 제어권",
                        "scikit-learn, PyTorch, TF 등 모두",
                        "유연성 최대, 커스터마이징 자유",
                        "인프라 관리 직접 필요",
                    ],
                    [
                        "BentoML",
                        "ML 특화 서빙 프레임워크",
                        "scikit-learn, PyTorch, TF, XGBoost",
                        "배치 추론, Docker 자동 생성, 간편 배포",
                        "BentoML 개념 학습 필요",
                    ],
                    [
                        "TorchServe",
                        "PyTorch 공식 서빙 도구",
                        "PyTorch 전용",
                        "PyTorch 최적화, 배치 처리, 멀티 모델",
                        "PyTorch 외 사용 불가",
                    ],
                    [
                        "TensorFlow Serving",
                        "TF/Keras 공식 서빙 도구",
                        "TensorFlow, Keras 전용",
                        "gRPC/REST 지원, 버전 관리 내장",
                        "TensorFlow 외 사용 불가",
                    ],
                    [
                        "Triton Inference Server",
                        "NVIDIA GPU 최적화 서빙",
                        "TF, PyTorch, ONNX, TensorRT",
                        "GPU 최적화, 고성능, 멀티 프레임워크",
                        "NVIDIA GPU 필수, 설정 복잡",
                    ],
                    [
                        "Ray Serve",
                        "분산 서빙, 멀티 모델 컴포지션",
                        "모든 프레임워크",
                        "수평 확장, 모델 체이닝, 동적 배포",
                        "Ray 클러스터 운영 지식 필요",
                    ],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# BentoML로 scikit-learn 모델 서빙 예시\n"
                    "import bentoml\n"
                    "from bentoml.io import NumpyNdarray, JSON\n"
                    "import numpy as np\n"
                    "\n"
                    "# 모델 저장 (학습 후 1회)\n"
                    "# bentoml.sklearn.save_model('iris_classifier', trained_pipeline)\n"
                    "\n"
                    "# 서비스 정의\n"
                    "iris_runner = bentoml.sklearn.get('iris_classifier:latest').to_runner()\n"
                    "\n"
                    "svc = bentoml.Service('iris_service', runners=[iris_runner])\n"
                    "\n"
                    "\n"
                    "@svc.api(input=NumpyNdarray(), output=JSON())\n"
                    "async def predict(input_data: np.ndarray) -> dict:\n"
                    '    """BentoML 비동기 예측 엔드포인트"""\n'
                    "    result = await iris_runner.predict.async_run(input_data)\n"
                    "    return {'predicted_class': int(result[0])}\n"
                    "\n"
                    "# 실행: bentoml serve service:svc --reload\n"
                    "# Docker: bentoml build && bentoml containerize iris_service:latest\n"
                ),
            },
            {
                "type": "note",
                "text": (
                    "이 시리즈에서는 FastAPI + MLflow 조합을 사용했습니다. "
                    "이 조합은 학습 부담이 적고 커스터마이징이 자유롭습니다. "
                    "프로덕션 규모로 성장하면 BentoML이나 Ray Serve 도입을 검토하세요."
                ),
            },
        ],
    }


def _section_monitoring_tools() -> dict:
    return {
        "title": "B.3 모니터링 도구 비교",
        "content": [
            (
                "모델 배포 후 성능 저하와 데이터 드리프트를 감지하는 것이 MLOps의 핵심 과제입니다. "
                "서비스 모니터링(인프라)과 모델 모니터링(ML 특화)은 다른 도구가 필요합니다."
            ),
            {
                "type": "table",
                "headers": ["도구", "유형", "주요 기능", "설정 난이도", "비용"],
                "rows": [
                    [
                        "Evidently AI",
                        "ML 특화 모니터링",
                        "데이터 드리프트, 모델 성능 저하, 데이터 품질 리포트",
                        "낮음 (Python 코드 몇 줄)",
                        "오픈소스",
                    ],
                    [
                        "Whylabs",
                        "ML 특화 모니터링 (SaaS)",
                        "실시간 데이터 프로파일링, 이상 감지, 알림",
                        "낮음 (whylogs 라이브러리)",
                        "무료 티어 + 유료",
                    ],
                    [
                        "Prometheus + Grafana",
                        "인프라/서비스 모니터링",
                        "지연시간, 처리량, 오류율, 사용자 정의 지표",
                        "중간 (yaml 설정 필요)",
                        "오픈소스",
                    ],
                    [
                        "Arize AI",
                        "ML 옵저버빌리티 플랫폼",
                        "피처 드리프트, 예측 품질, 설명 가능성",
                        "낮음 (SDK 연동)",
                        "유료 (개발자 무료)",
                    ],
                    [
                        "Fiddler AI",
                        "ML 모니터링 & 설명 가능성",
                        "드리프트, 공정성, 모델 설명, 알림",
                        "중간",
                        "유료",
                    ],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# Evidently AI로 데이터 드리프트 감지 예시\n"
                    "from evidently.report import Report\n"
                    "from evidently.metric_preset import DataDriftPreset, ClassificationPreset\n"
                    "import pandas as pd\n"
                    "\n"
                    "# 학습 데이터 (기준 참조 데이터)\n"
                    "reference_df = pd.DataFrame(X_train, columns=feature_names)\n"
                    "reference_df['target'] = y_train\n"
                    "\n"
                    "# 최근 서빙 데이터 (프로덕션 입력)\n"
                    "current_df = pd.DataFrame(X_recent, columns=feature_names)\n"
                    "current_df['target'] = y_recent  # 레이블이 없으면 생략 가능\n"
                    "\n"
                    "# 드리프트 리포트 생성\n"
                    "report = Report(metrics=[\n"
                    "    DataDriftPreset(),         # 피처 분포 변화 감지\n"
                    "    ClassificationPreset(),    # 분류 성능 지표 (레이블 있을 때)\n"
                    "])\n"
                    "report.run(reference_data=reference_df, current_data=current_df)\n"
                    "\n"
                    "# HTML 리포트 저장\n"
                    "report.save_html('drift_report.html')\n"
                    "\n"
                    "# 드리프트 여부 확인 (자동화 파이프라인용)\n"
                    "result = report.as_dict()\n"
                    "drift_detected = result['metrics'][0]['result']['dataset_drift']\n"
                    "if drift_detected:\n"
                    "    print('데이터 드리프트 감지! 모델 재학습 검토 필요')\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "Prometheus + Grafana는 서버 CPU/메모리/지연시간 같은 인프라 지표에 강하고, "
                    "Evidently AI는 피처 분포 변화나 모델 성능 저하 같은 ML 특화 지표에 강합니다. "
                    "두 도구를 조합하면 완전한 모니터링 체계를 구축할 수 있습니다."
                ),
            },
        ],
    }


def _section_maturity_model() -> dict:
    return {
        "title": "B.4 MLOps 성숙도 모델 (Level 0~3)",
        "content": [
            (
                "Google의 MLOps 성숙도 모델은 조직의 ML 자동화 수준을 0~3 레벨로 정의합니다. "
                "현재 레벨을 파악하고 다음 레벨로 점진적으로 발전시키는 로드맵을 세우세요."
            ),
            {
                "type": "table",
                "headers": ["레벨", "명칭", "특징", "자동화 수준", "주요 도구"],
                "rows": [
                    [
                        "Level 0",
                        "수동 ML",
                        "노트북으로 실험, 수동 배포, 재현성 없음",
                        "없음",
                        "Jupyter Notebook",
                    ],
                    [
                        "Level 1",
                        "ML 파이프라인 자동화",
                        "학습 파이프라인 코드화, 실험 추적, 모델 레지스트리",
                        "학습 자동화",
                        "MLflow, DVC, 스크립트",
                    ],
                    [
                        "Level 2",
                        "CI/CD 파이프라인",
                        "코드 변경 시 자동 학습/테스트/배포, 모니터링",
                        "학습 + 배포 자동화",
                        "GitHub Actions, Airflow, MLflow + Docker",
                    ],
                    [
                        "Level 3",
                        "완전 자동화 MLOps",
                        "드리프트 감지 → 자동 재학습 → 자동 배포, 피드백 루프",
                        "재학습까지 자동화",
                        "Kubeflow, Vertex AI, SageMaker, Evidently",
                    ],
                ],
            },
            {
                "type": "flow_diagram",
                "title": "MLOps 성숙도 발전 경로",
                "direction": "horizontal",
                "nodes": [
                    {"label": "Level 0", "sub": "노트북 실험"},
                    {"label": "Level 1", "sub": "파이프라인 + MLflow"},
                    {"label": "Level 2", "sub": "CI/CD + Docker"},
                    {"label": "Level 3", "sub": "자동 재학습 + 피드백 루프"},
                ],
                "note": "이 시리즈를 완료한 독자는 Level 1~2 수준의 MLOps를 실습했습니다.",
            },
            {
                "type": "note",
                "text": (
                    "대부분의 실제 프로젝트는 Level 1~2에서 충분합니다. "
                    "Level 3은 대량의 데이터가 지속적으로 들어오는 프로덕션 서비스에 필요하며, "
                    "구축 비용이 높습니다. 조직의 실제 필요에 맞는 레벨을 목표로 설정하세요."
                ),
            },
        ],
    }


def _section_learning_path() -> dict:
    return {
        "title": "B.5 추천 학습 경로",
        "content": [
            "MLOps 전문가로 성장하기 위한 단계별 학습 경로입니다.",
            {
                "type": "table",
                "headers": ["단계", "주제", "추천 자료", "예상 기간"],
                "rows": [
                    ["기초", "Python ML 기초 (Vol.1~5 완료)", "이 시리즈", "2~3개월"],
                    ["MLOps 입문", "MLflow 심화, Docker/K8s 기초", "MLflow 공식 문서, Docker 공식 튜토리얼", "1개월"],
                    ["클라우드", "AWS SageMaker 또는 GCP Vertex AI", "AWS/GCP 공식 문서, Coursera 강좌", "2개월"],
                    ["파이프라인", "Apache Airflow 또는 Prefect", "Astronomer Academy, Prefect 공식 문서", "1개월"],
                    ["심화", "분산 학습, Kubernetes MLOps", "Full Stack Deep Learning, MLOps Specialization", "3개월"],
                    ["실무", "오픈소스 프로젝트 기여, 포트폴리오 구축", "GitHub, Kaggle", "지속"],
                ],
            },
            {
                "type": "bullet_list",
                "items": [
                    "Coursera — Machine Learning Engineering for Production (MLOps) 전문화 과정 (Andrew Ng 팀)",
                    "Full Stack Deep Learning (https://fullstackdeeplearning.com) — 실전 ML 시스템 구축",
                    "Made with ML (https://madewithml.com) — MLOps 오픈 커리큘럼",
                    "MLOps Community (https://mlops.community) — 블로그, 팟캐스트, 슬랙 커뮤니티",
                    "Kaggle — 실전 데이터 경연과 노트북으로 알고리즘 실력 향상",
                ],
            },
            {
                "type": "tip",
                "text": (
                    "MLOps 취업을 목표로 한다면 GitHub에 이 시리즈의 프로젝트를 올리고, "
                    "README에 아키텍처 다이어그램과 실행 방법을 상세히 작성하세요. "
                    "실제 동작하는 엔드투엔드 파이프라인 포트폴리오가 가장 강력한 증거입니다."
                ),
            },
        ],
    }
