# 1. 네 숫자가 같음 p: 1111 × p점
# 2. 세 숫자가 같음 p, 한 숫자가 q: (10 × p + q)2 점
# 3. 두 숫자씩 같은 값 p, q: (p + q) × |p - q|점
# 4. 두 숫자가 같음 p, 나머지 두 숫자 다름 q, r: q × r점
# 5. 네 숫자 다 다름: 가장 작은 숫자

def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    
    # 1. 네 숫자가 다 같음
    if dice[0] == dice[3]:
        return 1111 * dice[0]
        
    # 2. 세 숫자가 같음
    elif dice[0] == dice[2]: # dice[0][1][2] p, dice[3] q
        return (10 * dice[0] + dice[3]) ** 2
    elif dice[1] == dice[3]: # dice[1][2][3] p, dice[0] q
        return (10 * dice[3] + dice[0]) ** 2
        
    # 3. 두 개씩 같음
    elif dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0] + dice[2]) * abs(dice[0] - dice[2])
        
    # 4. 두 개만 같고 나머지 두 개는 각각 다름
    elif dice[0] == dice[1]: # dice[0] = p, dice[2] = q, dice[3] = r
        return dice[2] * dice[3]
    elif dice[1] == dice[2]: # dice[1] = p, dice[0] = q, dice[3] = r
        return dice[0] * dice[3]
    elif dice[2] == dice[3]: # dice[2] = p, dice[0] = q, dice[1] = r
        return dice[0] * dice[1]
        
    # 5. 네 숫자가 다 다름
    else:
        return dice[0]