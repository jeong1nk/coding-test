import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # 1. 도메인 있어야 하고 '@leetcode.com'
    # 2. 접두사 이름은 반드시 문자로 시작
    # 3. 허용 기호는 대문자 또는 소문자, 숫자, 밑줄 '_', 마침표 '.', 하이픈 '-'

    cond = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"
    users = users[users['mail'].str.match(cond)]
    
    return users