from knapsack import knapsack0inf, knapsack01

def gatherJewelsInfo(numJewels):
    jewels = [] 
    for i in range(numJewels):
        jewelAttr = input().split(' ')
        size = int(jewelAttr[0])
        value = int(jewelAttr[1])
        jewel = (value, size)
        jewels.append(jewel)
    return jewels

def main():
    parameters = input().split(' ')
    numJewels = int(parameters[0])
    maxCapacity = int(parameters[1])
    jewels = gatherJewelsInfo(numJewels)
    print( " ".join(str(x) for x in knapsack0inf(jewels, maxCapacity)) )

if __name__ == "__main__":
    main()