import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(1, 15, 1000)  # From 0 to 10 seconds, with 1000 points

# Define the function y(t)
y = np.sin(t - np.pi/4)  # Define the original function, y(t) = sin(t - pi/4)

# Plot the graph
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')

# Set x-axis ticks for every 1 unit distance
plt.xticks(np.arange(1, 16, 1))

plt.grid(True)
plt.savefig("graph.png")
