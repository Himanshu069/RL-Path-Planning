
import numpy as np
import random

def q_learning(maze, start, goal, episodes=5000, alpha=0.1, gamma=0.9, epsilon=0.1):

    H, W = maze.shape
    # 4 actions: 0:Up, 1:Down, 2:Left, 3:Right
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1,1),(-1,-1),(1,-1)]
    q_table = np.zeros((H, W, len(actions)))

    # Training loop
    for episode in range(episodes):
        state = start
        done = False
        
        while not done:
            # Epsilon-greedy action selection
            if random.uniform(0, 1) < epsilon:
                action_index = random.randint(0, len(actions) - 1)  # Explore
            else:
                action_index = np.argmax(q_table[state[0], state[1]])  # Exploit

            action = actions[action_index]
            next_state = (state[0] + action[0], state[1] + action[1])

            # Check for invalid moves (wall or out of bounds)
            if not (0 <= next_state[0] < H and 0 <= next_state[1] < W and maze[next_state[0], next_state[1]] == 0):
                reward = -100  # High penalty for invalid moves
                # Update Q-value for taking this action from the current state
                q_table[state[0], state[1], action_index] = q_table[state[0], state[1], action_index] + \
                    alpha * (reward - q_table[state[0], state[1], action_index])
                continue # Try another action from the same state

            # Assign reward
            if next_state == goal:
                reward = 100
                done = True
            else:
                reward = -1  # Small penalty for each step

            # Q-learning update rule
            old_value = q_table[state[0], state[1], action_index]
            next_max = np.max(q_table[next_state[0], next_state[1]])
            
            new_value = old_value + alpha * (reward + gamma * next_max - old_value)
            q_table[state[0], state[1], action_index] = new_value

            state = next_state

    # Reconstruct path and create snapshots from the learned Q-table
    path = []
    snapshots = []
    prev = {}
    state = start
    
    # Safety break to prevent infinite loops if no path is found
    max_path_length = H * W
    
    while state != goal and len(path) < max_path_length:
        snapshots.append(state)
        path.append(state)
        
        # Choose the best action from the Q-table
        action_index = np.argmax(q_table[state[0], state[1]])
        action = actions[action_index]
        next_state = (state[0] + action[0], state[1] + action[1])

        # Check for invalid moves in the final path
        if not (0 <= next_state[0] < H and 0 <= next_state[1] < W and maze[next_state[0], next_state[1]] == 0):
            print("Warning: Optimal path learned by TD agent leads into a wall. Training may be insufficient.")
            # If the best action leads to a wall, we need to find an alternative.
            # For simplicity, we'll just stop here. A more robust solution would backtrack
            # or explore other actions from the Q-table.
            break
            
        if next_state in path:
            print("Warning: Path reconstruction entered a loop. The learned policy is not optimal.")
            break

        prev[next_state] = state
        state = next_state

    if state == goal:
        snapshots.append(goal)
        path.append(goal)
    
    return snapshots, prev

def reconstruct_path(prev, goal):
    path = []
    current = goal
    while current in prev:
        path.append(current)
        current = prev[current]
    path.append(current)
    path.reverse()
    return path
