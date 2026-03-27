"""
폰트 등록, 스타일 생성, 인라인 텍스트 처리
"""

import re

from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from pdf_styles import Colors, Typography, FONT_KOREAN, FONT_CODE


def register_fonts():
    """한국어 + 코드 폰트 등록"""
    pdfmetrics.registerFont(TTFont("Korean", FONT_KOREAN))


def _inline_code_replace(match):
    """인라인 코드 내 non-ASCII를 Korean 폰트로 전환"""
    content = match.group(1)
    if _has_non_ascii(content):
        content = wrap_cjk_in_code(content)
    return f'<font face="Courier" color="#3182F6">{content}</font>'


def process_inline(text):
    """인라인 마크업 변환: `code`, **bold**"""
    text = re.sub(r'`([^`]+)`', _inline_code_replace, text)
    text = re.sub(
        r'\*\*([^*]+)\*\*',
        r'<b>\1</b>',
        text,
    )
    return text


def _needs_korean_font(ch):
    """Courier로 렌더링할 수 없는 문자인지 판별.
    기본 ASCII + XML 엔티티 마크업은 Courier, 나머지는 Korean 폰트."""
    cp = ord(ch)
    return cp > 0x7E  # ASCII 범위(0x20~0x7E) 밖이면 Korean 필요


def _has_non_ascii(text):
    """텍스트에 ASCII 범위 밖 문자가 포함되어 있는지 확인"""
    return any(_needs_korean_font(ch) for ch in text)


def wrap_cjk_in_code(line):
    """코드 라인에서 non-ASCII 문자 구간을 Korean 폰트로 감싸기.
    ASCII 부분은 Courier, 한글/특수문자 부분은 Korean 폰트로 렌더링."""
    if not _has_non_ascii(line):
        return line

    result = []
    in_korean = False
    buf = []

    for ch in line:
        needs_kr = _needs_korean_font(ch)
        if needs_kr and not in_korean:
            if buf:
                result.append("".join(buf))
                buf = []
            in_korean = True
            buf.append(ch)
        elif not needs_kr and in_korean:
            if buf:
                result.append(
                    f'<font face="Korean">{"".join(buf)}</font>')
                buf = []
            in_korean = False
            buf.append(ch)
        else:
            buf.append(ch)

    if buf:
        if in_korean:
            result.append(
                f'<font face="Korean">{"".join(buf)}</font>')
        else:
            result.append("".join(buf))

    return "".join(result)


def create_styles():
    """전체 문서에서 사용할 ParagraphStyle 딕셔너리 반환"""
    s = {}

    s["body"] = ParagraphStyle(
        "Body", fontName="Korean",
        fontSize=Typography.BODY_SIZE,
        leading=Typography.BODY_LEADING,
        textColor=Colors.TEXT_PRIMARY,
        alignment=TA_JUSTIFY, spaceAfter=4,
    )
    s["body_center"] = ParagraphStyle(
        "BodyCenter", parent=s["body"], alignment=TA_CENTER,
    )
    s["h1"] = ParagraphStyle(
        "H1", fontName="Korean",
        fontSize=Typography.H1_SIZE,
        leading=Typography.H1_SIZE * 1.4,
        textColor=Colors.ACCENT_BLUE,
        spaceBefore=14, spaceAfter=10,
    )
    s["h2"] = ParagraphStyle(
        "H2", fontName="Korean",
        fontSize=Typography.H2_SIZE,
        leading=Typography.H2_SIZE * 1.4,
        textColor=Colors.TEXT_PRIMARY,
        spaceBefore=12, spaceAfter=6,
    )
    s["h3"] = ParagraphStyle(
        "H3", fontName="Korean",
        fontSize=Typography.H3_SIZE,
        leading=Typography.H3_SIZE * 1.4,
        textColor=Colors.TEXT_SECONDARY,
        spaceBefore=8, spaceAfter=4,
    )
    s["code"] = ParagraphStyle(
        "Code", fontName=FONT_CODE,
        fontSize=Typography.CODE_SIZE,
        leading=Typography.CODE_LEADING,
        textColor=Colors.TEXT_PRIMARY,
        backColor=Colors.BG_CODE,
    )
    s["caption"] = ParagraphStyle(
        "Caption", fontName="Korean",
        fontSize=Typography.CAPTION_SIZE,
        leading=Typography.CAPTION_SIZE * 1.5,
        textColor=Colors.TEXT_TERTIARY,
        alignment=TA_CENTER,
    )
    s["label"] = ParagraphStyle(
        "Label", fontName="Korean",
        fontSize=Typography.LABEL_SIZE,
        leading=Typography.LABEL_SIZE * 1.4,
        textColor=Colors.TEXT_SECONDARY,
    )
    s["toc_chapter"] = ParagraphStyle(
        "TocChapter", fontName="Korean",
        fontSize=Typography.TOC_CHAPTER_SIZE,
        leading=Typography.TOC_CHAPTER_SIZE * 1.6,
        textColor=Colors.TEXT_PRIMARY, spaceBefore=6,
    )
    s["toc_section"] = ParagraphStyle(
        "TocSection", fontName="Korean",
        fontSize=Typography.TOC_SIZE,
        leading=Typography.TOC_SIZE * 1.5,
        textColor=Colors.TEXT_SECONDARY, leftIndent=12,
    )
    s["footer"] = ParagraphStyle(
        "Footer", fontName="Korean",
        fontSize=Typography.FOOTER_SIZE,
        textColor=Colors.TEXT_TERTIARY, alignment=TA_CENTER,
    )
    s["bullet"] = ParagraphStyle(
        "Bullet", parent=s["body"],
        leftIndent=16, bulletIndent=6,
        spaceBefore=2, spaceAfter=2,
    )
    s["numbered"] = ParagraphStyle(
        "Numbered", parent=s["body"],
        leftIndent=20, spaceBefore=2, spaceAfter=2,
    )
    return s
