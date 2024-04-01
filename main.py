""""CSC111 Winter 2024 Project 2: Movie Recommendation System

Module Description
==================
This Python module is the main module where the program is run.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 Toryn Chua, Jacob Keluthara, Yeonjun Kim, Dan Kim.
"""
from recommendation_system import Main


def run() -> None:
    """Runs the program"""
    main = Main()
    main.run()


if __name__ == "__main__":
    run()
