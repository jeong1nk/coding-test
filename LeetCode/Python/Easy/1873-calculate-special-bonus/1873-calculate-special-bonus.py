import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    cond1 = employees['employee_id'] % 2 != 0
    cond2 = employees['name'].str[0] != 'M'

    employees['bonus'] = employees['salary'][cond1&cond2]
    employees['bonus'] = employees['bonus'].fillna(0)
    
    return employees[["employee_id", "bonus"]].sort_values(by='employee_id')
