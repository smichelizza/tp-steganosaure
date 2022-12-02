"""Stegosaure command line interface."""

import pathlib
from argparse import ArgumentParser

from .steganography import decrypt, encrypt


def _create_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="steganosaure", description="Hide messages in images")
    subparsers = parser.add_subparsers(help="Commands", dest="command", required=True)

    parser_encode = subparsers.add_parser("encrypt")
    parser_encode.add_argument("message")
    parser_encode.add_argument("input_image_path", type=pathlib.Path)
    parser_encode.add_argument("output_image_path", type=pathlib.Path)

    parser_decode = subparsers.add_parser("decrypt")
    parser_decode.add_argument("image_path", type=pathlib.Path)
    return parser


def main() -> None:
    """Entrypoint of the program."""
    parser = _create_parser()
    args = parser.parse_args()
    if args.command == "encrypt":
        encrypt(args.message, args.input_image_path, args.output_image_path)
    else:
        print(decrypt(args.image_path))
