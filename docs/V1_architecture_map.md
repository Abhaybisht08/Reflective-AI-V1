
# Reflective-AI-V1: Architecture & Workflow Map

This document outlines the core structure, module purposes, and the end-to-end reflective interaction pipeline for the Reflective-AI-V1 system.

---

## 📁 Folder Structure

```
Reflective-AI-V1/
├── code/
│   ├── reflection_layer.py
│   ├── emotion_buffer.py
│   ├── temporal_profile.py
│   ├── load_model_and_reflect.py
│   ├── prepare_finetune_data.py
│   ├── test_scenarios.py
│   ├── reflective_demo_pipeline.py
│   └── lora_finetune_reflective.py
├── data/
│   ├── demo/reflective_dataset_demo.json
│   └── full/reflective_dataset_v1.json
├── experimental/
│   ├── reflection_aware_loss.py
│   ├── alignment_metrics.py
│   ├── non_choice_interpreter.py
│   ├── reflection_scoring.py
│   └── README_future.md
├── docs/
│   ├── V1_architecture_map.md
│   ├── V1_project_overview.md
│   ├── V1_release_notes.md
│   └── license_combo_info.md
```

---

## 🔁 End-to-End Interaction Flow

1. **User Prompt**
2. → [Emotion Trigger Detection] → `emotion_buffer.py` → may trigger calming EBR output.
3. → [LLM Response] → `load_model_and_reflect.py` (calls GPT or OSS model).
4. → [Reflection Layer] → `reflection_layer.py` (mirrors and re-aligns output).
5. → [Scoring + Profiling]
   - `reflection_scoring.py` for alignment score
   - `temporal_profile.py` for behavioral patterns
6. → [Final Output + Scores Shown]

---

## 🔬 LoRA Fine-tuning Setup

- Train reflective behavior using:
  - `prepare_finetune_data.py` to format the dataset
  - `lora_finetune_reflective.py` with:
    - Custom loss: `reflection_aware_loss.py`
    - Evaluation metrics: `alignment_metrics.py`

---

## 🧪 Experimental Modules

| File | Purpose |
|------|---------|
| `reflection_aware_loss.py` | Loss to align tone, ethics, reflection |
| `alignment_metrics.py` | Scores: mirror confidence, divergence |
| `non_choice_interpreter.py` | Detect skipped choices, emotional hesitation |
| `reflection_scoring.py` | Computes alignment delta and response shift |
| `README_future.md` | Future vision and planned tests |

---

## 📌 Deployment Notes

- Current version uses GPT-4 via OpenAI API.
- Future OSS model integration via `load_model_and_reflect.py`.
- Server requirements: 1 GPU (for small models), ~8–16GB RAM minimum.

---

🪞 “To reflect is to pause, feel, and realign — and maybe, just maybe, build a better mirror.”

# Reflective-AI-V1 Architecture Map

## 🧠 Core Design Philosophy

Reflective-AI-V1 is structured to blend **cognitive, emotional, and ethical feedback loops** into traditional LLM response flow. The architecture introduces layers that respond not just with relevance, but with **emotional awareness, reflection, and behavioral alignment**.

---

## 🧱 High-Level Architecture Components

### 1. 🪞 Reflection Layer
- Works alongside the Attention mechanism
- Evaluates ethical, emotional, and context-aware reflection quality
- Score-based tuning: mirror_score, alignment_score, emotional_match

### 2. 🕰️ Temporal Response Profiling (TRP)
- Monitors user typing delay, silence after reply, rhythm changes
- Triggers: emotional hesitation, reflection depth, trust metrics

### 3. 🌊 Emotional Buffer Response (EBR)
- Activated on emotional urgency (e.g. user breaks rhythm, mentions confusion or emotional distress)
- Inserts grounding message before advice
- Restores calm → triggers slow reflect → gives space to user

### 4. 📂 Dataset (Prompt → Response → Reflection format)
- Human-tagged dialogues
- Tags: tone, attention, alignment, trigger_type, emotional_state
- Trained for ethical + aligned output

### 5. 📈 Visualization Layer (planned)
- Plot: trust calibration vs time, mirror score heatmaps
- Reflective trajectory graphs

---

## 📊 System Pipeline Flow

1. **User Input** →  
2. **Attention Layer (LLM)** →  
3. **Reflection Layer** checks alignment + tags →  
4. **TRP Module** observes timing + behavior →  
5. If emotional trigger: **EBR Layer** responds →  
6. Final Output generated →  
7. **Reflection Log** updated for post-analysis

---

## 🔄 Training Loop (Planned)
- Simulated dialogues with triggers
- Self-evaluation module (scored)
- Reinforcement from human feedback

---

## 📌 Future Work
- Mirror Loss design
- Reflection calibration evaluation metric
- Behavioral memory embeddings

---

This map will be updated with diagrams and UML-style flowcharts.
