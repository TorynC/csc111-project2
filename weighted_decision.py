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
            if subtree.root() == items[0]:
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
            if subtree.root() == item:
                self._root = subtree.root()
                self._subtrees = subtree.subtrees()
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

            year = int(row[0]) - (int(row[0]) % 10)

            runtime = int(row[0][:-4])




            tree.insert_sequence(row)
=======
            year = int(row[0]) - (int(row[0]) % 10) # if released year is 1927, then the year is 1920 which means 1920 ~ 1930.

            runtime = int(row[1][:-4])

            i = 1
            while True:     # 0 ~ 59, 60 ~ 119, 120 ~ 179, 180 ~ 239, 240 ~ 299, 300 ~ 359...
                if runtime - (60 * i) < 0:
                    runtime = 60 * (i - 1)
                    break
                i += 1

            genre = row[2].split(", ")


            tree.insert_sequence([year, runtime, genre, director, actor])

            # tree.insert_sequence(row)

>>>>>>> 9830f58566283c7d8ad1b182932bdf9d07ea6e13


    return tree


MOVIE_QUESTIONS = [
    'What year do you prefer movies from?',
    'What is your preferred running time for movies?',
    'Any preferred genre from the list?',
    'Any preferred directors?',
    'Any preferred actors?'
]


def get_user_input(questions: list[str]) -> list[Any]:
    """Return the user's answers to preference questions."""
    answers_so_far = []

    for i in range(len(questions)):
        print(questions[i])
        s = input(': ')
        answers_so_far.append(s)

    return answers_so_far


def recommendation_system(movie_file: str) -> None:    # Can be used for the test
    """Run a movie recommendation system based on the given movie data file.
    """
    tree_so_far = build_decision_tree(movie_file)
    user_input = get_user_input(MOVIE_QUESTIONS)

    for user in user_input:
        tree_so_far.convert_to_subtree(str(int(user)))

    if not tree_so_far.subtrees:
        print("no movies")
    else:
        for movie in tree_so_far.subtrees:
            print(movie)
