"""
커스텀 Flowable 컴포넌트 — CoverPage, ColoredBox, ChapterTitlePage, FlowDiagram
"""

import math

from reportlab.platypus import Flowable
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

from pdf_styles import (
    Colors, Typography,
    PAGE_WIDTH, PAGE_HEIGHT, MARGIN_LEFT, MARGIN_RIGHT,
    MARGIN_TOP, MARGIN_BOTTOM, CONTENT_WIDTH
)


class CoverPage(Flowable):
    """표지 페이지 — 상단 컬러 밴드 + 기하학적 장식"""

    def wrap(self, available_width, available_height):
        return available_width, available_height

    def draw(self):
        c = self.canv
        w = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
        h = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

        # ── 상단 넓은 컬러 밴드 (35%) ──
        band_h = h * 0.35
        c.setFillColor(Colors.ACCENT_BLUE)
        c.rect(-MARGIN_LEFT, h - band_h,
               PAGE_WIDTH, band_h + MARGIN_TOP, fill=1, stroke=0)

        # ── 밴드 위 기하학적 장식: 원형 ──
        c.saveState()
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFillAlpha(0.06)
        c.circle(w * 0.85, h - band_h * 0.4, 80, fill=1, stroke=0)
        c.circle(w * 0.7, h - band_h * 0.15, 40, fill=1, stroke=0)
        c.circle(w * 0.95, h - band_h * 0.7, 25, fill=1, stroke=0)
        c.restoreState()

        # ── 밴드 내 시리즈명 ──
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFillAlpha(0.7)
        c.setFont("Korean", 13)
        c.drawString(0, h - 35, "PYTHON MASTERY SERIES")
        c.setFillAlpha(1.0)

        # ── 밴드 내 볼륨 번호 ──
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFont("Korean", 60)
        c.drawString(0, h - 105, "Vol. 1")

        # ── 메인 타이틀 (밴드 아래) ──
        title_y = h - band_h - 55
        c.setFillColor(Colors.TEXT_PRIMARY)
        c.setFont("Korean", 44)
        c.drawString(0, title_y, "Python 입문")

        # ── 부제 ──
        c.setFillColor(Colors.TEXT_SECONDARY)
        c.setFont("Korean", 16)
        c.drawString(0, title_y - 35,
                     "기초부터 탄탄하게, 개발자로서의 첫 걸음")

        # ── 구분선 (악센트 컬러) ──
        c.setStrokeColor(Colors.ACCENT_BLUE)
        c.setLineWidth(2)
        c.line(0, title_y - 55, 80, title_y - 55)

        # ── 대상 독자 ──
        info_y = title_y - 80
        c.setFillColor(Colors.TEXT_TERTIARY)
        c.setFont("Korean", 11)
        c.drawString(0, info_y,
                     "CS/SW 학과 1학년  |  Python 초보자  |  MLOps 지망생")
        c.drawString(0, info_y - 20,
                     "Python 3.12  |  VS Code  |  macOS / Windows")

        # ── 하단 밴드 (얇은) ──
        c.setFillColor(Colors.BG_CHAPTER_HEADER)
        c.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
               PAGE_WIDTH, 18 * mm, fill=1, stroke=0)

        # 하단 텍스트
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFillAlpha(0.8)
        c.setFont("Korean", 10)
        c.drawCentredString(PAGE_WIDTH / 2 - MARGIN_LEFT,
                            -MARGIN_BOTTOM + 6 * mm,
                            "2026년 3월  |  v1.0")
        c.setFillAlpha(1.0)


