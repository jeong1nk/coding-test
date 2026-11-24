# included: 길이가 n인 boolean 배열
# 첫째항: a, 공차: d인 등차수열(연속하는 두 항의 차이가 모두 일정한 수열)
def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        if included[i] == True:
            answer += a
        a += d

    return answer