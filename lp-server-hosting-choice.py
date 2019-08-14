# Web server performance problem
from pulp import *

# The challenge is to maximise the number of hits serviced by the server farm
# X1 - Standard server 2U - 300W, 1000 hits/min
# X2 - Performance server 1U - 500W, 2000 hits/min
#
model = LpProblem("Maximising", LpMaximize)

#We can't install half a server, so the category for each serer type type is an integer.
X1 = LpVariable('X1', lowBound=0, cat='Integer')
X2 = LpVariable('X2', lowBound=0, cat='Integer')

#Our objective is to maximise the hits serviced by the web servers
model += 1000 * X1 + 2000 * X2, "Total Hits"

#Setup the constraints
budget = 400 * X1 + 1600 * X2
rack_space = 2 * X1 + X2
power = 300* X1 + 500 * X2

#Add constraints to the model
model += budget <= 36800
model += rack_space <= 44
model += power <= 12200

#Print the problem
print (model)

#Solve the problem
model.solve()
print ("Status : ", LpStatus[model.status])

#Print our changing cells
#Print the number of servers needed
for v in model.variables():
    print (v)
    print (v.varValue)

#Print our objective function value - Result (Target) cell
print ("Total Hits             = ", value(model.objective))