"""챕터 6: Docker 컨테이너 — 어디서나 동일하게 실행되는 앱 만들기."""


def get_chapter():
    """챕터 6 콘텐츠를 반환한다."""
    return {
        "number": 6,
        "title": "Docker 컨테이너",
        "subtitle": "어디서나 동일하게 실행되는 앱 만들기",
        "big_picture": (
            "\"내 컴퓨터에서는 잘 되는데...\" — 개발자라면 누구나 한 번씩 겪는 문제입니다. "
            "Docker는 이 문제를 해결합니다. "
            "애플리케이션과 그 실행 환경(Python 버전, 라이브러리, OS 설정)을 "
            "하나의 '컨테이너'로 포장하여 어디서든 동일하게 실행할 수 있게 합니다. "
            "이 챕터에서는 Docker의 핵심 개념부터 Dockerfile 작성, "
            "docker-compose로 여러 서비스를 함께 실행하는 법까지 배웁니다. "
            "MLOps 엔지니어가 되려면 Docker는 필수 역량입니다."
        ),
        "sections": [
            # ── 섹션 1: Docker란? 가상화 vs 컨테이너 ─────────────
            {
                "title": "Docker란? 가상화 vs 컨테이너",
                "content": [
                    "서버에서 여러 애플리케이션을 동시에 실행하려면 환경이 충돌하는 문제가 생깁니다. "
                    "예를 들어 앱 A는 Python 3.9, 앱 B는 Python 3.11이 필요할 수 있습니다. "
                    "가상 머신(VM)은 OS 전체를 격리하는 방법이고, "
                    "컨테이너는 OS 커널을 공유하며 훨씬 가볍게 격리합니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "가상 머신은 각자 독립된 집을 짓는 것입니다 — 개별 주방, 화장실, 전기 시스템이 있습니다. "
                            "반면 Docker 컨테이너는 아파트의 각 세대와 같습니다. "
                            "건물 인프라(OS 커널, 하드웨어)는 공유하지만 "
                            "각 세대는 완전히 격리된 공간을 가집니다. "
                            "컨테이너는 VM보다 훨씬 빠르게 시작되고, 용량도 훨씬 작습니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["항목", "가상 머신 (VM)", "Docker 컨테이너"],
                        "rows": [
                            ["크기", "수 GB (OS 전체 포함)", "수 MB ~ 수백 MB"],
                            ["시작 시간", "수 분", "수 초"],
                            ["OS 격리", "완전한 OS 격리", "커널 공유, 프로세스 격리"],
                            ["성능 오버헤드", "높음 (하이퍼바이저)", "낮음 (네이티브에 근접)"],
                            ["사용 사례", "OS 수준 격리 필요 시", "앱 배포, 마이크로서비스"],
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["Docker 용어", "설명", "비유"],
                        "rows": [
                            ["이미지 (Image)", "컨테이너를 만드는 설계도/청사진", "요리 레시피"],
                            ["컨테이너 (Container)", "이미지로부터 실행된 실체", "요리한 음식"],
                            ["Dockerfile", "이미지를 빌드하는 명령어 파일", "레시피 작성 노트"],
                            ["레지스트리 (Registry)", "이미지를 저장하고 공유하는 저장소", "레시피 공유 사이트"],
                            ["볼륨 (Volume)", "컨테이너 외부에 데이터 영속 저장", "냉장고 (재료 보관)"],
                        ],
                    },
                    {
                        "type": "flow_diagram",
                        "title": "Docker 이미지 → 컨테이너 라이프사이클",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "Dockerfile", "sub": "이미지 설계도"},
                            {"label": "docker build", "sub": "이미지 생성"},
                            {"label": "Image", "sub": "실행 가능한 패키지"},
                            {"label": "docker run", "sub": "컨테이너 생성"},
                            {"label": "Container", "sub": "실행 중인 인스턴스"},
                        ],
                        "note": "이미지 하나로 여러 컨테이너를 동시에 실행할 수 있습니다.",
                    },
                    {
                        "type": "note",
                        "text": (
                            "Docker Hub(hub.docker.com)는 공식 이미지 레지스트리입니다. "
                            "python:3.11-slim, nginx, postgres, redis 등 "
                            "수십만 개의 공개 이미지가 있습니다. "
                            "이미 검증된 이미지를 기반으로 나만의 이미지를 빌드하는 것이 표준 방식입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: Docker 설치 및 기본 명령어 ───────────────
            {
                "title": "Docker 설치 및 기본 명령어",
                "content": [
                    "Docker Desktop(macOS/Windows)이나 Docker Engine(Linux)을 설치하면 "
                    "docker 명령어를 사용할 수 있습니다. "
                    "기본 명령어를 익히면 공개 이미지를 즉시 활용할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── 설치 확인 ──────────────────────────────────────\n"
                            "docker --version          # Docker version 24.x.x\n"
                            "docker compose version    # Docker Compose version v2.x.x\n\n"
                            "# ── 이미지 관련 명령어 ──────────────────────────────\n"
                            "# Docker Hub에서 이미지 다운로드\n"
                            "docker pull python:3.11-slim\n\n"
                            "# 로컬에 저장된 이미지 목록 확인\n"
                            "docker images\n\n"
                            "# 이미지 삭제\n"
                            "docker rmi python:3.11-slim\n\n"
                            "# ── 컨테이너 실행 ───────────────────────────────────\n"
                            "# 기본 실행: 이미지에서 컨테이너 생성 후 실행\n"
                            "docker run python:3.11-slim python --version\n\n"
                            "# 인터랙티브 모드 (-it): 터미널로 직접 접근\n"
                            "docker run -it python:3.11-slim bash\n\n"
                            "# 백그라운드 실행 (-d) + 포트 매핑 (-p 호스트:컨테이너)\n"
                            "docker run -d -p 8080:80 nginx\n\n"
                            "# 컨테이너 이름 지정 (--name)\n"
                            "docker run -d --name my-nginx -p 8080:80 nginx"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── 실행 중인 컨테이너 관리 ────────────────────────\n"
                            "# 실행 중인 컨테이너 목록\n"
                            "docker ps\n\n"
                            "# 모든 컨테이너 목록 (정지된 것 포함)\n"
                            "docker ps -a\n\n"
                            "# 컨테이너 로그 확인\n"
                            "docker logs my-nginx\n"
                            "docker logs -f my-nginx    # 실시간 로그 스트리밍\n\n"
                            "# 실행 중인 컨테이너 내부에서 명령 실행\n"
                            "docker exec -it my-nginx bash\n\n"
                            "# 컨테이너 정지 / 재시작 / 삭제\n"
                            "docker stop my-nginx\n"
                            "docker start my-nginx\n"
                            "docker restart my-nginx\n"
                            "docker rm my-nginx          # 정지된 컨테이너 삭제\n"
                            "docker rm -f my-nginx       # 실행 중인 컨테이너 강제 삭제\n\n"
                            "# ── 정리 명령어 ─────────────────────────────────────\n"
                            "# 정지된 컨테이너, 미사용 이미지 등 일괄 정리\n"
                            "docker system prune        # 확인 후 삭제\n"
                            "docker system prune -af    # 전부 강제 삭제 (주의!)"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "자주 쓰는 옵션"],
                        "rows": [
                            ["docker pull", "이미지 다운로드", "이미지명:태그"],
                            ["docker run", "컨테이너 생성 및 실행", "-d, -it, -p, --name, -v, -e"],
                            ["docker ps", "실행 중인 컨테이너 목록", "-a (전체)"],
                            ["docker stop/start", "컨테이너 정지/시작", "컨테이너명 또는 ID"],
                            ["docker logs", "컨테이너 로그 출력", "-f (실시간 스트리밍)"],
                            ["docker exec", "실행 중인 컨테이너에서 명령 실행", "-it (인터랙티브)"],
                            ["docker rm", "컨테이너 삭제", "-f (강제)"],
                            ["docker rmi", "이미지 삭제", "이미지명 또는 ID"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "컨테이너 ID는 앞 3~4자리만 입력해도 됩니다. "
                            "예: docker stop a3f2 "
                            "또한 --rm 옵션을 붙이면 컨테이너 종료 시 자동으로 삭제됩니다: "
                            "docker run --rm python:3.11-slim python -c 'print(\"Hello\")'  "
                            "임시 테스트에 매우 유용합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 3: Dockerfile 작성법 ─────────────────────────
            {
                "title": "Dockerfile 작성법",
                "content": [
                    "Dockerfile은 이미지를 빌드하는 명령어들의 모음입니다. "
                    "각 명령어는 '레이어(layer)'를 만들며, "
                    "레이어는 캐싱되어 재빌드 시 변경된 레이어부터만 다시 실행됩니다. "
                    "이 레이어 구조를 이해하면 빌드 속도를 크게 최적화할 수 있습니다.",
                    {
                        "type": "table",
                        "headers": ["명령어", "설명", "예시"],
                        "rows": [
                            ["FROM", "베이스 이미지 지정 (첫 번째 줄)", "FROM python:3.11-slim"],
                            ["WORKDIR", "작업 디렉토리 설정", "WORKDIR /app"],
                            ["COPY", "호스트 파일을 이미지로 복사", "COPY . /app"],
                            ["RUN", "이미지 빌드 시 실행할 명령어", "RUN pip install -r requirements.txt"],
                            ["ENV", "환경 변수 설정", "ENV APP_ENV=production"],
                            ["EXPOSE", "컨테이너가 사용하는 포트 문서화", "EXPOSE 8000"],
                            ["CMD", "컨테이너 시작 시 기본 명령어 (덮어쓰기 가능)", "CMD [\"uvicorn\", \"main:app\"]"],
                            ["ENTRYPOINT", "컨테이너 시작 시 항상 실행할 명령어", "ENTRYPOINT [\"python\"]"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "dockerfile",
                        "code": (
                            "# ── FastAPI 앱을 위한 기본 Dockerfile ──────────────\n"
                            "# 1. 베이스 이미지: python:3.11-slim (경량 Debian 기반)\n"
                            "FROM python:3.11-slim\n\n"
                            "# 2. 작업 디렉토리 설정\n"
                            "WORKDIR /app\n\n"
                            "# 3. 의존성 파일 먼저 복사 (캐시 최적화 핵심!)\n"
                            "#    requirements.txt가 변경될 때만 pip install이 다시 실행됨\n"
                            "COPY requirements.txt .\n"
                            "RUN pip install --no-cache-dir -r requirements.txt\n\n"
                            "# 4. 나머지 소스 코드 복사\n"
                            "COPY . .\n\n"
                            "# 5. 포트 문서화 (실제 포트 오픈은 docker run -p 에서)\n"
                            "EXPOSE 8000\n\n"
                            "# 6. 환경 변수 기본값 설정\n"
                            "ENV APP_ENV=production\n\n"
                            "# 7. 컨테이너 시작 명령어\n"
                            "CMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "레이어 캐시 최적화의 핵심: 자주 변경되지 않는 것을 먼저 COPY/RUN하세요. "
                            "requirements.txt는 소스코드보다 덜 바뀌므로 먼저 복사합니다. "
                            "COPY . .를 먼저 하면 코드 한 줄 바꿔도 pip install부터 다시 실행됩니다."
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# .dockerignore 파일: 이미지에 포함하지 않을 파일 지정\n"
                            "# (Python의 .gitignore처럼 동작)\n"
                            "# .dockerignore 내용:\n"
                            "__pycache__\n"
                            "*.pyc\n"
                            ".git\n"
                            ".env\n"
                            "*.log\n"
                            "venv/\n"
                            ".pytest_cache/"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            ".env 파일은 절대 이미지에 포함하지 마세요! "
                            ".dockerignore에 반드시 추가하고, "
                            "시크릿은 docker run -e 옵션이나 docker-compose의 environment 섹션으로 전달하세요. "
                            "이미지를 Docker Hub에 공개하면 전 세계가 API 키를 볼 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: 이미지 빌드 및 실행 ──────────────────────
            {
                "title": "이미지 빌드 및 실행",
                "content": [
                    "Dockerfile을 작성했으면 이미지를 빌드하고 컨테이너로 실행해봅시다. "
                    "빌드 과정에서 각 명령어가 레이어로 쌓이는 것을 확인할 수 있습니다.",
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── 이미지 빌드 ─────────────────────────────────────\n"
                            "# -t: 이미지에 이름:태그 지정\n"
                            "# . : Dockerfile이 있는 디렉토리 (빌드 컨텍스트)\n"
                            "docker build -t my-fastapi-app:latest .\n\n"
                            "# 빌드 출력 예시:\n"
                            "#  [1/4] FROM python:3.11-slim        (캐시 히트 또는 다운로드)\n"
                            "#  [2/4] COPY requirements.txt .       (레이어 생성)\n"
                            "#  [3/4] RUN pip install ...           (패키지 설치)\n"
                            "#  [4/4] COPY . .                      (소스 복사)\n\n"
                            "# 빌드된 이미지 확인\n"
                            "docker images | grep my-fastapi-app\n\n"
                            "# ── 컨테이너 실행 ───────────────────────────────────\n"
                            "# -p 8000:8000 : 호스트 포트 8000 → 컨테이너 포트 8000 매핑\n"
                            "# -d : 백그라운드 실행\n"
                            "# --name: 컨테이너 이름 지정\n"
                            "docker run -d -p 8000:8000 --name api-server my-fastapi-app:latest\n\n"
                            "# 실행 확인\n"
                            "docker ps\n"
                            "curl http://localhost:8000/health\n\n"
                            "# 로그 확인\n"
                            "docker logs -f api-server"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── 환경 변수 주입 (-e 옵션) ───────────────────────\n"
                            "docker run -d \\\n"
                            "  -p 8000:8000 \\\n"
                            "  -e DATABASE_URL=postgresql://user:pass@db:5432/mydb \\\n"
                            "  -e SECRET_KEY=my-secret-key \\\n"
                            "  -e APP_ENV=production \\\n"
                            "  --name api-server \\\n"
                            "  my-fastapi-app:latest\n\n"
                            "# ── .env 파일로 환경 변수 일괄 주입 ───────────────\n"
                            "docker run -d \\\n"
                            "  -p 8000:8000 \\\n"
                            "  --env-file .env.production \\\n"
                            "  --name api-server \\\n"
                            "  my-fastapi-app:latest\n\n"
                            "# ── 볼륨 마운트 (-v 옵션) ───────────────────────────\n"
                            "# 호스트 경로:컨테이너 경로 (개발 중 코드 변경 즉시 반영)\n"
                            "docker run -d \\\n"
                            "  -p 8000:8000 \\\n"
                            "  -v $(pwd)/app:/app/app \\\n"
                            "  --name api-dev \\\n"
                            "  my-fastapi-app:latest"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "개발 환경에서는 -v 볼륨 마운트로 코드를 컨테이너에 실시간 반영하고, "
                            "운영 환경에서는 COPY로 코드를 이미지 안에 포함시킵니다. "
                            "uvicorn --reload 옵션과 볼륨 마운트를 함께 쓰면 "
                            "FastAPI 앱을 호스트에서 개발하면서 컨테이너로 즉시 테스트할 수 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 5: docker-compose로 멀티 컨테이너 ───────────
            {
                "title": "docker-compose로 멀티 컨테이너 관리",
                "content": [
                    "실제 앱은 웹 서버, 데이터베이스, 캐시 등 여러 서비스로 구성됩니다. "
                    "docker-compose는 여러 컨테이너를 하나의 YAML 파일로 정의하고 "
                    "한 번에 실행/정지하는 도구입니다.",
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": (
                            "# docker-compose.yml — FastAPI + PostgreSQL + Redis\n"
                            "version: '3.9'\n\n"
                            "services:\n"
                            "  # ── 1. FastAPI 웹 서버 ────────────────────────────\n"
                            "  api:\n"
                            "    build: .                    # 현재 디렉토리 Dockerfile 빌드\n"
                            "    ports:\n"
                            "      - '8000:8000'\n"
                            "    environment:\n"
                            "      - DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydb\n"
                            "      - REDIS_URL=redis://redis:6379/0\n"
                            "    depends_on:\n"
                            "      db:\n"
                            "        condition: service_healthy  # DB가 준비된 후 시작\n"
                            "      redis:\n"
                            "        condition: service_started\n"
                            "    volumes:\n"
                            "      - ./app:/app/app          # 개발 시 코드 실시간 반영\n"
                            "    networks:\n"
                            "      - app-network\n\n"
                            "  # ── 2. PostgreSQL 데이터베이스 ─────────────────────\n"
                            "  db:\n"
                            "    image: postgres:15-alpine\n"
                            "    environment:\n"
                            "      POSTGRES_USER: myuser\n"
                            "      POSTGRES_PASSWORD: mypassword\n"
                            "      POSTGRES_DB: mydb\n"
                            "    volumes:\n"
                            "      - postgres_data:/var/lib/postgresql/data  # 데이터 영속화\n"
                            "    healthcheck:\n"
                            "      test: ['CMD-SHELL', 'pg_isready -U myuser']\n"
                            "      interval: 10s\n"
                            "      timeout: 5s\n"
                            "      retries: 5\n"
                            "    networks:\n"
                            "      - app-network\n\n"
                            "  # ── 3. Redis 캐시 ─────────────────────────────────\n"
                            "  redis:\n"
                            "    image: redis:7-alpine\n"
                            "    networks:\n"
                            "      - app-network\n\n"
                            "volumes:\n"
                            "  postgres_data:               # 이름 있는 볼륨 (영속 저장)\n\n"
                            "networks:\n"
                            "  app-network:\n"
                            "    driver: bridge"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── docker-compose 주요 명령어 ──────────────────────\n"
                            "# 모든 서비스 시작 (백그라운드)\n"
                            "docker compose up -d\n\n"
                            "# 이미지 새로 빌드 후 시작\n"
                            "docker compose up -d --build\n\n"
                            "# 서비스 상태 확인\n"
                            "docker compose ps\n\n"
                            "# 특정 서비스 로그\n"
                            "docker compose logs api\n"
                            "docker compose logs -f api      # 실시간\n\n"
                            "# 특정 서비스에서 명령 실행\n"
                            "docker compose exec api bash\n"
                            "docker compose exec db psql -U myuser mydb\n\n"
                            "# 모든 서비스 정지\n"
                            "docker compose stop\n\n"
                            "# 모든 서비스 정지 + 컨테이너 삭제\n"
                            "docker compose down\n\n"
                            "# 컨테이너 + 볼륨 삭제 (데이터까지 초기화 — 주의!)\n"
                            "docker compose down -v"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "docker-compose 네트워크에서는 서비스명이 곧 호스트명입니다. "
                            "api 서비스에서 PostgreSQL에 접속할 때 호스트를 'db'로 지정하면 "
                            "자동으로 db 서비스 컨테이너로 연결됩니다. "
                            "IP 주소를 하드코딩할 필요가 없습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: 볼륨, 네트워크, 환경 변수 ───────────────
            {
                "title": "볼륨, 네트워크, 환경 변수 심화",
                "content": [
                    "컨테이너는 기본적으로 상태가 없습니다(stateless). "
                    "컨테이너를 삭제하면 내부 데이터도 사라집니다. "
                    "볼륨은 데이터를 컨테이너 외부에 영속적으로 저장하는 메커니즘입니다.",
                    {
                        "type": "table",
                        "headers": ["볼륨 유형", "설명", "사용 사례"],
                        "rows": [
                            ["이름 있는 볼륨\n(Named Volume)", "Docker가 관리하는 영속 저장소", "DB 데이터, 운영 환경"],
                            ["바인드 마운트\n(Bind Mount)", "호스트 디렉토리를 컨테이너에 연결", "개발 시 코드 실시간 반영"],
                            ["tmpfs 마운트", "메모리에만 저장 (컨테이너 종료 시 삭제)", "임시 파일, 비밀 데이터"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── 이름 있는 볼륨 (Named Volume) ───────────────────\n"
                            "# 볼륨 생성\n"
                            "docker volume create my-data\n\n"
                            "# 볼륨을 마운트하여 컨테이너 실행\n"
                            "docker run -v my-data:/app/data my-app\n\n"
                            "# 볼륨 목록 / 상세 정보\n"
                            "docker volume ls\n"
                            "docker volume inspect my-data\n\n"
                            "# ── 환경 변수 우선순위 ───────────────────────────────\n"
                            "# 1. docker run -e (가장 높음)\n"
                            "# 2. docker-compose environment 섹션\n"
                            "# 3. Dockerfile ENV\n"
                            "# 4. 기본값 (코드 내 os.getenv('KEY', 'default'))\n\n"
                            "# ── 네트워크 확인 ────────────────────────────────────\n"
                            "docker network ls\n"
                            "docker network inspect app-network"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# FastAPI 앱에서 환경 변수 안전하게 읽기\n"
                            "import os\n"
                            "from functools import lru_cache\n"
                            "from pydantic_settings import BaseSettings\n\n\n"
                            "class Settings(BaseSettings):\n"
                            "    \"\"\"환경 변수를 타입-안전하게 읽는 설정 클래스.\"\"\"\n\n"
                            "    database_url: str\n"
                            "    secret_key: str\n"
                            "    app_env: str = 'development'\n"
                            "    redis_url: str = 'redis://localhost:6379/0'\n\n"
                            "    class Config:\n"
                            "        env_file = '.env'          # 로컬 개발용 .env 파일\n"
                            "        env_file_encoding = 'utf-8'\n\n\n"
                            "@lru_cache\n"
                            "def get_settings() -> Settings:\n"
                            "    \"\"\"설정 인스턴스를 반환한다 (캐시됨).\"\"\"\n"
                            "    return Settings()\n\n\n"
                            "# 사용 예시\n"
                            "settings = get_settings()\n"
                            "print(settings.app_env)        # production (환경 변수)\n"
                            "print(settings.database_url)   # postgresql://..."
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "pydantic-settings 라이브러리를 사용하면 "
                            "환경 변수를 타입 검증과 함께 읽을 수 있습니다. "
                            "필수 환경 변수가 없으면 앱 시작 시 즉시 에러가 발생하여 "
                            "운영 환경에서의 설정 오류를 조기에 발견할 수 있습니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "python:3.11-slim 이미지를 사용하면 full 버전 대비 이미지 크기를 70% 이상 줄일 수 있습니다.",
            "Dockerfile에서 requirements.txt를 소스 코드보다 먼저 COPY하면 레이어 캐시를 활용해 빌드 시간을 단축합니다.",
            ".dockerignore 파일을 반드시 작성하여 .git, __pycache__, .env 등이 이미지에 포함되지 않도록 합니다.",
            "docker-compose에서 depends_on + healthcheck를 함께 사용하면 DB가 실제로 준비된 후 앱이 시작됩니다.",
            "개발 중에는 바인드 마운트(-v ./app:/app/app)로 코드를 실시간 반영하고, 운영에는 COPY로 이미지에 포함시킵니다.",
            "docker compose logs -f [서비스명]으로 특정 서비스 로그만 실시간으로 볼 수 있습니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "Docker 이미지와 컨테이너의 관계를 가장 잘 설명한 것은?"
                ),
                "choices": [
                    "A) 이미지와 컨테이너는 동일한 개념이다",
                    "B) 이미지는 실행 중인 인스턴스이고, 컨테이너는 설계도이다",
                    "C) 이미지는 설계도이고, 컨테이너는 이미지로부터 생성된 실행 인스턴스이다",
                    "D) 하나의 이미지로는 하나의 컨테이너만 만들 수 있다",
                ],
                "answer": "C",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "Dockerfile에서 레이어 캐시를 최적화하기 위해 올바른 순서는?"
                ),
                "choices": [
                    "A) COPY . .  →  COPY requirements.txt .  →  RUN pip install",
                    "B) COPY requirements.txt .  →  RUN pip install  →  COPY . .",
                    "C) RUN pip install  →  COPY requirements.txt .  →  COPY . .",
                    "D) COPY . .  →  RUN pip install  →  COPY requirements.txt .",
                ],
                "answer": "B",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "docker-compose.yml에서 api 서비스가 PostgreSQL 컨테이너에 접속할 때 "
                    "호스트명으로 사용해야 하는 값은? (서비스명이 'db'인 경우)"
                ),
                "choices": [
                    "A) localhost",
                    "B) 127.0.0.1",
                    "C) db",
                    "D) postgres",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "Python 3.11-slim을 베이스로, 작업 디렉토리를 /app으로 설정하고, "
                    "requirements.txt 복사 및 pip install 후 소스 코드를 복사하며, "
                    "포트 8000을 노출하고 uvicorn으로 main:app을 실행하는 Dockerfile을 작성하세요."
                ),
                "hint": (
                    "FROM python:3.11-slim → WORKDIR /app → COPY requirements.txt . → "
                    "RUN pip install --no-cache-dir -r requirements.txt → COPY . . → "
                    "EXPOSE 8000 → CMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "FastAPI 앱(api)과 PostgreSQL(db)을 함께 실행하는 docker-compose.yml을 작성하세요. "
                    "api는 현재 디렉토리에서 빌드하고 포트 8000을 노출합니다. "
                    "db는 postgres:15-alpine 이미지를 사용하고 이름 있는 볼륨으로 데이터를 영속화합니다."
                ),
                "hint": (
                    "services 아래 api (build: ., ports: ['8000:8000'], depends_on: [db])와 "
                    "db (image: postgres:15-alpine, environment: POSTGRES_USER 등, "
                    "volumes: postgres_data:/var/lib/postgresql/data)를 정의합니다. "
                    "최하단에 volumes: postgres_data: 선언을 추가하는 것을 잊지 마세요."
                ),
            },
        ],
        "challenge": {
            "question": (
                "챕터 5에서 만든 FastAPI + SQLAlchemy 앱을 완전히 컨테이너화하세요. "
                "요구사항: "
                "1) Dockerfile을 작성하여 앱을 이미지로 빌드합니다. "
                "2) docker-compose.yml로 FastAPI 앱과 PostgreSQL을 함께 실행합니다. "
                "3) PostgreSQL 데이터는 이름 있는 볼륨으로 영속화합니다. "
                "4) DB 헬스체크를 추가하여 DB가 준비된 후 앱이 시작되도록 합니다. "
                "5) 환경 변수(DATABASE_URL, SECRET_KEY)는 .env 파일로 관리하고 "
                ".dockerignore에 .env를 추가합니다. "
                "6) docker compose up -d --build 한 번으로 전체 환경이 올라와야 합니다. "
                "7) docker compose exec db psql로 DB에 직접 접속하여 테이블을 확인합니다."
            ),
            "hint": (
                "Dockerfile: python:3.11-slim 기반, requirements.txt 먼저 COPY. "
                "docker-compose.yml: api 서비스에 env_file: .env 지정, "
                "db 서비스에 healthcheck 추가 (pg_isready -U ${POSTGRES_USER}). "
                "앱의 DATABASE_URL에서 호스트를 'db'(서비스명)로 설정하는 것이 핵심입니다."
            ),
        },
        "summary": [
            "Docker는 앱과 실행 환경을 컨테이너로 패키징하여 '내 컴퓨터에서는 되는데' 문제를 해결한다.",
            "이미지는 설계도, 컨테이너는 이미지로부터 생성된 실행 인스턴스다. 하나의 이미지로 여러 컨테이너를 실행할 수 있다.",
            "Dockerfile에서 requirements.txt를 소스 코드보다 먼저 복사하면 레이어 캐시를 활용해 빌드가 빨라진다.",
            "docker-compose.yml로 여러 서비스(앱 + DB + 캐시)를 한 번에 정의하고 실행할 수 있다.",
            "이름 있는 볼륨으로 DB 데이터를 영속화하고, .dockerignore와 환경 변수로 시크릿을 안전하게 관리한다.",
            "docker-compose 네트워크에서는 서비스명이 곧 호스트명이므로 IP 하드코딩 없이 서비스 간 통신이 가능하다.",
        ],
    }
