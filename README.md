# A Calibrated Stochastic Model for a Seed Metering Simulation

---

## Project Overview
This repository contains a Python simulation of a **26-cell seed metering plate** design for a metering mechanism calibrated with gear configurations (ratios) from the Baldan PLB row planter manual.

The project resolves the discrepancy between theoretical spacing of $20.0$ cm and the mean experimental field results of $21.7$ cm [1] by incoporating:
1. **Mechanical Tansmission:** Sprocket-to-plate ratios.
2. **Ground Wheel Slip ($\lambda$):** Modeling the interaction between soil and ground wheel.
3. **Stochastic Monte Carlo Model:** Accounts for the probablistc misses and double pickup events.

---

### 1. Mechanical Transmission
The simulation treats the metering mechanism as a mechanically linked system. Plate rotation is derived from ground wheel travel confined to a specified gear ratio.

**Reference:** Intergrated **Baldan PLB Gear Table**

**Transmission Equation:** 

$$S_{a} = \frac{1}{\text{SeedsPerMeter} \cdot (1 - \lambda)}$$

 Where $$\lambda$$ represents the ground-wheel slip coefficient.

### 2. Ground Wheel Slip
The variable is embedde in the mechanical tranmission model above

### 3. Stochastic Monte Carlo Model
