def solution(strArr):
    answer = 0
    dict_len = {}
    
    for s in strArr:
        length = len(s)
        
        if length not in dict_len:
            dict_len[length] = 1
        else:
            dict_len[length] += 1
        
    answer = max(dict_len.values())
    
    return answer