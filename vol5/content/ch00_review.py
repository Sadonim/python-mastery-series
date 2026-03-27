"""
Ch 0: 복습 & ML 준비
Python Mastery Series Vol.5 — ML & MLOps
"""


def get_chapter():
    return {
        "number": 0,
        "title": "복습 & ML 준비",
        "subtitle": "Vol.4 핵심 정리와 머신러닝 개발 환경 구축",
        "big_picture": (
            "Vol.5를 시작하기 전에 Vol.4에서 배운 FastAPI, Docker, CI/CD의 핵심을 빠르게 복습합니다. "
            "이 지식들은 ML 모델을 실제 서비스로 배포하는 MLOps의 뼈대가 됩니다. "
            "그리고 머신러닝이 무엇인지, AI와 어떻게 다른지, 어떤 문제를 풀 수 있는지 "
            "전체 그림을 잡습니다. 마지막으로 scikit-learn, numpy, pandas, matplotlib을 "
            "설치하고 ML 실습 환경을 준비합니다."
        ),
        "sections": [
            {
                "title": "Vol.4 핵심 복습 — FastAPI, Docker, CI/CD",
                "content": [
                    "Vol.5의 ML 모델은 FastAPI로 API가 되고, Docker로 배포되고, "
                    "CI/CD로 자동 검증됩니다. Vol.4 핵심 패턴을 빠르게 짚고 넘어갑시다.",
                    {
                        "type": "heading",
                        "text": "FastAPI — ML 모델 서빙의 핵심",
                    },
                    "FastAPI는 타입 힌트 기반으로 자동 문서화(Swagger UI)를 제공하는 "
                    "고성능 비동기 웹 프레임워크입니다. ML 예측 결과를 API로 노출할 때 "
                    "가장 널리 사용됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Vol.4 복습 — FastAPI 기본 패턴\n"
                            "from fastapi import FastAPI\n"
                            "from pydantic import BaseModel\n"
                            "\n"
                            "app = FastAPI(title='ML API 예시')\n"
                            "\n"
                            "# 요청/응답 스키마 정의 (Pydantic 모델)\n"
                            "class PredictRequest(BaseModel):\n"
                            "    features: list[float]  # 입력 피처 벡터\n"
                            "\n"
                            "class PredictResponse(BaseModel):\n"
                            "    prediction: float      # 예측값\n"
                            "    confidence: float      # 신뢰도\n"
                            "\n"
                            "@app.post('/predict', response_model=PredictResponse)\n"
                            "async def predict(req: PredictRequest):\n"
                            "    # 실제 모델 추론 자리 (Vol.5에서 채워나갈 부분)\n"
                            "    return PredictResponse(prediction=42.0, confidence=0.95)\n"
                            "\n"
                            "# 실행: uvicorn main:app --reload\n"
                            "# 문서: http://localhost:8000/docs"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "Docker — ML 환경 재현성의 열쇠",
                    },
                    "ML 프로젝트의 가장 큰 골칫거리 중 하나가 '내 컴퓨터에서는 됐는데 서버에서 안 돼'입니다. "
                    "Docker는 이 문제를 해결합니다. 모델 학습 환경과 서빙 환경을 동일하게 유지할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Vol.4 복습 — ML 앱 Dockerfile 패턴\n"
                            "# Dockerfile\n"
                            "# FROM python:3.11-slim\n"
                            "# WORKDIR /app\n"
                            "# COPY requirements.txt .\n"
                            "# RUN pip install --no-cache-dir -r requirements.txt\n"
                            "# COPY . .\n"
                            "# CMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n"
                            "\n"
                            "# 빌드 및 실행\n"
                            "docker build -t ml-api:v1 .\n"
                            "docker run -p 8000:8000 ml-api:v1\n"
                            "\n"
                            "# Docker Compose (DB + API 함께 실행)\n"
                            "# docker-compose up --build"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "CI/CD — 모델 품질 자동 검증",
                    },
                    "GitHub Actions로 코드가 푸시될 때마다 자동으로 테스트하고 배포합니다. "
                    "MLOps에서는 모델 성능 지표도 CI/CD 파이프라인에서 자동으로 검증합니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Vol.4 복습 — GitHub Actions CI/CD 패턴\n"
                            "# .github/workflows/test.yml\n"
                            "# name: ML API 테스트\n"
                            "# on: [push, pull_request]\n"
                            "# jobs:\n"
                            "#   test:\n"
                            "#     runs-on: ubuntu-latest\n"
                            "#     steps:\n"
                            "#       - uses: actions/checkout@v4\n"
                            "#       - uses: actions/setup-python@v4\n"
                            "#         with: {python-version: '3.11'}\n"
                            "#       - run: pip install -r requirements.txt\n"
                            "#       - run: pytest tests/ -v\n"
                            "#       - run: python evaluate_model.py  # 모델 성능 검증"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "FastAPI + Docker + CI/CD 조합은 MLOps의 핵심 기술 스택입니다. "
                            "Vol.4를 마쳤다면 이미 MLOps의 절반을 준비한 것입니다. "
                            "Vol.5에서는 여기에 ML 모델 학습과 관리를 추가합니다."
                        ),
                    },
                ],
            },
            {
                "title": "머신러닝이란? — AI vs ML vs DL",
                "content": [
                    "머신러닝을 배우기 전에 용어 정리가 필요합니다. "
                    "AI, ML, DL은 뉴스에서 혼용되지만 실제로는 포함 관계입니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "AI는 큰 마트 건물이고, ML은 그 안의 '학습' 코너입니다. "
                            "DL은 ML 코너 안에 있는 '딥러닝 특화 매장'입니다. "
                            "마트(AI) 전체에는 학습 코너 외에도 규칙 기반 시스템, "
                            "검색 알고리즘, 전문가 시스템 같은 다른 코너들도 있습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["구분", "정의", "예시", "특징"],
                        "rows": [
                            [
                                "AI (인공지능)",
                                "인간의 지능을 모방하는 모든 기술",
                                "체스 프로그램, 음성 인식, 추천 시스템",
                                "가장 넓은 개념",
                            ],
                            [
                                "ML (머신러닝)",
                                "데이터에서 패턴을 학습하는 알고리즘",
                                "스팸 필터, 집값 예측, 이상 감지",
                                "AI의 하위 분야",
                            ],
                            [
                                "DL (딥러닝)",
                                "다층 신경망을 사용하는 ML",
                                "이미지 인식, 번역, GPT",
                                "ML의 하위 분야, 대용량 데이터 필요",
                            ],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "머신러닝의 핵심 아이디어",
                    },
                    "전통적인 프로그래밍과 머신러닝의 차이를 이해하는 것이 출발점입니다.",
                    {
                        "type": "table",
                        "headers": ["구분", "전통적 프로그래밍", "머신러닝"],
                        "rows": [
                            ["입력", "데이터 + 규칙(코드)", "데이터 + 정답(레이블)"],
                            ["출력", "결과", "규칙(모델)"],
                            ["사람의 역할", "모든 규칙을 직접 작성", "데이터를 준비하고 학습 지시"],
                            ["적합한 문제", "규칙이 명확한 경우", "규칙이 너무 복잡하거나 불명확한 경우"],
                            ["예시", "환율 계산, 정렬 알고리즘", "얼굴 인식, 자연어 처리"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "머신러닝은 '마법'이 아닙니다. "
                            "좋은 데이터 + 적절한 알고리즘 + 올바른 평가가 조합된 공학입니다. "
                            "데이터 품질이 모델 성능의 80%를 결정합니다."
                        ),
                    },
                ],
            },
            {
                "title": "ML 문제 유형 — 지도·비지도·강화학습",
                "content": [
                    "머신러닝 문제는 크게 세 가지 유형으로 나뉩니다. "
                    "어떤 데이터가 있느냐, 무엇을 예측하려 하느냐에 따라 유형이 결정됩니다.",
                    {
                        "type": "heading",
                        "text": "지도학습 (Supervised Learning)",
                    },
                    "입력(X)과 정답(y) 쌍으로 이루어진 데이터로 학습합니다. "
                    "가장 많이 사용되는 유형입니다.",
                    {
                        "type": "table",
                        "headers": ["세부 유형", "목표", "예시 알고리즘", "실제 활용"],
                        "rows": [
                            [
                                "회귀 (Regression)",
                                "연속적인 수치 예측",
                                "선형회귀, 랜덤포레스트",
                                "집값 예측, 기온 예측, 주가 예측",
                            ],
                            [
                                "분류 (Classification)",
                                "카테고리 예측",
                                "로지스틱회귀, SVM, KNN",
                                "스팸 탐지, 질병 진단, 이미지 분류",
                            ],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "비지도학습 (Unsupervised Learning)",
                    },
                    "정답 레이블 없이 데이터의 구조나 패턴을 스스로 찾습니다.",
                    {
                        "type": "table",
                        "headers": ["세부 유형", "목표", "예시 알고리즘", "실제 활용"],
                        "rows": [
                            [
                                "클러스터링",
                                "비슷한 데이터 그룹화",
                                "K-Means, DBSCAN",
                                "고객 세분화, 이상 탐지",
                            ],
                            [
                                "차원 축소",
                                "고차원 데이터를 저차원으로",
                                "PCA, t-SNE",
                                "시각화, 특성 추출",
                            ],
                            [
                                "연관 규칙",
                                "함께 등장하는 패턴 발견",
                                "Apriori",
                                "장바구니 분석, 추천 시스템",
                            ],
                        ],
                    },
                    {
                        "type": "heading",
                        "text": "강화학습 (Reinforcement Learning)",
                    },
                    "환경과의 상호작용을 통해 보상을 최대화하는 행동 정책을 학습합니다. "
                    "게임 AI, 로봇 제어, 자율주행에 활용됩니다. Vol.5에서는 다루지 않지만 "
                    "개념으로 알아두는 것이 좋습니다.",
                    {
                        "type": "note",
                        "text": (
                            "Vol.5에서는 지도학습을 중심으로 배웁니다. "
                            "현업 ML 업무의 70% 이상이 지도학습(분류 또는 회귀)입니다. "
                            "비지도학습은 Ch.6 비지도학습 챕터에서 다룹니다."
                        ),
                    },
                ],
            },
            {
                "title": "ML 워크플로우 개요",
                "content": [
                    "머신러닝 프로젝트는 단순히 '모델 학습'이 아닙니다. "
                    "데이터 수집부터 서비스 배포까지 전체 파이프라인을 이해해야 합니다. "
                    "MLOps는 이 전체 흐름을 자동화하고 운영하는 것입니다.",
                    {
                        "type": "flow_diagram",
                        "title": "ML 워크플로우",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "1. 문제 정의", "sub": "비즈니스 목표 → ML 문제로 변환"},
                            {"label": "2. 데이터 수집", "sub": "DB, API, 크롤링, 센서 데이터"},
                            {"label": "3. 데이터 전처리", "sub": "결측값 처리, 정규화, 특성 추출"},
                            {"label": "4. 모델 학습", "sub": "알고리즘 선택, 하이퍼파라미터 튜닝"},
                            {"label": "5. 모델 평가", "sub": "정확도, F1, RMSE 등 지표 측정"},
                            {"label": "6. 배포", "sub": "FastAPI 서빙, Docker 컨테이너화"},
                            {"label": "7. 모니터링", "sub": "데이터 드리프트, 성능 저하 감지"},
                        ],
                        "note": "각 단계는 순환합니다. 모니터링에서 문제 발견 시 데이터 수집부터 다시 시작합니다.",
                    },
                    {
                        "type": "heading",
                        "text": "Vol.5 학습 로드맵",
                    },
                    {
                        "type": "table",
                        "headers": ["챕터", "주제", "워크플로우 단계"],
                        "rows": [
                            ["Ch 0", "복습 & ML 준비", "환경 구축"],
                            ["Ch 1", "ML 기초 이론", "문제 정의, 알고리즘 이해"],
                            ["Ch 2", "Scikit-learn 기초", "전처리, 학습, 평가"],
                            ["Ch 3", "분류 문제 심화", "특성 엔지니어링, 튜닝"],
                            ["Ch 4", "회귀 문제 심화", "정규화, 앙상블"],
                            ["Ch 5", "모델 평가 & 선택", "교차 검증, 지표 이해"],
                            ["Ch 6", "비지도학습", "클러스터링, 차원 축소"],
                            ["Ch 7", "ML 파이프라인", "Pipeline, ColumnTransformer"],
                            ["Ch 8", "모델 배포 & MLOps", "FastAPI 서빙, 실험 추적"],
                            ["Ch 9", "종합 프로젝트", "E2E ML 서비스 구축"],
                        ],
                    },
                ],
            },
            {
                "title": "개발 환경 준비",
                "content": [
                    "ML 개발을 위한 핵심 라이브러리를 설치합니다. "
                    "각 라이브러리의 역할을 이해하고 사용 목적을 파악해두면 "
                    "나중에 어떤 도구를 언제 써야 할지 판단이 쉬워집니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# Vol.5 ML 개발 환경 설치\n"
                            "mkdir ml_mastery && cd ml_mastery\n"
                            "python3 -m venv venv\n"
                            "source venv/bin/activate        # macOS / Linux\n"
                            "# venv\\Scripts\\activate        # Windows\n"
                            "\n"
                            "# 핵심 ML 라이브러리 설치\n"
                            "pip install scikit-learn numpy pandas matplotlib seaborn\n"
                            "\n"
                            "# 실험 관리 및 MLOps 도구\n"
                            "pip install mlflow joblib\n"
                            "\n"
                            "# 개발 편의 도구\n"
                            "pip install jupyter notebook ipykernel\n"
                            "\n"
                            "# 설치 확인\n"
                            "python -c \"import sklearn; print('scikit-learn', sklearn.__version__)\"\n"
                            "python -c \"import numpy; print('numpy', numpy.__version__)\"\n"
                            "python -c \"import pandas; print('pandas', pandas.__version__)\"\n"
                            "\n"
                            "pip freeze > requirements.txt"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["라이브러리", "버전 (권장)", "주요 역할", "Vol.5 활용"],
                        "rows": [
                            ["scikit-learn", "1.4+", "ML 알고리즘 모음", "Ch 2-7 모든 챕터"],
                            ["numpy", "1.26+", "수치 연산 배열", "행렬 연산, 데이터 변환"],
                            ["pandas", "2.x", "테이블형 데이터 처리", "데이터 로드, 전처리"],
                            ["matplotlib", "3.8+", "기본 시각화", "학습 곡선, 산점도"],
                            ["seaborn", "0.13+", "통계 시각화", "분포, 히트맵, 상관관계"],
                            ["mlflow", "2.x", "실험 추적 및 모델 관리", "Ch 8 MLOps"],
                            ["joblib", "1.3+", "모델 직렬화 (저장/로드)", "Ch 8 배포"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 환경 설치 검증 스크립트\n"
                            "import sys\n"
                            "\n"
                            "def check_library(name, import_name=None):\n"
                            "    \"\"\"라이브러리 설치 여부와 버전을 확인합니다.\"\"\"\n"
                            "    module_name = import_name or name\n"
                            "    try:\n"
                            "        module = __import__(module_name)\n"
                            "        version = getattr(module, '__version__', '버전 정보 없음')\n"
                            "        print(f'  [OK] {name}: {version}')\n"
                            "        return True\n"
                            "    except ImportError:\n"
                            "        print(f'  [실패] {name}: 설치되지 않음')\n"
                            "        return False\n"
                            "\n"
                            "print('=== Vol.5 환경 검증 ===')\n"
                            "libraries = [\n"
                            "    ('scikit-learn', 'sklearn'),\n"
                            "    ('numpy', None),\n"
                            "    ('pandas', None),\n"
                            "    ('matplotlib', None),\n"
                            "    ('seaborn', None),\n"
                            "    ('mlflow', None),\n"
                            "    ('joblib', None),\n"
                            "]\n"
                            "\n"
                            "결과 = [check_library(name, imp) for name, imp in libraries]\n"
                            "성공 = sum(결과)\n"
                            "print(f'\\n결과: {성공}/{len(libraries)} 라이브러리 설치 완료')\n"
                            "if 성공 == len(libraries):\n"
                            "    print('Vol.5 학습 준비 완료!')\n"
                            "else:\n"
                            "    print('pip install 명령어로 누락된 라이브러리를 설치하세요.')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "Jupyter Notebook은 탐색적 분석(EDA)에 편리하지만, "
                            "프로덕션 코드는 반드시 .py 파일로 작성하세요. "
                            "노트북은 버전 관리(Git)와 테스트가 어렵고, "
                            "MLOps 파이프라인에 직접 통합하기 불편합니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "ML 프로젝트를 시작할 때는 항상 '어떤 문제를 푸는가'를 먼저 정의하세요. "
            "지도학습인지 비지도학습인지, 분류인지 회귀인지 명확히 해야 올바른 알고리즘을 선택할 수 있습니다.",
            "데이터 품질이 모델 성능의 80%를 결정합니다. "
            "고급 알고리즘을 쓰기 전에 데이터를 충분히 탐색하고 정제하세요.",
            "scikit-learn은 공식 문서가 매우 잘 되어 있습니다. "
            "모르는 클래스가 나오면 sklearn.org 문서에서 파라미터와 예제를 먼저 확인하세요.",
            "Vol.4에서 만든 FastAPI 프로젝트를 그대로 활용하세요. "
            "Ch.8에서 ML 모델을 그 위에 얹는 방식으로 MLOps를 완성합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 중 머신러닝(ML)에 대한 설명으로 가장 올바른 것은?",
                "choices": [
                    "ML은 AI와 완전히 별개의 분야다",
                    "ML은 데이터에서 패턴을 학습하는 AI의 하위 분야다",
                    "딥러닝(DL)은 ML보다 더 넓은 개념이다",
                    "ML은 항상 레이블(정답)이 있는 데이터를 필요로 한다",
                ],
                "answer": "2번",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "집값 예측 모델을 만들려 한다. 어떤 ML 문제 유형에 해당하는가?",
                "choices": [
                    "분류 (Classification)",
                    "클러스터링 (Clustering)",
                    "회귀 (Regression)",
                    "강화학습 (Reinforcement Learning)",
                ],
                "answer": "3번",
            },
            {
                "number": 3,
                "type": "short_answer",
                "question": (
                    "ML 워크플로우의 7단계를 순서대로 나열하세요.\n"
                    "(힌트: 문제 정의 → ... → 모니터링)"
                ),
                "answer": (
                    "문제 정의 → 데이터 수집 → 데이터 전처리 → "
                    "모델 학습 → 모델 평가 → 배포 → 모니터링"
                ),
            },
        ],
        "challenge": {
            "question": (
                "다음 ML 시나리오를 읽고 각각 어떤 ML 문제 유형(회귀/분류/클러스터링)인지 분류하고, "
                "적합한 scikit-learn 알고리즘 1개씩을 제안하세요.\n\n"
                "① 군 장병 체력 측정 데이터를 바탕으로 부상 위험도 점수(0~100)를 예측\n"
                "② 네트워크 로그 데이터에서 정상/비정상 트래픽 판별 (레이블 없음)\n"
                "③ 이메일이 스팸인지 아닌지 판별\n"
                "④ 다음 달 부대 보급품 소비량 예측"
            ),
            "hint": (
                "수치를 예측하면 회귀, 카테고리를 예측하면 분류, "
                "레이블 없이 그룹화하면 클러스터링입니다. "
                "scikit-learn 알고리즘: LinearRegression, LogisticRegression, "
                "RandomForestClassifier, KMeans 등을 고려해보세요."
            ),
        },
        "summary": [
            "AI는 인공지능 전체, ML은 데이터 학습 기반 AI의 하위 분야, DL은 신경망 기반 ML입니다.",
            "지도학습(정답 있음)은 회귀와 분류로 나뉘며, 현업 ML의 70% 이상을 차지합니다.",
            "비지도학습은 레이블 없이 데이터의 구조(클러스터, 패턴)를 찾습니다.",
            "ML 워크플로우는 문제 정의 → 데이터 수집 → 전처리 → 학습 → 평가 → 배포 → 모니터링입니다.",
            "MLOps는 이 전체 워크플로우를 자동화하고 지속 운영하는 것이며, FastAPI + Docker + CI/CD가 핵심입니다.",
            "scikit-learn, numpy, pandas, matplotlib을 설치하고 환경 검증 스크립트로 확인하세요.",
        ],
    }
