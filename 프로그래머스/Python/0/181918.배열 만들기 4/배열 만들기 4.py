# stk[-1] >= arr[i] 인 경우에는 i에 변화없음!
def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    
    return stk