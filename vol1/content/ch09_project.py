"""
Chapter 9: 미니 프로젝트 — CLI 가계부
배운 모든 것을 활용하여 실전 프로그램을 만든다.
"""


def get_chapter():
    return {
        "number": 9,
        "title": "미니 프로젝트 — CLI 가계부",
        "subtitle": "배운 모든 것을 활용하자",
        "big_picture": (
            "Chapter 1~8에서 배운 변수, 조건문, 반복문, 함수, 자료구조, "
            "문자열, 모듈을 하나의 프로그램에 모두 녹여냅니다. "
            "직접 동작하는 CLI 가계부를 단계별로 만들며, "
            "'아는 것'을 '할 수 있는 것'으로 전환하는 경험을 합니다."
        ),
        "sections": [
            # ── 섹션 1: 프로젝트 소개 & 요구사항 분석 ──
            {
                "title": "9.1 프로젝트 소개 & 요구사항 분석",
                "content": [
                    (
                        "우리가 만들 프로그램은 **CLI(Command Line Interface) 가계부**입니다. "
                        "터미널에서 실행하며, 수입과 지출을 기록하고, "
                        "잔액을 확인하고, 월별 요약까지 볼 수 있는 실용적인 도구입니다."
                    ),
                    {
                        "type": "analogy",
                        "text": (
                            "종이 가계부를 떠올려 보세요. "
                            "날짜를 쓰고, 카테고리를 적고, 금액을 기록합니다. "
                            "우리는 이 과정을 Python으로 자동화하는 것입니다."
                        ),
                    },
                    "**요구사항 정리:**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "수입/지출 기록 추가 (날짜, 카테고리, 금액, 메모)",
                            "전체 거래 목록 조회",
                            "현재 잔액 계산 및 표시",
                            "카테고리별 지출 요약",
                            "월별 필터링 조회",
                            "데이터 파일 저장/불러오기 (프로그램 종료 후에도 유지)",
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "실무에서도 프로그래밍 전에 '요구사항 정리'를 먼저 합니다. "
                            "무엇을 만들지 명확히 해야 코드가 방향을 잃지 않습니다."
                        ),
                    },
                    "**사용할 Python 개념:**",
                    {
                        "type": "table",
                        "headers": ["개념", "활용 위치"],
                        "rows": [
                            ["변수 & 타입 변환", "금액 입력 처리"],
                            ["조건문 (if/elif/else)", "메뉴 선택 분기"],
                            ["반복문 (while/for)", "메인 루프, 목록 순회"],
                            ["함수", "기능별 코드 분리"],
                            ["리스트 & 딕셔너리", "거래 데이터 저장"],
                            ["문자열 포매팅", "출력 형식 지정"],
                            ["모듈 (datetime, json)", "날짜 처리, 파일 저장"],
                        ],
                    },
                ],
            },
            # ── 섹션 2: 설계 — 데이터 구조 선택 ──
            {
                "title": "9.2 설계: 데이터 구조 선택",
                "content": [
                    (
                        "프로그램의 핵심은 **데이터를 어떻게 저장할 것인가**입니다. "
                        "가계부의 한 건의 거래를 딕셔너리로, "
                        "여러 건의 거래를 리스트로 관리합니다."
                    ),
                    "**하나의 거래 데이터 (딕셔너리):**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 거래 한 건을 딕셔너리로 표현\n"
                            "transaction = {\n"
                            '    "date": "2026-03-15",      # 날짜 (문자열)\n'
                            '    "type": "지출",             # "수입" 또는 "지출"\n'
                            '    "category": "식비",         # 카테고리\n'
                            '    "amount": 12000,            # 금액 (정수)\n'
                            '    "memo": "점심 김치찌개"      # 메모\n'
                            "}"
                        ),
                    },
                    "**전체 거래 데이터 (리스트):**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 모든 거래를 리스트에 담기\n"
                            "transactions = [\n"
                            '    {"date": "2026-03-01", "type": "수입",\n'
                            '     "category": "월급", "amount": 2000000, "memo": "3월 급여"},\n'
                            '    {"date": "2026-03-05", "type": "지출",\n'
                            '     "category": "교통", "amount": 1350, "memo": "버스"},\n'
                            '    {"date": "2026-03-05", "type": "지출",\n'
                            '     "category": "식비", "amount": 8500, "memo": "저녁"},\n'
                            "]"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "왜 딕셔너리 + 리스트 조합인가? "
                            "딕셔너리는 키로 각 항목에 의미를 부여하고, "
                            "리스트는 순서가 있는 여러 건을 담기에 최적입니다. "
                            "이 조합은 실무에서도 JSON 데이터 처리의 기본 패턴입니다."
                        ),
                    },
                    "**프로그램 전체 구조 설계:**",
                    {
                        "type": "flow_diagram",
                        "direction": "vertical",
                        "nodes": [
                            {"label": "메뉴 출력"},
                            {"label": "사용자 선택 입력"},
                            {"label": "함수 호출 (1~6)"},
                            {"label": "저장 후 종료"},
                        ],
                        "note": "while 루프로 반복: 1.수입/지출 추가 2.목록 조회 3.잔액 4.카테고리 요약 5.월별 조회 6.종료",
                    },
                ],
            },
            # ── 섹션 3: 단계 1 — 기본 구조 만들기 ──
            {
                "title": "9.3 단계 1: 기본 구조 만들기",
                "content": [
                    (
                        "먼저 프로그램의 뼈대를 세웁니다. "
                        "메인 루프와 메뉴 시스템을 만들어 프로그램이 "
                        "반복적으로 사용자 입력을 받을 수 있게 합니다."
                    ),
                    "**메뉴 출력 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def show_menu():\n"
                            '    """메뉴를 화면에 출력한다."""\n'
                            "    print()\n"
                            '    print("=" * 40)\n'
                            '    print("       나의 가계부 v1.0")\n'
                            '    print("=" * 40)\n'
                            '    print("  1. 수입/지출 추가")\n'
                            '    print("  2. 거래 목록 조회")\n'
                            '    print("  3. 잔액 확인")\n'
                            '    print("  4. 카테고리별 요약")\n'
                            '    print("  5. 월별 조회")\n'
                            '    print("  6. 저장 후 종료")\n'
                            '    print("-" * 40)'
                        ),
                    },
                    "**메인 루프:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def main():\n"
                            '    """프로그램 진입점. 메인 루프를 실행한다."""\n'
                            "    # 거래 데이터를 담을 리스트\n"
                            "    transactions = []\n"
                            "\n"
                            '    print("가계부 프로그램을 시작합니다!")\n'
                            "\n"
                            "    while True:\n"
                            "        show_menu()\n"
                            '        choice = input("메뉴 번호를 입력하세요: ").strip()\n'
                            "\n"
                            '        if choice == "1":\n'
                            "            add_transaction(transactions)\n"
                            '        elif choice == "2":\n'
                            "            show_transactions(transactions)\n"
                            '        elif choice == "3":\n'
                            "            show_balance(transactions)\n"
                            '        elif choice == "4":\n'
                            "            show_category_summary(transactions)\n"
                            '        elif choice == "5":\n'
                            "            show_monthly(transactions)\n"
                            '        elif choice == "6":\n'
                            '            save_data(transactions, "ledger.json")\n'
                            '            print("프로그램을 종료합니다. 안녕히!")\n'
                            "            break\n"
                            "        else:\n"
                            '            print("잘못된 입력입니다. 1~6 사이 숫자를 입력하세요.")\n'
                            "\n"
                            "\n"
                            '# 프로그램 실행\n'
                            'if __name__ == "__main__":\n'
                            "    main()"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "while True + break 패턴: 사용자가 종료를 선택할 때까지 "
                            "프로그램이 계속 돌아가는 구조입니다. "
                            "대부분의 CLI 프로그램이 이 패턴을 사용합니다."
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "strip()을 사용하면 사용자가 실수로 입력한 "
                            "앞뒤 공백을 제거할 수 있습니다. "
                            "입력 처리에서 항상 습관적으로 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 단계 2 — 핵심 기능 구현 ──
            {
                "title": "9.4 단계 2: 핵심 기능 구현",
                "content": [
                    "이제 각 메뉴에 연결될 핵심 함수를 하나씩 구현합니다.",
                    "**수입/지출 추가 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from datetime import date\n"
                            "\n"
                            "\n"
                            "def get_valid_amount():\n"
                            '    """양수 정수 금액을 입력받아 반환한다."""\n'
                            "    while True:\n"
                            '        raw = input("금액을 입력하세요: ").strip()\n'
                            "        if raw.isdigit() and int(raw) > 0:\n"
                            "            return int(raw)\n"
                            '        print("올바른 양수 금액을 입력해주세요.")\n'
                            "\n"
                            "\n"
                            "def add_transaction(transactions):\n"
                            '    """새 거래를 입력받아 transactions 리스트에 추가한다."""\n'
                            '    print("\\n--- 거래 추가 ---")\n'
                            "\n"
                            "    # 수입/지출 선택\n"
                            "    while True:\n"
                            '        t_type = input("유형 (수입/지출): ").strip()\n'
                            '        if t_type in ("수입", "지출"):\n'
                            "            break\n"
                            '        print("수입 또는 지출만 입력해주세요.")\n'
                            "\n"
                            "    # 카테고리 선택\n"
                            '    if t_type == "수입":\n'
                            '        categories = ["월급", "용돈", "부업", "기타"]\n'
                            "    else:\n"
                            '        categories = ["식비", "교통", "쇼핑", "문화", "기타"]\n'
                            "\n"
                            '    print("카테고리:", " / ".join(categories))\n'
                            "    while True:\n"
                            '        category = input("카테고리를 선택하세요: ").strip()\n'
                            "        if category in categories:\n"
                            "            break\n"
                            '        print(f"다음 중 선택해주세요: {categories}")\n'
                            "\n"
                            "    # 금액 입력 (검증 포함)\n"
                            "    amount = get_valid_amount()\n"
                            "\n"
                            "    # 메모 입력\n"
                            '    memo = input("메모 (선택사항, 엔터로 건너뛰기): ").strip()\n'
                            '    if not memo:\n'
                            '        memo = "없음"\n'
                            "\n"
                            "    # 거래 딕셔너리 생성\n"
                            "    transaction = {\n"
                            '        "date": str(date.today()),\n'
                            '        "type": t_type,\n'
                            '        "category": category,\n'
                            '        "amount": amount,\n'
                            '        "memo": memo,\n'
                            "    }\n"
                            "\n"
                            "    # 리스트에 추가\n"
                            "    transactions.append(transaction)\n"
                            '    print(f"\\n{t_type} {amount:,}원이 추가되었습니다!")'
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "사용자 입력은 항상 문자열입니다. "
                            "금액처럼 숫자가 필요한 곳에서는 반드시 "
                            "int() 변환과 유효성 검사를 해야 합니다."
                        ),
                    },
                    "**거래 목록 조회 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def show_transactions(transactions):\n"
                            '    """전체 거래 목록을 출력한다."""\n'
                            '    print("\\n--- 전체 거래 목록 ---")\n'
                            "\n"
                            "    if not transactions:\n"
                            '        print("기록된 거래가 없습니다.")\n'
                            "        return\n"
                            "\n"
                            "    # 헤더 출력\n"
                            '    print(f\'{"번호":>4} {"날짜":<12} {"유형":<4} '
                            '{"카테고리":<6} {"금액":>10} {"메모"}\')\n'
                            '    print("-" * 55)\n'
                            "\n"
                            "    # 각 거래 출력\n"
                            "    for i, t in enumerate(transactions, start=1):\n"
                            '        sign = "+" if t["type"] == "수입" else "-"\n'
                            "        print(\n"
                            '            f\'{i:>4} {t["date"]:<12} {t["type"]:<4} \'\n'
                            '            f\'{t["category"]:<6} \'\n'
                            '            f\'{sign}{t["amount"]:>9,}원 {t["memo"]}\'\n'
                            "        )\n"
                            "\n"
                            '    print(f"\\n총 {len(transactions)}건")'
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "enumerate(list, start=1)을 사용하면 "
                            "번호를 1부터 자동으로 매길 수 있습니다. "
                            "Ch6에서 배운 내용이 여기서 활용됩니다."
                        ),
                    },
                    "**잔액 계산 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def calculate_balance(transactions):\n"
                            '    """총 수입, 총 지출, 잔액을 계산하여 튜플로 반환한다."""\n'
                            "    total_income = 0\n"
                            "    total_expense = 0\n"
                            "\n"
                            "    for t in transactions:\n"
                            '        if t["type"] == "수입":\n'
                            '            total_income += t["amount"]\n'
                            "        else:\n"
                            '            total_expense += t["amount"]\n'
                            "\n"
                            "    balance = total_income - total_expense\n"
                            "    return total_income, total_expense, balance\n"
                            "\n"
                            "\n"
                            "def show_balance(transactions):\n"
                            '    """잔액 정보를 화면에 출력한다."""\n'
                            '    print("\\n--- 잔액 확인 ---")\n'
                            "\n"
                            "    income, expense, balance = calculate_balance(transactions)\n"
                            "\n"
                            '    print(f"총 수입:  {income:>12,}원")\n'
                            '    print(f"총 지출:  {expense:>12,}원")\n'
                            '    print("-" * 25)\n'
                            '    print(f"잔  액:  {balance:>12,}원")\n'
                            "\n"
                            "    if balance < 0:\n"
                            '        print("⚠ 지출이 수입을 초과했습니다!")'
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "calculate_balance()는 계산만 하고 "
                            "show_balance()는 출력만 합니다. "
                            "이렇게 역할을 분리하면 "
                            "나중에 계산 결과를 다른 곳에서도 재사용할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 단계 3 — 고급 기능 ──
            {
                "title": "9.5 단계 3: 고급 기능",
                "content": [
                    "기본 기능이 완성되었으니, 이제 더 유용한 기능을 추가합니다.",
                    "**카테고리별 요약 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def show_category_summary(transactions):\n"
                            '    """카테고리별 지출 합계를 출력한다."""\n'
                            '    print("\\n--- 카테고리별 지출 요약 ---")\n'
                            "\n"
                            "    # 지출 거래만 필터\n"
                            "    expenses = [\n"
                            '        t for t in transactions if t["type"] == "지출"\n'
                            "    ]\n"
                            "\n"
                            "    if not expenses:\n"
                            '        print("지출 기록이 없습니다.")\n'
                            "        return\n"
                            "\n"
                            "    # 카테고리별 합계 딕셔너리 만들기\n"
                            "    summary = {}\n"
                            "    for t in expenses:\n"
                            '        cat = t["category"]\n'
                            "        if cat in summary:\n"
                            '            summary[cat] += t["amount"]\n'
                            "        else:\n"
                            '            summary[cat] = t["amount"]\n'
                            "\n"
                            "    # 금액 큰 순서대로 정렬하여 출력\n"
                            "    total_expense = sum(summary.values())\n"
                            "\n"
                            "    for cat, amount in sorted(\n"
                            "        summary.items(), key=lambda x: x[1], reverse=True\n"
                            "    ):\n"
                            "        ratio = amount / total_expense * 100\n"
                            '        bar = "#" * int(ratio / 5)  # 간단한 막대 그래프\n'
                            '        print(f"  {cat:<6} {amount:>10,}원 ({ratio:5.1f}%) {bar}")\n'
                            "\n"
                            '    print(f"\\n  합계   {total_expense:>10,}원")'
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "리스트 컴프리헨션으로 지출만 필터링하고, "
                            "sorted()의 key 인자로 금액 순 정렬을 합니다. "
                            "Ch6에서 배운 고급 기법의 실전 활용입니다."
                        ),
                    },
                    "**월별 필터 조회 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def show_monthly(transactions):\n"
                            '    """특정 월의 거래만 필터하여 출력한다."""\n'
                            '    print("\\n--- 월별 조회 ---")\n'
                            "\n"
                            "    month_input = input(\n"
                            '        "조회할 연월을 입력하세요 (예: 2026-03): "\n'
                            "    ).strip()\n"
                            "\n"
                            "    # 입력한 연월로 시작하는 거래 필터\n"
                            "    filtered = [\n"
                            '        t for t in transactions\n'
                            '        if t["date"].startswith(month_input)\n'
                            "    ]\n"
                            "\n"
                            "    if not filtered:\n"
                            '        print(f"{month_input}에 해당하는 거래가 없습니다.")\n'
                            "        return\n"
                            "\n"
                            '    print(f"\\n{month_input} 거래 내역:")\n'
                            "    for t in filtered:\n"
                            '        sign = "+" if t["type"] == "수입" else "-"\n'
                            "        print(\n"
                            '            f\'  {t["date"]} {t["type"]} \'\n'
                            '            f\'{t["category"]} {sign}{t["amount"]:,}원\'\n'
                            "        )\n"
                            "\n"
                            "    # 해당 월 소계\n"
                            "    month_income = sum(\n"
                            '        t["amount"] for t in filtered if t["type"] == "수입"\n'
                            "    )\n"
                            "    month_expense = sum(\n"
                            '        t["amount"] for t in filtered if t["type"] == "지출"\n'
                            "    )\n"
                            '    print(f"\\n  수입: {month_income:,}원 | "\n'
                            '          f"지출: {month_expense:,}원 | "\n'
                            '          f"차액: {month_income - month_expense:,}원")'
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "startswith()는 문자열 메서드입니다. "
                            "날짜가 'YYYY-MM-DD' 형식이므로, "
                            "'2026-03'으로 시작하는지 확인하면 "
                            "해당 월의 데이터만 간단히 필터링됩니다."
                        ),
                    },
                    "**파일 저장/불러오기 함수:**",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n"
                            "\n"
                            "\n"
                            "def save_data(transactions, filename):\n"
                            '    """거래 데이터를 JSON 파일로 저장한다."""\n'
                            "    try:\n"
                            '        with open(filename, "w", encoding="utf-8") as f:\n'
                            "            json.dump(\n"
                            "                transactions, f,\n"
                            "                ensure_ascii=False, indent=2\n"
                            "            )\n"
                            '        print(f"데이터가 {filename}에 저장되었습니다. "\n'
                            '              f"({len(transactions)}건)")\n'
                            "    except IOError as e:\n"
                            '        print(f"저장 실패: {e}")\n'
                            "\n"
                            "\n"
                            "def load_data(filename):\n"
                            '    """JSON 파일에서 거래 데이터를 불러온다."""\n'
                            "    try:\n"
                            '        with open(filename, "r", encoding="utf-8") as f:\n'
                            "            data = json.load(f)\n"
                            '        print(f"{filename}에서 {len(data)}건을 불러왔습니다.")\n'
                            "        return data\n"
                            "    except FileNotFoundError:\n"
                            '        print("저장된 데이터가 없습니다. 새로 시작합니다.")\n'
                            "        return []\n"
                            "    except json.JSONDecodeError:\n"
                            '        print("파일이 손상되었습니다. 새로 시작합니다.")\n'
                            "        return []"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "파일 작업은 항상 예외가 발생할 수 있습니다. "
                            "try/except로 FileNotFoundError, "
                            "IOError, JSONDecodeError를 처리해야 "
                            "프로그램이 비정상 종료되지 않습니다."
                        ),
                    },
                    (
                        "main() 함수를 수정하여 시작 시 데이터를 불러오도록 합니다:"
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def main():\n"
                            '    """개선된 메인 함수: 시작 시 파일에서 데이터 로드."""\n'
                            '    filename = "ledger.json"\n'
                            "    transactions = load_data(filename)\n"
                            "\n"
                            '    print("가계부 프로그램을 시작합니다!")\n'
                            "\n"
                            "    while True:\n"
                            "        show_menu()\n"
                            '        choice = input("메뉴 번호를 입력하세요: ").strip()\n'
                            "\n"
                            '        if choice == "1":\n'
                            "            add_transaction(transactions)\n"
                            '        elif choice == "2":\n'
                            "            show_transactions(transactions)\n"
                            '        elif choice == "3":\n'
                            "            show_balance(transactions)\n"
                            '        elif choice == "4":\n'
                            "            show_category_summary(transactions)\n"
                            '        elif choice == "5":\n'
                            "            show_monthly(transactions)\n"
                            '        elif choice == "6":\n'
                            "            save_data(transactions, filename)\n"
                            '            print("프로그램을 종료합니다. 안녕히!")\n'
                            "            break\n"
                            "        else:\n"
                            '            print("잘못된 입력입니다. 1~6 사이를 입력하세요.")'
                        ),
                    },
                ],
            },
            # ── 섹션 6: 코드 리뷰 & 개선 포인트 ──
            {
                "title": "9.6 코드 리뷰 & 개선 포인트",
                "content": [
                    (
                        "완성된 가계부를 돌아보며, "
                        "어떤 개념을 어디서 사용했는지 정리하고, "
                        "더 개선할 수 있는 부분을 찾아봅시다."
                    ),
                    "**사용된 개념 회고:**",
                    {
                        "type": "table",
                        "headers": ["챕터", "개념", "사용 위치"],
                        "rows": [
                            ["Ch1~2", "변수, 타입 변환", "금액 입력 시 int() 변환"],
                            ["Ch3", "비교/논리 연산자", "입력 유효성 검사 조건"],
                            ["Ch4", "if/elif/else", "메뉴 분기, 수입/지출 판단"],
                            ["Ch4", "while 루프", "메인 루프, 입력 재시도"],
                            ["Ch4", "for 루프", "거래 목록 순회"],
                            ["Ch5", "함수 정의/호출", "모든 기능을 함수로 분리"],
                            ["Ch5", "매개변수/반환값", "transactions 전달, 튜플 반환"],
                            ["Ch6", "리스트/딕셔너리", "데이터 저장의 핵심 구조"],
                            ["Ch6", "리스트 컴프리헨션", "필터링 (지출만, 월별)"],
                            ["Ch7", "f-string, strip()", "출력 포매팅, 입력 정리"],
                            ["Ch7", "startswith()", "월별 날짜 필터링"],
                            ["Ch8", "import (json, datetime)", "파일 저장, 오늘 날짜"],
                        ],
                    },
                    "**리팩토링 제안 (도전 과제):**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "**상수 분리**: 카테고리 목록을 함수 밖 상수(INCOME_CATEGORIES 등)로 빼기",
                            "**입력 함수 일반화**: get_valid_choice(prompt, options)처럼 범용 입력 함수 만들기",
                            "**통계 기능 추가**: 일 평균 지출, 최대 지출 항목 찾기",
                            "**날짜 검증**: 사용자가 직접 날짜를 입력할 때 datetime.strptime()으로 검증하기",
                            "**CSV 내보내기**: json 외에 csv 모듈로 엑셀에서 열 수 있는 파일 만들기",
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "코드 리뷰의 핵심 질문: "
                            "'같은 패턴이 반복되는 곳은 없는가?' "
                            "'함수 하나가 너무 많은 일을 하고 있지 않은가?' "
                            "이 질문을 스스로에게 물어보세요."
                        ),
                    },
                    "**완성 코드 전체를 하나의 파일로 정리하면 약 120줄입니다.** "
                    "처음에는 길게 느껴질 수 있지만, "
                    "함수별로 나눠 읽으면 각 부분이 20줄 이내의 작은 단위라는 것을 알 수 있습니다.",
                    {
                        "type": "note",
                        "text": (
                            "프로그래밍은 '작은 부품을 만들어 조립하는 일'입니다. "
                            "이 프로젝트에서 경험한 것처럼, "
                            "작은 함수를 먼저 만들고 나중에 메인 루프에서 "
                            "조립하는 것이 올바른 접근법입니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "코딩 전에 반드시 요구사항을 글로 정리하세요. 코드보다 설계가 먼저입니다.",
            "한 번에 전체를 만들지 마세요. 작은 기능 하나를 완성하고 테스트한 뒤 다음으로 넘어가세요.",
            "사용자 입력은 항상 의심하세요. '숫자를 입력하세요'라고 해도 문자를 입력하는 사람이 있습니다.",
            "함수 하나는 한 가지 일만 하도록 만드세요. 이름만 보고 무슨 일을 하는지 알 수 있어야 합니다.",
            "에러 처리를 미루지 마세요. 파일 I/O, 타입 변환 등에서 try/except는 필수입니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "coding",
                "question": (
                    "가계부에 '수정' 기능을 추가하세요. "
                    "거래 번호를 입력받아 해당 거래의 금액을 수정할 수 있도록 만드세요."
                ),
                "hint": (
                    "transactions[번호-1]로 해당 딕셔너리에 접근한 후 "
                    "새 값으로 업데이트합니다. 번호 범위 검증을 잊지 마세요."
                ),
            },
            {
                "number": 2,
                "type": "coding",
                "question": (
                    "가계부에 '삭제' 기능을 추가하세요. "
                    "거래 번호를 입력받아 해당 거래를 삭제하되, "
                    "삭제 전 확인 메시지를 출력하세요."
                ),
                "hint": (
                    "del transactions[번호-1] 또는 transactions.pop(번호-1)을 사용하세요. "
                    "'정말 삭제하시겠습니까? (y/n)' 확인을 추가하세요."
                ),
            },
            {
                "number": 3,
                "type": "coding",
                "question": (
                    "카테고리별 요약에 수입 카테고리도 포함하도록 "
                    "show_category_summary() 함수를 확장하세요. "
                    "수입과 지출을 구분하여 표시하세요."
                ),
                "hint": (
                    "먼저 수입/지출을 분리한 뒤, "
                    "각각에 대해 카테고리 합계를 구하면 됩니다."
                ),
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "검색 기능을 추가하세요. "
                    "메모에 특정 단어가 포함된 거래를 찾아 출력하는 "
                    "search_transactions(transactions, keyword) 함수를 만드세요."
                ),
                "hint": (
                    "'keyword in t[\"memo\"]'로 문자열 포함 여부를 확인할 수 있습니다. "
                    "대소문자 구분 없이 검색하려면 .lower()를 사용하세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "가계부를 '예산 관리' 기능으로 확장하세요. "
                "카테고리별 월 예산을 설정하고, "
                "지출이 예산의 80%를 넘으면 경고를 표시하고, "
                "100%를 넘으면 초과 금액을 알려주세요. "
                "예산 데이터도 JSON 파일에 함께 저장하세요."
            ),
            "hint": (
                "budget = {'식비': 300000, '교통': 50000, ...} 형태의 "
                "딕셔너리를 만들고, 카테고리별 사용 금액과 비교하세요. "
                "저장 시 {'transactions': [...], 'budget': {...}} "
                "형태로 구조를 변경하세요."
            ),
        },
        "summary": [
            "CLI 가계부 프로젝트를 통해 Ch1~8의 모든 개념을 실전에 적용했습니다.",
            "요구사항 분석 → 데이터 구조 설계 → 단계별 구현 순서로 진행하는 것이 좋은 개발 습관입니다.",
            "리스트 + 딕셔너리 조합은 구조화된 데이터를 다루는 가장 기본적인 패턴입니다.",
            "사용자 입력은 반드시 유효성 검사를 거쳐야 하며, 파일 I/O에는 예외 처리가 필수입니다.",
            "함수를 작고 명확하게 만들면 코드 가독성과 유지보수성이 크게 향상됩니다.",
            "json 모듈을 사용하면 Python 자료구조를 파일로 쉽게 저장하고 불러올 수 있습니다.",
        ],
    }
