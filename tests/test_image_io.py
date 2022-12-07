import pathlib

import numpy as np
from hypothesis import given
from hypothesis.extra.numpy import arrays
from hypothesis.strategies import integers, just, tuples

from steganosaure.image_io import load_image, save_image


def test_load_save_load(size_image_path: pathlib.Path) -> None:
    _filename = "a.png"
    original_image = load_image(size_image_path)
    save_image(original_image, _filename)
    new_image = load_image(_filename)
    np.testing.assert_array_equal(original_image, new_image)


@given(
    arrays(
        dtype="uint8",
        shape=tuples(
            integers(min_value=16, max_value=128),
            integers(min_value=16, max_value=128),
            just(3),
        ),
    )
)
def test_image_identity(array: np.ndarray) -> None:
    _filename = "a.png"
    save_image(array, _filename)
    img = load_image(_filename)
    np.testing.assert_array_equal(array, img)
