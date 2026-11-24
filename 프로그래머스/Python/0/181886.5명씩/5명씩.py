def solution(names):
    answer = []
    
    # names[::5] 하면 좀더 간단
    for i in range(0, len(names), 5):
        answer.append(names[i])
        
    return answer