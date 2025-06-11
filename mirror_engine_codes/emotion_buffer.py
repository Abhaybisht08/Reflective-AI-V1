# emotion_buffer.py

"""
Emotional Buffer Response (EBR) Module
--------------------------------------
This module detects emotional urgency in user input and returns a buffered,
calming response before the system proceeds with final reasoning.

EBR is part of the Reflective-AI architecture for ethical and human-centered dialogue.
"""

import re
from typing import Dict

# Define emotional urgency keywords and emotional tone patterns
EMOTIONAL_URGENCY_KEYWORDS = [
    "panic", "lost", "urgent", "confused", "help", "emergency",
    "stuck", "overwhelmed", "don't know", "crying", "hopeless"
]

VALIDATION_RESPONSES = [
    "I'm here with you. Let's take a moment before we move forward.",
    "Take a deep breath. You're not alone. I'm listening.",
    "I sense this matters to you. Let's slow down and understand together.",
    "Let’s pause first — what you’re feeling is valid."
]

def detect_emotional_urgency(user_input: str) -> bool:
    """
    Detects if the user's input indicates emotional urgency.
    Returns True if such a signal is detected.
    """
    lower_input = user_input.lower()
    return any(keyword in lower_input for keyword in EMOTIONAL_URGENCY_KEYWORDS)

def generate_buffer_response() -> str:
    """
    Returns a grounding response from the buffer pool.
    """
    import random
    return random.choice(VALIDATION_RESPONSES)

def apply_ebr_if_needed(user_input: str) -> Dict[str, str]:
    """
    Applies Emotional Buffer Response if user input is emotionally urgent.
    Returns a dictionary with status and either original or buffered reply.
    """
    if detect_emotional_urgency(user_input):
        return {
            "status": "buffered",
            "response": generate_buffer_response()
        }
    else:
        return {
            "status": "pass_through",
            "response": user_input
        }

# --- For test/demo ---
if __name__ == "__main__":
    test_input = "I'm feeling completely lost and don’t know what to do."
    result = apply_ebr_if_needed(test_input)
    print(result)
