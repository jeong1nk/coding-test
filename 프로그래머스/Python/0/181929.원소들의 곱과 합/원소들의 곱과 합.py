def solution(num_list):
    numx = 1 # 곱해야 하니까
    nump = 0
    
    for n in num_list:
        numx *= n
        nump += n
        
    if numx < (nump ** 2):
        return 1
    else:
        return 0