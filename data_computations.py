"""."""
import csv


class Movie:
    """Class that represents one movie."""

    title: str
    release_year: int
    age_rate: str
    imdb_rating: float
    meta_score: int
    runtime: int
    genre: set[str]
    description: str
    director: str
    stars: set[str]
    gross: int

    def __init__(self, title, release_year, age_rate, imdb_rating, meta_score, runtime, genre, description, director,
                 stars, gross):
        self.title = title
        self.release_year = release_year
        self.age_rate = age_rate
        self.imdb_rating = imdb_rating
        self.meta_score = meta_score
        self.runtime = runtime
        self.genre = genre
        self.description = description
        self.director = director
        self.stars = stars
        self.gross = gross


def csv_to_object(file_name: str) -> list[Movie]:
    """A function that will take in a review file and output a list of Movie objects."""

    output_lst = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            m = Movie(row)

    return output_lst
