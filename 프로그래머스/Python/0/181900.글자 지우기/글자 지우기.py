def solution(my_string, indices):
    list_ms = list(my_string)
    
    for i in indices:
        # remove 사용시 인덱스가 변경되므로 공백으로 유지
        list_ms[i] = ""
        
    return "".join(list_ms)