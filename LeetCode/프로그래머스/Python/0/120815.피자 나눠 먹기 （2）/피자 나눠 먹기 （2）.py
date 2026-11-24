import math

def solution(n):
    # 필요한 피자 조각 수: 최소공배수
    # 필요한 피자의 수: 최소공배수 // 6
    answer = (6 * n) // math.gcd(6, n)
    return answer // 6