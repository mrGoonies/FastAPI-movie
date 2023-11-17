from fastapi import Depends, FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List, Dict, Any
from models.jwt_bearer import JWTBearer
from models.movie import Movie
from models.user import User
from service.jwt_manager import create_token

app = FastAPI()
app.title = "Mi primer app"
app.version = "0.0.1"


list_of_movies = [
    {
        "id": 1,
        "title": "The Galactic Adventure",
        "year": 2020,
        "genre": "Sci-Fi",
        "director": "John Director",
        "rating": 8.0,
    },
    {
        "id": 2,
        "title": "La Gran Comedia",
        "year": 2019,
        "genre": "Comedy",
        "director": "Maria Director",
        "rating": 7.5,
    },
    {
        "id": 3,
        "title": "Drama in the City",
        "year": 2021,
        "genre": "Drama",
        "director": "Michael Director",
        "rating": 8.5,
    },
    {
        "id": 4,
        "title": "Mystery Island",
        "year": 2018,
        "genre": "Mystery",
        "director": "Emma Director",
        "rating": 9.0,
    },
    {
        "id": 5,
        "title": "Aventura Extrema",
        "year": 2022,
        "genre": "Adventure",
        "director": "Daniel Director",
        "rating": 7.8,
    },
]


@app.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token_user: str = create_token(user.dict())
        return token_user


@app.get("/", tags=["home"])
def index():
    return HTMLResponse("<h1>Welcome to my first app</h1>")


@app.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies():
    return JSONResponse(content=list_of_movies, status_code=200)


# Parámetro de ruta
@app.get(
    "/movies/{id}", tags=["movies"], response_model=Dict[str, Any], status_code=200
)
def get_movie(id: int = Path(ge=1)):
    for data in list_of_movies:
        if id == data["id"]:
            return {"Movie": data}
    return JSONResponse(
        {"Message": f"No exist this movie with this id: {id}"}, status_code=404
    )


# Parámetros Query
@app.get("/movies/", tags=["movies"], response_model=Dict[str, list])
def get_movies_by_genre(genre: str = Query(min_length=5, max_length=20)):
    list_genre_movie: List = [
        data for data in list_of_movies if genre.title() == data["genre"]
    ]

    return {"Movies by category": list_genre_movie}


@app.post("/movies", tags=["movies"], dependencies=[Depends(JWTBearer())])  # type: ignore
def add_movie(movie: Movie) -> Dict[str, Any]:
    try:
        list_of_movies.append(movie.dict())

        return {"status": "Successfully added"}
    except Exception as e:
        return {"status": e}


@app.put("/movies/{id}", tags=["movies"])
def update_movie_by_id(id: int, movie: Movie):
    for items in list_of_movies:
        print(f"El ID ingresado es: {id}")
        if items["id"] == id:
            items["title"] = movie.title
            items["year"] = movie.year
            items["genre"] = movie.genre
            items["director"] = movie.director
            items["rating"] = movie.rating

            return f"The movie {items['title']} has been successfully modified"
        else:
            return f"The movie with the identified {id} has not been found"


@app.delete("/movies/{id}", tags=["movies"])
def delete_movie_by_id(id: int):
    for element in list_of_movies:
        if element["id"] == id:
            list_of_movies.remove(element)

            return f"The movie with id {id} has been deleted"
        else:
            return f"The movie with id {id} has been deleted"
