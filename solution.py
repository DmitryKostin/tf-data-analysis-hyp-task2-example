import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 944932368

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    statistic, pvalue = ks_2samp(x, y)
    return pvalue < alpha
