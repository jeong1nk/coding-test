def solution(arr, delete_list):
    answer = []
    for s in arr:
        if s not in delete_list:
            answer.append(s)
    return answer