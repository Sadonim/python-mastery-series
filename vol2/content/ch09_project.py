"""
Chapter 9: 미니 프로젝트 — 주소록 관리 시스템
OOP, 파일 I/O, 예외처리를 종합하여 실전 프로그램을 만든다.
"""


def get_chapter():
    return {
        "number": 9,
        "title": "미니 프로젝트 — 주소록 관리 시스템",
        "subtitle": "Vol.2에서 배운 모든 것을 하나로",
        "big_picture": (
            "Chapter 1~8에서 배운 클래스, 상속, 파일 입출력, 예외처리, 정규식을 "
            "하나의 프로그램에 녹여냅니다. "
            "Contact 클래스로 연락처를 표현하고, AddressBook 클래스로 관리하며, "
            "JSON 파일로 데이터를 영구 저장합니다. "
            "'설계 → 구현 → 테스트'의 개발 흐름을 실전으로 익힙니다."
        ),
        "sections": [
            # ── 섹션 1: 프로젝트 소개 & 요구사항 분석 ──
            {
                "title": "9.1 프로젝트 소개 & 요구사항 분석",
                "content": [
                    (
                        "이번 프로젝트는 **CLI 주소록 관리 시스템**입니다. "
                        "스마트폰 연락처 앱을 터미널 버전으로 직접 만들어 봅니다. "
                        "이름, 전화번호, 이메일, 메모를 저장하고, "
                        "정규식 검색으로 빠르게 찾을 수 있습니다."
                    ),
                    {
                        "type": "analogy",
                        "text": (
                            "스마트폰 연락처 앱을 떠올려 보세요. "
                            "연락처를 추가하고, 이름으로 검색하고, 삭제합니다. "
                            "앱을 닫아도 연락처가 남아 있죠. "
                            "우리는 이 모든 기능을 Python으로 직접 구현합니다."
                        ),
                    },
                    "**요구사항 정리:**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "연락처 추가 (이름, 전화번호, 이메일, 메모)",
                            "전체 목록 보기 (정렬 가능)",
                            "이름 또는 전화번호로 검색 (정규식 지원)",
                            "연락처 수정",
                            "연락처 삭제",
                            "JSON 파일로 저장/불러오기 (프로그램 재실행 후에도 유지)",
                            "잘못된 입력에 대한 예외처리",
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "전체 프로그램 구조",
                        "steps": [
                            "프로그램 시작",
                            "JSON 파일 불러오기 (없으면 빈 주소록)",
                            "메인 메뉴 표시",
                            "사용자 입력 → 기능 실행 (추가/검색/수정/삭제/목록)",
                            "변경사항 자동 저장",
                            "종료 선택 시 프로그램 종료",
                        ],
                    },
                    "**사용할 Python 개념 (Vol.2 총정리):**",
                    {
                        "type": "table",
                        "headers": ["개념", "활용 위치", "챕터"],
                        "rows": [
                            ["클래스 & 인스턴스", "Contact, AddressBook 클래스", "Ch1-2"],
                            ["매직 메서드", "__str__, __repr__, __eq__", "Ch3"],
                            ["예외처리", "입력 검증, 파일 오류 처리", "Ch4"],
                            ["파일 I/O & JSON", "주소록 저장/불러오기", "Ch5"],
                            ["정규식 (re)", "이름/전화번호 검색", "Ch6"],
                            ["리스트 컴프리헨션", "검색 결과 필터링", "Ch7"],
                            ["이터레이터/제너레이터", "대용량 주소록 처리", "Ch8"],
                        ],
                    },
                ],
            },
            # ── 섹션 2: Contact 클래스 설계 ──
            {
                "title": "9.2 Contact 클래스 설계",
                "content": [
                    (
                        "주소록의 가장 기본 단위인 **연락처 하나**를 클래스로 표현합니다. "
                        "데이터(속성)와 행동(메서드)을 함께 묶는 것이 OOP의 핵심입니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import re\n"
                            "from datetime import datetime\n"
                            "\n"
                            "\n"
                            "class Contact:\n"
                            '    """연락처 하나를 표현하는 클래스"""\n'
                            "\n"
                            "    def __init__(self, name: str, phone: str,\n"
                            "                 email: str = '', memo: str = ''):\n"
                            '        """연락처 초기화 — 이름과 전화번호는 필수"""\n'
                            "        # 입력값 검증\n"
                            "        if not name.strip():\n"
                            "            raise ValueError('이름은 비워 둘 수 없습니다.')\n"
                            "        if not self._is_valid_phone(phone):\n"
                            "            raise ValueError(\n"
                            "                f'올바른 전화번호 형식이 아닙니다: {phone}\\n'\n"
                            "                '예시) 010-1234-5678 또는 0101234567'\n"
                            "            )\n"
                            "\n"
                            "        self.name = name.strip()\n"
                            "        self.phone = phone.strip()\n"
                            "        self.email = email.strip()\n"
                            "        self.memo = memo.strip()\n"
                            "        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M')\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "    @staticmethod\n"
                            "    def _is_valid_phone(phone: str) -> bool:\n"
                            '        """전화번호 형식 검사 — 정규식 활용"""\n'
                            "        # 010-1234-5678 또는 01012345678 형식 허용\n"
                            "        pattern = r'^0\\d{1,2}[-\\s]?\\d{3,4}[-\\s]?\\d{4}$'\n"
                            "        return bool(re.match(pattern, phone.strip()))\n"
                            "\n"
                            "    def __str__(self) -> str:\n"
                            '        """사용자 친화적 출력"""\n'
                            "        lines = [\n"
                            "            f'이름: {self.name}',\n"
                            "            f'전화: {self.phone}',\n"
                            "        ]\n"
                            "        if self.email:\n"
                            "            lines.append(f'이메일: {self.email}')\n"
                            "        if self.memo:\n"
                            "            lines.append(f'메모: {self.memo}')\n"
                            "        return '\\n'.join(lines)\n"
                            "\n"
                            "    def __repr__(self) -> str:\n"
                            '        """개발자용 출력 — 디버깅에 활용"""\n'
                            "        return (\n"
                            "            f'Contact(name={self.name!r}, '\n"
                            "            f'phone={self.phone!r}, '\n"
                            "            f'email={self.email!r})'\n"
                            "        )\n"
                            "\n"
                            "    def __eq__(self, other: object) -> bool:\n"
                            '        """전화번호가 같으면 동일 연락처로 판단"""\n'
                            "        if not isinstance(other, Contact):\n"
                            "            return NotImplemented\n"
                            "        return self.phone == other.phone\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "    def to_dict(self) -> dict:\n"
                            '        """JSON 저장을 위해 딕셔너리로 변환"""\n'
                            "        return {\n"
                            "            'name': self.name,\n"
                            "            'phone': self.phone,\n"
                            "            'email': self.email,\n"
                            "            'memo': self.memo,\n"
                            "            'created_at': self.created_at,\n"
                            "        }\n"
                            "\n"
                            "    @classmethod\n"
                            "    def from_dict(cls, data: dict) -> 'Contact':\n"
                            '        """딕셔너리에서 Contact 객체 복원"""\n'
                            "        contact = cls(\n"
                            "            name=data['name'],\n"
                            "            phone=data['phone'],\n"
                            "            email=data.get('email', ''),\n"
                            "            memo=data.get('memo', ''),\n"
                            "        )\n"
                            "        # 저장된 생성 시각 복원\n"
                            "        contact.created_at = data.get('created_at', contact.created_at)\n"
                            "        return contact\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "to_dict()와 from_dict()는 객체를 직렬화(serialize)/역직렬화(deserialize)하는 "
                            "패턴입니다. JSON, DB 저장 모두 이 패턴을 사용합니다. "
                            "실무에서 매우 자주 쓰이니 꼭 익혀 두세요."
                        ),
                    },
                ],
            },
            # ── 섹션 3: AddressBook 클래스 ──
            {
                "title": "9.3 AddressBook 클래스",
                "content": [
                    (
                        "여러 Contact를 관리하는 **컨테이너 클래스**를 만듭니다. "
                        "추가, 검색, 수정, 삭제, 저장/불러오기 기능을 모두 담습니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import json\n"
                            "import re\n"
                            "from pathlib import Path\n"
                            "\n"
                            "\n"
                            "class AddressBook:\n"
                            '    """주소록 전체를 관리하는 클래스"""\n'
                            "\n"
                            "    DEFAULT_FILE = 'addressbook.json'\n"
                            "\n"
                            "    def __init__(self, filepath: str = DEFAULT_FILE):\n"
                            "        self.filepath = Path(filepath)\n"
                            "        self._contacts: list[Contact] = []\n"
                            "        self.load()  # 파일에서 자동 불러오기\n"
                            "\n"
                            "    def add(self, contact: Contact) -> None:\n"
                            '        """연락처 추가 — 중복 전화번호 방지"""\n'
                            "        if contact in self._contacts:\n"
                            "            raise ValueError(\n"
                            "                f'이미 등록된 전화번호입니다: {contact.phone}'\n"
                            "            )\n"
                            "        self._contacts.append(contact)\n"
                            "        self.save()\n"
                            "        print(f'✓ {contact.name} 님이 추가되었습니다.')\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "    def search(self, query: str) -> list[Contact]:\n"
                            '        """이름 또는 전화번호로 검색 (정규식 지원)"""\n'
                            "        try:\n"
                            "            pattern = re.compile(query, re.IGNORECASE)\n"
                            "        except re.error:\n"
                            "            # 정규식이 아닌 일반 문자열로 처리\n"
                            "            pattern = re.compile(re.escape(query), re.IGNORECASE)\n"
                            "\n"
                            "        results = [\n"
                            "            c for c in self._contacts\n"
                            "            if pattern.search(c.name) or pattern.search(c.phone)\n"
                            "        ]\n"
                            "        return results\n"
                            "\n"
                            "    def update(self, phone: str, **kwargs) -> bool:\n"
                            '        """전화번호로 연락처를 찾아 수정"""\n'
                            "        contact = self._find_by_phone(phone)\n"
                            "        if contact is None:\n"
                            "            return False\n"
                            "\n"
                            "        # 허용된 필드만 수정\n"
                            "        allowed = {'name', 'phone', 'email', 'memo'}\n"
                            "        for key, value in kwargs.items():\n"
                            "            if key in allowed:\n"
                            "                setattr(contact, key, value.strip())\n"
                            "\n"
                            "        self.save()\n"
                            "        return True\n"
                            "\n"
                            "    def delete(self, phone: str) -> bool:\n"
                            '        """전화번호로 연락처 삭제"""\n'
                            "        contact = self._find_by_phone(phone)\n"
                            "        if contact is None:\n"
                            "            return False\n"
                            "        self._contacts.remove(contact)\n"
                            "        self.save()\n"
                            "        return True\n"
                            "\n"
                            "    def list_all(self, sort_by: str = 'name') -> list[Contact]:\n"
                            '        """전체 목록 반환 — 이름순 정렬 기본"""\n'
                            "        return sorted(self._contacts, key=lambda c: getattr(c, sort_by))\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "    def _find_by_phone(self, phone: str) -> Contact | None:\n"
                            '        """내부용: 전화번호로 연락처 조회"""\n'
                            "        for contact in self._contacts:\n"
                            "            if contact.phone == phone.strip():\n"
                            "                return contact\n"
                            "        return None\n"
                            "\n"
                            "    def save(self) -> None:\n"
                            '        """JSON 파일로 저장"""\n'
                            "        try:\n"
                            "            data = [c.to_dict() for c in self._contacts]\n"
                            "            with open(self.filepath, 'w', encoding='utf-8') as f:\n"
                            "                json.dump(data, f, ensure_ascii=False, indent=2)\n"
                            "        except OSError as e:\n"
                            "            print(f'[경고] 저장 실패: {e}')\n"
                            "\n"
                            "    def load(self) -> None:\n"
                            '        """JSON 파일에서 불러오기"""\n'
                            "        if not self.filepath.exists():\n"
                            "            return  # 파일 없으면 빈 주소록으로 시작\n"
                            "        try:\n"
                            "            with open(self.filepath, 'r', encoding='utf-8') as f:\n"
                            "                data = json.load(f)\n"
                            "            self._contacts = [Contact.from_dict(d) for d in data]\n"
                            "        except (json.JSONDecodeError, KeyError) as e:\n"
                            "            print(f'[경고] 파일 불러오기 실패 ({e}). 빈 주소록으로 시작합니다.')\n"
                            "            self._contacts = []\n"
                            "\n"
                            "    def __len__(self) -> int:\n"
                            "        return len(self._contacts)\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "save()를 add(), update(), delete() 안에서 자동 호출합니다. "
                            "사용자가 명시적으로 저장하지 않아도 변경사항이 항상 파일에 반영됩니다. "
                            "이런 설계를 '자동 영속성(auto-persistence)'이라고 합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: CLI 인터페이스 ──
            {
                "title": "9.4 CLI 인터페이스 구현",
                "content": [
                    (
                        "사용자가 프로그램과 대화하는 **메뉴 기반 인터페이스**를 만듭니다. "
                        "while 루프로 메뉴를 반복 표시하고, "
                        "사용자 입력에 따라 적절한 기능을 호출합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def print_menu() -> None:\n"
                            '    """메인 메뉴 출력"""\n'
                            "    print('\\n' + '='*40)\n"
                            "    print('     📒 주소록 관리 시스템')\n"
                            "    print('='*40)\n"
                            "    print('1. 연락처 추가')\n"
                            "    print('2. 전체 목록 보기')\n"
                            "    print('3. 연락처 검색')\n"
                            "    print('4. 연락처 수정')\n"
                            "    print('5. 연락처 삭제')\n"
                            "    print('0. 종료')\n"
                            "    print('-'*40)\n"
                            "\n"
                            "\n"
                            "def input_contact() -> Contact:\n"
                            '    """사용자로부터 연락처 정보 입력받기"""\n'
                            "    print('\\n[연락처 추가]')\n"
                            "    while True:\n"
                            "        try:\n"
                            "            name = input('이름 (필수): ').strip()\n"
                            "            phone = input('전화번호 (필수, 예: 010-1234-5678): ').strip()\n"
                            "            email = input('이메일 (선택, Enter 건너뜀): ').strip()\n"
                            "            memo = input('메모 (선택, Enter 건너뜀): ').strip()\n"
                            "            return Contact(name, phone, email, memo)\n"
                            "        except ValueError as e:\n"
                            "            print(f'입력 오류: {e}')\n"
                            "            retry = input('다시 입력하시겠습니까? (y/n): ')\n"
                            "            if retry.lower() != 'y':\n"
                            "                raise  # 취소: 상위로 예외 전달\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def display_contacts(contacts: list[Contact]) -> None:\n"
                            '    """연락처 목록 출력"""\n'
                            "    if not contacts:\n"
                            "        print('표시할 연락처가 없습니다.')\n"
                            "        return\n"
                            "    print(f'\\n총 {len(contacts)}명')\n"
                            "    print('-'*50)\n"
                            "    for i, c in enumerate(contacts, 1):\n"
                            "        print(f'{i:3}. {c.name:<12} {c.phone:<15} {c.email}')\n"
                            "    print('-'*50)\n"
                            "\n"
                            "\n"
                            "def run_search(book: AddressBook) -> None:\n"
                            '    """검색 기능 실행"""\n'
                            "    query = input('\\n검색어 (이름 또는 전화번호): ').strip()\n"
                            "    if not query:\n"
                            "        print('검색어를 입력해 주세요.')\n"
                            "        return\n"
                            "    results = book.search(query)\n"
                            "    if results:\n"
                            "        print(f'검색 결과: {len(results)}건')\n"
                            "        display_contacts(results)\n"
                            "        # 검색 결과에서 상세 정보 선택 보기\n"
                            "        choice = input('상세 보기 (번호 입력, Enter 건너뜀): ').strip()\n"
                            "        if choice.isdigit():\n"
                            "            idx = int(choice) - 1\n"
                            "            if 0 <= idx < len(results):\n"
                            "                print(f'\\n{results[idx]}')\n"
                            "    else:\n"
                            "        print(f'검색 결과가 없습니다: {query!r}')\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def run_update(book: AddressBook) -> None:\n"
                            '    """수정 기능 실행"""\n'
                            "    phone = input('\\n수정할 연락처 전화번호: ').strip()\n"
                            "    print('변경할 항목만 입력하세요. 변경 없으면 Enter를 누르세요.')\n"
                            "    new_name = input('새 이름: ').strip()\n"
                            "    new_email = input('새 이메일: ').strip()\n"
                            "    new_memo = input('새 메모: ').strip()\n"
                            "\n"
                            "    kwargs = {}\n"
                            "    if new_name:\n"
                            "        kwargs['name'] = new_name\n"
                            "    if new_email:\n"
                            "        kwargs['email'] = new_email\n"
                            "    if new_memo:\n"
                            "        kwargs['memo'] = new_memo\n"
                            "\n"
                            "    if not kwargs:\n"
                            "        print('변경된 내용이 없습니다.')\n"
                            "        return\n"
                            "\n"
                            "    if book.update(phone, **kwargs):\n"
                            "        print('✓ 수정이 완료되었습니다.')\n"
                            "    else:\n"
                            "        print(f'전화번호를 찾을 수 없습니다: {phone}')\n"
                        ),
                    },
                ],
            },
            # ── 섹션 5: 메인 루프 & 전체 실행 ──
            {
                "title": "9.5 메인 루프 & 전체 실행",
                "content": [
                    (
                        "모든 기능을 하나로 묶는 **메인 루프**입니다. "
                        "프로그램의 진입점(entry point)으로, "
                        "AddressBook을 생성하고 메뉴를 반복 실행합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "def main() -> None:\n"
                            '    """주소록 프로그램 진입점"""\n'
                            "    book = AddressBook()  # 자동으로 JSON 파일 불러오기\n"
                            "    print(f'주소록을 불러왔습니다. (총 {len(book)}명)')\n"
                            "\n"
                            "    while True:\n"
                            "        print_menu()\n"
                            "        choice = input('메뉴를 선택하세요: ').strip()\n"
                            "\n"
                            "        try:\n"
                            "            if choice == '1':      # 추가\n"
                            "                contact = input_contact()\n"
                            "                book.add(contact)\n"
                            "\n"
                            "            elif choice == '2':    # 목록\n"
                            "                contacts = book.list_all()\n"
                            "                display_contacts(contacts)\n"
                            "\n"
                            "            elif choice == '3':    # 검색\n"
                            "                run_search(book)\n"
                            "\n"
                            "            elif choice == '4':    # 수정\n"
                            "                run_update(book)\n"
                            "\n"
                            "            elif choice == '5':    # 삭제\n"
                            "                phone = input('삭제할 연락처 전화번호: ').strip()\n"
                            "                confirm = input(f'{phone} 을(를) 삭제할까요? (y/n): ')\n"
                            "                if confirm.lower() == 'y':\n"
                            "                    if book.delete(phone):\n"
                            "                        print('✓ 삭제되었습니다.')\n"
                            "                    else:\n"
                            "                        print('전화번호를 찾을 수 없습니다.')\n"
                            "\n"
                            "            elif choice == '0':    # 종료\n"
                            "                print('주소록을 종료합니다. 안녕히 계세요!')\n"
                            "                break\n"
                            "\n"
                            "            else:\n"
                            "                print('올바른 메뉴 번호를 입력해 주세요 (0~5).')\n"
                            "\n"
                            "        except ValueError as e:\n"
                            "            print(f'오류: {e}')\n"
                            "        except KeyboardInterrupt:\n"
                            "            print('\\n\\n강제 종료됩니다.')\n"
                            "            break\n"
                            "\n"
                            "\n"
                            "if __name__ == '__main__':\n"
                            "    main()\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "if __name__ == '__main__': 구문은 이 파일을 직접 실행할 때만 main()을 호출합니다. "
                            "다른 파일에서 import할 때는 main()이 자동 실행되지 않습니다. "
                            "모든 Python 실행 파일에 이 패턴을 사용하세요."
                        ),
                    },
                    "**전체 파일 구조:**",
                    {
                        "type": "table",
                        "headers": ["파일", "역할"],
                        "rows": [
                            ["contact.py", "Contact 클래스 정의"],
                            ["addressbook.py", "AddressBook 클래스 정의"],
                            ["cli.py", "CLI 인터페이스 함수들"],
                            ["main.py", "프로그램 진입점 (main 함수)"],
                            ["addressbook.json", "데이터 저장 파일 (자동 생성)"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "소규모 프로젝트는 파일 하나에 모두 넣어도 됩니다. "
                            "하지만 코드가 커지면 위 구조처럼 기능별로 파일을 분리하세요. "
                            "파일 하나는 300~400줄을 넘지 않는 것이 이상적입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 개선 & 확장 아이디어 ──
            {
                "title": "9.6 개선 & 확장 아이디어",
                "content": [
                    (
                        "기본 프로그램이 완성되면 다양한 방향으로 확장할 수 있습니다. "
                        "실력을 늘리기 위한 도전 과제들을 살펴봅니다."
                    ),
                    {
                        "type": "table",
                        "headers": ["난이도", "개선 아이디어", "필요 개념"],
                        "rows": [
                            ["★☆☆", "그룹(태그) 기능 추가", "리스트, 문자열"],
                            ["★☆☆", "이메일 형식 유효성 검사", "정규식"],
                            ["★★☆", "CSV 파일 내보내기/가져오기", "csv 모듈"],
                            ["★★☆", "생일 필드 추가 & D-day 계산", "datetime"],
                            ["★★★", "즐겨찾기 기능 (상위 표시)", "정렬 키"],
                            ["★★★", "중복 연락처 병합 기능", "비교 로직"],
                            ["★★★", "GUI 버전으로 변환", "tkinter 또는 PyQt"],
                        ],
                    },
                    "**코드 품질 개선 포인트:**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "Contact를 dataclass로 전환 — 보일러플레이트 코드 제거",
                            "타입 힌트 완성 — 모든 함수에 매개변수/반환 타입 명시",
                            "단위 테스트 작성 — pytest로 각 메서드 검증",
                            "로깅(logging) 추가 — print 대신 log 레벨 활용",
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 개선 예시: dataclass로 Contact 재작성\n"
                            "from dataclasses import dataclass, field, asdict\n"
                            "from datetime import datetime\n"
                            "\n"
                            "\n"
                            "@dataclass\n"
                            "class Contact:\n"
                            "    name: str\n"
                            "    phone: str\n"
                            "    email: str = ''\n"
                            "    memo: str = ''\n"
                            "    created_at: str = field(\n"
                            "        default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M')\n"
                            "    )\n"
                            "\n"
                            "    def to_dict(self) -> dict:\n"
                            "        return asdict(self)  # dataclass 전용 변환 함수\n"
                            "\n"
                            "    # __eq__, __repr__ 등은 dataclass가 자동 생성\n"
                            "    # frozen=True로 설정하면 불변 객체가 됨\n"
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "작동하는 코드를 먼저 만들고, 그 다음에 개선하세요. '완벽한 설계'를 기다리다 시작도 못하는 것이 더 나쁩니다.",
            "클래스 하나가 너무 많은 일을 하면 분리하세요. Contact는 데이터 표현, AddressBook은 관리, main은 UI — 각자 역할이 명확합니다.",
            "예외처리는 사용자의 잘못된 입력을 위한 것이지, 버그를 숨기기 위한 것이 아닙니다. 예외 메시지는 구체적으로 작성하세요.",
            "JSON은 사람이 읽을 수 있는 파일 형식입니다. indent=2 옵션으로 저장하면 텍스트 편집기로도 열어볼 수 있습니다.",
            "정규식 검색은 강력하지만 사용자가 잘못된 패턴을 입력할 수 있습니다. 항상 re.error 예외를 처리하세요.",
        ],
        "exercises": [
            {
                "number": 1,
                "title": "이메일 유효성 검사 추가",
                "description": (
                    "Contact._is_valid_phone()처럼 _is_valid_email() 정적 메서드를 작성하세요. "
                    "이메일에 @가 포함되고, 도메인 부분에 .이 있으면 유효한 것으로 판단합니다."
                ),
                "hint": "정규식 패턴: r'^[\\w.+-]+@[\\w-]+\\.[\\w.-]+$'",
            },
            {
                "number": 2,
                "title": "이름순/날짜순 정렬 선택",
                "description": (
                    "list_all() 호출 시 사용자가 '이름순' 또는 '등록일순'을 선택할 수 있도록 "
                    "CLI 인터페이스를 수정하세요."
                ),
                "hint": "sort_by 매개변수에 'name' 또는 'created_at'을 전달하면 됩니다.",
            },
            {
                "number": 3,
                "title": "즐겨찾기 기능",
                "description": (
                    "Contact에 favorite: bool = False 속성을 추가하고, "
                    "즐겨찾기 연락처를 목록 상단에 표시하는 기능을 구현하세요."
                ),
                "hint": "list_all()에서 sorted() 정렬 키를 lambda c: (not c.favorite, c.name)으로 설정하세요.",
            },
            {
                "number": 4,
                "title": "CSV 내보내기",
                "description": (
                    "AddressBook에 export_csv(filename) 메서드를 추가하세요. "
                    "Python 내장 csv 모듈을 사용하여 전체 연락처를 CSV 파일로 저장합니다."
                ),
                "hint": "import csv 후 csv.DictWriter를 사용하면 딕셔너리를 바로 CSV로 쓸 수 있습니다.",
            },
            {
                "number": 5,
                "title": "연락처 개수 표시 개선",
                "description": (
                    "AddressBook에 __str__을 구현하여 "
                    "'주소록: 12명 (즐겨찾기: 3명)'과 같은 요약 문자열을 반환하게 하세요."
                ),
                "hint": "len()은 __len__으로 구현되어 있습니다. __str__에서 self._contacts를 순회하세요.",
            },
        ],
        "challenge": {
            "question": (
                "AddressBook을 상속받아 BusinessBook 클래스를 만들어 보세요. "
                "BusinessBook은 Contact에 '회사명'과 '직책' 필드가 추가된 "
                "BusinessContact를 저장합니다. "
                "일반 연락처와 비즈니스 연락처를 함께 관리할 수 있어야 합니다."
            ),
            "hint": (
                "BusinessContact(Contact)로 Contact를 상속받고, "
                "추가 필드를 __init__에서 정의하세요. "
                "AddressBook의 add() 메서드는 Contact 또는 BusinessContact 모두 받을 수 있습니다 "
                "(파이썬의 다형성 덕분에). to_dict()와 from_dict()도 오버라이드하세요."
            ),
        },
        "summary": [
            "Contact 클래스는 연락처 하나를 표현하며, 검증(validation)을 __init__에서 수행합니다.",
            "AddressBook 클래스는 Contact 목록을 관리하고, JSON 파일로 자동 저장/불러오기를 합니다.",
            "정규식(re 모듈)으로 이름·전화번호 검색 기능을 구현하며, 잘못된 패턴 입력도 안전하게 처리합니다.",
            "CLI 인터페이스는 while 루프 + try/except 조합으로 안정적인 메뉴 기반 대화를 구현합니다.",
            "to_dict() / from_dict() 패턴은 객체를 JSON으로 직렬화/역직렬화하는 표준적인 방법입니다.",
        ],
    }
