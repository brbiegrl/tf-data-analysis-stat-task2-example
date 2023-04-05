import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 909631698 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    y = 0.5 - 2*x/(41**2)
    loc = y.mean()
    scale = np.sqrt(np.var(y)) / np.sqrt(len(y))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
