# ===================================== 
# Project: Calibrated Stochastic Model 
# Author: Wezi Zimba (c) 2026
# =====================================

N = 10000 # Simulation trials
Lambda = 0.085 # Ground slip coeffecient
exp_spcng = 20.0 # expected spacin in [cm]
expr_mean = 21.7 # experimental mean in [cm]
seed_ran = 42 

# Mechanical Parameters
N_cells = 26 
C_w = 4.163

# Gear Calibration (from Baldan PLAB planter manual for 20cm spacing)
sprocket_A = 8 # Motor sprocket "A" 
sprocket_B = 11 # Moved sprocket "B"
ratio = sprocket_A/sprocket_B # Transmission (r)

# Event probabilities
p0 = 0.04
p1 = 0.94
p2 = 0.02
assert abs(p0+p1+p2-1) < 1e-9
