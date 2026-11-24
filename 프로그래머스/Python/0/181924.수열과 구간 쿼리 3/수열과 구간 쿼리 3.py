# 두 변수의 값을 한 번에 교환 가능하다는 사실 잊지 말기
# arr[i],arr[j]=arr[j],arr[i] 
def solution(arr, queries):
    for i,j in queries:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr