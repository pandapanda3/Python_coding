# Leet Code 75: 177. Nth Highest Salary

import pandas as pd
import numpy as np


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # if N <= 0:
    #     return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [np.nan]})
    
    # if N > len(salaries):
    #     return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [np.nan]})
    
    # nth_highest = salaries.iloc[N - 1]
    
    # return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [nth_highest]})
    employee = employee.drop_duplicates(subset=['salary']).sort_values(by=['salary'], ascending=False)
    result = pd.DataFrame({f'getNthHighestSalary({N})': [np.nan]})
    if N > 0 and N <= len(employee):
        result = pd.DataFrame({f'getNthHighestSalary({N})': [employee['salary'].iloc[N - 1]]})
    
    return result

