from collections import deque

"""
This module will be imported into run.py
"""

def write_to_file(filename, data):
    """
    Write to file
    """
    with open(filename, "a") as file:
        file.writelines(data)
        
def update_guess(username, guess):
    """
    Update guesses.txt with player's incorrect guesses
    """
    write_to_file("data/guesses.txt", "{0} - {1}\n".format(username, guess))