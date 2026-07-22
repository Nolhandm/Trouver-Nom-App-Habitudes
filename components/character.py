import streamlit as st
import config
from services.statsServices import get_total_xp, compute_level, compute_cumul_xp_for_level, compute_xp_for_level, compute_rank

class CharacterComponent:

    def __init__(self):
        self.total_xp = get_total_xp()
        self.level = compute_level()

        st.title("This is the character Class")
        st.image(config.DICT_PATH_VAGABOND_IMG[compute_rank()], width=200)
        st.write(f"Niveau actuel : {self.level}")

        text = f"{self.total_xp-compute_cumul_xp_for_level(self.level-1)} / {compute_xp_for_level(self.level)} XP"
        st.progress(value=(self.total_xp-compute_cumul_xp_for_level(self.level-1))/compute_xp_for_level(self.level), text=text)

        st.write(f"XP total cummulé : {self.total_xp}")