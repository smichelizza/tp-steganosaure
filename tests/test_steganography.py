import pathlib

from hypothesis import given
from hypothesis.strategies import text

from steganosaure.steganography import decrypt, encrypt


@given(sample_string=text())
def test_encrypt_then_decrypt(
    size_image_path: pathlib.Path, sample_string: str
) -> None:
    output_filepath = "a.png"
    encrypt(sample_string, size_image_path, output_filepath)
    output_message = decrypt(output_filepath)
    assert sample_string == output_message
