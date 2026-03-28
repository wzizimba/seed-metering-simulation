from parameters import N_cells, C_w, ratio, Lambda

def S_m(ratio: float=ratio) -> float:
    return (N_cells*ratio)/C_w

def s_t(ratio: float=ratio) -> float:
    return C_w/(N_cells*ratio)

def s_a(ratio: float=ratio, lam: float=Lambda) -> float:
    return s_t(ratio)/(1-lam)
