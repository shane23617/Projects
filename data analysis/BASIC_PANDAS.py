from datetime import date
import sqlalchemy as sql
import pandas as pd


data = pd.read_csv("cleaned_data.csv")

# SEPARATING YEAR,MONTH AND DAY INTO SEPARATE COLUMNS
data['year'] = pd.to_datetime(data['date']).dt.year
data['month'] = pd.to_datetime(data['date']).dt.month
data['day'] = pd.to_datetime(data['date']).dt.day

# CALCULATION OF THE REVENUE

data['revenue'] = data['quantity']*data['unit_price']

# PRICE OF THE DISCOUNTED PRODUCTS

data["discount(/100)"] = data['discount_pct'] / 100
data.drop(columns = ["discount_pct"], inplace = True)
data["discount_amount"] = data["unit_price"] * data["discount(/100)"]
data["final_amount"] = data["unit_price"] - data["discount_amount"]

"""
ANOTHER WAY TO CALCULATE FINAL AMOUNT
data["final_amount"] = data["unit_price"] * ( 1 - data["discount(/100)"] )
"""

# SHOWING THE NUMBER OF ROWS AND COLUMN

"""
print(data.shape)
"""
# CHECKING FOR DUPLICATE TRANSACTIONS

#print(data.duplicated().any())

# TOP 10 PRODUCTS WITH HIGHEST REVENUE 

sorted_data = data.sort_values(by=["revenue", "product"], ascending = False)
#print(sorted_data.head(10).to_string())

# DATE RANGE FOR THE ENTIRE DATASET

start_date = data["date"].min()
end_date = data["date"].max()
#print(f"the date ranges from {start_date} to {end_date}")

# GETTING COLUMN NAMES AND DATA TYPES

column_datatype = data.dtypes
column_names = data.columns.tolist()
#print(f"column_names are {column_names} and the following are their datatypes {column_datatype}")

# TOTAL REVENUE

total_revenue = sum(data["unit_price"] * data["quantity"])
#print(total_revenue)

# AVERAGE SALE VALUE

average_sale_vale = total_revenue / len(data)
#print(average_sale_vale)
#] print(data.head(5).to_string())

#x = data.groupby(["order_status"])["final_amount"].sum()
print(data.head(3) .to_string())



