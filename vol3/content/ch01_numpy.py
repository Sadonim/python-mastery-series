"""
Ch 1: NumPy 기초
Python Mastery Series Vol.3 — 데이터 분석
"""


def get_chapter():
    return {
        "number": 1,
        "title": "NumPy 기초",
        "subtitle": "빠른 수치 연산의 핵심 — ndarray 이해와 활용",
        "big_picture": (
            "Python 리스트는 유연하지만 수백만 개의 숫자를 다루기엔 느립니다. "
            "NumPy의 ndarray는 C로 구현된 연속 메모리 구조를 사용해 Python 리스트보다 "
            "10~100배 빠른 수치 연산을 제공합니다. "
            "이 챕터에서는 ndarray를 만들고, 인덱싱하고, 기본 연산을 수행하는 법을 배웁니다."
        ),
        "sections": [
            {
                "title": "NumPy가 왜 필요한가 — Python 리스트 vs ndarray",
                "content": [
                    "데이터 분석에서는 수십만~수백만 개의 숫자를 반복 계산하는 일이 흔합니다. "
                    "Python 기본 리스트로 이런 작업을 하면 너무 느립니다. "
                    "그 이유를 이해하면 NumPy를 왜 써야 하는지 자연스럽게 납득됩니다.",
                    {
                        "type": "heading",
                        "text": "Python 리스트의 구조적 문제",
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "Python 리스트는 '다양한 물건을 담을 수 있는 서랍장'입니다. "
                            "각 서랍(요소)에는 정수, 문자열, 심지어 다른 리스트도 들어갈 수 있어 유연합니다. "
                            "하지만 그 유연함의 대가로 각 요소는 별도의 메모리 공간에 따로 저장되고, "
                            "리스트는 그 주소들의 목록을 갖고 있습니다. "
                            "반면 NumPy 배열은 '같은 크기의 숫자만 담는 일렬 창고'입니다. "
                            "모든 숫자가 연속된 메모리에 저장되어 CPU 캐시를 효율적으로 활용합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "import time\n"
                            "\n"
                            "N = 1_000_000  # 백만 개의 숫자\n"
                            "\n"
                            "# Python 리스트로 합산\n"
                            "py_list = list(range(N))\n"
                            "start = time.time()\n"
                            "total = sum(py_list)\n"
                            "py_time = time.time() - start\n"
                            "print(f'Python 리스트: {py_time * 1000:.2f} ms')  # 약 30~50 ms\n"
                            "\n"
                            "# NumPy 배열로 합산\n"
                            "np_array = np.arange(N)\n"
                            "start = time.time()\n"
                            "total = np.sum(np_array)\n"
                            "np_time = time.time() - start\n"
                            "print(f'NumPy 배열:   {np_time * 1000:.2f} ms')  # 약 0.5~2 ms\n"
                            "\n"
                            "print(f'\\nNumPy가 {py_time / np_time:.0f}배 빠름!')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["항목", "Python 리스트", "NumPy ndarray"],
                        "rows": [
                            ["요소 타입", "혼합 가능 (int, str, list...)", "동일 타입만 (int64, float64...)"],
                            ["메모리 구조", "포인터 배열 (간접 접근)", "연속 메모리 (직접 접근)"],
                            ["연산 속도", "느림 (Python 루프)", "빠름 (C 구현)"],
                            ["수학 연산", "직접 지원 안 함", "벡터 연산, 브로드캐스팅 지원"],
                            ["메모리 사용", "많음 (각 요소에 타입 정보 포함)", "적음 (타입 정보 공유)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 메모리 사용량 비교\n"
                            "import sys\n"
                            "\n"
                            "py_list = list(range(1000))\n"
                            "np_array = np.arange(1000, dtype=np.int64)\n"
                            "\n"
                            "# 리스트: 각 요소가 파이썬 객체 → 요소당 약 28 bytes\n"
                            "py_size = sys.getsizeof(py_list) + sum(sys.getsizeof(x) for x in py_list)\n"
                            "print(f'Python 리스트: {py_size:,} bytes')  # 약 36,056 bytes\n"
                            "\n"
                            "# ndarray: int64 = 8 bytes × 1000개\n"
                            "print(f'NumPy 배열:   {np_array.nbytes:,} bytes')  # 8,000 bytes\n"
                            "print(f'메모리 절약: {py_size / np_array.nbytes:.1f}배')"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "NumPy는 내부적으로 C와 Fortran으로 작성된 BLAS/LAPACK 라이브러리를 사용합니다. "
                            "즉, Python 코드처럼 보여도 실제 계산은 C 수준의 속도로 실행됩니다. "
                            "이것이 Python으로도 과학 계산이 가능한 비결입니다."
                        ),
                    },
                ],
            },
            {
                "title": "ndarray 생성하기",
                "content": [
                    "NumPy 배열을 만드는 방법은 여러 가지입니다. "
                    "용도에 따라 적합한 생성 함수를 선택하는 것이 중요합니다.",
                    {
                        "type": "heading",
                        "text": "np.array — 기존 데이터로 배열 만들기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 1차원 배열 (1D)\n"
                            "scores = np.array([85, 92, 78, 95, 88])\n"
                            "print(scores)        # [85 92 78 95 88]\n"
                            "print(type(scores))  # <class 'numpy.ndarray'>\n"
                            "\n"
                            "# 2차원 배열 (2D) — 리스트의 리스트\n"
                            "matrix = np.array([\n"
                            "    [1, 2, 3],\n"
                            "    [4, 5, 6],\n"
                            "    [7, 8, 9],\n"
                            "])\n"
                            "print(matrix)\n"
                            "# [[1 2 3]\n"
                            "#  [4 5 6]\n"
                            "#  [7 8 9]]\n"
                            "\n"
                            "# dtype 지정\n"
                            "prices = np.array([10.5, 20.3, 15.8], dtype=np.float32)\n"
                            "flags = np.array([True, False, True], dtype=bool)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "np.zeros, np.ones, np.full — 특정 값으로 채우기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 0으로 채운 배열\n"
                            "zeros = np.zeros(5)             # [0. 0. 0. 0. 0.]\n"
                            "zeros_2d = np.zeros((3, 4))     # 3행 4열, 모두 0.0\n"
                            "\n"
                            "# 1로 채운 배열\n"
                            "ones = np.ones((2, 3))          # [[1. 1. 1.], [1. 1. 1.]]\n"
                            "ones_int = np.ones((2, 3), dtype=int)  # 정수형으로\n"
                            "\n"
                            "# 특정 값으로 채우기\n"
                            "filled = np.full((2, 2), 7)     # [[7, 7], [7, 7]]\n"
                            "pi_arr = np.full(4, np.pi)      # [3.14159... × 4]\n"
                            "\n"
                            "# 단위행렬 (대각선이 1)\n"
                            "eye = np.eye(3)\n"
                            "# [[1. 0. 0.]\n"
                            "#  [0. 1. 0.]\n"
                            "#  [0. 0. 1.]]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "np.arange, np.linspace — 범위 배열",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# np.arange — 정수/부동소수 범위 (Python range와 유사)\n"
                            "a = np.arange(10)          # [0 1 2 3 4 5 6 7 8 9]\n"
                            "b = np.arange(0, 10, 2)    # [0 2 4 6 8]  (시작, 끝, 간격)\n"
                            "c = np.arange(0.0, 1.0, 0.2)  # [0.  0.2 0.4 0.6 0.8]\n"
                            "\n"
                            "# np.linspace — 개수를 지정해서 균등 간격 생성\n"
                            "# np.linspace(시작, 끝, 개수) — 끝값 포함!\n"
                            "d = np.linspace(0, 1, 5)   # [0.   0.25 0.5  0.75 1.  ]\n"
                            "e = np.linspace(0, 360, 7) # [0. 60. 120. 180. 240. 300. 360.]\n"
                            "\n"
                            "# arange vs linspace 선택 기준\n"
                            "# - 간격을 알 때: arange (예: 0.1 단위)\n"
                            "# - 개수를 알 때: linspace (예: 100개 균등 분할)\n"
                            "print('arange:', np.arange(0, 1.1, 0.25))  # 부동소수점 오차 주의!\n"
                            "print('linspace:', np.linspace(0, 1, 5))    # 정확한 끝값 보장"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "np.arange를 부동소수점과 함께 사용하면 부동소수점 오차로 인해 "
                            "예상보다 많거나 적은 원소가 생길 수 있습니다. "
                            "균등 간격이 필요하면 np.linspace를 사용하는 것이 더 안전합니다."
                        ),
                    },
                ],
            },
            {
                "title": "배열 속성 이해하기",
                "content": [
                    "배열의 속성을 읽으면 데이터의 구조를 즉시 파악할 수 있습니다. "
                    "데이터 분석 과정에서 배열이 예상과 다른 형태일 때 속성 확인이 디버깅의 첫 번째 단계입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 학생 성적표: 5명, 3과목\n"
                            "grades = np.array([\n"
                            "    [85, 92, 78],   # 학생 1: 국어, 수학, 영어\n"
                            "    [90, 88, 95],   # 학생 2\n"
                            "    [72, 85, 80],   # 학생 3\n"
                            "    [95, 97, 92],   # 학생 4\n"
                            "    [65, 70, 75],   # 학생 5\n"
                            "])\n"
                            "\n"
                            "print(f'shape (형태): {grades.shape}')    # (5, 3) — 5행 3열\n"
                            "print(f'ndim  (차원): {grades.ndim}')     # 2 — 2차원 배열\n"
                            "print(f'size  (원소수): {grades.size}')   # 15 — 총 15개 값\n"
                            "print(f'dtype (타입): {grades.dtype}')    # int64\n"
                            "print(f'nbytes(바이트): {grades.nbytes}') # 120 (15 × 8 bytes)\n"
                            "\n"
                            "# 1D 배열의 속성\n"
                            "arr_1d = np.array([1, 2, 3, 4, 5])\n"
                            "print(f'\\n1D shape: {arr_1d.shape}')  # (5,) — 튜플, 1차원\n"
                            "print(f'1D ndim:  {arr_1d.ndim}')    # 1\n"
                            "\n"
                            "# 3D 배열 예시 (이미지 배치: N장, 높이, 너비)\n"
                            "images = np.zeros((10, 64, 64))  # 10장의 64×64 이미지\n"
                            "print(f'\\n3D shape: {images.shape}')  # (10, 64, 64)\n"
                            "print(f'3D ndim:  {images.ndim}')    # 3"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "주요 dtype 종류",
                    },
                    {
                        "type": "table",
                        "headers": ["dtype", "크기", "범위", "사용 예"],
                        "rows": [
                            ["int32", "4 bytes", "-2억 ~ 2억", "일반 정수 데이터"],
                            ["int64", "8 bytes", "-9경 ~ 9경", "큰 정수, 기본값"],
                            ["float32", "4 bytes", "약 ±3.4e38", "GPU 연산, 메모리 절약"],
                            ["float64", "8 bytes", "약 ±1.8e308", "정밀 계산, 기본값"],
                            ["bool", "1 byte", "True/False", "마스킹, 필터링"],
                            ["complex128", "16 bytes", "복소수", "신호 처리"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "dtype을 명시하지 않으면 NumPy가 자동으로 추론합니다: "
                            "정수 → int64, 부동소수점 → float64. "
                            "머신러닝에서 GPU를 사용할 때는 float32가 float64보다 2배 빠르고 메모리를 절반만 씁니다."
                        ),
                    },
                ],
            },
            {
                "title": "인덱싱과 슬라이싱",
                "content": [
                    "배열에서 원하는 데이터를 꺼내는 방법입니다. "
                    "Python 리스트와 유사하지만 2D 이상에서 강력한 기능을 제공합니다.",
                    {
                        "type": "heading",
                        "text": "1D 배열 인덱싱 & 슬라이싱",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "scores = np.array([85, 92, 78, 95, 88, 76, 90])\n"
                            "#                   0   1   2   3   4   5   6\n"
                            "#                  -7  -6  -5  -4  -3  -2  -1\n"
                            "\n"
                            "# 단일 원소 접근\n"
                            "print(scores[0])   # 85  — 첫 번째\n"
                            "print(scores[-1])  # 90  — 마지막\n"
                            "print(scores[-2])  # 76  — 뒤에서 두 번째\n"
                            "\n"
                            "# 슬라이싱 [start:stop:step] — stop은 미포함\n"
                            "print(scores[1:4])    # [92 78 95] — 인덱스 1,2,3\n"
                            "print(scores[:3])     # [85 92 78] — 처음부터 3개\n"
                            "print(scores[3:])     # [95 88 76 90] — 인덱스 3부터 끝\n"
                            "print(scores[::2])    # [85 78 88 90] — 2칸씩 건너뛰기\n"
                            "print(scores[::-1])   # [90 76 88 95 78 92 85] — 역순"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "2D 배열 인덱싱 & 슬라이싱",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 5명 학생, 3과목 성적표\n"
                            "grades = np.array([\n"
                            "    [85, 92, 78],\n"
                            "    [90, 88, 95],\n"
                            "    [72, 85, 80],\n"
                            "    [95, 97, 92],\n"
                            "    [65, 70, 75],\n"
                            "])\n"
                            "\n"
                            "# 단일 원소: [행, 열]\n"
                            "print(grades[0, 0])  # 85  — 1번 학생, 1번 과목\n"
                            "print(grades[3, 1])  # 97  — 4번 학생, 2번 과목\n"
                            "\n"
                            "# 특정 행 (학생 전체 성적)\n"
                            "print(grades[0])     # [85 92 78] — 1번 학생 전체\n"
                            "print(grades[0, :])  # 위와 동일\n"
                            "\n"
                            "# 특정 열 (과목별 전체 성적)\n"
                            "print(grades[:, 0])  # [85 90 72 95 65] — 국어 점수 전체\n"
                            "print(grades[:, 1])  # [92 88 85 97 70] — 수학 점수 전체\n"
                            "\n"
                            "# 부분 행렬 슬라이싱\n"
                            "print(grades[1:3, :2])  # 2~3번 학생의 국어/수학\n"
                            "# [[90 88]\n"
                            "#  [72 85]]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "불리언 인덱싱 (Boolean Indexing)",
                    },
                    "조건을 만족하는 원소만 선택하는 강력한 기능입니다. 데이터 필터링에 핵심적으로 사용됩니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "scores = np.array([85, 92, 78, 95, 88, 76, 90])\n"
                            "\n"
                            "# 조건 마스크 생성 (True/False 배열)\n"
                            "mask = scores >= 90\n"
                            "print(mask)  # [False  True False  True False False  True]\n"
                            "\n"
                            "# 마스크로 필터링\n"
                            "high_scores = scores[mask]\n"
                            "print(high_scores)  # [92 95 90] — 90점 이상만\n"
                            "\n"
                            "# 한 줄로 작성\n"
                            "print(scores[scores >= 90])   # [92 95 90]\n"
                            "print(scores[scores < 80])    # [78 76]\n"
                            "\n"
                            "# 복합 조건: & (and), | (or), ~ (not)\n"
                            "print(scores[(scores >= 80) & (scores < 90)])  # [85 88]\n"
                            "print(scores[(scores < 80) | (scores >= 95)])  # [78 95 76]\n"
                            "\n"
                            "# 2D에서 불리언 인덱싱\n"
                            "grades = np.array([[85, 92, 78], [90, 88, 95], [72, 85, 80]])\n"
                            "# 80점 미만인 점수들을 70으로 올리기 (조건 마스킹 후 값 할당)\n"
                            "low_mask = grades < 80\n"
                            "new_grades = grades.copy()  # 원본 보존 (불변성 원칙)\n"
                            "new_grades[low_mask] = 70\n"
                            "print(new_grades)"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "NumPy 슬라이싱은 뷰(view)를 반환합니다. "
                            "즉 슬라이스를 수정하면 원본 배열도 변경됩니다! "
                            "원본을 보존하려면 반드시 .copy()를 사용하세요."
                        ),
                    },
                ],
            },
            {
                "title": "기본 연산 — 브로드캐스팅과 벡터 연산",
                "content": [
                    "NumPy의 핵심 강점은 루프 없이 배열 전체에 연산을 적용하는 벡터 연산입니다. "
                    "브로드캐스팅은 크기가 다른 배열 간의 연산을 자동으로 처리하는 규칙입니다.",
                    {
                        "type": "heading",
                        "text": "기본 산술 연산",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "a = np.array([1, 2, 3, 4, 5])\n"
                            "b = np.array([10, 20, 30, 40, 50])\n"
                            "\n"
                            "# 원소별 연산 (element-wise)\n"
                            "print(a + b)   # [11 22 33 44 55]\n"
                            "print(a - b)   # [ -9 -18 -27 -36 -45]\n"
                            "print(a * b)   # [10 40 90 160 250]\n"
                            "print(b / a)   # [10. 10. 10. 10. 10.]\n"
                            "print(a ** 2)  # [ 1  4  9 16 25]\n"
                            "\n"
                            "# 스칼라 연산 (브로드캐스팅의 가장 단순한 형태)\n"
                            "scores = np.array([75, 80, 85, 90, 95])\n"
                            "print(scores + 5)     # [80 85 90 95 100] — 모든 점수에 +5\n"
                            "print(scores * 1.1)   # 10% 가산점\n"
                            "print((scores - 70) * 2)  # 기준점 70에서 2배 환산"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "브로드캐스팅 — 크기가 다른 배열 간 연산",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 2D 배열 + 1D 배열 브로드캐스팅\n"
                            "# 5명 학생, 3과목 (원점수)\n"
                            "grades = np.array([\n"
                            "    [85, 92, 78],\n"
                            "    [90, 88, 95],\n"
                            "    [72, 85, 80],\n"
                            "])\n"
                            "\n"
                            "# 각 과목별 가산점: 국어+2, 수학+5, 영어+3\n"
                            "bonus = np.array([2, 5, 3])\n"
                            "\n"
                            "# shape (3, 3) + shape (3,) → 브로드캐스팅으로 (3, 3)\n"
                            "new_grades = grades + bonus\n"
                            "print(new_grades)\n"
                            "# [[87 97 81]\n"
                            "#  [92 93 98]\n"
                            "#  [74 90 83]]\n"
                            "\n"
                            "# 각 학생별 기준점 차감: 1번-70, 2번-75, 3번-65\n"
                            "baseline = np.array([70, 75, 65]).reshape(3, 1)  # 열 벡터\n"
                            "print(grades - baseline)\n"
                            "# [[15 22  8]\n"
                            "#  [15 13 20]\n"
                            "#  [ 7 20 15]]"
                        ),
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "브로드캐스팅은 '자동 복사-붙여넣기'라고 생각하면 됩니다. "
                            "작은 배열이 큰 배열의 크기에 맞게 자동으로 복제되어 연산이 수행됩니다. "
                            "실제로 메모리에 복사하지 않고 계산하기 때문에 메모리 효율적입니다."
                        ),
                    },
                ],
            },
            {
                "title": "유니버설 함수 (ufunc) — 집계와 수학 연산",
                "content": [
                    "NumPy는 수학 연산, 집계, 통계 함수를 배열 전체에 빠르게 적용하는 ufunc을 제공합니다. "
                    "Python 내장 함수(sum, max 등)보다 훨씬 빠르고 축(axis) 개념으로 방향을 지정할 수 있습니다.",
                    {
                        "type": "heading",
                        "text": "기본 집계 함수",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 5명 학생, 3과목 성적\n"
                            "grades = np.array([\n"
                            "    [85, 92, 78],\n"
                            "    [90, 88, 95],\n"
                            "    [72, 85, 80],\n"
                            "    [95, 97, 92],\n"
                            "    [65, 70, 75],\n"
                            "])\n"
                            "\n"
                            "# 전체 집계\n"
                            "print(f'총합:    {np.sum(grades)}')    # 1449\n"
                            "print(f'평균:    {np.mean(grades):.2f}')  # 96.60\n"
                            "print(f'최대:    {np.max(grades)}')    # 97\n"
                            "print(f'최솟값:  {np.min(grades)}')    # 65\n"
                            "print(f'표준편차: {np.std(grades):.2f}') # 10.14\n"
                            "\n"
                            "# axis=0: 열 방향 (각 과목별)\n"
                            "print('과목별 평균:', np.mean(grades, axis=0))\n"
                            "# [81.4 86.4 84.0]\n"
                            "\n"
                            "# axis=1: 행 방향 (각 학생별)\n"
                            "print('학생별 평균:', np.mean(grades, axis=1))\n"
                            "# [85.   91.   79.   94.67 70.  ]\n"
                            "\n"
                            "# 최댓값의 인덱스\n"
                            "print('최고 성적 학생:', np.argmax(np.mean(grades, axis=1)))  # 3"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "수학 함수들",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "x = np.array([1.0, 4.0, 9.0, 16.0, 25.0])\n"
                            "\n"
                            "print(np.sqrt(x))   # [1. 2. 3. 4. 5.] — 제곱근\n"
                            "print(np.abs(np.array([-3, -1, 0, 2, 5])))  # [3 1 0 2 5] — 절댓값\n"
                            "print(np.exp(np.array([0, 1, 2])))  # [1. 2.718 7.389] — e^x\n"
                            "print(np.log(np.array([1, np.e, np.e**2])))  # [0. 1. 2.] — 자연로그\n"
                            "\n"
                            "# 반올림 계열\n"
                            "vals = np.array([1.2, 2.5, 3.7, 4.1])\n"
                            "print(np.round(vals))   # [1. 2. 4. 4.] — 반올림\n"
                            "print(np.floor(vals))   # [1. 2. 3. 4.] — 내림\n"
                            "print(np.ceil(vals))    # [2. 3. 4. 5.] — 올림\n"
                            "\n"
                            "# 정렬\n"
                            "scores = np.array([85, 92, 78, 95, 88])\n"
                            "print(np.sort(scores))           # [78 85 88 92 95] — 오름차순\n"
                            "print(np.sort(scores)[::-1])     # [95 92 88 85 78] — 내림차순\n"
                            "print(np.argsort(scores))        # [2 0 4 1 3] — 정렬 인덱스"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "np.sum(), np.mean() 등은 grades.sum(), grades.mean()으로도 호출할 수 있습니다. "
                            "배열의 메서드 형태로 부르는 것이 더 간결할 때가 많습니다."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "실용 예제 — 성적 분포 분석",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 30명 학생 성적 시뮬레이션\n"
                            "np.random.seed(42)\n"
                            "class_scores = np.random.randint(50, 101, size=30)\n"
                            "\n"
                            "# 기술 통계\n"
                            "stats = {\n"
                            "    '평균': np.mean(class_scores),\n"
                            "    '중앙값': np.median(class_scores),\n"
                            "    '표준편차': np.std(class_scores),\n"
                            "    '최솟값': np.min(class_scores),\n"
                            "    '최댓값': np.max(class_scores),\n"
                            "    '범위': np.ptp(class_scores),  # peak-to-peak\n"
                            "    'Q1': np.percentile(class_scores, 25),\n"
                            "    'Q3': np.percentile(class_scores, 75),\n"
                            "}\n"
                            "\n"
                            "for k, v in stats.items():\n"
                            "    print(f'{k:6s}: {v:.1f}')\n"
                            "\n"
                            "# 등급 분포\n"
                            "a_grade = np.sum(class_scores >= 90)  # A등급\n"
                            "b_grade = np.sum((class_scores >= 80) & (class_scores < 90))\n"
                            "print(f'\\nA등급: {a_grade}명, B등급: {b_grade}명')"
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "배열을 수정하기 전에 항상 .copy()를 사용하세요. "
            "NumPy 슬라이싱은 뷰(view)를 반환하므로 원본 데이터가 예상치 못하게 바뀔 수 있습니다.",
            "axis 파라미터를 헷갈린다면: axis=0은 '행을 따라' (결과가 열 방향), "
            "axis=1은 '열을 따라' (결과가 행 방향)으로 기억하세요.",
            "dtype을 명시적으로 지정하면 메모리 사용량과 계산 정확도를 제어할 수 있습니다. "
            "머신러닝 모델 입력에는 float32, 금융 계산에는 float64를 사용하세요.",
            "np.where(조건, 참일 때 값, 거짓일 때 값)는 조건부 배열을 만들 때 유용합니다. "
            "예: np.where(scores >= 80, 'pass', 'fail')",
            "%timeit을 사용해 Python 루프 vs NumPy 연산의 속도를 직접 비교해보세요. "
            "차이를 눈으로 확인하면 NumPy를 더 적극적으로 사용하게 됩니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "다음 코드의 출력 결과는?\n\na = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a.shape, a.ndim, a.size)",
                "choices": [
                    "(2, 3) 2 6",
                    "(3, 2) 2 6",
                    "(2, 3) 3 6",
                    "(6,) 1 6",
                ],
                "answer": 0,
                "explanation": (
                    "a는 2행 3열의 2D 배열입니다. "
                    "shape는 (2, 3), ndim은 2차원이므로 2, "
                    "size는 전체 원소 수인 2×3=6입니다."
                ),
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "아래 코드에서 grades[:, 0]이 의미하는 것은?\n\n"
                    "grades = np.array([[85, 92, 78], [90, 88, 95], [72, 85, 80]])"
                ),
                "choices": [
                    "첫 번째 행 전체: [85, 92, 78]",
                    "첫 번째 열 전체: [85, 90, 72]",
                    "모든 행의 마지막 원소: [78, 95, 80]",
                    "전체 배열의 평균",
                ],
                "answer": 1,
                "explanation": (
                    "grades[:, 0]에서 :는 '모든 행'을 의미하고, 0은 첫 번째 열(인덱스 0)을 의미합니다. "
                    "따라서 모든 행의 첫 번째 원소, 즉 [85, 90, 72]가 반환됩니다."
                ),
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "다음 조건에 맞는 코드를 작성하세요.\n\n"
                    "① 1부터 20까지 홀수로만 이루어진 배열을 np.arange로 생성\n"
                    "② 해당 배열에서 10보다 큰 원소만 불리언 인덱싱으로 추출\n"
                    "③ 추출된 배열의 합, 평균, 최댓값을 출력\n"
                    "④ 원본 배열은 수정하지 말 것"
                ),
                "answer_code": (
                    "import numpy as np\n"
                    "\n"
                    "# ① 1부터 20까지 홀수 배열\n"
                    "odd_arr = np.arange(1, 21, 2)  # [1 3 5 7 9 11 13 15 17 19]\n"
                    "print('원본:', odd_arr)\n"
                    "\n"
                    "# ② 10보다 큰 원소 추출 (불리언 인덱싱)\n"
                    "filtered = odd_arr[odd_arr > 10]  # [11 13 15 17 19]\n"
                    "print('필터링 결과:', filtered)\n"
                    "\n"
                    "# ③ 집계\n"
                    "print(f'합계:  {np.sum(filtered)}')\n"
                    "print(f'평균:  {np.mean(filtered):.1f}')\n"
                    "print(f'최댓값: {np.max(filtered)}')\n"
                    "\n"
                    "# ④ 원본 확인 (변경되지 않아야 함)\n"
                    "print('원본 확인:', odd_arr)"
                ),
            },
            {
                "number": 4,
                "type": "multiple_choice",
                "question": (
                    "다음 브로드캐스팅 코드의 결과는?\n\n"
                    "a = np.array([[1, 2, 3], [4, 5, 6]])\n"
                    "b = np.array([10, 20, 30])\n"
                    "print(a + b)"
                ),
                "choices": [
                    "[[11 22 33]\n [14 25 36]]",
                    "[[11 12 13]\n [24 25 26]]",
                    "오류: 크기가 다른 배열은 더할 수 없다",
                    "[[10 40 90]\n [40 100 180]]",
                ],
                "answer": 0,
                "explanation": (
                    "b의 shape (3,)가 a의 shape (2, 3)의 마지막 차원과 일치하므로 브로드캐스팅이 가능합니다. "
                    "b가 [[10, 20, 30], [10, 20, 30]]으로 복제되어 a와 더해집니다. "
                    "결과: [[1+10, 2+20, 3+30], [4+10, 5+20, 6+30]] = [[11, 22, 33], [14, 25, 36]]"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "10명의 학생 성적 데이터(아래)를 NumPy 배열로 만들고 다음을 구하세요.\n\n"
                    "scores = [78, 65, 92, 88, 73, 95, 81, 67, 84, 90]\n\n"
                    "① 평균, 중앙값, 표준편차 출력\n"
                    "② 평균 이상인 학생 수\n"
                    "③ 상위 3명의 점수 (내림차순 정렬 후 앞 3개)\n"
                    "④ 각 점수를 100점 만점 기준으로 정규화 (0~1 사이 값으로)"
                ),
                "answer_code": (
                    "import numpy as np\n"
                    "\n"
                    "scores = np.array([78, 65, 92, 88, 73, 95, 81, 67, 84, 90])\n"
                    "\n"
                    "# ① 기술 통계\n"
                    "print(f'평균:    {np.mean(scores):.2f}')\n"
                    "print(f'중앙값:  {np.median(scores):.1f}')\n"
                    "print(f'표준편차: {np.std(scores):.2f}')\n"
                    "\n"
                    "# ② 평균 이상인 학생 수\n"
                    "avg = np.mean(scores)\n"
                    "above_avg = np.sum(scores >= avg)\n"
                    "print(f'\\n평균({avg:.1f}) 이상: {above_avg}명')\n"
                    "\n"
                    "# ③ 상위 3명의 점수\n"
                    "top3 = np.sort(scores)[::-1][:3]\n"
                    "print(f'상위 3명: {top3}')\n"
                    "\n"
                    "# ④ 정규화 (min-max scaling)\n"
                    "normalized = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))\n"
                    "print(f'\\n정규화:')\n"
                    "for orig, norm in zip(scores, normalized):\n"
                    "    print(f'  {orig}점 → {norm:.3f}')"
                ),
            },
        ],
        "challenge": {
            "question": (
                "학교에서 30명의 학생이 5과목 시험을 봤습니다. "
                "np.random.seed(42)를 사용해 50~100 사이의 정수 점수를 생성하고 다음을 구현하세요.\n\n"
                "① 전체 성적 배열 생성 (shape: 30×5)\n"
                "② 각 학생의 총점과 평균 계산\n"
                "③ 평균이 가장 높은 학생과 가장 낮은 학생의 인덱스\n"
                "④ 과목별 평균, 최고점, 최저점을 테이블 형태로 출력\n"
                "⑤ 전체 학생 중 3과목 이상 80점 이상인 학생 수"
            ),
            "hint": (
                "np.random.randint(50, 101, size=(30, 5))로 배열을 생성하고, "
                "axis=1로 학생별 집계, axis=0으로 과목별 집계를 수행하세요. "
                "⑤번은 (grades >= 80)으로 불리언 배열을 만든 후 "
                ".sum(axis=1)로 각 학생이 80점 이상인 과목 수를 구할 수 있습니다."
            ),
        },
        "summary": [
            "NumPy ndarray는 연속 메모리 구조로 Python 리스트보다 10~100배 빠른 수치 연산을 제공합니다.",
            "배열 생성: np.array, np.zeros/ones/full, np.arange, np.linspace 중 용도에 맞게 선택합니다.",
            "배열 속성: shape(형태), ndim(차원 수), size(원소 수), dtype(타입)을 항상 확인하세요.",
            "2D 배열 인덱싱은 [행, 열] 형태이며, [:, 0]은 첫 번째 열 전체를 의미합니다.",
            "불리언 인덱싱으로 조건에 맞는 원소만 효율적으로 필터링할 수 있습니다.",
            "axis 파라미터: axis=0은 행 방향 집계(과목별), axis=1은 열 방향 집계(학생별)입니다.",
        ],
    }
