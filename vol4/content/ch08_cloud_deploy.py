"""챕터 8: 클라우드 배포 — 로컬 앱을 세상에 공개하는 법."""


def get_chapter():
    """챕터 8 콘텐츠를 반환한다."""
    return {
        "number": 8,
        "title": "클라우드 배포",
        "subtitle": "로컬 앱을 세상에 공개하는 법",
        "big_picture": (
            "로컬에서 완성한 FastAPI 앱을 실제 사용자가 접근할 수 있으려면 "
            "클라우드 서버에 배포해야 합니다. "
            "클라우드는 서버를 직접 구매·운영하지 않고 "
            "필요할 때 필요한 만큼 빌려 쓰는 인프라입니다. "
            "이 챕터에서는 클라우드 서비스 유형을 이해하고, "
            "EC2에 Docker로 직접 배포하는 법, "
            "Railway/Render 같은 PaaS로 쉽게 배포하는 법, "
            "환경 변수와 시크릿 관리, "
            "그리고 배포 후 모니터링 기초까지 배웁니다."
        ),
        "sections": [
            # ── 섹션 1: 클라우드 기초 ────────────────────────────
            {
                "title": "클라우드 기초: IaaS, PaaS, SaaS",
                "content": [
                    "클라우드 서비스는 제공하는 추상화 수준에 따라 세 가지로 분류됩니다. "
                    "어느 계층을 선택하느냐에 따라 제어 수준과 운영 복잡도가 달라집니다.",
                    {
                        "type": "analogy",
                        "text": (
                            "클라우드 서비스 유형은 자동차 이용 방식과 비슷합니다. "
                            "IaaS는 렌터카 — 차(서버)를 빌려서 직접 운전(설정, 운영)합니다. "
                            "PaaS는 택시 — 목적지(앱 코드)만 말하면 알아서 데려다 줍니다. "
                            "SaaS는 버스/지하철 — 노선(기능)이 정해져 있고 그냥 탑니다."
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["유형", "설명", "관리 범위", "대표 서비스"],
                        "rows": [
                            [
                                "IaaS\n(인프라형)",
                                "가상 서버, 네트워크, 스토리지 제공",
                                "OS, 미들웨어, 앱 모두 직접 관리",
                                "AWS EC2, GCP Compute Engine, Azure VM",
                            ],
                            [
                                "PaaS\n(플랫폼형)",
                                "앱 실행 환경 제공 (OS, 런타임 포함)",
                                "앱 코드와 데이터만 관리",
                                "Railway, Render, Fly.io, Heroku",
                            ],
                            [
                                "SaaS\n(소프트웨어형)",
                                "완성된 소프트웨어 제공",
                                "사용만 함",
                                "Gmail, Notion, GitHub, Slack",
                            ],
                        ],
                    },
                    {
                        "type": "table",
                        "headers": ["항목", "IaaS (EC2)", "PaaS (Railway/Render)"],
                        "rows": [
                            ["초기 설정", "복잡 (OS, Docker, 방화벽 등)", "간단 (저장소 연결만)"],
                            ["제어 수준", "높음 (모든 것 직접 설정)", "낮음 (플랫폼이 처리)"],
                            ["비용", "저렴 (프리티어 포함)", "소규모 무료, 이후 유료"],
                            ["확장성", "수동 또는 Auto Scaling 설정", "플랫폼이 자동 처리"],
                            ["추천 상황", "세밀한 제어 필요, 대규모 서비스", "빠른 프로토타입, 소규모 서비스"],
                        ],
                    },
                    {
                        "type": "note",
                        "text": (
                            "MLOps 엔지니어는 주로 IaaS(EC2, GCP VM)를 다룹니다. "
                            "모델 서빙 서버의 GPU 타입, 메모리, 네트워크를 세밀하게 제어해야 하기 때문입니다. "
                            "그러나 빠른 데모나 API 서버 배포에는 PaaS가 훨씬 효율적입니다."
                        ),
                    },
                ],
            },
            # ── 섹션 2: AWS EC2 / GCP Compute Engine 기초 ─────────
            {
                "title": "AWS EC2 / GCP Compute Engine 기초",
                "content": [
                    "EC2(Elastic Compute Cloud)는 AWS의 가상 서버 서비스입니다. "
                    "인스턴스를 생성하면 리눅스 서버 하나를 받는 것과 같습니다. "
                    "여기에 Docker를 설치하고 컨테이너를 실행하는 것이 기본 배포 패턴입니다.",
                    {
                        "type": "table",
                        "headers": ["단계", "AWS EC2", "GCP Compute Engine"],
                        "rows": [
                            ["서비스 접근", "AWS Console > EC2", "GCP Console > Compute Engine"],
                            ["인스턴스 생성", "Launch Instance", "VM 인스턴스 만들기"],
                            ["추천 무료 티어", "t2.micro (1vCPU, 1GB RAM)", "e2-micro (0.25vCPU, 1GB RAM)"],
                            ["OS 이미지", "Amazon Linux 2023 / Ubuntu 22.04", "Debian 12 / Ubuntu 22.04"],
                            ["접속 방식", "SSH (키 페어)", "SSH (gcloud 또는 키 페어)"],
                            ["방화벽", "Security Group (포트 80, 443, 22)", "방화벽 규칙"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── EC2 인스턴스에 SSH 접속 후 Docker 설치 (Ubuntu 기준) ──\n"
                            "ssh -i my-key.pem ubuntu@[EC2 퍼블릭 IP]\n\n"
                            "# 패키지 업데이트\n"
                            "sudo apt-get update && sudo apt-get upgrade -y\n\n"
                            "# Docker 설치 (공식 스크립트 사용)\n"
                            "curl -fsSL https://get.docker.com -o get-docker.sh\n"
                            "sudo sh get-docker.sh\n\n"
                            "# 현재 사용자를 docker 그룹에 추가 (sudo 없이 docker 실행)\n"
                            "sudo usermod -aG docker $USER\n"
                            "newgrp docker\n\n"
                            "# Docker Compose 설치\n"
                            "sudo apt-get install -y docker-compose-plugin\n\n"
                            "# 설치 확인\n"
                            "docker --version\n"
                            "docker compose version"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── EC2에서 앱 배포 절차 ─────────────────────────────\n\n"
                            "# 방법 1: Docker Hub에서 이미지 직접 Pull\n"
                            "docker pull myusername/my-fastapi-app:latest\n"
                            "docker run -d \\\n"
                            "  -p 80:8000 \\\n"
                            "  --env-file /home/ubuntu/.env \\\n"
                            "  --name api-server \\\n"
                            "  --restart unless-stopped \\\n"
                            "  myusername/my-fastapi-app:latest\n\n"
                            "# 방법 2: 소스 코드를 git clone 후 docker compose\n"
                            "git clone https://github.com/myusername/my-app.git\n"
                            "cd my-app\n"
                            "cp .env.example .env\n"
                            "# .env 파일 편집 (nano .env)\n"
                            "docker compose up -d --build\n\n"
                            "# ── 앱 자동 재시작 설정 ──────────────────────────────\n"
                            "# --restart unless-stopped: 서버 재부팅 시에도 자동 시작\n"
                            "# (docker-compose.yml의 restart: unless-stopped 와 동일)"
                        ),
                    },
                    {
                        "type": "warning",
                        "text": (
                            "EC2 Security Group에서 포트를 열 때는 필요한 포트만 허용하세요. "
                            "SSH(22)는 가능하면 내 IP로만 제한하고, "
                            "HTTP(80)/HTTPS(443)는 전체(0.0.0.0/0)에 개방합니다. "
                            "데이터베이스 포트(5432, 3306)는 절대 외부에 노출하지 마세요."
                        ),
                    },
                ],
            },
            # ── 섹션 3: 환경 변수와 시크릿 관리 ──────────────────
            {
                "title": "환경 변수와 시크릿 관리",
                "content": [
                    "배포 환경에서 API 키, DB 비밀번호, 암호화 키 등 민감한 정보를 "
                    "코드에 하드코딩하거나 Git에 커밋하면 절대 안 됩니다. "
                    "환경 변수와 시크릿 관리 서비스를 사용하는 것이 표준입니다.",
                    {
                        "type": "table",
                        "headers": ["방법", "설명", "적합한 환경"],
                        "rows": [
                            [".env 파일", "로컬 환경 변수 파일 (.gitignore에 추가)", "로컬 개발"],
                            ["docker run -e", "컨테이너 실행 시 직접 주입", "단순 배포"],
                            ["docker --env-file", ".env 파일을 컨테이너에 주입", "서버 배포"],
                            ["GitHub Secrets", "CI/CD 파이프라인용 시크릿", "GitHub Actions"],
                            ["AWS SSM Parameter Store", "AWS 환경 시크릿 중앙 관리", "AWS 운영 환경"],
                            ["AWS Secrets Manager", "자동 교체 지원 고급 시크릿 관리", "대규모 AWS 환경"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 환경 변수 안전하게 로드하기 ─────────────────────\n"
                            "import os\n"
                            "from pathlib import Path\n\n\n"
                            "def load_required_env(key: str) -> str:\n"
                            "    \"\"\"필수 환경 변수를 읽는다. 없으면 즉시 에러 발생.\"\"\"\n"
                            "    value = os.environ.get(key)\n"
                            "    if not value:\n"
                            "        raise EnvironmentError(\n"
                            "            f'필수 환경 변수 {key!r}가 설정되지 않았습니다. '\n"
                            "            f'.env 파일 또는 시스템 환경 변수를 확인하세요.'\n"
                            "        )\n"
                            "    return value\n\n\n"
                            "# 앱 시작 시 모든 필수 환경 변수 검증\n"
                            "DATABASE_URL = load_required_env('DATABASE_URL')\n"
                            "SECRET_KEY   = load_required_env('SECRET_KEY')\n"
                            "APP_ENV      = os.environ.get('APP_ENV', 'development')\n\n\n"
                            "# .env 파일 예시 (절대 Git에 커밋하지 마세요)\n"
                            "# DATABASE_URL=postgresql://user:pass@localhost:5432/mydb\n"
                            "# SECRET_KEY=super-secret-key-change-in-production\n"
                            "# APP_ENV=development"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── .gitignore에 반드시 추가 ────────────────────────\n"
                            "# .gitignore 내용:\n"
                            ".env\n"
                            ".env.*\n"
                            "!.env.example   # 예시 파일은 커밋 OK (실제 값 없음)\n\n"
                            "# ── .env.example 파일 (커밋 가능한 템플릿) ───────────\n"
                            "# .env.example 내용:\n"
                            "DATABASE_URL=postgresql://user:password@localhost:5432/dbname\n"
                            "SECRET_KEY=your-secret-key-here\n"
                            "APP_ENV=development\n"
                            "REDIS_URL=redis://localhost:6379/0\n\n"
                            "# ── 서버에 .env 파일 안전하게 복사 ─────────────────\n"
                            "# SCP로 암호화 전송 (SSH 키 사용)\n"
                            "scp -i my-key.pem .env.production ubuntu@[EC2-IP]:/home/ubuntu/.env"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "git secret 또는 git-crypt 도구를 사용하면 "
                            ".env 파일을 암호화한 채로 Git에 관리할 수 있습니다. "
                            "팀 협업 시 유용하지만, 개인 프로젝트에서는 "
                            ".env.example + 안전한 파일 전송으로도 충분합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 4: Docker 이미지 레지스트리 ─────────────────
            {
                "title": "Docker 이미지 레지스트리 (Docker Hub, ECR/GCR)",
                "content": [
                    "이미지 레지스트리는 Docker 이미지를 저장하고 공유하는 저장소입니다. "
                    "개발 환경에서 빌드한 이미지를 레지스트리에 Push하고, "
                    "서버에서 Pull하여 실행하는 것이 표준 배포 패턴입니다.",
                    {
                        "type": "table",
                        "headers": ["레지스트리", "제공사", "무료 한도", "특징"],
                        "rows": [
                            ["Docker Hub", "Docker", "공개 이미지 무제한, 비공개 1개", "가장 널리 사용"],
                            ["ECR (Elastic Container Registry)", "AWS", "500MB/월", "AWS 서비스와 통합"],
                            ["GCR (Google Container Registry)", "GCP", "0.5GB 무료", "GCP 서비스와 통합"],
                            ["GitHub Container Registry (ghcr.io)", "GitHub", "공개 무제한", "GitHub Actions 연동 편리"],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── Docker Hub Push / Pull ───────────────────────────\n\n"
                            "# 로그인\n"
                            "docker login\n\n"
                            "# 이미지 빌드 (이름 규칙: 사용자명/저장소명:태그)\n"
                            "docker build -t myusername/my-fastapi-app:v1.0.0 .\n"
                            "docker build -t myusername/my-fastapi-app:latest .\n\n"
                            "# Docker Hub에 Push\n"
                            "docker push myusername/my-fastapi-app:v1.0.0\n"
                            "docker push myusername/my-fastapi-app:latest\n\n"
                            "# 서버에서 Pull 후 실행\n"
                            "docker pull myusername/my-fastapi-app:v1.0.0\n"
                            "docker run -d -p 80:8000 myusername/my-fastapi-app:v1.0.0\n\n"
                            "# ── GitHub Container Registry (ghcr.io) 사용 ──────────\n"
                            "# GitHub Personal Access Token으로 로그인\n"
                            "echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin\n\n"
                            "# 이미지 태그 및 Push\n"
                            "docker tag my-app:latest ghcr.io/username/my-app:latest\n"
                            "docker push ghcr.io/username/my-app:latest"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "이미지 태그 전략: latest는 가장 최신 버전의 별칭입니다. "
                            "운영 환경에서는 v1.2.3 같은 명시적 버전 태그나 "
                            "Git 커밋 SHA(예: sha-a3f2c1d)를 함께 사용하여 "
                            "어느 버전이 배포되었는지 추적하고, 필요 시 이전 버전으로 롤백할 수 있게 하세요."
                        ),
                    },
                ],
            },
            # ── 섹션 5: EC2 + Docker 배포 시나리오 ───────────────
            {
                "title": "EC2 + Docker 배포 시나리오",
                "content": [
                    "이제 지금까지 배운 모든 것을 합쳐 실제 배포 시나리오를 살펴봅니다. "
                    "GitHub Actions CI/CD로 Docker 이미지를 빌드하여 레지스트리에 Push하고, "
                    "EC2 서버가 새 이미지를 Pull하여 무중단으로 교체합니다.",
                    {
                        "type": "flow_diagram",
                        "title": "전체 배포 파이프라인: Local → Registry → Cloud",
                        "direction": "horizontal",
                        "nodes": [
                            {"label": "로컬 개발", "sub": "코드 작성 + 테스트"},
                            {"label": "git push", "sub": "GitHub main 브랜치"},
                            {"label": "GitHub Actions", "sub": "CI: lint + test"},
                            {"label": "docker build", "sub": "이미지 빌드"},
                            {"label": "Registry Push", "sub": "Docker Hub / ghcr.io"},
                            {"label": "EC2 Pull & Run", "sub": "새 컨테이너 교체"},
                        ],
                        "note": "각 단계 실패 시 이후 단계는 실행되지 않습니다.",
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": (
                            "# .github/workflows/deploy.yml — EC2 자동 배포\n"
                            "name: Deploy to EC2\n\n"
                            "on:\n"
                            "  push:\n"
                            "    branches: [main]\n\n"
                            "jobs:\n"
                            "  deploy:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n\n"
                            "      # Docker 이미지 빌드 및 Docker Hub Push\n"
                            "      - uses: docker/login-action@v3\n"
                            "        with:\n"
                            "          username: ${{ secrets.DOCKERHUB_USERNAME }}\n"
                            "          password: ${{ secrets.DOCKERHUB_TOKEN }}\n\n"
                            "      - uses: docker/build-push-action@v5\n"
                            "        with:\n"
                            "          push: true\n"
                            "          tags: ${{ secrets.DOCKERHUB_USERNAME }}/my-app:latest\n\n"
                            "      # SSH로 EC2에 접속하여 새 이미지 배포\n"
                            "      - name: EC2에 배포\n"
                            "        uses: appleboy/ssh-action@v1\n"
                            "        with:\n"
                            "          host: ${{ secrets.EC2_HOST }}\n"
                            "          username: ubuntu\n"
                            "          key: ${{ secrets.EC2_SSH_KEY }}\n"
                            "          script: |\n"
                            "            docker pull ${{ secrets.DOCKERHUB_USERNAME }}/my-app:latest\n"
                            "            docker stop api-server || true\n"
                            "            docker rm api-server || true\n"
                            "            docker run -d \\\n"
                            "              --name api-server \\\n"
                            "              --restart unless-stopped \\\n"
                            "              -p 80:8000 \\\n"
                            "              --env-file /home/ubuntu/.env \\\n"
                            "              ${{ secrets.DOCKERHUB_USERNAME }}/my-app:latest"
                        ),
                    },
                    {
                        "type": "tip",
                        "text": (
                            "무중단 배포(Zero-downtime deployment)를 위해서는 "
                            "Nginx를 앞단에 두고 Blue-Green 또는 Rolling 배포 전략을 사용합니다. "
                            "간단한 방법은 포트를 교대로 사용하는 것입니다: "
                            "새 컨테이너를 8001 포트로 시작 후 헬스체크 통과하면 "
                            "Nginx가 트래픽을 8001로 전환하고 8000 컨테이너를 종료합니다."
                        ),
                    },
                ],
            },
            # ── 섹션 6: PaaS 배포 옵션 ───────────────────────────
            {
                "title": "PaaS 배포 옵션: Railway, Render, Fly.io",
                "content": [
                    "PaaS는 인프라 설정 없이 코드만 연결하면 자동으로 빌드하고 배포합니다. "
                    "빠른 프로토타입, 소규모 서비스, 개인 프로젝트에 매우 적합합니다.",
                    {
                        "type": "table",
                        "headers": ["서비스", "무료 티어", "특징", "추천 상황"],
                        "rows": [
                            [
                                "Railway",
                                "월 $5 크레딧",
                                "GitHub 연동, 자동 배포, DB 내장",
                                "빠른 프로토타입",
                            ],
                            [
                                "Render",
                                "Web Service 무료 (느림)",
                                "정적 사이트, Web Service, Cron 지원",
                                "소규모 API 서버",
                            ],
                            [
                                "Fly.io",
                                "3개 인스턴스 무료",
                                "글로벌 엣지 배포, Docker 기반",
                                "글로벌 저지연 서비스",
                            ],
                            [
                                "Heroku",
                                "없음 (유료 전환)",
                                "가장 오래된 PaaS, 다양한 Add-on",
                                "대규모 생태계 활용",
                            ],
                        ],
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── Railway 배포 (CLI 사용) ──────────────────────────\n"
                            "# 설치\n"
                            "npm install -g @railway/cli\n\n"
                            "# 로그인\n"
                            "railway login\n\n"
                            "# 프로젝트 초기화 (저장소 루트에서)\n"
                            "railway init\n\n"
                            "# 환경 변수 설정\n"
                            "railway variables set DATABASE_URL=postgresql://...\n"
                            "railway variables set SECRET_KEY=my-secret\n\n"
                            "# 배포\n"
                            "railway up\n\n"
                            "# 배포 URL 확인\n"
                            "railway open\n\n"
                            "# ── Render 배포 (render.yaml 파일) ─────────────────\n"
                            "# render.yaml 내용:\n"
                            "services:\n"
                            "  - type: web\n"
                            "    name: my-fastapi-app\n"
                            "    runtime: python\n"
                            "    buildCommand: pip install -r requirements.txt\n"
                            "    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT\n"
                            "    envVars:\n"
                            "      - key: DATABASE_URL\n"
                            "        fromDatabase:\n"
                            "          name: my-postgres\n"
                            "          property: connectionString"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── Fly.io 배포 ─────────────────────────────────────\n"
                            "# Fly CLI 설치 (macOS)\n"
                            "brew install flyctl\n\n"
                            "# 로그인\n"
                            "fly auth login\n\n"
                            "# 앱 초기화 (Dockerfile 자동 감지)\n"
                            "fly launch\n\n"
                            "# 환경 변수(시크릿) 설정\n"
                            "fly secrets set DATABASE_URL=postgresql://...\n"
                            "fly secrets set SECRET_KEY=my-secret\n\n"
                            "# 배포\n"
                            "fly deploy\n\n"
                            "# 로그 확인\n"
                            "fly logs\n\n"
                            "# 앱 상태 확인\n"
                            "fly status"
                        ),
                    },
                    {
                        "type": "note",
                        "text": (
                            "PaaS 서비스는 대부분 GitHub 저장소와 연동하면 "
                            "main 브랜치에 Push될 때마다 자동으로 빌드하고 배포합니다. "
                            "별도의 CI/CD 파이프라인 설정 없이도 자동 배포가 가능합니다. "
                            "단, 플랫폼 종속성이 생기는 트레이드오프가 있습니다."
                        ),
                    },
                ],
            },
            # ── 섹션 7: 모니터링 기초 ─────────────────────────────
            {
                "title": "모니터링 기초: 로그, 헬스체크, 알림",
                "content": [
                    "배포 후 앱이 정상 동작하는지 지속적으로 확인하는 것이 모니터링입니다. "
                    "로그 수집, 헬스체크 엔드포인트, 에러 알림은 "
                    "운영 환경의 기본 안전망입니다.",
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── FastAPI 헬스체크 엔드포인트 ──────────────────────\n"
                            "import time\n"
                            "from fastapi import FastAPI\n"
                            "from sqlalchemy import text\n\n\n"
                            "app = FastAPI()\n"
                            "_start_time = time.time()\n\n\n"
                            "@app.get('/health')\n"
                            "def health_check():\n"
                            "    \"\"\"기본 헬스체크: 앱이 살아있는지만 확인한다.\"\"\"\n"
                            "    return {'status': 'ok', 'uptime': time.time() - _start_time}\n\n\n"
                            "@app.get('/health/ready')\n"
                            "def readiness_check(db=Depends(get_db)):\n"
                            "    \"\"\"준비 상태 확인: DB 연결까지 검증한다.\"\"\"\n"
                            "    try:\n"
                            "        db.execute(text('SELECT 1'))\n"
                            "        return {'status': 'ready', 'database': 'ok'}\n"
                            "    except Exception as e:\n"
                            "        raise HTTPException(\n"
                            "            status_code=503,\n"
                            "            detail={'status': 'not_ready', 'database': str(e)},\n"
                            "        )"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": (
                            "# ── 구조화된 로깅 설정 ───────────────────────────────\n"
                            "import logging\n"
                            "import sys\n"
                            "from contextlib import asynccontextmanager\n\n\n"
                            "def setup_logging() -> None:\n"
                            "    \"\"\"운영 환경에 적합한 로깅을 설정한다.\"\"\"\n"
                            "    logging.basicConfig(\n"
                            "        level=logging.INFO,\n"
                            "        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',\n"
                            "        handlers=[logging.StreamHandler(sys.stdout)],\n"
                            "    )\n\n\n"
                            "@asynccontextmanager\n"
                            "async def lifespan(app: FastAPI):\n"
                            "    \"\"\"앱 시작/종료 시 실행되는 라이프사이클 훅.\"\"\"\n"
                            "    setup_logging()\n"
                            "    logger = logging.getLogger(__name__)\n"
                            "    logger.info('앱 시작 완료')\n"
                            "    yield\n"
                            "    logger.info('앱 종료')\n\n\n"
                            "app = FastAPI(lifespan=lifespan)\n\n\n"
                            "# ── 요청 로깅 미들웨어 ────────────────────────────────\n"
                            "@app.middleware('http')\n"
                            "async def log_requests(request, call_next):\n"
                            "    \"\"\"모든 HTTP 요청을 로깅한다.\"\"\"\n"
                            "    logger = logging.getLogger('access')\n"
                            "    start = time.time()\n"
                            "    response = await call_next(request)\n"
                            "    duration = (time.time() - start) * 1000\n"
                            "    logger.info(\n"
                            "        '%s %s %d %.1fms',\n"
                            "        request.method, request.url.path,\n"
                            "        response.status_code, duration,\n"
                            "    )\n"
                            "    return response"
                        ),
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": (
                            "# ── Docker 컨테이너 로그 모니터링 ────────────────────\n\n"
                            "# 실시간 로그 스트리밍\n"
                            "docker logs -f api-server\n\n"
                            "# 최근 100줄만 확인\n"
                            "docker logs --tail 100 api-server\n\n"
                            "# 특정 시간 이후 로그\n"
                            "docker logs --since '2026-03-27T00:00:00' api-server\n\n"
                            "# ── docker-compose에 헬스체크 추가 ──────────────────\n"
                            "# docker-compose.yml 예시:\n"
                            "services:\n"
                            "  api:\n"
                            "    image: my-fastapi-app:latest\n"
                            "    healthcheck:\n"
                            "      test: ['CMD', 'curl', '-f', 'http://localhost:8000/health']\n"
                            "      interval: 30s\n"
                            "      timeout: 10s\n"
                            "      retries: 3\n"
                            "      start_period: 20s    # 앱 시작 시간 고려"
                        ),
                    },
                    {
                        "type": "table",
                        "headers": ["모니터링 도구", "유형", "무료 티어", "특징"],
                        "rows": [
                            ["UptimeRobot", "가용성 모니터링", "50개 모니터 무료", "5분 간격 헬스체크, 이메일 알림"],
                            ["Sentry", "에러 추적", "5,000건/월 무료", "Python 예외 자동 캡처, 스택트레이스"],
                            ["Grafana Cloud", "메트릭/로그", "10GB/월 무료", "Prometheus 연동, 대시보드"],
                            ["AWS CloudWatch", "AWS 네이티브", "기본 무료", "EC2 로그/메트릭 통합"],
                        ],
                    },
                    {
                        "type": "tip",
                        "text": (
                            "운영 환경 최소 모니터링 세트: "
                            "UptimeRobot(헬스체크) + Sentry(에러 추적) + docker logs(실시간 로그). "
                            "이 세 가지만 있어도 장애 발생 시 즉시 인지하고 원인을 파악할 수 있습니다. "
                            "pip install sentry-sdk[fastapi] 후 "
                            "sentry_sdk.init(dsn='...') 한 줄로 Sentry 연동이 완료됩니다."
                        ),
                    },
                ],
            },
        ],
        "practical_tips": [
            "EC2 프리티어(t2.micro)와 Docker를 조합하면 무료로 실제 서비스를 운영할 수 있습니다. 1년 무료 후 Railway/Render로 이전을 고려하세요.",
            "--restart unless-stopped 옵션을 사용하면 EC2 재부팅 시에도 컨테이너가 자동으로 재시작됩니다.",
            ".env.example 파일을 항상 최신 상태로 유지하면 팀원이 새 환경을 설정할 때 빠뜨리는 환경 변수를 방지할 수 있습니다.",
            "이미지 태그에 Git 커밋 SHA를 포함하면 (예: v1.0.0-a3f2c1d) 어느 커밋이 배포되었는지 추적하고 빠르게 롤백할 수 있습니다.",
            "FastAPI /health 엔드포인트를 UptimeRobot 등에 등록하면 서비스 다운 즉시 이메일/SMS 알림을 받을 수 있습니다.",
            "Sentry 연동은 pip install sentry-sdk[fastapi] 후 단 2줄로 완료됩니다. 운영 환경에서 발생하는 모든 예외를 자동 수집합니다.",
        ],
        "exercises": [
            {
                "number": 1,
                "type": "multiple_choice",
                "question": (
                    "IaaS, PaaS, SaaS 중 '앱 코드만 제공하면 인프라와 OS를 플랫폼이 관리'하는 서비스 유형은?"
                ),
                "choices": [
                    "A) IaaS",
                    "B) PaaS",
                    "C) SaaS",
                    "D) FaaS",
                ],
                "answer": "B",
            },
            {
                "number": 2,
                "type": "multiple_choice",
                "question": (
                    "Docker 컨테이너가 서버 재부팅 후에도 자동으로 재시작되도록 하는 옵션은?"
                ),
                "choices": [
                    "A) --auto-restart",
                    "B) --always-on",
                    "C) --restart unless-stopped",
                    "D) --keep-alive",
                ],
                "answer": "C",
            },
            {
                "number": 3,
                "type": "multiple_choice",
                "question": (
                    "민감한 시크릿 정보(API 키, DB 비밀번호)를 관리하는 올바른 방법은?"
                ),
                "choices": [
                    "A) 소스 코드에 직접 하드코딩한다",
                    "B) .env 파일을 Git에 커밋한다",
                    "C) 환경 변수나 시크릿 관리 서비스를 사용하고 .gitignore에 .env를 추가한다",
                    "D) 이미지 빌드 시 Dockerfile에 ARG로 전달한다",
                ],
                "answer": "C",
            },
            {
                "number": 4,
                "type": "coding",
                "question": (
                    "FastAPI 앱에 두 가지 헬스체크 엔드포인트를 추가하세요. "
                    "GET /health는 앱이 살아있으면 {'status': 'ok'}를 반환하고, "
                    "GET /health/ready는 DB 연결이 가능하면 {'status': 'ready', 'database': 'ok'}를, "
                    "실패하면 HTTP 503을 반환합니다."
                ),
                "hint": (
                    "@app.get('/health')는 단순히 {'status': 'ok'}를 반환합니다. "
                    "@app.get('/health/ready')는 db.execute(text('SELECT 1'))을 try/except로 감싸고, "
                    "예외 발생 시 HTTPException(status_code=503)을 raise합니다."
                ),
            },
            {
                "number": 5,
                "type": "coding",
                "question": (
                    "GitHub Actions 워크플로우를 작성하세요. "
                    "main 브랜치에 Push 시: "
                    "1) Docker Hub에 로그인하고, "
                    "2) 이미지를 빌드하여 'myuser/my-app:latest'로 Push하며, "
                    "3) SSH로 EC2에 접속하여 새 이미지를 Pull하고 컨테이너를 재시작합니다."
                ),
                "hint": (
                    "docker/login-action@v3으로 Docker Hub 로그인, "
                    "docker/build-push-action@v5으로 빌드 및 Push, "
                    "appleboy/ssh-action@v1으로 EC2 SSH 접속 후 "
                    "docker pull → docker stop → docker rm → docker run 순서로 실행합니다. "
                    "EC2_HOST, EC2_SSH_KEY는 GitHub Secrets에 저장합니다."
                ),
            },
        ],
        "challenge": {
            "question": (
                "Vol.4에서 만든 FastAPI + PostgreSQL + Docker 프로젝트를 실제 클라우드에 배포하세요. "
                "요구사항: "
                "1) AWS EC2 프리티어(t2.micro) 또는 Railway/Render에 배포합니다. "
                "2) Docker Hub 또는 ghcr.io에 이미지를 Push합니다. "
                "3) 모든 시크릿(DB URL, SECRET_KEY)은 환경 변수로 관리하며 코드에 하드코딩하지 않습니다. "
                "4) GET /health와 GET /health/ready 엔드포인트를 구현합니다. "
                "5) UptimeRobot(무료)에 /health URL을 등록하여 5분 간격 모니터링을 설정합니다. "
                "6) Sentry SDK를 연동하여 예외가 자동 수집되도록 합니다. "
                "7) 챕터 7의 GitHub Actions CI/CD와 연결하여 main Push 시 자동 배포가 이루어집니다. "
                "최종 결과물로 배포된 앱의 URL과 GitHub Actions 실행 로그를 확인하세요."
            ),
            "hint": (
                "EC2 사용 시: 보안 그룹에서 포트 80(HTTP)과 22(SSH)만 허용합니다. "
                "Docker Hub 이미지를 Pull하여 --restart unless-stopped로 실행하세요. "
                "Railway 사용 시: railway init 후 환경 변수를 Railway 대시보드에서 설정합니다. "
                "Sentry: pip install sentry-sdk[fastapi] 후 "
                "sentry_sdk.init(dsn=os.environ['SENTRY_DSN'])을 main.py에 추가합니다."
            ),
        },
        "summary": [
            "클라우드는 IaaS(EC2 등 가상 서버), PaaS(Railway 등 앱 실행 환경), SaaS(완성된 소프트웨어) 세 계층으로 분류된다.",
            "EC2 + Docker는 세밀한 제어가 필요한 MLOps 환경에, Railway/Render는 빠른 배포가 필요한 소규모 서비스에 적합하다.",
            "환경 변수와 시크릿은 .env 파일(.gitignore 필수) 또는 플랫폼 시크릿 관리 서비스로 관리하고 코드에 하드코딩하지 않는다.",
            "이미지 레지스트리(Docker Hub, ghcr.io)에 버전 태그와 latest를 함께 Push하면 추적과 롤백이 용이하다.",
            "GitHub Actions CD 파이프라인으로 main Push 시 자동으로 이미지를 빌드하고 서버에 배포할 수 있다.",
            "헬스체크 엔드포인트 + 구조화된 로깅 + UptimeRobot/Sentry 연동이 운영 환경 기본 안전망이다.",
        ],
    }
