import matplotlib.pyplot as plt
import numpy as np
import math

filename = "data_car/2part-1.txt"

fig, ax = plt.subplots()

with open(filename, 'r') as f:

	# get values
	lines = f.readlines()
	time_recorded, distance_recorded = [], []
	for line in lines:
		line.replace("\n", "")
		time, _, _, distance, _ = line.split()

		distance_recorded.append(float(distance))
		time_recorded.append(float(time))

	# draw	
	ax.plot(time_recorded, distance_recorded, label='Kp = 0.65, Ki = 0.0001, Kd = 0.02', linestyle='-')

time = np.linspace(0, 10,10)
target = time*0 + 300
# plot
ax.plot(time, target, color='red', label= 'target', linestyle='--')

plt.title('Distance by time')
plt.ylabel('Distance (mm)')
plt.xlabel('Time (s)')
plt.grid()
plt.legend()
plt.show()