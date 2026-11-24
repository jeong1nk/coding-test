def solution(rny_string):
    rny_list = list(rny_string)
    
    for i in range(len(rny_list)):
        if rny_list[i] == "m":
            rny_list[i] = "rn"
            
    rny_string = "".join(rny_list)
    
    return rny_string