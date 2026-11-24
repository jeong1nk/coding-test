def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        # stk 가 빈배열: arr[i]를 stk에 추가, i+1
        if stk == []: 
            stk.append(arr[i])
            i += 1
        else: # stk에 원소가 있고
            if stk[-1] == arr[i] : # stk의 마지막 원소 = arr[i]
                stk.pop()
                i += 1
                #stk의 마지막 원소를 stk에서 제거, i+1
            else: # stk의 마지막 원소 != arr[i]
                stk.append(arr[i])
                i += 1
                #stk의 마지막에 arr[i]를 추가, i+1

    if stk == [] : return [-1]
    return stk