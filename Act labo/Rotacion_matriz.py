# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 18:21:36 2025

@author: Julia
"""

import numpy as np
import pandas as pd

# Definir un ángulo de rotación de 45 grados
theta = np.radians(45)

# Matriz de rotación
T = np.array([[np.cos(theta), -np.sin(theta)], 
              [np.sin(theta), np.cos(theta)]])

# Guardar la matriz en un archivo CSV
pd.DataFrame(T).to_csv('Trot.csv', index=False, header=False)