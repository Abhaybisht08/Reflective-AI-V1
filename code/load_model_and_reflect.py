
"""
load_model_and_reflect.py

Loads base LLM (e.g., GPT-J, Mistral) and injects reflection-aware processing.
Adds hooks for:
- Trigger detection
- Reflection scoring
- EBR/Mirror outputs
"""

from openai import ChatCompletion
from reflection_layer import reflect_response
from emotion_buffer import apply_ebr_if_needed
from experimental.reflection_scoring import compute_reflection_scores


def get_raw_response(prompt):
    completion = ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message["content"]


def main():
    user_prompt = input("User: ")

    # Step 1: Check emotional triggers (EBR)
    ebr_output = apply_ebr_if_needed(user_prompt)
    if ebr_output:
        print("System (EBR):", ebr_output)
        return

    # Step 2: Get raw LLM response
    raw_output = get_raw_response(user_prompt)

    # Step 3: Reflect the response
    reflected_output = reflect_response(user_prompt, raw_output)

    # Step 4: Compute reflection metrics
    scores = compute_reflection_scores(raw_output, reflected_output)

    # Step 5: Output with metrics
    print("System (Raw):", raw_output)
    print("System (Reflected):", reflected_output)
    print("→ Reflection Scores:", scores)


if __name__ == "__main__":
    main()
