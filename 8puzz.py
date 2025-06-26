from collections import deque
import copy

goal_state =[
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

def get_neighbour(state):
    neighbours = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row,col =i,j
    
    directions =[(-1,0),(1,0),(0,-1),(0,1)]

    for dr,dc in directions:
        new_row,new_col = row+dr,col+dc

        if 0<=new_row<3 and 0<=new_col<3:
            new_state = copy.deepcopy(state)
            new_state[row][col],new_state[new_row][new_col] = new_state[new_row][new_col],new_state[row][col]
            neighbours.append(new_state)

    return neighbours

def bfs(start):
    visited = set()
    queue = deque()
    queue.append((start,[]))
    
    while queue :
        current,path = queue.popleft()

        if current == goal_state:
            return path+ [current]
        state_tuple= tuple(map(tuple,current))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbour in get_neighbour(current):
            queue.append((neighbour,path+[current]))
    return None

initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]

print(bfs(initial_state))