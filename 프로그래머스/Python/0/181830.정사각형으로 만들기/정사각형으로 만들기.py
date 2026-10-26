def solution(arr):
    row = len(arr)
    column = len(arr[0])
    
    if row > column:
        for i in arr:
            while len(i) < row:
                i.append(0)
                
    elif row < column:
        while len(arr) < column:
            arr.append([0] * column)
            
    return arr