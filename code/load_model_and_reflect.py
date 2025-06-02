"""
load_model_and_reflect.py

Loads base LLM (e.g., GPT-J, Mistral) and injects reflection-aware processing.
Adds hooks for:
- Trigger detection
- Reflection scoring
- EBR/Mirror outputs

"""

# load_model_and_reflect.py

"""
Load Model and Reflect
----------------------
This module handles prompt passing to a language model (e.g., GPT-4) and
post-processes the response through the Reflection Layer and Emotional Buffer.
"""

import openai
import os
from emotion_buffer import apply_ebr_if_needed
from reflection_layer import reflect_response

# Set your OpenAI API key from environment or direct assignment
openai.api_key = os.getenv("OPENAI_API_KEY", "your-key-here")

def get_raw_response(prompt: str, model: str = "gpt-4") -> str:
    """
    Sends prompt to the language model and returns raw response.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()

def get_reflected_output(user_input: str, apply_reflection: bool = True) -> str:
    """
    Main pipeline: handles EBR → LLM → Reflection (if enabled).
    """
    # Step 1: Emotional buffering
    ebr_result = apply_ebr_if_needed(user_input)
    if ebr_result["status"] == "buffered":
        return ebr_result["response"]

    # Step 2: Get raw model response
    raw_output = get_raw_response(user_input)

    # Step 3: Apply reflection layer
    if apply_reflection:
        return reflect_response(user_input, raw_output)
    else:
        return raw_output

# --- Demo/Test ---
if __name__ == "__main__":
    prompt = "I feel very anxious and unsure what to do next."
    result = get_reflected_output(prompt)
    print("\nFinal Output:\n", result)
