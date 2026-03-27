"""
Python Mastery Series Vol.2 — PDF 생성 메인 스크립트
실행: cd vol2 && python3 generate.py
"""

import sys
import time

from pdf_engine import PDFBuilder

# 챕터 콘텐츠 임포트
from content.ch00_review import get_chapter as ch00
from content.ch01_class_basics import get_chapter as ch01
from content.ch02_inheritance import get_chapter as ch02
from content.ch03_special_methods import get_chapter as ch03
from content.ch04_exceptions import get_chapter as ch04
from content.ch05_file_io import get_chapter as ch05
from content.ch06_regex import get_chapter as ch06
from content.ch07_iterators import get_chapter as ch07
from content.ch08_decorators import get_chapter as ch08
from content.ch09_project import get_chapter as ch09

# 부록 임포트
from content.appendix_a import get_appendix as app_a
from content.appendix_b import get_appendix as app_b
from content.appendix_c import get_appendix as app_c


OUTPUT_PATH = "output/python_mastery_vol2.pdf"


def main():
    start = time.time()
    print("=" * 50)
    print("Python Mastery Series Vol.2 — PDF 생성")
    print("=" * 50)

    # 챕터 데이터 수집
    chapters = [
        ch00(), ch01(), ch02(), ch03(), ch04(),
        ch05(), ch06(), ch07(), ch08(), ch09(),
    ]
    appendices = [app_a(), app_b(), app_c()]

    print(f"\n총 {len(chapters)}개 챕터 + {len(appendices)}개 부록 로드 완료")

    # PDF 빌드
    builder = PDFBuilder(
        OUTPUT_PATH,
        volume_num=2,
        volume_subtitle="Python 심화",
    )

    print("  [1/4] 표지 생성...")
    builder.add_cover_page(
        subtitle="객체지향부터 고급 패턴까지, 한 단계 더 깊이",
    )

    print("  [2/4] 목차 생성...")
    builder.add_toc(chapters)

    print("  [3/4] 챕터 렌더링...")
    for ch in chapters:
        num = ch["number"]
        title = ch["title"]
        print(f"    Ch {num}: {title}")
        builder.render_chapter(ch)

    print("  [4/4] 부록 렌더링...")
    for app in appendices:
        print(f"    {app['title']}")
        builder.render_appendix(app)

    # 빌드
    print("\n  PDF 빌드 중...")
    path = builder.build()

    elapsed = time.time() - start
    print(f"\n완료! {elapsed:.1f}초 소요")
    print(f"출력: {path}")
    print("=" * 50)


if __name__ == "__main__":
    main()
