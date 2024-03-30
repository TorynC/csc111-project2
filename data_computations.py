"""."""
import csv
from typing import Optional


class Movie:
    """Class that represents one movie."""

    title: str
    release_year: int
    age_rate: str
    imdb_rating: float
    meta_score: Optional[int]
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
        next(reader)
        for row in reader:
            title = row[1]
            release_year = int(row[2])
            age_rate = row[3]
            runtime = int(row[4].split()[0])
            imdb_rating = float(row[6])
            description = row[7]
            metascore = int(row[8])
            director = row[9]
            stars = {row[10], row[11], row[12], row[13]}
            genre = set(row[5].split())
            gross = int(row[15])
            output_lst.append(
                Movie(title, release_year, age_rate, imdb_rating, metascore, runtime, genre, description, director,
                      stars, gross))

    return output_lst
