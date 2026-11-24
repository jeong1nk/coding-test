def solution(hp):
    if hp % 5 == 0:
        return hp // 5
    
    if (hp % 5) % 3 == 0:
        return (hp // 5) + ((hp % 5) // 3)
    
    return (hp // 5) + ((hp % 5) // 3) + (hp % 5 % 3)