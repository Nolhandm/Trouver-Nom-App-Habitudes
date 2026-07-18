from sqlmodel import Session, select
from db.init_db import get_engine
from datetime import date
from db.models import *
import pandas as pd

# ---------- Gestion habitudes --------------------
def add_new_habit(name, time_coeff, difficulty_coeff, importance_coeff):
    if name.strip() == '':
        return

    with Session(get_engine()) as session:
        session.add(Habit(name = name,time_coeff=time_coeff,difficulty_coeff=difficulty_coeff,importance_coeff=importance_coeff))
        session.commit()

def get_all_habits():
    with Session(get_engine()) as session:
        statement = select(Habit)
        return session.exec(statement).all()

# ----------- Validation ------------------

def get_all_checked_habit_ids(validation_date : date):
    with Session(get_engine()) as session:
        statement = select(Validation_habits.habit_id).where(Validation_habits.validation_date == validation_date)
        return session.exec(statement).all()


def check_habit(habit_id, validation_date):
    with Session(get_engine()) as session:
        session.add(Validation_habits(habit_id=habit_id, validation_date=validation_date))
        session.commit()

def uncheck_habit(habit_id, validation_date):
    with Session(get_engine()) as session:

        statement = (select(Validation_habits)
                     .where(Validation_habits.habit_id==habit_id)
                     .where(Validation_habits.validation_date==validation_date))

        val_habit = session.exec(statement).first()

        session.delete(val_habit)
        session.commit()