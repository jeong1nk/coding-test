# 파이썬은 언패킹이 가능한 걸 잊지말기!
def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        s, e = parts[i]
        answer += my_strings[i][s:e+1]
    return answer