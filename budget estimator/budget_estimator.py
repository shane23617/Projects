"""
 the aim of the project is to distribute monthly income across different expenses which are the following:
 RENT, GROCERY, EMERGENCY, TOILETRIES, SAVINGS,POCKET MONEY AND AN INVESTMENT ACCOUNT
 
 RENT IS FIXED, SAVINGS IS FIXED, INVESTMENT IS FIXED, ALL THE OTHER EXPENSES FLUCTUATE
 
 GOALS:
 MAXIMIZE SAVINGS ACCOUNT
 MINIMIZE SPENDING MONEY BUT MAXIMIZE SATISFACTION
 VARIABLES:
 X1 = RENT
 X2 = GROCERY
 X3 = EMERGENCY
 X4 = SAVINGS
 X5 = INVESTMENT
 X6 = TOILETRIES
 X7 = DATA AND AIRTIME
 Z = Allowance

 OBJECTIVE FUNCTION:
 
 Z = X1 + X2 + X3 + X4 + X5 + X6
 
 CONSTRAINTS:
 
 X1 + X3 + X4 <= 3500
 X2 + X6 <=700
 X5 + X7 <=2500

  X(i)>=0 FOR i=1,2,3,4,5,6,7

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

budget_limits = [1600, 1500, 200, 500, 1500, 500]
variables = np.array(['rent','grocery','emergency','investment','savings','pocket_money'])
colors = sns.color_palette('pastel')[0:len(variables)]
plt.pie( budget_limits, labels = variables, colors = colors, autopct='%1.1f%%')
plt.title('expenses allocation')
plt.show()
"""

from pulp import *
import seaborn as sns
import matplotlib.pyplot as plt

problem = pulp.LpProblem("Expense_allocation",LpMaximize)

x1 = pulp.LpVariable('rent',0,1600,'integer')
x2 = pulp.LpVariable('grocery',0,1500,'integer')
x3 = pulp.LpVariable('emergency',0,500,'integer')
x4 = pulp.LpVariable('investment',0,500,'integer')
x5 = pulp.LpVariable('data',0,300,'integer')
x6 = pulp.LpVariable('savings',0,2000,'integer')
x7 = pulp.LpVariable('pocket_money',0,300,'integer')

problem += pulp.lpSum([x1,x2,x3,x4,x5,x6,x7])
problem += pulp.lpSum([x1,x2,x3]) <=3500
problem += pulp.lpSum([x5,x7])<=700
problem += pulp.lpSum([x4,x6])<=2500

status = problem.solve()
print('status: ',status)

for variable in problem.variables():
    print(variable," = ",variable.value())
print("objective function value = ",value(problem.objective))

variables = problem.variables()
colors = sns.color_palette('pastel')[0:len(problem.variables())]
plt.pie(variables.value(), lables=problem.variables(), colors=colors, autopct='%1.1f%%')
plt.title('expenses allocation')
plt.show()










