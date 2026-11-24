# 1. i : arr 인덱스의 위치 번호,
# 2. s <= i <= e : arr[s] 부터 arr[e] 까지 중에
# 3. k 보다 크면서 가장 작은 값
def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        temp = []
        for i in range(s, e + 1):
            # k보다 크면서 가장 작은 arr[i] 값 저장
            if arr[i] > k:
                temp.append(arr[i])
            
        if temp == []:
            # 쿼리의 답이 존재하지 않으면 -1을 저장
            result.append(-1)
        else:
            result.append(min(temp))
    
    return result