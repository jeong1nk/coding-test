def solution(arr, k):
    answer = []
    
    for num in arr:
        # 지금까지 나온 적이 없으면 배열 맨뒤에 추가
        if num not in answer:
            answer.append(num)
        # k만큼 만들기
        if len(answer) == k:
            break
            
    # 완성될 배열의 길이가 K보다 작으면 나머지 값을 -1로 채우기       
    while len(answer) < k:
        answer.append(-1)
        
    return answer