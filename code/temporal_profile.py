"""
temporal_profile.py

Implements Temporal Response Profiling (TRP) for Reflective-AI-V1.
Captures timing-based behavioral signals such as delay between user prompt and response,
reading latency, and hesitation indicators to support emotionally aware mirroring.

Author: Abhay & Team
"""

import time
from typing import Dict

class TemporalProfile:
    """
    Tracks timing-based features of user interactions to detect emotional or reflective states.
    """

    def __init__(self):
        self.last_prompt_time = None
        self.last_response_time = None

    def log_prompt(self) -> None:
        """
        Call this method when a new user prompt is received.
        """
        self.last_prompt_time = time.time()

    def log_response(self) -> None:
        """
        Call this method when the AI mirror responds.
        """
        self.last_response_time = time.time()

    def calculate_response_delay(self) -> float:
        """
        Returns the delay between user prompt and AI response (in seconds).
        If either time is missing, returns -1.
        """
        if self.last_prompt_time and self.last_response_time:
            return round(self.last_response_time - self.last_prompt_time, 3)
        return -1.0

    def tag_delay(self, delay: float) -> str:
        """
        Tags delay into qualitative buckets.
        """
        if delay < 1.5:
            return "impulsive"
        elif 1.5 <= delay < 5:
            return "neutral"
        elif 5 <= delay < 15:
            return "reflective"
        else:
            return "hesitant"

    def profile(self) -> Dict:
        """
        Returns a complete temporal profile after a prompt-response round.
        """
        delay = self.calculate_response_delay()
        return {
            "delay": delay,
            "timing_tag": self.tag_delay(delay)
        }

