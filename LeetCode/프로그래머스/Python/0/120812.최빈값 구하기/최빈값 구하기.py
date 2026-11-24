from collections import Counter

def solution(array):
    cnt_arr = Counter(array)
    most_num = cnt_arr.most_common()
    
    if len(most_num) > 1 and most_num[0][1] == most_num[1][1]:
        return -1

    return most_num[0][0]