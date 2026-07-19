import streamlit as st
from services.statsServices import get_total_xp, compute_level, compute_cumul_xp_for_level, compute_xp_for_level

class CharacterComponent:

    def __init__(self):
        self.total_xp = get_total_xp()
        self.level = compute_level()
        self.xp_above_level = compute_cumul_xp_for_level(self.level) - self.total_xp

        st.title("This is the character Class")
        st.write(f"XP total actuel : {self.total_xp}")
        st.write(f"XP above : {compute_cumul_xp_for_level(self.level + 1)}")
        st.write(f"XP Total nécéssaire : {compute_cumul_xp_for_level(self.level + 1)}")
        st.write(f"XP Nécéssaire : {compute_xp_for_level(self.level + 1)}")
        st.write(f"Niveau actuel : {self.level}")
        st.progress(value=self.xp_above_level/compute_xp_for_level(self.level))
