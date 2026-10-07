def solution(code):
    ret = ''
    mode = 0
    
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = (mode + 1) % 2
        else:
            if (idx % 2 == 0) and (mode == 0):
                ret += code[idx]
            elif (idx % 2 != 0) and (mode == 1):
                ret += code[idx]
                
    return ret if ret else "EMPTY"