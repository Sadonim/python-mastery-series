"""
부록 B: OOP 디자인 패턴 입문
Python으로 배우는 4가지 핵심 디자인 패턴.
"""


def get_appendix():
    return {
        "title": "부록 B: OOP 디자인 패턴 입문",
        "sections": [
            # ── 섹션 1: 디자인 패턴이란? ──
            {
                "title": "B.1 디자인 패턴이란?",
                "content": [
                    (
                        "디자인 패턴(design pattern)은 소프트웨어 개발에서 자주 등장하는 "
                        "문제들에 대한 **검증된 해결책 템플릿**입니다. "
                        "1994년 'GoF(Gang of Four)'가 23가지 패턴을 정리한 이후 "
                        "전 세계 개발자들이 공통 언어처럼 사용하고 있습니다."
                    ),
                    {
                        "type": "analogy",
                        "text": (
                            "건축의 설계 도면과 비슷합니다. "
                            "아파트를 지을 때 매번 처음부터 설계하지 않고, "
                            "검증된 평면도 패턴(거실 중심형, 복도형 등)을 활용하듯이, "
                            "소프트웨어도 검증된 구조 패턴을 재사용합니다."
                        ),
                    },
                    "**패턴의 3가지 분류:**",
                    {
                        "type": "table",
                        "headers": ["분류", "목적", "대표 패턴"],
                        "rows": [
                            ["생성(Creational)", "객체 생성 방식 추상화", "싱글톤, 팩토리, 빌더"],
                            ["구조(Structural)", "클래스/객체 조합 방식", "어댑터, 데코레이터, 프록시"],
                            ["행동(Behavioral)", "객체 간 책임 분배", "옵저버, 전략, 커맨드"],
                        ],
                    },
                    (
                        "이 부록에서는 Python 개발에서 가장 자주 쓰이는 "
                        "싱글톤, 팩토리, 옵저버, 전략 패턴을 다룹니다. "
                        "각 패턴은 '문제 → 해결책 → 코드' 순서로 설명합니다."
                    ),
                    {
                        "type": "tip",
                        "text": (
                            "패턴을 외우려 하지 마세요. "
                            "'이럴 때 이런 구조를 쓰면 좋다'는 감각을 익히는 것이 목표입니다. "
                            "패턴 이름보다 패턴이 해결하는 문제를 먼저 이해하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 2: 싱글톤 패턴 ──
            {
                "title": "B.2 싱글톤 패턴 (Singleton)",
                "content": [
                    "**문제:** 클래스의 인스턴스가 프로그램 전체에서 단 하나만 존재해야 할 때.",
                    (
                        "예를 들어 설정(Config), 로깅(Logger), DB 연결 풀처럼 "
                        "하나의 인스턴스를 공유해야 하는 경우입니다. "
                        "여러 인스턴스가 생기면 설정이 불일치하거나 리소스 낭비가 발생합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "class AppConfig:\n"
                            '    """싱글톤 패턴 — 메타클래스 방식"""\n'
                            "    _instance = None  # 유일한 인스턴스 저장\n"
                            "\n"
                            "    def __new__(cls):\n"
                            "        if cls._instance is None:\n"
                            "            cls._instance = super().__new__(cls)\n"
                            "            # 초기 설정값 (한 번만 실행)\n"
                            "            cls._instance._settings = {\n"
                            "                'debug': False,\n"
                            "                'max_connections': 10,\n"
                            "                'language': 'ko',\n"
                            "            }\n"
                            "        return cls._instance\n"
                            "\n"
                            "    def get(self, key: str, default=None):\n"
                            "        return self._settings.get(key, default)\n"
                            "\n"
                            "    def set(self, key: str, value) -> None:\n"
                            "        self._settings[key] = value\n"
                            "\n"
                            "\n"
                            "# 어디서 생성해도 같은 인스턴스\n"
                            "config1 = AppConfig()\n"
                            "config2 = AppConfig()\n"
                            "print(config1 is config2)   # True — 동일 객체!\n"
                            "\n"
                            "config1.set('debug', True)\n"
                            "print(config2.get('debug'))  # True — 공유됨\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python에서는 모듈 자체가 싱글톤처럼 동작합니다. "
                            "설정 파일을 모듈 수준 변수로 정의하고 import하면 "
                            "별도 패턴 없이도 싱글톤 효과를 얻을 수 있습니다. "
                            "과도한 싱글톤 사용은 테스트를 어렵게 만드니 주의하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 팩토리 패턴 ──
            {
                "title": "B.3 팩토리 패턴 (Factory)",
                "content": [
                    "**문제:** 생성할 객체의 타입을 런타임에 결정해야 할 때.",
                    (
                        "예를 들어 파일 형식(JSON/CSV/XML)에 따라 다른 파서 객체를 만들어야 하는 경우, "
                        "클라이언트 코드가 직접 클래스 이름을 알지 않아도 됩니다. "
                        "팩토리 함수(또는 클래스)에 타입 정보만 전달하면 알아서 올바른 객체를 반환합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from abc import ABC, abstractmethod\n"
                            "\n"
                            "\n"
                            "# 공통 인터페이스 정의\n"
                            "class Notification(ABC):\n"
                            '    """알림 발송의 공통 인터페이스"""\n'
                            "\n"
                            "    @abstractmethod\n"
                            "    def send(self, message: str, recipient: str) -> None:\n"
                            "        ...\n"
                            "\n"
                            "\n"
                            "# 구체 구현체들\n"
                            "class EmailNotification(Notification):\n"
                            "    def send(self, message: str, recipient: str) -> None:\n"
                            "        print(f'[이메일] {recipient} → {message}')\n"
                            "\n"
                            "\n"
                            "class SMSNotification(Notification):\n"
                            "    def send(self, message: str, recipient: str) -> None:\n"
                            "        print(f'[SMS] {recipient} → {message}')\n"
                            "\n"
                            "\n"
                            "class PushNotification(Notification):\n"
                            "    def send(self, message: str, recipient: str) -> None:\n"
                            "        print(f'[푸시] {recipient} → {message}')\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 팩토리 함수 — 타입 문자열로 객체 생성\n"
                            "def create_notification(channel: str) -> Notification:\n"
                            '    """채널 이름으로 적절한 알림 객체 생성"""\n'
                            "    channels = {\n"
                            "        'email': EmailNotification,\n"
                            "        'sms': SMSNotification,\n"
                            "        'push': PushNotification,\n"
                            "    }\n"
                            "    cls = channels.get(channel.lower())\n"
                            "    if cls is None:\n"
                            "        raise ValueError(\n"
                            "            f'지원하지 않는 채널: {channel!r}\\n'\n"
                            "            f'지원 채널: {\", \".join(channels.keys())}'\n"
                            "        )\n"
                            "    return cls()\n"
                            "\n"
                            "\n"
                            "# 사용 예시\n"
                            "for channel in ['email', 'sms', 'push']:\n"
                            "    notifier = create_notification(channel)\n"
                            "    notifier.send('주문이 완료되었습니다', 'user@example.com')\n"
                            "\n"
                            "# 새 채널 추가 시: 클래스만 만들고 딕셔너리에 등록하면 끝\n"
                            "# 기존 코드를 전혀 수정하지 않아도 됨 — 개방/폐쇄 원칙(OCP)\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "팩토리 패턴의 핵심은 '어떤 클래스를 만들지'를 한 곳에서 결정한다는 것입니다. "
                            "새 타입을 추가할 때 팩토리만 수정하면 되고, "
                            "나머지 코드는 건드리지 않아도 됩니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 옵저버 패턴 ──
            {
                "title": "B.4 옵저버 패턴 (Observer)",
                "content": [
                    "**문제:** 한 객체의 상태가 바뀔 때 여러 객체에 자동으로 알려야 할 때.",
                    (
                        "예를 들어 쇼핑몰에서 재고가 들어오면 관심 등록한 모든 사용자에게 알림을 보내야 합니다. "
                        "판매자(Subject)와 구매자(Observer)는 서로를 직접 알지 않아도 되며, "
                        "느슨한 결합(loose coupling)을 유지합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from abc import ABC, abstractmethod\n"
                            "\n"
                            "\n"
                            "# 옵저버 인터페이스\n"
                            "class Observer(ABC):\n"
                            "    @abstractmethod\n"
                            "    def update(self, event: str, data: dict) -> None:\n"
                            "        ...\n"
                            "\n"
                            "\n"
                            "# 구독 관리 믹스인\n"
                            "class Observable:\n"
                            '    """옵저버 등록/해제/알림 기능 제공"""\n'
                            "\n"
                            "    def __init__(self):\n"
                            "        self._observers: list[Observer] = []\n"
                            "\n"
                            "    def subscribe(self, observer: Observer) -> None:\n"
                            "        if observer not in self._observers:\n"
                            "            self._observers.append(observer)\n"
                            "\n"
                            "    def unsubscribe(self, observer: Observer) -> None:\n"
                            "        self._observers.remove(observer)\n"
                            "\n"
                            "    def notify(self, event: str, data: dict) -> None:\n"
                            "        for observer in self._observers:\n"
                            "            observer.update(event, data)\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# Subject: 재고 관리 시스템\n"
                            "class StockManager(Observable):\n"
                            "    def __init__(self):\n"
                            "        super().__init__()\n"
                            "        self._stock: dict[str, int] = {}\n"
                            "\n"
                            "    def restock(self, product: str, quantity: int) -> None:\n"
                            "        self._stock[product] = self._stock.get(product, 0) + quantity\n"
                            "        # 재입고 시 모든 옵저버에게 알림\n"
                            "        self.notify('restock', {'product': product, 'qty': quantity})\n"
                            "\n"
                            "\n"
                            "# 구체 옵저버들\n"
                            "class EmailAlert(Observer):\n"
                            "    def __init__(self, email: str):\n"
                            "        self.email = email\n"
                            "\n"
                            "    def update(self, event: str, data: dict) -> None:\n"
                            "        if event == 'restock':\n"
                            "            print(f'[이메일 → {self.email}] '\n"
                            "                  f\"{data['product']} 재입고! ({data['qty']}개)\")\n"
                            "\n"
                            "\n"
                            "class SlackBot(Observer):\n"
                            "    def update(self, event: str, data: dict) -> None:\n"
                            "        print(f\"[슬랙] #{event}: {data['product']} \"\n"
                            "              f\"{data['qty']}개 입고됨\")\n"
                            "\n"
                            "\n"
                            "# 실행\n"
                            "manager = StockManager()\n"
                            "manager.subscribe(EmailAlert('buyer@shop.com'))\n"
                            "manager.subscribe(SlackBot())\n"
                            "\n"
                            "manager.restock('에어팟', 50)\n"
                            "# [이메일 → buyer@shop.com] 에어팟 재입고! (50개)\n"
                            "# [슬랙] #restock: 에어팟 50개 입고됨\n"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "Python의 내장 GUI 라이브러리 tkinter, "
                            "Django의 signals, SQLAlchemy의 이벤트 시스템 모두 "
                            "옵저버 패턴을 기반으로 구현되어 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 전략 패턴 ──
            {
                "title": "B.5 전략 패턴 (Strategy)",
                "content": [
                    "**문제:** 같은 작업을 다양한 방법으로 수행해야 하며, 런타임에 방법을 교체해야 할 때.",
                    (
                        "예를 들어 정렬 기준(가격순/평점순/리뷰순)을 사용자가 선택할 수 있어야 하는 경우, "
                        "if/elif 분기를 늘리는 대신 '알고리즘'을 객체로 만들어 교체합니다."
                    ),
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from abc import ABC, abstractmethod\n"
                            "from typing import Callable\n"
                            "\n"
                            "\n"
                            "# 전략 인터페이스\n"
                            "class SortStrategy(ABC):\n"
                            "    @abstractmethod\n"
                            "    def sort(self, products: list[dict]) -> list[dict]:\n"
                            "        ...\n"
                            "\n"
                            "\n"
                            "# 구체 전략들\n"
                            "class SortByPrice(SortStrategy):\n"
                            "    def sort(self, products: list[dict]) -> list[dict]:\n"
                            "        return sorted(products, key=lambda p: p['price'])\n"
                            "\n"
                            "\n"
                            "class SortByRating(SortStrategy):\n"
                            "    def sort(self, products: list[dict]) -> list[dict]:\n"
                            "        return sorted(products, key=lambda p: p['rating'], reverse=True)\n"
                            "\n"
                            "\n"
                            "class SortByReviewCount(SortStrategy):\n"
                            "    def sort(self, products: list[dict]) -> list[dict]:\n"
                            "        return sorted(products, key=lambda p: p['reviews'], reverse=True)\n"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 컨텍스트: 전략을 사용하는 쇼핑몰\n"
                            "class ProductCatalog:\n"
                            "    def __init__(self):\n"
                            "        self._products: list[dict] = []\n"
                            "        self._strategy: SortStrategy = SortByPrice()  # 기본 전략\n"
                            "\n"
                            "    def add(self, name: str, price: int, rating: float, reviews: int):\n"
                            "        self._products.append({\n"
                            "            'name': name, 'price': price,\n"
                            "            'rating': rating, 'reviews': reviews\n"
                            "        })\n"
                            "\n"
                            "    def set_sort_strategy(self, strategy: SortStrategy) -> None:\n"
                            "        # 런타임에 전략 교체 — 기존 코드 변경 없이!\n"
                            "        self._strategy = strategy\n"
                            "\n"
                            "    def get_sorted(self) -> list[dict]:\n"
                            "        return self._strategy.sort(self._products)\n"
                            "\n"
                            "\n"
                            "# 사용 예시\n"
                            "catalog = ProductCatalog()\n"
                            "catalog.add('노트북', 1_200_000, 4.5, 320)\n"
                            "catalog.add('마우스', 35_000, 4.8, 1500)\n"
                            "catalog.add('키보드', 89_000, 4.2, 780)\n"
                            "\n"
                            "catalog.set_sort_strategy(SortByPrice())\n"
                            "print('가격순:', [p['name'] for p in catalog.get_sorted()])\n"
                            "# ['마우스', '키보드', '노트북']\n"
                            "\n"
                            "catalog.set_sort_strategy(SortByRating())\n"
                            "print('평점순:', [p['name'] for p in catalog.get_sorted()])\n"
                            "# ['마우스', '노트북', '키보드']\n"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "Python에서는 클래스 대신 함수(lambda 포함)를 전략으로 전달하는 것도 가능합니다. "
                            "sorted(products, key=lambda p: p['price']) 처럼 key 함수를 바꾸는 것이 "
                            "가장 Pythonic한 전략 패턴입니다. "
                            "클래스 기반 전략은 전략이 상태(state)를 가져야 할 때 유용합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 패턴 요약 & 선택 가이드 ──
            {
                "title": "B.6 패턴 요약 & 선택 가이드",
                "content": [
                    {
                        "type": "table",
                        "headers": ["패턴", "분류", "핵심 목적", "사용 시기"],
                        "rows": [
                            [
                                "싱글톤 (Singleton)", "생성",
                                "인스턴스를 하나만 유지",
                                "설정, 로거, DB 커넥션 풀",
                            ],
                            [
                                "팩토리 (Factory)", "생성",
                                "객체 생성 로직을 한 곳에 집중",
                                "타입에 따라 다른 클래스를 생성해야 할 때",
                            ],
                            [
                                "옵저버 (Observer)", "행동",
                                "이벤트 기반 자동 알림",
                                "상태 변화를 여러 객체에 전파해야 할 때",
                            ],
                            [
                                "전략 (Strategy)", "행동",
                                "알고리즘을 런타임에 교체",
                                "같은 작업의 다양한 구현을 바꿔 써야 할 때",
                            ],
                        ],
                    },
                    "**디자인 패턴 적용 전 체크리스트:**",
                    {
                        "type": "numbered_list",
                        "items": [
                            "패턴 없이도 해결할 수 있다면 단순하게 유지하세요 (YAGNI 원칙).",
                            "코드 중복이 3회 이상 반복될 때 패턴 도입을 고려하세요 (Rule of Three).",
                            "패턴을 먼저 정하고 코드를 끼워 맞추지 마세요. 리팩토링으로 자연스럽게 등장해야 합니다.",
                            "팀원이 패턴 이름만으로 의도를 파악할 수 있으면 성공입니다.",
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "GoF 23가지 패턴 전체를 배우려면 "
                            "'파이썬으로 살펴보는 아키텍처 패턴' (코스모스, 2021) 또는 "
                            "Refactoring.Guru (https://refactoring.guru/ko/design-patterns) "
                            "사이트를 참고하세요. 모든 패턴에 Python 예제가 있습니다."
                        ),
                    },
                ],
            },
        ],
    }
