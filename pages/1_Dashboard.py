import streamlit as st
from utils.Date import Date
from datetime import date, timedelta
from services.habitudesService import get_all_habits

# ---------------------------------------------
# ---------------- Fonctions ------------------
# ---------------------------------------------

def previous_date():
    st.session_state.ACTUAL_DATE = st.session_state.ACTUAL_DATE - timedelta(days=1)
    sync_calendar()

def next_date():
    st.session_state.ACTUAL_DATE = st.session_state.ACTUAL_DATE + timedelta(days=1)
    sync_calendar()

# Forcer le calendrier à se synchroniser avec ACTUAL_DATE
def sync_calendar():
    st.session_state.calendar_picker = st.session_state.ACTUAL_DATE

def update_date():
    st.session_state.ACTUAL_DATE = st.session_state.calendar_picker

# -------------------------------------------------------------
# ---------------- Début de l'interface -----------------------
# -------------------------------------------------------------

st.title("📅 Suivi des Quêtes")

# ---------------- Système de date -----------------------

# Classe personnalisé pour la gestion de date
if 'ACTUAL_DATE' not in st.session_state:
    st.session_state.ACTUAL_DATE = date.today()

# Initialiser la clé du calendrier
if 'calendar_picker' not in st.session_state:
    st.session_state.calendar_picker = st.session_state.ACTUAL_DATE

# Affichage des boutons de navigation et de la date centrale
col_prev, col_date, col_next = st.columns([0.5, 1, 0.5])

with col_prev:
    st.button("◀", use_container_width=True, on_click=previous_date)

with col_date:
    #st.markdown(f"<div style='text-align: center; font-size: 1.2em; font-weight: bold; padding-top: 10px;'>{st.session_state.selected_date.strftime('%d/%m/%Y')}</div>", unsafe_allow_html=True)
    st.date_input("Aller à...", label_visibility="collapsed", key="calendar_picker", on_change=update_date, format="DD/MM/YYYY")

with col_next:
    st.button("▶", use_container_width=True, on_click=next_date)

st.divider()

# ----------- Liste des habitudes -----------------

list_habits = get_all_habits()

st.subheader("✅ Liste des quêtes")

# Si trop lent passer à itertuples
for habit in list_habits.itertuples():

    # Colonnes pour habitudes et case à cocher
    col_name, col_info, col_check = st.columns([0.7, 0.2, 0.1])

    with col_name:
        st.write(habit.name)

    with col_info:
        pass
        #st.caption(f"⏱️ {habit.coeff_temps}min | ⚡ {habit.coeff_difficulte}/10")

    with col_check:
        st.checkbox('Valider',label_visibility='hidden', value=False, key=f"habit_check_{habit.habit_id}")