class ColoredBox(Flowable):
    """배경색 + 선택적 좌측 스트라이프가 있는 텍스트 박스.
    페이지를 넘는 콘텐츠는 자동 분할됨."""

    def __init__(self, content, bg_color, border_color=None,
                 accent_color=None, width=None, padding=8):
        super().__init__()
        self.content = list(content)
        self.bg_color = bg_color
        self.border_color = border_color
        self.accent_color = accent_color
        self.box_width = width or CONTENT_WIDTH
        self.padding = padding
        self._fixed_height = None

    def _inner_width(self):
        w = self.box_width - 2 * self.padding
        if self.accent_color:
            w -= 4
        return w

    def wrap(self, available_width, available_height):
        self.box_width = min(self.box_width, available_width)
        inner_w = self._inner_width()
        total_height = self.padding * 2
        for item in self.content:
            _w, h = item.wrap(inner_w, available_height)
            total_height += h
        self._fixed_height = total_height
        return self.box_width, total_height

    def split(self, available_width, available_height):
        """콘텐츠가 페이지를 넘으면 두 박스로 분할"""
        self.box_width = min(self.box_width, available_width)
        inner_w = self._inner_width()

        # 현재 페이지에 들어갈 아이템 계산
        used = self.padding * 2
        fit_items = []
        remaining = []
        split_found = False

        for item in self.content:
            if split_found:
                remaining.append(item)
                continue
            _w, h = item.wrap(inner_w, available_height)
            if used + h <= available_height:
                used += h
                fit_items.append(item)
            else:
                split_found = True
                remaining.append(item)

        if not fit_items:
            return []
        if not remaining:
            return [self]

        first = ColoredBox(
            fit_items, self.bg_color, self.border_color,
            self.accent_color, self.box_width, self.padding)
        second = ColoredBox(
            remaining, self.bg_color, self.border_color,
            self.accent_color, self.box_width, self.padding)
        return [first, second]

    def draw(self):
        c = self.canv
        w = self.box_width
        h = self._fixed_height

        # 배경
        c.setFillColor(self.bg_color)
        c.setStrokeColor(self.border_color or self.bg_color)
        c.setLineWidth(0.5)
        c.roundRect(0, 0, w, h, 4, fill=1,
                    stroke=1 if self.border_color else 0)

        # 좌측 악센트 스트라이프
        if self.accent_color:
            c.setFillColor(self.accent_color)
            c.roundRect(0, 0, 4, h, 2, fill=1, stroke=0)

        # 콘텐츠 렌더링
        x_offset = self.padding + (6 if self.accent_color else 0)
        y_offset = h - self.padding
        inner_width = self._inner_width()

        for item in self.content:
            _iw, ih = item.wrap(inner_width, h)
            y_offset -= ih
            item.drawOn(c, x_offset, y_offset)


class ChapterMarker(Flowable):
    """보이지 않는 마커 — 페이지 데코레이터에 챕터 컬러/제목 전달"""

    def __init__(self, accent_color, chapter_label):
        super().__init__()
        self.accent_color = accent_color
        self.chapter_label = chapter_label

    def wrap(self, available_width, available_height):
        return 0, 0

    def draw(self):
        # 캔버스에 챕터 정보를 저장 (데코레이터에서 읽음)
        self.canv._current_accent = self.accent_color
        self.canv._current_chapter = self.chapter_label


class SectionHeader(Flowable):
    """섹션 헤더: 좌측 컬러 블록 마커 + 하단 그라데이션 구분선"""

    def __init__(self, title, accent_color, width=None):
        super().__init__()
        self.title = title
        self.accent_color = accent_color
        self.box_width = width or CONTENT_WIDTH
        self._h = 0

    def wrap(self, available_width, available_height):
        self.box_width = min(self.box_width, available_width)
        self._h = 32  # 고정 높이
        return self.box_width, self._h

    def draw(self):
        c = self.canv
        w = self.box_width

        # 좌측 컬러 블록 마커 (6px 넓이, 둥근 모서리)
        c.setFillColor(self.accent_color)
        c.roundRect(0, 2, 5, self._h - 6, 2, fill=1, stroke=0)

        # 제목 텍스트
        c.setFillColor(Colors.TEXT_PRIMARY)
        c.setFont("Korean", 17)
        c.drawString(14, 10, self.title)

        # 하단 그라데이션 구분선 (악센트 → 투명)
        c.setStrokeColor(self.accent_color)
        c.setStrokeAlpha(0.4)
        c.setLineWidth(1)
        c.line(0, 0, w * 0.35, 0)
        c.setStrokeColor(Colors.BORDER_DEFAULT)
        c.setStrokeAlpha(0.2)
        c.line(w * 0.35, 0, w, 0)
        c.setStrokeAlpha(1.0)


