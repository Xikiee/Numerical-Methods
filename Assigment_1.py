import numpy as np
import math
import matplotlib.pyplot as plt
import time 

###################################### Step 1 ######################################
# multiply a random number between 0-1 by 2 pi to get a random number between 0-2pi
2*math.pi*np.random.rand()


###################################### Step 2 ######################################
def get_random_radian(N):
   return 2*math.pi*np.random.rand(N)

trial_1_var = get_random_radian(10000)

plt.hist(trial_1_var, bins = 6)
print(f'The mean is {np.mean(trial_1_var)}')
print(f'The standard deviation is {np.std(trial_1_var)}')
plt.show()

###################################### Step 3 ######################################
ss = 0.5 #step size

def get_xy_velocities(N):  # N in this case is the number of persons
    velocity = []
    for n in range(N):
        x_direction = ss * math.cos(2 * math.pi * np.random.rand()) #cos of angle gives the x direction
        y_direction = ss * math.sin(2 * math.pi * np.random.rand()) #sin of angle gives the y direction
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


###################################### Step 4 ######################################
Np = 1000  # persons
ns_2 = 500  # number of steps


start_position = np.zeros([Np, 2])  # starting position of prisoners (all zeros)
copy_position_2 = [start_position.copy()]  # Creating a copy for plotting

for i in range(ns_2):  # making the path for 500 steps
    start_position += get_xy_velocities(Np)  # Adding the 1000 random velocities to the 1000 starting positions
    copy_position_2.append(start_position.copy())  # Storing the position for plotting

copy_position_2 = np.array(copy_position_2)  # Convert copy_positions_2 to array

#Ploting the figure with animation 
fig, ax = plt.subplots(figsize=(8,8))

def update_plot(frame):
    ax.clear()
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    for j in range(Np):
        ax.plot(copy_position_2[:frame, j, 0], copy_position_2[:frame, j, 1], marker='o', markersize=1)
    ax.set_title('1000 Prisoner Paths')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.grid(True)

#creating animation
for j in range(ns_2):
   update_plot(j)
   plt.pause(0.000000000001)
   fig.canvas.draw()
   fig.canvas.flush_events()
plt.show() #warning running this will take a lot of time and the rest will not run until after the animation is finished (even if the figure is exited out)

#plotting a 2d histogram with the x and y possition of each prisoner
plt.figure()
plt.hist2d(copy_position_2[ns_2,:,0], copy_position_2[ns_2,:, 1], bins = (50,50), cmap=plt.cm.jet)
plt.title('Final Positions')
plt.show()

###################################### Step 5 ######################################
#creating an array with all the final distances for each of the prisoners 
magnitude = np.sqrt(copy_position_2[:,:, 0]**2 +copy_position_2[:,:,1]**2) #each row is the distance each prisoner is at that time
final_positon = magnitude[:, -1] #takes the last row and therfore the distance each priosner is to the starting point
msd = np.mean(magnitude**2, axis=1) #axis = 1 means to take the mean of every row(time) in magnitude^2
#msd = 2nDt. n = 2 as it is 2 dimensional and t is the time
time_steps = np.arange(0,ns_2+1) 
diff_c = msd / (2*2*time_steps)
theoretical_d = ss**2/(2*2*1)
theoretical_dx = np.full(501, theoretical_d) #creating x points for graphing the theoretical d

plt.plot(time_steps,diff_c, label="Experimental")
plt.plot(time_steps, theoretical_dx, label="Theoretical")
plt.legend()
plt.title('Diffusion Coefficient over Time (s)')
plt.xlabel('Time (s)')
plt.ylabel('Diffusion Coefficient')

plt.show()
###################################### Step 6 ######################################
 
fig = plt.figure(figsize = (8,8))
fig.suptitle('Experimental Distances at different times')

#graph 1 
ax1 = plt.subplot(2,2,1)
ax1.hist2d(copy_position_2[125,:,0], copy_position_2[125, :, 1], bins = 50)
ax1.set_title('125 s')


#graph 2 
ax2 = plt.subplot(2,2,2)
ax2.hist2d(copy_position_2[250,:,0], copy_position_2[250, :, 1], bins = 50)
ax2.set_title('250 s')


#graph 3
ax3 = plt.subplot(2,2,3)
ax3.hist2d(copy_position_2[375, :, 0], copy_position_2[375,:, 1], bins = 50)
ax3.set_title('375 s')


#graph 4
ax4 = plt.subplot(2, 2, 4)
ax4.hist2d(copy_position_2[500, :, 0], copy_position_2[500, :, 1], bins = 50)
ax4.set_title('500 s')


plt.plot()
plt.show()

###################################### Step 7 ######################################

# Make data.
x_surf = np.arange(-30, 30, 0.025)
y_surf = np.arange(-30, 30, 0.025)

x_surf,y_surf = np.meshgrid(x_surf, y_surf)

#creating the green function
from matplotlib import cm
def green_function(t):
    exp = (-(x_surf**2 +y_surf**2))/(4*theoretical_d *t)
    return 1/(4*np.pi*theoretical_d*t)*np.exp(exp)

#plotting the figure
fig_surf = plt.figure(figsize = (12,10))
fig_surf.suptitle('Experimental Histogram vs Theoretical PFD')

#graph set for t = 125 s
#histogram plot
ax1 = plt.subplot(2,2,1)
ax1.hist2d(copy_position_2[125, :, 0], copy_position_2[125, :, 1], bins = 50)
ax1.set_title('125 s')
#surface plot
surf1 = fig_surf.add_subplot(2,2,3, projection='3d')
surf1a = surf1.plot_surface(x_surf,y_surf, green_function(125), cmap=cm.magma,linewidth=0, antialiased=False)
surf1.set_zlim(-0.01, 0.01)
surf1.set_title('125 s')
fig_surf.colorbar(surf1a, shrink=0.5, aspect=5)# Add a color bar which maps values to colors.

#graph set for t = 500 s 
#histogram plot
ax2 = plt.subplot(2,2,2)
ax2.hist2d(copy_position_2[500, :, 0], copy_position_2[500, :, 1], bins = 50)
ax2.set_title('500 s')
#surface plot
surf2 = fig_surf.add_subplot(2,2,4, projection='3d')
surf2a = surf2.plot_surface(x_surf,y_surf, green_function(500), cmap=cm.magma,linewidth=0, antialiased=False)
surf2.set_zlim(-0.01, 0.01)
surf2.set_title('500 s')
fig_surf.colorbar(surf2a, shrink=0.5, aspect=5)

plt.show()