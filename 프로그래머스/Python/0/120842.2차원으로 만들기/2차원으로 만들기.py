def solution(num_list, n):
    answer = []
    cnt = 0
    
    for i in range(len(num_list) // n):
        answer.append(num_list[cnt : cnt + n])
        cnt += n 
        
    return answer