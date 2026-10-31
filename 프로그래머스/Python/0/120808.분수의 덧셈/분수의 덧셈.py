import math

def solution(numer1, denom1, numer2, denom2):
    # 분자1 * 분모2 , 분자2 * 분모1 한 뒤 최대공약수로 나누기
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    gcd_num = math.gcd(numer, denom)
    
    return [numer // gcd_num, denom // gcd_num]
    