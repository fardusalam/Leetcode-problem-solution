import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    sorted_df = employee['salary'].sort_values(ascending = False)
    unique_salaries = sorted_df.unique()

    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    else:
        result = unique_salaries[1]
        return pd.DataFrame({'SecondHighestSalary' : [result]})
