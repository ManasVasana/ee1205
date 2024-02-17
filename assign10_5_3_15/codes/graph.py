import matplotlib.pyplot as plt
with open("sequence_points.txt", 'r') as file:
    sequence = [int(line.strip()) for line in file]
n_values = range(0, len(sequence))

# Create stem plot with blue markers for most points
plt.stem(n_values[:-1], sequence[:-1], markerfmt='bo', linefmt='b-', basefmt='k-')
# Plot the last point with a red cross marker
plt.stem(n_values[-1:], sequence[-1:], markerfmt='rx', linefmt='r-', basefmt='k-')
plt.xlabel("n")
plt.ylabel("y(n)")
plt.grid(True)
plt.savefig("graph.png")
