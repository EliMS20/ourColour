import numpy as np
from skimage import color

def smooth_recolor_one(img_np, old_color, new_color, sigma=10):
    """
        img_np (ndarray): Input RGB image (uint8)
        old_color (ndarray): Old RGB color (3,)
        new_color (ndarray): New RGB color (3,)
        sigma (float): Controls smoothness of transition (ΔE range)
        RETURN-
        recolored image (uint8)
    """
    img_lab = color.rgb2lab(img_np / 255.0)
    old_lab = color.rgb2lab(np.array([[old_color]]) / 255.0)[0, 0]
    new_lab = color.rgb2lab(np.array([[new_color]]) / 255.0)[0, 0]

    # LAB distance map
    dist = np.linalg.norm(img_lab - old_lab, axis=-1)
    weights = np.exp(-(dist**2) / (2 * sigma**2))

    # Apply weighted shift
    shift = new_lab - old_lab
    img_lab += weights[..., np.newaxis] * shift

    recolored = color.lab2rgb(img_lab)
    return np.clip(recolored * 255, 0, 255).astype(np.uint8)
