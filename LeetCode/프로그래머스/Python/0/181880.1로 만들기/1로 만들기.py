def solution(num_list):
    count = 0
    
    while True:
        for i in range(len(num_list)):
            if num_list.count(1) == len(num_list):
                return count
            elif num_list[i]  == 1:
                continue 

            if num_list[i] % 2 == 0:
                num_list[i] //= 2
                count += 1
            else: # 홀수
                num_list[i] = (num_list[i] - 1) // 2
                count += 1
            
        