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
    import doctest

    doctest.testmod(verbose=True)

    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'recommendation_system'],
        'allowed-io': [],
        'max_line_length': 120,
        'disable': []
    })
    run()
