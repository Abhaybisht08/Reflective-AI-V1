"""
reflection_layer.py

Core logic for the Reflective AI system.
Implements a Reflection Layer that aligns responses based on emotional, ethical, and timing-based inputs.

Author: Abhay & Team
Project: Reflective-AI-V1
"""

from typing import Dict, Optional

class ReflectionLayer:
    """
    Reflection Layer for ethical and emotional alignment of language model outputs.
    """

    def __init__(self):
        # Initialize parameters, thresholds, or any learning configs here
        self.reflection_rules = {
            "high_delay": "slow_down_response",
            "emotional_tone_low": "soften_language",
            "user_trigger_detected": "mirror_then_buffer",
        }

    def analyze_context(self, context: Dict) -> Dict:
        """
        Analyze incoming user context to extract reflective signals.
        Args:
            context (Dict): {
                'tone': str,
                'delay': float,
                'emotion': str,
                'user_trigger': Optional[str]
            }

        Returns:
            Dict: flags like {'soften': True, 'pause': True}
        """
        flags = {
            "soften": False,
            "pause": False,
            "mirror_first": False
        }

        if context.get("delay", 0) > 8.0:
            flags["pause"] = True

        if context.get("tone") in ["low", "sad", "frustrated"]:
            flags["soften"] = True

        if context.get("user_trigger") is not None:
            flags["mirror_first"] = True

        return flags

    def apply_reflection(self, raw_response: str, context_flags: Dict) -> str:
        """
        Modifies the raw response based on reflection flags.
        Args:
            raw_response (str): original LLM response
            context_flags (Dict): output from analyze_context()

        Returns:
            str: modified, aligned response
        """
        response = raw_response

        if context_flags.get("pause"):
            response = "Let me pause for a moment before we dive in.\n" + response

        if context_flags.get("soften"):
            response = self._soften_response(response)

        if context_flags.get("mirror_first"):
            response = "I hear you. That matters.\n" + response

        return response

    def _soften_response(self, response: str) -> str:
        """
        Internal method to soften language tone.
        """
        soft_prefix = "Here’s something gently for you:\n"
        return soft_prefix + response
