# week4_practice

**Ubuntu에서 Flask 웹 서버를 실행하고, 브라우저로 VM·컨테이너·Docker 요약 페이지를 확인하는 실습입니다.**

진행 순서: **내 GitHub 저장소 준비 → Ubuntu로 clone → 실행 환경 구성 → 앱 실행 → 서비스 확인**

> 학교에서 `apt`·`pip` 다운로드가 막히면 **3번의 파일·이력 확인까지** 진행합니다. 4번 이후는 다운로드 가능한 Ubuntu 환경에서 진행하거나, 다음 수업의 Codespaces에서 이어갑니다. 인증서 검증을 끄지 않습니다.

## 1. 내 GitHub 저장소 준비 — 실습 시작 전

### 방법 A. Fork (권장)

1. 브라우저에서 [교수자 저장소](https://github.com/Mok2Lee/week4_practice)를 엽니다.
2. **Fork → Create a new fork**를 선택합니다.
3. Owner를 **본인 계정**, 이름을 **week4_practice**로 지정해 생성합니다.
4. 주소가 `https://github.com/본인계정/week4_practice`인지 확인합니다.

**Fork는 GitHub에 내 저장소를 만드는 작업, clone은 저장소를 내 컴퓨터로 내려받는 작업입니다.** Fork 후에도 Ubuntu에서 clone해야 합니다.

<details>
<summary>방법 B. Clone한 프로젝트를 새 저장소로 올리기 (Fork를 사용하지 않을 때)</summary>

GitHub에서 본인 계정에 **week4_practice**라는 빈 저장소를 만듭니다. README·.gitignore·라이선스는 추가하지 않습니다.

Git이 설치되고 본인 GitHub 인증이 가능한 **Windows의 Git Bash 또는 VS Code 터미널**에서 실행합니다. `YOUR_GITHUB_ID`는 본인 GitHub 아이디로 바꿉니다.

```bash
git clone https://github.com/Mok2Lee/week4_practice.git
cd week4_practice
git remote rename origin upstream
git remote add origin https://github.com/YOUR_GITHUB_ID/week4_practice.git
git push -u origin main
git remote -v
```

`origin`은 본인 저장소, `upstream`은 교수자 저장소입니다. GitHub의 본인 저장소에 파일이 보이면 준비가 끝납니다. push 시 인증 안내가 나오면 본인 계정으로 인증합니다. GitHub 계정 비밀번호를 Git 비밀번호로 사용하지 않습니다.

</details>

## 2. Ubuntu 접속

강의자료에 따라 **VirtualBox Ubuntu 설치 → Vim 실습 → SSH 설정 → PuTTY 접속**을 완료합니다.

| 항목 | 수업의 NAT 접속 설정 |
|---|---|
| PuTTY 실행 위치 | Windows |
| Host Name / Port | `127.0.0.1` / `2222` |
| 연결 방식 | SSH |
| 로그인 계정 | Ubuntu 설치 시 만든 계정 |
| VirtualBox 포트 전달 | 호스트 `127.0.0.1:2222` → 게스트 `22` |

**이후 명령은 PuTTY로 접속한 Ubuntu 터미널에서 실행합니다.** Ubuntu 콘솔에서도 같은 명령을 사용할 수 있습니다.

## 3. 내 저장소를 Ubuntu로 clone

본인 GitHub 저장소의 **Code → HTTPS**에서 주소를 복사합니다. 아래 `YOUR_GITHUB_ID`를 본인 아이디로 바꿉니다.

```bash
cd ~
git clone https://github.com/YOUR_GITHUB_ID/week4_practice.git
cd week4_practice
ls -a
git remote -v
git status
git log --oneline -5
```

확인: `app.py`, `requirements.txt`, `templates`, `static`이 보이고, **origin이 본인 저장소 주소**여야 합니다. 폴더가 이미 있으면 clone을 반복하지 않고 기존 폴더로 이동합니다.

| 파일 | 역할 |
|---|---|
| `app.py` | 브라우저의 요청을 받아 HTML을 전달하는 Flask 앱 |
| `templates/index.html` | VM·컨테이너·Docker 요약 화면 |
| `static/style.css` | 화면의 색상·배치·글자 서식 |
| `requirements.txt` | 설치할 Python 라이브러리 목록 |

> clone은 **파일과 변경 이력**을 가져옵니다. Python 라이브러리 설치와 앱 실행은 따로 진행합니다.

## 4. Ubuntu 실행 환경 구성

Ubuntu 22.04/24.04 LTS 기준입니다. **패키지 다운로드가 가능한 환경**에서 진행합니다.

### ① Python과 기본 도구 설치

```bash
sudo apt update
sudo apt install -y python3 python3-venv git curl
python3 --version
```

Git이 없어 3번을 진행하지 못했다면 도구 설치 후 3번으로 돌아갑니다.

### ② 프로젝트 전용 Python 가상환경 생성

```bash
cd ~/week4_practice
python3 -m venv .venv
source .venv/bin/activate
```

터미널 앞에 `(.venv)`가 표시되는지 확인합니다. **.venv는 Python 라이브러리를 분리하는 폴더**이며, VirtualBox의 가상머신과는 다릅니다.

### ③ Flask 설치

```bash
python -m pip install -r requirements.txt
python -m flask --version
```

Flask 버전이 출력되면 준비가 끝납니다. `.venv`는 GitHub에 올리지 않습니다.

## 5. 앱 실행

가상환경이 활성화된 `~/week4_practice`에서 실행합니다.

```bash
python -m flask --app app run --host=0.0.0.0 --port=5000
```

`Running on ...:5000`이 나오면 서버가 실행 중입니다. **이 터미널은 열어 둡니다.** `0.0.0.0`은 접속을 받을 범위를 지정하는 값이며 브라우저에 입력하는 주소가 아닙니다. 이 서버는 수업용 개발 서버입니다.

## 6. 서비스 확인

### ① Ubuntu 안에서 확인

새 PuTTY 창으로 같은 Ubuntu에 접속하여 실행합니다.

```bash
curl -I http://127.0.0.1:5000
```

`HTTP/1.1 200 OK`가 나오면 Ubuntu 안에서 웹 요청에 정상 응답한 것입니다.

### ② Windows 브라우저에서 확인

VirtualBox **설정 → 네트워크 → NAT → 고급 → 포트 전달**에서 기존 SSH 규칙은 유지하고 아래 규칙을 추가합니다. 설정을 위해 VM을 종료했다면 부팅·접속 후 7번 명령으로 앱을 다시 실행합니다.

| 이름 | 프로토콜 | 호스트 IP | 호스트 포트 | 게스트 IP | 게스트 포트 |
|---|---|---|---|---|---|
| Flask | TCP | `127.0.0.1` | `5000` | 공란 | `5000` |

Windows 브라우저에서 [http://127.0.0.1:5000](http://127.0.0.1:5000)에 접속합니다.

- **가상머신과 컨테이너** 제목과 VM·Container·Docker 설명이 보입니다.
- 서버 터미널에 `GET / ... 200` 요청 기록이 출력됩니다.

접속 경로: **Windows 브라우저 :5000 → VirtualBox 포트 전달 → Ubuntu Flask :5000**

> Ubuntu의 `127.0.0.1`은 Ubuntu 자신, Windows의 `127.0.0.1`은 Windows 자신입니다. Windows에서 VM으로 연결하려면 위 포트 전달이 필요합니다.

## 7. 종료와 다시 실행

서버 터미널에서 **Ctrl+C**로 종료한 뒤 `deactivate`로 가상환경을 빠져나옵니다. 다음에 실행할 때는 설치를 반복하지 않습니다.

```bash
cd ~/week4_practice
source .venv/bin/activate
python -m flask --app app run --host=0.0.0.0 --port=5000
```

## 8. Vim으로 화면 문장 수정

서버를 종료하고 `vim templates/index.html`을 실행합니다. 파일 아래쪽 **나의 실습 기록** 문장을 수정한 뒤 `Esc → :wq → Enter`로 저장합니다. 앱을 다시 실행하고 브라우저를 새로고침해 변경을 확인합니다.

## 오류 확인

| 증상 | 확인할 내용 |
|---|---|
| apt·pip 인증서/다운로드 오류 | 학교에서는 설치를 멈추고 오류를 교수자에게 확인 |
| `No module named flask` | `.venv` 활성화 후 `python -m pip install -r requirements.txt` 실행 여부 |
| `Could not import 'app'` | `pwd`, `ls`로 `app.py`가 있는 폴더인지 확인 |
| Ubuntu curl 접속 실패 | Flask가 실행 중인지, 포트가 5000인지 확인 |
| Ubuntu는 200, Windows는 접속 실패 | `--host=0.0.0.0`, NAT 포트 전달, 방화벽 규칙 확인 |
| 5000 포트 사용 중 | 이전 실습 서버를 Ctrl+C로 종료; Windows의 다른 앱이 사용 중이면 호스트 포트만 5001로 바꾸고 브라우저도 `:5001` 사용 |

## 다음 수업 연결

다음 시간에는 **본인 저장소를 Codespaces에서 열고**, 같은 앱을 실행한 뒤 Dockerfile 작성 → 이미지 생성 → 컨테이너 실행으로 이어갑니다. Codespaces에는 저장소가 이미 있으므로 다시 clone하지 않습니다. `.venv` 생성·설치 후 앱을 실행하고 **Ports의 5000번 → 브라우저에서 열기**로 확인합니다. VirtualBox 포트 전달은 필요하지 않습니다.

참고: [Flask 설치](https://flask.palletsprojects.com/en/stable/installation/) · [Flask 실행](https://flask.palletsprojects.com/en/stable/quickstart/) · [GitHub Fork](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)
