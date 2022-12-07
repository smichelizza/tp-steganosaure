import numpy as np


def retrieve_least_significant_bits(array: np.ndarray) -> np.ndarray:
    # return array % 2
    return array & 1


def modify_least_significant_bits(message: np.ndarray, image: np.ndarray) -> np.ndarray:
    # return image & 0b11111110 | retrieve_least_significant_bits(message)
    return image >> 1 << 1 | retrieve_least_significant_bits(message)
