def solution(n):
    answer = 0
    
    
    for idx in range(1, n+1):
        cnt = 0
        for num in range(1, idx+1):
            if idx % num == 0 :
                cnt += 1
            
            if cnt > 2:
                answer += 1
                break
            
    return answer