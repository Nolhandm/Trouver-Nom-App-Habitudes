from sqlalchemy import func
from sqlmodel import Session, select
from db.init_db import get_engine
from db.models import *
from math import sqrt, pow

base_xp = 10
base_level = 1000
increase_level = 100

def get_total_xp():
    with Session(get_engine()) as session:

        # Get number of checks for each habit
        statement = (select(Habit, func.count().label('total'))
                     .join(Validation_habits, Validation_habits.habit_id == Habit.habit_id)
                     .group_by(Habit.habit_id))
        result = session.exec(statement).all()

        final_xp = 0
        for hab in result:
            final_xp += base_xp*hab[1]*(hab[0].time_coeff+hab[0].difficulty_coeff+hab[0].importance_coeff)
        return final_xp

def compute_level():

    cumul = get_total_xp()
    level = (increase_level/2 - base_level + sqrt(pow(base_level-increase_level/2,2)+2*increase_level*cumul))/increase_level+1

    return int(level)

def compute_cumul_xp_for_level(level):
    if level <= 0:
        return 0
    return int(increase_level/2*pow(level,2) + (base_level-increase_level/2)*level)

def compute_xp_for_level(level):
    if level <= 0:
        return 0
    return int(base_level + (level-1)*increase_level)

def compute_rank():
    return 4