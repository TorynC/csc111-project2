"""."""
import csv
from typing import Optional


class Movie:
    """Class that represents one movie."""

    title: str
    release_year: int
    imdb_rating: float
    runtime: int
    genre: set[str]
    director: str
    stars: set[str]

    def __init__(self, title, release_year, imdb_rating, runtime, genre, director, stars):
        self.title = title
        self.release_year = release_year
        self.imdb_rating = imdb_rating
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.stars = stars


def csv_to_object(file_name: str) -> list[Movie]:
    """A function that will take in a review file and output a list of Movie objects."""

    output_lst = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            title = row[1]
            release_year = int(row[2])
            runtime = int(row[4].split()[0])
            imdb_rating = float(row[6])
            director = row[9]
            stars = {row[10], row[11], row[12], row[13]}
            genre = set(row[5].split(", "))
            output_lst.append(
                Movie(title, release_year, imdb_rating, runtime, genre, director, stars))

    return output_lst
