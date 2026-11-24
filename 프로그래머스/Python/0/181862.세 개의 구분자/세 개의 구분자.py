# split(): 구분자를 기준으로 문자열을 쪼갠다. 단, 구분자 앞뒤에 아무런 글자가 없으면 그 자리를 빈 문자열("")로 채운다.

import re
def solution(myStr):
    answer = []
    my_list = re.split(r"[abc]", myStr)

    for text in my_list:
        if text != "": answer.append(text)

    if len(answer) == 0:
        return ["EMPTY"]
    else:
        return answer