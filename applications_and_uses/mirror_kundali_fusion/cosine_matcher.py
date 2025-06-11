# cosine_matcher.py
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def match_vectors(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0]
