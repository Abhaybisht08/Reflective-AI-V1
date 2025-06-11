
from reflection_loader import load_reflection
from symbolic_mapper import map_to_symbols
from prompt_fuser import fuse_prompt

reflection = load_reflection()
symbols = map_to_symbols(reflection)
prompt = fuse_prompt(reflection, symbols)

print("Generated Creative Prompt:", prompt)
