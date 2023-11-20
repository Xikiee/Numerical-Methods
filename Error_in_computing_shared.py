#practice 1 ()
import numpy as np
number_1 = np.array([0.1])
for n in range(1,30):
    number_1 = np.vstack((number_1 , number_1[-1]*10 - 0.9)) #creates a new colunm which uses the values from the last column
number_2 = np.array([0.1])
for n in range(1,30):
    number_2 = np.vstack((number_2, number_2[-1]*10 - 18))
print(f" number_2 = {number_2}") 

#investigate the result of np.sin(1e40 * np.pi)

import numpy as np
import matplotlib.pyplot as plt

v = np.logspace(0,40, 41)
y = np.sin(v*np.pi)
plt.loglog(v,np.abs(y))
plt.show()

#try the following commands in python
import numpy as np
np.iinfo(np.int32).min
np.iinfo(np.int32).max
i = np.int16(np.iinfo(np.int32).max)


g = 0.1 
type(g)
print(f"{g:1.15e}")#prints g to 15 digits (at some point you will get an error showing that 0.1 stored in the computer is not equal to 0.1(go to 30 decimal places))


i = 2.0**1000
for i in range(200):
    i *= 2 
    print(i)