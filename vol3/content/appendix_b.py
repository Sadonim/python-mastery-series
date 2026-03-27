"""
부록 B: Matplotlib 스타일 가이드
"""


def get_appendix():
    return {
        "title": "부록 B: Matplotlib 스타일 가이드",
        "sections": [
            _section_chart_types(),
            _section_color_palette(),
            _section_best_practices(),
            _section_korean_font(),
        ],
    }


def _section_chart_types():
    return {
        "title": "차트 유형별 사용 가이드",
        "content": [
            "데이터의 특성에 맞는 차트를 선택하는 것이 효과적인 시각화의 첫걸음입니다.",
            {
                "type": "table",
                "headers": ["차트 유형", "사용 시기", "Matplotlib 함수"],
                "rows": [
                    ["선 그래프 (Line)", "시간에 따른 변화 추이", "plt.plot()"],
                    ["막대 그래프 (Bar)", "카테고리별 비교", "plt.bar() / plt.barh()"],
                    ["산점도 (Scatter)", "두 변수 간 관계", "plt.scatter()"],
                    ["히스토그램 (Histogram)", "데이터 분포 확인", "plt.hist()"],
                    ["파이 차트 (Pie)", "전체 대비 비율 (5개 이하)", "plt.pie()"],
                    ["박스플롯 (Box)", "분포 + 이상치 확인", "plt.boxplot()"],
                    ["히트맵 (Heatmap)", "상관관계 / 행렬 데이터", "sns.heatmap()"],
                ],
            },
            {
                "type": "warning",
                "text": (
                    "파이 차트는 항목이 5개를 초과하면 가독성이 떨어집니다. "
                    "6개 이상이면 막대 그래프를 사용하세요."
                ),
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "import matplotlib.pyplot as plt\n"
                    "import numpy as np\n\n"
                    "# 기본 4종 차트 한 번에 그리기\n"
                    "fig, axes = plt.subplots(2, 2, figsize=(10, 8))\n\n"
                    "# 선 그래프\n"
                    "x = np.arange(10)\n"
                    "axes[0, 0].plot(x, x**2, marker='o')\n"
                    "axes[0, 0].set_title('선 그래프')\n\n"
                    "# 막대 그래프\n"
                    "categories = ['A', 'B', 'C', 'D']\n"
                    "values = [25, 40, 30, 55]\n"
                    "axes[0, 1].bar(categories, values, color='#3182F6')\n"
                    "axes[0, 1].set_title('막대 그래프')\n\n"
                    "# 산점도\n"
                    "axes[1, 0].scatter(np.random.randn(50), np.random.randn(50))\n"
                    "axes[1, 0].set_title('산점도')\n\n"
                    "# 히스토그램\n"
                    "axes[1, 1].hist(np.random.randn(1000), bins=30, color='#03B26C')\n"
                    "axes[1, 1].set_title('히스토그램')\n\n"
                    "plt.tight_layout()\n"
                    "plt.savefig('chart_examples.png', dpi=150)\n"
                    "plt.show()"
                ),
            },
        ],
    }


def _section_color_palette():
    return {
        "title": "색상 팔레트 추천",
        "content": [
            "일관된 색상 사용은 시각화의 전문성을 높여줍니다.",
            {"type": "heading", "text": "TDS 기반 추천 색상"},
            {
                "type": "table",
                "headers": ["용도", "색상명", "Hex 코드"],
                "rows": [
                    ["주요 데이터", "Blue", "#3182F6"],
                    ["보조 데이터", "Teal", "#18A5A5"],
                    ["성공/증가", "Green", "#03B26C"],
                    ["경고/주의", "Orange", "#FE9800"],
                    ["위험/감소", "Red", "#F04452"],
                    ["중립/배경", "Grey", "#8B95A1"],
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# TDS 색상 팔레트 정의\n"
                    "TDS_COLORS = {\n"
                    "    'blue': '#3182F6',\n"
                    "    'teal': '#18A5A5',\n"
                    "    'green': '#03B26C',\n"
                    "    'orange': '#FE9800',\n"
                    "    'red': '#F04452',\n"
                    "    'purple': '#A234C7',\n"
                    "}\n\n"
                    "# 사용 예시\n"
                    "colors = list(TDS_COLORS.values())\n"
                    "plt.bar(['A', 'B', 'C', 'D', 'E', 'F'],\n"
                    "        [10, 25, 15, 30, 20, 35],\n"
                    "        color=colors)"
                ),
            },
            {"type": "heading", "text": "Seaborn 내장 팔레트"},
            {
                "type": "table",
                "headers": ["팔레트 이름", "특징", "사용 시기"],
                "rows": [
                    ["deep", "진한 색조, 기본값", "일반적인 시각화"],
                    ["pastel", "부드러운 파스텔톤", "프레젠테이션용"],
                    ["Set2", "구분이 명확한 8색", "카테고리 비교"],
                    ["coolwarm", "파랑↔빨강 그라디언트", "상관관계 히트맵"],
                    ["viridis", "색각 이상자 친화적", "연속 데이터"],
                ],
            },
        ],
    }


