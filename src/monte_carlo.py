import numpy as np
import matplotlib.pyplot as plt
from parameters import N_cells, N, p0, p1, p2, Lambda, ratio, C_w, exp_spcng, expr_mean, seed_ran
from kinematic import s_a

def simulation(n_trials: int = N, ratio: float=ratio, lam: float=Lambda) -> np.ndarray:
    
    # Generation of stochastic spacing data based on geaar-drive kinematics
    rng = np.random.default_rng(seed_ran)
    sa_cm = s_a(ratio, lam)*100
    outcomes = rng.choice([0, 1, 2], size=(n_trials, N_cells), 
                          p=[p0, p1, p2])
    spacing = []
    for trial in outcomes:
        for seeds in trial:
            if seeds == 0:
                continue
            spacing.append(sa_cm/seeds)

    return np.array(spacing)
