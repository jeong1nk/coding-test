def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        if flag[i] == True:
            answer += [arr[i]] * (arr[i] * 2)
        else: # flag[i] == False
            # 끝에서 부터 arr[i]개: :-arr[i]
            answer = answer[:-arr[i]]
            
    return answer
 