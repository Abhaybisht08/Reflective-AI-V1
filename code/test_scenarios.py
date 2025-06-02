
"""
test_scenarios.py

Simulates various test cases for the Reflective-AI pipeline.
Covers:
- Emotional triggers (EBR)
- Reflection logic
- TRP-influenced response modulation
"""

from reflection_layer import reflect_response
from emotion_buffer import apply_ebr_if_needed
from experimental.reflection_scoring import compute_reflection_scores


def run_test(prompt):
    print(f"🧪 Prompt: {prompt}")

    ebr_output = apply_ebr_if_needed(prompt)
    if ebr_output:
        print("System (EBR):", ebr_output)
        return

    # Simulate base LLM output
    base_output = f"Simulated response to: '{prompt}'"

    # Mirror and score
    reflected_output = reflect_response(prompt, base_output)
    scores = compute_reflection_scores(base_output, reflected_output)

    print("System (Raw):", base_output)
    print("System (Reflected):", reflected_output)
    print("→ Reflection Scores:", scores)
    print("-" * 60)


def main():
    test_prompts = [
        "I am feeling so lost and I don’t know what to do.",
        "Tell me a joke about AI.",
        "Can you explain quantum computing simply?",
        "Why did you ignore my last message?",
        "Everything feels like it's falling apart."
    ]

    for prompt in test_prompts:
        run_test(prompt)


if __name__ == "__main__":
    main()
