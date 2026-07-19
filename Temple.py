import streamlit as st
from db.init_db import init_db
from services.statsServices import get_total_xp, compute_level
from components.character import CharacterComponent

init_db()

st.set_page_config(page_title="Application Habitudes", page_icon="⚔️")

st.title("⚔️ Tableau de Bord des Habitudes")
st.write("Bienvenue, Héros ! Coche tes quêtes pour gagner de l'XP.")

chara = CharacterComponent()