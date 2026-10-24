# picture -> .와 x로 이루어짐
# 문제: 각 문자를 k배 늘림(가로) -> 문자를 k배 늘린 전체를 k배 늘림(세로)
def solution(picture, k):
    answer = []
    
    for row in picture:
        # 한 줄 전체를 for문으로 훑으며 k배씩 늘리기(가로)
        row_k = ""
        for text in row:
            row_k += text * k
        
        # 늘리기(가로)완료한 한 줄을 k배로 만듦-> 결과 리스트에 넣음
        for _ in range(k):
            answer.append(row_k)
            
    return answer