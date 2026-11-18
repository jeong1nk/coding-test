#swapcase() 사용해도 OK
def solution(my_string):
    answer = ''
    
    for char in my_string:
        if ord(char) >= 97 and ord(char) <= 122:
            answer += char.upper()
        else:
            answer += char.lower()
            
    return answer