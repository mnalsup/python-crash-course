import matplotlib.pyplot as plt

plt.style.use('seaborn')
input = [num for num in range(0,5)]
squares = [num**2 for num in input]
cubes = [num**3 for num in input]
fig, ax = plt.subplots()
ax.plot(input, cubes)
ax.plot(input, squares, linewidth=3)

ax.set_title("Square")

plt.show()
