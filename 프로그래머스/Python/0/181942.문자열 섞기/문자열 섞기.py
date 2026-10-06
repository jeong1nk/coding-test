def solution(str1, str2):
    answer = []
    list1 = list(str1)
    list2 = list(str2)
    for i in range(len(str1)):
        answer.append(list1[i])
        answer.append(list2[i])
    return "".join(answer)