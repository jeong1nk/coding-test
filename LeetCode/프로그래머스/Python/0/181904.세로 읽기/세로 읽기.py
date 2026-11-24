def solution(my_string, m, c):
    ms_dict = {}
    
    for i in range(len(my_string)):
        row = i // m  # 줄
        col = i % m   # 열
        
        # 딕셔너리에 없으면 새로 만듦
        if row not in ms_dict:
            ms_dict[row] = []
            
        ms_dict[row].append(my_string[i])
    
    answer = ""
    for row in ms_dict:
        answer += ms_dict[row][c - 1]
        
    return answer