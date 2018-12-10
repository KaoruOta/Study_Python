import numpy as np

# The 1x7 road
road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])

# This function takes in the road and determines where to stop
def find_stop_index(road):
    ## TODO: Iterate through the road array
    ## TODO: Check if a stop sign ('s') is found in the array
    ## If one is, break out of your iteration
    ## and return the value of the index that is *right before* the stop sign
    ## Change the stop_index value
    #stop_index = 0
    
    length = len(road)
    for index in range(0, length):
        value = road[index]
        if value == 's':
            stop_index = index -1
            break
            
    return stop_index



# Test code - do not change
import array_solution

# This line calls the stop function and stores the output
stop = find_stop_index(road)
correct_stop = array_solution.stop_test(road)

# Assertion, comparison test
try:
    assert(stop == correct_stop)
    print('That\'s right!')
except:
    print ('Your code returned that the stop index is: ' +str(stop) 
           + ', which does not match the correct value: ' +str(correct_stop))

# Test 2
stop2 = find_stop_index(array_solution.test_road)
correct_stop2 = array_solution.stop_test(array_solution.test_road)

try:
    assert(stop2 == correct_stop2)    
    print('You passed the second test!')
except:
    print ('For test 2, your code returned that the stop index is: ' +str(stop2) 
           + ', which does not match the correct value.')
