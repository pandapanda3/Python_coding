# Leet Code 75: 184. Department Highest Salary
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee,department,left_on='departmentId',right_on='id',how = 'left')
    gf = df.groupby('departmentId').max()
    rf= pd.merge(left=df,right=gf,on=['salary','name_y'])
    return rf[['name_y', 'name_x_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x_x': 'Employee', 'salary': 'Salary'})


if __name__ == '__main__':
    employee_data = {'id': [1, 2, 3, 4, 5],
                     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                     'salary': [70000, 80000, 120000, 90000, 110000],
                     'departmentId': [1, 1, 2, 2, 3]}
    
    employee = pd.DataFrame(employee_data)
    
    
    department_data = {'id': [1, 2, 3],
                       'name': ['HR', 'Engineering', 'Marketing']}
    
    department = pd.DataFrame(department_data)
    result = department_highest_salary(employee,department)