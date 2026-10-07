def solution(num_list):
    numx = 1 # 곱해야 하니까

    for n in num_list:
        numx *= n
        
    if numx < (sum(num_list) ** 2):
        return 1
    else:
        return 0