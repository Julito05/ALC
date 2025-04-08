# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:50:08 2025

@author: Julia
"""

import numpy as np
import pandas as pd

# Rotación de 45°
theta = np.radians(45)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])

# Rotación de -45°
R_inv = np.array([[np.cos(-theta), -np.sin(-theta)],
                  [np.sin(-theta),  np.cos(-theta)]])

# Escalado
S = np.array([[2, 0],
              [0, 3]])

# Composición: R_inv @ S @ R
T = R_inv @ S @ R

# Guardar en CSV
pd.DataFrame(T).to_csv("TroInv.csv", index=False, header=False)
