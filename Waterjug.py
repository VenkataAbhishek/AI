from collections import deque

def WaterJug(a_capacity,b_capacity,target):
    visited = set()
    queue = deque()
    queue.append((0,0,[]))
    while queue :
        a,b,steps = queue.popleft()
        if (a,b) in visited: continue
        steps = steps +[(a,b)]
        visited.add((a,b))

        if a==target or b== target:
            return steps

        possible_moves=[
            (a,b_capacity),(a_capacity,b),(a,0),(0,b),
            (a+min(a_capacity-a,b),b-min(a_capacity-a,b)),
            (a-min(b_capacity-b,a),b+min(b_capacity-b,a))
        ] 

        for move in possible_moves:
            if move not in visited:
                queue.append((move[0],move[1],steps))

a_capasity = 5
b_capasity = 3
target = 1
steps = WaterJug(a_capasity,b_capasity,target)
print(steps)