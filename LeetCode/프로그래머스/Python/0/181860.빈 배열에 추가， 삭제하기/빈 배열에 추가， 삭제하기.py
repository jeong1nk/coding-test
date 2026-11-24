def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        if flag[i] == True:
            answer += [arr[i]] * (arr[i] * 2)
        else: # flag[i] == False
            # 끝에서 부터 arr[i]개: :-arr[i] 사용하면 조금 더 간단
             for _ in range(arr[i]):
                answer.pop()
            
    return answer
 