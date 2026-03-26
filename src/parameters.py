# import os 
# read = os.path.dirname(os.path.abspath(__file__))
# data_path = os.path.join(read, '..', 'data', 'experimental_results.csv')

# Constants 
N = 10000
Seed_ran = 42
noise_frac = 0.015
p_miss = 0.05
p_double = 0.02

# Baldan PLB gear table 9from manual)
gear_combinations = {
    (8, 15): 3.5, (8, 13): 4.0, (8, 12): 4.5,
    (8, 11): 5.0, (8, 10): 5.5, (8, 9): 6.0,
    (8, 8): 6.5,  (9, 8): 7.5,  (10, 8): 8.5
}

# Calibartion
motor_A = 8
motor_B = 11
dia_wheel = 0.64
wheel_slip = 0.085
N_cells = 26

# Operation
speed_kph = 4.0
speed_mps = speed_kph/3.6
