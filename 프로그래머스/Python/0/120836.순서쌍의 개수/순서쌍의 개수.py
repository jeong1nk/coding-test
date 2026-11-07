def solution(n):
    measure = []
    
    for num in range(1, n+1):
        if n % num == 0:
            measure.append([num, n // num])
            
    return len(measure)