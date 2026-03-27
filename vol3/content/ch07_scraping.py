"""챕터 7: 웹 스크래핑 — 웹 페이지에서 데이터를 직접 추출하는 법."""


def get_chapter():
    """챕터 7 콘텐츠를 반환한다."""
    return {
        "number": 7,
        "title": "웹 스크래핑",
        "subtitle": "웹 페이지에서 데이터를 직접 추출하는 법",
        "big_picture": (
            "API를 제공하지 않는 웹사이트에서도 데이터를 수집할 수 있습니다. "
            "웹 스크래핑은 HTML 페이지를 다운로드하고 필요한 정보를 추출하는 기술입니다. "
            "Python의 BeautifulSoup 라이브러리는 복잡한 HTML 구조에서 "
            "원하는 데이터를 간결하게 추출할 수 있게 해줍니다. "
            "단, 스크래핑은 윤리적·법적 기준을 지키며 책임감 있게 사용해야 합니다."
        ),
        "sections": [
            # ── 섹션 1: 웹 스크래핑 기초와 윤리 ─────────────────
            {
                "title": "웹 스크래핑이란? 윤리와 법적 고려사항",
                "content": [
                    "웹 스크래핑(Web Scraping)은 웹 페이지의 HTML 코드를 다운로드하여 "
                    "필요한 데이터를 자동으로 추출하는 기술입니다. "
                    "API가 없는 사이트에서 데이터를 수집할 때 사용하지만, "
                    "반드시 규칙을 지켜야 합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "웹 스크래핑은 도서관에서 책을 읽고 필요한 정보를 노트에 옮기는 것과 같습니다. "
                            "공개된 정보를 읽는 것은 문제없지만, "
                            "도서관 규칙(robots.txt)을 무시하거나, "
                            "책을 너무 빨리 꺼내 다른 이용자를 방해하거나(서버 부하), "
                            "저작권 있는 내용을 무단으로 배포(저작권 침해)하면 안 됩니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["항목", "지켜야 할 사항", "이유"],
                        "rows": [
                            ["robots.txt 확인", "스크래핑 허용 경로만 수집", "사이트 운영자의 명시적 규칙"],
                            ["요청 속도 제한", "time.sleep(1~2초) 사용", "서버 과부하 방지"],
                            ["이용약관 확인", "스크래핑 금지 여부 확인", "법적 분쟁 예방"],
                            ["로그인 필요 페이지", "원칙적으로 스크래핑 금지", "계정 약관 위반 가능"],
                            ["개인정보", "수집·저장 금지", "개인정보보호법 위반"],
                            ["상업적 사용", "사전 허가 필요", "저작권법 위반 가능"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import urllib.robotparser\n\n\n"
                            "def can_scrape(site_url, target_url, user_agent='*'):\n"
                            "    \"\"\"robots.txt를 확인하여 스크래핑 가능 여부를 반환한다.\"\"\"\n"
                            "    rp = urllib.robotparser.RobotFileParser()\n"
                            "    rp.set_url(f'{site_url}/robots.txt')\n"
                            "    try:\n"
                            "        rp.read()\n"
                            "        return rp.can_fetch(user_agent, target_url)\n"
                            "    except Exception:\n"
                            "        return True  # robots.txt 없으면 허용으로 간주\n\n\n"
                            "# 사용 예\n"
                            "allowed = can_scrape(\n"
                            "    'https://example.com',\n"
                            "    'https://example.com/products',\n"
                            ")\n"
                            "print(f'스크래핑 허용: {allowed}')"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "스크래핑 전 반드시 robots.txt를 확인하세요. "
                            "예: https://www.google.com/robots.txt. "
                            "Disallow: / 는 전체 금지를 의미합니다. "
                            "또한 이용약관에 '자동화된 수집 금지' 조항이 있으면 "
                            "법적 책임이 발생할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: HTML 기초 구조 이해 ───────────────────────
            {
                "title": "HTML 기초 구조 이해",
                "content": [
                    "웹 스크래핑을 하려면 HTML의 기본 구조를 이해해야 합니다. "
                    "HTML은 태그(tag), 속성(attribute), 텍스트로 이루어진 계층 구조입니다.",
                    {
                        "type": "table",
                        "headers": ["개념", "설명", "예시"],
                        "rows": [
                            ["태그(tag)", "HTML 요소를 정의하는 마크업", "<h1>, <p>, <div>, <a>"],
                            ["속성(attribute)", "태그의 추가 정보", "class, id, href, src"],
                            ["텍스트(text)", "태그 안의 실제 내용", "<p>안녕하세요</p>"],
                            ["중첩(nesting)", "태그 안에 태그 포함", "<div><p>내용</p></div>"],
                            ["CSS 선택자", "요소를 선택하는 패턴", ".class, #id, tag"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# 스크래핑 대상 HTML 구조 예시\n"
                            "sample_html = \"\"\"\n"
                            "<html>\n"
                            "  <body>\n"
                            "    <div id=\"main\">\n"
                            "      <h1 class=\"title\">Python 뉴스</h1>\n"
                            "      <ul class=\"news-list\">\n"
                            "        <li class=\"news-item\">\n"
                            "          <a href=\"/news/1\" class=\"news-link\">Python 4.0 출시</a>\n"
                            "          <span class=\"date\">2026-03-27</span>\n"
                            "        </li>\n"
                            "        <li class=\"news-item\">\n"
                            "          <a href=\"/news/2\" class=\"news-link\">데이터 분석 트렌드</a>\n"
                            "          <span class=\"date\">2026-03-26</span>\n"
                            "        </li>\n"
                            "      </ul>\n"
                            "    </div>\n"
                            "  </body>\n"
                            "</html>\n"
                            "\"\"\"\n\n"
                            "# CSS 선택자 패턴\n"
                            "# div#main          → id가 main인 div\n"
                            "# .news-item        → class가 news-item인 모든 요소\n"
                            "# .news-list .news-link  → .news-list 안의 .news-link\n"
                            "# a[href]           → href 속성이 있는 a 태그\n"
                            "# li:first-child    → 첫 번째 li 요소"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "브라우저에서 스크래핑하려는 페이지를 열고 "
                            "원하는 요소에서 마우스 우클릭 → '검사'(또는 F12)를 누르면 "
                            "해당 요소의 HTML 코드와 class/id를 확인할 수 있습니다. "
                            "이를 통해 올바른 CSS 선택자를 찾아보세요."
                        ),
                    },
                ],
            },
            # ── 섹션 3: BeautifulSoup 기초 ────────────────────────
            {
                "title": "BeautifulSoup 기초: find, find_all, select",
                "content": [
                    "BeautifulSoup은 HTML/XML 파싱과 탐색을 위한 Python 라이브러리입니다. "
                    "복잡한 HTML 구조에서 원하는 요소를 직관적으로 찾을 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# pip install beautifulsoup4 requests\n"
                            "from bs4 import BeautifulSoup\n"
                            "import requests\n\n\n"
                            "# HTML 문자열에서 파싱\n"
                            "html = \"\"\"\n"
                            "<div id=\"main\">\n"
                            "  <h1 class=\"title\">Python 뉴스</h1>\n"
                            "  <p class=\"desc\">최신 Python 소식을 전합니다.</p>\n"
                            "  <ul>\n"
                            "    <li class=\"news-item\"><a href=\"/1\">기사 1</a></li>\n"
                            "    <li class=\"news-item\"><a href=\"/2\">기사 2</a></li>\n"
                            "    <li class=\"news-item\"><a href=\"/3\">기사 3</a></li>\n"
                            "  </ul>\n"
                            "</div>\n"
                            "\"\"\"\n\n"
                            "soup = BeautifulSoup(html, 'html.parser')\n\n"
                            "# find(): 조건에 맞는 첫 번째 요소 반환 (없으면 None)\n"
                            "title = soup.find('h1')              # 태그명으로 찾기\n"
                            "print(title.text)                    # Python 뉴스\n\n"
                            "main = soup.find('div', id='main')   # 태그 + id\n"
                            "desc = soup.find('p', class_='desc') # 태그 + class (class_ 사용)\n"
                            "print(desc.text)                     # 최신 Python 소식을 전합니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from bs4 import BeautifulSoup\n\n\n"
                            "html = \"\"\"\n"
                            "<ul>\n"
                            "  <li class=\"news-item\"><a href=\"/1\">기사 1</a></li>\n"
                            "  <li class=\"news-item\"><a href=\"/2\">기사 2</a></li>\n"
                            "  <li class=\"news-item\"><a href=\"/3\">기사 3</a></li>\n"
                            "</ul>\n"
                            "\"\"\"\n\n"
                            "soup = BeautifulSoup(html, 'html.parser')\n\n"
                            "# find_all(): 조건에 맞는 모든 요소를 리스트로 반환\n"
                            "items = soup.find_all('li', class_='news-item')\n"
                            "print(f'기사 수: {len(items)}')  # 3\n\n"
                            "for item in items:\n"
                            "    link = item.find('a')           # 각 li 안의 a 태그\n"
                            "    print(link.text)                # 기사 1, 기사 2, 기사 3\n"
                            "    print(link.get('href'))         # /1, /2, /3\n"
                            "    print(link['href'])             # 동일 (딕셔너리 방식)\n\n\n"
                            "# select(): CSS 선택자로 찾기 (find_all의 CSS 버전)\n"
                            "links = soup.select('li.news-item > a')  # li.news-item의 직계 a\n"
                            "hrefs = [a['href'] for a in links]\n"
                            "print(hrefs)  # ['/1', '/2', '/3']"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["메서드", "반환값", "사용 상황"],
                        "rows": [
                            ["find(tag)", "첫 번째 요소 또는 None", "단일 요소 찾을 때"],
                            ["find_all(tag)", "요소 리스트 (없으면 [])", "여러 요소 찾을 때"],
                            ["select_one(css)", "첫 번째 요소 또는 None", "CSS 선택자, 단일"],
                            ["select(css)", "요소 리스트 (없으면 [])", "CSS 선택자, 복수"],
                            [".text / .get_text()", "태그 안의 텍스트 추출", "내용을 문자열로"],
                            [".get('attr')", "속성 값 또는 None", "href, src 등 속성 추출"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "find()는 요소가 없으면 None을 반환합니다. "
                            "None에서 .text를 호출하면 AttributeError가 발생하므로, "
                            "항상 None 체크를 하거나 "
                            "`tag.get_text(strip=True) if tag else ''` 패턴을 사용하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 4: CSS 선택자와 데이터 추출 ─────────────────
            {
                "title": "CSS 선택자로 데이터 추출하기",
                "content": [
                    "CSS 선택자는 HTML 요소를 정밀하게 선택하는 강력한 문법입니다. "
                    "BeautifulSoup의 select()와 select_one() 메서드로 활용할 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["선택자", "의미", "예시"],
                        "rows": [
                            ["tag", "태그명", "div, p, a, li"],
                            [".class", "클래스", ".news-item, .title"],
                            ["#id", "아이디", "#main, #header"],
                            ["tag.class", "태그 + 클래스", "p.desc, li.active"],
                            ["parent child", "자손 선택자 (깊이 무관)", "div a, ul li"],
                            ["parent > child", "직계 자식 선택자", "ul > li, div > p"],
                            ["[attr]", "속성 존재", "a[href], img[src]"],
                            ["[attr=val]", "속성 값 일치", "a[href='/home']"],
                            ["[attr^=val]", "속성 값 시작", "a[href^='https']"],
                            [":first-child", "첫 번째 자식", "li:first-child"],
                            [":nth-child(n)", "n번째 자식", "tr:nth-child(2)"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from bs4 import BeautifulSoup\n\n\n"
                            "html = \"\"\"\n"
                            "<table class=\"data-table\">\n"
                            "  <thead>\n"
                            "    <tr><th>이름</th><th>점수</th><th>등급</th></tr>\n"
                            "  </thead>\n"
                            "  <tbody>\n"
                            "    <tr><td>김철수</td><td>92</td><td>A</td></tr>\n"
                            "    <tr><td>이영희</td><td>85</td><td>B</td></tr>\n"
                            "    <tr><td>박민수</td><td>78</td><td>C</td></tr>\n"
                            "  </tbody>\n"
                            "</table>\n"
                            "\"\"\"\n\n"
                            "soup = BeautifulSoup(html, 'html.parser')\n\n"
                            "# 헤더 추출\n"
                            "headers = [th.get_text(strip=True) for th in soup.select('thead th')]\n"
                            "print(headers)  # ['이름', '점수', '등급']\n\n"
                            "# 데이터 행 추출\n"
                            "rows = []\n"
                            "for tr in soup.select('tbody tr'):\n"
                            "    cells = tr.select('td')\n"
                            "    row = [cell.get_text(strip=True) for cell in cells]\n"
                            "    rows.append(row)\n\n"
                            "for row in rows:\n"
                            "    print(row)  # ['김철수', '92', 'A'] 등"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "from bs4 import BeautifulSoup\n\n\n"
                            "html = \"\"\"\n"
                            "<div class=\"products\">\n"
                            "  <div class=\"product\">\n"
                            "    <h3 class=\"name\">Python 입문서</h3>\n"
                            "    <span class=\"price\">25,000원</span>\n"
                            "    <a class=\"link\" href=\"/book/1\">상세보기</a>\n"
                            "  </div>\n"
                            "  <div class=\"product\">\n"
                            "    <h3 class=\"name\">데이터 분석 완전정복</h3>\n"
                            "    <span class=\"price\">32,000원</span>\n"
                            "    <a class=\"link\" href=\"/book/2\">상세보기</a>\n"
                            "  </div>\n"
                            "</div>\n"
                            "\"\"\"\n\n"
                            "soup = BeautifulSoup(html, 'html.parser')\n\n"
                            "# 각 상품 카드에서 데이터 추출\n"
                            "books = []\n"
                            "for card in soup.select('div.product'):\n"
                            "    name = card.select_one('.name')\n"
                            "    price = card.select_one('.price')\n"
                            "    link = card.select_one('a.link')\n\n"
                            "    books.append({\n"
                            "        'name': name.get_text(strip=True) if name else '',\n"
                            "        'price': price.get_text(strip=True) if price else '',\n"
                            "        'url': link.get('href', '') if link else '',\n"
                            "    })\n\n"
                            "for book in books:\n"
                            "    print(f\"{book['name']} — {book['price']} ({book['url']})\")"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "get_text(strip=True)는 태그 내부의 모든 텍스트를 합치고 "
                            "앞뒤 공백을 제거합니다. "
                            ".text는 공백을 제거하지 않으므로 "
                            "실제 스크래핑에서는 get_text(strip=True)를 사용하는 것이 좋습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: 테이블 데이터 추출과 DataFrame 변환 ───────
            {
                "title": "테이블 데이터 추출과 DataFrame 변환",
                "content": [
                    "HTML 테이블은 데이터 분석에서 자주 스크래핑하는 구조입니다. "
                    "추출한 데이터를 pandas DataFrame으로 변환하면 "
                    "즉시 분석과 저장에 활용할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# pip install pandas\n"
                            "import pandas as pd\n"
                            "from bs4 import BeautifulSoup\n\n\n"
                            "def html_table_to_df(html, table_index=0):\n"
                            "    \"\"\"HTML에서 테이블을 추출하여 DataFrame으로 반환한다.\"\"\"\n"
                            "    # pandas read_html: HTML 테이블을 자동으로 파싱\n"
                            "    tables = pd.read_html(html)\n"
                            "    if not tables:\n"
                            "        raise ValueError('HTML에서 테이블을 찾을 수 없습니다')\n"
                            "    return tables[table_index]\n\n\n"
                            "sample_html = \"\"\"\n"
                            "<table>\n"
                            "  <tr><th>이름</th><th>나이</th><th>도시</th></tr>\n"
                            "  <tr><td>김철수</td><td>25</td><td>서울</td></tr>\n"
                            "  <tr><td>이영희</td><td>23</td><td>부산</td></tr>\n"
                            "  <tr><td>박민수</td><td>27</td><td>인천</td></tr>\n"
                            "</table>\n"
                            "\"\"\"\n\n"
                            "df = html_table_to_df(sample_html)\n"
                            "print(df)\n"
                            "print(df.dtypes)"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import time\n"
                            "import pandas as pd\n"
                            "import requests\n"
                            "from bs4 import BeautifulSoup\n\n\n"
                            "def scrape_table_from_url(url, table_css='table', sleep=1.0):\n"
                            "    \"\"\"URL에서 테이블 데이터를 스크래핑하여 DataFrame으로 반환한다.\"\"\"\n"
                            "    headers = {\n"
                            "        'User-Agent': (\n"
                            "            'Mozilla/5.0 (compatible; PythonScraper/1.0; '\n"
                            "            '+https://example.com/bot)'\n"
                            "        )\n"
                            "    }\n\n"
                            "    response = requests.get(url, headers=headers, timeout=15)\n"
                            "    response.raise_for_status()\n\n"
                            "    time.sleep(sleep)  # 서버 부하 방지 — 예의 있는 스크래핑\n\n"
                            "    soup = BeautifulSoup(response.text, 'html.parser')\n"
                            "    table = soup.select_one(table_css)\n\n"
                            "    if table is None:\n"
                            "        raise ValueError(f'테이블을 찾을 수 없습니다: {table_css}')\n\n"
                            "    # 헤더 추출\n"
                            "    headers_row = table.select('th')\n"
                            "    col_names = [th.get_text(strip=True) for th in headers_row]\n\n"
                            "    # 데이터 행 추출\n"
                            "    rows = []\n"
                            "    for tr in table.select('tbody tr'):\n"
                            "        cells = [td.get_text(strip=True) for td in tr.select('td')]\n"
                            "        if cells:\n"
                            "            rows.append(cells)\n\n"
                            "    return pd.DataFrame(rows, columns=col_names if col_names else None)"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "스크래핑 시 요청 사이에 반드시 time.sleep()을 사용하세요. "
                            "짧은 간격으로 대량의 요청을 보내면 서버에 과부하를 주고, "
                            "IP 차단의 원인이 됩니다. "
                            "일반적으로 요청 사이에 1~3초의 대기 시간을 권장합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 실용 예제 ─────────────────────────────────
            {
                "title": "실용 예제: 뉴스 헤드라인과 도서 정보 수집",
                "content": [
                    "지금까지 배운 내용을 종합하여 실제 스크래핑 프로젝트를 작성합니다. "
                    "연습용 사이트인 books.toscrape.com을 사용합니다.",
                    {
                        "type": "heading",
                        "text": "예제 1: Hacker News 뉴스 헤드라인 수집",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import time\n"
                            "import requests\n"
                            "from bs4 import BeautifulSoup\n\n\n"
                            "def scrape_hn_headlines(pages=1):\n"
                            "    \"\"\"Hacker News 헤드라인을 수집한다.\"\"\"\n"
                            "    base_url = 'https://news.ycombinator.com'\n"
                            "    all_stories = []\n\n"
                            "    for page in range(1, pages + 1):\n"
                            "        url = f'{base_url}/?p={page}'\n"
                            "        response = requests.get(url, timeout=15)\n"
                            "        response.raise_for_status()\n\n"
                            "        soup = BeautifulSoup(response.text, 'html.parser')\n\n"
                            "        # 각 기사 항목 선택\n"
                            "        items = soup.select('tr.athing')\n"
                            "        for item in items:\n"
                            "            title_tag = item.select_one('.titleline > a')\n"
                            "            if not title_tag:\n"
                            "                continue\n\n"
                            "            story = {\n"
                            "                'id': item.get('id', ''),\n"
                            "                'title': title_tag.get_text(strip=True),\n"
                            "                'url': title_tag.get('href', ''),\n"
                            "            }\n"
                            "            all_stories.append(story)\n\n"
                            "        if page < pages:\n"
                            "            time.sleep(2)  # 페이지 간 대기\n\n"
                            "    return all_stories\n\n\n"
                            "# 사용 예\n"
                            "# stories = scrape_hn_headlines(pages=1)\n"
                            "# for s in stories[:5]:\n"
                            "#     print(f\"{s['title']}\")\n"
                            "#     print(f\"  → {s['url']}\")"
                        ),
                    },
                    {
                        "type": "heading",
                        "text": "예제 2: 도서 정보 스크래핑 (books.toscrape.com)",
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "import time\n"
                            "import requests\n"
                            "import pandas as pd\n"
                            "from bs4 import BeautifulSoup\n\n\n"
                            "RATING_MAP = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}\n\n\n"
                            "def scrape_books(max_pages=3):\n"
                            "    \"\"\"books.toscrape.com에서 도서 목록을 수집한다.\"\"\"\n"
                            "    # books.toscrape.com은 스크래핑 연습용으로 제공된 사이트\n"
                            "    base_url = 'https://books.toscrape.com/catalogue'\n"
                            "    url = f'{base_url}/page-1.html'\n"
                            "    all_books = []\n"
                            "    page = 1\n\n"
                            "    while url and page <= max_pages:\n"
                            "        response = requests.get(url, timeout=15)\n"
                            "        response.raise_for_status()\n\n"
                            "        soup = BeautifulSoup(response.text, 'html.parser')\n\n"
                            "        for article in soup.select('article.product_pod'):\n"
                            "            title_tag = article.select_one('h3 > a')\n"
                            "            price_tag = article.select_one('.price_color')\n"
                            "            rating_tag = article.select_one('.star-rating')\n\n"
                            "            rating_word = (\n"
                            "                rating_tag['class'][1] if rating_tag else 'One'\n"
                            "            )\n\n"
                            "            all_books.append({\n"
                            "                'title': title_tag['title'] if title_tag else '',\n"
                            "                'price': price_tag.get_text(strip=True) if price_tag else '',\n"
                            "                'rating': RATING_MAP.get(rating_word, 0),\n"
                            "            })\n\n"
                            "        # 다음 페이지 URL 탐색\n"
                            "        next_btn = soup.select_one('li.next > a')\n"
                            "        url = f'{base_url}/{next_btn[\"href\"]}' if next_btn else None\n"
                            "        page += 1\n"
                            "        if url:\n"
                            "            time.sleep(1)\n\n"
                            "    return pd.DataFrame(all_books)\n\n\n"
                            "# 사용 예\n"
                            "# df = scrape_books(max_pages=2)\n"
                            "# print(df.head())\n"
                            "# print(f'평균 평점: {df[\"rating\"].mean():.2f}')\n"
                            "# df.to_csv('books.csv', index=False, encoding='utf-8-sig')"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "스크래핑 연습에는 books.toscrape.com, quotes.toscrape.com, "
                            "toscrape.com 등 연습용으로 만들어진 사이트를 사용하세요. "
                            "실제 상업 사이트에서 연습하면 IP 차단이나 법적 문제가 생길 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "스크래핑 전 robots.txt를 반드시 확인하고 이용약관을 검토하세요.",
            "요청 사이에 time.sleep(1~2)을 추가하여 서버 부하를 방지하세요.",
            "find() 결과는 None일 수 있으므로 항상 None 체크 후 .text를 호출하세요.",
            "get_text(strip=True)로 공백이 제거된 깨끗한 텍스트를 추출하세요.",
            "pandas read_html()은 HTML 테이블을 한 줄로 DataFrame으로 변환합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": "BeautifulSoup에서 class 속성으로 요소를 찾을 때 올바른 방법은?",
                "choices": [
                    "A) soup.find('p', class='desc')",
                    "B) soup.find('p', class_='desc')",
                    "C) soup.find('p', className='desc')",
                    "D) soup.find('p').class('desc')",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": "CSS 선택자에서 특정 클래스의 직계 자식 요소를 선택하는 방법은?",
                "choices": [
                    "A) .parent .child",
                    "B) .parent + .child",
                    "C) .parent > .child",
                    "D) .parent ~ .child",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": "스크래핑 시 서버 부하를 방지하기 위한 올바른 방법은?",
                "choices": [
                    "A) 여러 스레드로 동시에 요청한다",
                    "B) requests 대신 다른 라이브러리를 사용한다",
                    "C) 요청 사이에 time.sleep()으로 대기 시간을 둔다",
                    "D) 헤더에 User-Agent를 설정하지 않는다",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "다음 HTML에서 모든 링크(a 태그)의 텍스트와 href를 "
                    "딕셔너리 리스트로 추출하는 함수 `extract_links(html)`을 작성하세요. "
                    "반환 형식: [{'text': '링크텍스트', 'href': 'URL'}, ...]"
                ),
                "hint": (
                    "soup.find_all('a') 또는 soup.select('a')로 모든 a 태그를 찾습니다. "
                    "link.get_text(strip=True)로 텍스트, link.get('href', '')로 href를 추출하세요."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "books.toscrape.com의 첫 페이지에서 "
                    "5점(Five) 평점을 받은 도서 제목만 리스트로 반환하는 "
                    "함수 `get_five_star_books()`를 작성하세요."
                ),
                "hint": (
                    "requests.get()으로 https://books.toscrape.com/catalogue/page-1.html을 가져옵니다. "
                    "soup.select('.star-rating.Five')로 5점 요소를 찾고, "
                    "각 요소의 부모(article)에서 h3 > a의 title 속성을 추출하세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "books.toscrape.com에서 여러 페이지의 도서 정보를 수집하여 분석 리포트를 생성하세요. "
                "수집 내용: 제목, 가격, 평점 (3페이지 이상). "
                "분석 내용: 1) 평점별 도서 수 집계, "
                "2) 가격 분포 (최솟값, 최댓값, 평균), "
                "3) 평점이 4점 이상인 도서 목록. "
                "결과를 books_report.json으로 저장하고, "
                "수집한 전체 데이터는 books_data.csv로 저장하세요. "
                "모든 요청 사이에 1초 이상 대기해야 합니다."
            ),
            "hint": (
                "가격 문자열에서 숫자만 추출하려면 "
                "float(price.replace('Â£', '').replace('£', ''))를 사용하세요. "
                "평점별 집계는 df['rating'].value_counts().to_dict()로 할 수 있습니다."
            ),
        },
        "summary": [
            "웹 스크래핑 전 robots.txt 확인, 이용약관 검토, 적절한 요청 간격 유지가 필수다.",
            "BeautifulSoup의 find()/find_all()은 태그명·클래스·id로, select()는 CSS 선택자로 요소를 찾는다.",
            "get_text(strip=True)로 공백 없는 깨끗한 텍스트를, get('attr')로 속성 값을 추출한다.",
            "테이블 데이터는 pandas read_html()로 한 줄에 DataFrame으로 변환할 수 있다.",
            "time.sleep()은 예의 있는 스크래핑의 핵심으로, 서버 부하와 IP 차단을 방지한다.",
        ],
    }
