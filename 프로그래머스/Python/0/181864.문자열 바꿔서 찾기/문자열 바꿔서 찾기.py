def solution(myString, pat):
    ms_list = list(myString)
    
    for i in range(len(ms_list)):
        if ms_list[i] == "A":
            ms_list[i] = "B"
        else:
            ms_list[i] = "A"
            
    myString = "".join(ms_list)
    if pat in myString: 
        return 1
    else: 
        return 0
