from sqlmodel import SQLModel, create_engine, Session
import streamlit as st
from db.models import Habitudes

# Emplacement Database
DATABASE_URL = "sqlite:///./db/database.db"

# Obtenir un engine pour accéder à la db
@st.cache_resource
def get_engine():
    return create_engine(DATABASE_URL, echo=True)

# Initialisation de la base de données
@st.cache_resource
def init_db():
    print("Initialisation de la base de données.")
    SQLModel.metadata.create_all(get_engine())
    print("Base de données prête.")
