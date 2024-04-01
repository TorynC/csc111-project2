""""CSC111 Project 2: Movie Recommendation System

The part where we create ask questions and run recommending system and give recommanding movies.
Simply, get input and run the code and give the output.
This is not the file where we putting system. This is for calling system.

separate the recommendation system with 2 ways one way with decision tree asking questions based on quiz when user doesnt have an account
another way is when user does have an account using graph and user watchlist
"""
from recommendation_system import Main

if __name__ == "__main__":
    main = Main()
    main.run()
