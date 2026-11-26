import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    cond = r"(^|\s)DIAB1"
    patients = patients[patients['conditions'].str.contains(cond)]

    return patients