from collections import deque

def is_goal(state, target):
    return state[0] == target or state[1] == target

def water_jug_bfs(x, y, target):
    visited = set()
    queue = deque()

    start_state = (0, 0)
    queue.append((start_state, [start_state])) 

    while queue:
        (jug_x, jug_y), path = queue.popleft()
        
        if (jug_x, jug_y) in visited:
            continue
            
        visited.add((jug_x, jug_y))

        if is_goal((jug_x, jug_y), target):
            for step in path:
                print(f"Step: X={step[0]}, Y={step[1]}")
            return path
            
        next_states = [
            (x, jug_y), 
            (jug_x, y), 
            (0, jug_y), 
            (jug_x, 0), 
            (jug_x - min(jug_x, y - jug_y), jug_y + min(jug_x, y - jug_y)),
            (jug_x + min(jug_y, x - jug_x), jug_y - min(jug_y, x - jug_x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))

    return None

solution_path = water_jug_bfs(4, 3, 2)
if not solution_path:
    print("No solution found.")