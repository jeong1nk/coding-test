def solution(emergency):
    answer = []
    # 1. 응급도 순으로 환자들을 세우기
    sorted_emergency = sorted(emergency, reverse=True)
    
    # 2. 환자들의 응급도와 순위를 딕셔너리로 저장
    rank_dict = {}
    for idx, num in enumerate(sorted_emergency, start=1):
        rank_dict[num] = idx
    
    # 3. 딕셔너리로 저장해둔 값에서 순위만 따로 저장해 반환
    for num in emergency:
        answer.append(rank_dict[num])
    
    return answer
