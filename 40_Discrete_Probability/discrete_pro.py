#### 
# TODO: Create a Python list of the values in the 'Count' column.
# Your list should start with 54 and follow the same order
# as the data in the column: 54, 111, 163, etc.
###

count_data = [54,111,163,222,277,336,276,220,171,111,59]

# Run this code cell. You do not need to change anything

# A for loop to print out every value in the count_data list
# The len() function determines the size of the list
# The range() function creates an integer 
#           list from 0 to len(count_data).

for i in range(len(count_data)):
    print(count_data[i])

### 
# TODO: calculate the sum of the count_data list 
#     and put the sum in the total_count variable
###

total_count = sum(count_data)

# This will print out the result
print(total_count)

###
# INSTRUCTIONS: Use a for loop to iterate through the 
#      count_data list
# 
# For each value in the list, divide the value by the total_count
# variable.
#
# You will need to append the results to a new list
#
###

normalized_counts = []

for i in range(len(count_data)):
    #print(count_data[i])
    normalized_counts.append(count_data[i]/total_count)
    
# TODO: Write a for loop to itera
#te through the count_data list.
#       Use the for loop example given previously to help
#       get yourself started

    # TODO: Inside the for loop, divide each value in
    # count_data by the total_count variable and append
    # the result to the normalized_counts variable.

print('Here are the normalized counts: ' )
print(normalized_counts)

import plot
plot.plot_probability(normalized_counts)
