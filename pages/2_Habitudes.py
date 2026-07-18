import streamlit as st
from services.habitudesService import add_new_habit, get_all_habits
import pandas as pd

options = [1,2,3,4,5,6,7,8,9,10]

with st.expander("➕ Ajouter une nouvelle habitude", expanded=False) as expander:
    with st.form("Ajouter une habitude :"):

        nom = st.text_input("Nom de l'habitude")

        temps = st.selectbox('Temps', options)
        difficulte = st.selectbox('Difficulté', options)
        importance = st.selectbox('Importance', options)

        submitted = st.form_submit_button("Ajouter")

        if submitted:
            if not nom or nom.strip() == "":
                st.error("Le nom n'est pas valide")
            else :
                add_new_habit(nom, temps, difficulte, importance)
                st.success("Habitude ajoutée !")
                expander.expanded = False
                st.rerun()

habitudes = get_all_habits()
st.table(habitudes)