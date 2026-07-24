import numpy as np

class AssignmentSolver:
    def __init__(self,matrix,demand_values, supply_values,objective_function,x_variables):
        self._matrix = matrix
        self._demand_values = demand_values
        self._supply_values = supply_values
        self._objective_function = objective_function
        self._x_variables = x_variables

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self,matrix):
        self._matrix = matrix

    @property
    def demand_values(self):
        return self._demand_values

    @demand_values.setter
    def demand_values(self,demand_values):
        self._demand_values = demand_values

    @property
    def supply_values(self):
        return self._supply_values
    @supply_values.setter
    def supply_values(self,supply_values):
        self._supply_values = supply_values

    @property
    def objective_function(self):
        return self._objective_function
    @objective_function.setter
    def objective_function(self,objective_function):
        self._objective_function = objective_function

    @property
    def x_variables(self):
        return self._x_variables
    @x_variables.setter
    def x_variables(self,x_variable):
        self._x_variables = x_variable
    def constraints(self):
        constraints = []
        #supply constraints
        for i in range (len(self._supply_values)):
            row_sum = np.sum(self._x_variables[i, :])
            constraints.append(row_sum <=self._supply_values[i])

        #demand constraints
        for j in range(len(self._demand_values)):
            column_sum = np.sum(self._x_variables[:, j])
            constraints.append(column_sum >=self._demand_values[j])

        return constraints

    def least_cost_method(self):
        demand = self._demand_values.copy().astype(float)
        supply = self._supply_values.copy().astype(float)
        cost = self._matrix.copy().astype(float)
        x = np.zeros((len(supply), len(demand)))
        while np.any(supply > 0) and np.any(demand > 0):

            i, j = np.unravel_index(np.argmin(cost), cost.shape)
            allocation = min(supply[i], demand[j])
            x[i, j] = allocation
            supply[i] -= allocation
            demand[j] -= allocation


            if supply[i] == 0:
                cost[i, :] = np.inf  # blocks exhausted rows from being picked again
            if demand[j] == 0:
                cost[:, j] = np.inf  # blocks exhausted columns from being picked again

        self._x_variables = x
        return x
    def vogel_method(self):
        supply =self._supply_values.copy().astype(float)
        demand = self._demand_values.copy().astype(float)
        x = np.zeros((len(supply), len(demand)))
        cost = self._matrix.copy().astype(float)
        remaining = True
        while remaining:
            row_penalty = np.full(len(supply), -np.inf)
            column_penalty = np.full(len(demand), -np.inf)
            for i in range(len(supply)):
                if supply[i] > 0:
                    available = cost[i, cost[i, :] < np.inf ]
                    if len(available) >= 2 :
                        smallest_row_cost = np.sort(available)[:2]
                        row_penalty[i] = smallest_row_cost[1] - smallest_row_cost[0]
                    elif len(available) == 1 :
                        row_penalty[i] = available[0]
                else:
                    row_penalty[i] =  -np.inf
            for j in range(len(demand)):

                if demand[j] > 0:
                    available = cost[ cost[:, j] < np.inf, j]
                    if len(available) >= 2 :
                        smallest_row_cost = np.sort(available)[:2]
                        row_penalty[i] = smallest_row_cost[1] - smallest_row_cost[0]
                    elif len(available) == 1 :
                        row_penalty[i] = available[0]
                else:
                    column_penalty[j] = -np.inf
            max_row_penalty = max(row_penalty)
            max_column_penalty = max(column_penalty)
            if max_row_penalty >= max_column_penalty:
                selected_row = np.argmax(row_penalty)
                selected_column = np.argmin(cost[selected_row, :])
            else:
                selected_column = np.argmax(column_penalty)
                selected_row = np.argmin(cost[: ,selected_column])

            allocation = min(supply[selected_row], demand[selected_column])
            x[selected_row, selected_column] = allocation
            supply[selected_row] -= allocation
            demand[selected_column] -= allocation
            if supply[selected_row] == 0:
                cost[selected_row, :] = np.inf

            if demand[selected_column] == 0:
                cost[:, selected_column] = np.inf

            if np.all(supply == 0) and np.all(demand == 0):
                    remaining = False

        self._x_variables = x
        return x

    def north_west_corner_method(self):
        supply =self._supply_values.copy().astype(float)
        demand = self._demand_values.copy().astype(float)
        cost = self._matrix.copy().astype(float)
        x = np.zeros((len(supply), len(demand)))

        pass

    def modified_solution(self):
        pass

if __name__ == "__main__":

    #Try to randomly generate the integer cost values
    matrix = np.array([(12,18,22,31,38,25),(15,14,20,28,35,22),(34,29,24,16,14,27),(41,37,26,22,18,30)])
    demand_values = np.array([60, 45, 70, 55 , 80, 50])
    supply_values = np.array([120, 95,110,75])

    surplus = supply_values.sum() - demand_values.sum()
    if surplus > 0:
        balanced_matrix = np.hstack([matrix, np.zeros((4, 1))])
        balanced_demand = np.append(demand_values, surplus)

    elif surplus == 0:
        balanced_matrix = matrix
        balanced_demand = demand_values
        print("The problem is balanced")
    else:
        balanced_matrix = np.vstack([matrix, np.zeros((1, matrix.shape[1]))])
        supply_values = np.append(supply_values, -surplus)
        balanced_demand = demand_values

    objective_function = lambda x: np.sum(balanced_matrix*x)
    x_variable = np.zeros(balanced_matrix.shape)
    solver = AssignmentSolver(balanced_matrix,balanced_demand,supply_values,objective_function,x_variable)
    result = solver.vogel_method()
    print(result)
    print("Constraints met:", solver.constraints())








