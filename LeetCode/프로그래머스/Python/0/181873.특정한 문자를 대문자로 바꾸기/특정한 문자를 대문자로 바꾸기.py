def solution(myString, alp):
    ms_list = list(myString)

    for i in range(len(ms_list)):
        if ms_list[i] == alp:
            ms_list[i] = ms_list[i].upper()

            
    return "".join(ms_list)