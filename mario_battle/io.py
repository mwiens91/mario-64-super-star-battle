"""Contains functions for displaying and retreiving info.

All using the command line, at present.
"""

from mario_battle.constants import COURSE_DICTIONARY


def display_welcome_message():
    """Displays a welcome message to the user."""
    print("HEY WELCOME TO MARIO")

def get_player_names():
    """Gets the player names from the user.

    Returns:
        A tuple of two strings, containing the player names.
    """
    return ("Matt", "Branko")

def get_number_of_rounds():
    """Gets the number of rounds from the user.

    The number of rounds must be odd and be no more than 15 (the number
    of courses in Mario 64).

    Returns:
        An integer specifying the number of rounds.
    """
    return 5

def print_courses(course_dict=COURSE_DICTIONARY):
    """Prints a set of Mario 64 courses.

    By default, this includes all of the courses, all listed as
    unplayed, if the course_dict argument isn't passed in.

    Arg:
        course_dict: An optional dictionary (following the schema of
            COURSE_DICTIONARY from constants.py) specifying for each
            course number, what the name of the course is and whether it
            has already been played. Defaults to all courses, with all
            of them unplayed.
    """
    print(course_dict)
