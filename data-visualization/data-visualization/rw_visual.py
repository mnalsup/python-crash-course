import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    plt.style.use('classic')
    fig,ax = plt.subplots()
    
    rw = RandomWalk(10000)
    rw.fill_walk()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    
    rw2 = RandomWalk(10000)
    rw2.fill_walk()
    point_numbers = range(rw2.num_points)
    ax.scatter(rw2.x_values, rw2.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
    
    rw3 = RandomWalk(10_000)
    rw3.fill_walk()
    point_numbers = range(rw3.num_points)
    ax.scatter(rw3.x_values, rw3.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none', s=15)

    plt.show()
