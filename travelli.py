from itertools import permutations

def Tsp_Dp(cost):
    num = len(cost)
    nodes = list(range(1,num))
    min_cost = float('inf')

    for per in permutations(nodes):
        current_node = 0
        current_cost = 0
        for node in per:
            current_cost += cost[current_node][node]
            current_node = node
        current_cost += cost[current_node][0]
        min_cost = min(min_cost,current_cost)
        print(min_cost)
        
    return min_cost

cost =[
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = Tsp_Dp(cost)
print(result)