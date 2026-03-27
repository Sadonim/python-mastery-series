"""
부록 B: Docker & CLI 명령어 모음
컨테이너화와 배포에 필요한 Docker, docker-compose, GitHub Actions 명령어를 한눈에 정리한다.
"""


def get_appendix():
    return {
        "title": "부록 B: Docker & CLI 명령어 모음",
        "sections": [
            _section_docker_commands(),
            _section_compose_commands(),
            _section_dockerfile_instructions(),
            _section_github_actions_keywords(),
            _section_deploy_cli(),
        ],
    }


def _section_docker_commands() -> dict:
    return {
        "title": "B.1 Docker 명령어",
        "content": [
            (
                "Docker CLI의 핵심 명령어를 이미지, 컨테이너, 볼륨, 네트워크 범주로 정리합니다. "
                "실무에서 가장 자주 사용하는 명령어 위주로 모았습니다."
            ),
            {
                "type": "table",
                "headers": ["범주", "명령어", "설명"],
                "rows": [
                    # 이미지
                    ["이미지", "docker build -t 이름:태그 .", "현재 디렉터리 Dockerfile로 이미지 빌드"],
                    ["이미지", "docker images", "로컬 이미지 목록 조회"],
                    ["이미지", "docker pull 이미지:태그", "Docker Hub에서 이미지 다운로드"],
                    ["이미지", "docker push 이미지:태그", "Docker Hub에 이미지 업로드"],
                    ["이미지", "docker rmi 이미지ID", "이미지 삭제"],
                    ["이미지", "docker image prune", "사용하지 않는 이미지 일괄 삭제"],
                    ["이미지", "docker tag 원본 새이름:태그", "이미지에 새 태그 추가"],
                    # 컨테이너
                    ["컨테이너", "docker run -p 8000:8000 이미지", "컨테이너 생성 & 실행"],
                    ["컨테이너", "docker run -d 이미지", "백그라운드(detach) 실행"],
                    ["컨테이너", "docker run --rm 이미지", "종료 시 컨테이너 자동 삭제"],
                    ["컨테이너", "docker run -e KEY=값 이미지", "환경 변수 주입"],
                    ["컨테이너", "docker ps", "실행 중인 컨테이너 목록"],
                    ["컨테이너", "docker ps -a", "모든 컨테이너 목록 (중지 포함)"],
                    ["컨테이너", "docker stop 컨테이너ID", "컨테이너 정상 종료 (SIGTERM)"],
                    ["컨테이너", "docker kill 컨테이너ID", "컨테이너 강제 종료 (SIGKILL)"],
                    ["컨테이너", "docker rm 컨테이너ID", "컨테이너 삭제 (중지 후 가능)"],
                    ["컨테이너", "docker logs 컨테이너ID", "컨테이너 로그 출력"],
                    ["컨테이너", "docker logs -f 컨테이너ID", "로그 실시간 스트리밍"],
                    ["컨테이너", "docker exec -it 컨테이너ID bash", "실행 중 컨테이너 내부 접속"],
                    ["컨테이너", "docker inspect 컨테이너ID", "컨테이너 상세 정보 (JSON)"],
                    # 볼륨
                    ["볼륨", "docker volume create 이름", "이름있는 볼륨 생성"],
                    ["볼륨", "docker volume ls", "볼륨 목록 조회"],
                    ["볼륨", "docker volume rm 이름", "볼륨 삭제"],
                    ["볼륨", "docker run -v 볼륨명:/경로 이미지", "볼륨 마운트"],
                    ["볼륨", "docker run -v /호스트:/컨테이너 이미지", "호스트 디렉터리 마운트"],
                    # 네트워크
                    ["네트워크", "docker network create 이름", "사용자 정의 네트워크 생성"],
                    ["네트워크", "docker network ls", "네트워크 목록 조회"],
                    ["네트워크", "docker network connect 네트워크 컨테이너", "컨테이너를 네트워크에 연결"],
                ],
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 실전 자주 쓰는 패턴\n"
                    "\n"
                    "# 빌드 & 즉시 실행 (개발 중 빠른 확인)\n"
                    "docker build -t todo-api:dev . && docker run --rm -p 8000:8000 todo-api:dev\n"
                    "\n"
                    "# 환경 변수 파일로 실행\n"
                    "docker run --env-file .env -p 8000:8000 todo-api:latest\n"
                    "\n"
                    "# 실행 중인 컨테이너에서 명령 실행 (디버깅)\n"
                    "docker exec -it $(docker ps -q --filter name=todo) bash\n"
                    "\n"
                    "# 사용하지 않는 이미지/컨테이너 정리 (디스크 공간 확보)\n"
                    "docker system prune -f\n"
                    "\n"
                    "# 이미지 레이어 내역 확인\n"
                    "docker history todo-api:latest\n"
                ),
            },
        ],
    }


