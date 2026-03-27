"""
Python Mastery Series Vol.5 — PDF 생성 메인 스크립트
실행: cd vol5 && python3 generate.py
"""

import time

from pdf_engine import PDFBuilder

from content.ch00_review import get_chapter as ch00
from content.ch01_ml_intro import get_chapter as ch01
from content.ch02_sklearn_basics import get_chapter as ch02
from content.ch03_sklearn_advanced import get_chapter as ch03
from content.ch04_model_evaluation import get_chapter as ch04
from content.ch05_feature_engineering import get_chapter as ch05
from content.ch06_mlflow import get_chapter as ch06
from content.ch07_model_serving import get_chapter as ch07
from content.ch08_monitoring import get_chapter as ch08
from content.ch09_project import get_chapter as ch09

from content.appendix_a import get_appendix as app_a
from content.appendix_b import get_appendix as app_b
from content.appendix_c import get_appendix as app_c


OUTPUT_PATH = "output/python_mastery_vol5.pdf"


def main():
    start = time.time()
    print("=" * 50)
    print("Python Mastery Series Vol.5 — PDF 생성")
    print("=" * 50)

    chapters = [
        ch00(), ch01(), ch02(), ch03(), ch04(),
        ch05(), ch06(), ch07(), ch08(), ch09(),
    ]
    appendices = [app_a(), app_b(), app_c()]

    print(f"\n총 {len(chapters)}개 챕터 + {len(appendices)}개 부록 로드 완료")

    builder = PDFBuilder(
        OUTPUT_PATH,
        volume_num=5,
        volume_subtitle="ML & MLOps",
    )

    print("  [1/4] 표지 생성...")
    builder.add_cover_page(
        subtitle="머신러닝부터 모델 운영까지, MLOps 엔지니어의 첫걸음",
    )

    print("  [2/4] 목차 생성...")
    builder.add_toc(chapters)

    print("  [3/4] 챕터 렌더링...")
    for ch in chapters:
        print(f"    Ch {ch['number']}: {ch['title']}")
        builder.render_chapter(ch)

    print("  [4/4] 부록 렌더링...")
    for app in appendices:
        print(f"    {app['title']}")
        builder.render_appendix(app)

    print("\n  PDF 빌드 중...")
    path = builder.build()

    elapsed = time.time() - start
    print(f"\n완료! {elapsed:.1f}초 소요")
    print(f"출력: {path}")
    print("=" * 50)


if __name__ == "__main__":
    main()
