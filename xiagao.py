# coding: utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

for i in range(0,200):
    x=i
    k=-0.3274*x**3 + 89.72*x**2 - 4034*x +3.29e+04
    print(str(int(k)))