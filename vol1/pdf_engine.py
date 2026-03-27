"""
Python Mastery Series — PDF 빌더
콘텐츠 딕셔너리 -> reportlab Flowable -> PDF
"""

from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable,
)

from pdf_styles import (
    Colors, Typography, Spacing,
    PAGE_SIZE, PAGE_WIDTH, PAGE_HEIGHT,
    MARGIN_TOP, MARGIN_BOTTOM, MARGIN_LEFT, MARGIN_RIGHT,
    CONTENT_WIDTH, FONT_CODE,
)
from pdf_components import (
    CoverPage as _CoverPage, ColoredBox, ChapterTitlePage, FlowDiagram,
)
from pdf_text import register_fonts, create_styles, process_inline, wrap_cjk_in_code


class PDFBuilder:
    """콘텐츠 딕셔너리를 PDF로 변환하는 메인 빌더"""

    def __init__(self, output_path, volume_num=1, volume_subtitle="Python 입문"):
        self.output_path = output_path
        self.volume_num = volume_num
        self.volume_subtitle = volume_subtitle
        self.volume_label = f"Vol.{volume_num}"
        self.story = []
        self.styles = create_styles()
        self.current_accent = Colors.ACCENT_BLUE
        self.current_chapter_title = ""
        register_fonts()

    # ── 표지 ─────────────────────────────────────────────────
    def add_cover_page(self, **kwargs):
        cover_kwargs = {
            "volume_num": self.volume_num,
            "title": self.volume_subtitle,
        }
        cover_kwargs.update(kwargs)
        self.story.append(_CoverPage(**cover_kwargs))
        self.story.append(PageBreak())

    def _cover_text(self, text, size, color):
        self.story.append(Paragraph(
            text,
            ParagraphStyle("cover", fontName="Korean", fontSize=size,
                           textColor=color, alignment=TA_CENTER,
                           leading=size * 1.3),
        ))

    # ── 목차 ─────────────────────────────────────────────────
    def add_toc(self, chapters):
        self.story.append(Paragraph("목차", self.styles["h1"]))
        self.story.append(Spacer(1, 8 * mm))
        self.story.append(HRFlowable(
            width="100%", thickness=1, color=Colors.BORDER_DEFAULT,
            spaceAfter=6 * mm))

        for ch in chapters:
            num = ch["number"]
            color = (Colors.CHAPTER_COLORS[num]
                     if num < len(Colors.CHAPTER_COLORS)
                     else Colors.ACCENT_BLUE)
            hex_val = color.hexval() if hasattr(color, "hexval") else str(color)
            self.story.append(Paragraph(
                f'<font color="{hex_val}">Chapter {num}</font>'
                f'&nbsp;&nbsp;&nbsp;{ch["title"]}',
                self.styles["toc_chapter"],
            ))
            for sec in ch.get("sections", []):
                self.story.append(Paragraph(
                    f'\u2022 {sec["title"]}',
                    self.styles["toc_section"],
                ))
            self.story.append(Spacer(1, 2 * mm))

        self.story.append(Spacer(1, 4 * mm))
        self.story.append(HRFlowable(
            width="100%", thickness=0.5, color=Colors.BORDER_DEFAULT,
            spaceAfter=4 * mm))
        for label in [
            "부록 A: Python 키워드 & 내장함수 총정리",
            "부록 B: 자주 하는 실수 Top 20",
            "부록 C: 추천 학습 자료 & 로드맵",
        ]:
            self.story.append(Paragraph(label, self.styles["toc_section"]))
        self.story.append(PageBreak())

    # ── 챕터 ─────────────────────────────────────────────────
    def render_chapter(self, chapter):
        num = chapter["number"]
        accent = (Colors.CHAPTER_COLORS[num]
                  if num < len(Colors.CHAPTER_COLORS)
                  else Colors.ACCENT_BLUE)

        # 챕터 메타 마커 삽입 (페이지 데코레이터용)
        from pdf_components import ChapterMarker
        self.story.append(ChapterMarker(accent, f"Ch {num}"))

        # 타이틀 페이지
        self.story.append(ChapterTitlePage(
            num, chapter["title"],
            chapter.get("subtitle", ""), accent))
        self.story.append(PageBreak())

        # 큰 그림
        if "big_picture" in chapter:
            self._big_picture_box(chapter["big_picture"], accent)

        # 섹션
        for sec in chapter.get("sections", []):
            self._render_section(sec, accent)

        # 실무 팁 / 연습문제 / 도전과제 / 요약
        if "practical_tips" in chapter:
            self._render_tips(chapter["practical_tips"])
        if "exercises" in chapter:
            self._render_exercises(chapter["exercises"])
        if "challenge" in chapter:
            self._render_challenge(chapter["challenge"])
        if "summary" in chapter:
            self._render_summary(chapter["summary"])

        self.story.append(PageBreak())

    # ── 부록 ─────────────────────────────────────────────────
    def render_appendix(self, appendix):
        self.story.append(PageBreak())
        self.story.append(Paragraph(appendix["title"], self.styles["h1"]))
        self.story.append(Spacer(1, Spacing.SM))
        self.story.append(HRFlowable(
            width="100%", thickness=1, color=Colors.ACCENT_BLUE,
            spaceAfter=6 * mm))
        for sec in appendix.get("sections", []):
            self._render_section(sec, Colors.ACCENT_BLUE)

    # ── 빌드 ─────────────────────────────────────────────────
    def build(self):
        doc = SimpleDocTemplate(
            self.output_path, pagesize=PAGE_SIZE,
            topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
            leftMargin=MARGIN_LEFT, rightMargin=MARGIN_RIGHT,
            title=f"Python Mastery Series {self.volume_label} - {self.volume_subtitle}",
            author="Python Mastery Series",
        )
        doc.build(self.story,
                  onFirstPage=self._page_decorator,
                  onLaterPages=self._page_decorator)
        return self.output_path

    # ── 내부 렌더러 ──────────────────────────────────────────
    def _big_picture_box(self, text, accent):
        from pdf_components import HeaderBox
        self.story.append(HeaderBox(
            label="\u25b6 큰 그림",
            body_text=process_inline(text),
            header_color=accent,
            bg_color=Colors.BG_CARD,
            body_style=self.styles["body"],
        ))
        self.story.append(Spacer(1, Spacing.MD))

    def _render_section(self, section, accent):
        # h2 섹션 헤더: 좌측 컬러 블록 마커 + 하단 그라데이션 구분선
        from pdf_components import SectionHeader
        self.story.append(SectionHeader(section["title"], accent))
        for item in section.get("content", []):
            if isinstance(item, str):
                self.story.append(Paragraph(
                    process_inline(item), self.styles["body"]))
            elif isinstance(item, dict):
                self._render_block(item, accent)
        self.story.append(Spacer(1, Spacing.SM))

    def _render_block(self, block, accent):
        t = block.get("type", "")
        dispatch = {
            "code": lambda b: self._render_code(b, accent),
            "note": lambda b: self._note_box(
                b, Colors.BG_TIP, Colors.ACCENT_BLUE, "알아두면 좋아요"),
            "warning": lambda b: self._note_box(
                b, Colors.BG_WARNING, Colors.ACCENT_RED, "주의"),
            "tip": lambda b: self._note_box(
                b, Colors.BG_TIP, Colors.ACCENT_BLUE, "팁"),
            "analogy": lambda b: self._note_box(
                b, Colors.BG_CARD, Colors.ACCENT_TEAL, "비유로 이해하기"),
            "table": self._render_table,
            "bullet_list": lambda b: self._bullets(b.get("items", [])),
            "numbered_list": lambda b: self._numbers(b.get("items", [])),
            "heading": lambda b: self.story.append(
                Paragraph(b["text"], self.styles["h3"])),
            "diagram": self._render_diagram,
            "flow_diagram": self._render_flow_diagram,
            "spacer": lambda _: self.story.append(Spacer(1, Spacing.SM)),
        }
        handler = dispatch.get(t)
        if handler:
            handler(block)

    def _render_code(self, block, accent=None):
        lang = block.get("language", "python")
        title = block.get("title", "")
        elements = []
        if title:
            elements.append(Paragraph(
                f'<font color="#6B7684">{title}</font>',
                ParagraphStyle("CT", fontName="Korean", fontSize=9,
                               textColor=Colors.TEXT_SECONDARY,
                               spaceAfter=2)))
        for line in block.get("code", "").strip().split("\n"):
            safe = (line.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;") or "&nbsp;")
            safe = wrap_cjk_in_code(safe)
            elements.append(Paragraph(
                safe,
                ParagraphStyle("CL", fontName=FONT_CODE,
                               fontSize=Typography.CODE_SIZE,
                               leading=Typography.CODE_LEADING,
                               textColor=Colors.TEXT_PRIMARY)))
        # 언어 라벨을 컬러 배지 스타일로
        badge_color = accent or Colors.ACCENT_BLUE
        lang_p = Paragraph(
            f'<font color="{badge_color.hexval()}">'
            f'<b>{lang}</b></font>',
            ParagraphStyle("LL", fontName="Korean", fontSize=8,
                           textColor=badge_color,
                           alignment=TA_RIGHT))
        self.story.append(ColoredBox(
            [lang_p] + elements, Colors.BG_CODE,
            border_color=Colors.BORDER_CODE,
            accent_color=accent,
            padding=Spacing.CODE_PADDING))
        self.story.append(Spacer(1, Spacing.SM))

    def _note_box(self, block, bg, accent, label):
        elements = [
            Paragraph(
                f'<font color="{accent.hexval()}">{label}</font>',
                ParagraphStyle("NL", fontName="Korean", fontSize=10,
                               spaceAfter=3)),
            Paragraph(process_inline(block.get("text", "")),
                      self.styles["body"]),
        ]
        self.story.append(ColoredBox(
            elements, bg, accent_color=accent, padding=8))
        self.story.append(Spacer(1, Spacing.SM))

    def _render_table(self, block):
        headers = block.get("headers", [])
        rows = block.get("rows", [])
        h_sty = ParagraphStyle(
            "TH", fontName="Korean", fontSize=9.5,
            textColor=Colors.TEXT_INVERSE, leading=14)
        c_sty = ParagraphStyle(
            "TC", fontName="Korean", fontSize=9.5,
            textColor=Colors.TEXT_PRIMARY, leading=14)
        data = []
        def _esc(txt):
            s = str(txt)
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        if headers:
            data.append([Paragraph(_esc(h), h_sty) for h in headers])
        for row in rows:
            data.append([Paragraph(_esc(c), c_sty) for c in row])
        if not data:
            return
        n = len(data[0])
        tbl = Table(data, colWidths=[CONTENT_WIDTH / n] * n)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), Colors.BG_CHAPTER_HEADER),
            ("TEXTCOLOR", (0, 0), (-1, 0), Colors.TEXT_INVERSE),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, -1), "Korean"),
            ("FONTSIZE", (0, 0), (-1, -1), 9.5),
            ("TOPPADDING", (0, 0), (-1, -1), Spacing.TABLE_CELL_PAD),
            ("BOTTOMPADDING", (0, 0), (-1, -1), Spacing.TABLE_CELL_PAD),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, Colors.BORDER_DEFAULT),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [Colors.BG_PAGE, Colors.BG_CARD]),
        ]))
        self.story.append(tbl)
        self.story.append(Spacer(1, Spacing.SM))

    def _bullets(self, items):
        for item in items:
            self.story.append(Paragraph(
                f"\u2022 &nbsp;{process_inline(item)}",
                self.styles["bullet"]))

    def _numbers(self, items):
        for i, item in enumerate(items, 1):
            self.story.append(Paragraph(
                f"{i}. &nbsp;{process_inline(item)}",
                self.styles["numbered"]))

    def _render_flow_diagram(self, block):
        nodes = block.get("nodes", [])
        if not nodes:
            return
        self.story.append(FlowDiagram(
            nodes=nodes,
            arrow_labels=block.get("arrow_labels"),
            direction=block.get("direction", "horizontal"),
            title=block.get("title"),
            note=block.get("note"),
            accent_color=block.get("accent_color"),
        ))
        self.story.append(Spacer(1, Spacing.SM))

    def _render_diagram(self, block):
        lines = block.get("text", "").strip().split("\n")
        elements = []
        for line in lines:
            safe = (line.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;") or "&nbsp;")
            safe = wrap_cjk_in_code(safe)
            elements.append(Paragraph(
                safe,
                ParagraphStyle("DL", fontName=FONT_CODE, fontSize=9,
                               leading=12, textColor=Colors.TEXT_SECONDARY)))
        self.story.append(ColoredBox(
            elements, Colors.BG_CARD,
            border_color=Colors.BORDER_DEFAULT, padding=10))
        self.story.append(Spacer(1, Spacing.SM))

    def _render_tips(self, tips):
        self.story.append(Spacer(1, Spacing.MD))
        self.story.append(Paragraph("실무 팁", self.styles["h2"]))
        for tip in tips:
            self.story.append(ColoredBox(
                [Paragraph(process_inline(tip), self.styles["body"])],
                Colors.BG_TIP, accent_color=Colors.ACCENT_BLUE, padding=8))
            self.story.append(Spacer(1, 3))

    def _render_exercises(self, exercises):
        self.story.append(Spacer(1, Spacing.MD))
        self.story.append(Paragraph("연습문제", self.styles["h2"]))
        for ex in exercises:
            num = ex.get("number", "")
            q_type = ex.get("type", "coding")
            label = "객관식" if q_type == "multiple_choice" else "코딩"
            elems = [Paragraph(
                f'<font color="#03B26C">Q{num}.</font> '
                f'<font color="#8B95A1">[{label}]</font> '
                f'{process_inline(ex.get("question", ""))}',
                self.styles["body"])]
            if q_type == "multiple_choice":
                for ch in ex.get("choices", []):
                    safe_ch = (str(ch).replace("&", "&amp;")
                                      .replace("<", "&lt;")
                                      .replace(">", "&gt;"))
                    elems.append(Paragraph(
                        f"&nbsp;&nbsp;&nbsp;&nbsp;{safe_ch}",
                        self.styles["body"]))
            if "hint" in ex:
                elems.append(Paragraph(
                    f'<font color="#8B95A1">힌트: {ex["hint"]}</font>',
                    ParagraphStyle("H", fontName="Korean", fontSize=9,
                                   textColor=Colors.TEXT_TERTIARY,
                                   spaceBefore=2)))
            self.story.append(ColoredBox(
                elems, Colors.BG_EXERCISE,
                border_color=Colors.BORDER_DEFAULT, padding=8))
            self.story.append(Spacer(1, 3))

    def _render_challenge(self, challenge):
        self.story.append(Spacer(1, Spacing.SM))
        elems = [
            Paragraph(
                '<font color="#F04452">도전 과제</font>',
                ParagraphStyle("ChL", fontName="Korean", fontSize=12,
                               textColor=Colors.ACCENT_RED, spaceAfter=4)),
            Paragraph(process_inline(challenge.get("question", "")),
                      self.styles["body"]),
        ]
        if "hint" in challenge:
            elems.append(Paragraph(
                f'<font color="#8B95A1">힌트: {challenge["hint"]}</font>',
                ParagraphStyle("ChH", fontName="Korean", fontSize=9,
                               textColor=Colors.TEXT_TERTIARY,
                               spaceBefore=4)))
        self.story.append(ColoredBox(
            elems, Colors.BG_WARNING,
            accent_color=Colors.ACCENT_RED, padding=10))

    def _render_summary(self, points):
        self.story.append(Spacer(1, Spacing.MD))
        from pdf_components import HeaderBox
        body_items = []
        for pt in points:
            body_items.append(Paragraph(
                f"\u2713 &nbsp;{process_inline(pt)}",
                self.styles["body"]))
        self.story.append(HeaderBox(
            label="\u2728 요약",
            header_color=Colors.ACCENT_BLUE,
            bg_color=Colors.BG_SUMMARY,
            body_text=None,
            body_style=self.styles["body"],
            extra_content=body_items,
        ))

    # ── 페이지 데코레이터 ────────────────────────────────────
    def _page_decorator(self, canvas_obj, doc_obj):
        page_num = canvas_obj.getPageNumber()
        if page_num <= 2:
            return

        # 챕터 마커에서 설정된 컬러 읽기
        accent = getattr(canvas_obj, '_current_accent',
                         self.current_accent)
        self.current_accent = accent

        canvas_obj.saveState()

        # 상단 챕터별 컬러 스트라이프 (2px)
        canvas_obj.setFillColor(accent)
        canvas_obj.rect(
            0, PAGE_HEIGHT - 3,
            PAGE_WIDTH, 3, fill=1, stroke=0)

        # 상단 라인 (연한)
        canvas_obj.setStrokeColor(Colors.BORDER_DEFAULT)
        canvas_obj.setLineWidth(0.3)
        canvas_obj.line(
            MARGIN_LEFT, PAGE_HEIGHT - MARGIN_TOP + 5,
            PAGE_WIDTH - MARGIN_RIGHT, PAGE_HEIGHT - MARGIN_TOP + 5)

        # 하단 푸터
        canvas_obj.setFont("Korean", Typography.FOOTER_SIZE)
        canvas_obj.setFillColor(Colors.TEXT_TERTIARY)
        canvas_obj.drawCentredString(
            PAGE_WIDTH / 2, 12 * mm,
            f"Python Mastery Series {self.volume_label}  |  {page_num}")

        # 하단 컬러 스트라이프 (1px)
        canvas_obj.setFillColor(accent)
        canvas_obj.setFillAlpha(0.3)
        canvas_obj.rect(0, 0, PAGE_WIDTH, 1.5, fill=1, stroke=0)
        canvas_obj.setFillAlpha(1.0)

        canvas_obj.restoreState()
