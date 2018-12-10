import numpy as np

# A one-lane road, represented by an array
# Here is a 1x7 road
road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])

# Print out some information about this road
print('The length of this array is: ' + str(len(road)))

# Access the first index and read its value
value = road[0]
print('\n')
print('Value at index [0] = ' +str(value))

# Read the last item in the array
# A negative index moves from the end of the list backwards!
value_end = road[-1]
print('\n')
print('Value at index [-1] = ' +str(value_end))

# Compare first and last values
equal = (value == value_end)
print('\n')
print('Are the first and last values equal? ' +str(equal))

