import numpy as np
import math
import matplotlib.pyplot as plt
import time 

# Step 1
# multiply a random number between 0-1 by 2 pi to get a random number between 0-2pi
2*math.pi*np.random.rand()


# Step 2
def get_random_radian(N):
   return 2*math.pi*np.random.rand(N)

trial_1_var = get_random_radian(10000)

plt.hist(trial_1_var, bins = 6)
mean_1 = np.mean(trial_1_var)
std_1 = np.std(trial_1_var)
plt.show()
print(mean_1, std_1)

#Step 3
#create a random walk of a person 
#create a function get_xy_velocities(N) which returns a (x,y) vector containing the step in a random direction with a magnitude of 0.5m
#store the dirrection of the person in a matrix pos where the first colunm is the x position and the second column is the y position 

import numpy as np
xy_array = np.array[(0,0)]

number_1 = np.array([0.1])
for n in range(1,30):
    number_1 = np.vstack((number_1 , number_1[-1]*10 - 0.9))

def get_xy_velocities(N): #N in this case is the number of steps 
   for i in range(0, N):
      np.vstack(())
      x_1 = (0.5*N - y_1**2)**0.5
      y_1 = (0.5*N- x_1**2)**0.5
      return (x_1, y_1)
get_xy_velocities(10) 