def _section_compose_commands() -> dict:
    return {
        "title": "B.2 docker-compose 명령어",
        "content": [
            (
                "docker-compose는 여러 컨테이너를 하나의 YAML 파일로 정의하고 "
                "함께 관리하는 도구입니다. 로컬 개발 환경 구성에 주로 사용합니다."
            ),
            {
                "type": "table",
                "headers": ["명령어", "설명", "주요 옵션"],
                "rows": [
                    ["docker compose up", "서비스 시작 (없으면 빌드)", "--build, -d (백그라운드)"],
                    ["docker compose up --build", "이미지 다시 빌드 후 시작", "소스 변경 후 반드시 사용"],
                    ["docker compose down", "서비스 중지 & 컨테이너 삭제", "-v (볼륨도 삭제)"],
                    ["docker compose start", "중지된 컨테이너 시작", "빌드 없이 재시작"],
                    ["docker compose stop", "서비스 중지 (컨테이너 유지)", ""],
                    ["docker compose restart", "서비스 재시작", "설정 변경 시 사용"],
                    ["docker compose ps", "서비스 상태 확인", ""],
                    ["docker compose logs", "서비스 로그 출력", "-f (실시간), 서비스명"],
                    ["docker compose exec 서비스 cmd", "실행 중 서비스에서 명령 실행", "exec api bash"],
                    ["docker compose run 서비스 cmd", "새 컨테이너에서 명령 실행", "--rm 자동 삭제"],
                    ["docker compose build", "이미지만 빌드 (시작 안 함)", "--no-cache"],
                    ["docker compose config", "설정 파일 유효성 검사 & 출력", ""],
                    ["docker compose pull", "서비스 이미지 최신 버전으로 갱신", ""],
                ],
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 개발 워크플로우 예시\n"
                    "\n"
                    "# 처음 시작 (빌드 + 백그라운드 실행)\n"
                    "docker compose up --build -d\n"
                    "\n"
                    "# 로그 실시간 확인 (api 서비스만)\n"
                    "docker compose logs -f api\n"
                    "\n"
                    "# 소스 코드 변경 후 재빌드\n"
                    "docker compose up --build api\n"
                    "\n"
                    "# DB 마이그레이션 실행 (임시 컨테이너)\n"
                    "docker compose run --rm api python -m alembic upgrade head\n"
                    "\n"
                    "# 테스트 실행 (임시 컨테이너, 완료 후 자동 삭제)\n"
                    "docker compose run --rm api pytest tests/ -v\n"
                    "\n"
                    "# 전체 정리 (볼륨까지 삭제 — 주의!)\n"
                    "docker compose down -v\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "Docker Compose v2(docker compose)는 v1(docker-compose)과 달리 "
                    "Go로 재작성되어 Docker CLI에 통합되었습니다. "
                    "2023년 이후 배포된 Docker Desktop은 v2가 기본입니다. "
                    "스크립트 작성 시 둘 다 지원하려면 버전을 확인하세요."
                ),
            },
        ],
    }


