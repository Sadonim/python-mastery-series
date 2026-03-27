"""
부록 C: 시리즈 완결 & 다음 단계
Vol.5 마무리 체크리스트, 전체 5권 요약, 다음 단계 추천,
추천 학습 자료, 전체 로드맵을 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 C: 시리즈 완결 & 다음 단계",
        "sections": [
            _section_checklist(),
            _section_series_summary(),
            _section_next_steps(),
            _section_resources(),
            _section_roadmap(),
        ],
    }


def _section_checklist() -> dict:
    return {
        "title": "C.1 Vol.5 마무리 체크리스트",
        "content": [
            "Vol.5를 완료하기 전에 아래 항목을 모두 확인하세요. 부족한 부분은 해당 챕터를 복습하세요.",
            {
                "type": "table",
                "headers": ["분류", "항목", "확인 기준", "체크"],
                "rows": [
                    # 머신러닝 기초
                    ["ML 기초", "지도/비지도/강화학습", "세 가지 유형의 차이와 사용 사례 설명 가능", "[ ]"],
                    ["ML 기초", "과적합/과소적합", "학습/검증 곡선으로 진단 가능", "[ ]"],
                    ["ML 기초", "교차검증", "K-Fold CV로 모델 성능 신뢰성 있게 평가", "[ ]"],
                    # 사이킷런
                    ["scikit-learn", "Pipeline 구성", "전처리 + 모델을 Pipeline으로 묶기", "[ ]"],
                    ["scikit-learn", "GridSearchCV", "하이퍼파라미터 탐색 후 최적값 선택", "[ ]"],
                    ["scikit-learn", "평가 지표", "목적에 맞는 지표 선택 (F1, AUC 등)", "[ ]"],
                    # MLflow
                    ["MLflow", "실험 추적", "mlflow.log_param/metric/artifact 사용", "[ ]"],
                    ["MLflow", "모델 레지스트리", "Production alias로 모델 등록 및 로드", "[ ]"],
                    ["MLflow", "MLflow UI", "브라우저에서 실험 결과 비교 가능", "[ ]"],
                    # FastAPI 서빙
                    ["FastAPI 서빙", "모델 로드", "lifespan으로 앱 시작 시 모델 1회 로드", "[ ]"],
                    ["FastAPI 서빙", "/predict 엔드포인트", "JSON 입력 -> 예측 -> JSON 응답", "[ ]"],
                    ["FastAPI 서빙", "입력 검증", "Pydantic Field로 피처 범위 및 개수 검증", "[ ]"],
                    # Docker
                    ["Docker", "Dockerfile 작성", "멀티 스테이지 빌드 또는 기본 빌드", "[ ]"],
                    ["Docker", "docker-compose", "MLflow + API 서비스 함께 실행", "[ ]"],
                    ["Docker", "헬스체크", "depends_on condition으로 서비스 순서 보장", "[ ]"],
                    # 모니터링
                    ["모니터링", "예측 로그", "구조화 JSON 로그로 예측 기록", "[ ]"],
                    ["모니터링", "/metrics 엔드포인트", "지연시간, 예측 분포 통계 제공", "[ ]"],
                    # 프로젝트
                    ["미니 프로젝트", "Ch9 완성", "전체 파이프라인 6단계 완성 + Docker 실행", "[ ]"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "체크리스트에서 MLflow 관련 항목이 부족하다면 Ch 6~7을 복습하세요. "
                    "MLflow는 이후 딥러닝, NLP, 컴퓨터 비전 프로젝트에서도 동일하게 활용할 수 있어 "
                    "투자 대비 효과가 매우 큰 도구입니다."
                ),
            },
        ],
    }


def _section_series_summary() -> dict:
    return {
        "title": "C.2 전체 시리즈 5권 완결 요약",
        "content": [
            (
                "Python Mastery Series 5권을 완주한 것을 진심으로 축하합니다! "
                "입문 수준에서 시작하여 실전 MLOps 파이프라인까지 완성한 여정을 돌아봅니다."
            ),
            {
                "type": "table",
                "headers": ["권", "제목", "핵심 주제", "완료 후 역량"],
                "rows": [
                    [
                        "Vol.1",
                        "Python 기초",
                        "자료형, 제어문, 함수, 클래스, 파일 I/O",
                        "Python 코드를 읽고 작성할 수 있다",
                    ],
                    [
                        "Vol.2",
                        "Python 심화",
                        "데코레이터, 제너레이터, 컨텍스트 매니저, 비동기",
                        "파이썬다운 관용구와 고급 패턴을 사용할 수 있다",
                    ],
                    [
                        "Vol.3",
                        "데이터 분석",
                        "NumPy, pandas, Matplotlib, 통계 기초",
                        "데이터를 불러와 분석하고 시각화할 수 있다",
                    ],
                    [
                        "Vol.4",
                        "웹 & 배포",
                        "FastAPI, SQLAlchemy, Docker, GitHub Actions",
                        "API 서버를 만들어 컨테이너로 배포할 수 있다",
                    ],
                    [
                        "Vol.5",
                        "ML & MLOps",
                        "scikit-learn, MLflow, 모델 서빙, 모니터링",
                        "ML 파이프라인을 구축하고 프로덕션에 배포할 수 있다",
                    ],
                ],
            },
            "**각 권에서 쌓은 역량은 서로 긴밀하게 연결됩니다:**",
            {
                "type": "bullet_list",
                "items": [
                    "Vol.1 기초 → Vol.2 심화 → 클린하고 효율적인 Python 코드 작성",
                    "Vol.3 데이터 분석 → Vol.5 ML → 데이터를 이해하고 모델을 만드는 기반",
                    "Vol.4 FastAPI/Docker → Vol.5 서빙/배포 → 모델을 실제 서비스로 연결",
                    "5권 전체 → 엔드투엔드 ML 파이프라인 구축 역량",
                ],
            },
            {
                "type": "note",
                "text": (
                    "이 시리즈는 '코드를 짜는 것'이 아니라 '문제를 해결하는 것'에 집중했습니다. "
                    "각 챕터의 미니 프로젝트를 완성한 경험이 실제 업무나 취업 인터뷰에서 "
                    "가장 큰 자산이 될 것입니다."
                ),
            },
        ],
    }


def _section_next_steps() -> dict:
    return {
        "title": "C.3 다음 단계 추천",
        "content": [
            (
                "시리즈를 완료했다면 관심 분야에 따라 더 깊이 탐구할 수 있습니다. "
                "아래 4가지 방향 중 하나를 선택하거나 병행하여 전문성을 쌓으세요."
            ),
            {
                "type": "heading",
                "text": "방향 1: 딥러닝 (Deep Learning)",
            },
            {
                "type": "bullet_list",
                "items": [
                    "PyTorch 기초: 텐서, 자동 미분, nn.Module, DataLoader",
                    "신경망 아키텍처: MLP, CNN, RNN, Transformer 이해",
                    "학습 기법: 배치 정규화, 드롭아웃, 학습률 스케줄러",
                    "추천 자료: fast.ai 강좌, PyTorch 공식 튜토리얼, Deep Learning Book (Goodfellow)",
                ],
            },
            {
                "type": "heading",
                "text": "방향 2: 자연어 처리 (NLP)",
            },
            {
                "type": "bullet_list",
                "items": [
                    "Hugging Face Transformers: BERT, GPT 계열 사전학습 모델 활용",
                    "텍스트 분류, 개체명 인식, 기계 번역, 텍스트 생성",
                    "LangChain으로 LLM 기반 애플리케이션 구축",
                    "추천 자료: Hugging Face NLP Course (무료), Stanford CS224N",
                ],
            },
            {
                "type": "heading",
                "text": "방향 3: 컴퓨터 비전 (Computer Vision)",
            },
            {
                "type": "bullet_list",
                "items": [
                    "이미지 분류: ResNet, EfficientNet, ViT",
                    "객체 탐지: YOLO 계열, Detectron2",
                    "이미지 분할: Segment Anything Model (SAM)",
                    "추천 자료: fast.ai Part 1, PyTorch Image Models (timm) 문서",
                ],
            },
            {
                "type": "heading",
                "text": "방향 4: MLOps 심화",
            },
            {
                "type": "bullet_list",
                "items": [
                    "클라우드 ML: AWS SageMaker, GCP Vertex AI, Azure ML",
                    "쿠버네티스 기반 MLOps: Kubeflow, Seldon Core",
                    "피처 스토어: Feast, Hopsworks로 피처 재사용성 확보",
                    "추천 자료: Coursera MLOps Specialization, Full Stack Deep Learning",
                ],
            },
            {
                "type": "table",
                "headers": ["방향", "난이도", "취업 연결", "흥미 포인트"],
                "rows": [
                    ["딥러닝", "중간", "AI 연구원, ML 엔지니어", "인간 수준의 인식 능력 구현"],
                    ["NLP", "중간~높음", "LLM 엔지니어, AI 제품 개발", "언어를 이해하는 AI 만들기"],
                    ["컴퓨터 비전", "중간", "자율주행, 의료AI, 로보틱스", "눈을 가진 AI 만들기"],
                    ["MLOps 심화", "중간", "ML 플랫폼 엔지니어, DevOps+ML", "AI를 안정적으로 운영하기"],
                ],
            },
        ],
    }


def _section_resources() -> dict:
    return {
        "title": "C.4 추천 학습 자료",
        "content": [
            "방향별로 검증된 학습 자료를 선별했습니다. 무료 자료를 먼저 활용하고 유료 자료로 심화하세요.",
            {
                "type": "heading",
                "text": "도서",
            },
            {
                "type": "table",
                "headers": ["도서명", "저자", "분야", "수준", "특징"],
                "rows": [
                    ["핸즈온 머신러닝 (3판)", "오렐리앙 제롱", "ML/DL", "입문~중급", "scikit-learn, TF/Keras 실습 중심"],
                    ["파이썬 머신러닝 완벽 가이드", "권철민", "ML", "입문~중급", "한국어, 실무 예제 풍부"],
                    ["딥러닝 파이토치 교과서", "서지영", "DL", "입문", "PyTorch 한국어 입문서"],
                    ["자연어 처리 쿡북", "Packt", "NLP", "중급", "NLTK, spaCy, Transformers 레시피"],
                    ["Designing Machine Learning Systems", "Chip Huyen", "MLOps", "중급~고급", "실전 ML 시스템 설계"],
                    ["Machine Learning Engineering", "Andriy Burkov", "MLOps", "중급", "ML 엔지니어링 실무 가이드"],
                ],
            },
            {
                "type": "heading",
                "text": "온라인 강좌",
            },
            {
                "type": "table",
                "headers": ["강좌명", "플랫폼", "분야", "비용", "특징"],
                "rows": [
                    ["Machine Learning Specialization", "Coursera (Andrew Ng)", "ML 기초", "유료(청강 무료)", "ML 입문 표준 강좌"],
                    ["Deep Learning Specialization", "Coursera (Andrew Ng)", "DL", "유료(청강 무료)", "DL 심화 5개 코스"],
                    ["MLOps Specialization", "Coursera (Andrew Ng 팀)", "MLOps", "유료", "프로덕션 ML 시스템"],
                    ["fast.ai Practical Deep Learning", "fast.ai", "DL", "무료", "하향식 실습 중심, PyTorch"],
                    ["Hugging Face NLP Course", "Hugging Face", "NLP", "무료", "Transformers 공식 강좌"],
                    ["Full Stack Deep Learning", "FSDL", "DL + MLOps", "무료(강의)", "실전 ML 프로젝트 전체 과정"],
                ],
            },
            {
                "type": "heading",
                "text": "커뮤니티 & 실습 플랫폼",
            },
            {
                "type": "bullet_list",
                "items": [
                    "Kaggle (kaggle.com) — 경진대회, 데이터셋, 노트북으로 실전 경험",
                    "Hugging Face Hub (huggingface.co) — 사전학습 모델, 데이터셋, Spaces",
                    "Papers With Code (paperswithcode.com) — 논문 + 코드, 벤치마크 추적",
                    "MLOps Community (mlops.community) — 블로그, 팟캐스트, Slack",
                    "Reddit r/MachineLearning — ML 연구 트렌드 및 토론",
                    "GitHub Trending — 인기 ML/AI 오픈소스 프로젝트 발굴",
                ],
            },
        ],
    }


def _section_roadmap() -> dict:
    return {
        "title": "C.5 전체 학습 로드맵",
        "content": [
            "5권 시리즈와 그 이후의 학습 경로를 한눈에 볼 수 있는 전체 로드맵입니다.",
            {
                "type": "flow_diagram",
                "title": "Python Mastery Series — 전체 로드맵",
                "direction": "vertical",
                "nodes": [
                    {"label": "Vol.1 Python 기초", "sub": "자료형, 함수, 클래스"},
                    {"label": "Vol.2 Python 심화", "sub": "데코레이터, 비동기, 고급 패턴"},
                    {"label": "Vol.3 데이터 분석", "sub": "NumPy, pandas, 시각화"},
                    {"label": "Vol.4 웹 & 배포", "sub": "FastAPI, Docker, CI/CD"},
                    {"label": "Vol.5 ML & MLOps", "sub": "scikit-learn, MLflow, 서빙"},
                    {"label": "분기점: 방향 선택", "sub": "딥러닝 / NLP / 비전 / MLOps 심화"},
                ],
                "note": "각 권은 독립적으로 학습 가능하지만, Vol.1부터 순서대로 학습하면 이해도가 가장 높습니다.",
            },
            {
                "type": "table",
                "headers": ["이후 경로", "기간", "목표 역할", "핵심 기술"],
                "rows": [
                    [
                        "딥러닝 심화",
                        "3~6개월",
                        "ML/DL 엔지니어",
                        "PyTorch, CNN, Transformer, 분산 학습",
                    ],
                    [
                        "NLP / LLM",
                        "3~6개월",
                        "LLM 엔지니어, AI 제품 개발",
                        "Hugging Face, RAG, Fine-tuning, LangChain",
                    ],
                    [
                        "컴퓨터 비전",
                        "3~6개월",
                        "비전 엔지니어, 자율주행 AI",
                        "YOLO, SAM, Detectron2, OpenCV",
                    ],
                    [
                        "MLOps 심화",
                        "3~6개월",
                        "ML 플랫폼 엔지니어",
                        "Kubeflow, Vertex AI, SageMaker, Feature Store",
                    ],
                    [
                        "포트폴리오 구축",
                        "지속",
                        "취업 / 프리랜서",
                        "GitHub, Kaggle, 블로그, 오픈소스 기여",
                    ],
                ],
            },
            "**마지막으로 드리는 메시지:**",
            (
                "이 시리즈를 끝까지 완주한 것은 대단한 성취입니다. "
                "코드를 배우는 것보다 더 중요한 것은 '문제를 정의하고 해결하는 사고방식'입니다. "
                "앞으로 어떤 기술을 배우든, 이 시리즈에서 익힌 '단계별로 생각하고 구현하는 습관'이 "
                "가장 강력한 무기가 될 것입니다. "
                "계속 코딩하고, 계속 배우고, 계속 만들어 나가세요!"
            ),
            {
                "type": "tip",
                "text": (
                    "포트폴리오 프로젝트 아이디어: 이 시리즈의 Ch9 미니 프로젝트를 발전시켜 "
                    "실제 관심 도메인(금융, 의료, 스포츠, 게임 등)의 데이터로 "
                    "자신만의 ML 파이프라인을 구축하고 GitHub에 공개하세요. "
                    "README에 문제 정의, 데이터 출처, 모델 성능, 아키텍처 다이어그램을 포함하면 "
                    "채용 담당자에게 강한 인상을 남길 수 있습니다."
                ),
            },
        ],
    }
