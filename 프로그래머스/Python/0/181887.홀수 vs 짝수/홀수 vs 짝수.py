def solution(num_list):
    even = 0
    odd = 0
    
    for i in range(len(num_list)):
        if (i+1) % 2 == 0: # 짝수 번째
            even += num_list[i]
        else: # 홀수 번째
            odd += num_list[i]
            
    return max(even, odd)