import numpy as np
import pytest
from hypothesis import given
from hypothesis.strategies import text

from steganosaure.string_conversion import decode_bits, encode_string

_sample_bits = np.array(
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
)


def test_encode_string1() -> None:
    r = encode_string("")
    assert r.size == 0


def test_encode_string2() -> None:
    r = encode_string("x")
    assert r.size == 8


def test_encode_string3() -> None:
    r = encode_string("ABC")
    assert np.all(r == _sample_bits)
    np.testing.assert_array_equal(r, _sample_bits)


def test_decode_bits1() -> None:
    r = decode_bits(_sample_bits)
    assert r == "ABC"


@given(text())
def test_encode_then_decode(sample_string: str) -> None:
    assert decode_bits(encode_string(sample_string)) == sample_string


@pytest.mark.parametrize(
    "input, output",
    [
        ("", []),
        (
            "ABC",
            np.array(
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
            ),
        ),
    ],
)
def test_encode_string(input: str, output: np.ndarray) -> None:
    np.testing.assert_array_equal(encode_string(input), output)


@pytest.mark.parametrize(
    "input, output",
    [
        (
            np.array(
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
            ),
            "ABC",
        ),
    ],
)
def test_decode_bits(input: np.ndarray, output: str) -> None:
    assert decode_bits(input) == output