class HeaderBox(Flowable):
    """상단 컬러 헤더 바가 있는 박스 (큰 그림, 요약 등)"""

    def __init__(self, label, header_color, bg_color, body_text,
                 body_style, extra_content=None, width=None):
        super().__init__()
        self.label = label
        self.header_color = header_color
        self.bg_color = bg_color
        self.body_text = body_text
        self.body_style = body_style
        self.extra = extra_content or []
        self.box_width = width or CONTENT_WIDTH
        self._h = 0

    def wrap(self, available_width, available_height):
        from reportlab.platypus import Paragraph as P
        self.box_width = min(self.box_width, available_width)
        inner = self.box_width - 24
        h = 36  # 헤더 바 높이
        if self.body_text:
            p = P(self.body_text, self.body_style)
            _w, ph = p.wrap(inner, available_height)
            h += ph + 16
            self._body_p = p
        else:
            self._body_p = None
        for item in self.extra:
            _w, ih = item.wrap(inner, available_height)
            h += ih
        h += 12  # 하단 패딩
        self._h = h
        return self.box_width, h

    def split(self, available_width, available_height):
        """페이지에 안 들어가면 다음 페이지로 이동"""
        w, h = self.wrap(available_width, available_height)
        if h <= available_height:
            return [self]
        return []

    def draw(self):
        c = self.canv
        w = self.box_width
        h = self._h

        # 본문 배경
        c.setFillColor(self.bg_color)
        c.roundRect(0, 0, w, h, 6, fill=1, stroke=0)

        # 상단 컬러 헤더 바
        c.setFillColor(self.header_color)
        c.roundRect(0, h - 30, w, 30, 6, fill=1, stroke=0)
        # 하단 모서리 채우기 (둥근 부분 없애기)
        c.rect(0, h - 30, w, 10, fill=1, stroke=0)

        # 헤더 라벨
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFont("Korean", 12)
        c.drawString(12, h - 22, self.label)

        # 본문 콘텐츠
        y = h - 42
        inner = w - 24
        if self._body_p:
            _w, bh = self._body_p.wrap(inner, h)
            self._body_p.drawOn(c, 12, y - bh)
            y -= bh + 8

        for item in self.extra:
            _w, ih = item.wrap(inner, h)
            y -= ih
            item.drawOn(c, 12, y)


class ChapterTitlePage(Flowable):
    """챕터 시작 전체 페이지 — 풀 컬러 배경 + 워터마크 번호"""

    def __init__(self, chapter_num, title, subtitle, accent_color):
        super().__init__()
        self.chapter_num = chapter_num
        self.title = title
        self.subtitle = subtitle
        self.accent_color = accent_color

    def wrap(self, available_width, available_height):
        return available_width, available_height

    def _darken(self, hex_color, factor=0.75):
        """색상을 어둡게 만들기"""
        from reportlab.lib.colors import HexColor
        r, g, b = hex_color.red, hex_color.green, hex_color.blue
        return HexColor(
            f"#{int(r*factor*255):02x}"
            f"{int(g*factor*255):02x}"
            f"{int(b*factor*255):02x}")

    def draw(self):
        c = self.canv
        w = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
        h = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM
        accent = self.accent_color
        dark = self._darken(accent, 0.7)

        # ── 풀 컬러 배경 ──
        c.setFillColor(accent)
        c.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
               PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        # ── 하단 어두운 밴드 (20%) ──
        band_h = h * 0.22
        c.setFillColor(dark)
        c.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
               PAGE_WIDTH, band_h + MARGIN_BOTTOM, fill=1, stroke=0)

        # ── 대형 워터마크 번호 (반투명) ──
        c.saveState()
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFillAlpha(0.08)
        c.setFont("Korean", 220)
        c.drawRightString(w + 10, h * 0.25,
                          str(self.chapter_num))
        c.restoreState()

        # ── 상단: "CHAPTER" 라벨 ──
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFillAlpha(0.6)
        c.setFont("Korean", 13)
        c.drawString(0, h - 40, "CHAPTER")
        c.setFillAlpha(1.0)

        # ── 챕터 번호 ──
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFont("Korean", Typography.CHAPTER_NUM_SIZE + 12)
        c.drawString(0, h - 95,
                     f"{self.chapter_num:02d}")

        # ── 구분선 (반투명 흰색) ──
        c.setStrokeColor(Colors.TEXT_INVERSE)
        c.setStrokeAlpha(0.3)
        c.setLineWidth(1.5)
        c.line(0, h - 110, w * 0.4, h - 110)
        c.setStrokeAlpha(1.0)

        # ── 챕터 제목 ──
        c.setFillColor(Colors.TEXT_INVERSE)
        c.setFont("Korean", Typography.CHAPTER_TITLE_SIZE + 4)
        c.drawString(0, h - 155, self.title)

        # ── 부제목 ──
        if self.subtitle:
            c.setFillColor(Colors.TEXT_INVERSE)
            c.setFillAlpha(0.7)
            c.setFont("Korean", Typography.CHAPTER_SUBTITLE_SIZE + 2)
            c.drawString(0, h - 185, self.subtitle)
            c.setFillAlpha(1.0)

        # ── 하단 밴드 위 장식 라인 ──
        c.setStrokeColor(Colors.TEXT_INVERSE)
        c.setStrokeAlpha(0.15)
        c.setLineWidth(0.5)
        c.line(-MARGIN_LEFT, band_h - MARGIN_BOTTOM + band_h,
               PAGE_WIDTH, band_h - MARGIN_BOTTOM + band_h)
        c.setStrokeAlpha(1.0)


