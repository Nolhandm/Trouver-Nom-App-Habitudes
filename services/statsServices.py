from sqlalchemy import func
from sqlmodel import Session, select
from db.init_db import get_engine
from db.models import *

base_xp = 10

def get_actual_xp():
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

