import matplotlib.pyplot as plt

# Read data from output.txt
x_stem = []
y_stem = []
with open("output.txt", "r") as file:
    next(file)  # skip header
    for line in file:
        n, y = map(float, line.strip().split())
        x_stem.append(int(n))
        y_stem.append(y)

# Read data from result_terms.txt
y_scatter = []
with open("result_terms.txt", "r") as file:
    for line in file:
        y_scatter.append(int(line.strip()))

# Plot stem plot
plt.stem(x_stem, y_stem, linefmt='b-', markerfmt='bo', basefmt=' ')

# Plot scatter plot
plt.scatter(range(len(y_scatter)), y_scatter, color='r', marker='X', zorder=5)  # zorder for bringing it to the front

# Highlight y(n) = 27750 with yellow color
highlight_index = y_stem.index(27750)
plt.scatter([highlight_index], [27750], color='yellow', zorder=6)  # zorder for bringing it to the front

# Add labels and title
plt.xlabel('n')
plt.ylabel('y(n)')

# Show plot
plt.savefig("graph.png")
