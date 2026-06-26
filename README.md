# 🔥 Pokémon Analysis & Comparison — EDA + Interactive Tool

**1,025 Pokémon. Deep EDA. Interactive radar chart comparisons. Who's the stronger 'mon?**

[![Streamlit App](https://img.shields.io/badge/Live_Demo-Pokémon_Comparison-FF6B6B?style=for-the-badge&logo=streamlit&logoColor=white)](https://mehta-27-pokemon-analysis-and-comparison.streamlit.app)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-0E1117?style=for-the-badge&logo=python&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-0E1117?style=for-the-badge)](LICENSE)
[![Dataset](https://img.shields.io/badge/Dataset-1,025_Pokémon_2025-3B82F6?style=for-the-badge)](pokemon_complete_2025.csv)

---

## 🎯 What's Inside

| Deliverable | What It Does |
|-------------|-------------|
| **📓 `main.ipynb`** — Deep EDA | Type distributions · stat analysis · legendary vs regular · playstyle classification · speed tiers · 46 derived features |
| **🌐 `app.py`** — Streamlit App | Select any 2 Pokémon → artwork · radar chart · stat‑by‑stat winner · offensive vs defensive playstyle verdict |

---

## 🔥 Streamlit App

**[→ Launch the App](https://mehta-27-pokemon-analysis-and-comparison.streamlit.app)**

Pick any two Pokémon and instantly see:

```
┌──────────────────────────────────────────────┐
│              POKÉMON COMPARISON               │
├──────────────────────────────────────────────┤
│                                              │
│  Charizard  🖼       Blastoise  🖼            │
│       └──────────┬──────────┘                │
│                  ▼                            │
│       ⬡ RADAR CHART (HP/ATK/DEF/             │
│         SPATK/SPDEF/SPEED)                    │
│                                              │
│   🏆 Winners: HP→Char · ATK→Char · ...       │
│   ⚔️ Charizard: Offensive 🔥                  │
│   ⚔️ Blastoise: Defensive 🛡️                  │
└──────────────────────────────────────────────┘
```

### Features
- **Pokémon artwork** — fetched live from PokémonDB
- **Radar chart** — Plotly dark‑mode polar chart, 6 base stats
- **Stat‑by‑stat winner** — who wins HP, Attack, Defense, etc.
- **Playstyle analysis** — `(ATK + SPATK) / (DEF + SPDEF + HP)` > 1 = Offensive

---

## 📓 EDA Notebook (`main.ipynb`)

A thorough **46‑column, 1,025‑row** exploratory analysis:

### Type Distribution
- **Water** is the most common primary type
- **Flying** dominates as secondary type
- Dual‑type Pokémon outnumber single‑type

### Base Stats
| Stat | Mean | Median | Range |
|------|:----:|:------:|:-----:|
| BST | 427.7 | 450 | 175–720 |
| Attack | 77.5 | — | — |
| Speed | 67.2 | — | — |

### Legendary vs Regular
- Legendaries have **~100 higher median BST**
- Clear threshold around 580 BST

### Playstyle Classification
- Mean attack/defense ratio: **1.15**
- ~35% of Pokémon are balanced
- **Dragon** and **Steel** have highest average BST

---

## 📊 Dataset

**[`pokemon_complete_2025.csv`](pokemon_complete_2025.csv)** — 1,025 Pokémon × 43 columns

| Category | Columns |
|----------|---------|
| **Identifiers** | `name`, `pokedex_number`, `japanese_name` |
| **Types** | `type_1`, `type_2` |
| **Base Stats** | `hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed` |
| **Physical** | `height_m`, `weight_kg`, `abilities`, `ability_1`, `ability_2` |
| **Classification** | `against_*` (18 resistances), `is_legendary`, `is_mythical`, `generation` |
| **Derived** | `base_stat_total`, `stat_tier`, `attack_defense_ratio` |

---

## 🚀 Quick Start

```bash
git clone https://github.com/Mehta-27/pokemon-analysis-and-comparison.git
cd pokemon-analysis-and-comparison
pip install -r requirements.txt
streamlit run app.py    # Launch the web app
jupyter notebook main.ipynb  # Explore the EDA
```

---

## 📁 Structure

```
pokemon-analysis-and-comparison/
├── app.py                        # Streamlit comparison tool
├── main.ipynb                    # Full EDA notebook
├── pokemon_complete_2025.csv     # 1,025 × 43 dataset
├── requirements.txt              # streamlit, pandas, plotly
├── LICENSE                       # MIT
└── .streamlit/
    └── config.toml               # Dark theme config
```

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **EDA** | pandas, matplotlib, seaborn, numpy |
| **Web App** | Streamlit |
| **Charts** | Plotly (polar radar) |
| **Images** | PokémonDB API |
| **Deployment** | Streamlit Community Cloud |

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/Mehta-27">Rishit Mehta</a><br>
  <sub>Data sourced from PokeAPI · Pokémon is © Nintendo/The Pokémon Company</sub>
</p>
