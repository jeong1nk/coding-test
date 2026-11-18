def solution(sides):
    two_side = sum(sides) - max(sides)
    
    if two_side > max(sides):
        return 1
    else:
        return 2
