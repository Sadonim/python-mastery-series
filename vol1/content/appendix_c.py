"""
부록 C: 추천 학습 자료 & 로드맵
Vol.1 이후의 학습 방향과 활용 가능한 자료를 안내한다.
"""


def get_appendix():
    return {
        "title": "부록 C: 추천 학습 자료 & 로드맵",
        "sections": [
            # ── 섹션 1: 온라인 학습 자료 ──
            {
                "title": "C.1 온라인 학습 자료",
                "content": [
                    (
                        "혼자 공부할 때 가장 중요한 것은 "
                        "좋은 자료를 찾는 것입니다. "
                        "아래는 검증된 무료/유료 학습 자료입니다."
                    ),
                    "**공식 문서 (무료, 가장 정확):**",
                    {
                        "type": "table",
                        "headers": ["자료", "URL", "특징"],
                        "rows": [
                            [
                                "Python 공식 튜토리얼",
                                "docs.python.org/ko/3/tutorial",
                                "한국어 번역 제공, 가장 정확한 기본서",
                            ],
                            [
                                "Python 공식 레퍼런스",
                                "docs.python.org/ko/3/library",
                                "모든 내장 모듈의 상세 설명",
                            ],
                            [
                                "PEP 8 스타일 가이드",
                                "peps.python.org/pep-0008",
                                "Python 코드 작성의 표준 규칙",
                            ],
                            [
                                "Real Python",
                                "realpython.com",
                                "영문, 주제별 깊이 있는 튜토리얼",
                            ],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "공식 문서가 처음엔 어렵게 느껴질 수 있지만, "
                            "가장 정확하고 최신 정보를 제공합니다. "
                            "모르는 함수가 있을 때 공식 문서를 찾아보는 습관을 들이세요."
                        ),
                    },
                    "**무료 강의 플랫폼:**",
                    {
                        "type": "table",
                        "headers": ["플랫폼", "추천 강의", "특징"],
                        "rows": [
                            [
                                "생활코딩",
                                "Python 입문",
                                "한국어, 완전 초보 대상, 무료",
                            ],
                            [
                                "코드잇 (Codeit)",
                                "프로그래밍 기초 in Python",
                                "한국어, 실습 중심, 일부 무료",
                            ],
                            [
                                "인프런",
                                "파이썬 입문 강의 다수",
                                "한국어, 유/무료 혼합, 실무 강의 많음",
                            ],
                            [
                                "Coursera",
                                "Python for Everybody (UMich)",
                                "영문(한글 자막), 대학 수준, 수료증 발급",
                            ],
                            [
                                "edX",
                                "MITx 6.00.1x",
                                "영문, MIT 수준 컴퓨터 과학 입문",
                            ],
                        ],
                    },
                    "**추천 YouTube 채널:**",
                    {
                        "type": "table",
                        "headers": ["채널명", "언어", "특징"],
                        "rows": [
                            [
                                "나도코딩",
                                "한국어",
                                "Python 기초~중급, 프로젝트 실습",
                            ],
                            [
                                "조코딩 (JoCoding)",
                                "한국어",
                                "입문자 친화적, 다양한 프로젝트",
                            ],
                            [
                                "Corey Schafer",
                                "영어",
                                "Python 핵심 개념을 명확하게 설명",
                            ],
                            [
                                "Tech With Tim",
                                "영어",
                                "Python 프로젝트 중심, 게임/웹 개발",
                            ],
                            [
                                "ArjanCodes",
                                "영어",
                                "Python 설계 패턴, 코드 품질 중심",
                            ],
                        ],
                    },
                ],
            },
            # ── 섹션 2: 추천 도서 ──
            {
                "title": "C.2 추천 도서",
                "content": [
                    (
                        "동영상 강의가 '빠르게 따라하기'에 좋다면, "
                        "책은 '깊이 이해하기'에 좋습니다. "
                        "수준별로 추천 도서를 정리합니다."
                    ),
                    "**초보 단계 (Vol.1 병행/후속):**",
                    {
                        "type": "table",
                        "headers": ["도서명", "저자", "특징"],
                        "rows": [
                            [
                                "혼자 공부하는 파이썬",
                                "윤인성",
                                "그림 많음, 독학 최적화, 한국어",
                            ],
                            [
                                "Do it! 점프 투 파이썬",
                                "박응용",
                                "한국 Python 입문서의 고전, 온라인 무료 버전",
                            ],
                            [
                                "파이썬 코딩 도장",
                                "남재윤",
                                "단원별 연습문제 풍부, 한국어",
                            ],
                        ],
                    },
                    "**중급 단계 (Vol.2~3 병행):**",
                    {
                        "type": "table",
                        "headers": ["도서명", "저자", "특징"],
                        "rows": [
                            [
                                "파이썬 알고리즘 인터뷰",
                                "박상길",
                                "코딩 테스트 대비, LeetCode 문제 풀이",
                            ],
                            [
                                "이것이 취업을 위한 코딩 테스트다",
                                "나동빈",
                                "취업 대비 알고리즘 총정리, 한국어",
                            ],
                            [
                                "Fluent Python (2판)",
                                "Luciano Ramalho",
                                "Python 심화 필독서, 영문(번역판 있음)",
                            ],
                        ],
                    },
                    "**고급/실무 단계 (Vol.4~5 병행):**",
                    {
                        "type": "table",
                        "headers": ["도서명", "저자", "특징"],
                        "rows": [
                            [
                                "Effective Python (2판)",
                                "Brett Slatkin",
                                "90가지 베스트 프랙티스, 영문(번역판 있음)",
                            ],
                            [
                                "클린 코드 (Clean Code)",
                                "Robert C. Martin",
                                "언어 무관 코드 품질 바이블, 필독서",
                            ],
                            [
                                "파이썬 클린 코드",
                                "Mariano Anaya",
                                "Python 특화 클린 코드, 한국어 번역판",
                            ],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "책을 읽을 때는 반드시 코드를 직접 타이핑하세요. "
                            "눈으로만 읽으면 이해한 것 같지만, "
                            "막상 코드를 쓰려 하면 모르는 경우가 많습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 코딩 연습 사이트 ──
            {
                "title": "C.3 코딩 연습 사이트",
                "content": [
                    (
                        "프로그래밍 실력은 '읽기'가 아니라 '풀기'로 늡니다. "
                        "아래 사이트에서 매일 한 문제씩 풀어보세요."
                    ),
                    {
                        "type": "table",
                        "headers": ["사이트", "URL", "난이도", "특징"],
                        "rows": [
                            [
                                "백준 Online Judge",
                                "boj.kr",
                                "입문~고급",
                                "한국 최대 규모, 문제 수 2만+, 단계별 분류",
                            ],
                            [
                                "프로그래머스",
                                "programmers.co.kr",
                                "입문~중급",
                                "한국 기업 코딩테스트 출제 플랫폼, 실전 대비",
                            ],
                            [
                                "LeetCode",
                                "leetcode.com",
                                "입문~고급",
                                "글로벌 표준, 해외 취업 준비 필수, 영문",
                            ],
                            [
                                "HackerRank",
                                "hackerrank.com",
                                "입문~중급",
                                "언어별 연습 트랙, 자격증 발급, 영문",
                            ],
                            [
                                "Codewars",
                                "codewars.com",
                                "입문~고급",
                                "단(kyu) 시스템, 다른 사람 풀이 비교 가능",
                            ],
                        ],
                    },
                    "**추천 학습 순서:**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "백준 '단계별로 풀기'에서 입출력~반복문 단계 완료",
                            "프로그래머스 Lv.0 → Lv.1 문제 풀기",
                            "LeetCode Easy 문제 50개 풀기",
                            "프로그래머스 Lv.2, LeetCode Medium 도전",
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "문제를 못 풀겠으면 30분 고민 후 풀이를 보세요. "
                            "단, 풀이를 보고 나서 반드시 '안 보고 다시 풀기'를 하세요. "
                            "이 과정 없이는 실력이 늘지 않습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: Vol.1 이후 학습 로드맵 ──
            {
                "title": "C.4 Vol.1 이후 학습 로드맵",
                "content": [
                    (
                        "Python Mastery Series는 5권으로 구성되어 있으며, "
                        "Vol.1은 그 첫 단계입니다. "
                        "각 권의 주제와 목표를 미리 살펴봅시다."
                    ),
                    {
                        "type": "table",
                        "headers": ["권", "주제", "핵심 내용", "기간 (권장)"],
                        "rows": [
                            [
                                "Vol.1",
                                "Python 기초",
                                "변수, 제어문, 함수, 자료구조, 문자열, 모듈",
                                "4~6주",
                            ],
                            [
                                "Vol.2",
                                "Python 심화",
                                "OOP, 예외처리 심화, 파일 I/O, 정규표현식, 패키지",
                                "4~6주",
                            ],
                            [
                                "Vol.3",
                                "데이터 & 자동화",
                                "NumPy, Pandas, 시각화, 웹 스크래핑, API 호출",
                                "6~8주",
                            ],
                            [
                                "Vol.4",
                                "웹 & 배포",
                                "Flask/FastAPI, DB, Docker, CI/CD, 클라우드",
                                "6~8주",
                            ],
                            [
                                "Vol.5",
                                "ML & MLOps",
                                "Scikit-learn, 모델 학습, MLflow, 파이프라인 자동화",
                                "8~10주",
                            ],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "Vol.1", "sub": "Python 기초"},
                            {"label": "Vol.2", "sub": "Python 심화"},
                            {"label": "Vol.3", "sub": "데이터 분석"},
                            {"label": "Vol.4", "sub": "웹 & 배포"},
                            {"label": "Vol.5", "sub": "ML & MLOps"},
                        ],
                        "title": "Python Mastery Series 전체 로드맵",
                    },
                    {
                        "type": "note",
                        "text": (
                            "각 권의 기간은 매일 1~2시간 학습 기준입니다. "
                            "모든 권을 마치면 약 6~9개월이 소요되며, "
                            "이후 실무 프로젝트 경험을 더하면 "
                            "주니어 MLOps 엔지니어 수준에 도달할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: Python 자격증 안내 ──
            {
                "title": "C.5 Python 자격증 안내",
                "content": [
                    (
                        "Python Institute에서 운영하는 국제 자격증이 있습니다. "
                        "실력을 객관적으로 증명하고 싶을 때 도전해 보세요."
                    ),
                    {
                        "type": "table",
                        "headers": ["자격증", "정식 명칭", "난이도", "대상", "응시료"],
                        "rows": [
                            [
                                "PCEP",
                                "Certified Entry-Level Python Programmer",
                                "입문",
                                "Vol.1 완료 수준",
                                "약 $59",
                            ],
                            [
                                "PCAP",
                                "Certified Associate in Python Programming",
                                "중급",
                                "Vol.2 완료 수준 (OOP 포함)",
                                "약 $295",
                            ],
                            [
                                "PCPP1",
                                "Certified Professional in Python Programming 1",
                                "고급",
                                "Vol.3~4 수준 (고급 OOP, 네트워크)",
                                "약 $295",
                            ],
                        ],
                    },
                    "**PCEP 시험 구성:**",
                    {
                        "type": "bullet_list",
                        "items": [
                            "문항 수: 30문항 (객관식 + 빈칸 채우기)",
                            "시간: 45분",
                            "합격 기준: 70% 이상",
                            "응시 방법: Pearson VUE 온라인 또는 시험 센터",
                            "출제 범위: 기본 문법, 자료형, 제어문, 함수, 예외처리",
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "PCEP는 Vol.1의 내용만으로도 충분히 도전 가능합니다. "
                            "Python Institute 공식 사이트(pythoninstitute.org)에서 "
                            "무료 연습 문제를 풀어보고 실력을 점검하세요."
                        ),
                    },
                    (
                        "**한국 자격증:** "
                        "국내에서는 정보처리기사(필기 과목에 Python 포함)와 "
                        "ADP(Advanced Data Analytics Professional)가 있습니다. "
                        "정보처리기사는 CS 전공자에게 필수 자격증이며, "
                        "Vol.2~3 수준의 프로그래밍 지식이 필요합니다."
                    ),
                ],
            },
            # ── 섹션 6: MLOps 로드맵 미리보기 ──
            {
                "title": "C.6 MLOps 로드맵 미리보기",
                "content": [
                    (
                        "이 책의 최종 목표인 MLOps 엔지니어가 되기까지의 "
                        "전체 여정을 미리 살펴봅니다. "
                        "지금 당장 모든 것을 알 필요는 없지만, "
                        "어디로 가고 있는지 아는 것은 중요합니다."
                    ),
                    "**MLOps란?**",
                    (
                        "MLOps = Machine Learning + Operations의 합성어입니다. "
                        "머신러닝 모델을 개발하고, 배포하고, "
                        "운영하는 전체 생애주기를 관리하는 분야입니다."
                    ),
                    {
                        "type": "analogy",
                        "text": (
                            "요리에 비유하면: 데이터 과학자가 레시피(모델)를 만들고, "
                            "MLOps 엔지니어가 그 레시피를 대량 생산 가능한 "
                            "공장 라인(파이프라인)으로 만드는 역할입니다."
                        ),
                    },
                    "**단계별 로드맵:**",
                    {
                        "type": "flow_diagram",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "1단계: Python 기초", "sub": "Vol.1 (현재 위치)"},
                            {"label": "2단계: Python 심화", "sub": "Vol.2 — OOP, 파일, 패키지"},
                            {"label": "3단계: 데이터 분석", "sub": "Vol.3 — NumPy, Pandas"},
                            {"label": "4단계: 웹 & 인프라", "sub": "Vol.4 — Flask, Docker"},
                            {"label": "5단계: ML & MLOps", "sub": "Vol.5 — Scikit-learn, MLflow"},
                            {"label": "목표: 주니어 MLOps 엔지니어"},
                        ],
                        "title": "학습 로드맵",
                    },
                    "**단계별 필요 기술:**",
                    {
                        "type": "table",
                        "headers": ["단계", "핵심 기술", "도구/프레임워크"],
                        "rows": [
                            [
                                "1. Python 기초",
                                "프로그래밍 사고방식",
                                "Python, VS Code, Git",
                            ],
                            [
                                "2. Python 심화",
                                "OOP, 패키지 관리",
                                "pip, venv, pytest",
                            ],
                            [
                                "3. 데이터 분석",
                                "데이터 가공/시각화",
                                "NumPy, Pandas, Matplotlib",
                            ],
                            [
                                "4. 웹 & 인프라",
                                "API 개발, 컨테이너",
                                "FastAPI, Docker, GitHub Actions",
                            ],
                            [
                                "5. ML 기초",
                                "모델 학습/평가",
                                "Scikit-learn, XGBoost",
                            ],
                            [
                                "6. MLOps 실무",
                                "파이프라인 자동화",
                                "MLflow, Airflow, Kubernetes",
                            ],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "이 로드맵은 '최단 경로'가 아니라 '탄탄한 경로'입니다. "
                            "기초를 건너뛰고 MLOps로 바로 가려는 유혹을 이겨내세요. "
                            "Vol.1의 기초가 탄탄해야 Vol.5의 MLOps가 가능합니다."
                        ),
                    },
                    "**MLOps 엔지니어의 일상:**",
                    {
                        "type": "bullet_list",
                        "items": [
                            "데이터 파이프라인 구축 및 모니터링",
                            "ML 모델 학습 자동화 (재학습 스케줄링)",
                            "모델 성능 모니터링 및 드리프트 감지",
                            "A/B 테스트 환경 구성",
                            "모델 서빙 API 개발 및 최적화",
                            "인프라 관리 (Docker, Kubernetes, 클라우드)",
                        ],
                    },
                    (
                        "MLOps는 '코딩만 잘하면 되는' 분야가 아닙니다. "
                        "소프트웨어 공학, 데이터 과학, 인프라 운영의 "
                        "교차점에 있는 분야이기 때문에, "
                        "각 단계를 충실히 밟아가는 것이 가장 빠른 길입니다."
                    ),
                    {
                        "type": "tip",
                        "text": (
                            "지금 가장 중요한 것은 Vol.1을 완전히 이해하는 것입니다. "
                            "Ch9 미니 프로젝트를 스스로 확장해 보고, "
                            "부록 B의 실수를 모두 이해했다면, "
                            "Vol.2로 넘어갈 준비가 된 것입니다!"
                        ),
                    },
                ],
            },
        ],
    }
