def solution(myString):
    answer = []
    ms_list = myString.split("x")
    
    for i in range(len(ms_list)):
        if ms_list[i] != "" : answer.append(ms_list[i])

    return sorted(answer)