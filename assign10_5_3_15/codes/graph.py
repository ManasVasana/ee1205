import matplotlib.pyplot as plt

def plot_stem_graph_from_file(filename):
    with open(filename, 'r') as file:
        sequence = [int(line.strip()) for line in file]

    n_values = range(1, len(sequence) + 1)
    plt.stem(n_values, sequence, markerfmt='o', linefmt='b-', basefmt='k-')
    plt.title("Sequence: y(n) = (n+1)/2 * (2*x(0) + n*d) u(n)")
    plt.xlabel("n")
    plt.ylabel("y(n)")
    plt.grid(True)
    plt.savefig("graph.png")

# Example usage
plot_stem_graph_from_file("sequence_points.txt")
