def solution(age):
    answer = ''
    
    for num in str(age):
        answer += chr(97+int(num))
        
    return answer