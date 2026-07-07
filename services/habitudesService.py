from sqlmodel import SQLModel, create_engine, Session
from db.initialisation_db import get_engine
from db.models import *
import pandas as pd

# Ajouter une habitude
def add_habitude(nom, temps, difficulte, importance):
    with Session(get_engine()) as session:
        newHab = Habitudes(nom=nom,coeff_temps=temps,coeff_difficulte=difficulte,coeff_importance=importance)
        session.add(newHab)
        session.commit()

def get_habitudes():
    with Session(get_engine()) as session:
        df = pd.read_sql("SELECT * FROM habitudes", session.bind)
        return df