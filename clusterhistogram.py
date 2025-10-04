def recolor_clusters(img_np, labels, palette_old, palette_new):
   
    from skimage import exposure
    from scipy.spatial.distance import cdist
    import numpy as np

    H, W, C = img_np.shape
    result = np.zeros_like(img_np)

    # --- Step 1: Match clusters between palettes ---
    distances = cdist(palette_old, palette_new)
    mapping = np.argmin(distances, axis=1)

    # --- Step 2: Histogram match per cluster ---
    for k_src, k_ref in enumerate(mapping):
        src_mask = (labels == k_src)

        # Extract pixels for this cluster
        src_pixels = img_np[src_mask]

        if len(src_pixels) == 0:
            continue

        # Create synthetic "reference" color based on palette_new
        # (You can replace this with sampled pixels if you have a reference image)
        ref_color = np.full_like(src_pixels, palette_new[k_ref])

        # Match histogram of this cluster to the new cluster color distribution
        matched = np.zeros_like(src_pixels)
        for c in range(3):  # RGB
            matched[:, c] = exposure.match_histograms(
                src_pixels[:, c], ref_color[:, c]
            )

        result[src_mask] = matched

    # Clip + reshape to image
    recolored_img = np.clip(result, 0, 255).astype(np.uint8)
    return recolored_img
