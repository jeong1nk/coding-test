# set: 중복을 허용하지 않고 순서가 없는 데이터의 모임
def solution(l, r):
    answer = []
    for i in range(l, r+1): 
        # 0과 5를 제거했을 때 다른 문자가 남아 있는지 확인       
        if not (set(str(i)) - {'0', '5'}):
            answer.append(i)
        
    return answer if answer else [-1]