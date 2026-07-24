import numpy as np
import pulp as pl

lp_problem  = pl.LpProblem("Maximize_profit", pl.LpMaximize)

x1 = pl.LpVariable("x1",0)
x2 = pl.LpVariable("x2",0)
x3 = pl.LpVariable("x3",0)

lp_problem += 3*x1 + 2*x2 + 4*x3, "Objective_function"
lp_problem += 2*x1 + x2 + x3 <= 20, "Constraint_1"
lp_problem += 4*x1 + 3*x2 + 5*x3 <= 40, "Constraint_2"
lp_problem += x1 + 2*x2 + 3*x3 <= 30, "Constraint_3"
lp_problem.solve()
print("Status:", pl.LpStatus[lp_problem.status])
print("Optimal value of x1:", x1.varValue)
print("Optimal value of x2:", x2.varValue)
print("Optimal value of x3:", x3.varValue)
print("Maximum Profit:", pl.value(lp_problem.objective))






