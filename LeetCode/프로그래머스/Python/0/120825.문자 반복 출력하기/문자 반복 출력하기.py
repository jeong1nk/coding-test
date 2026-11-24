# 리스트 컴프리헨션: "".join([s * n for s in my_string])
def solution(my_string, n):
    answer = []
    list_ms = list(my_string)
    
    for s in list_ms:
        answer.append(s*n)
        
    return ''.join(answer)