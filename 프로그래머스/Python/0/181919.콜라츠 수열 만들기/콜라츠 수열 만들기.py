# x가 짝수: x // 2
# x가 홀수: 3 * x + 1
# x가 1이 되면 종료
def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0: 
            n = n // 2
        else: 
            n = 3 * n + 1
        
        answer.append(n)
            
    return answer