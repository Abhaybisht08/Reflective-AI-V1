"""
non_choice_interpreter.py

🤫 Detects silence, skipped choices, or delayed replies — signals for emotional state or reflection.

Module for interpreting user hesitation, silence, and non-selection behavior.
Inspired by the principle that 'not choosing is a form of choosing.'

Used to trigger gentle reflective prompts or EBR grounding.
"""

def detect_non_choice(user_input):
    """
    Detects non-committal or reflective user input patterns.

    Parameters:
    - user_input: str

    Returns:
    - dict with 'type': 'non_choice', 'action': recommendation
    """
    hesitation_keywords = ["...", "not sure", "maybe", "hmm", "I don’t know", "can't decide", "either way"]

    if any(hint in user_input.lower() for hint in hesitation_keywords):
        return {
            "type": "non_choice",
            "action": "reflective pause",
            "note": "User expressing hesitation or deep reflection. Avoid forced choices."
        }

    return {
        "type": "explicit_choice",
        "action": "proceed normally"
    }


# TODO: In future integration with TRP (temporal_profile.py),
# add timestamp-based silence detection logic:
# def interpret_silence(user_input_timestamps): ...

