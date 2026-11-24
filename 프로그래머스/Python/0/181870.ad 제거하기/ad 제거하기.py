# ad가 들어있는 방식으로 푼다면 뒤에서부터 remove()해야 인덱스가 꼬이지 않음
def solution(strArr):
    answer = []
    for text in strArr:
        if "ad" not in text:
            answer.append(text)
    return answer