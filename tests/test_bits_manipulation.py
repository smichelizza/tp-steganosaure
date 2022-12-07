import numpy as np
from hypothesis import given
from hypothesis.extra.numpy import arrays
from hypothesis.strategies import integers

from steganosaure.bits_manipulation import (
    modify_least_significant_bits,
    retrieve_least_significant_bits,
)


@given(
    arrays(
        dtype="uint8",
        shape=integers(min_value=16, max_value=1024),
        elements=integers(min_value=0, max_value=1),
    )
)
def test_trivial_lsb(bits: np.ndarray) -> None:
    np.testing.assert_array_equal(bits, retrieve_least_significant_bits(bits))


def test_retrieve_simple_example() -> None:
    np.testing.assert_array_equal(
        np.array([1, 0, 1]), retrieve_least_significant_bits(np.array([1, 2, 3]))
    )


def test_modify_simple_example() -> None:
    np.testing.assert_array_equal(
        np.array([0, 3, 2]),
        modify_least_significant_bits(np.array([0, 1, 0]), np.array([1, 2, 3])),
    )


@given(
    arrays(
        dtype="uint8",
        shape=integers(min_value=16, max_value=1024),
        elements=integers(min_value=0, max_value=1),
    )
)
def test_modify(bits: np.ndarray) -> None:
    np.testing.assert_array_equal(
        modify_least_significant_bits(bits, np.zeros_like(bits, dtype="uint8")), bits
    )
