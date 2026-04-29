import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from parameters import ratio, Lambda, exp_spcng, expr_mean, sprocket_A, sprocket_B
from kinematic import s_a


def contour():
    ratios = np.linspace(0.4, 1.4, 300)
    slips = [0.0, 0.05, 0.085, 0.12]
    linestyles=["-","--","-.",":"]

    fig, ax = plt.subplots(figsize=(8, 5))

    for lam, ls in zip(slips,linestyles):
        spacings = [s_a(r, lam)*100 for r in ratios]
        ax.plot(ratios, spacings, color="black", linestyle=ls,
                linewidth=1.5,label=f"Lambda = {lam:.1%}")

    ax.axhline(exp_spcng, color='gray', linestyle="--", linewidth=1.2, label=f"Target: {exp_spcng} cm")
    ax.axhline(expr_mean, color="gray", linestyle=":", linewidth=1.2, label=f"Experimental mean: {expr_mean} cm")
    ax.axvline(ratio, color="gray", linestyle="-.", linewidth=1, label=f"Gear Ratio: {sprocket_A}/{sprocket_B} = {ratio:.3f}")

    ax.set_xlabel("Transmission Ratio r = A/B")
    ax.set_ylabel("Actual Spacing Sa [cm]")
    ax.set_title("Kinematic Spacing Contour (26-cell plate)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    contour()
