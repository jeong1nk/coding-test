def solution(arr, idx):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] == 1 and i >= idx:
            answer.append(i)
    
    if answer == []: return -1
    return min(answer)