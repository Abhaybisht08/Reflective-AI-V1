
from person1_vector import get_person1_vector
from person2_vector import get_person2_vector
from relationship_map import compute_relationship_map

p1 = get_person1_vector()
p2 = get_person2_vector()
map = compute_relationship_map(p1, p2)

print("Relationship Map Output:", map)
