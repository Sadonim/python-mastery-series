"""챕터 4: 예외 처리 — 오류를 우아하게 다루는 법."""


def get_chapter():
    """챕터 4 콘텐츠를 반환한다."""
    return {
        "number": 4,
        "title": "예외 처리",
        "subtitle": "오류를 우아하게 다루는 법",
        "big_picture": (
            "프로그램은 항상 예상대로 동작하지 않습니다. "
            "존재하지 않는 파일, 잘못된 사용자 입력, 네트워크 오류 — "
            "이런 상황을 미리 처리하지 않으면 프로그램이 갑자기 죽습니다. "
            "Python의 예외 처리 문법은 '발생할 수 있는 문제'와 "
            "'정상적인 로직'을 깔끔하게 분리해 "
            "견고하고 신뢰할 수 있는 프로그램을 만들게 해줍니다."
        ),
        "sections": [
            # ── 섹션 1: 에러 vs 예외 ──────────────────────────────
            {
                "title": "에러와 예외란 무엇인가",
                "content": [
                    "Python의 오류는 크게 두 가지입니다. "
                    "**문법 오류(SyntaxError)**는 코드 작성이 잘못된 것으로 "
                    "실행 전에 발견됩니다. "
                    "**예외(Exception)**는 실행 중에 발생하는 오류로, "
                    "프로그램이 처리할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 문법 오류 — 코드가 실행조차 되지 않음\n"
                            "# if x = 5:   ← SyntaxError: 비교는 ==, 대입은 =\n\n"
                            "# 런타임 예외 — 실행 중 발생\n"
                            "numbers = [1, 2, 3]\n"
                            "print(numbers[10])   # IndexError: list index out of range\n\n"
                            "text = '안녕하세요'\n"
                            "result = text + 5    # TypeError: str + int 불가\n\n"
                            "value = int('abc')   # ValueError: 변환 불가"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "왜 예외 처리가 필요한가",
                    },
                    {
                        "type": "analogy",
                        "text": (
                            "예외 처리는 자동차의 에어백과 같습니다. "
                            "평소에는 작동하지 않지만, 충돌(예외)이 발생했을 때 "
                            "탑승자(프로그램과 데이터)를 보호합니다. "
                            "에어백 없이 운전하면 사고 시 치명적이듯, "
                            "예외 처리 없는 코드는 오류 발생 시 바로 종료됩니다."
                        ),
                    },
                    {
                        "type": "bullet_list",
                        "items": [
                            "사용자 경험 보호: 프로그램이 갑자기 종료되는 것을 방지합니다.",
                            "데이터 안전: 파일이나 데이터베이스를 손상 없이 닫을 수 있습니다.",
                            "디버깅 용이: 오류 원인을 구체적인 메시지로 알려줍니다.",
                            "복구 가능성: 오류 상황에서도 대안적인 동작을 수행할 수 있습니다.",
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["자주 보는 예외", "발생 원인", "예시"],
                        "rows": [
                            ["ValueError", "값의 형식이나 범위가 잘못됨", "int('abc')"],
                            ["TypeError", "잘못된 타입으로 연산", "'hello' + 5"],
                            ["IndexError", "리스트 범위 초과", "list[100]"],
                            ["KeyError", "딕셔너리에 없는 키", "d['없는키']"],
                            ["FileNotFoundError", "파일이 존재하지 않음", "open('없는파일.txt')"],
                            ["ZeroDivisionError", "0으로 나눔", "10 / 0"],
                            ["AttributeError", "없는 속성·메서드 접근", "None.upper()"],
                            ["NameError", "정의되지 않은 변수 사용", "print(미정의변수)"],
                        ],
                    },
                ],
            },
            # ── 섹션 2: try / except / else / finally ────────────
            {
                "title": "try / except / else / finally 구문",
                "content": [
                    "Python의 예외 처리는 네 가지 절(clause)로 구성됩니다. "
                    "각 절은 명확한 역할을 가지고 있습니다.",
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "try 블록 실행"},
                            {"label": "예외 발생?"},
                            {"label": "except 블록 실행", "color": "#F04452"},
                            {"label": "else 블록 실행 (예외 없을 때)", "color": "#03B26C"},
                            {"label": "finally 블록 항상 실행", "color": "#3182F6"},
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 기본 구조\n"
                            "try:\n"
                            "    # 예외가 발생할 수 있는 코드\n"
                            "    result = int(input('숫자를 입력하세요: '))\n"
                            "    quotient = 100 / result\n\n"
                            "except ValueError:\n"
                            "    # 숫자가 아닌 입력 처리\n"
                            "    print('오류: 유효한 정수를 입력해 주세요.')\n\n"
                            "except ZeroDivisionError:\n"
                            "    # 0 입력 처리\n"
                            "    print('오류: 0으로 나눌 수 없습니다.')\n\n"
                            "else:\n"
                            "    # 예외가 전혀 발생하지 않았을 때만 실행\n"
                            "    print(f'결과: {quotient:.2f}')\n\n"
                            "finally:\n"
                            "    # 예외 발생 여부와 관계없이 항상 실행\n"
                            "    print('계산을 마칩니다.')"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["절", "실행 조건", "주요 용도"],
                        "rows": [
                            ["try", "항상", "예외 가능성 있는 코드"],
                            ["except", "예외 발생 시", "오류 처리, 복구"],
                            ["else", "예외 없을 때만", "성공 시 추가 작업"],
                            ["finally", "항상 (예외 유무 무관)", "정리 작업 (파일 닫기, 연결 해제)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 여러 예외를 한 번에 처리\n"
                            "def parse_age(text):\n"
                            "    \"\"\"문자열을 나이로 변환한다.\"\"\"\n"
                            "    try:\n"
                            "        age = int(text)\n"
                            "        if age < 0 or age > 150:\n"
                            "            raise ValueError(f'나이 범위 초과: {age}')\n"
                            "        return age\n"
                            "    except (ValueError, TypeError) as error:\n"
                            "        # 여러 예외를 튜플로 묶어서 처리\n"
                            "        print(f'입력 오류: {error}')\n"
                            "        return None\n\n\n"
                            "print(parse_age('25'))     # 25\n"
                            "print(parse_age('abc'))    # 입력 오류: ... → None\n"
                            "print(parse_age('-5'))     # 입력 오류: 나이 범위 초과: -5 → None\n"
                            "print(parse_age(None))     # 입력 오류: ... → None"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "`except Exception as e:` 처럼 `as` 키워드로 "
                            "예외 객체를 변수에 담을 수 있습니다. "
                            "`e.args`, `str(e)` 등으로 오류 메시지를 확인하세요."
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "`except:` (예외 타입 없이) 또는 `except Exception:` 만 쓰면 "
                            "모든 예외를 잡습니다. 너무 넓은 범위는 "
                            "Ctrl+C(KeyboardInterrupt)나 프로그램 종료 신호까지 잡아버릴 수 있습니다. "
                            "항상 구체적인 예외 타입을 명시하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 예외 계층 구조 ───────────────────────────
            {
                "title": "예외 계층 구조",
                "content": [
                    "Python의 모든 예외는 계층 구조를 이룹니다. "
                    "부모 클래스를 잡으면 자식 클래스도 함께 잡힙니다.",
                    {
                        "type": "flow_diagram",
                        "nodes": [
                            {"label": "BaseException"},
                            {"label": "Exception (일반 예외)", "color": "#3182F6"},
                            {"label": "ValueError  |  TypeError  |  OSError  |  ...", "color": "#4593FC"},
                            {"label": "FileNotFoundError (OSError의 자식)", "color": "#90C2FF"},
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["계층", "클래스", "설명"],
                        "rows": [
                            ["최상위", "BaseException", "모든 예외의 조상"],
                            ["최상위", "SystemExit", "sys.exit() 호출 시"],
                            ["최상위", "KeyboardInterrupt", "Ctrl+C 입력 시"],
                            ["일반", "Exception", "대부분의 프로그램 예외"],
                            ["값/타입", "ValueError", "값이 잘못됨"],
                            ["값/타입", "TypeError", "타입이 잘못됨"],
                            ["파일/IO", "OSError", "운영체제 관련 오류"],
                            ["파일/IO", "FileNotFoundError", "파일 없음 (OSError 자식)"],
                            ["파일/IO", "PermissionError", "권한 없음 (OSError 자식)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# except 절 순서: 구체적인 것을 먼저!\n"
                            "try:\n"
                            "    with open('data.txt') as f:\n"
                            "        content = f.read()\n\n"
                            "except FileNotFoundError:\n"
                            "    # 더 구체적인 예외를 먼저\n"
                            "    print('파일을 찾을 수 없습니다.')\n\n"
                            "except PermissionError:\n"
                            "    print('파일 읽기 권한이 없습니다.')\n\n"
                            "except OSError as e:\n"
                            "    # 나머지 OS 오류를 마지막에 처리\n"
                            "    print(f'파일 오류: {e}')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "예외 계층에서 부모를 먼저 쓰면 자식 예외가 절대 잡히지 않습니다. "
                            "항상 자식(구체적인) 예외를 먼저, 부모(포괄적인) 예외를 나중에 작성하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: raise 와 사용자 정의 예외 ────────────────
            {
                "title": "raise와 사용자 정의 예외",
                "content": [
                    "`raise` 키워드로 예외를 직접 발생시킬 수 있습니다. "
                    "그리고 Exception을 상속받아 도메인에 맞는 예외 클래스를 만들 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# raise로 예외 발생시키기\n"
                            "def set_temperature(value):\n"
                            "    \"\"\"온도를 설정한다. 유효 범위: -50 ~ 100°C\"\"\"\n"
                            "    if not isinstance(value, (int, float)):\n"
                            "        raise TypeError(f'온도는 숫자여야 합니다: {type(value)}')\n"
                            "    if value < -50 or value > 100:\n"
                            "        raise ValueError(f'온도 범위를 벗어났습니다: {value}°C')\n"
                            "    return value\n\n\n"
                            "try:\n"
                            "    set_temperature(150)\n"
                            "except ValueError as e:\n"
                            "    print(f'입력 오류: {e}')\n"
                            "# 입력 오류: 온도 범위를 벗어났습니다: 150°C"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "사용자 정의 예외 클래스",
                    },
                    "라이브러리나 큰 프로그램을 만들 때는 도메인 전용 예외를 만드는 것이 좋습니다. "
                    "예외 이름만 봐도 어떤 상황인지 즉시 알 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 예외 계층 설계\n"
                            "class BankError(Exception):\n"
                            "    \"\"\"은행 관련 예외의 기반 클래스.\"\"\"\n\n\n"
                            "class InsufficientFundsError(BankError):\n"
                            "    \"\"\"잔액 부족 예외.\"\"\"\n\n"
                            "    def __init__(self, balance, amount):\n"
                            "        self.balance = balance\n"
                            "        self.amount = amount\n"
                            "        super().__init__(\n"
                            "            f'잔액 부족: 현재 잔액 {balance:,}원, '\n"
                            "            f'출금 요청 {amount:,}원'\n"
                            "        )\n\n\n"
                            "class InvalidAmountError(BankError):\n"
                            "    \"\"\"유효하지 않은 금액 예외.\"\"\"\n\n"
                            "    def __init__(self, amount):\n"
                            "        super().__init__(f'금액은 양수여야 합니다: {amount}')\n\n\n"
                            "class BankAccount:\n"
                            "    \"\"\"간단한 은행 계좌 클래스.\"\"\"\n\n"
                            "    def __init__(self, owner, balance=0):\n"
                            "        self.owner = owner\n"
                            "        self._balance = balance\n\n"
                            "    def deposit(self, amount):\n"
                            "        \"\"\"입금한다.\"\"\"\n"
                            "        if amount <= 0:\n"
                            "            raise InvalidAmountError(amount)\n"
                            "        self._balance += amount\n"
                            "        return self._balance\n\n"
                            "    def withdraw(self, amount):\n"
                            "        \"\"\"출금한다.\"\"\"\n"
                            "        if amount <= 0:\n"
                            "            raise InvalidAmountError(amount)\n"
                            "        if amount > self._balance:\n"
                            "            raise InsufficientFundsError(self._balance, amount)\n"
                            "        self._balance -= amount\n"
                            "        return self._balance\n\n\n"
                            "account = BankAccount('김철수', 50000)\n\n"
                            "try:\n"
                            "    account.withdraw(70000)\n"
                            "except InsufficientFundsError as e:\n"
                            "    print(f'출금 실패: {e}')\n"
                            "    print(f'  부족 금액: {e.amount - e.balance:,}원')\n"
                            "except BankError as e:\n"
                            "    print(f'은행 오류: {e}')"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "사용자 정의 예외는 `Exception`을 직접 상속하거나 "
                            "도메인 기반 클래스를 통해 상속합니다. "
                            "`super().__init__(메시지)` 호출을 잊지 마세요."
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "예외 다시 발생시키기 (re-raise)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import logging\n\n\n"
                            "def process_data(data):\n"
                            "    \"\"\"데이터를 처리한다. 오류는 로그 후 재발생.\"\"\"\n"
                            "    try:\n"
                            "        result = int(data['value'])\n"
                            "        return result * 2\n"
                            "    except KeyError as e:\n"
                            "        # 로그를 남기고 예외를 다시 발생\n"
                            "        logging.error(f'필수 키가 없습니다: {e}')\n"
                            "        raise  # 원래 예외를 그대로 재발생시킴\n"
                            "    except ValueError as e:\n"
                            "        # 예외를 변환하여 다시 발생 (원인 연결)\n"
                            "        raise TypeError(f'데이터 형식 오류: {data}') from e"
                        ),
                    },
                ],
            },
            # ── 섹션 5: EAFP vs LBYL ─────────────────────────────
            {
                "title": "EAFP vs LBYL 스타일",
                "content": [
                    "예외를 처리하는 두 가지 철학이 있습니다. "
                    "Python은 **EAFP** 스타일을 선호합니다.",
                    {
                        "type": "table",
                        "headers": ["스타일", "이름", "설명", "언어"],
                        "rows": [
                            ["LBYL", "Look Before You Leap", "먼저 조건 확인 후 실행", "C, Java"],
                            ["EAFP", "Easier to Ask Forgiveness than Permission", "일단 시도 후 예외 처리", "Python"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# LBYL 스타일 (비파이썬적)\n"
                            "def get_value_lbyl(data, key):\n"
                            "    \"\"\"LBYL: 먼저 키 존재를 확인한다.\"\"\"\n"
                            "    if key in data:           # 먼저 확인\n"
                            "        value = data[key]\n"
                            "        if isinstance(value, str):    # 또 확인\n"
                            "            return value.upper()\n"
                            "    return '기본값'\n\n\n"
                            "# EAFP 스타일 (파이썬적)\n"
                            "def get_value_eafp(data, key):\n"
                            "    \"\"\"EAFP: 일단 시도하고 예외를 처리한다.\"\"\"\n"
                            "    try:\n"
                            "        return data[key].upper()\n"
                            "    except KeyError:\n"
                            "        return '기본값'\n"
                            "    except AttributeError:\n"
                            "        return '기본값'"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "EAFP는 멀티스레드 환경에서도 더 안전합니다. "
                            "LBYL에서는 '확인'과 '실행' 사이에 상태가 바뀔 수 있지만 "
                            "(Time of Check to Time of Use, TOCTOU 문제), "
                            "EAFP는 예외 자체가 원자적입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 ────────────────────────────────
            {
                "title": "실용 예제: 입력 검증과 파일 처리",
                "content": [
                    "예외 처리가 실제로 어떻게 쓰이는지 두 가지 실용 예제로 확인합니다.",
                    {
                        "type": "heading",
                        "text": "예제 1: 견고한 사용자 입력 검증",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def input_integer(prompt, min_val=None, max_val=None):\n"
                            "    \"\"\"정수를 입력받는다. 유효할 때까지 반복.\"\"\"\n"
                            "    while True:\n"
                            "        try:\n"
                            "            raw = input(prompt)\n"
                            "            value = int(raw)\n\n"
                            "            if min_val is not None and value < min_val:\n"
                            "                raise ValueError(\n"
                            "                    f'{min_val} 이상의 숫자를 입력해 주세요.'\n"
                            "                )\n"
                            "            if max_val is not None and value > max_val:\n"
                            "                raise ValueError(\n"
                            "                    f'{max_val} 이하의 숫자를 입력해 주세요.'\n"
                            "                )\n"
                            "            return value\n\n"
                            "        except ValueError as e:\n"
                            "            print(f'입력 오류: {e}')\n"
                            "            print('다시 입력해 주세요.')\n\n\n"
                            "# 사용 예\n"
                            "age = input_integer('나이를 입력하세요 (1~120): ', 1, 120)\n"
                            "score = input_integer('점수를 입력하세요 (0~100): ', 0, 100)\n"
                            "print(f'나이: {age}세, 점수: {score}점')"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "예제 2: 안전한 파일 처리",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def read_config(filepath):\n"
                            "    \"\"\"설정 파일을 읽어 딕셔너리로 반환한다.\"\"\"\n"
                            "    config = {}\n"
                            "    try:\n"
                            "        with open(filepath, encoding='utf-8') as f:\n"
                            "            for line_number, line in enumerate(f, start=1):\n"
                            "                line = line.strip()\n"
                            "                if not line or line.startswith('#'):\n"
                            "                    continue  # 빈 줄과 주석 건너뜀\n"
                            "                try:\n"
                            "                    key, value = line.split('=', 1)\n"
                            "                    config[key.strip()] = value.strip()\n"
                            "                except ValueError:\n"
                            "                    print(\n"
                            "                        f'경고: {filepath}의 {line_number}번 줄을 '\n"
                            "                        f'파싱할 수 없습니다: {line!r}'\n"
                            "                    )\n\n"
                            "    except FileNotFoundError:\n"
                            "        print(f'설정 파일을 찾을 수 없습니다: {filepath}')\n"
                            "        print('기본 설정을 사용합니다.')\n\n"
                            "    except PermissionError:\n"
                            "        print(f'파일 읽기 권한이 없습니다: {filepath}')\n\n"
                            "    return config\n\n\n"
                            "# config.txt 예시:\n"
                            "# host = localhost\n"
                            "# port = 8080\n"
                            "# debug = true\n\n"
                            "settings = read_config('config.txt')\n"
                            "print(settings.get('host', '기본호스트'))"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "중첩 try-except는 '바깥'에서 파일 오류, '안'에서 파싱 오류를 처리합니다. "
                            "각 계층이 자신이 처리할 수 있는 예외만 처리하는 것이 좋은 설계입니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "예외 타입은 항상 구체적으로 명시하세요. `except Exception:` 만 쓰는 것은 피하세요.",
            "finally는 파일·네트워크·DB 연결 등 반드시 닫아야 하는 자원 정리에 사용하세요.",
            "사용자 정의 예외 이름은 Error로 끝내는 것이 Python 관례입니다 (ValueError처럼).",
            "예외 메시지에는 무엇이 잘못됐는지와 기대값을 포함시키면 디버깅이 훨씬 쉬워집니다.",
            "EAFP 스타일을 기본으로 사용하되, 조건 검사가 더 명확한 경우엔 LBYL도 괜찮습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "다음 중 예외 발생 여부와 관계없이 항상 실행되는 절은?"
                ),
                "choices": [
                    "A) try",
                    "B) except",
                    "C) else",
                    "D) finally",
                ],
                "answer": "D",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "except 절에서 두 가지 예외를 동시에 처리하는 올바른 문법은?"
                ),
                "choices": [
                    "A) except ValueError, TypeError:",
                    "B) except (ValueError, TypeError):",
                    "C) except ValueError | TypeError:",
                    "D) except ValueError or TypeError:",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "EAFP 스타일에 대한 설명으로 가장 올바른 것은?",
                "choices": [
                    "A) 조건문으로 사전에 검사하는 방식이다",
                    "B) 일단 실행하고 예외가 발생하면 처리하는 방식이다",
                    "C) 예외를 절대 발생시키지 않는 방식이다",
                    "D) C언어 스타일의 오류 처리 방식이다",
                ],
                "answer": "B",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "문자열 리스트에서 정수로 변환 가능한 것만 골라 합계를 반환하는 "
                    "함수 `safe_sum(items)`를 작성하세요. "
                    "변환 불가능한 항목은 건너뜁니다."
                ),
                "hint": (
                    "for 루프 안에서 try-except ValueError를 사용합니다. "
                    "정수 변환 성공 시 total에 더하고, 실패 시 continue하세요."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "AgeError(ValueError의 자식)를 정의하고, "
                    "나이를 검증하는 함수 `validate_age(age)`를 만드세요. "
                    "나이가 정수가 아니면 TypeError, "
                    "0 미만이거나 150 초과이면 AgeError를 발생시킵니다."
                ),
                "hint": (
                    "class AgeError(ValueError): pass 로 간단히 정의합니다. "
                    "isinstance(age, int) 로 타입 검사하세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "숫자 맞추기 게임을 예외 처리를 활용하여 만드세요. "
                "1~100 사이 랜덤 숫자를 생성하고, "
                "사용자가 숫자를 입력할 때: "
                "정수가 아니면 '숫자를 입력해 주세요.' 메시지를 출력하고, "
                "범위를 벗어나면 '1~100 사이의 숫자를 입력해 주세요.'를 출력합니다. "
                "정답 시 시도 횟수를 출력하고, "
                "Ctrl+C 누르면 '게임을 종료합니다.' 를 출력하며 깔끔하게 종료하세요."
            ),
            "hint": (
                "import random 후 random.randint(1, 100). "
                "while True 루프 안에서 try-except를 사용합니다. "
                "KeyboardInterrupt를 except로 잡으면 Ctrl+C 처리가 가능합니다. "
                "범위 초과는 직접 raise ValueError(...)로 발생시키세요."
            ),
        },
        "summary": [
            "예외는 실행 중에 발생하는 오류로, try-except로 처리하여 프로그램이 중단되지 않게 한다.",
            "try / except / else / finally 네 절이 각각 명확한 역할을 가진다.",
            "except 절에는 구체적인 예외 타입을 명시하고, 자식 예외를 부모보다 먼저 작성한다.",
            "raise로 예외를 직접 발생시키고, Exception을 상속해 도메인 전용 예외를 만든다.",
            "Python은 EAFP(일단 시도, 예외 처리) 스타일을 선호한다.",
            "finally는 파일·연결 등 반드시 정리해야 하는 자원을 안전하게 닫는 데 사용한다.",
        ],
    }
