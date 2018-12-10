# Import the random module and reference it as rd
import random as rd

def simulate_coin_flips(num_trials):
    '''
    A function to simulate coin flips
    
    Args:
        num_trials (int): The number of coin flip 
                          trials to simulate
    Returns:
        int: The percentage of heads from the trials
    '''
    heads = 0.0 # A counter for the number of heads
    tails = 0.0 # A counter for the number of tails
    p_heads = 0.5 # The probability for heads

    # Simulate coin flips up to the num_trials specified
    for i in range(num_trials):
        # Collect a random number between [0,1]
        random_number = rd.random()
        # If the number is less than heads count it as heads
        # Otherwise, count it as tails
        if random_number < p_heads:
            heads = heads + 1.0
        else:
            tails += 1
    # Calculate the percentage of heads based on the number of 
    # heads and trials
    percent_heads = heads / num_trials
    return percent_heads
    
percentage = simulate_coin_flips(200) # calling the function
print(percentage)# Import the random module and reference it as rd
