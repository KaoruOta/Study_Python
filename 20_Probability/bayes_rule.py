# Given three input probabilities, complete this function
# so that it returns the posterior probability

def bayes(p_A, p_B_given_A, p_notB_given_notA):
    
    ## TODO: Calculate the posterior probability
    ## and change this value
    
    p_not_A = 1 - p_A
    p_B_given_notA = 1 - p_notB_given_notA
    
    p_B_A = p_B_given_A * p_A
    p_B_notA = p_B_given_notA*p_not_A
    
    p_B = p_B_A + p_B_notA
    
    
    posterior = (p_B_given_A*p_A)/p_B
    
    return posterior


## TODO: Change these values, run your code with them, and use print 
## statements to see the output of your function and get feedback
p_A = 0.2
p_B_given_A = 0.9
p_notB_given_notA = 0.5

posterior = bayes(p_A, p_B_given_A, p_notB_given_notA)
print('Your function returned that the posterior is: ' + str(posterior))

# Test code - do not change
import solution

test_p_A = 0.4
test_p_B_given_A = 0.7
test_p_notB_given_notA = 0.9

# This line calls your function and stores the output
posterior = bayes(test_p_A, test_p_B_given_A, test_p_notB_given_notA)
correct_posterior = solution.bayes(test_p_A, test_p_B_given_A, test_p_notB_given_notA)

# Assertion, comparison test
try:
    
    assert(abs(posterior - correct_posterior) < 0.0001)
    print('That\'s right!')
except:
    print ('Your code returned that the posterior is: ' +str(posterior) 
           + ', which does not match the correct value.')
