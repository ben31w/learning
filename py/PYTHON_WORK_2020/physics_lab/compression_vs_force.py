"""
Plot the compression vs. force of a spring, and calculate the spring constant
for a physics lab.
@author Ben Wright
@version 2021.04.09
"""

import matplotlib.pyplot as plt

compressions = [0, 0.005, 0.010, 0.017, 0.023, 0.032]
weights = [0, 1.96, 3.92, 5.88, 7.85, 9.81]

fl_compressions = [0, 0.032]
fl_weights = [0, 9.81]
slope = (9.81 / 0.032)

# Plot the data
fig = plt.figure()
plt.plot(compressions, weights, 'bo-')
plt.plot(fl_compressions, fl_weights, 'r--')
plt.xlabel('Compression (m)')
plt.ylabel('Force (N)')
plt.title('Spring Compression vs. Force')
plt.grid(True, lw=0.75)
plt.text(0.025, 0, f"slope: {slope}", c='r')
fig.savefig('compression_vs_force')
plt.show()
