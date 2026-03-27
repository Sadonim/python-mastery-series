"""
Python Mastery Series Vol.1 — 디자인 토큰 & 스타일 정의
TDS(Toss Design System) 기반 블루-그레이 뉴트럴 톤
"""

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# ── 페이지 설정 ──────────────────────────────────────────────
PAGE_SIZE = A4
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
MARGIN_TOP = 25 * mm
MARGIN_BOTTOM = 20 * mm
MARGIN_LEFT = 22 * mm
MARGIN_RIGHT = 22 * mm
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

# ── 폰트 경로 ────────────────────────────────────────────────
FONT_DIR = "/Users/sadonim/Desktop/python-mastery-series/vol1/assets/fonts"
FONT_KOREAN = f"{FONT_DIR}/NotoSansKR-Variable.ttf"
FONT_CODE = "Courier"

# ── 컬러 팔레트 (TDS 기반 블루-그레이 뉴트럴) ──────────────
class Colors:
    # 텍스트
    TEXT_PRIMARY = HexColor("#333D4B")      # grey800
    TEXT_SECONDARY = HexColor("#6B7684")    # grey600
    TEXT_TERTIARY = HexColor("#8B95A1")     # grey500
    TEXT_INVERSE = HexColor("#FFFFFF")

    # 배경
    BG_PAGE = HexColor("#FFFFFF")
    BG_CARD = HexColor("#F2F4F6")           # grey100
    BG_CODE = HexColor("#F5F7FA")           # 코드 블록 배경
    BG_TIP = HexColor("#E8F3FF")            # blue50 (팁 박스)
    BG_NOTE = HexColor("#FFF3E0")           # orange50 (노트 박스)
    BG_WARNING = HexColor("#FFEEEE")        # red50 (경고 박스)
    BG_CHAPTER_HEADER = HexColor("#2C3E50") # 챕터 헤더 배경
    BG_EXERCISE = HexColor("#F0FAF6")       # green50 (연습문제)
    BG_SUMMARY = HexColor("#F9FAFB")        # grey50

    # 강조
    ACCENT_BLUE = HexColor("#3182F6")       # blue500 (주 강조)
    ACCENT_TEAL = HexColor("#18A5A5")       # teal500 (보조 강조)
    ACCENT_GREEN = HexColor("#03B26C")      # green500 (성공)
    ACCENT_ORANGE = HexColor("#FE9800")     # orange500 (경고)
    ACCENT_RED = HexColor("#F04452")        # red500 (위험)

    # 테두리
    BORDER_DEFAULT = HexColor("#E5E8EB")    # grey200
    BORDER_CODE = HexColor("#D1D6DB")       # grey300
    BORDER_STRONG = HexColor("#B0B8C1")     # grey400

    # 챕터별 악센트 컬러 (좌측 스트라이프 + 아이콘)
    CHAPTER_COLORS = [
        HexColor("#3182F6"),  # Ch0: 블루
        HexColor("#18A5A5"),  # Ch1: 틸
        HexColor("#A234C7"),  # Ch2: 퍼플
        HexColor("#03B26C"),  # Ch3: 그린
        HexColor("#FE9800"),  # Ch4: 오렌지
        HexColor("#3182F6"),  # Ch5: 블루
        HexColor("#18A5A5"),  # Ch6: 틸
        HexColor("#A234C7"),  # Ch7: 퍼플
        HexColor("#03B26C"),  # Ch8: 그린
        HexColor("#F04452"),  # Ch9: 레드 (프로젝트)
    ]


# ── 타이포그래피 ──────────────────────────────────────────────
class Typography:
    # 챕터 타이틀 (표지용)
    CHAPTER_NUM_SIZE = 48
    CHAPTER_TITLE_SIZE = 28
    CHAPTER_SUBTITLE_SIZE = 16

    # 섹션 제목
    H1_SIZE = 22        # 대제목
    H2_SIZE = 17        # 중제목
    H3_SIZE = 14        # 소제목

    # 본문
    BODY_SIZE = 11
    BODY_LEADING = 18   # 줄간격
    CODE_SIZE = 9.5
    CODE_LEADING = 14

    # 기타
    CAPTION_SIZE = 9
    LABEL_SIZE = 10
    FOOTER_SIZE = 8
    TOC_SIZE = 11
    TOC_CHAPTER_SIZE = 13


# ── 간격 토큰 ────────────────────────────────────────────────
class Spacing:
    XS = 2 * mm     # 미세 간격
    SM = 4 * mm      # 작은 간격
    MD = 8 * mm      # 기본 간격
    LG = 12 * mm     # 큰 간격
    XL = 16 * mm     # 섹션 간 간격
    XXL = 24 * mm    # 챕터 간 간격

    # 컴포넌트별
    CODE_PADDING = 10    # 코드 블록 내부 패딩 (pt)
    BOX_PADDING = 8      # 박스 내부 패딩 (pt)
    TABLE_CELL_PAD = 6   # 테이블 셀 패딩 (pt)