def _section_best_practices():
    return {
        "title": "그래프 꾸미기 베스트 프랙티스",
        "content": [
            {
                "type": "numbered_list",
                "items": [
                    "**제목은 반드시 포함** — 그래프가 무엇을 보여주는지 명확히",
                    "**축 라벨 필수** — x축과 y축이 무엇을 나타내는지",
                    "**범례 위치 최적화** — 데이터를 가리지 않는 위치에 배치",
                    "**불필요한 요소 제거** — 3D 효과, 과도한 그리드 제거",
                    "**적절한 그래프 크기** — figsize로 가독성 확보",
                    "**DPI 설정** — 인쇄/발표용은 150~300 DPI",
                ],
            },
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# 깔끔한 그래프 템플릿\n"
                    "fig, ax = plt.subplots(figsize=(8, 5))\n\n"
                    "# 데이터 그리기\n"
                    "ax.plot(x, y, color='#3182F6', linewidth=2, label='매출')\n\n"
                    "# 꾸미기\n"
                    "ax.set_title('월별 매출 추이', fontsize=14, fontweight='bold')\n"
                    "ax.set_xlabel('월', fontsize=11)\n"
                    "ax.set_ylabel('매출 (만원)', fontsize=11)\n"
                    "ax.legend(loc='upper left')\n"
                    "ax.grid(axis='y', alpha=0.3)  # y축 그리드만\n"
                    "ax.spines['top'].set_visible(False)    # 상단 테두리 제거\n"
                    "ax.spines['right'].set_visible(False)  # 우측 테두리 제거\n\n"
                    "plt.tight_layout()\n"
                    "plt.savefig('clean_chart.png', dpi=150, bbox_inches='tight')"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "`plt.style.use('seaborn-v0_8-whitegrid')`를 사용하면 "
                    "기본 스타일보다 훨씬 깔끔한 그래프를 만들 수 있습니다."
                ),
            },
        ],
    }


def _section_korean_font():
    return {
        "title": "한글 폰트 설정 방법",
        "content": [
            "Matplotlib은 기본적으로 한글을 지원하지 않아 별도 설정이 필요합니다.",
            {"type": "heading", "text": "macOS"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "import matplotlib.pyplot as plt\n\n"
                    "# macOS: AppleGothic 사용\n"
                    "plt.rcParams['font.family'] = 'AppleGothic'\n"
                    "plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지"
                ),
            },
            {"type": "heading", "text": "Windows"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "# Windows: Malgun Gothic 사용\n"
                    "plt.rcParams['font.family'] = 'Malgun Gothic'\n"
                    "plt.rcParams['axes.unicode_minus'] = False"
                ),
            },
            {"type": "heading", "text": "범용 (Noto Sans KR)"},
            {
                "type": "code",
                "language": "python",
                "code": (
                    "from matplotlib import font_manager, rc\n\n"
                    "# Noto Sans KR 폰트 경로 지정\n"
                    "font_path = '/path/to/NotoSansKR-Regular.ttf'\n"
                    "font_manager.fontManager.addfont(font_path)\n"
                    "rc('font', family='Noto Sans KR')\n"
                    "plt.rcParams['axes.unicode_minus'] = False"
                ),
            },
            {
                "type": "note",
                "text": (
                    "`axes.unicode_minus = False`를 반드시 설정하세요. "
                    "그렇지 않으면 음수 부호(-)가 네모(□)로 표시됩니다."
                ),
            },
        ],
    }
