""""CSC111 Winter 2024 Project 2: Movie Recommendation System

Module Description
==================
This Python module is data computing module where use data class to save
movies' data and return the list of all the movies' data in list.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 Toryn Chua, Jacob Keluthara, Yeonjun Kim, Dan Kim.
"""
import csv


class Movie:
    """Class that represents one movie.

    Instance Attributes:
        - title: title of the movie
        - release_year: released year for the movie
        - imdb_rating: movie's rating on the imdb website
        - runtime: running time of the movie
        - genre: genre that movie contians
        - director: director of the movie
        - stars: stars acted on the movie
    """

    title: str
    release_year: int
    imdb_rating: float
    runtime: int
    genre: set[str]
    director: str
    stars: set[str]

    def __init__(self, title: str, release_year: int, imdb_rating: float, runtime: int,
                 genre: set[str], director: str, stars: set[str]) -> None:
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
    with open(file_name, encoding='utf-8') as file:
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


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['csv'],
        'allowed-io': ['csv_to_object'],
        'max-line-length': 120
    })
