def solution(arr, queries):
    for s, e in queries:
        for i in range(len(arr)): # 범위를 s 부터 e 까지 하는 것이 더 나음
            if s <= i <= e:
                arr[i] += 1
        
    return arr