def solution(myString):
    ms_list = list(myString)

    for i in range(len(ms_list)):
        if ms_list[i] == "a":
            ms_list[i] = "A"
        elif ms_list[i] == "A":
            pass
        else :
            ms_list[i] = ms_list[i].lower()
            
    return "".join(ms_list)