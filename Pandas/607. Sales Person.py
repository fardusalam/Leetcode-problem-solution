import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # getting "RED" company Id from company table
    red_com_id = company.loc[company['name'] == 'RED', 'com_id']
    
    if red_com_id.empty:
        return sales_person[['name']]

    red_com_id = red_com_id.iloc[0]
    #getting 'sales_id' from orders table where 'com_id' matches 'RED' company
    sale_id = orders.loc[orders['com_id'] == red_com_id, 'sales_id'].tolist()

    #filtering salespersons who have not made any sales
    no_sales_person = sales_person[~sales_person['sales_id'].isin(sale_id)]
    
    return no_sales_person[['name']]