# Transportation Problem Solver
import numpy as np

def northWestCornerMethod(supply, demand, cost):
    # Initialize the Tableau with zeros
    tableau = np.zeros((len(supply), len(demand)))

    # Now we must iterate through the Tableau to find the optimal solution
    i = 1
    j = 1
    n = 1
    while i < len(supply) and j < len(demand):
        print("Iteration: " + str(n)) 
        if supply[i] > demand[j]:
            # The supply is greater than the demand
            tableau[i][j] = demand[j]
            supply[i] -= demand[j]
            demand[j] = 0
            j += 1
            n += 1

            print(tableau)
        elif supply[i] < demand[j]:
            # The demand is greater than the supply
            tableau[i][j] = supply[i]
            demand[j] -= supply[i]
            supply[i] = 0
            i += 1
            n += 1

            print(tableau)
        else:
            # The supply and demand are equal
            tableau[i][j] = supply[i]
            supply[i] = 0
            demand[j] = 0
            i += 1
            j += 1
            n += 1

            print(tableau)

    return tableau

def leastCostMethod(supply, demand, cost):
    supply = supply
    demand = demand
    cost = cost

    # Initialize the Tableau with zeros
    tableau = np.zeros((len(supply), len(demand)))

    while sum(supply) != 0 and sum(demand) != 0:
        i = 0
        j = 0
        iteration = 1

        print("Iteration: " + str(iteration))
        for i in range(len(supply)):
            for j in range(len(demand)):
                if supply[i] != 0 and demand[j] != 0:
                    if iteration == 1:
                        minCost = cost[i][j]
                        minI = i
                        minJ = j
                    elif cost[i][j] < minCost:
                        minCost = cost[i][j]
                        minI = i
                        minJ = j
        
        if supply[minI] > demand[minJ]:
            tableau[minI][minJ] = demand[minJ]
            supply[minI] -= demand[minJ]
            demand[minJ] = 0
            print(tableau)
            iteration += 1
        elif supply[minI] < demand[minJ]:
            tableau[minI][minJ] = supply[minI]
            demand[minJ] -= supply[minI]
            supply[minI] = 0
            print(tableau)
            iteration += 1
        else:
            tableau[minI][minJ] = supply[minI]
            supply[minI] = 0
            demand[minJ] = 0
            print(tableau)
            iteration += 1

    return tableau


def VogelApproximationMethod(supply, demand, cost):
    supply = supply
    demand = demand
    cost = cost

def getCost (cost, initialAlloc):
    cost = 0
    for i in range(len(initialAlloc)):
        for j in range(len(initialAlloc[i])):
            cost += initialAlloc[i][j] * cost[i][j]
    print("The cost is: " + str(cost))
   
def __main__():
    # Initialize the Tableau by creating the initial datasets
    # First, Find the number of Factories
    numFactories = int(input("Enter the number of factories: "))
    # Second, Find the number of Warehouses
    numStores = int(input("Enter the number of Stores: "))

    # Then we ask the supply of each factory
    supply = np.zeros(numFactories)
    for i in range(numFactories):
        supply[i] = int(input("Enter the supply of factory " + str(i+1) + ": "))
    
    # Then we ask the demand of each store
    demand = np.zeros(numStores)
    for i in range(numStores):
        demand[i] = int(input("Enter the demand of store " + str(i+1) + ": "))
    
    # Then we create a cost matrix
    cost = np.zeros((numFactories, numStores))
    for i in range(numFactories):
        for j in range(numStores):
            cost[i][j] = int(input("Enter the cost of transporting from factory " + str(i+1) + " to store " + str(j+1) + ": "))
    
    # We must also check if the supply and demand are equal. Otherwise, we must add a dummy factory or store
    if sum(supply) != sum(demand):
        if sum(supply) > sum(demand):
            # We must add a dummy store
            demand = np.append(demand, sum(supply) - sum(demand))
            supply = np.append(supply, np.zeros((numStores, 1)), axis=1)
            cost = np.append(cost, np.zeros((numFactories, 1)), axis=1)
        else:
            # We must add a dummy factory
            supply = np.append(supply, sum(demand) - sum(supply))
            demand = np.append(demand, np.zeros((1, numFactories)), axis=0)
            cost = np.append(cost, np.zeros((1, numStores)), axis=0)

    # Now we create the Tableau using the three different methods (NWC, LCM and VAM)
    tableauNWC = northWestCornerMethod(supply, demand, cost)
#    getCost(cost, tableauNWC)
    tableauLCM = leastCostMethod(supply, demand, cost)
#    getCost(cost, tableauLCM)
#    tableauVAM = VogelApproximationMethod(supply, demand, cost)

if __name__ == "__main__":
    __main__()