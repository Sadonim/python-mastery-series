"""
부록 A: Python 키워드 & 내장함수 총정리
Vol.1에서 다루는 핵심 키워드와 내장함수를 한눈에 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 A: Python 키워드 & 내장함수 총정리",
        "sections": [
            # ── 섹션 1: Python 키워드 35개 ──
            {
                "title": "A.1 Python 키워드 35개",
                "content": [
                    (
                        "키워드(keyword)는 Python이 미리 예약한 단어로, "
                        "변수명이나 함수명으로 사용할 수 없습니다. "
                        "Python 3.12 기준 35개 키워드가 있으며, "
                        "이 책에서 다루는 범위를 챕터별로 정리합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 키워드 목록 확인하기\n"
                            "import keyword\n"
                            "print(keyword.kwlist)\n"
                            "print(f'총 {len(keyword.kwlist)}개')"
                        ),
                    },
                    "**값 관련 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["True", "불리언 참", "is_valid = True", "Ch2"],
                            ["False", "불리언 거짓", "is_done = False", "Ch2"],
                            ["None", "값 없음", "result = None", "Ch2"],
                        ],
                    },
                    "**연산자 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["and", "논리 AND", "if a and b:", "Ch3"],
                            ["or", "논리 OR", "if a or b:", "Ch3"],
                            ["not", "논리 NOT", "if not done:", "Ch3"],
                            ["in", "포함 여부", "if x in my_list:", "Ch4"],
                            ["is", "동일 객체 확인", "if x is None:", "Ch3"],
                        ],
                    },
                    "**조건문 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["if", "조건 시작", "if score >= 90:", "Ch4"],
                            ["elif", "추가 조건", "elif score >= 80:", "Ch4"],
                            ["else", "나머지 조건", "else:", "Ch4"],
                        ],
                    },
                    "**반복문 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["for", "순회 반복", "for i in range(10):", "Ch4"],
                            ["while", "조건 반복", "while running:", "Ch4"],
                            ["break", "루프 탈출", "break", "Ch4"],
                            ["continue", "다음 반복으로", "continue", "Ch4"],
                            ["pass", "아무것도 안 함", "pass  # 나중에 구현", "Ch4"],
                        ],
                    },
                    "**함수 관련 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["def", "함수 정의", "def greet(name):", "Ch5"],
                            ["return", "값 반환", "return result", "Ch5"],
                            ["lambda", "익명 함수", "square = lambda x: x ** 2", "Ch5"],
                            ["global", "전역 변수 접근", "global count", "Ch5"],
                            ["nonlocal", "바깥 스코프 변수 접근", "nonlocal total", "Ch5"],
                        ],
                    },
                    "**예외처리 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["try", "예외 감시 시작", "try:", "Ch8"],
                            ["except", "예외 처리", "except ValueError:", "Ch8"],
                            ["finally", "항상 실행", "finally:", "Ch8"],
                            ["raise", "예외 발생시키기", "raise ValueError('...')", "Vol.2"],
                        ],
                    },
                    "**모듈/임포트 키워드:**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["import", "모듈 가져오기", "import math", "Ch8"],
                            ["from", "모듈에서 선택", "from math import sqrt", "Ch8"],
                            ["as", "별칭 부여", "import numpy as np", "Ch8"],
                        ],
                    },
                    "**클래스/고급 키워드 (Vol.2에서 상세 학습):**",
                    {
                        "type": "table",
                        "headers": ["키워드", "의미", "예시", "챕터"],
                        "rows": [
                            ["class", "클래스 정의", "class Dog:", "Vol.2"],
                            ["with", "컨텍스트 관리자", "with open('f') as f:", "Ch8"],
                            ["yield", "제너레이터 반환", "yield value", "Vol.2"],
                            ["del", "객체 삭제", "del my_list[0]", "Ch6"],
                            ["assert", "디버깅 검증", "assert x > 0", "Vol.2"],
                            ["async", "비동기 함수", "async def fetch():", "Vol.3"],
                            ["await", "비동기 대기", "await response", "Vol.3"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "모든 키워드를 지금 외울 필요는 없습니다. "
                            "코드를 쓰다 보면 자연스럽게 익숙해집니다. "
                            "이 표는 '이런 게 있었지?' 할 때 찾아보는 용도로 활용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 내장함수 핵심 30개 ──
            {
                "title": "A.2 내장함수 핵심 30개",
                "content": [
                    (
                        "내장함수(built-in function)는 import 없이 바로 사용할 수 있는 함수입니다. "
                        "Python에는 약 70개의 내장함수가 있으며, "
                        "그중 가장 자주 쓰는 30개를 정리합니다."
                    ),
                    "**입출력 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# print() — 화면에 출력\n"
                            'print("안녕하세요")           # 안녕하세요\n'
                            'print("a", "b", sep="-")    # a-b\n'
                            'print("끝", end="!")         # 끝!\n'
                            "\n"
                            "# input() — 사용자 입력 받기 (항상 문자열 반환)\n"
                            'name = input("이름: ")       # 사용자가 입력한 문자열'
                        ),
                    },
                    "**타입 확인 & 변환 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# type() — 타입 확인\n"
                            "type(42)           # <class 'int'>\n"
                            "type(3.14)         # <class 'float'>\n"
                            "\n"
                            "# int() — 정수로 변환\n"
                            'int("42")          # 42\n'
                            "int(3.99)          # 3 (소수점 버림)\n"
                            "\n"
                            "# float() — 실수로 변환\n"
                            'float("3.14")      # 3.14\n'
                            "float(10)          # 10.0\n"
                            "\n"
                            "# str() — 문자열로 변환\n"
                            "str(42)            # '42'\n"
                            "str(True)          # 'True'\n"
                            "\n"
                            "# bool() — 불리언 변환\n"
                            "bool(0)            # False\n"
                            'bool("")           # False\n'
                            "bool(1)            # True\n"
                            'bool("hello")      # True\n'
                            "\n"
                            "# isinstance() — 타입 확인 (True/False)\n"
                            "isinstance(42, int)         # True\n"
                            'isinstance("hi", str)       # True'
                        ),
                    },
                    "**컬렉션 생성 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# list() — 리스트 생성/변환\n"
                            'list("abc")        # ["a", "b", "c"]\n'
                            "list(range(3))     # [0, 1, 2]\n"
                            "\n"
                            "# dict() — 딕셔너리 생성\n"
                            'dict(name="철수", age=20)  # {"name": "철수", "age": 20}\n'
                            "\n"
                            "# tuple() — 튜플 생성/변환\n"
                            "tuple([1, 2, 3])   # (1, 2, 3)\n"
                            "\n"
                            "# set() — 집합 생성 (중복 제거)\n"
                            "set([1, 2, 2, 3])  # {1, 2, 3}"
                        ),
                    },
                    "**길이 & 범위 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# len() — 길이/개수\n"
                            'len("Python")      # 6\n'
                            "len([1, 2, 3])     # 3\n"
                            "\n"
                            "# range() — 정수 범위 생성\n"
                            "list(range(5))          # [0, 1, 2, 3, 4]\n"
                            "list(range(1, 6))       # [1, 2, 3, 4, 5]\n"
                            "list(range(0, 10, 2))   # [0, 2, 4, 6, 8]"
                        ),
                    },
                    "**정렬 & 순서 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# sorted() — 정렬된 새 리스트 반환 (원본 변경 없음)\n"
                            "sorted([3, 1, 2])              # [1, 2, 3]\n"
                            "sorted([3, 1, 2], reverse=True) # [3, 2, 1]\n"
                            'sorted(["b", "a", "c"])         # ["a", "b", "c"]\n'
                            "\n"
                            "# reversed() — 역순 이터레이터 반환\n"
                            "list(reversed([1, 2, 3]))  # [3, 2, 1]"
                        ),
                    },
                    "**반복 도우미 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# enumerate() — 인덱스와 값을 함께\n"
                            'fruits = ["사과", "바나나", "포도"]\n'
                            "for i, fruit in enumerate(fruits):\n"
                            '    print(f"{i}: {fruit}")   # 0: 사과, 1: 바나나 ...\n'
                            "\n"
                            "# zip() — 여러 이터러블을 묶기\n"
                            'names = ["철수", "영희"]\n'
                            "scores = [90, 85]\n"
                            "for name, score in zip(names, scores):\n"
                            '    print(f"{name}: {score}점")\n'
                            "\n"
                            "# map() — 모든 요소에 함수 적용\n"
                            'numbers = list(map(int, ["1", "2", "3"]))  # [1, 2, 3]\n'
                            "\n"
                            "# filter() — 조건에 맞는 요소만\n"
                            "evens = list(filter(lambda x: x % 2 == 0, range(10)))\n"
                            "# [0, 2, 4, 6, 8]"
                        ),
                    },
                    "**수학 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# sum() — 합계\n"
                            "sum([1, 2, 3, 4, 5])   # 15\n"
                            "\n"
                            "# max() / min() — 최댓값 / 최솟값\n"
                            "max(3, 7, 1)            # 7\n"
                            "min([10, 20, 5])        # 5\n"
                            "\n"
                            "# abs() — 절댓값\n"
                            "abs(-42)                # 42\n"
                            "\n"
                            "# round() — 반올림\n"
                            "round(3.14159, 2)       # 3.14\n"
                            "round(2.5)              # 2 (은행원 반올림)"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "round()는 '은행원 반올림(banker's rounding)'을 사용합니다. "
                            "round(0.5)는 0, round(1.5)는 2가 됩니다. "
                            "정확한 반올림이 필요하면 math 모듈이나 decimal 모듈을 사용하세요."
                        ),
                    },
                    "**파일 & 디버깅 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# open() — 파일 열기\n"
                            'with open("data.txt", "r", encoding="utf-8") as f:\n'
                            "    content = f.read()\n"
                            "\n"
                            "# id() — 객체의 고유 ID (메모리 주소)\n"
                            "a = [1, 2]\n"
                            "id(a)  # 예: 4507123456\n"
                            "\n"
                            "# dir() — 객체가 가진 속성/메서드 목록\n"
                            'dir("")  # 문자열의 모든 메서드 목록\n'
                            "\n"
                            "# help() — 도움말 출력\n"
                            "help(len)  # len 함수의 설명서"
                        ),
                    },
                    "**포매팅 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# format() — 값을 형식에 맞게 변환\n"
                            'format(1234567, ",")     # "1,234,567"\n'
                            'format(0.1234, ".2%")    # "12.34%"\n'
                            'format(42, "08b")        # "00101010" (8자리 2진수)'
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "내장함수 전체 목록은 Python 공식 문서의 "
                            "'Built-in Functions' 페이지에서 확인할 수 있습니다. "
                            "여기에 정리한 30개만 잘 익혀도 대부분의 상황을 처리할 수 있습니다."
                        ),
                    },
                    "**내장함수 요약 표:**",
                    {
                        "type": "table",
                        "headers": ["함수", "한줄 설명", "반환 타입"],
                        "rows": [
                            ["print()", "화면에 출력", "None"],
                            ["input()", "사용자 입력 받기", "str"],
                            ["len()", "길이/개수 반환", "int"],
                            ["range()", "정수 범위 생성", "range"],
                            ["type()", "타입 확인", "type"],
                            ["int()", "정수 변환", "int"],
                            ["float()", "실수 변환", "float"],
                            ["str()", "문자열 변환", "str"],
                            ["bool()", "불리언 변환", "bool"],
                            ["list()", "리스트 생성/변환", "list"],
                            ["dict()", "딕셔너리 생성", "dict"],
                            ["tuple()", "튜플 생성/변환", "tuple"],
                            ["set()", "집합 생성", "set"],
                            ["sorted()", "정렬된 리스트 반환", "list"],
                            ["reversed()", "역순 이터레이터", "iterator"],
                            ["enumerate()", "인덱스+값 쌍", "iterator"],
                            ["zip()", "여러 이터러블 묶기", "iterator"],
                            ["map()", "함수 일괄 적용", "iterator"],
                            ["filter()", "조건 필터링", "iterator"],
                            ["sum()", "합계", "number"],
                            ["max()", "최댓값", "해당 타입"],
                            ["min()", "최솟값", "해당 타입"],
                            ["abs()", "절댓값", "number"],
                            ["round()", "반올림", "number"],
                            ["open()", "파일 열기", "file object"],
                            ["isinstance()", "타입 확인", "bool"],
                            ["id()", "객체 고유 ID", "int"],
                            ["dir()", "속성/메서드 목록", "list"],
                            ["help()", "도움말 출력", "None"],
                            ["format()", "형식 지정 변환", "str"],
                        ],
                    },
                ],
            },
        ],
    }
