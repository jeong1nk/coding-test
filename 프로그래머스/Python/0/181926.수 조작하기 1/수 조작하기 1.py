def solution(n, control):
    # for i in range(len(control)):
    #     if control[i] == "w": n += 1
    #     elif control[i] == "s": n -= 1
    #     elif control[i] == "d": n += 10
    #     else: n -= 10
    
    # 딕셔너리 사용시 좀 더 깔끔
    con = {"w":1, "s":-1, "d":10, "a":-10}
    for i in control:
        n += con[i]
    return n