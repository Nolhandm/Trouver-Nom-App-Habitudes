from sqlmodel import SQLModel,Field
from typing import Optional

# Table des Habitudes
class Habitudes(SQLModel, table=True):

    # Id autogénéré
    habitude_id: Optional[int] = Field(default=None, primary_key=True)

    nom: str = Field(nullable=False, min_length=2, max_length=100)
    coeff_temps: int = Field(nullable=False, ge=1, le=10)
    coeff_difficulte: int = Field(nullable=False, ge=1, le=10)
    coeff_importance: int = Field(nullable=False, ge=1, le=10)