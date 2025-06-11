# kundali_vector.py
# This module generates a symbolic personality vector based on Vedic Kundali planetary positions.

# Example structure — assumes planetary sign inputs and uses symbolic 3D mapping

sign_map = {
    'ARIES': [1, 0, 0],
    'TAURUS': [0.8, 0.2, 0],
    'GEMINI': [0.6, 0.4, 0.2],
    'CANCER': [0.2, 0.8, 0.6],
    'LEO': [1, 0.2, 0.2],
    'VIRGO': [0.5, 0.5, 0.3],
    'LIBRA': [0.7, 0.3, 0.4],
    'SCORPIO': [0.3, 1, 0.6],
    'SAGITTARIUS': [0.9, 0.2, 0.5],
    'CAPRICORN': [0.4, 0.6, 0.4],
    'AQUARIUS': [0.6, 0.3, 1],
    'PISCES': [0.2, 0.7, 1],
}

def generate_kundali_vector(planet_signs):
    vectors = [sign_map[sign] for sign in planet_signs.values()]
    avg_vector = [sum(x)/len(x) for x in zip(*vectors)]
    return avg_vector
