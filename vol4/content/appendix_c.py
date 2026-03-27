"""
부록 C: Vol.5 미리보기 & 학습 전략
Vol.4 마무리 체크리스트, Vol.5 ML & MLOps 미리보기, 추천 자료, 전체 로드맵을 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 C: Vol.5 미리보기 & 학습 전략",
        "sections": [
            _section_checklist(),
            _section_vol5_preview(),
            _section_taste_code(),
            _section_resources(),
            _section_roadmap(),
        ],
    }


def _section_checklist() -> dict:
    return {
        "title": "Vol.4 마무리 체크리스트",
        "content": [
            "Vol.5로 넘어가기 전에 아래 항목을 모두 확인하세요.",
            {
                "type": "table",
                "headers": ["분류", "항목", "확인 기준", "체크"],
                "rows": [
                    # FastAPI
                    ["FastAPI", "라우터 & 엔드포인트", "GET/POST/PUT/DELETE 5개 메서드 구현 가능", "[ ]"],
                    ["FastAPI", "Pydantic 스키마", "BaseModel로 요청/응답 검증, Field 옵션 사용", "[ ]"],
                    ["FastAPI", "의존성 주입", "Depends()로 DB 세션 주입 가능", "[ ]"],
                    ["FastAPI", "Swagger UI", "http://localhost:8000/docs 접속 & 테스트", "[ ]"],
                    # SQLAlchemy
                    ["SQLAlchemy", "ORM 모델 정의", "mapped_column, Mapped 타입 사용", "[ ]"],
                    ["SQLAlchemy", "CRUD 쿼리", "add, commit, query, filter, delete 사용", "[ ]"],
                    ["SQLAlchemy", "세션 관리", "get_db() 의존성 패턴 이해", "[ ]"],
                    # pytest
                    ["pytest", "TestClient", "실서버 없이 API 엔드포인트 테스트", "[ ]"],
                    ["pytest", "fixture", "conftest.py에 공용 fixture 작성", "[ ]"],
                    ["pytest", "커버리지", "pytest --cov 로 80% 이상 달성", "[ ]"],
                    # Docker
                    ["Docker", "Dockerfile 작성", "FROM, WORKDIR, COPY, RUN, CMD 지시어 사용", "[ ]"],
                    ["Docker", "이미지 빌드", "docker build -t 이름 . 실행 가능", "[ ]"],
                    ["Docker", "docker-compose", "docker compose up --build 로 앱 실행", "[ ]"],
                    # CI/CD
                    ["GitHub Actions", "워크플로우 작성", ".github/workflows/ci.yml 생성 & 실행 확인", "[ ]"],
                    ["GitHub Actions", "자동 테스트", "push 시 pytest 자동 실행 확인", "[ ]"],
                    # 프로젝트
                    ["미니 프로젝트", "Ch9 완성", "Todo API 전체 구현 + 테스트 + Docker + CI", "[ ]"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "체크리스트에서 3개 이상 부족하다면 해당 챕터를 복습하세요. "
                    "특히 SQLAlchemy 세션 관리와 pytest fixture는 "
                    "Vol.5 ML 모델 서빙 API 작성에 직접 활용됩니다."
                ),
            },
        ],
    }


def _section_vol5_preview() -> dict:
    return {
        "title": "Vol.5: ML & MLOps 미리보기",
        "content": [
            (
                "Vol.5에서는 머신러닝 모델을 만들고, 실험을 관리하고, "
                "모델을 API로 서빙하고, 프로덕션에서 모니터링하는 "
                "MLOps(Machine Learning Operations) 전 과정을 배웁니다. "
                "Vol.4에서 배운 FastAPI + Docker 스킬이 그대로 활용됩니다."
            ),
            {
                "type": "table",
                "headers": ["챕터", "주제", "핵심 기술", "Vol.4 연관"],
                "rows": [
                    ["Ch 0", "복습: Vol.4 핵심 요약", "FastAPI, Docker, pytest", "전체"],
                    ["Ch 1", "머신러닝 기초", "Scikit-learn, 지도/비지도 학습", "Vol.3 Pandas/NumPy"],
                    ["Ch 2", "분류 & 회귀 모델", "LinearRegression, RandomForest, SVM", "Vol.3 데이터 처리"],
                    ["Ch 3", "모델 평가 & 튜닝", "교차검증, GridSearchCV, ROC-AUC", ""],
                    ["Ch 4", "실험 관리 — MLflow", "run, log_metric, log_model, UI", "Docker 환경 활용"],
                    ["Ch 5", "모델 서빙 API", "FastAPI + joblib, 예측 엔드포인트", "Ch 9 Todo API 구조"],
                    ["Ch 6", "모델 패키징 & 배포", "MLflow Model Registry, Docker", "Ch 7 Dockerfile"],
                    ["Ch 7", "데이터 파이프라인", "Prefect/Airflow 기초, 스케줄링", "Ch 8 GitHub Actions"],
                    ["Ch 8", "모델 모니터링", "데이터 드리프트, Evidently, 알림", "Ch 8 배포 전략"],
                    ["Ch 9", "미니 프로젝트", "분류 모델 + MLflow + FastAPI 서빙", "Ch 9 Todo API"],
                ],
            },
            {
                "type": "note",
                "text": (
                    "MLOps = ML(머신러닝) + DevOps(개발운영). "
                    "모델을 만드는 것뿐 아니라 '운영 가능한 상태로 유지'하는 것이 핵심입니다. "
                    "Vol.4에서 배운 API 서버, 컨테이너화, CI/CD는 MLOps의 필수 기반 기술입니다."
                ),
            },
        ],
    }


def _section_taste_code() -> dict:
    return {
        "title": "Vol.5 맛보기 코드",
        "content": [
            "Vol.5에서 다룰 핵심 기술을 간략하게 미리 살펴봅니다.",
            {
                "type": "heading",
                "text": "Scikit-learn — 분류 모델 30줄",
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# Vol.5 Ch1 맛보기: Scikit-learn으로 붓꽃 분류 모델 만들기\n"
                    "from sklearn.datasets import load_iris\n"
                    "from sklearn.model_selection import train_test_split\n"
                    "from sklearn.ensemble import RandomForestClassifier\n"
                    "from sklearn.metrics import accuracy_score, classification_report\n"
                    "import joblib\n"
                    "\n"
                    "\n"
                    "# 1. 데이터 로드 (Iris: 붓꽃 3종 분류)\n"
                    "iris = load_iris()\n"
                    "X, y = iris.data, iris.target\n"
                    "\n"
                    "# 2. 학습/테스트 분리 (8:2 비율)\n"
                    "X_train, X_test, y_train, y_test = train_test_split(\n"
                    "    X, y, test_size=0.2, random_state=42, stratify=y\n"
                    ")\n"
                    "\n"
                    "# 3. 모델 학습 (랜덤 포레스트)\n"
                    "model = RandomForestClassifier(n_estimators=100, random_state=42)\n"
                    "model.fit(X_train, y_train)\n"
                    "\n"
                    "# 4. 평가\n"
                    "y_pred = model.predict(X_test)\n"
                    "print(f'정확도: {accuracy_score(y_test, y_pred):.4f}')  # 약 0.9667\n"
                    "print(classification_report(y_test, y_pred,\n"
                    "                            target_names=iris.target_names))\n"
                    "\n"
                    "# 5. 모델 저장\n"
                    "joblib.dump(model, 'iris_model.pkl')\n"
                    "print('모델 저장 완료: iris_model.pkl')\n"
                ),
            },
            {
                "type": "heading",
                "text": "FastAPI + Scikit-learn — 모델 서빙 API",
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# Vol.5 Ch5 맛보기: 학습된 모델을 FastAPI로 서빙\n"
                    "import joblib\n"
                    "import numpy as np\n"
                    "from fastapi import FastAPI\n"
                    "from pydantic import BaseModel, Field\n"
                    "\n"
                    "\n"
                    "# 모델 로드 (앱 시작 시 한 번만)\n"
                    "model = joblib.load('iris_model.pkl')\n"
                    "CLASSES = ['setosa', 'versicolor', 'virginica']\n"
                    "\n"
                    "app = FastAPI(title='붓꽃 분류 API')\n"
                    "\n"
                    "\n"
                    "class IrisFeatures(BaseModel):\n"
                    '    """붓꽃 4개 특성값 입력"""\n'
                    "    sepal_length: float = Field(..., ge=0, description='꽃받침 길이 (cm)')\n"
                    "    sepal_width: float = Field(..., ge=0, description='꽃받침 너비 (cm)')\n"
                    "    petal_length: float = Field(..., ge=0, description='꽃잎 길이 (cm)')\n"
                    "    petal_width: float = Field(..., ge=0, description='꽃잎 너비 (cm)')\n"
                    "\n"
                    "\n"
                    "@app.post('/predict')\n"
                    "def predict(features: IrisFeatures) -> dict:\n"
                    '    """붓꽃 종류를 예측한다."""\n'
                    "    X = np.array([[\n"
                    "        features.sepal_length, features.sepal_width,\n"
                    "        features.petal_length, features.petal_width,\n"
                    "    ]])\n"
                    "    pred = model.predict(X)[0]\n"
                    "    proba = model.predict_proba(X)[0]\n"
                    "\n"
                    "    return {\n"
                    "        'prediction': CLASSES[pred],\n"
                    "        'confidence': round(float(proba.max()), 4),\n"
                    "        'probabilities': {\n"
                    "            cls: round(float(p), 4)\n"
                    "            for cls, p in zip(CLASSES, proba)\n"
                    "        },\n"
                    "    }\n"
                    "\n"
                    "# 실행: uvicorn serve:app --reload\n"
                    "# 예측 요청: POST /predict\n"
                    "# {\"sepal_length\": 5.1, \"sepal_width\": 3.5,\n"
                    "#  \"petal_length\": 1.4, \"petal_width\": 0.2}\n"
                    "# => {\"prediction\": \"setosa\", \"confidence\": 0.98, ...}\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "이 모델 서빙 API 구조는 Ch9 Todo API와 거의 동일합니다. "
                    "라우터, Pydantic 스키마, 의존성 주입 패턴이 그대로 적용됩니다. "
                    "Vol.4를 완료했다면 Vol.5 시작이 훨씬 쉽습니다."
                ),
            },
        ],
    }


def _section_resources() -> dict:
    return {
        "title": "추천 학습 자료",
        "content": [
            {
                "type": "table",
                "headers": ["분류", "이름", "특징", "링크"],
                "rows": [
                    # Vol.4 관련
                    ["공식 문서", "FastAPI 공식 튜토리얼", "인터랙티브 학습, 한국어 번역 있음", "fastapi.tiangolo.com"],
                    ["공식 문서", "SQLAlchemy 2.0 문서", "ORM 패턴 상세 설명", "docs.sqlalchemy.org"],
                    ["공식 문서", "Docker Docs - Get Started", "컨테이너 기초부터 Compose까지", "docs.docker.com"],
                    ["공식 문서", "GitHub Actions 공식 가이드", "워크플로우 문법 & 예제", "docs.github.com/actions"],
                    ["도서", "FastAPI 완벽 가이드", "실전 API 개발 패턴 수록", ""],
                    ["강좌", "점프 투 FastAPI", "무료 온라인 한국어 강좌", "wikidocs.net/book/8531"],
                    # Vol.5 사전 준비
                    ["Vol.5 준비", "Scikit-learn 공식 튜토리얼", "User Guide + API Reference", "scikit-learn.org"],
                    ["Vol.5 준비", "MLflow 공식 문서", "실험 추적, 모델 레지스트리", "mlflow.org"],
                    ["Vol.5 준비", "머신러닝 with Python 개론", "Andrew Ng Coursera ML 강좌", "coursera.org"],
                    ["커뮤니티", "FastAPI GitHub Discussions", "질문, 트러블슈팅", "github.com/fastapi/fastapi"],
                    ["커뮤니티", "Reddit r/MachineLearning", "ML 트렌드 & 논문 토론", "reddit.com/r/MachineLearning"],
                ],
            },
            {
                "type": "note",
                "text": (
                    "FastAPI와 SQLAlchemy 중 막히는 부분이 있다면 "
                    "공식 문서 예제를 먼저 실행해보세요. "
                    "MLOps 목표라면 Scikit-learn 공식 튜토리얼을 "
                    "Vol.4 완료 후 바로 시작하는 것을 추천합니다."
                ),
            },
        ],
    }


def _section_roadmap() -> dict:
    return {
        "title": "전체 로드맵 & 다음 단계",
        "content": [
            "Python Mastery Series 5권 전체 학습 경로입니다.",
            {
                "type": "flow_diagram",
                "direction": "vertical",
                "nodes": [
                    {
                        "label": "Vol.1: Python 기초",
                        "sub": "변수, 조건문, 반복문, 함수, 자료구조",
                    },
                    {
                        "label": "Vol.2: Python 심화",
                        "sub": "OOP, 예외 처리, 파일 I/O, 데코레이터, 이터레이터",
                    },
                    {
                        "label": "Vol.3: 데이터 분석",
                        "sub": "NumPy, Pandas, Matplotlib, Seaborn, 공공 API",
                    },
                    {
                        "label": "Vol.4: 웹 & 배포 (현재)",
                        "sub": "FastAPI, SQLAlchemy, pytest, Docker, GitHub Actions",
                    },
                    {
                        "label": "Vol.5: ML & MLOps",
                        "sub": "Scikit-learn, MLflow, 모델 서빙, 모니터링, 파이프라인",
                    },
                ],
                "title": "Python Mastery Series 전체 학습 로드맵",
                "note": "현재 Vol.4 완료 — 다음은 Vol.5 ML & MLOps",
            },
            {
                "type": "table",
                "headers": ["완료 후 달성 역량", "Vol.4", "Vol.5 (예정)"],
                "rows": [
                    ["REST API 설계 & 구현", "O — FastAPI CRUD", "O — 모델 서빙 API"],
                    ["DB 연동", "O — SQLAlchemy ORM", "O — 실험 메타데이터 저장"],
                    ["테스트 자동화", "O — pytest 80% 커버리지", "O — 모델 성능 회귀 테스트"],
                    ["컨테이너화", "O — Dockerfile, Compose", "O — ML 파이프라인 컨테이너화"],
                    ["CI/CD", "O — GitHub Actions", "O — 모델 재학습 파이프라인"],
                    ["ML 모델 개발", "X", "O — Scikit-learn, 교차검증"],
                    ["실험 추적", "X", "O — MLflow Tracking Server"],
                    ["모델 배포", "X", "O — MLflow Registry + API"],
                    ["운영 모니터링", "X", "O — 데이터 드리프트, 알림"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "Vol.5 시작 전 준비: "
                    "pip install scikit-learn mlflow matplotlib seaborn 설치 후 "
                    "Scikit-learn 공식 튜토리얼의 'Getting Started' 섹션을 먼저 읽으세요. "
                    "Vol.3 Pandas + NumPy 지식이 모델 데이터 전처리에 바로 활용됩니다."
                ),
            },
            (
                "Vol.4 과정을 수료한 것을 축하합니다! "
                "이제 여러분은 Python으로 실전 배포 가능한 API 서버를 만들고 "
                "컨테이너화·자동화까지 완성할 수 있는 수준이 되었습니다. "
                "Vol.5에서 머신러닝 모델을 이 위에 올려 완전한 MLOps 파이프라인을 완성해 봅시다."
            ),
        ],
    }
