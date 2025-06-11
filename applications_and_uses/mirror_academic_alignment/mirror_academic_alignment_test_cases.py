
from applicant_vector import get_applicant_vector
from lab_vector import get_lab_vector
from alignment_score import match_vectors

applicant = get_applicant_vector()
lab = get_lab_vector()
score = match_vectors(applicant, lab)

print(f"Academic Alignment Score: {score:.2f}")
