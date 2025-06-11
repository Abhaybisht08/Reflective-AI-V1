
from kundali_vector import generate_kundali_vector
from mirror_vector import load_mirror_vector
from cosine_matcher import match_vectors

sample_kundali = {
    'Sun': 'AQUARIUS',
    'Moon': 'CANCER',
    'Mars': 'LIBRA',
    'Mercury': 'CAPRICORN',
    'Jupiter': 'SAGITTARIUS',
    'Venus': 'PISCES',
    'Saturn': 'AQUARIUS',
    'Rahu': 'CANCER',
    'Ketu': 'CAPRICORN'
}

kundali_vector = generate_kundali_vector(sample_kundali)
mirror_vector = load_mirror_vector()
score = match_vectors(kundali_vector, mirror_vector)

print(f"Mirror–Kundali Alignment Score: {score:.2f}")
