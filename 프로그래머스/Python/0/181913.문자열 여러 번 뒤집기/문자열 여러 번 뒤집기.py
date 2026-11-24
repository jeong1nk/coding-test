def solution(my_string, queries):
    list_ms = list(my_string)
    
    for s, e in queries:
        # list[::-1]: 역순
        list_ms[s:e + 1] = list_ms[s:e + 1][::-1]
        
    return "".join(list_ms)