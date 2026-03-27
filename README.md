# Python Mastery Series

CS/SW 학과 1학년, 군 전문인력, Python 완전 초보자를 위한 **한국어 Python 교육 시리즈**.

MLOps 엔지니어를 목표로 기초부터 실무까지 단계적으로 학습할 수 있도록 설계되었습니다.

## Volumes

| Volume | Title | Pages | Status |
|--------|-------|-------|--------|
| Vol.1 | **Python 입문** — 변수, 함수, 자료구조, 모듈 | ~180p | Done |
| Vol.2 | **Python 심화** — OOP, 예외처리, 정규표현식, 파일 I/O | ~180p | Planned |
| Vol.3 | **데이터 분석** — NumPy, Pandas, 시각화, API | ~180p | Planned |
| Vol.4 | **웹 & 배포** — Flask/FastAPI, Docker, CI/CD | ~180p | Planned |
| Vol.5 | **ML & MLOps** — Scikit-learn, MLflow, 파이프라인 | ~180p | Planned |

## PDF Generation

각 볼륨 폴더에서:

```bash
pip install reportlab
python3 generate.py
```

출력: `output/python_mastery_vol1.pdf`

## Design

- TDS(Toss Design System) 기반 블루-그레이 뉴트럴 톤
- 한국어 본문 + 한국어 코드 주석
- 그래픽 FlowDiagram 컴포넌트 (둥근 박스 + 화살표)
- 챕터별 악센트 컬러 시스템

## Target Audience

- CS/SW 학과 1학년 학생
- 군 전문인력 (개발 직무)
- Python 완전 초보 → MLOps 엔지니어 목표

## Font

한국어 렌더링을 위해 [Noto Sans KR](https://fonts.google.com/noto/specimen/Noto+Sans+KR) 폰트가 필요합니다.
`vol1/assets/fonts/NotoSansKR-Variable.ttf`에 포함되어 있습니다.

## License

Educational use. Content is in Korean.
