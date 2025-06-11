
from dialogue_parser import parse_dialogue
from mirror_response_layer import enhance_response

sample = "I'm not sure if I can do this."
parsed = parse_dialogue(sample)
enhanced = enhance_response(parsed)

print("Enhanced Response:", enhanced)
