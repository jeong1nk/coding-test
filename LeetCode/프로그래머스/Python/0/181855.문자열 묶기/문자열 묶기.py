def solution(strArr):
    answer = 0
    dict_len = {}
    
    for s in strArr:
        if len(s) not in dict_len:
            dict_len[len(s)] = 1
        else:
            dict_len[len(s)] += 1
        
    answer = max(dict_len.values())
    
    return answer