from collections import deque

# Each state is represented as (monkey_pos, box_pos, monkey_on_box)
# Positions are tuples like (x, y)

def is_goal(state, banana_pos):
    monkey_pos, box_pos, on_box = state
    return on_box and box_pos == banana_pos and monkey_pos == box_pos

def get_successors(state, banana_pos, grid_size=(3, 3)):
    monkey_pos, box_pos, on_box = state
    successors = []

    # Move in 4 directions
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        new_monkey = (monkey_pos[0] + dx, monkey_pos[1] + dy)
        if 0 <= new_monkey[0] < grid_size[0] and 0 <= new_monkey[1] < grid_size[1]:
            successors.append((new_monkey, box_pos, False))  # walking resets climbing

    # Push box if adjacent
    if abs(monkey_pos[0] - box_pos[0]) + abs(monkey_pos[1] - box_pos[1]) == 1:
        dx = box_pos[0] - monkey_pos[0]
        dy = box_pos[1] - monkey_pos[1]
        new_box = (box_pos[0] + dx, box_pos[1] + dy)
        if 0 <= new_box[0] < grid_size[0] and 0 <= new_box[1] < grid_size[1]:
            successors.append((box_pos, new_box, False))

    # Climb the box if at the same position
    if monkey_pos == box_pos and not on_box:
        successors.append((monkey_pos, box_pos, True))

    return successors

def monkey_banana_problem(monkey_start, box_start, banana_pos):
    initial_state = (monkey_start, box_start, False)
    queue = deque()
    visited = set()

    queue.append((initial_state, []))  # (state, path)

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue
        visited.add(current_state)

        if is_goal(current_state, banana_pos):
            return path + [current_state]

        for successor in get_successors(current_state, banana_pos):
            queue.append((successor, path + [current_state]))

    return None

# Define positions
monkey_start = (0, 0)
box_start = (1, 1)
banana_pos = (2, 2)

solution = monkey_banana_problem(monkey_start, box_start, banana_pos)

if solution:
    print("Solution found! Steps:")
    for state in solution:
        pos, box, on_box = state
        print(f"Monkey at {pos}, Box at {box}, {'On box' if on_box else 'On ground'}")
    print("Monkey grabs the bananas!")
else:
    print("No solution found.")
