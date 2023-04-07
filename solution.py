import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 909631698 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p; t = 41; mu = 0.5; sigma = -np.exp(1)
    y = np.random.norm(mu, sigma, n) / t
    loc = y.mean()
    scale = np.sqrt(np.var(y)) / np.sqrt(len(y))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
