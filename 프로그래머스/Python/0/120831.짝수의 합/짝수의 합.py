def solution(n):
    answer = 0
    
    #range(2, n+1, 2) 하면 조금 더 깔끔
    for num in range(1, n + 1):
        if num % 2 == 0:
            answer += num
    
    return answer