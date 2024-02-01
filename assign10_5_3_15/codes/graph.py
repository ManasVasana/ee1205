import matplotlib.pyplot as plt

def generate_sequence(x0, d, n):
    return [x0 + i * d for i in range(n)]

def plot_sequence(x0, d, n):
    sequence = generate_sequence(x0, d, n)
    plt.plot(sequence, marker='o')
    plt.title(f"Sequence: x(n) = x(0) + n * d")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.grid(True)
    plt.savefig("graph.png")

# Example usage with x0=200, d=50, and n=30
x0 = 200  # initial value
d = 50    # common difference
n = 30    # number of terms

plot_sequence(x0, d, n)