def _section_dockerfile_instructions() -> dict:
    return {
        "title": "B.3 Dockerfile 지시어",
        "content": [
            (
                "Dockerfile은 Docker 이미지를 만드는 설계도입니다. "
                "각 지시어는 이미지 레이어를 하나씩 추가합니다. "
                "레이어 수가 적을수록 이미지가 가볍습니다."
            ),
            {
                "type": "table",
                "headers": ["지시어", "설명", "예시"],
                "rows": [
                    ["FROM 이미지:태그", "베이스 이미지 지정 (필수, 첫 줄)", "FROM python:3.12-slim"],
                    ["WORKDIR /경로", "작업 디렉터리 설정 (없으면 생성)", "WORKDIR /app"],
                    ["COPY 소스 목적지", "호스트 파일을 이미지로 복사", "COPY requirements.txt ."],
                    ["ADD 소스 목적지", "COPY + URL/tar 압축 해제 지원", "COPY 사용 권장 (명시적)"],
                    ["RUN 명령어", "이미지 빌드 시 명령 실행 (레이어 생성)", "RUN pip install -r requirements.txt"],
                    ["ENV KEY=값", "환경 변수 설정 (빌드 & 실행 시 모두)", "ENV PYTHONDONTWRITEBYTECODE=1"],
                    ["ARG 이름=기본값", "빌드 시에만 사용되는 변수", "ARG APP_VERSION=1.0.0"],
                    ["EXPOSE 포트", "컨테이너 리슨 포트 문서화 (실제 개방은 -p 옵션)", "EXPOSE 8000"],
                    ["VOLUME /경로", "마운트 포인트 선언", "VOLUME /app/data"],
                    ["USER 사용자", "이후 명령을 실행할 사용자 (보안)", "USER nobody"],
                    ["HEALTHCHECK", "컨테이너 건강 상태 확인 명령 정의", "HEALTHCHECK CMD curl -f http://localhost/health"],
                    ["CMD [명령, 인수]", "컨테이너 기본 실행 명령 (덮어쓰기 가능)", "CMD [\"uvicorn\", \"app.main:app\"]"],
                    ["ENTRYPOINT [명령]", "컨테이너 고정 실행 명령 (덮어쓰기 불가)", "ENTRYPOINT [\"python\"]"],
                    ["LABEL key=값", "이미지 메타데이터 추가", "LABEL maintainer=\"dev@example.com\""],
                ],
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# Python 프로젝트용 최적화 Dockerfile 전체 예시\n"
                    "FROM python:3.12-slim\n"
                    "\n"
                    "# 메타데이터\n"
                    "LABEL maintainer=\"dev@example.com\"\n"
                    "\n"
                    "# Python 최적화 환경 변수\n"
                    "ENV PYTHONDONTWRITEBYTECODE=1 \\\n"
                    "    PYTHONUNBUFFERED=1\n"
                    "\n"
                    "WORKDIR /app\n"
                    "\n"
                    "# 의존성 먼저 (캐시 활용)\n"
                    "COPY requirements.txt .\n"
                    "RUN pip install --no-cache-dir -r requirements.txt\n"
                    "\n"
                    "# 소스 코드 복사\n"
                    "COPY app/ ./app/\n"
                    "\n"
                    "# 비루트 사용자로 실행 (보안 강화)\n"
                    "RUN adduser --disabled-password --gecos '' appuser\n"
                    "USER appuser\n"
                    "\n"
                    "EXPOSE 8000\n"
                    "\n"
                    "HEALTHCHECK --interval=30s --timeout=10s \\\n"
                    "  CMD python -c \"import urllib.request; urllib.request.urlopen('http://localhost:8000/health')\"\n"
                    "\n"
                    "CMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n"
                ),
            },
            {
                "type": "note",
                "text": (
                    "CMD vs ENTRYPOINT: CMD는 docker run 실행 시 덮어쓸 수 있고, "
                    "ENTRYPOINT는 고정됩니다. "
                    "ENTRYPOINT [\"python\"] + CMD [\"app.py\"]로 조합하면 "
                    "docker run 이미지 다른스크립트.py 처럼 스크립트만 교체할 수 있습니다."
                ),
            },
        ],
    }


