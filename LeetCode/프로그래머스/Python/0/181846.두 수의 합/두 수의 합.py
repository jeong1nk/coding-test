def solution(a, b):
    # 계산하기 편하게 뒤집기
    a = a[::-1]
    b = b[::-1]

    answer = []
    lower_num = 0 #올림수

    # for문으로 숫자 하나씩 계산하기
    for idx in range(max(len(a), len(b))):
        # 삼항 연산자로 길이를 벗어나면 0으로 처리
        num_a = int(a[idx]) if idx < len(a) else 0
        num_b = int(b[idx]) if idx < len(b) else 0
        
        num = num_a + num_b + lower_num
                     
        # num // 10: 십의 자리(올림수),  num % 10: 일의 자리
        lower_num = num // 10
        answer.append(str(num % 10))
                     
    # for문이 끝나고 올림수가 남아 있으면 추가
    if lower_num != 0:
        answer.append(str(lower_num))
                     
    return "".join(answer[::-1])