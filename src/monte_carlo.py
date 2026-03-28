import numpy as np
from parameters import N_cells, N, p0, p1, p2, Lambda, ratio, seed_ran
from kinematic import s_a

def simulation(n_trials: int = N, ratio: float=ratio, lam: float=Lambda) -> np.ndarray:
    
    # Generation of stochastic spacing data based on geaar-drive kinematics
        # Each cell pass draws from three outcomes: 
        # X=0 (p0), X=1 (p1), X=2 (p2)
    rng = np.random.default_rng(seed_ran)
    sa_cm = s_a(ratio, lam)*100
    outcomes = rng.choice([0, 1, 2], size=(n_trials, N_cells), 
                          p=[p0, p1, p2])
    spacings = []
    for trial in outcomes:
        for seeds in trial:
            if seeds == 0:
                continue
            spacings.append(sa_cm/seeds)

    return np.array(spacings)
