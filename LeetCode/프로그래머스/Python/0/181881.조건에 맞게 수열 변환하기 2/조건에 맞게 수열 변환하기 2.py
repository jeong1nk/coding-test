def solution(arr):
    answer = []
    result = 0
    
    while True:
         # answer = arr 는 같은 리스트를 참조하게 되므로 주의!
        answer = arr[:]
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1

        if arr == answer:
            return result

        result += 1