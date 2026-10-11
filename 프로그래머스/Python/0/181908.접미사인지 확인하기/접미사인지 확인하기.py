def solution(my_string, is_suffix):
    ms_list = []
    
    for i in range(len(my_string)):
        ms_list.append(my_string[i:])
        
    if is_suffix in ms_list: return 1
    else: return 0
    