def solution(myString, pat):
    count = 0
    
    # pat길이 뭉텅이씩만 돌면되니까 -len(pat)+1
    for i in range(len(myString) - len(pat) + 1):
        # 문자열을 인덱스 i부터 이동하면서 pat길이 만큼 비교
        if myString[i: i+len(pat)] == pat:
            count += 1

    return count