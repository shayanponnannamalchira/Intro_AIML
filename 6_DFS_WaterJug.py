from collections import deque

def is_goal(state, target):
    return state[0] == target or state[1] == target

def water_jug_dfs(x, y, target):
    stack = []
    visited = set()

    start_state = (0, 0)
    stack.append((start_state, [start_state])) 

    while stack:
        (jug_x, jug_y), path = stack.pop()
        
        current_state = (jug_x, jug_y)
        
        if current_state in visited:
            continue
            
        visited.add(current_state)

        if is_goal(current_state, target):
            print("Solution Path Found (DFS):")
            for step in path:
                print(f"Step: X={step[0]}, Y={step[1]}")
            return path
            
        fill_x = (x, jug_y)
        fill_y = (jug_x, y)
        empty_x = (0, jug_y)
        empty_y = (jug_x, 0)
        
        pour_x_to_y = (
            jug_x - min(jug_x, y - jug_y), 
            jug_y + min(jug_x, y - jug_y)
        )
        
        pour_y_to_x = (
            jug_x + min(jug_y, x - jug_x), 
            jug_y - min(jug_y, x - jug_x)
        )
        
        next_states = [fill_x, fill_y, empty_x, empty_y, pour_x_to_y, pour_y_to_x]

        for state in next_states:
            if state not in visited:
                stack.append((state, path + [state]))

    return None

solution_path_dfs = water_jug_dfs(4, 3, 2)

if not solution_path_dfs:
    print("\nNo solution found for the given capacities and target.")