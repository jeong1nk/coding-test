def solution(money):
    cup = money // 5500
    
    return [cup, money - cup * 5500]