from parameters import gear_combinations, wheel_slip

def spacing(motor_A=8, moved_B=11, slip=wheel_slip): # Spacing calculation based on gear combinations
    
        seeds_m = gear_combinations.get((motor_A, moved_B))
        if seeds_m is None:
            raise ValueError(f"Sprocket combo ({motor_A}, {moved_B}) not in Gear combination table.")
            
        theor_s = 1.0/seeds_m # Theoretical Spacing
        actual_s = theor_s/(1-slip) 
        
        return actual_s
