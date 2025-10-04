def recolor_clusters(img_np, labels_src, palette_old, palette_new,
                     ref_img_np=None, ref_labels=None):
    """
    Recolors img_np using per-cluster histogram matching to another image.
    
    Parameters:
        img_np (ndarray): Source image (H, W, 3)
        labels_src (ndarray): Cluster labels for source image
        palette_old (ndarray): Cluster centers of source image
        palette_new (ndarray): Cluster centers of reference image
        ref_img_np (ndarray): Reference image (H, W, 3)
        ref_labels (ndarray): Cluster labels of reference image
    
    Returns:
        recolored_img (ndarray): Histogram-matched recolored image
    """
    from skimage import exposure
    from scipy.spatial.distance import cdist
    import numpy as np

    H, W, C = img_np.shape
    result = np.zeros_like(img_np)

    # --- Match clusters between palettes (by color similarity) ---
    distances = cdist(palette_old, palette_new)
    mapping = np.argmin(distances, axis=1)

    # --- Histogram match per cluster ---
    for k_src, k_ref in enumerate(mapping):
        src_mask = (labels_src == k_src)
        if ref_img_np is None or ref_labels is None:
            # Fallback to global mean color
            ref_pixels = np.full_like(img_np[src_mask], palette_new[k_ref])
        else:
            ref_mask = (ref_labels == k_ref)
            ref_pixels = ref_img_np[ref_mask]
            if len(ref_pixels) == 0:
                ref_pixels = np.full_like(img_np[src_mask], palette_new[k_ref])

        src_pixels = img_np[src_mask]
        if len(src_pixels) == 0:
            continue

        matched = np.zeros_like(src_pixels)
        for c in range(3):  # RGB
            matched[:, c] = exposure.match_histograms(
                src_pixels[:, c], ref_pixels[:, c]
            )

        result[src_mask] = matched

    recolored_img = np.clip(result, 0, 255).astype(np.uint8)
    return recolored_img
