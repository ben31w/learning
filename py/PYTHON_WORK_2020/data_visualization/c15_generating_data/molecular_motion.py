"""
Visualizing the path of a pollen grain on the surface of a drop of water, as
it keeps getting pushed in random directions by water molecules.
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break