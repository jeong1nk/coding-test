# 알파벳 전체를 사용해야 하는 경우: 아스키 코드 + ord()를 사용
# 아스키 코드 A~Z: 65~90, 아스키 코드 a~z: 97~122
# 배열 인덱스 A~Z: 0~25,  a~z: 26~51
def solution(my_string):
    answer = [0] * 52
    
    for text in my_string:
        if 65 <= ord(text) <= 90:
            answer[ord(text) - 65] += 1
        elif 97 <= ord(text) <= 122:
            answer[ord(text) - 71] += 1 # 65 + 26
            
    return answer