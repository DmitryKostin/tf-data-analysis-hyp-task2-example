import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 944932368

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    return anderson_ksamp([x, y]).pvalue < alpha
