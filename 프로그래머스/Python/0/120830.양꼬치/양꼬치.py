def solution(n, k):
    price = (n * 12000) + (k * 2000)
    
    if n >= 10:
        price -= (n // 10 * 2000)
        
    return price