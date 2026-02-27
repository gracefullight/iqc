import random

import matplotlib.pyplot as plt
import sympy as sp


def exercise2(N=1000):
    """Goal: Compute and simulate measurement probabilities, then plot a histogram.

    Qubit: |ψ⟩ = 1/2|0⟩ + (√3/2)|1⟩
    Theoretical probabilities: P(0), P(1)
    Simulate N measurements and plot histogram.
    """
    # 1. Define the amplitudes for |0⟩ and |1⟩ using sympy for exact arithmetic
    #    |ψ⟩ = (1/2)|0⟩ + (√3/2)|1⟩
    amp_0 = sp.Rational(1, 2)  # Amplitude for |0⟩
    amp_1 = sp.sqrt(3) / 2  # Amplitude for |1⟩

    # 2. Calculate the measurement probabilities
    #    P(0) = |amp_0|^2, P(1) = |amp_1|^2
    p0 = sp.simplify(abs(amp_0) ** 2)
    p1 = sp.simplify(abs(amp_1) ** 2)
    print("Theoretical probabilities:")
    print(f"P(0) = |1/2|^2 = {float(p0):.3f}")
    print(f"P(1) = |√3/2|^2 = {float(p1):.3f}")

    # 3. Simulate N measurements using Python's random module
    #    For each trial, generate a random number r in [0,1).
    #    If r < P(0), record 0; else record 1.
    outcomes = []
    for _ in range(N):
        r = random.random()
        if r < p0:
            outcomes.append(0)
        else:
            outcomes.append(1)

    # 4. Plot a histogram (bar chart) of the measurement outcomes
    #    Compare the observed frequencies to the theoretical probabilities.
    count_0 = outcomes.count(0)
    count_1 = outcomes.count(1)
    plt.bar([0, 1], [count_0, count_1], tick_label=["0", "1"])
    plt.title(f"Measurement outcomes for N={N}")
    plt.xlabel("Outcome")
    plt.ylabel("Counts")
    # Annotate bars with observed frequencies
    plt.text(0, count_0, f"{count_0}", ha="center", va="bottom")
    plt.text(1, count_1, f"{count_1}", ha="center", va="bottom")
    plt.show()


if __name__ == "__main__":
    exercise2()
