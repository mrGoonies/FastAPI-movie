from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

current_day = date.today()


class Movie(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    year: int = Field(le=int(current_day.strftime("%Y")))
    genre: str = Field(min_length=5, max_length=20)
    director: str = Field(min_length=4, max_length=25)
    rating: Optional[float] = Field(ge=1.0, le=10.0)

    # Valores por defecto
    class Config:
        json_schema_extra = {
            "example": {
                "id": 000,
                "title": "Movie Name",
                "year": 0000,
                "genre": "Genre Name",
                "director": "Director Name",
                "rating": None,
            }
        }
