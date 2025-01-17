import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

import math

chat_id = 393669278 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы


    alpha = 1-p
    n = x.size
    mean = x.mean()

    var_est = np.var(x)

    xi1 = chi2.ppf(1-(alpha/2), n)
    xi2 = chi2.ppf((alpha/2), n)

    return math.sqrt(((n-1)*var_est/xi1)/13), \
           math.sqrt(((n-1)*var_est/xi2)/13)
