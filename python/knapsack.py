
# items: a list of tuples [ (itemValue, itemWeight), ... ]
# maxCapacity: the maximum capacity of the knapsack
# Output: the best value achievable with a knapsack of given size, by index
# note for 0k knapsack, items can simply be duplicated k times, with run time O(k*len(items)*maxCapacity)
def knapsack01(items, maxCapacity):
    container = [0]*(maxCapacity+1) # for up to and including best values
    #container = [float("-inf")]*(maxCapacity+1) # for exact best values
    for itemValue, itemWeight in items:
        for j in range(len(container)-1, -1, -1):
            if j-itemWeight >= 0:
                container[j] = max(container[j], container[j-itemWeight] + itemValue)
    return container

# items: a list of tuples [ (itemValue, itemWeight), ... ]
# maxCapacity: the maximum capacity of the knapsack
# Output: the best value achievable with a knapsack of given size, by index
def knapsack0inf(items, maxCapacity):
    container = [0]*(maxCapacity+1) # for up to and including best values
    #container = [float("-inf")]*(maxCapacity+1) # for exact best values
    for itemValue, itemWeight in items:
        for j in range(len(container)):
            if j+itemWeight < len(container):
                container[j+itemWeight] = max(container[j+itemWeight], container[j] + itemValue)
    return container