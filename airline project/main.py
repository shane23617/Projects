from pulp import *

variables = ['short_haul pilots','long haul pilots','co-pilots short haul','long haul co-pilots','senior FA(short haul)','senior FA(long haul)','junior FA(short haul)','junior FA(long haul)','check in staff','baggage handling','gate management','security personnel','lounge staff','engine maintenance','cabin maintenance','avionics maintenance','emergency equipment','scheduling and dispatch','customer service','training and compliance']

labour_cost = [320, 300, 210, 195, 140, 155, 95, 105, 75, 65, 80, 85, 70, 180, 160, 200, 150, 90, 72, 95]

scheduling_LP = pulp.LpProblem('Airline_flight_scheduling_optimization', LpMinimize)
airline_variables = pulp.LpVariable.dicts("variables", variables,0,None,'continuous')
#objective function
scheduling_LP += pulp.lpSum(labour_cost[i] * airline_variables[variable] for i, variable in enumerate(variables))


# aviation regulatory constraints
scheduling_LP += pulp.lpSum([airline_variables[variables[0]],airline_variables[variables[1]]]) <= 900
# constraint for co-pilot ratio
scheduling_LP += airline_variables[variables[3]] >= 0.5 * airline_variables[variables[1]]
#minimum crew coverage
scheduling_LP += pulp.lpSum([airline_variables[variables[0]],airline_variables[variables[2]]]) >= 600
#senoir flight attendant proportion
chosen_1 = [4,5,6,7]
scheduling_LP += lpSum([airline_variables[variables[4]],airline_variables[variables[5]]]) >= 0.4 * lpSum(airline_variables[variables[i]] for i in chosen_1)

#operational coverage constraint
scheduling_LP += airline_variables[variables[0]] >= 400
scheduling_LP += airline_variables[variables[1]] >= 300
chosen_2 = [8,9,10]
scheduling_LP += lpSum([airline_variables[variables[u]] for u in chosen_2]) >= 1200
scheduling_LP += airline_variables[variables[11]] >= 126

#maintance regulatory constraints
scheduling_LP += airline_variables[variables[13]] >= 200
scheduling_LP += airline_variables[variables[15]] >= 0.2 * airline_variables[variables[1]]
chosen_3 = [13,14,15,16]
scheduling_LP += lpSum(airline_variables[variables[o]] for o in chosen_3) <= 800

#budget constraints
scheduling_LP += lpSum([labour_cost[i] * airline_variables[variable] for i, variable in enumerate(variables)]) <= 2500000
scheduling_LP += lpSum(labour_cost[i] * airline_variables[variables[i]] for i in chosen_3) <= 400000
chosen_5 = [8,9,10,11,12]
scheduling_LP += lpSum(labour_cost[i] * airline_variables[variables[i]] for i in chosen_5) <= 300000

#workforce balance constraints
scheduling_LP += airline_variables[variables[19]] >= 0.05 * lpSum(airline_variables[variables[i]] for i in range(19))
scheduling_LP += airline_variables[variables[18]] >= 500
scheduling_LP += airline_variables[variables[17]] >= 150

status = scheduling_LP.solve()
print("status: ", status)
for variable in scheduling_LP.variables():
    print(variable," = ",variable.value())
constraints = scheduling_LP.constraints
print('constraints: ', constraints)# make the constraints be in different lines
print("objective function value = ",value(scheduling_LP.objective))















