def solution(arr):
    row = len(arr)
    column = len(arr[0])
    
    if row > column:
        for x in arr:
            x.extend([0] * (row - column))
                
    elif row < column:
        # for 문 안에서 안쓰이면 _ 로 해도 OK
        for y in range(column - row):
            arr.append([0] * column)
            
    return arr