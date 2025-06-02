
"""
alignment_metrics.py

Module for evaluating how well model outputs reflect user intent,
emotional tone, and reflective depth.
📏 Metrics to measure how well the model mirrors the user — across tone, attention, and intent.
Includes: mirror confidence score, divergence index, tone similarity.
"""

import numpy as np
from sklearn.metrics import accuracy_score, f1_score

def compute_token_alignment(predicted_tokens, reflected_tokens):
    """
    Computes simple token-level alignment accuracy.

    Parameters:
    - predicted_tokens: list of strings (from original model output)
    - reflected_tokens: list of strings (from reflected response)

    Returns:
    - float accuracy
    """
    min_len = min(len(predicted_tokens), len(reflected_tokens))
    correct = sum(1 for i in range(min_len) if predicted_tokens[i] == reflected_tokens[i])
    return correct / max(len(predicted_tokens), 1)

def compute_sentiment_shift_score(pred_sentiment, refl_sentiment):
    """
    Computes a score penalizing strong sentiment divergence.

    Parameters:
    - pred_sentiment: float in [-1, 1]
    - refl_sentiment: float in [-1, 1]

    Returns:
    - float score (0 = worst shift, 1 = aligned tone)
    """
    return 1.0 - abs(pred_sentiment - refl_sentiment)

def compute_delay_score(read_delay, reply_delay):
    """
    Computes normalized delay behavior score. Ideal replies occur after reflection pause.

    Parameters:
    - read_delay: float (seconds between user sending and reading)
    - reply_delay: float (seconds taken to respond)

    Returns:
    - float score between 0 and 1 (higher = better reflective pacing)
    """
    if reply_delay <= 0:
        return 0.0
    delay_ratio = read_delay / reply_delay
    return min(1.0, max(0.0, delay_ratio))

def calculate_mirror_confidence(response_tokens, reflection_tokens, pred_sentiment, refl_sentiment):
    """
    Combines token alignment and tone similarity to produce mirror confidence score.

    Parameters:
    - response_tokens: list of tokens from raw output
    - reflection_tokens: list of tokens from reflected output
    - pred_sentiment: float sentiment of original output
    - refl_sentiment: float sentiment of reflected output

    Returns:
    - float mirror confidence score (0–1)
    """
    alignment = compute_token_alignment(response_tokens, reflection_tokens)
    tone_match = compute_sentiment_shift_score(pred_sentiment, refl_sentiment)
    return 0.5 * alignment + 0.5 * tone_match
