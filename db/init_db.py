from sqlmodel import SQLModel, create_engine, Session
import streamlit as st
from db.models import Habit

# Database URL
DATABASE_URL = "sqlite:///./db/database.db"

# Get an engine to access db
@st.cache_resource
def get_engine():
    return create_engine(DATABASE_URL, echo=False)

# Init database
@st.cache_resource
def init_db():
    print("Initialisation de la base de données.")
    SQLModel.metadata.create_all(get_engine())
    print("Base de données prête.")
