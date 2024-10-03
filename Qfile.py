# Imports.
import numpy as np

# Q-learning parameters("default" values).
gamma = 0.75
alpha = 0.9

# Location to state.
locations = {
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
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
}
# Actions.
actions = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
]
# Rewards matrix.
R = np.array([
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,1000,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
])
# Initial Q values.
Q = np.array(np.zeros([16,16]))

# Implement Q learning.
for i in range(1000):
    current = np.random.randint(0,16)
    playable_actions = []
    for j in range(16):
        if R[current, j] > 0:
            playable_actions.append(j)
    next_state = np.random.choice(playable_actions)
    # Time difference.
    TD = R[] + gamma * Q[] - Q[]