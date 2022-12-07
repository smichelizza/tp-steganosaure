from pathlib import Path
from typing import Union

import numpy as np

from steganosaure.bits_manipulation import (
    modify_least_significant_bits,
    retrieve_least_significant_bits,
)
from steganosaure.image_io import load_image, save_image
from steganosaure.string_conversion import decode_bits, encode_string


def encrypt(
    message: str,
    input_image_path: Union[Path, str],
    output_image_path: Union[Path, str],
) -> None:
    input_image = load_image(input_image_path)
    flat_image = input_image.reshape(-1)
    bits = encode_string(message)
    bits_padded = np.pad(bits, (0, flat_image.size - bits.size))

    flat_modified = modify_least_significant_bits(bits_padded, flat_image)

    reconstructed_image = flat_modified.reshape(input_image.shape)
    save_image(reconstructed_image, output_image_path)


def decrypt(image_path: Union[Path, str]) -> str:
    input_image = load_image(image_path)
    flat_image = input_image.reshape(-1)
    bits = retrieve_least_significant_bits(flat_image)
    return decode_bits(bits).rstrip("\x00")