def _section_github_actions_keywords() -> dict:
    return {
        "title": "B.4 GitHub Actions YAML 주요 키워드",
        "content": [
            (
                "GitHub Actions 워크플로우는 YAML 파일로 정의합니다. "
                "주요 키워드와 역할을 정리합니다."
            ),
            {
                "type": "table",
                "headers": ["키워드", "역할", "예시 / 설명"],
                "rows": [
                    ["name", "워크플로우 이름", "name: CI"],
                    ["on", "트리거 이벤트 정의", "on: push, pull_request"],
                    ["on.push.branches", "Push 시 대상 브랜치", "branches: [main, develop]"],
                    ["on.pull_request", "PR 이벤트 트리거", "branches: [main]"],
                    ["on.schedule", "스케줄 실행 (cron)", "cron: '0 9 * * 1' — 매주 월 오전 9시"],
                    ["jobs", "병렬 실행 작업 그룹", "jobs: test:, build:"],
                    ["jobs.runs-on", "실행 환경 (OS)", "ubuntu-latest, windows-latest, macos-latest"],
                    ["jobs.needs", "선행 작업 완료 후 실행", "needs: test — test 완료 후 시작"],
                    ["jobs.steps", "순차 실행 단계 목록", "steps: - name: ..."],
                    ["steps.uses", "공개 Action 사용", "uses: actions/checkout@v4"],
                    ["steps.run", "쉘 명령어 실행", "run: pytest tests/ -v"],
                    ["steps.with", "Action 입력 파라미터", "with: python-version: '3.12'"],
                    ["steps.env", "스텝 환경 변수", "env: SECRET_KEY: ${{ secrets.KEY }}"],
                    ["steps.if", "조건부 실행", "if: always() — 이전 실패와 무관하게"],
                    ["secrets.KEY", "저장소 시크릿 참조", "secrets.DOCKER_TOKEN"],
                    ["env (job/step)", "환경 변수 설정", "env: DATABASE_URL: sqlite:///test.db"],
                    ["strategy.matrix", "매트릭스 빌드", "python-version: ['3.11', '3.12']"],
                    ["artifacts", "빌드 산출물 업로드/다운로드", "actions/upload-artifact@v4"],
                ],
            },
            {
                "type": "code",
                "language": "yaml",
                "code": (
                    "# GitHub Actions 워크플로우 전체 구조 예시\n"
                    "name: CI/CD Pipeline\n"
                    "\n"
                    "on:\n"
                    "  push:\n"
                    "    branches: [main]\n"
                    "  pull_request:\n"
                    "    branches: [main]\n"
                    "\n"
                    "jobs:\n"
                    "  test:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    strategy:\n"
                    "      matrix:\n"
                    "        python-version: ['3.11', '3.12']   # 두 버전에서 동시 테스트\n"
                    "    steps:\n"
                    "      - uses: actions/checkout@v4\n"
                    "      - uses: actions/setup-python@v5\n"
                    "        with:\n"
                    "          python-version: ${{ matrix.python-version }}\n"
                    "          cache: 'pip'\n"
                    "      - run: pip install -r requirements.txt\n"
                    "      - run: pytest tests/ --cov=app --cov-fail-under=80\n"
                    "\n"
                    "  deploy:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    needs: test             # test 완료 후에만 실행\n"
                    "    if: github.ref == 'refs/heads/main'   # main 브랜치만\n"
                    "    steps:\n"
                    "      - uses: actions/checkout@v4\n"
                    "      - name: Docker 이미지 빌드 & 푸시\n"
                    "        env:\n"
                    "          DOCKER_TOKEN: ${{ secrets.DOCKER_TOKEN }}\n"
                    "        run: |\n"
                    "          echo $DOCKER_TOKEN | docker login -u myuser --password-stdin\n"
                    "          docker build -t myuser/todo-api:latest .\n"
                    "          docker push myuser/todo-api:latest\n"
                ),
            },
        ],
    }


