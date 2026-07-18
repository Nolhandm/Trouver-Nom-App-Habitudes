import streamlit as st
from db.init_db import init_db
from services.statsServices import get_actual_xp

init_db()

st.set_page_config(page_title="Application Habitudes", page_icon="⚔️")

st.title("⚔️ Tableau de Bord des Habitudes")
st.write("Bienvenue, Héros ! Coche tes quêtes pour gagner de l'XP.")

st.write(f"XP actuel : {get_actual_xp()}")