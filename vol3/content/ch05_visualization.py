"""챕터 5: 데이터 시각화 — Matplotlib, Pandas 내장 시각화, Seaborn."""


def get_chapter():
    """챕터 5 콘텐츠를 반환한다."""
    return {
        "number": 5,
        "title": "데이터 시각화",
        "subtitle": "Matplotlib, Pandas 내장 시각화, Seaborn",
        "big_picture": (
            "숫자만 가득한 표는 패턴을 보기 어렵습니다. "
            "시각화는 데이터 안에 숨겨진 이야기를 그림으로 꺼내는 작업입니다. "
            "이 장에서는 Python 시각화의 기반인 Matplotlib 기초부터 시작하여 "
            "Pandas 내장 시각화, 그리고 통계 시각화 라이브러리 Seaborn까지 익힙니다. "
            "어떤 상황에 어떤 차트를 선택해야 하는지도 함께 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: Matplotlib 기초 ────────────────────────────
            {
                "title": "Matplotlib 기초: figure, axes, plot",
                "content": [
                    "Matplotlib은 Python 시각화의 근간이 되는 라이브러리입니다. "
                    "거의 모든 Python 시각화 도구가 Matplotlib 위에서 동작합니다. "
                    "먼저 Figure(도화지)와 Axes(그래프 영역)의 관계를 이해해야 합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "Figure는 액자 전체이고, Axes는 그 안의 그림 영역입니다. "
                            "하나의 Figure 안에 여러 Axes(서브플롯)를 배치할 수 있습니다. "
                            "액자 하나에 여러 사진을 넣는 것처럼요. "
                            "그림을 그리는 실제 작업은 항상 Axes 위에서 합니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["객체", "역할", "비유"],
                        "rows": [
                            ["Figure", "전체 그림 창", "액자 (캔버스)"],
                            ["Axes", "그래프가 그려지는 영역", "액자 안의 그림 한 칸"],
                            ["Axis", "x축 또는 y축", "그림의 눈금자"],
                            ["Artist", "선, 점, 텍스트 등 모든 요소", "그림 안의 각 요소"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import matplotlib.pyplot as plt\n"
                            "import matplotlib\n\n"
                            "# 한글 폰트 설정 (macOS)\n"
                            "matplotlib.rc('font', family='AppleGothic')\n"
                            "# Windows: matplotlib.rc('font', family='Malgun Gothic')\n"
                            "# 마이너스 기호 깨짐 방지\n"
                            "matplotlib.rcParams['axes.unicode_minus'] = False\n\n\n"
                            "# ── 방법 1: pyplot 인터페이스 (빠른 작성) ────────\n"
                            "plt.figure(figsize=(8, 5))   # 그림 크기 (인치 단위)\n"
                            "plt.plot([1, 2, 3, 4], [10, 20, 15, 30])  # 꺾은선 그래프\n"
                            "plt.title('간단한 선 그래프')\n"
                            "plt.xlabel('X축')\n"
                            "plt.ylabel('Y축')\n"
                            "plt.show()\n\n"
                            "# ── 방법 2: 객체 지향 인터페이스 (권장) ──────────\n"
                            "fig, ax = plt.subplots(figsize=(8, 5))\n"
                            "ax.plot([1, 2, 3, 4], [10, 20, 15, 30])\n"
                            "ax.set_title('객체 지향 방식')\n"
                            "ax.set_xlabel('X축')\n"
                            "ax.set_ylabel('Y축')\n"
                            "plt.tight_layout()  # 여백 자동 조정\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "plt.xxx() 방식과 ax.set_xxx() 방식 두 가지가 있습니다. "
                            "간단한 단일 그래프는 plt 방식도 괜찮지만, "
                            "서브플롯이나 복잡한 그래프는 반드시 객체 지향(ax) 방식을 사용하세요. "
                            "실무에서는 객체 지향 방식이 표준입니다."
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Jupyter Notebook에서는 첫 셀에 `%matplotlib inline`을 실행하면 "
                            "plt.show() 없이도 그래프가 자동으로 출력됩니다. "
                            "VS Code나 일반 Python 스크립트에서는 plt.show()가 필요합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 기본 차트 유형 ────────────────────────────
            {
                "title": "기본 차트: 선 그래프, 막대 그래프, 산점도, 히스토그램, 파이 차트",
                "content": [
                    "데이터의 특성에 맞는 차트를 선택하는 것이 시각화의 첫 번째 과제입니다. "
                    "각 차트 유형의 용도와 사용법을 익혀봅니다.",
                    {
                        "type": "table",
                        "headers": ["차트 유형", "함수", "적합한 데이터"],
                        "rows": [
                            ["선 그래프", "ax.plot()", "시계열, 추세"],
                            ["막대 그래프", "ax.bar() / ax.barh()", "범주형 비교"],
                            ["산점도", "ax.scatter()", "두 수치 변수 관계"],
                            ["히스토그램", "ax.hist()", "수치 분포"],
                            ["파이 차트", "ax.pie()", "비율/구성"],
                            ["박스플롯", "ax.boxplot()", "분포와 이상치"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import matplotlib.pyplot as plt\n"
                            "import numpy as np\n\n\n"
                            "# ── 선 그래프 — 시계열 데이터 ─────────────────\n"
                            "월 = ['1월', '2월', '3월', '4월', '5월', '6월']\n"
                            "매출_A = [1200, 1350, 1100, 1500, 1400, 1650]\n"
                            "매출_B = [980, 1050, 1200, 1100, 1300, 1250]\n\n"
                            "fig, ax = plt.subplots(figsize=(9, 5))\n"
                            "ax.plot(월, 매출_A, marker='o', label='A지점', linewidth=2)\n"
                            "ax.plot(월, 매출_B, marker='s', label='B지점', linewidth=2, linestyle='--')\n"
                            "ax.set_title('월별 지점 매출 추이', fontsize=14)\n"
                            "ax.set_xlabel('월')\n"
                            "ax.set_ylabel('매출액 (만원)')\n"
                            "ax.legend()\n"
                            "ax.grid(True, alpha=0.3)\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 막대 그래프 ────────────────────────────────\n"
                            "과목 = ['국어', '수학', '영어', '과학', '사회']\n"
                            "점수 = [85, 92, 78, 88, 76]\n\n"
                            "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n\n"
                            "# 세로 막대\n"
                            "bars = axes[0].bar(과목, 점수, color=['#3182F6', '#03B26C', '#F04452',\n"
                            "                                       '#FFC342', '#A234C7'])\n"
                            "axes[0].set_title('과목별 점수 (세로)')\n"
                            "axes[0].set_ylim(0, 110)\n"
                            "# 막대 위에 값 표시\n"
                            "for bar, val in zip(bars, 점수):\n"
                            "    axes[0].text(bar.get_x() + bar.get_width() / 2,\n"
                            "                 bar.get_height() + 1, str(val), ha='center')\n\n"
                            "# 가로 막대\n"
                            "axes[1].barh(과목, 점수, color='#3182F6')\n"
                            "axes[1].set_title('과목별 점수 (가로)')\n"
                            "axes[1].set_xlim(0, 110)\n\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 산점도와 히스토그램 ─────────────────────────\n"
                            "np.random.seed(42)\n"
                            "공부시간 = np.random.normal(5, 1.5, 100)\n"
                            "시험점수 = 공부시간 * 10 + np.random.normal(0, 5, 100)\n"
                            "시험점수 = np.clip(시험점수, 0, 100)\n\n"
                            "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n\n"
                            "# 산점도\n"
                            "axes[0].scatter(공부시간, 시험점수, alpha=0.6, color='#3182F6', s=40)\n"
                            "axes[0].set_title('공부시간 vs 시험점수')\n"
                            "axes[0].set_xlabel('공부시간 (시간)')\n"
                            "axes[0].set_ylabel('시험점수')\n\n"
                            "# 히스토그램\n"
                            "axes[1].hist(시험점수, bins=15, color='#03B26C', edgecolor='white',\n"
                            "             alpha=0.8)\n"
                            "axes[1].set_title('시험점수 분포')\n"
                            "axes[1].set_xlabel('점수')\n"
                            "axes[1].set_ylabel('빈도')\n"
                            "axes[1].axvline(시험점수.mean(), color='red', linestyle='--',\n"
                            "                label=f'평균: {시험점수.mean():.1f}')\n"
                            "axes[1].legend()\n\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                ],
            },
            # ── 섹션 3: 그래프 커스터마이징 ──────────────────────
            {
                "title": "그래프 커스터마이징: 제목, 라벨, 범례, 색상, 스타일",
                "content": [
                    "기본 그래프에 다양한 꾸밈을 추가하면 "
                    "데이터의 의미를 더욱 명확하게 전달할 수 있습니다. "
                    "전문적인 시각화를 위한 주요 커스터마이징 옵션을 익혀봅니다.",
                    {
                        "type": "table",
                        "headers": ["요소", "메서드", "주요 파라미터"],
                        "rows": [
                            ["제목", "ax.set_title()", "fontsize, fontweight, pad"],
                            ["축 라벨", "ax.set_xlabel/ylabel()", "fontsize, labelpad"],
                            ["눈금", "ax.set_xticks/yticks()", "—"],
                            ["눈금 라벨", "ax.set_xticklabels()", "rotation, fontsize"],
                            ["범례", "ax.legend()", "loc, fontsize, framealpha"],
                            ["격자", "ax.grid()", "True/False, alpha, linestyle"],
                            ["축 범위", "ax.set_xlim/ylim()", "(최솟값, 최댓값)"],
                            ["스타일", "plt.style.use()", "'seaborn', 'ggplot' 등"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import matplotlib.pyplot as plt\n"
                            "import numpy as np\n\n\n"
                            "# ── 스타일 설정 ──────────────────────────────────\n"
                            "# 사용 가능한 스타일 목록: plt.style.available\n"
                            "plt.style.use('seaborn-v0_8-whitegrid')  # 깔끔한 배경\n\n"
                            "# TDS 색상 팔레트 정의 (재사용 가능)\n"
                            "TDS_COLORS = {\n"
                            "    'primary': '#3182F6',   # blue500\n"
                            "    'success': '#03B26C',   # green500\n"
                            "    'danger': '#F04452',    # red500\n"
                            "    'warning': '#FE9800',   # orange500\n"
                            "    'purple': '#A234C7',    # purple500\n"
                            "}\n\n"
                            "# ── 종합 커스터마이징 예제 ────────────────────────\n"
                            "월 = list(range(1, 13))\n"
                            "매출 = [1200, 1350, 1100, 1500, 1400, 1650,\n"
                            "        1700, 1600, 1450, 1550, 1800, 2000]\n\n"
                            "fig, ax = plt.subplots(figsize=(11, 6))\n\n"
                            "# 선 그래프\n"
                            "ax.plot(월, 매출, color=TDS_COLORS['primary'],\n"
                            "        linewidth=2.5, marker='o', markersize=7,\n"
                            "        markerfacecolor='white', markeredgewidth=2,\n"
                            "        label='월별 매출')\n\n"
                            "# 평균선 추가\n"
                            "평균 = sum(매출) / len(매출)\n"
                            "ax.axhline(평균, color=TDS_COLORS['danger'],\n"
                            "           linestyle='--', linewidth=1.5,\n"
                            "           label=f'연평균 {평균:,.0f}만원')\n\n"
                            "# 최댓값 강조\n"
                            "max_idx = 매출.index(max(매출))\n"
                            "ax.annotate(f'최고 {max(매출):,}만원',\n"
                            "            xy=(월[max_idx], max(매출)),\n"
                            "            xytext=(월[max_idx] - 1.5, max(매출) + 80),\n"
                            "            arrowprops={'arrowstyle': '->', 'color': 'gray'},\n"
                            "            fontsize=10, color='gray')\n\n"
                            "# 제목과 라벨\n"
                            "ax.set_title('2024년 월별 매출 현황', fontsize=16,\n"
                            "             fontweight='bold', pad=15)\n"
                            "ax.set_xlabel('월', fontsize=12)\n"
                            "ax.set_ylabel('매출액 (만원)', fontsize=12)\n"
                            "ax.set_xticks(월)\n"
                            "ax.set_xticklabels([f'{m}월' for m in 월])\n"
                            "ax.legend(fontsize=11, framealpha=0.9)\n"
                            "ax.set_ylim(900, 2200)\n\n"
                            "plt.tight_layout()\n"
                            "plt.savefig('monthly_sales.png', dpi=150, bbox_inches='tight')\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "plt.savefig()는 plt.show() 이전에 호출해야 합니다. "
                            "show() 이후에는 Figure가 초기화되어 빈 파일이 저장됩니다. "
                            "dpi=150~300이 고품질 이미지 기준이며, bbox_inches='tight'는 "
                            "그래프 주변의 여백을 자동으로 잘라줍니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 서브플롯 ──────────────────────────────────
            {
                "title": "서브플롯: subplot, subplots로 여러 그래프 배치",
                "content": [
                    "하나의 Figure 안에 여러 그래프를 격자 형태로 배치하면 "
                    "데이터 간의 비교와 종합 분석이 훨씬 수월해집니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import matplotlib.pyplot as plt\n"
                            "import numpy as np\n\n\n"
                            "# ── plt.subplots(행, 열) ─────────────────────────\n"
                            "fig, axes = plt.subplots(2, 2, figsize=(12, 10))\n\n"
                            "np.random.seed(42)\n"
                            "데이터 = np.random.normal(0, 1, 200)\n"
                            "x = np.linspace(0, 10, 100)\n\n"
                            "# [0, 0] — 선 그래프\n"
                            "axes[0, 0].plot(x, np.sin(x), color='#3182F6')\n"
                            "axes[0, 0].set_title('사인 함수')\n\n"
                            "# [0, 1] — 히스토그램\n"
                            "axes[0, 1].hist(데이터, bins=20, color='#03B26C', edgecolor='white')\n"
                            "axes[0, 1].set_title('정규분포 히스토그램')\n\n"
                            "# [1, 0] — 산점도\n"
                            "axes[1, 0].scatter(데이터[:100], 데이터[100:], alpha=0.5, s=30,\n"
                            "                   color='#F04452')\n"
                            "axes[1, 0].set_title('산점도')\n\n"
                            "# [1, 1] — 박스플롯\n"
                            "데이터_그룹 = [np.random.normal(m, 1, 50) for m in [0, 1, 2, 3]]\n"
                            "axes[1, 1].boxplot(데이터_그룹, labels=['A', 'B', 'C', 'D'])\n"
                            "axes[1, 1].set_title('박스플롯')\n\n"
                            "fig.suptitle('다양한 차트 모음', fontsize=16, fontweight='bold', y=1.02)\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 불규칙한 레이아웃: GridSpec ──────────────────\n"
                            "from matplotlib.gridspec import GridSpec\n\n\n"
                            "fig = plt.figure(figsize=(12, 8))\n"
                            "gs = GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.3)\n\n"
                            "# 첫 행 전체 사용 (넓은 그래프)\n"
                            "ax_top = fig.add_subplot(gs[0, :])\n"
                            "월 = list(range(1, 13))\n"
                            "매출 = [1200, 1350, 1100, 1500, 1400, 1650,\n"
                            "        1700, 1600, 1450, 1550, 1800, 2000]\n"
                            "ax_top.plot(월, 매출, marker='o', color='#3182F6', linewidth=2)\n"
                            "ax_top.set_title('연간 매출 추이 (상단 전체)')\n\n"
                            "# 두 번째 행: 3개 서브플롯\n"
                            "for i, (제목, 색상) in enumerate([\n"
                            "    ('1분기', '#3182F6'), ('2분기', '#03B26C'), ('3분기', '#F04452')\n"
                            "]):\n"
                            "    ax = fig.add_subplot(gs[1, i])\n"
                            "    ax.bar(['A지점', 'B지점', 'C지점'],\n"
                            "           np.random.randint(500, 2000, 3), color=색상)\n"
                            "    ax.set_title(제목)\n\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "axes를 2D 배열로 받으면 axes[행, 열]로 접근합니다. "
                            "1행이나 1열만 있는 경우 axes[인덱스]로 접근합니다. "
                            "항상 2D 배열로 받으려면 subplots(squeeze=False)를 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: Pandas 내장 시각화와 Seaborn ─────────────
            {
                "title": "Pandas 내장 시각화와 Seaborn 소개",
                "content": [
                    "Pandas DataFrame은 Matplotlib을 직접 다루지 않고도 "
                    "df.plot()으로 빠르게 시각화할 수 있습니다. "
                    "Seaborn은 통계 시각화에 특화된 고수준 라이브러리로, "
                    "아름답고 정보량이 많은 그래프를 간결한 코드로 만들 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import pandas as pd\n"
                            "import matplotlib.pyplot as plt\n\n\n"
                            "# ── Pandas 내장 시각화: df.plot() ────────────────\n"
                            "df = pd.DataFrame({\n"
                            "    '월': list(range(1, 7)),\n"
                            "    '서울': [1200, 1350, 1100, 1500, 1400, 1650],\n"
                            "    '부산': [980, 1050, 1200, 1100, 1300, 1250],\n"
                            "    '대구': [750, 820, 780, 900, 850, 950],\n"
                            "}).set_index('월')\n\n"
                            "# 선 그래프\n"
                            "ax = df.plot(figsize=(10, 5), marker='o',\n"
                            "             title='월별 지점별 매출')\n"
                            "ax.set_xlabel('월')\n"
                            "ax.set_ylabel('매출액 (만원)')\n"
                            "plt.show()\n\n"
                            "# 막대 그래프\n"
                            "df.plot(kind='bar', figsize=(10, 5),\n"
                            "        title='월별 지점별 매출 (막대)')\n"
                            "plt.xticks(rotation=0)\n"
                            "plt.tight_layout()\n"
                            "plt.show()\n\n"
                            "# 누적 막대\n"
                            "df.plot(kind='bar', stacked=True, figsize=(10, 5),\n"
                            "        title='월별 지점별 매출 (누적 막대)')\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["kind 파라미터", "차트 유형"],
                        "rows": [
                            ["'line' (기본)", "선 그래프"],
                            ["'bar'", "세로 막대 그래프"],
                            ["'barh'", "가로 막대 그래프"],
                            ["'hist'", "히스토그램"],
                            ["'scatter'", "산점도 (x, y 파라미터 필요)"],
                            ["'pie'", "파이 차트"],
                            ["'box'", "박스플롯"],
                            ["'area'", "영역 그래프"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── Seaborn 소개 ─────────────────────────────────\n"
                            "import seaborn as sns\n"
                            "import pandas as pd\n"
                            "import numpy as np\n"
                            "import matplotlib.pyplot as plt\n\n\n"
                            "# Seaborn 테마 설정\n"
                            "sns.set_theme(style='whitegrid', palette='muted')\n\n"
                            "# 예제 데이터\n"
                            "np.random.seed(42)\n"
                            "학생 = pd.DataFrame({\n"
                            "    '공부시간': np.random.normal(5, 1.5, 150),\n"
                            "    '성적': np.random.normal(75, 12, 150),\n"
                            "    '학년': np.random.choice(['1학년', '2학년', '3학년'], 150),\n"
                            "    '전공': np.random.choice(['이공계', '인문계', '예체능'], 150),\n"
                            "})\n"
                            "학생['성적'] = np.clip(학생['성적'], 0, 100)\n\n"
                            "# ── heatmap — 상관관계 시각화 ─────────────────\n"
                            "수치형 = 학생[['공부시간', '성적']]\n"
                            "상관관계 = 수치형.corr()\n\n"
                            "fig, ax = plt.subplots(figsize=(5, 4))\n"
                            "sns.heatmap(상관관계, annot=True, fmt='.2f',\n"
                            "            cmap='RdBu_r', vmin=-1, vmax=1, ax=ax)\n"
                            "ax.set_title('변수 간 상관관계')\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── boxplot — 그룹별 분포 비교 ──────────────────\n"
                            "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n\n"
                            "sns.boxplot(data=학생, x='학년', y='성적',\n"
                            "            palette='Set2', ax=axes[0])\n"
                            "axes[0].set_title('학년별 성적 분포')\n\n"
                            "# ── countplot — 범주형 빈도 ──────────────────────\n"
                            "sns.countplot(data=학생, x='전공', hue='학년',\n"
                            "              palette='Set2', ax=axes[1])\n"
                            "axes[1].set_title('전공별 학년 구성')\n"
                            "axes[1].legend(title='학년')\n\n"
                            "plt.tight_layout()\n"
                            "plt.show()\n\n"
                            "# ── scatterplot — 두 수치 변수 관계 (hue로 그룹 구분) ─\n"
                            "fig, ax = plt.subplots(figsize=(8, 6))\n"
                            "sns.scatterplot(data=학생, x='공부시간', y='성적',\n"
                            "                hue='전공', style='학년',\n"
                            "                alpha=0.7, ax=ax)\n"
                            "ax.set_title('공부시간 vs 성적 (전공/학년 구분)')\n"
                            "plt.tight_layout()\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Seaborn은 Matplotlib 위에서 동작합니다. "
                            "Seaborn으로 그래프를 그린 뒤 ax 객체를 사용하여 "
                            "Matplotlib 커스터마이징을 추가로 적용할 수 있습니다. "
                            "두 라이브러리는 서로 호환됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 — 매출 대시보드 ─────────────────
            {
                "title": "실용 예제: 매출 대시보드 만들기",
                "content": [
                    "지금까지 배운 시각화 기법을 모두 활용하여 "
                    "실전 매출 대시보드를 만들어봅니다. "
                    "하나의 Figure 안에 여러 차트를 배치하여 "
                    "데이터의 다양한 측면을 한눈에 볼 수 있게 구성합니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import matplotlib.pyplot as plt\n"
                            "import matplotlib\n"
                            "import pandas as pd\n"
                            "import numpy as np\n\n\n"
                            "matplotlib.rc('font', family='AppleGothic')\n"
                            "matplotlib.rcParams['axes.unicode_minus'] = False\n"
                            "plt.style.use('seaborn-v0_8-whitegrid')\n\n"
                            "# ── 데이터 준비 ─────────────────────────────────\n"
                            "np.random.seed(42)\n"
                            "월_목록 = [f'{m}월' for m in range(1, 13)]\n"
                            "지점_목록 = ['강남', '홍대', '판교', '부산']\n\n"
                            "매출_df = pd.DataFrame(\n"
                            "    np.random.randint(800, 2500, (12, 4)),\n"
                            "    index=월_목록,\n"
                            "    columns=지점_목록,\n"
                            ")\n"
                            "제품_매출 = pd.Series(\n"
                            "    [4200, 3100, 1800, 2600, 900],\n"
                            "    index=['노트북', '스마트폰', '태블릿', '모니터', '기타'],\n"
                            ")"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 대시보드 레이아웃 구성 ───────────────────────\n"
                            "from matplotlib.gridspec import GridSpec\n\n\n"
                            "fig = plt.figure(figsize=(16, 10),\n"
                            "                 facecolor='#F9FAFB')  # grey50\n"
                            "fig.suptitle('2024년 매출 현황 대시보드',\n"
                            "             fontsize=18, fontweight='bold',\n"
                            "             y=0.98, color='#191F28')\n\n"
                            "gs = GridSpec(2, 3, figure=fig,\n"
                            "              hspace=0.45, wspace=0.35,\n"
                            "              left=0.06, right=0.97,\n"
                            "              top=0.92, bottom=0.07)\n\n"
                            "TDS = {'primary': '#3182F6', 'success': '#03B26C',\n"
                            "       'danger': '#F04452', 'warning': '#FE9800',\n"
                            "       'purple': '#A234C7'}\n\n"
                            "# ── 그래프 1: 월별 전체 매출 추이 (상단 전체) ────\n"
                            "ax1 = fig.add_subplot(gs[0, :])\n"
                            "총매출 = 매출_df.sum(axis=1)\n"
                            "ax1.fill_between(월_목록, 총매출, alpha=0.15, color=TDS['primary'])\n"
                            "ax1.plot(월_목록, 총매출, marker='o', color=TDS['primary'],\n"
                            "         linewidth=2.5, markersize=8)\n"
                            "평균 = 총매출.mean()\n"
                            "ax1.axhline(평균, color=TDS['danger'], linestyle='--',\n"
                            "            linewidth=1.5, label=f'연평균 {평균:,.0f}만원')\n"
                            "ax1.set_title('월별 전체 매출 추이', fontsize=13, pad=10)\n"
                            "ax1.set_ylabel('매출액 (만원)')\n"
                            "ax1.legend(fontsize=10)\n"
                            "ax1.tick_params(axis='x', rotation=0)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 그래프 2: 지점별 연간 매출 막대 (하단 좌) ────\n"
                            "ax2 = fig.add_subplot(gs[1, 0])\n"
                            "지점별_합계 = 매출_df.sum()\n"
                            "colors = [TDS['primary'], TDS['success'],\n"
                            "          TDS['warning'], TDS['purple']]\n"
                            "bars = ax2.bar(지점별_합계.index, 지점별_합계.values,\n"
                            "               color=colors, edgecolor='white', linewidth=0.5)\n"
                            "for bar, val in zip(bars, 지점별_합계.values):\n"
                            "    ax2.text(bar.get_x() + bar.get_width() / 2,\n"
                            "             bar.get_height() + 50,\n"
                            "             f'{val:,}', ha='center', fontsize=9)\n"
                            "ax2.set_title('지점별 연간 매출', fontsize=12)\n"
                            "ax2.set_ylabel('매출액 (만원)')\n\n"
                            "# ── 그래프 3: 제품별 매출 파이 (하단 중) ──────────\n"
                            "ax3 = fig.add_subplot(gs[1, 1])\n"
                            "wedges, texts, autotexts = ax3.pie(\n"
                            "    제품_매출.values,\n"
                            "    labels=제품_매출.index,\n"
                            "    autopct='%1.1f%%',\n"
                            "    colors=[TDS['primary'], TDS['success'], TDS['warning'],\n"
                            "             TDS['purple'], '#B0B8C1'],\n"
                            "    startangle=90,\n"
                            "    pctdistance=0.8,\n"
                            ")\n"
                            "for text in autotexts:\n"
                            "    text.set_fontsize(9)\n"
                            "ax3.set_title('제품별 매출 비중', fontsize=12)\n\n"
                            "# ── 그래프 4: 지점별 누적 막대 (하단 우) ──────────\n"
                            "ax4 = fig.add_subplot(gs[1, 2])\n"
                            "분기_df = pd.DataFrame({\n"
                            "    'Q1': 매출_df.iloc[0:3].sum(),\n"
                            "    'Q2': 매출_df.iloc[3:6].sum(),\n"
                            "    'Q3': 매출_df.iloc[6:9].sum(),\n"
                            "    'Q4': 매출_df.iloc[9:12].sum(),\n"
                            "}).T\n"
                            "분기_df.plot(kind='bar', stacked=True, ax=ax4,\n"
                            "             color=colors, edgecolor='white',\n"
                            "             linewidth=0.5, legend=True)\n"
                            "ax4.set_title('분기별 지점 누적 매출', fontsize=12)\n"
                            "ax4.set_xlabel('')\n"
                            "ax4.set_ylabel('매출액 (만원)')\n"
                            "ax4.tick_params(axis='x', rotation=0)\n"
                            "ax4.legend(title='지점', fontsize=8, title_fontsize=9)\n\n"
                            "plt.savefig('sales_dashboard.png', dpi=150,\n"
                            "            bbox_inches='tight', facecolor=fig.get_facecolor())\n"
                            "plt.show()"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "대시보드를 만들 때는 색상 일관성이 중요합니다. "
                            "TDS 팔레트처럼 미리 색상 딕셔너리를 정의해두고 재사용하면 "
                            "일관된 스타일을 유지할 수 있습니다. "
                            "배경색(facecolor)을 grey50(#F9FAFB)으로 설정하면 "
                            "더 전문적인 대시보드 느낌이 납니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "차트 유형 선택 원칙: 추세는 선 그래프, 비교는 막대, 분포는 히스토그램/박스플롯, 관계는 산점도.",
            "한글이 깨질 때: matplotlib.rc('font', family='AppleGothic')과 axes.unicode_minus=False를 설정하세요.",
            "plt.savefig()는 plt.show() 이전에 호출해야 파일이 제대로 저장됩니다.",
            "Pandas df.plot()은 빠른 탐색에 유용하고, 세밀한 제어가 필요할 때는 Matplotlib 객체 지향 방식을 사용하세요.",
            "Seaborn은 통계 시각화에 강력합니다. hue, style 파라미터로 그룹 정보를 차트에 자연스럽게 담을 수 있습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "Matplotlib에서 Figure와 Axes의 관계를 올바르게 설명한 것은?"
                ),
                "choices": [
                    "A) Figure는 그래프 영역이고, Axes는 전체 창이다",
                    "B) Figure는 전체 창(액자)이고, Axes는 그 안의 그래프 영역이다",
                    "C) 둘은 동일한 개념이다",
                    "D) Axes는 x축과 y축만을 의미한다",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "plt.savefig()를 plt.show() 이후에 호출하면 어떤 문제가 발생하는가?"
                ),
                "choices": [
                    "A) 파일이 저장되지 않는다",
                    "B) 빈 그림이 저장된다",
                    "C) 오류가 발생한다",
                    "D) 더 고화질로 저장된다",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "Seaborn의 heatmap을 사용할 때 annot=True의 의미는?"
                ),
                "choices": [
                    "A) 축 라벨을 자동으로 설정한다",
                    "B) 각 셀에 수치 값을 표시한다",
                    "C) 색상 범례를 숨긴다",
                    "D) 행과 열 이름을 표시한다",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "5개 도시의 월별 기온 데이터(12개월)를 생성하여 "
                    "① 선 그래프로 추이를 나타내고, "
                    "② 각 도시의 연평균 기온 막대 그래프를 "
                    "하나의 Figure 안에 subplots으로 배치하세요."
                ),
                "hint": "fig, axes = plt.subplots(1, 2, figsize=(14, 5))로 시작하세요.",
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "DataFrame에서 수치형 컬럼들의 상관관계를 Seaborn heatmap으로 시각화하고, "
                    "두 컬럼 간의 산점도에 회귀선을 추가(sns.regplot)하세요."
                ),
                "hint": "상관관계: df.corr(). 회귀선 포함 산점도: sns.regplot(data=df, x='col1', y='col2')",
            },
        ],
        "challenge": {
            "question": (
                "학생 성적 데이터(10명 이상, 국어/수학/영어/과학 포함)를 분석하는 "
                "4개 차트로 구성된 종합 시각화 보고서를 만드세요. "
                "① 과목별 평균 점수 가로 막대 그래프. "
                "② 학생별 총점 분포 히스토그램 (평균선 포함). "
                "③ 수학 vs 영어 산점도 (등급별 색상 구분). "
                "④ 과목별 점수 분포 박스플롯. "
                "모든 차트에 적절한 제목, 라벨, 범례를 추가하고 "
                "파일로 저장하세요."
            ),
            "hint": (
                "GridSpec 또는 subplots(2, 2)로 2x2 레이아웃을 구성하세요. "
                "산점도의 등급별 색상은 등급 컬럼을 만든 뒤 "
                "map()으로 색상 딕셔너리를 매핑하거나 Seaborn scatterplot의 hue 파라미터를 사용하세요."
            ),
        },
        "summary": [
            "Matplotlib의 핵심 구조는 Figure(전체 창)와 Axes(그래프 영역)이며, 객체 지향 방식(ax)이 표준이다.",
            "차트 유형 선택: 추세→선, 비교→막대, 분포→히스토그램/박스, 관계→산점도, 비율→파이.",
            "set_title, set_xlabel, legend, grid, annotate 등으로 그래프를 상세하게 커스터마이징한다.",
            "subplots(행, 열)과 GridSpec으로 여러 그래프를 하나의 Figure에 배치한다.",
            "df.plot()은 빠른 탐색에, Matplotlib 직접 사용은 세밀한 제어에 적합하다.",
            "Seaborn은 heatmap, boxplot, countplot, scatterplot 등 통계 시각화를 간결한 코드로 제공한다.",
        ],
    }
