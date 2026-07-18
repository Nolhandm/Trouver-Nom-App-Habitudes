from sqlmodel import SQLModel, create_engine, Session
from db.init_db import get_engine
from db.models import *
import pandas as pd

# Ajouter une habitude
def add_new_habit(name, time_coeff, difficulty_coeff, importance_coeff):
    if name.strip() == '':
        return

    with Session(get_engine()) as session:
        session.add(Habit(name = name,time_coeff=time_coeff,difficulty_coeff=difficulty_coeff,importance_coeff=importance_coeff))
        session.commit()

def get_all_habits():
    with Session(get_engine()) as session:
        return pd.read_sql("SELECT * FROM Habits", session.bind)

def get_habit_by_name(name):
    with Session(get_engine()) as session:
        df = pd.read_sql(f"SELECT * FROM Habits WHERE nom={name}", session.bind)
        return df



