"""
reflection_scoring.py

Module for scoring alignment between raw model response and its reflection.
Used for measuring depth, ethical alignment, and emotional tone improvement.
"""

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compute_reflection_scores(raw_output, reflected_output, embedding_model=None):
    """
    Computes alignment scores between raw and reflected outputs.

    Parameters:
    - raw_output: str, original LLM output
    - reflected_output: str, post-processed reflective output
    - embedding_model: optional sentence embedding model with encode() method

    Returns:
    - dict with alignment metrics:
        - cosine_similarity
        - delta_length
        - semantic_shift (if model provided)
    """

    scores = {
        "delta_length": abs(len(reflected_output) - len(raw_output))
    }

    if embedding_model:
        emb_raw = embedding_model.encode(raw_output, convert_to_tensor=True)
        emb_reflected = embedding_model.encode(reflected_output, convert_to_tensor=True)

        cosine_sim = cosine_similarity(
            emb_raw.cpu().detach().numpy().reshape(1, -1),
            emb_reflected.cpu().detach().numpy().reshape(1, -1)
        )[0][0]

        scores["semantic_alignment"] = round(cosine_sim, 4)
        scores["semantic_shift"] = round(1.0 - cosine_sim, 4)
    else:
        scores["semantic_alignment"] = "N/A (no model)"
        scores["semantic_shift"] = "N/A (no model)"

    return scores

