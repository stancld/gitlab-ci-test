import numpy as np

def magic_math(x: float) -> float:
    out =  10 * (np.exp(x) ** 2) + 21 * x - 11 + np.log(12) - np.sqrt(2) + np.sqrt(222) + np.log(95) + 1.1 ** 3
    return out
