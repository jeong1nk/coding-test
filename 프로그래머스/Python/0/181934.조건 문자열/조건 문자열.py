# eval(): 문자열 형태의 식을 실행, 보안 이슈로 사용 지양
def solution(ineq, eq, n, m):

    if ineq == ">":
        return int(n >= m) if eq == "=" else int(n > m)
    else:
        return int(n <= m) if eq == "=" else int(n < m)