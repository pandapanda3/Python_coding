import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age','name'])
    return df

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # row, col = players.shape
    # return [row, col]
    print(f'{type(players.shape)}')
    return list(players.shape)

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees.head(3)
    # return employees[0:3]
    return employees.iloc[:3, :]

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df1 = students[students['student_id'] == 1]
    df2 = students[students['student_id'] == 1][['name', 'age']]
    print(df1)
    print(df2)
    
    # return students.loc[students["student_id"] == 101, ["name", "age"]]
    # #OR
    # return students.loc[students["student_id"] == 101, "name" :]
    #OR
    return students[students['student_id'] == 1][['name', 'age']]

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    # return employees.assign(bonus=2 * employees['salary'])
    return employees

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # return customers.drop_duplicates(subset=['email']) or
    return customers.drop_duplicates(subset='email')

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees
    # return employees.assign(salary=2 * employees['salary'])

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id": "student_id", "first": "first_name", "last": "last_name", "age": "age_in_years"})

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students[['grade']].astype(int)
    return students
    # return students.astype({'grade': 'int'})

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"].fillna(0, inplace = True)
    return products


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather=weather.pivot(index='month', columns='city', values='temperature')
    return weather

def pivotTest() -> pd.DataFrame:
    df = pd.DataFrame({'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso', 'ElPaso','ElPaso','ElPaso'],'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],'temperature': [13, 23, 34, 43, 52, 16,23,34,23,12],'animals': ['roster', 'panda', 'panda', 'duck', 'duck', 'roster', 'duck', 'duck', 'panda', 'roster']})
    df1 = df.pivot(index='month', columns='city', values='temperature')
    df3 = df.pivot(index='month', columns='city', values=['temperature','animals'])
    df2 = df.pivot(index='month', columns='city')['temperature']
    print(df1)
    print(df2)
    print(df3)
    
def meltTable() -> pd.DataFrame:
    data = {
        'product': ['A', 'B', 'C'],
        'Q1': [100, 150, 200],
        'Q2': [110, 160, 210],
        'Q3': [120, 170, 220],
        'Q4': [130, 180, 230]
    }
    
    report = pd.DataFrame(data)
    print(f'The original report: \n{report}')
    
    report=report.melt(id_vars=['product'],var_name='quarter',value_name='sales')
    print(f'The melt report: \n{report}')
    return report


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Dot Notation: (world.population) is shorter and more concise but has limitations. It can only be used when the column name is a valid Python identifier (e.g., no spaces, no special characters, not a Python keyword)
    # return world[(world.population >= 25000000) | (world.area  >= 3000000)].filter(items=['name', 'population', 'area'])
    # Bracket Notation: (world['population']) is more flexible and can handle column names that contain spaces, special characters, or conflict with Python keywords. It is also the standard syntax when programmatically accessing columns.
    return world[(world['area'] >= 3000000) | (world['population'] >= 25000000)][['name', 'population', 'area']]

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats']=='Y') & (products['recyclable']=='Y')][['product_id']]

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # df = customers[~customers['id'].isin(orders['customerId'])][['name']]
    # df = df.rename(columns={'name': 'Customers'})
    # return df

    # new dataframe created by merging customers and orders
    newDF = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left')

    # selecting the rows where customerId is null
    newDF = newDF[newDF['customerId'].isna()]

    # returning the names of the customers in a renamed column
    return newDF[['name']].rename(columns={'name':'Customers'})


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]
    # turn to a list
    df = sorted(df['author_id'].unique(), reverse=False)
    # return back to a DataFrame
    result_df = pd.DataFrame({'id': df})
    return result_df

if __name__ == '__main__':
    # student_data = [[1,15,'ROSA'],[2,11,'jack'],[3,11,'peggy'],[4,20,'panda']]
    # student_df=createDataframe(student_data)
    # getDataframeSize(student_df)
    # selectData(student_df)
    # pivotTest()
    meltTable()