def solution(myString):
    target = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    list_ms = list(myString)
    
    for idx in range(len(list_ms)):
        if list_ms[idx] in target:
            list_ms[idx] = 'l'
            
    return ''.join(list_ms)