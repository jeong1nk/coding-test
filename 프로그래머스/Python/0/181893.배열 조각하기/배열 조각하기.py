def solution(arr, query):
    
    for idx in range(len(query)):
        if idx % 2 == 0: # 짝수 인덱스
            arr = arr[:query[idx] + 1]
        else: #홀수 인덱스
            arr = arr[query[idx]:]
                      
    return arr