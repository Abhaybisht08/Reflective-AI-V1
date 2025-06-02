# 📂 Code Folder – Module Map for Reflective AI V1

This folder contains the core and supporting modules for the Reflective AI framework.
Each file serves a specific role in realizing emotionally-aware, ethically-aligned AI systems.

---

## 🧭 Project Map (Mirror-First Overview)

| File                        | Role                                               | Status              |
|----------------------------|----------------------------------------------------|---------------------|
| `reflection_layer.py`      | Core logic of mirror architecture                  | ✅ Anchor            |
| `emotion_buffer.py`        | EBR grounding before reply                         | ✅ Trust             |
| `temporal_profile.py`      | Behavioral rhythm + timing analysis                | ✅ Behavioral Insight|
| `load_model_and_reflect.py`| Inject model + reflection path                     | ✅ LLM Integration   |
| `prepare_finetune_data.py` | Dataset → Fine-tuning ready format                 | ✅ Training Bridge   |
| `test_scenarios.py`        | Behavioral test cases and response mirror testing  | ✅ Eval Layer        |
| `reflective_demo_pipeline.py` | Public-facing demo pipeline                    | ✅ Showcase Core     |
| `lora_finetune_reflective.py` | LoRA-based tuning to inject reflective behavior | ✅ Reflective Training|

🪞 This structure reflects the alignment between emotion, attention, silence, and trust.

— Maintained with intent by  
Reflective-AI-V1 • Mirror First, Model Next

---

## 🔧 Developer Guide (Hands-On)

### ▶️ How to Run the Demo

```bash
python load_model_and_reflect.py
```

The script will:
1. Check emotional triggers (EBR)
2. Query LLM (GPT-4 by default)
3. Reflect the output using mirror layer
4. Print raw + reflected response and alignment scores

---

### 📊 Running Tests

```bash
python test_scenarios.py
```

This will simulate scenarios to test:
- Trigger detection
- EBR fallback
- Reflection accuracy

---

### 🛠 Future Additions

These are in planning or development:
- LoRA fine-tuning for OSS models
- Dataset prep automation from logs
- API wrapper for online use

---

### 🧠 Tech Requirements

- Python ≥ 3.10
- OpenAI API key for GPT-4
- HuggingFace + LoRA for OSS-based models

---

This `code/` folder is the functional layer of our mirror.  
It converts human hesitation, silence, and emotion into actionable reflection.
