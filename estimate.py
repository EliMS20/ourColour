import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
from skimage import color

def estimate_distinct_colors_lab(
    img_input,
    max_k=64,
    distance_thresh=10,
    sample_pixels=100_000,
    random_state=42
):
    """
    Estimate visually distinct colors using perceptual LAB color distance.

    Parameters:
        img_input (str or ndarray): Path to image or image array.
        max_k (int): Max number of clusters for initial color grouping.
        distance_thresh (float): LAB Euclidean distance threshold for merging (ΔE).
                                 ~2 = very similar, 10–20 = noticeable, 30+ = very distinct.
        sample_pixels (int): Number of random pixels to sample for speed.
        random_state (int): Random seed for reproducibility.

    Returns:
        (int, list[np.ndarray]): (count, list of representative colors [RGB uint8])
    """
    # Load and prepare image
    if isinstance(img_input, str):
        arr = np.array(Image.open(img_input).convert("RGB"))
    else:
        arr = np.array(img_input)
        if arr.ndim == 2:
            arr = np.stack([arr]*3, axis=-1)
    pixels = arr.reshape(-1, 3).astype(np.uint8)
    n = pixels.shape[0]

    # Random sampling for large images
    rng = np.random.default_rng(random_state)
    if n > sample_pixels:
        idx = rng.choice(n, size=sample_pixels, replace=False)
        sample = pixels[idx]
    else:
        sample = pixels

    # Over-cluster the pixels with KMeans
    uniq = np.unique(sample, axis=0)
    k = min(max_k, len(uniq))
    km = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    labels = km.fit_predict(sample)
    centroids = km.cluster_centers_
    counts = np.bincount(labels, minlength=len(centroids))

    # Convert to LAB for perceptual distance
    lab_centroids = color.rgb2lab(centroids.reshape(1, -1, 3) / 255.0).reshape(-1, 3)

    # Pairwise distances in LAB space
    D = squareform(pdist(lab_centroids))

    # Union-Find to merge close colors (transitive merging)
    parent = list(range(len(centroids)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in range(len(centroids)):
        for j in range(i + 1, len(centroids)):
            if D[i, j] < distance_thresh:
                union(i, j)

    # Group centroids and compute representative colors
    groups = {}
    for i in range(len(centroids)):
        r = find(i)
        groups.setdefault(r, []).append(i)

    reps = []
    for grp in groups.values():
        grp = np.array(grp)
        w = counts[grp].astype(float)
        weighted = np.average(centroids[grp], axis=0, weights=w)
        reps.append(np.clip(weighted.round(), 0, 255).astype(np.uint8))

    return len(reps), reps