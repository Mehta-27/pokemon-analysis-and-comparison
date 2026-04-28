<div align="center">

# 🔥 Pokémon Analytics — EDA & Comparison Tool

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mehta-27-pokemon-analysis-and-comparison.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.3-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-6.7-3F4F75?logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A comprehensive Pokémon data science project featuring deep exploratory data analysis and an interactive Streamlit web app for head‑to‑head Pokémon comparison.**

[Live Demo](https://mehta-27-pokemon-analysis-and-comparison.streamlit.app) · [Notebook](main.ipynb) · [Report Bug](https://github.com/Mehta-27/pokemon-analysis-and-comparison/issues)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Live Demo](#-live-demo)
- [Dataset](#-dataset)
- [Key Insights from EDA](#-key-insights-from-eda)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Streamlit App Usage](#-streamlit-app-usage)
- [Screenshots](#-screenshots)
- [Author](#-author)
- [License](#-license)

---

## 🎯 About the Project

This project performs an end‑to‑end **Exploratory Data Analysis (EDA)** on a comprehensive Pokémon dataset covering all generations up to 2025. The analysis uncovers patterns in base stats, type distributions, legendary vs. regular Pokémon performance, and strategic playstyle classifications.

A **Streamlit web application** is also included, allowing users to interactively compare any two Pokémon side‑by‑side using radar charts, stat breakdowns, winner‑per‑stat logic, and offensive/defensive playstyle analysis.

---

## ✨ Key Features

### 📓 Jupyter Notebook (`main.ipynb`)
- **Dataset Overview** — Shape, dtypes, missing values, and descriptive statistics
- **Type Distribution Analysis** — Frequency and combination analysis of Pokémon types
- **Base Stat Exploration** — Distributions, correlations, and tier-based analysis
- **Legendary vs. Regular** — Statistical comparison and performance benchmarks
- **Playstyle Classification** — Offensive/Defensive ratio analysis using Attack+SpAtk vs Defense+SpDef+HP
- **Speed Tier Analysis** — Categorization of Pokémon into speed brackets
- **Visualizations** — Publication-quality charts with Matplotlib, Seaborn, and Plotly

### 🌐 Streamlit App (`app.py`)
- **Pokémon Selector** — Search and select any two Pokémon from the full dataset
- **Artwork Display** — Renders official Pokémon artwork from PokémonDB
- **Radar Chart** — Interactive Plotly polar chart comparing all 6 base stats
- **Stat-by-Stat Winner** — Highlights which Pokémon wins each stat category
- **Playstyle Verdict** — Classifies each Pokémon as Offensive 🔥 or Defensive 🛡️

---

## 🚀 Live Demo

👉 **[Launch the App on Streamlit Cloud](https://mehta-27-pokemon-analysis-and-comparison.streamlit.app)**

---

## 📊 Dataset

| Property | Detail |
|----------|--------|
| **File** | `pokemon_complete_2025.csv` |
| **Records** | 1,000+ Pokémon (all generations through 2025) |
| **Features** | 40+ columns |
| **Source** | PokéAPI aggregated dataset |

### Key Columns

| Column | Description |
|--------|-------------|
| `name` | Pokémon name |
| `type_1`, `type_2` | Primary and secondary types |
| `hp`, `attack`, `defense` | Physical base stats |
| `sp_attack`, `sp_defense`, `speed` | Special stats and speed |
| `base_stat_total` | Sum of all 6 base stats |
| `is_legendary`, `is_mythical` | Legendary/Mythical flags |
| `generation` | Game generation (I–IX) |
| `stat_tier` | Performance tier classification |
| `attack_defense_ratio` | Offensive vs. defensive balance |

---

## 💡 Key Insights from EDA

1. **Water** is the most common primary type, while **Flying** dominates as a secondary type
2. **Legendary Pokémon** have a median BST ~100 points higher than regular Pokémon
3. The **playstyle ratio** (Offensive Total / Defensive Total) effectively separates sweepers from walls — a ratio > 1 indicates an offensive build
4. **Speed** follows a right-skewed distribution — most Pokémon are slow, but a few speedsters dominate
5. **Dragon** and **Steel** types consistently rank among the highest average BST across generations
6. **Generation V** introduced the most new Pokémon, while later generations focused on quality over quantity

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.11** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **Matplotlib & Seaborn** | Static visualizations |
| **Plotly** | Interactive charts (radar plots) |
| **Streamlit** | Web application framework |
| **Jupyter Notebook** | EDA environment |

---

## 📁 Project Structure

```
pokemon-analysis-and-comparison/
├── app.py                        # Streamlit comparison app
├── main.ipynb                    # Full EDA notebook
├── pokemon_complete_2025.csv     # Dataset
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── LICENSE                       # MIT License
└── .streamlit/
    └── config.toml               # Streamlit theme configuration
```

---

## 🏁 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Mehta-27/pokemon-analysis-and-comparison.git
cd pokemon-analysis-and-comparison

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### Running the Notebook

```bash
jupyter notebook main.ipynb
```

---

## 🎮 Streamlit App Usage

1. **Select Pokémon** — Use the two dropdown menus to pick any Pokémon
2. **View Artwork** — Official artwork is displayed side by side
3. **Analyze Radar Chart** — Hover over the interactive polar chart to compare stats
4. **Check Winners** — See which Pokémon wins each stat category
5. **Read Playstyle** — The app classifies each as Offensive 🔥 or Defensive 🛡️

---

## 📸 Screenshots

| Comparison View | Radar Chart |
|:---:|:---:|
| *Select any two Pokémon for head-to-head comparison* | *Interactive radar chart powered by Plotly* |

---

## 👤 Author

**Mehta Rishit**

- GitHub: [@Mehta-27](https://github.com/Mehta-27)
- Instagram: [@mehtarizzhit_27](https://www.instagram.com/mehtarizzhit_27)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If you found this project useful, give it a star on GitHub! ⭐**

</div>