class FlowDiagram(Flowable):
    """그래픽 플로우 다이어그램 — 둥근 박스 + 화살표 연결.

    nodes: str 리스트 또는 {"label": str, "sub": str, "color": str} 딕셔너리 리스트
    arrow_labels: 연속 노드 사이 화살표 위에 표시할 텍스트 리스트 (선택)
    direction: "horizontal" | "vertical"
    """

    BOX_H = 30
    BOX_MIN_W = 52
    BOX_PAD_X = 10
    ARROW_LEN = 30
    ARROW_HEAD = 5
    ROW_GAP = 20
    SUB_GAP = 13
    FONT_LABEL = "Korean"
    FONT_SIZE = 9.5
    FONT_SUB = 7.5
    FONT_ARROW = 7

    def __init__(self, nodes, arrow_labels=None, direction="horizontal",
                 title=None, note=None, accent_color=None, width=None):
        super().__init__()
        self.nodes = nodes
        self.arrow_labels = arrow_labels or []
        self.direction = direction
        self.title = title
        self.note = note
        self.accent = (HexColor(accent_color)
                       if isinstance(accent_color, str)
                       else (accent_color or Colors.ACCENT_BLUE))
        self.box_width = width or CONTENT_WIDTH
        self._rows = []
        self._node_ws = []
        self._h = 0
        self._has_sub = False

    # ── 헬퍼 ────────────────────────────────────────────
    @staticmethod
    def _lbl(node):
        return node["label"] if isinstance(node, dict) else str(node)

    @staticmethod
    def _sub(node):
        return node.get("sub", "") if isinstance(node, dict) else ""

    @staticmethod
    def _clr(node):
        if isinstance(node, dict) and "color" in node:
            c = node["color"]
            return HexColor(c) if isinstance(c, str) else c
        return None

    @staticmethod
    def _tint(color, strength=0.14):
        """색상의 밝은 틴트 생성 (배경용)"""
        r = 1.0 - (1.0 - color.red) * strength
        g = 1.0 - (1.0 - color.green) * strength
        b = 1.0 - (1.0 - color.blue) * strength
        return HexColor(
            f"#{min(255,int(r*255)):02x}"
            f"{min(255,int(g*255)):02x}"
            f"{min(255,int(b*255)):02x}")

    # ── wrap ────────────────────────────────────────────
    def wrap(self, available_width, available_height):
        self.box_width = min(self.box_width, available_width)
        self._has_sub = any(self._sub(n) for n in self.nodes)

        # 각 노드 박스 너비 계산
        self._node_ws = []
        for n in self.nodes:
            tw = stringWidth(self._lbl(n), self.FONT_LABEL, self.FONT_SIZE)
            sub = self._sub(n)
            if sub:
                tw = max(tw, stringWidth(sub, self.FONT_LABEL, self.FONT_SUB))
            self._node_ws.append(max(self.BOX_MIN_W, tw + 2 * self.BOX_PAD_X))

        # 레이아웃: 수평이면 자동 줄바꿈, 수직이면 한 줄에 하나씩
        if self.direction == "vertical":
            self._rows = [[i] for i in range(len(self.nodes))]
        else:
            rows, cur, cur_w = [], [], 0.0
            for i, nw in enumerate(self._node_ws):
                gap = self.ARROW_LEN if cur else 0
                if cur_w + gap + nw > self.box_width and cur:
                    rows.append(cur)
                    cur, cur_w = [i], nw
                else:
                    cur.append(i)
                    cur_w += gap + nw
            if cur:
                rows.append(cur)
            self._rows = rows

        # 전체 높이 계산
        row_h = self.BOX_H + (self.SUB_GAP if self._has_sub else 0)
        h = 8  # 상단 여백
        if self.title:
            h += 18
        h += len(self._rows) * row_h
        h += max(0, len(self._rows) - 1) * self.ROW_GAP
        if self.note:
            h += 18
        h += 8  # 하단 여백
        self._row_h = row_h
        self._h = h
        return self.box_width, h

    # ── draw ────────────────────────────────────────────
    def draw(self):
        c = self.canv
        y = self._h - 4

        # 배경 (연한 회색 라운드 사각형)
        c.setFillColor(HexColor("#F8F9FB"))
        c.roundRect(0, 0, self.box_width, self._h, 8, fill=1, stroke=0)
        c.setStrokeColor(Colors.BORDER_DEFAULT)
        c.setLineWidth(0.5)
        c.roundRect(0, 0, self.box_width, self._h, 8, fill=0, stroke=1)

        # 타이틀
        if self.title:
            y -= 14
            c.setFont(self.FONT_LABEL, 10)
            c.setFillColor(Colors.TEXT_SECONDARY)
            c.drawCentredString(self.box_width / 2, y, self.title)
            y -= 6

        # 각 행 렌더링
        for ri, row_idx in enumerate(self._rows):
            y -= self.BOX_H

            if self.direction == "vertical":
                max_w = max(self._node_ws[i] for i in row_idx)
                box_w = min(max_w * 1.3, self.box_width * 0.6)
                x = (self.box_width - box_w) / 2
                for idx in row_idx:
                    self._draw_node(c, x, y, box_w, idx)
            else:
                total = (sum(self._node_ws[i] for i in row_idx)
                         + self.ARROW_LEN * max(0, len(row_idx) - 1))
                x = (self.box_width - total) / 2
                for j, idx in enumerate(row_idx):
                    nw = self._node_ws[idx]
                    self._draw_node(c, x, y, nw, idx)
                    if j < len(row_idx) - 1:
                        ax1 = x + nw + 3
                        ax2 = x + nw + self.ARROW_LEN - 3
                        ay = y + self.BOX_H / 2
                        self._arrow(c, ax1, ay, ax2, ay)
                        if idx < len(self.arrow_labels):
                            lbl = self.arrow_labels[idx]
                            if lbl:
                                c.setFont(self.FONT_LABEL, self.FONT_ARROW)
                                c.setFillColor(Colors.TEXT_TERTIARY)
                                c.drawCentredString(
                                    (ax1 + ax2) / 2, ay + 7, lbl)
                    x += nw + self.ARROW_LEN

            if self._has_sub:
                y -= self.SUB_GAP

            # 행 간 연결 화살표
            if ri < len(self._rows) - 1:
                mid_x = self.box_width / 2
                self._arrow(c, mid_x, y - 2, mid_x, y - self.ROW_GAP + 4)
                y -= self.ROW_GAP

        # 하단 노트
        if self.note:
            c.setFont(self.FONT_LABEL, 8.5)
            c.setFillColor(Colors.TEXT_TERTIARY)
            c.drawCentredString(self.box_width / 2, 6, self.note)

    # ── 노드 박스 그리기 ────────────────────────────────
    def _draw_node(self, c, x, y, w, idx):
        node = self.nodes[idx]
        nc = self._clr(node) or self.accent
        fill = self._tint(nc)

        c.setFillColor(fill)
        c.setStrokeColor(nc)
        c.setLineWidth(1.2)
        c.roundRect(x, y, w, self.BOX_H, 7, fill=1, stroke=1)

        label = self._lbl(node)
        c.setFillColor(Colors.TEXT_PRIMARY)
        c.setFont(self.FONT_LABEL, self.FONT_SIZE)
        tw = stringWidth(label, self.FONT_LABEL, self.FONT_SIZE)
        c.drawString(x + (w - tw) / 2,
                     y + (self.BOX_H - self.FONT_SIZE) / 2 + 1,
                     label)

        sub = self._sub(node)
        if sub:
            c.setFont(self.FONT_LABEL, self.FONT_SUB)
            c.setFillColor(Colors.TEXT_TERTIARY)
            sw = stringWidth(sub, self.FONT_LABEL, self.FONT_SUB)
            c.drawString(x + (w - sw) / 2, y - 11, sub)

    # ── 화살표 그리기 ───────────────────────────────────
    def _arrow(self, c, x1, y1, x2, y2):
        c.setStrokeColor(Colors.TEXT_SECONDARY)
        c.setFillColor(Colors.TEXT_SECONDARY)
        c.setLineWidth(1.2)
        c.line(x1, y1, x2, y2)
        angle = math.atan2(y2 - y1, x2 - x1)
        hs = self.ARROW_HEAD
        p = c.beginPath()
        p.moveTo(x2, y2)
        p.lineTo(x2 - hs * math.cos(angle - 0.4),
                 y2 - hs * math.sin(angle - 0.4))
        p.lineTo(x2 - hs * math.cos(angle + 0.4),
                 y2 - hs * math.sin(angle + 0.4))
        p.close()
        c.drawPath(p, fill=1, stroke=0)
