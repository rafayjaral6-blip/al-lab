from pathlib import Path

import numpy as np
from PIL import Image


def image_to_features(path: str | Path, size: tuple[int, int] = (64, 64)) -> np.ndarray:
    """Load an image, convert it to grayscale, resize it, and flatten its pixels.

    Args:
        path: Image file path.
        size: Target image size as (width, height).

    Returns:
        A one-dimensional uint8 array with size[0] * size[1] pixel values.
    """
    with Image.open(path) as image:
        grayscale = image.convert("L").resize(size)
        return np.asarray(grayscale, dtype=np.uint8).flatten()
