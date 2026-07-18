import streamlit as st
from db.init_db import init_db

init_db()

st.set_page_config(page_title="Application Habitudes", page_icon="⚔️")

st.title("⚔️ Tableau de Bord des Habitudes")
st.write("Bienvenue, Héros ! Coche tes quêtes pour gagner de l'XP.")

# Vos logique de jeu ici
if st.button("Valider la quête du jour"):
    st.success("Quête validée ! +50 XP")
    # Ici vous appelleriez votre fonction pour mettre à jour la DB

st.info("Utilise le menu à gauche pour naviguer vers la Boutique ou ton Profil.")