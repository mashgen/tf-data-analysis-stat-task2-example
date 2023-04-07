import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 156090715 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = len(x)*(x*x).mean()
    return ((1/35)*loc / chi2.ppf(1-alpha/2, df=2*len(x)))**0.5, \
           ((1/35)*loc / chi2.ppf(alpha/2, df=2*len(x)))**0.5
