import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Pokémon Analyzer", layout="wide")

# -------------------- STYLE --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1 {
    text-align: center;
    font-size: 42px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD DATA --------------------
df = pd.read_csv("pokemon_complete_2025.csv")

# -------------------- TITLE --------------------
st.title("🔥 Pokémon Comparison Tool")

# -------------------- IMAGE FUNCTION --------------------
def get_image(name):
    name = name.lower()
    return f"https://img.pokemondb.net/artwork/{name}.jpg"

# -------------------- SELECT --------------------
pokemon_list = df["name"].unique()

col1, col2 = st.columns(2)

with col1:
    poke1 = st.selectbox("Select Pokémon 1", pokemon_list)

with col2:
    poke2 = st.selectbox("Select Pokémon 2", pokemon_list)

# -------------------- DATA --------------------
p1 = df[df["name"] == poke1].iloc[0]
p2 = df[df["name"] == poke2].iloc[0]

stats = ["hp","attack","defense","sp_attack","sp_defense","speed"]

p1_stats = p1[stats].values
p2_stats = p2[stats].values

# -------------------- IMAGES --------------------
col1, col2 = st.columns(2)

with col1:
    st.image(get_image(poke1), caption=poke1, use_container_width=True)

with col2:
    st.image(get_image(poke2), caption=poke2, use_container_width=True)

# -------------------- RADAR CHART --------------------
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=p1_stats,
    theta=stats,
    fill='toself',
    name=poke1
))

fig.add_trace(go.Scatterpolar(
    r=p2_stats,
    theta=stats,
    fill='toself',
    name=poke2
))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 150])),
    showlegend=True,
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- STAT TABLE --------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(poke1)
    st.write(p1[stats])

with col2:
    st.subheader(poke2)
    st.write(p2[stats])

# -------------------- WINNER LOGIC --------------------
winner = []

for stat in stats:
    if p1[stat] > p2[stat]:
        winner.append(poke1)
    elif p2[stat] > p1[stat]:
        winner.append(poke2)
    else:
        winner.append("Tie")

st.subheader("🏆 Stat Winners")
st.write(dict(zip(stats, winner)))

# -------------------- PLAYSTYLE --------------------
p1_ratio = (p1["attack"] + p1["sp_attack"]) / (p1["defense"] + p1["sp_defense"] + p1["hp"])
p2_ratio = (p2["attack"] + p2["sp_attack"]) / (p2["defense"] + p2["sp_defense"] + p2["hp"])

st.subheader("⚔️ Playstyle Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write(f"{poke1}: {'Offensive 🔥' if p1_ratio > 1 else 'Defensive 🛡️'}")

with col2:
    st.write(f"{poke2}: {'Offensive 🔥' if p2_ratio > 1 else 'Defensive 🛡️'}")