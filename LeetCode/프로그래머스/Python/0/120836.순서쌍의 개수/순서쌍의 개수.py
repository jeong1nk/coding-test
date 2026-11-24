def solution(n):
    measure = []
    
    for num in range(1, n+1):
        if n % num == 0:
            measure.append([num, n // num])
            
    return len(measure)

# 아래도 가능하긴 함
# def solution(n):
#     answer = 0
    
#     for num in range(1, n+1):
#         if n % num == 0:
#             answer += 1
            
#     return answer