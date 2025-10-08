"""
Plot the initial potential energy vs. final kinetic energy for a physics lab
@author Ben Wright
@version 2021.04.09
"""

import matplotlib.pyplot as plt

potential_energies = [0.020, 0.070]
kinetic_energies = [0.018, 0.058]
slope = (0.058 - 0.018) / (0.070 - 0.020)

fig = plt.figure()
plt.plot(potential_energies, kinetic_energies, 'bo-')
plt.xlabel('Potential Energy (J)')
plt.ylabel('Kinetic Energy (J)')
plt.title('Initial Potential Energy vs. Final Kinetic Energy for Two Hanging Masses')
plt.grid(True, lw=0.75)
plt.text(0.06, 0.020, f"slope: {slope:.3f}", c='b')
fig.savefig('potential_vs_kinetic')
plt.show()

