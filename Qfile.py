# Imports.
import numpy as np

# Setting for the Q-Learning.
gamma = 0.75
alpha = 0.9

# States.
location_to_state = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11
}

# Actions.
actions = [0,1,2,3,4,5,6,7,8,9,10,11]

# Rewards.
R = np.array([
    [0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0],
    [0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,1000,1,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,1],
    [0,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,1,0,0,1,0]
])

# Dictionary.
state_to_location = {state: location for location, state in location_to_state.items()}

Q = np.array(np.zeros([12,12]))

# Q-learning.
for i in range(1000):
    current_st = np.random.randint(0,12)
    playable_actions = []
    for j in range(12):
        if R[current_st, j] > 0:
            playable_actions.append(j)
    next_st = np.random.choice(playable_actions)
    TD = R[current_st, next_st] + gamma * Q[next_st, np.argmax(Q[next_st,])] - Q[current_st, next_st]
    Q[current_st, next_st] = Q[current_st, next_st] + alpha * TD

print(Q.astype(int))
