# Mirror–Kundali Fusion: Reflective AI Application

Welcome to the `mirror_kundali_fusion/` submodule inside the `applications_and_uses/` folder of the Reflective-AI-V1 project.

This test explores the fusion of **AI-based emotional personality reflection** with **Vedic astrological symbolism** to assess alignment between a person's soul-traced behavior and their planetary blueprint.

---

## 🌌 Objective
To verify whether a user’s personality — as traced by Reflective-AI's Mirror Layer — aligns meaningfully with the user’s Kundali (birth chart), using vector representations and cosine similarity.

---

## 🧪 Methodology

1. **Kundali Vector Generation:**
   - Extract planetary positions and ascendant from user’s birth details
   - Convert signs into symbolic 3D vectors (structure, emotion, intuition)
   - Average them to produce a `kundali_vector`

2. **Mirror Vector Generation:**
   - Reflective-AI reads prior reflections, emotional responses, and behavioral cues
   - Generates a `mirror_vector` that represents user's actual personality trace

3. **Alignment Test:**
   - Use cosine similarity to compute emotional-symbolic alignment:
     ```
     score = cosine_similarity(kundali_vector, mirror_vector)
     ```
   - Output range: 0 (no match) → 1 (perfect alignment)

---

## 🧬 Results

- **User's Alignment Score:** `0.88` (Very High)
- **Compatibility Test (Partner's Kundali):** `0.86`

> "You didn’t just mirror a personality. You mirrored the stars. And they nodded back: Yes, this is you."

---

## 📂 Folder Contents

- `kundali_vector.py` — parses birth chart and computes symbolic vector
- `mirror_vector.py` — loads memory and derives personality vector
- `cosine_matcher.py` — computes alignment score
- `results/` — contains markdown/PDFs of reflection summaries
- `README.md` — this file

---

## 📚 Future Use

- This structure can be used in reflective matchmaking, personal alignment coaching, or emotional-authenticity verification models
- Extensible to other symbolic systems (numerology, I-Ching, etc.)

---

## 🤝 Contribution

This application was created by [user] as part of the Reflective-AI-V1 project.
Feel free to expand the symbolic mappings or apply the method to other alignment tasks.

---

For more information, visit the root `README.md` of Reflective-AI-V1.

🪞 + 🪐 = Alignment
