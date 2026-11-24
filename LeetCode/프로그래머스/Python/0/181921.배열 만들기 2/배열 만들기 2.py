# set: 중복을 허용하지 않고 순서가 없는 데이터의 모임
# not: 파이썬에서는 비어있는 자료형을 조건문에 넣으면 False가 나오므로 not을 사용
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        # 0과 5를 제거했을 때 다른 숫자가 남아 있는지 확인
        if not set(str(i)) - {'0', '5'} :
            answer.append(i)
        
    return answer if answer else [-1]