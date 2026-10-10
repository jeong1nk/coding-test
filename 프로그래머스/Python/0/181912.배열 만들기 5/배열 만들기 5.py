def solution(intStrs, k, s, l):
    answer = []
    
    for list_s in intStrs:
        val = int(list_s[s:s + l])
        if val > k:
            answer.append(val)
            
    return answer