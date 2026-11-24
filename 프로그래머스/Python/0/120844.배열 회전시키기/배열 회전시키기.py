def solution(numbers, direction):
    answer = []
    
    if direction == "right":
        answer = [numbers[-1]] + numbers[:-1]
    else: #direction == "left"
        answer = numbers[1:] + [numbers[0]]
        
    return answer