import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 909631698 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    t = 41
    loc = (x.mean() + 0.5) / 840.5
    scale = np.sqrt(np.var(x)) / (840.5 * np.sqrt(len(x)))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
