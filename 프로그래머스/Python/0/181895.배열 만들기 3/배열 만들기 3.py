def solution(arr, intervals):
    answer = []
    
    a, b = intervals
    
    answer += arr[a[0]:a[1]+1]
    answer += arr[b[0]:b[1]+1]
    
    return answer