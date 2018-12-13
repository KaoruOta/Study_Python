import numpy as np
import car

# Create a 2D world of 0's
height = 4
width = 6
world = np.zeros((height, width))

# Define the initial car state
initial_position = [0, 0] # [y, x] (top-left corner)
velocity = [0, 1] # [vy, vx] (moving to the right)

# Create a car object with these initial params
carla = car.Car(initial_position, velocity, world)

print('Carla\'s initial state is: ' + str(carla.state))


# Move in the direction of the initial velocity
carla.move()

# Track the change in state
print('Carla\'s state is: ' + str(carla.state))


track_state = 0

while track_state != 99:
    if track_state == 0:
        velocity = [0,1]
        carla.move()

        print track_state
        print('Carla\'s state is: ' + str(carla.state))

        if carla.state[0][1] == 3:
            track_state = 1
        else:
            track_state = 0
    elif track_state == 1:
        velocity = [1,0]
        carla.state[1] = velocity
        carla.move()

        print track_state
        print('Carla\'s state is: ' + str(carla.state))

        if carla.state[0][0] == 3:
            track_state = 2
        else:
            track_state = 1
    elif track_state == 2:
        velocity = [0,-1]
        carla.state[1] = velocity
        carla.move()

        print track_state
        print('Carla\'s state is: ' + str(carla.state))

        if carla.state[0][1] == 0:
            track_state = 3
        else:
            track_state = 2
    elif track_state == 3:
        velocity = [-1,0]
        carla.state[1] = velocity
        carla.move()

        print track_state
        print('Carla\'s state is: ' + str(carla.state))

        if carla.state[0][0] == 0:
            track_state = 99
        else:
            track_state = 3
    else:
        break


# Display the world
carla.display_world()
