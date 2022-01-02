import matplotlib.pyplot as plt
import numpy as np
import math
# plt.rcParams['text.usetex'] = True


fig, ax = plt.subplots()


# Read data
Kp = [5]

Ki = [0.01]

Kd = [0.25]

for kp in Kp:
	for ki in Ki:
		for kd in Kd:

			filename = f"data250/kp={kp}_ki={ki}_kd={kd}.txt"

			with open(filename, 'r') as f:

				# get values
				lines = f.readlines()
				time_recorded, angle_recorded = [], []
				for line in lines:
					line.replace("\n", "")
					angle, time = line.split()

					angle_recorded.append(float(angle))
					time_recorded.append(float(time))

				# draw	
				ax.plot(angle_recorded, time_recorded, label=f'Kp = {kp}, Ki = {ki}, Kd = {kd} ', linestyle='-')

time = np.linspace(0, 5,10)
target = time*0 + 360

# plot
ax.plot(time, target, color='red', label= 'target', linestyle='--')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (degrees)')
# ax.title()
plt.grid()
plt.legend()
plt.show()