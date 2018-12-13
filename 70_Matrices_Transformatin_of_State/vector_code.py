def add(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        print("error! vectors must be same size to add")
        return 
    
    new_vector = []
    for i in range(len(vector_1)):
        value_1 = vector_1[i]
        value_2 = vector_2[i]
        new_val = value_1 + value_2
        new_vector.append(new_val)
    
    return new_vector

def multiply(scalar, vector):
    new_vector = []
    for value in vector:
        new_value = scalar * value
        new_vector.append(new_value)
    return new_vector

def dot_product(v1, v2):
    if len(v1) != len(v2):
        print("error! Vectors must have same length")
    
    result = 0
    for i in range(len(v1)):
        value_1 = v1[i]
        value_2 = v2[i]
        result += value_1 * value_2
    return result

##### test add #############
v1 = [1,2]
v2 = [3,4]

v_1_plus_2 = add(v1, v2)

print(v1, "plus", v2, "equals", v_1_plus_2)

##### test multiply #############
vector = [1,2,3,4,5]
number = 3

product = multiply(number, vector)

print(number, "times", vector, "equals", product)

##### test dot product #############
vector_1 = [7,2,3]
vector_2 = [1, 10, 4]

# should be 39 (7*1 + 2*10 + 3*4)
v1_dot_v2 = dot_product(vector_1, vector_2)


print(vector_1, "dot", vector_2, "equals", v1_dot_v2)
