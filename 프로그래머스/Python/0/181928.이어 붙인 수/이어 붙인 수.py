def solution(num_list):
    num_even = ''
    num_odd = ''
    
    for num in num_list:
        if num % 2 == 0:
            num_even += str(num)
        else:
            num_odd += str(num)
            
    return int(num_even) + int(num_odd)