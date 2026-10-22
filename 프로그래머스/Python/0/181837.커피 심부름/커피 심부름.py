def solution(order):
    answer = 0
    
    for menu in order:
        # americano 가 있으면 or anything 이면 +4500원
        if ("americano" in menu) or (menu == "anything"):
            answer += 4500
        else: # cafelatte 가 있으면 +5000원
            answer += 5000
            
    return answer
