def solution(n, t):
    answer = n
    
    for hour in range(t):
        answer *= 2
        
    return answer