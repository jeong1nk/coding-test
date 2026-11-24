def solution(my_string, overwrite_string, s):
    my_list = list(my_string)
    my_list[s:s+len(overwrite_string)] =  overwrite_string
    answer = "".join(my_list)
    return answer