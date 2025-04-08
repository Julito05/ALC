# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 21:11:18 2025

@author: Julia
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:55:19 2025

@author: Julia
"""

import numpy as np
import pandas as pd

# Definir un ángulo de rotación de 45 grados
theta = np.radians(-45)

# Matriz de rotación
T = np.array([[np.cos(theta), -np.sin(theta), 10], 
              [np.sin(theta), np.cos(theta), 20],
              [0, 0, 1]])

# Guardar la matriz en un archivo CSV
pd.DataFrame(T).to_csv('TrotCont.csv', index=False, header=False)