def solution(number):
    # 각 글자를 정수(int)로 변환하여 모두 더함
    return sum(map(int, number)) % 9