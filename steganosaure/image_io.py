from pathlib import Path
from typing import Union

import numpy as np
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte


def load_image(image_path: Union[Path, str]) -> np.ndarray:
    """
    Load an image.
    """
    return img_as_ubyte(imread(image_path))


def save_image(image: np.ndarray, image_path: Union[Path, str]) -> None:
    """
    Save an image.
    """
    imsave(image_path, image, plugin="pil", check_contrast=False)
