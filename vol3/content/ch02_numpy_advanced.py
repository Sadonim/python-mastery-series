"""
Ch 2: NumPy 심화
Python Mastery Series Vol.3 — 데이터 분석
"""


def get_chapter():
    return {
        "number": 2,
        "title": "NumPy 심화",
        "subtitle": "배열 변형, 결합, 난수, 선형대수까지",
        "big_picture": (
            "Ch 1에서 ndarray의 기초를 배웠다면, 이제 실전에서 꼭 필요한 심화 기능을 익힙니다. "
            "데이터를 원하는 형태로 변형하고, 여러 배열을 합치거나 나누고, "
            "난수로 시뮬레이션 데이터를 만들고, 선형대수 연산으로 머신러닝의 기초를 다집니다."
        ),
        "sections": [
            {
                "title": "배열 변형 — reshape, flatten, transpose",
                "content": [
                    "데이터를 원하는 형태로 바꾸는 것은 NumPy 작업의 핵심입니다. "
                    "특히 머신러닝 모델에 데이터를 입력할 때 올바른 shape으로 맞춰주는 것이 매우 중요합니다.",
                    {
                        "type": "heading",
                        "text": "reshape — 형태 바꾸기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 1D → 2D\n"
                            "arr = np.arange(12)  # [0 1 2 3 4 5 6 7 8 9 10 11]\n"
                            "mat = arr.reshape(3, 4)  # 3행 4열\n"
                            "print(mat)\n"
                            "# [[ 0  1  2  3]\n"
                            "#  [ 4  5  6  7]\n"
                            "#  [ 8  9 10 11]]\n"
                            "\n"
                            "# -1을 쓰면 해당 차원 크기를 자동 계산\n"
                            "print(arr.reshape(4, -1))   # 4행 → 4×3 = (4, 3)\n"
                            "print(arr.reshape(-1, 6))   # 6열 → 12/6=2행 = (2, 6)\n"
                            "print(arr.reshape(-1, 1))   # 열 벡터 (12, 1)\n"
                            "\n"
                            "# reshape은 원소 수가 같아야 함\n"
                            "# arr.reshape(3, 5)  # 오류! 12 ≠ 3×5\n"
                            "\n"
                            "# 뷰 vs 복사: reshape은 가능하면 뷰를 반환\n"
                            "mat2 = arr.reshape(2, 6)\n"
                            "mat2[0, 0] = 999\n"
                            "print(arr[0])  # 999 — 원본도 변경됨! .copy() 주의"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "flatten & ravel — 다차원을 1D로",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "mat = np.array([[1, 2, 3], [4, 5, 6]])\n"
                            "\n"
                            "# flatten() — 항상 복사본 반환 (안전)\n"
                            "flat = mat.flatten()\n"
                            "flat[0] = 999\n"
                            "print(mat[0, 0])  # 1 — 원본 유지됨\n"
                            "\n"
                            "# ravel() — 가능하면 뷰 반환 (빠름)\n"
                            "raveled = mat.ravel()\n"
                            "print(raveled)  # [1 2 3 4 5 6]\n"
                            "\n"
                            "# reshape(-1)과 동일한 효과\n"
                            "print(mat.reshape(-1))  # [1 2 3 4 5 6]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "transpose — 행과 열 바꾸기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "mat = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)\n"
                            "\n"
                            "# .T 속성으로 전치\n"
                            "print(mat.T)  # shape (3, 2)\n"
                            "# [[1 4]\n"
                            "#  [2 5]\n"
                            "#  [3 6]]\n"
                            "\n"
                            "# np.transpose()로도 가능\n"
                            "print(np.transpose(mat))\n"
                            "\n"
                            "# 실용 예제: 행렬 곱에서 shape 맞추기\n"
                            "# (30, 5) 성적표를 (5, 30)으로 — 과목별 분석\n"
                            "grades = np.random.randint(60, 101, size=(30, 5))\n"
                            "print(f'원본: {grades.shape}')         # (30, 5)\n"
                            "print(f'전치: {grades.T.shape}')       # (5, 30)"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "머신러닝에서 입력 데이터의 shape을 맞추는 것은 매우 빈번한 작업입니다. "
                            "reshape(-1, 1)은 1D 배열을 열 벡터로 만들 때, "
                            "reshape(1, -1)은 행 벡터로 만들 때 자주 씁니다."
                        ),
                    },
                ],
            },
            {
                "title": "배열 결합과 분할",
                "content": [
                    "여러 배열을 하나로 합치거나 하나를 여러 개로 나누는 작업입니다. "
                    "데이터셋을 병합하거나 학습/테스트 데이터로 분할할 때 사용합니다.",
                    {
                        "type": "heading",
                        "text": "결합 — concatenate, vstack, hstack",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "a = np.array([[1, 2], [3, 4]])\n"
                            "b = np.array([[5, 6], [7, 8]])\n"
                            "\n"
                            "# np.concatenate — axis 지정\n"
                            "print(np.concatenate([a, b], axis=0))  # 행 방향 결합 (위아래)\n"
                            "# [[1 2], [3 4], [5 6], [7 8]]  shape (4, 2)\n"
                            "\n"
                            "print(np.concatenate([a, b], axis=1))  # 열 방향 결합 (좌우)\n"
                            "# [[1 2 5 6], [3 4 7 8]]  shape (2, 4)\n"
                            "\n"
                            "# np.vstack — 수직 결합 (axis=0과 동일)\n"
                            "print(np.vstack([a, b]))  # shape (4, 2)\n"
                            "\n"
                            "# np.hstack — 수평 결합 (axis=1과 동일)\n"
                            "print(np.hstack([a, b]))  # shape (2, 4)\n"
                            "\n"
                            "# 실용 예제: 특성(feature)과 레이블(label) 합치기\n"
                            "features = np.random.rand(100, 3)   # 100행 3열\n"
                            "labels = np.random.randint(0, 2, size=(100, 1))  # 100행 1열\n"
                            "dataset = np.hstack([features, labels])  # (100, 4)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "np.stack — 새 축으로 쌓기",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "a = np.array([1, 2, 3])\n"
                            "b = np.array([4, 5, 6])\n"
                            "\n"
                            "# stack은 새로운 축을 추가해서 쌓음\n"
                            "s0 = np.stack([a, b], axis=0)  # shape (2, 3) — 행 방향\n"
                            "s1 = np.stack([a, b], axis=1)  # shape (3, 2) — 열 방향\n"
                            "print(s0)\n"
                            "# [[1 2 3]\n"
                            "#  [4 5 6]]\n"
                            "\n"
                            "# 이미지 처리 예: R, G, B 채널 합치기\n"
                            "r = np.zeros((64, 64))   # 빨강 채널\n"
                            "g = np.zeros((64, 64))   # 초록 채널\n"
                            "b_ch = np.zeros((64, 64))  # 파랑 채널\n"
                            "image = np.stack([r, g, b_ch], axis=2)  # (64, 64, 3)"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "분할 — split, hsplit, vsplit",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "arr = np.arange(12).reshape(4, 3)\n"
                            "\n"
                            "# np.split — 균등 분할\n"
                            "parts = np.split(arr, 2, axis=0)  # 행을 반으로\n"
                            "print(parts[0])  # [[0 1 2], [3 4 5]]\n"
                            "print(parts[1])  # [[6 7 8], [9 10 11]]\n"
                            "\n"
                            "# 학습/검증 데이터 분할 예시\n"
                            "data = np.arange(100)\n"
                            "train, test = np.split(data, [80])  # 앞 80개 학습, 뒤 20개 테스트\n"
                            "print(f'학습: {len(train)}개, 테스트: {len(test)}개')"
                        ),
                    },
                ],
            },
            {
                "title": "브로드캐스팅 규칙 상세",
                "content": [
                    "브로드캐스팅은 NumPy에서 가장 헷갈리는 개념 중 하나입니다. "
                    "규칙을 명확히 이해하면 복잡한 배열 연산도 루프 없이 처리할 수 있습니다.",
                    {
                        "type": "heading",
                        "text": "브로드캐스팅 3가지 규칙",
                    },
                    {
                        "type": "numbered_list",
                        "items": [
                            "두 배열의 ndim(차원 수)이 다르면, 차원 수가 적은 배열의 shape 앞에 1을 채웁니다.",
                            "어떤 차원의 크기가 1이면, 다른 배열의 해당 차원 크기에 맞게 '늘어납니다'.",
                            "어떤 차원에서도 크기가 다르고 둘 다 1이 아니면 오류가 발생합니다.",
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 규칙 적용 예시\n"
                            "# a: shape (4, 3)\n"
                            "# b: shape (3,)  → 규칙1: (1, 3) → 규칙2: (4, 3)\n"
                            "a = np.ones((4, 3))\n"
                            "b = np.array([1, 2, 3])\n"
                            "print((a + b).shape)  # (4, 3) — 성공\n"
                            "\n"
                            "# a: shape (4, 1)\n"
                            "# b: shape (3,)   → 규칙1: (1, 3) → 둘 다 브로드캐스팅\n"
                            "a = np.array([[1], [2], [3], [4]])  # (4, 1)\n"
                            "b = np.array([10, 20, 30])          # (3,) → (1, 3)\n"
                            "print(a + b)  # shape (4, 3)\n"
                            "# [[11 21 31]\n"
                            "#  [12 22 32]\n"
                            "#  [13 23 33]\n"
                            "#  [14 24 34]]\n"
                            "\n"
                            "# 실패 케이스\n"
                            "# a: shape (4, 2), b: shape (3,) → (1, 3)\n"
                            "# 2 vs 3 — 둘 다 1이 아니고 다름 → 오류\n"
                            "# np.ones((4, 2)) + np.array([1, 2, 3])  # ValueError!"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "브로드캐스팅 실용 예제 — 표준화(Standardization)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 머신러닝에서 자주 쓰는 특성 표준화\n"
                            "# 각 열(특성)의 평균=0, 표준편차=1로 변환\n"
                            "\n"
                            "# 100명의 키(cm), 몸무게(kg), 나이 데이터\n"
                            "np.random.seed(42)\n"
                            "data = np.column_stack([\n"
                            "    np.random.normal(170, 10, 100),  # 키: 평균 170\n"
                            "    np.random.normal(65, 15, 100),   # 몸무게: 평균 65\n"
                            "    np.random.randint(20, 60, 100),  # 나이: 20~60\n"
                            "])\n"
                            "print('원본 shape:', data.shape)  # (100, 3)\n"
                            "\n"
                            "# 각 열의 평균, 표준편차 계산 (axis=0 → 열 방향)\n"
                            "mean = data.mean(axis=0)   # shape (3,)\n"
                            "std = data.std(axis=0)     # shape (3,)\n"
                            "\n"
                            "# 브로드캐스팅: (100, 3) - (3,) → (100, 3)\n"
                            "standardized = (data - mean) / std\n"
                            "print('표준화 후 평균:', standardized.mean(axis=0).round(10))\n"
                            "print('표준화 후 표준편차:', standardized.std(axis=0).round(2))"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "브로드캐스팅이 헷갈리면 배열의 shape을 프린트해서 확인하는 것이 가장 빠릅니다. "
                            "NumPy 오류 메시지에는 두 배열의 shape이 표시되므로 "
                            "'operands could not be broadcast together with shapes'가 뜨면 "
                            "각 배열의 shape을 먼저 출력해보세요."
                        ),
                    },
                ],
            },
            {
                "title": "난수 생성 — np.random",
                "content": [
                    "실제 데이터가 없을 때 시뮬레이션 데이터를 만들거나, "
                    "머신러닝에서 가중치 초기화, 데이터 셔플링 등에 난수가 필수입니다.",
                    {
                        "type": "heading",
                        "text": "시드(seed)와 재현성",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# seed 없이 실행하면 매번 다른 결과\n"
                            "print(np.random.randint(0, 10, 5))  # 실행마다 다름\n"
                            "\n"
                            "# seed를 고정하면 항상 같은 결과 (재현 가능)\n"
                            "np.random.seed(42)\n"
                            "print(np.random.randint(0, 10, 5))  # 항상 [0 5 0 3 3]\n"
                            "\n"
                            "np.random.seed(42)  # 다시 seed 설정\n"
                            "print(np.random.randint(0, 10, 5))  # 동일하게 [0 5 0 3 3]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "주요 난수 함수",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "np.random.seed(42)\n"
                            "\n"
                            "# 정수 난수\n"
                            "dice = np.random.randint(1, 7, size=10)  # 주사위 10번\n"
                            "print('주사위:', dice)\n"
                            "\n"
                            "# 균등 분포 (0.0 ~ 1.0)\n"
                            "uniform = np.random.rand(5)      # [0, 1) 균등\n"
                            "uniform2 = np.random.uniform(2, 5, size=5)  # [2, 5) 균등\n"
                            "print('균등 분포:', uniform.round(3))\n"
                            "\n"
                            "# 정규 분포 (가우시안)\n"
                            "normal = np.random.randn(5)           # 평균 0, 표준편차 1\n"
                            "heights = np.random.normal(170, 10, size=100)  # 평균 170, 표준편차 10\n"
                            "print(f'신장 데이터: 평균={heights.mean():.1f}, 표준편차={heights.std():.1f}')\n"
                            "\n"
                            "# 선택 (샘플링)\n"
                            "items = ['사과', '바나나', '딸기', '포도']\n"
                            "print(np.random.choice(items, size=3))           # 복원 추출\n"
                            "print(np.random.choice(items, size=3, replace=False))  # 비복원 추출\n"
                            "\n"
                            "# 배열 섞기\n"
                            "arr = np.arange(10)\n"
                            "shuffled = arr.copy()\n"
                            "np.random.shuffle(shuffled)  # 제자리에서 섞음 (복사본 사용)\n"
                            "print('섞기:', shuffled)"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["함수", "분포/용도", "예시"],
                        "rows": [
                            ["np.random.randint(low, high, size)", "균등 정수", "주사위, 인덱스"],
                            ["np.random.rand(size)", "균등 실수 [0, 1)", "확률값, 가중치"],
                            ["np.random.normal(mean, std, size)", "정규 분포", "키, 몸무게, 노이즈"],
                            ["np.random.choice(arr, size, replace)", "배열에서 샘플링", "bootstrap, 데이터 분할"],
                            ["np.random.shuffle(arr)", "제자리 셔플", "데이터 섞기"],
                            ["np.random.permutation(n)", "순열 반환", "인덱스 셔플"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "최신 NumPy(1.17+)에서는 np.random.default_rng(seed)로 "
                            "Generator 객체를 만들어 사용하는 것이 권장됩니다. "
                            "멀티스레드 환경에서 더 안전하고, rng.integers(), rng.standard_normal() 등 "
                            "일관된 API를 제공합니다."
                        ),
                    },
                ],
            },
            {
                "title": "선형대수 기초 — np.dot과 np.linalg",
                "content": [
                    "선형대수는 머신러닝의 수학적 기초입니다. "
                    "NumPy는 행렬 연산, 역행렬, 고유값 등 핵심 선형대수 기능을 제공합니다.",
                    {
                        "type": "heading",
                        "text": "행렬 곱 — np.dot과 @ 연산자",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "A = np.array([[1, 2], [3, 4]])  # (2, 2)\n"
                            "B = np.array([[5, 6], [7, 8]])  # (2, 2)\n"
                            "\n"
                            "# 행렬 곱 (내적): np.dot 또는 @ 연산자\n"
                            "print(np.dot(A, B))\n"
                            "print(A @ B)       # 동일한 결과\n"
                            "# [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]]\n"
                            "# [[19 22]\n"
                            "#  [43 50]]\n"
                            "\n"
                            "# 원소별 곱 (행렬 곱이 아님)\n"
                            "print(A * B)  # [[5 12], [21 32]]\n"
                            "\n"
                            "# 벡터 내적\n"
                            "v1 = np.array([1, 2, 3])\n"
                            "v2 = np.array([4, 5, 6])\n"
                            "print(np.dot(v1, v2))  # 1*4 + 2*5 + 3*6 = 32\n"
                            "\n"
                            "# 머신러닝 예: 선형 회귀 예측\n"
                            "# y = Xw (X: 입력 데이터, w: 가중치)\n"
                            "X = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)\n"
                            "w = np.array([0.5, -0.3])               # (2,)\n"
                            "y_pred = X @ w  # (3,)\n"
                            "print('예측값:', y_pred)  # [0.4 0.3 0.2]"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "np.linalg — 선형대수 핵심 연산",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "A = np.array([[2, 1], [5, 3]], dtype=float)\n"
                            "\n"
                            "# 역행렬\n"
                            "A_inv = np.linalg.inv(A)\n"
                            "print('역행렬:\\n', A_inv)\n"
                            "\n"
                            "# A @ A_inv = 단위행렬 확인\n"
                            "identity = A @ A_inv\n"
                            "print('검증 (단위행렬에 가까울수록 OK):\\n', identity.round(10))\n"
                            "\n"
                            "# 행렬식 (determinant)\n"
                            "print('행렬식:', np.linalg.det(A))  # 2*3 - 1*5 = 1\n"
                            "\n"
                            "# 연립방정식 풀기: Ax = b\n"
                            "# 2x + y = 5\n"
                            "# 5x + 3y = 13\n"
                            "A = np.array([[2, 1], [5, 3]], dtype=float)\n"
                            "b = np.array([5, 13], dtype=float)\n"
                            "x = np.linalg.solve(A, b)\n"
                            "print('해:', x)  # [2. 1.] → x=2, y=1\n"
                            "\n"
                            "# 고유값, 고유벡터\n"
                            "eigenvalues, eigenvectors = np.linalg.eig(A)\n"
                            "print('고유값:', eigenvalues)\n"
                            "\n"
                            "# 노름(크기)\n"
                            "v = np.array([3.0, 4.0])\n"
                            "print('L2 노름:', np.linalg.norm(v))  # 5.0 (피타고라스)"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "np.linalg.solve(A, b)는 역행렬을 직접 구하는 것보다 "
                            "수치적으로 안정적이고 빠릅니다. "
                            "연립방정식을 풀 때는 inv(A) @ b보다 solve(A, b)를 사용하세요."
                        ),
                    },
                ],
            },
            {
                "title": "실용 예제 — 성적 분석과 이미지 데이터 기초",
                "content": [
                    "지금까지 배운 내용을 종합해서 실제 분석 시나리오에 적용해봅니다.",
                    {
                        "type": "heading",
                        "text": "예제 1: 성적 분석 종합",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "np.random.seed(7)\n"
                            "# 30명, 5과목 성적 (60~100점)\n"
                            "grades = np.random.randint(60, 101, size=(30, 5))\n"
                            "subjects = ['국어', '수학', '영어', '과학', '사회']\n"
                            "\n"
                            "# 1. 학생별 총점, 평균\n"
                            "totals = grades.sum(axis=1)      # shape (30,)\n"
                            "averages = grades.mean(axis=1)   # shape (30,)\n"
                            "\n"
                            "# 2. 과목별 통계\n"
                            "print('=== 과목별 통계 ===')\n"
                            "for i, subj in enumerate(subjects):\n"
                            "    col = grades[:, i]\n"
                            "    print(f'{subj}: 평균={col.mean():.1f}, '\n"
                            "          f'최고={col.max()}, 최저={col.min()}')\n"
                            "\n"
                            "# 3. 석차 계산 (총점 기준)\n"
                            "ranks = np.argsort(np.argsort(-totals)) + 1  # 내림차순 순위\n"
                            "top5_idx = np.argsort(-totals)[:5]\n"
                            "print('\\n=== 상위 5명 ===')\n"
                            "for idx in top5_idx:\n"
                            "    print(f'  학생 {idx+1:2d}번: 총점={totals[idx]}, '\n"
                            "          f'평균={averages[idx]:.1f}, 석차={ranks[idx]}')\n"
                            "\n"
                            "# 4. 부진 학생 (평균 70 미만) 과목별 보충 필요 여부\n"
                            "low_students = np.where(averages < 70)[0]\n"
                            "print(f'\\n보충 필요 학생: {len(low_students)}명')\n"
                            "for idx in low_students:\n"
                            "    weak_subjects = [subjects[j] for j in np.where(grades[idx] < 70)[0]]\n"
                            "    print(f'  학생 {idx+1}번 취약 과목: {\", \".join(weak_subjects)}')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "예제 2: 이미지 데이터 기초 조작",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import numpy as np\n"
                            "\n"
                            "# 흑백 이미지: 픽셀값 0~255의 2D 배열\n"
                            "# 실제로는 PIL이나 cv2로 읽지만, NumPy 배열 형태 이해 목적\n"
                            "np.random.seed(42)\n"
                            "image = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)\n"
                            "print('이미지 shape:', image.shape)  # (8, 8)\n"
                            "print('dtype:', image.dtype)          # uint8\n"
                            "\n"
                            "# 1. 이미지 통계\n"
                            "print(f'밝기 평균: {image.mean():.1f}')\n"
                            "print(f'어두운 픽셀(< 50): {np.sum(image < 50)}개')\n"
                            "\n"
                            "# 2. 정규화: 0~255 → 0.0~1.0\n"
                            "normalized = image.astype(np.float32) / 255.0\n"
                            "print(f'\\n정규화 후: min={normalized.min():.3f}, max={normalized.max():.3f}')\n"
                            "\n"
                            "# 3. 밝기 반전 (네거티브 효과)\n"
                            "inverted = 255 - image\n"
                            "\n"
                            "# 4. 임계값 처리 (이진화)\n"
                            "binary = np.where(image > 127, 255, 0).astype(np.uint8)\n"
                            "print(f'이진화: 흰색 픽셀={np.sum(binary == 255)}개')\n"
                            "\n"
                            "# 5. RGB 이미지: (높이, 너비, 채널) 구조\n"
                            "rgb_image = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)\n"
                            "print(f'\\nRGB 이미지 shape: {rgb_image.shape}')  # (64, 64, 3)\n"
                            "# 채널 분리\n"
                            "r_channel = rgb_image[:, :, 0]  # 빨강\n"
                            "g_channel = rgb_image[:, :, 1]  # 초록\n"
                            "b_channel = rgb_image[:, :, 2]  # 파랑\n"
                            "print(f'빨강 채널 평균: {r_channel.mean():.1f}')"
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "reshape에서 -1을 활용하면 크기를 직접 계산하지 않아도 됩니다. "
            "특히 배치 크기가 변하는 상황에서 reshape(-1, features)처럼 쓰면 유용합니다.",
            "재현 가능한 실험을 위해 np.random.seed()는 스크립트 최상단에 한 번만 설정하세요. "
            "함수 안에서 seed를 설정하면 호출할 때마다 같은 난수가 나와 의도치 않은 결과가 생깁니다.",
            "대용량 배열을 다룰 때 dtype을 float64 대신 float32로 바꾸면 메모리가 절반으로 줄어듭니다. "
            "단, 정밀도가 필요한 금융 계산에는 float64를 유지하세요.",
            "np.linalg.matrix_rank()로 행렬의 랭크를 확인하면 역행렬이 존재하는지 "
            "사전에 파악할 수 있습니다 (랭크 = 행/열 수이면 역행렬 존재).",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "다음 코드의 결과로 올바른 것은?\n\n"
                    "a = np.arange(6)\n"
                    "b = a.reshape(2, 3)\n"
                    "b[0, 0] = 99\n"
                    "print(a[0])"
                ),
                "choices": [
                    "0",
                    "99",
                    "오류 발생",
                    "None",
                ],
                "answer": 1,
                "explanation": (
                    "reshape()은 가능한 경우 뷰(view)를 반환합니다. "
                    "b와 a는 같은 메모리를 공유하므로 b를 수정하면 a도 변경됩니다. "
                    "원본을 보호하려면 a.reshape(2, 3).copy()처럼 복사본을 사용해야 합니다."
                ),
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "np.vstack과 np.hstack의 차이를 가장 잘 설명한 것은?"
                ),
                "choices": [
                    "vstack은 새 축을 추가하고, hstack은 기존 축으로 결합한다",
                    "vstack은 위아래(행)로 쌓고, hstack은 좌우(열)로 붙인다",
                    "vstack은 1D 배열만, hstack은 2D 배열만 지원한다",
                    "두 함수는 기능이 동일하다",
                ],
                "answer": 1,
                "explanation": (
                    "np.vstack([a, b])는 a 아래에 b를 쌓아 행 수가 늘어납니다 (axis=0). "
                    "np.hstack([a, b])는 a 오른쪽에 b를 붙여 열 수가 늘어납니다 (axis=1). "
                    "새 축을 추가해서 쌓는 것은 np.stack()입니다."
                ),
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "다음 조건을 만족하는 코드를 작성하세요.\n\n"
                    "① np.random.seed(0) 설정\n"
                    "② 0~1 사이 균등 분포의 (4, 4) 행렬 A 생성\n"
                    "③ A를 전치(transpose)한 행렬 B 생성\n"
                    "④ A @ B 행렬 곱 계산\n"
                    "⑤ 결과 행렬의 대각선 원소 합(trace) 출력"
                ),
                "answer_code": (
                    "import numpy as np\n"
                    "\n"
                    "# ① seed 설정\n"
                    "np.random.seed(0)\n"
                    "\n"
                    "# ② (4, 4) 균등 분포 행렬\n"
                    "A = np.random.rand(4, 4)\n"
                    "\n"
                    "# ③ 전치 행렬\n"
                    "B = A.T\n"
                    "\n"
                    "# ④ 행렬 곱\n"
                    "C = A @ B\n"
                    "print('결과 행렬 shape:', C.shape)  # (4, 4)\n"
                    "print('결과 행렬:\\n', C.round(3))\n"
                    "\n"
                    "# ⑤ 대각선 원소 합 (trace)\n"
                    "trace = np.trace(C)\n"
                    "print(f'trace: {trace:.4f}')"
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "아래 연립방정식을 np.linalg.solve로 풀고, "
                    "결과를 원래 방정식에 대입해서 검증하세요.\n\n"
                    "3x + 2y - z = 1\n"
                    "2x - 2y + 4z = -2\n"
                    "-x + 0.5y - z = 0"
                ),
                "answer_code": (
                    "import numpy as np\n"
                    "\n"
                    "# 계수 행렬 A와 상수 벡터 b\n"
                    "A = np.array([\n"
                    "    [3,   2,  -1],\n"
                    "    [2,  -2,   4],\n"
                    "    [-1,  0.5, -1],\n"
                    "])\n"
                    "b = np.array([1, -2, 0], dtype=float)\n"
                    "\n"
                    "# 연립방정식 풀기\n"
                    "x = np.linalg.solve(A, b)\n"
                    "print(f'x={x[0]:.4f}, y={x[1]:.4f}, z={x[2]:.4f}')\n"
                    "\n"
                    "# 검증: A @ x ≈ b\n"
                    "check = A @ x\n"
                    "print('검증 (A @ x):', check.round(10))\n"
                    "print('b:           ', b)\n"
                    "print('정확?', np.allclose(check, b))"
                ),
            },
            {
                "number": 5,
                "type": "multiple_choice",
                "question": (
                    "np.random.normal(0, 1, size=1000)로 생성한 배열의 "
                    "예상 평균과 표준편차에 가장 가까운 값은?"
                ),
                "choices": [
                    "평균 ≈ 0, 표준편차 ≈ 1",
                    "평균 ≈ 0.5, 표준편차 ≈ 0.5",
                    "평균 ≈ 1, 표준편차 ≈ 0",
                    "평균 ≈ 0, 표준편차 ≈ 2",
                ],
                "answer": 0,
                "explanation": (
                    "np.random.normal(mean, std, size)의 첫 번째 인자가 평균, 두 번째가 표준편차입니다. "
                    "normal(0, 1, ...)은 표준 정규 분포(평균 0, 표준편차 1)에서 샘플링합니다. "
                    "1000개의 샘플은 이론적인 값에 근사하지만, seed 없이 실행하면 소폭 차이가 있습니다."
                ),
            },
        ],
        "challenge": {
            "question": (
                "포트폴리오 시뮬레이션 — 몬테카를로 방법\n\n"
                "주식 A, B, C 세 종목에 투자한다고 가정합니다.\n\n"
                "① np.random.seed(42) 설정\n"
                "② 각 종목의 일별 수익률을 정규 분포로 시뮬레이션\n"
                "   - A: 평균 0.001, 표준편차 0.02, 252일\n"
                "   - B: 평균 0.0005, 표준편차 0.015, 252일\n"
                "   - C: 평균 0.0015, 표준편차 0.025, 252일\n"
                "③ 세 종목을 [0.4, 0.35, 0.25] 비율로 구성한 포트폴리오 일별 수익률 계산\n"
                "④ 초기 투자금 1,000만 원으로 252일 후 최종 자산 계산 (누적 수익률 적용)\n"
                "⑤ 포트폴리오 연간 기대수익률과 변동성(표준편차 × √252) 출력"
            ),
            "hint": (
                "일별 수익률 배열 3개를 np.column_stack으로 (252, 3) 행렬로 만들고, "
                "weights = np.array([0.4, 0.35, 0.25])와 행렬 곱(@)으로 포트폴리오 수익률을 계산하세요. "
                "누적 수익률은 np.cumprod(1 + daily_returns)로 구할 수 있습니다."
            ),
        },
        "summary": [
            "reshape(-1, n)은 배열의 총 원소 수에 맞게 행 수를 자동 계산하는 편리한 방법입니다.",
            "flatten()은 복사본, ravel()은 뷰를 반환합니다. 원본을 보호하려면 flatten()을 사용하세요.",
            "np.concatenate/vstack/hstack은 기존 차원으로 결합, np.stack은 새 차원을 추가해서 쌓습니다.",
            "브로드캐스팅 3규칙: 차원 앞에 1 채우기 → 크기 1인 차원 늘리기 → 불일치 시 오류.",
            "np.random.seed()로 난수를 고정하면 실험의 재현성을 보장할 수 있습니다.",
            "행렬 곱은 @ 연산자 또는 np.dot()을 사용하며, 연립방정식은 np.linalg.solve()로 풉니다.",
        ],
    }
