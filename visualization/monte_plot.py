import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from parameters import exp_spcng, expr_mean
from monte_carlo import simulation


def carloPlot():
    spacings = simulation()
    mean = spacings.mean()
    std  = spacings.std()

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(spacings, bins=60, density=True, color="steelblue", edgecolor="white", alpha=0.7)

    x = np.linspace(spacings.min(), spacings.max(), 300)
    ax.plot(x, norm.pdf(x, mean, std), color="black", linewidth=1.5)

    ax.axvline(mean, color="blue", linewidth=1.2, linestyle="-", label=f"Sim. mean: {mean:.2f} cm")
    ax.axvline(expr_mean, color="red", linewidth=1.2, linestyle="--", label=f"Exp. mean: {expr_mean} cm")
    ax.axvline(exp_spcng, color="green", linewidth=1.2, linestyle=":", label=f"Target: {exp_spcng} cm")

    ax.set_xlabel("Intra-row Spacing [cm]")
    ax.set_ylabel("Probability Density")
    ax.set_title(f"Monte Carlo Spacing Distribution")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    carloPlot()
