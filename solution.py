import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 944932368

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    p_val = cramervonmises_2samp(x, y).pvalue
    return p_val < alpha
