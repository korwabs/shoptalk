<div align="center">
  <img src="docs/assets/blast_icon_only.png" width="200" height="200" alt="BLAST Logo">
</div>

<p align="center" style="font-size: 24px">A high-performance serving engine for web browsing AI.</p>

<div align="center">

[![Website](https://img.shields.io/badge/lgcns.com-A50034)](https://www.lgcns.com/)

</div>

## ❓ Use Cases

1. **I want to add web browsing AI to my app...** BLAST serves web browsing AI with an OpenAI-compatible API and concurrency and streaming baked in.
2. **I need to automate workflows...** BLAST will automatically cache and parallelize to keep costs down and enable interactive-level latencies.
3. **Just want to use this locally...** BLAST makes sure you stay under budget and not hog your computer's memory.

# BLAST Luxia 프로젝트 설정 가이드

이 문서는 BLAST Luxia 프로젝트의 의존성 설치 및 실행 환경 설정 방법을 안내합니다.

## 프로젝트 구조

BLAST Luxia 프로젝트는 Python 백엔드와 Next.js 프론트엔드로 구성되어 있습니다:
- Python 백엔드: `pyproject.toml`을 통한 의존성 관리
- Next.js 프론트엔드: `blastai/frontend` 디렉토리에 위치

## 의존성 설치 및 환경 설정

### 1. 백엔드(Python) 의존성 설치

```bash
pip install -e ".[dev]"
```

이 명령은 다음 작업을 수행합니다:
- `pyproject.toml`에 정의된 모든 필수 의존성 설치
- 개발용 추가 의존성(`dev`) 설치
- `-e` 플래그로 개발 모드 활성화 (코드 변경 사항이 바로 반영됨)

주요 의존성:
- pydantic: 데이터 검증
- browser-use: 브라우저 상호작용
- fastapi & uvicorn: API 서버
- playwright: 웹 자동화
- 기타 유틸리티 라이브러리

### 2. 프론트엔드(Next.js) 의존성 설치

```bash
cd ./blastai/frontend
npm install
```

이 명령은 `package.json`에 정의된 모든 JavaScript/TypeScript 의존성을 설치합니다.

주요 의존성:
- Next.js: React 기반 웹 프레임워크
- React: UI 라이브러리
- TailwindCSS: 스타일링
- 기타 유틸리티 라이브러리

## 애플리케이션 실행

### 백엔드 실행

```bash
blastai serve
```

이 명령은 BLAST 백엔드 서버를 시작합니다. 기본 포트는 8000입니다.

### 프론트엔드 개발 서버 실행 (선택 사항)

```bash
cd ./blastai/frontend
npm run dev
```

이 명령은 Next.js 개발 서버를 시작합니다. 기본 포트는 3000입니다.

## 간단한 사용법

README.md 파일에 따르면, 설치 후 다음과 같이 간단히 Python 클라이언트를 통해 사용할 수 있습니다:

```python
from openai import OpenAI

client = OpenAI(
    api_key="not-needed",
    base_url="http://127.0.0.1:8000"
)

# Stream real-time browser actions
stream = client.responses.create(
    model="not-needed",
    input="Compare fried chicken reviews for top 10 fast food restaurants",
    stream=True
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta if " " in event.delta else "<screenshot>", end="", flush=True)
```


## ✨ Features

- 🔄 **OpenAI-Compatible API** Drop-in replacement for OpenAI's API
- 🚄 **High Performance** Automatic parallelism and prefix caching
- 📡 **Streaming** Stream browser-augmented LLM output to users
- 📊 **Concurrency** Out-of-the-box support many users with efficient resource management

## 📄 MIT License

As it should be!
