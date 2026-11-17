def solution(my_string):
    vowel = ["a", "e", "i", "o", "u"]
    for char in vowel:
        my_string = my_string.replace(char, "")
        
    return my_string