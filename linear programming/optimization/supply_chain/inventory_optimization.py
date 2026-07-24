import scipy.stats as stats
import numpy as np
import pulp as plp
import pandas as pd
import math
"""

Manufacturing lead time -> is the time it takes for a product to be produced (raw materials to finished good)
Lead times( supplier lead time) -> time it take a supplier to transport goods to the company
lead time -> time it takes from when a customer place an order to when it is ready to be shipped 

"""
data = pd.read_csv("supply_chain_data.csv")

units_sold = data["Number of products sold"].sum()

operating_days = len(data)

lead_time_average = data["Lead times"].mean()

lead_time_standard_dev = data["Lead times"].std()

average_daily_demand = units_sold / operating_days

lead_time_demand_mean = average_daily_demand * lead_time_average

z_score = 1.96 # Z-SCORE FOR A 95% TARGET SERVICE LEVEL

reorder_point = lead_time_demand_mean + z_score * lead_time_standard_dev
"""
EOQ (ECONOMIC ORDER QUANTITY) -> USED TO DETERMINE THE IDEAL ORDER SIZE A COMPANY SHOULD PURCHASE TO MINIMIZE TOTAL INVENTORY, 
INCLUDING ORDERING ,HOLDING AND SHORTAGE COST
"""
# WE CAN USE UNITS SOLD AS ANNUAL DEMAND SINCE OUR DATASET DOES NOT HAVE THE RIGHT CHARACTERISTICS
ordering_cost = data["Shipping costs"]
data["holding cost rate"] = data["costs"] * data["price"]
EOQ = math.sqrt((2 * ordering_cost * holding_rate) / H)