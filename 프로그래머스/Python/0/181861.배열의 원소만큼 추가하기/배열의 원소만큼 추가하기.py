# append는 리스트 자체를 통째로 넣으므로 extend 사용
# extend(): 내장 함수, 각 요소들을 풀어서 하나씩 추가
def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num] * num)
    return answer