def solution(rank, attendance):
    answer = []
    result = 0
    
    for i in range(len(rank)):
        if attendance[i] == True:
            # rank[i]: 등수, i: 학생번호
            answer.append((rank[i], i))
    
    answer.sort()
    
    result = 10000 * answer[0][1] + 100 * answer[1][1] + answer[2][1]
    return result