def solution(arr):
    # while에서 빠져나오기 위해 1024도 추가
    power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    
    while len(arr) not in power:
        arr.append(0)
        
    return arr