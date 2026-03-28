from parameters import N_cells, C_w, ratio, Lambda

def S_m(ratio: float=ratio) -> float:
    'Seeds delivered every meter of forward travel'
    'Sm=(Nxr)/Cw'
    return (N_cells*ratio)/C_w

def s_t(ratio: float=ratio) -> float:
    'Theoretical intra-row spacing in [m] withput slip'
    'st=Cw/(Nxr)'
    return C_w/(N_cells*ratio)

def s_a(ratio: float=ratio, lam: float=Lambda) -> float:
    'Actual spacing in [m] with ground slip accounted for'
    'sa=st/(1-lambda)'
    return s_t(ratio)/(1-lam)
