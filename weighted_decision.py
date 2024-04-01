""""CSC111 Winter 2024 Project 2: Movie Recommendation System

Module Description
==================
This Python module is weighted decision module where get the data for the
movies and user input and then create movie recommendation based on the given
data.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 Toryn Chua, Jacob Keluthara, Yeonjun Kim, Dan Kim.
"""
from __future__ import annotations
from typing import Any, Optional
from data_computations import csv_to_object


class Tree:
    """A recursive tree data structure.

    Representation Invariants:
        - self._root is not None or self._subtrees == []
        - all(not subtree.is_empty() for subtree in self._subtrees)
    """
    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If root is None, the tree is empty.

        Preconditions:
            - root is not none or subtrees == []
        """
        self._root = root
        self._subtrees = subtrees

    def insert_sequence(self, items: list) -> None:
        """Insert the given items into this tree.

        The inserted items form a chain of descendants, where:
            - items[0] is a child of this tree's root
            - items[1] is a child of items[0]
            - items[2] is a child of items[1]
            - etc.

        Do nothing if items is empty.

        The root of this chain (i.e. items[0]) should be added as a new subtree within this tree, as long as items[0]
        does not already exist as a child of the current root node. That is, create a new subtree for it
        and append it to this tree's existing list of subtrees.

        If items[0] is already a child of this tree's root, instead recurse into that existing subtree rather
        than create a new subtree with items[0]. If there are multiple occurrences of items[0] within this tree's
        children, pick the left-most subtree with root value items[0] to recurse into.

        Preconditions:
            - not self.is_empty()
        """
        if not items:
            return

        for subtree in self._subtrees:
            if subtree._root == items[0]:
                subtree.insert_sequence(items[1:])
                return

        new_subtree = Tree(items[0], [])
        self._subtrees.append(new_subtree)
        new_subtree.insert_sequence(items[1:])

    def convert_to_subtree(self, item: Optional[Any]) -> None:
        """Change the tree into the subtree which has the matching root with given item
        If there is not matching subtree in the tree, change tree into an empty tree
        """
        for subtree in self._subtrees:
            if subtree._root == item:
                self._root = subtree._root
                self._subtrees = subtree._subtrees
                return
        self._root = None
        self._subtrees = []

    @property
    def subtrees(self) -> list[Tree]:
        """Return subtrees of the tree
        """
        return self._subtrees

    @property
    def root(self) -> Any:
        """Return root of the tree
        """
        return self._root


def build_decision_tree(file: str) -> Tree:
    """Build a decision tree storing the movie data from the given file.

    For the given file, each line should be in this format:
    Poster_Link,Series_Title,Released_Year,Certificate,Runtime,Genre,IMDB_Rating,Overview,Meta_score,Director,
    Star1,Star2,Star3,Star4,No_of_Votes,Gross
    """
    tree = Tree('', [])  # The start of a decision tree

    movies = csv_to_object(file)

    for movie in movies:
        # Removing one's digit to make group and set the range of years.
        # 1920s, 1930s, 1940s.... (In real code, it is saved as int and there is no 's' at the end.)
        year = movie.release_year - (movie.release_year % 10)

        # The same method for runtime. Given runtime = 155 min turn to 120.
        runtime = movie.runtime

        # 0 ~ 59, 60 ~ 119, 120 ~ 179, 180 ~ 239, 240 ~ 299, 300 ~ 359...
        # The lowest number for each range will be stored.
        i = 1
        while True:
            if runtime - (60 * i) < 0:
                runtime = 60 * (i - 1)
                break
            i += 1

        director = movie.director.lower()

        stars = movie.stars
        stars.add("")

        title = movie.title
        rating = movie.imdb_rating

        # Since there is cases where user don't put any director or actors for their input, we added empty cases for
        # each movie saved in our tree.
        # We added the case of (no director, no actor), (no direct, actor), (director, actor), (director, no actor).
        # In the file, since each movie has max 3 genre, and 4 actors, at the movie's title degree of the tree, ther
        # -e are duplications.
        for g in movie.genre:
            for s in stars:
                tree.insert_sequence([year, runtime, g.lower(), director, s.lower(), title, rating])
                tree.insert_sequence([year, runtime, g.lower(), "", s.lower(), title, rating])
    return tree


def recommendation_system(movie_file: str, user_input: dict) -> list[str]:
    """Run a movie recommendation system based on the given movie data file and return the list of recommending movie's
    title.
    """
    tree_so_far = build_decision_tree(movie_file)

    # Removing all the subtrees that does not match with user's input.
    tree_so_far.convert_to_subtree(int(user_input["year"]) - (int(user_input["year"]) % 10))

    # Setting user's input as range to match with saved runtime in the decision tree.
    runtime = int(user_input["runtime"])
    i = 1
    while True:  # 0 ~ 59, 60 ~ 119, 120 ~ 179, 180 ~ 239, 240 ~ 299, 300 ~ 359...
        if runtime - (60 * i) < 0:
            runtime = 60 * (i - 1)
            break
        i += 1

    tree_so_far.convert_to_subtree(runtime)
    tree_so_far.convert_to_subtree(user_input["genre"].lower())
    tree_so_far.convert_to_subtree(user_input["director"].lower())

    if not tree_so_far.subtrees:  # The case when there is no matching movies.
        return get_top_5_movies(movie_file)
    else:
        movies_so_far = {}
        user_pref_actors = [user_input["actor1"].lower(), user_input["actor2"].lower(), user_input["actor3"].lower()]
        movie_titles = []

        # Get the movies that has matching actors with user's input and save their rating as dictionary.
        # This dictionary removes all the duplicant created in the decision tree.
        for i in range(len(tree_so_far.subtrees)):
            for user_a in user_pref_actors:
                if user_a == tree_so_far.subtrees[i].root:
                    for m in tree_so_far.subtrees[i].subtrees:
                        movies_so_far[m.root] = m.subtrees[0].root

        # Using dictionary, sort the movies by the rating.
        for key in movies_so_far:
            if not movie_titles:
                movie_titles.append(key)
            else:
                added = False
                for i in range(len(movie_titles)):
                    if movies_so_far[movie_titles[i]] < movies_so_far[key]:
                        movie_titles.insert(i, key)
                        added = True
                        break
                if not added:
                    movie_titles.append(key)

        if len(movie_titles) > 5:  # Since there is more than 5 movies, leave only top 5 movies.
            for _ in range(len(movie_titles) - 5):
                movie_titles.pop()
        elif len(movie_titles) < 5:  # Since there is less then 5 movies, add top rating movies.
            m = get_top_5_movies(movie_file)
            for _ in range(5 - len(movie_titles)):
                movie_titles.append(m.pop())

        return movie_titles


def get_top_5_movies(movie_file: str) -> list[str]:
    """Return top 5 movies with the highest ratings.
    """
    movies_so_far = []
    movies = csv_to_object(movie_file)
    for movie in movies:
        movies_so_far.append((movie.title, movie.imdb_rating))
    movies_so_far.sort(key=lambda x: x[1], reverse=True)
    top_5 = movies_so_far[:5]

    top_5_titles = [m[0] for m in top_5]
    return top_5_titles


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['data_computations'],
        'allowed-io': [],
        'max-line-length': 120
    })