def _section_deploy_cli() -> dict:
    return {
        "title": "B.5 배포 관련 CLI 명령어 모음",
        "content": [
            (
                "배포 파이프라인에서 자주 사용하는 CLI 명령어를 정리합니다. "
                "로컬 테스트부터 클라우드 배포까지의 흐름입니다."
            ),
            {
                "type": "table",
                "headers": ["도구", "명령어", "설명"],
                "rows": [
                    # uvicorn
                    ["uvicorn", "uvicorn app.main:app --reload", "개발 서버 (자동 재시작)"],
                    ["uvicorn", "uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4", "프로덕션 서버"],
                    # pip
                    ["pip", "pip install -r requirements.txt", "의존성 설치"],
                    ["pip", "pip freeze > requirements.txt", "현재 환경 의존성 저장"],
                    ["pip", "pip list --outdated", "업데이트 가능한 패키지 확인"],
                    # pytest
                    ["pytest", "pytest tests/ -v", "상세 테스트 실행"],
                    ["pytest", "pytest tests/ --cov=app --cov-report=html", "HTML 커버리지 리포트"],
                    ["pytest", "pytest tests/ -x", "첫 번째 실패 시 즉시 중단"],
                    ["pytest", "pytest tests/ -k 'test_create'", "이름 패턴으로 테스트 필터"],
                    # git
                    ["git", "git tag v1.0.0 && git push --tags", "릴리즈 태그 생성 & 푸시"],
                    ["git", "git log --oneline --graph", "커밋 히스토리 그래프 출력"],
                    # curl
                    ["curl", "curl -s http://localhost:8000/health | python -m json.tool", "헬스체크 & JSON 포맷 출력"],
                    ["curl", "curl -X POST ... -v", "-v 옵션으로 헤더까지 출력"],
                    # httpie (curl 대안)
                    ["httpie", "http POST localhost:8000/todos/ title='공부'", "curl보다 직관적인 HTTP 클라이언트"],
                ],
            },
            {
                "type": "code",
                "language": "bash",
                "code": (
                    "# 배포 전 체크리스트 자동화 스크립트 예시\n"
                    "#!/bin/bash\n"
                    "set -e   # 오류 발생 시 즉시 중단\n"
                    "\n"
                    "echo '=== 1. 테스트 실행 ==='\n"
                    "pytest tests/ -v --cov=app --cov-fail-under=80\n"
                    "\n"
                    "echo '=== 2. Docker 이미지 빌드 ==='\n"
                    "docker build -t todo-api:$(git rev-parse --short HEAD) .\n"
                    "\n"
                    "echo '=== 3. 헬스체크 확인 ==='\n"
                    "docker run -d --name todo-test -p 18000:8000 todo-api:latest\n"
                    "sleep 3\n"
                    "curl -sf http://localhost:18000/health && echo 'Health OK'\n"
                    "docker stop todo-test && docker rm todo-test\n"
                    "\n"
                    "echo '=== 배포 준비 완료! ==='\n"
                ),
            },
            {
                "type": "tip",
                "text": (
                    "httpie(pip install httpie)는 curl보다 읽기 편한 HTTP 클라이언트입니다. "
                    "'http POST localhost:8000/todos/ title=공부하기'처럼 "
                    "Content-Type 헤더 없이도 JSON 요청을 보낼 수 있어 "
                    "개발 중 API 테스트에 매우 편리합니다."
                ),
            },
        ],
    }
