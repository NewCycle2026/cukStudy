# 🎓 AI 개발 실무 2차 과제 - 레벤슈타인 거리 기반 챗봇

> 사용자 입력 문장과 학습 데이터 간 **레벤슈타인 거리(문자 편집 거리)** 를 계산하여  
> 가장 유사한 질문을 찾아 적절한 답변을 출력하는 한국어 챗봇입니다.

---

## 📂 프로젝트 개요

- 기존 TF-IDF + 코사인 유사도 챗봇의 구조를 변형
- 거리 기반 유사도 측정 방식으로 **레벤슈타인 거리**를 사용
- 질문-답변 학습 데이터셋은 공개된 `ChatbotData.csv` 활용

---

## 📚 데이터셋 정보

- 파일명: `ChatbotData.csv`

---

## 🛠️ 실행 환경

- Python 3.12+
- Ubuntu 22.04 (VirtualBox)
- VSCode Remote-SSH 또는 터미널 환경

---

## 📦 설치 및 실행

### 1. 가상환경 생성 및 패키지 설치

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
