"""
부록 C: Vol.4 미리보기 & 학습 전략
"""


def get_appendix():
    return {
        "title": "부록 C: Vol.4 미리보기 & 학습 전략",
        "sections": [
            _section_checklist(),
            _section_vol4_preview(),
            _section_resources(),
            _section_roadmap(),
        ],
    }


def _section_checklist():
    return {
        "title": "Vol.3 마무리 체크리스트",
        "content": [
            "Vol.4로 넘어가기 전에 아래 항목을 확인하세요.",
            {
                "type": "table",
                "headers": ["항목", "확인 기준", "체크"],
                "rows": [
                    ["NumPy", "ndarray 생성, 인덱싱, 브로드캐스팅 이해", "[ ]"],
                    ["Pandas 기초", "DataFrame 생성, 조회, 필터링 가능", "[ ]"],
                    ["Pandas 심화", "groupby, merge, pivot_table 활용", "[ ]"],
                    ["시각화", "Matplotlib으로 기본 5종 차트 생성", "[ ]"],
                    ["API", "requests로 REST API 호출 가능", "[ ]"],
                    ["스크래핑", "BeautifulSoup으로 웹 데이터 추출", "[ ]"],
                    ["파이프라인", "ETL 파이프라인 구축 경험", "[ ]"],
                    ["미니 프로젝트", "Ch9 프로젝트 완성", "[ ]"],
                ],
            },
            {
                "type": "tip",
                "text": (
                    "체크리스트에서 2개 이상 부족하다면 해당 챕터를 복습하세요. "
                    "데이터 분석 기초가 탄탄해야 Vol.4의 웹/배포 내용을 잘 소화할 수 있습니다."
                ),
            },
        ],
    }


def _section_vol4_preview():
    return {
        "title": "Vol.4: 웹 & 배포 미리보기",
        "content": [
            (
                "Vol.4에서는 Python으로 만든 프로그램을 실제 서비스로 배포하는 방법을 다룹니다. "
                "웹 프레임워크, 컨테이너화, CI/CD, 클라우드 배포까지 실무 기술을 배웁니다."
            ),
            {
                "type": "table",
                "headers": ["챕터", "주제", "핵심 기술"],
                "rows": [
                    ["Ch 1-2", "Flask 웹 개발", "라우팅, 템플릿, REST API"],
                    ["Ch 3-4", "FastAPI", "비동기, 타입 검증, Swagger"],
                    ["Ch 5", "데이터베이스", "SQLite, SQLAlchemy ORM"],
                    ["Ch 6", "Docker", "컨테이너, 이미지, docker-compose"],
                    ["Ch 7", "테스트 & CI/CD", "pytest, GitHub Actions"],
                    ["Ch 8", "클라우드 배포", "AWS/GCP 기초, 배포 자동화"],
                    ["Ch 9", "프로젝트", "API 서버 + Docker + CI/CD"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "title": "Vol.4 맛보기: FastAPI로 API 서버 만들기",
                "code": (
                    "from fastapi import FastAPI\n\n"
                    "app = FastAPI()\n\n"
                    "@app.get('/hello')\n"
                    "def hello():\n"
                    "    return {'message': '안녕하세요!'}\n\n"
                    "# 실행: uvicorn main:app --reload\n"
                    "# 자동 API 문서: http://localhost:8000/docs"
                ),
            },
        ],
    }


def _section_resources():
    return {
        "title": "추천 학습 자료",
        "content": [
            {
                "type": "table",
                "headers": ["분류", "이름", "특징"],
                "rows": [
                    ["공식 문서", "Flask 한국어 문서", "가벼운 웹 프레임워크"],
                    ["공식 문서", "FastAPI 공식 튜토리얼", "인터랙티브 학습 가능"],
                    ["공식 문서", "Docker Docs - Get Started", "컨테이너 기초"],
                    ["도서", "Two Scoops of Django", "Python 웹 베스트 프랙티스"],
                    ["도서", "Docker in Action", "Docker 실전 활용"],
                    ["강좌", "점프 투 FastAPI", "무료 온라인 한국어 강좌"],
                    ["실습", "GitHub Actions 공식 가이드", "CI/CD 파이프라인 구축"],
                ],
            },
            {
                "type": "note",
                "text": (
                    "Flask와 FastAPI 중 하나만 익혀도 충분합니다. "
                    "MLOps 목표라면 FastAPI를 추천합니다 — 비동기 지원과 "
                    "자동 API 문서 생성이 ML 모델 서빙에 적합합니다."
                ),
            },
        ],
    }


def _section_roadmap():
    return {
        "title": "전체 로드맵",
        "content": [
            "Python Mastery Series 5권 전체 학습 경로입니다.",
            {
                "type": "flow_diagram",
                "direction": "vertical",
                "nodes": [
                    {"label": "Vol.1: Python 기초", "sub": "변수, 함수, 자료구조"},
                    {"label": "Vol.2: Python 심화", "sub": "OOP, 예외, 데코레이터"},
                    {"label": "Vol.3: 데이터 분석", "sub": "NumPy, Pandas, 시각화 (현재)"},
                    {"label": "Vol.4: 웹 & 배포", "sub": "Flask, Docker, CI/CD"},
                    {"label": "Vol.5: ML & MLOps", "sub": "Scikit-learn, MLflow"},
                ],
                "title": "Python Mastery Series 학습 로드맵",
                "note": "현재 Vol.3 완료 — 다음은 Vol.4 웹 & 배포",
            },
            {
                "type": "tip",
                "text": (
                    "각 Volume은 이전 Volume의 지식을 기반으로 합니다. "
                    "건너뛰지 말고 순서대로 학습하세요."
                ),
            },
        ],
    }
