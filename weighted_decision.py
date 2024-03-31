""""CSC111 Project 2:
"""
from __future__ import annotations
import csv
from typing import Any, Optional


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

    # def is_empty(self) -> bool:
    #     """Return whether this tree is empty.
    #
    #     >>> t1 = Tree(None, [])
    #     >>> t1.is_empty()
    #     True
    #     >>> t2 = Tree(3, [])
    #     >>> t2.is_empty()
    #     False
    #     """
    #     return self._root is None

    # def __len__(self) -> int:
    #     """Return the number of items contained in this tree.
    #
    #     >>> t1 = Tree(None, [])
    #     >>> len(t1)
    #     0
    #     >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
    #     >>> len(t2)
    #     3
    #     """
    #     if self.is_empty():
    #         return 0
    #     else:
    #         size = 1  # count the root
    #         for subtree in self._subtrees:
    #             size += subtree.__len__()  # could also write len(subtree)
    #         return size

    # def __contains__(self, item: Any) -> bool:
    #     """Return whether the given is in this tree.
    #
    #     >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
    #     >>> t.__contains__(1)
    #     True
    #     >>> t.__contains__(5)
    #     True
    #     >>> t.__contains__(4)
    #     False
    #     """
    #     if self.is_empty():
    #         return False
    #     elif self._root == item:
    #         return True
    #     else:
    #         for subtree in self._subtrees:
    #             if subtree.__contains__(item):
    #                 return True
    #         return False

    # def __str__(self) -> str:
    #     """Return a string representation of this tree.
    #     """
    #     return self._str_indented(0).rstrip()
    #
    # def _str_indented(self, depth: int) -> str:
    #     """Return an indented string representation of this tree.
    #
    #     The indentation level is specified by the <depth> parameter.
    #     """
    #     if self.is_empty():
    #         return ''
    #     else:
    #         str_so_far = '  ' * depth + f'{self._root}\n'
    #         for subtree in self._subtrees:
    #             str_so_far += subtree._str_indented(depth + 1)
    #         return str_so_far

    # def remove(self, item: Any) -> bool:
    #     """Delete *one* occurrence of the given item from this tree.
    #
    #     Do nothing if the item is not in this tree.
    #     Return whether the given item was deleted.
    #     """
    #     if self.is_empty():
    #         return False
    #     elif self._root == item:
    #         self._delete_root()
    #         return True
    #     else:
    #         for subtree in self._subtrees:
    #             deleted = subtree.remove(item)
    #             if deleted and subtree.is_empty():
    #                 self._subtrees.remove(subtree)
    #                 return True
    #             elif deleted:
    #                 return True
    #         return False

    # def _delete_root(self) -> None:
    #     """Remove the root item of this tree.
    #
    #     Preconditions:
    #         - not self.is_empty()
    #     """
    #     if self._subtrees == []:
    #         self._root = None
    #     else:
    #         last_subtree = self._subtrees.pop()
    #
    #         self._root = last_subtree._root
    #         self._subtrees.extend(last_subtree._subtrees)

    # def __repr__(self) -> str:
    #     """Return a one-line string representation of this tree.
    #     """
    #     str_so_far = "Tree(" + str(self._root) + ", ["
    #     i = 0
    #     for t in self._subtrees:
    #         str_so_far += t.__repr__()
    #         i += 1
    #         if i != len(self._subtrees):
    #             str_so_far += ", "
    #     str_so_far += "])"
    #     return str_so_far

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

        >>> t = Tree(111, [])
        >>> t.insert_sequence([1, 2, 3])
        >>> print(t)
        111
          1
            2
              3
        >>> t.insert_sequence([1, 3, 5])
        >>> print(t)
        111
          1
            2
              3
            3
              5
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
    """
    tree = Tree('', [])  # The start of a decision tree

    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            row.pop(15)
            row.pop(14)
            row.pop(8)
            row.pop(7)
            row.pop(6)
            row.pop(3)
            row.pop(0)
            row.append(row.pop(0))
            # at the end we got Released_Year,Runtime,Genre,Director,Star1,Star2,Star3,Star4,Series_Title

            # if released year is 1927, then the year is 1920 which means 1920 ~ 1930.
            year = int(row[0]) - (int(row[0]) % 10)

            runtime = int(row[1][:-4])

            i = 1
            while True:     # 0 ~ 59, 60 ~ 119, 120 ~ 179, 180 ~ 239, 240 ~ 299, 300 ~ 359...
                if runtime - (60 * i) < 0:
                    runtime = 60 * (i - 1)
                    break
                i += 1

            genre = row[2].split(", ")

            director = row[3]

            actor = [row[4], row[5], row[6], row[7]]

            for g in genre:
                tree.insert_sequence([year, runtime, g, "", "", row[8]])
                tree.insert_sequence([year, runtime, g, director, "", row[8]])
                for a in actor:
                    tree.insert_sequence([year, runtime, g, director, a, row[8]])
                    tree.insert_sequence([year, runtime, g, "", a, row[8]])
    return tree


def recommendation_system(movie_file: str, user_input: dict) -> list[str]:
    """Run a movie recommendation system based on the given movie data file and return the list of recommending movie's
    title.
    """
    tree_so_far = build_decision_tree(movie_file)

    tree_so_far.convert_to_subtree(str(int(user_input["year"])))
    tree_so_far.convert_to_subtree(str(int(user_input["runtime"])))
    tree_so_far.convert_to_subtree(user_input["genre"])
    tree_so_far.convert_to_subtree(user_input["director"])

    if not tree_so_far.subtrees:
        return get_top_5_movies(movie_file)
    else:
        movies_so_far = []
        user_pref_actors = [user_input["actor1"], user_input["actor2"], user_input["actor3"]]
        for i in range(len(tree_so_far.subtrees)):
            for user_a in user_pref_actors:
                if user_a == tree_so_far.subtrees[i].root:
                    for m in tree_so_far.subtrees[i].subtrees:
                        movies_so_far.append(m.root)
        if len(movies_so_far) > 5:
            for _ in range(len(movies_so_far) - 5):
                movies_so_far.pop()
        elif len(movies_so_far) < 5
            m = get_top_5_movies(movie_file)
            for _ in range(5 - len(movies_so_far)):
                movies_so_far.append(m.pop())
        return movies_so_far


def get_top_5_movies(movie_file: str) -> list[str]:
    """Return top 5 movies with the highest ratings.
    """
    movies_so_far = []
    with open(movie_file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            rating = float(row[6])
            movies_so_far.append((row[1], rating))

    movies_so_far.sort(key=lambda x: x[1], reverse=True)
    top_5 = movies_so_far[:5]

    top_5_titles = [movie[0] for movie in top_5]
    return top_5_titles
