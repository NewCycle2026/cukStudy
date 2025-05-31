# pandas는 CSV 파일 불러오기에 사용
import pandas as pd

# Levenshtein 패키지는 문자열 간 레벤슈타인 거리 계산에 사용
import Levenshtein  # pip install python-Levenshtein

# CSV 파일에서 질문(Q)과 답변(A) 컬럼을 각각 리스트로 불러오는 함수
def load_data(filepath: str):
    data = pd.read_csv(filepath)               # CSV 파일 읽기
    questions = data['Q'].tolist()             # 질문 리스트
    answers = data['A'].tolist()               # 답변 리스트
    return questions, answers

# 사용자 입력과 학습된 질문 리스트 간의 레벤슈타인 거리 계산
def find_best_match(user_input: str, questions: list):
    min_distance = float('inf')                                # 최소 거리 초기값 설정
    best_index = -1                                            # 가장 유사한 질문의 인덱스
    for idx, question in enumerate(questions):                 # 모든 질문에 대해 반복
        distance = Levenshtein.distance(user_input, question)  # 거리 계산
        if distance < min_distance:                            # 더 짧은 거리 발견 시 갱신
            min_distance = distance
            best_index = idx
    return best_index                                           # 가장 유사한 질문의 인덱스 반환

# 메인 챗봇 실행 함수
def chatbot():
    questions, answers = load_data('ChatbotData.csv')            # 데이터 불러오기
    print("안녕하세요! 무엇을 도와드릴까요? (종료하려면 'exit' 입력)")  # 첫 인사
    while True:
        user_input = input("당신: ").strip()                      # 사용자 입력 받기
        if user_input.lower() == 'exit':                          # 종료 명령 처리
            print("챗봇을 종료합니다. 좋은 하루 보내세요!")
            break
        best_index = find_best_match(user_input, questions)       # 최적 매칭 질문 찾기
        if best_index != -1:
            print("챗봇:", answers[best_index])                    # 해당 답변 출력
        else:
            print("챗봇: 죄송해요, 이해하지 못했어요.")                # 매칭 실패 시 메시지

# 프로그램 실행 시 chatbot() 호출
if __name__ == "__main__":
    chatbot()

