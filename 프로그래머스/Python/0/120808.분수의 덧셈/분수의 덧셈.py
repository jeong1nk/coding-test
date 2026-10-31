import math

def solution(numer1, denom1, numer2, denom2):
    # 분자1 * 분모2 , 분자2 * 분모1 한 뒤 최대공약수로 나누기
    denom = denom1 * denom2
    num = numer1 * denom2 + numer2 * denom1
    
    denom_gcd = math.gcd(num, denom)
    
    return [num // denom_gcd, denom // denom_gcd]
    