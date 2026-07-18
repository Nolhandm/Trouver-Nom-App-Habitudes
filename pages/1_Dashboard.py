import streamlit as st
from datetime import date, timedelta
from services.habitudesService import get_all_habits, get_all_checked_habit_ids, check_habit, uncheck_habit

# ---------------------------------------------
# ----------- Variables globales --------------
# ---------------------------------------------

# Classe personnalisé pour la gestion de date
if 'ACTUAL_DATE' not in st.session_state:
    st.session_state.ACTUAL_DATE = date.today()

list_habits = get_all_habits()

checked_habits_id = get_all_checked_habit_ids(st.session_state.ACTUAL_DATE)

# ---------------------------------------------
# ---------------- Fonctions ------------------
# ---------------------------------------------

def previous_date():
    st.session_state.ACTUAL_DATE = st.session_state.ACTUAL_DATE - timedelta(days=1)
    sync_calendar()
    sync_checkboxes()

def next_date():
    st.session_state.ACTUAL_DATE = st.session_state.ACTUAL_DATE + timedelta(days=1)
    sync_calendar()
    sync_checkboxes()

# Forcer le calendrier à se synchroniser avec ACTUAL_DATE
def sync_calendar():
    st.session_state.calendar_picker = st.session_state.ACTUAL_DATE

def update_date():
    st.session_state.ACTUAL_DATE = st.session_state.calendar_picker
    sync_checkboxes()

def sync_checkboxes():
    global checked_habits_id
    checked_habits_id = get_all_checked_habit_ids(st.session_state.ACTUAL_DATE)
    for h in list_habits:
        st.session_state[f"habit_check_{h.habit_id}"] = h.habit_id in checked_habits_id

# -------------------------------------------------------------
# ---------------- Début de l'interface -----------------------
# -------------------------------------------------------------

st.title("📅 Suivi des Quêtes")

# ---------------- Système de date -----------------------

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

st.subheader("✅ Liste des quêtes")

for habit in list_habits:

    # Colonnes pour habitudes et case à cocher
    col_name, col_info, col_check = st.columns([0.7, 0.2, 0.1])

    with col_name:
        st.write(habit.name)

    with col_info:
        st.caption(f"⏱️ {habit.time_coeff}min | ⚡ {habit.difficulty_coeff}/10")


    with col_check:

        checkbox_key = f"habit_check_{habit.habit_id}"
        if checkbox_key not in st.session_state:
            st.session_state[checkbox_key] = habit.habit_id in checked_habits_id

        is_checked = habit.habit_id in checked_habits_id

        checked = st.checkbox('Valider', label_visibility='hidden', key=checkbox_key)
        if checked != is_checked:
            if checked:
                check_habit(habit.habit_id, st.session_state.ACTUAL_DATE)
            else:
                uncheck_habit(habit.habit_id, st.session_state.ACTUAL_DATE)

