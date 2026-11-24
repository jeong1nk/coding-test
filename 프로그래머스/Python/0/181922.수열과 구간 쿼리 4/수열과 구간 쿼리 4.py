def solution(arr, queries):
    # 문제에 0도 포함되어 있으므로 k=0일 경우 예외처리가 필요
    for s, e, k in queries:
        if k == 0:
            continue
            
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
                
    return arr