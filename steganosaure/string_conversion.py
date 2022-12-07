import numpy as np


def encode_string(string: str) -> np.ndarray:
    return np.unpackbits(np.array([c for c in string.encode()], dtype=np.uint8))


def decode_bits(bits: np.ndarray) -> str:
    return bytes(np.packbits(bits)).decode()
