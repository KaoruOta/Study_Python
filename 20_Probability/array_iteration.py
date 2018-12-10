import numpy as np

# A 1x7 road
road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])

# Iterate through the array
length = len(road)
for index in range(0, length):
    # Find and store the value at each index
    value = road[index]
    # Print a new line and the value
    print('road['+str(index)+'] = '+str(value))

# Iterate and exit the loop (return) once you reach index 3 - the middle
for index in range(0, length):
    # Check if index is equal to 3
    print(str(index))
    if index == 3:
        print('We\'ve reached the middle of the road and we\'re leaving the loop!')
        break
