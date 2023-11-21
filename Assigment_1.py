import numpy as np
import math
import matplotlib.pyplot as plt
from math import sin, cos, pi
import time 

# Step 1
# multiply a random number between 0-1 by 2 pi to get a random number between 0-2pi
2*math.pi*np.random.rand()


# Step 2
def get_random_radian(N):
   return 2*math.pi*np.random.rand(N)

trial_1_var = get_random_radian(10000)

plt.hist(trial_1_var, bins = 6)
print(f'The mean is {np.mean(trial_1_var)}')
print(f'The standard deviation is {np.std(trial_1_var)}')
plt.show()

#Step 3
ss = 0.5 #step size

def get_xy_velocities(N):  # N in this case is the number of persons
    velocity = []
    for n in range(N):
        x_direction = ss * math.cos(2 * math.pi * np.random.rand())
        y_direction = ss * math.sin(2 * math.pi * np.random.rand())
        velocity.append([x_direction, y_direction])
    return np.array(velocity)


position = np.array([[0.0,0.0]]) #starting position of prisoner
ns = 1000 #number of steps

copy_position = [position.copy().flatten()] # Creating a copy for plotting

for i in range(0,ns): # making the path for 1000 steps
   position += get_xy_velocities(1)  # Adding the random velocity to the starting position
   copy_position.append(position.copy().flatten())  # Storing the position for plotting


copy_position = np.array(copy_position) # Convert copy_positions to array as the previous for loop resulted in a tuple formating 

# Ploting the path
plt.figure(figsize=(8, 8))
plt.plot(copy_position[:, 0], copy_position[:, 1], marker='o')
plt.title('Prisoner Path')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)
plt.show()


# Step 4
Np = 1000  # persons
ns_2 = 500  # number of steps


start_position = np.zeros([Np, 2])  # starting position of prisoners (all zeros)
copy_position_2 = [start_position.copy()]  # Creating a copy for plotting


def get_xy_velocities(N):
    velocity = []
    for n in range(N):
        x_direction = ss * np.cos(2 * np.pi * np.random.rand())
        y_direction = ss * np.sin(2 * np.pi * np.random.rand())
        velocity.append([x_direction, y_direction])
    return np.array(velocity)


for i in range(ns_2):  # making the path for 500 steps
    start_position += get_xy_velocities(Np)  # Adding the random velocity to the starting position
    copy_position_2.append(start_position.copy())  # Storing the position for plotting


copy_position_2 = np.array(copy_position_2)  # Convert copy_positions to array

#Ploting the figure with animation 
fig, ax = plt.subplots(figsize=(8,8))

def update_plot(frame):
    ax.clear()
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    for j in range(Np):
        ax.plot(copy_position_2[:frame, j, 0], copy_position_2[:frame, j, 1], marker='o', markersize=1)
    ax.set_title('Prisoner Path')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.grid(True)

#creating animation
for j in range(ns_2):
   update_plot(j)
   plt.pause(0.1)
   fig.canvas.draw()
   fig.canvas.flush_events()

plt.show()

