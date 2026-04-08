# Calibrated Stochastic Model for a Seed Metering Simulation

## Project Overview
This repository contains a Python simulation of a **26-cell seed metering plate** design for a metering mechanism calibrated with gear configurations (ratios) from the Baldan PLB row planter manual. 

The project resolves the discrepancy between theoretical spacing of $20.0$ cm and the mean experimental field results of $20.35$ cm [1] by incoporating:
1. **Mechanical Tansmission:** Sprocket-to-plate ratios.
2. **Ground Wheel Slip ($\lambda$):** Modeling the interaction between soil and ground wheel.
3. **Stochastic Monte Carlo Model:** Accounts for the probablistc misses and double pickup events.

A ground slip of **$\lambda$ = 8.5%** is identified as a significant physical cause.

This project is a computational extension of the Bachelor thesis [1] 

---

### 1. Mechanical Transmission
The simulation treats the metering mechanism as a mechanically linked system. From the ground wheel through a chain-and-sprocket transmission. Plate rotation is derived from ground wheel travel confined to a specified gear ratio.

**Reference:** Intergrated **Baldan PLB Gear Table**

The number of seeds delivered in a meter is:

$$s_m = \frac{N \cdot r}{C_w}$$

Where $$r$$ is the transmission ratio

Theoretical intra-row spacing is therefore:

$$s_t = \frac{C_w}{N \cdot r}$$

**Transmission Equation:** 

$$S_{a} = \frac{1}{S_m \cdot (1 - \lambda)}$$

 Where $$\lambda$$ represents the ground-wheel slip coefficient.

### 2. Ground Wheel Slip
This occurs when the wheel rotates through an angle that reduces actual ground contaact and delivers less forward motion.

Actual spacing under slip is: 

$$S_a = \frac{s_t}{1 - \lambda}$$

### 3. Stochastic Model
To capture real-world disturbances, the model runs 10,000 trials and variablity through probabilistic pickup events is added. Each cell pass is modeled as a random draw from three outcomes:

**Event Probabilities:** 

a) Empty cell (p0): 0.04; 

b) Single seed (p1): 0.94; 

c) Double pickup (p2): 0.02;

The constraint: p0 + p1 + p2 = 1 is enforced

The total number of seeds for a give cell pass can be represented as: 

$$S_{total} = \sum_{i=1}^{N} X_i$$

Where $$X$$ is a discrete random variable with the probability mass function:

$P(X=0) = 0.04$

$P(X=1) = 0.94$

$P(X=2) = 0.02$

---

## Experimental Validation
The simulation was calibrated using experimental data collected at a constant foward speed of **4.0 km/h**. Results are recorded in 'data/experimental_data.csv'

---

## Reference
[1] Zimba, W. Construction of a Metering System for Maize Seed using Additive Manufacturing Technology, (2024). Department of Agricultural Engineering, University of Zambia. (Unpublished)

---
## Legal Notice
This project is a computational extension of a Bachelor's thesis conducted at the University of Zambia (2024). The simulation code is the original work of the author. The experimental data referenced belongs to the associated thesis.
