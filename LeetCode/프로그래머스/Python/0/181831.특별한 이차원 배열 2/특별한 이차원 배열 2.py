def solution(arr):
    result = 1
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                result = 0
            
    return result