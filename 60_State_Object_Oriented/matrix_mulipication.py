
# import the matrix file
import matrix

# The current predict state function
def predict_state_mtx(state, dt):
    ## TODO: Assume that the state passed in is a Matrix object
    ## Using a constant velocity model and a transformation matrix
    ## Create and return the new, predicted state!
    tx_matrix = matrix.Matrix([ [1, dt], 
                                [0, 1] ])
    
    predicted_state = tx_matrix * state
    
    return predicted_state

# initial state variables
initial_position = 10 # meters
velocity = 30 # m/s

# Initial state vector
initial_state = matrix.Matrix([ [initial_position], 
                                [velocity] ])


print('The initial state is: ' + str(initial_state))


# after 2 seconds make a prediction using the new function
state_est1 = predict_state_mtx(initial_state, 2)

print('State after 2 seconds is: ' + str(state_est1))
