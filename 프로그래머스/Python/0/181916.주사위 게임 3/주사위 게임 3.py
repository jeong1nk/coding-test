# 네 숫자 같음 p: 1111 × p점
# 세 숫자가 p, 한 숫자가 q: (10 × p + q)2 점
# 두 개씩 같은 값 p, q: (p + q) × |p - q|점
# 두 숫자가 p, 나머지 두 숫자가 각각 q, r: q × r점
# 네 주사위에 적힌 숫자가 모두 다름: 나온 숫자 중 가장 작은 숫자

def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    
    # 1. 네 숫자가 모두 같음
    if dice[0] == dice[3]:
        return 1111 * dice[0]
        
    # 2. 세 숫자가 같음
    elif dice[0] == dice[2]: # 앞 3개가 p, 마지막이 q
        return (10 * dice[0] + dice[3]) ** 2
    elif dice[1] == dice[3]: # 뒤 3개가 p, 첫 번째가 q
        return (10 * dice[3] + dice[0]) ** 2
        
    # 3. 두 개씩 같음
    elif dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0] + dice[2]) * abs(dice[0] - dice[2])
        
    # 4. 두 개만 같고 나머지 두 개는 각각 다름
    elif dice[0] == dice[1]: # dice[0]이 p, 나머지 q=dice[2], r=dice[3]
        return dice[2] * dice[3]
    elif dice[1] == dice[2]: # dice[1]이 p, 나머지 q=dice[0], r=dice[3]
        return dice[0] * dice[3]
    elif dice[2] == dice[3]: # dice[2]가 p, 나머지 q=dice[0], r=dice[1]
        return dice[0] * dice[1]
        
    # 5. 네 숫자가 모두 다름
    else:
        return dice[0]