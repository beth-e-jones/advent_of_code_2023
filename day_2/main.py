""""
Resources used to solve problem
https://python.land/introduction-to-python/python-boolean-and-operators 
[Accessed December 2nd 2023]
https://regexr.com/ [Accessed 2nd December 2023] 
https://regex101.com/ [Accessed 2nd December 2023]
https://realpython.com/replace-string-python/ [Acessed 2nd December 2023]
https://www.programiz.com/python-programming/tuple [Accessed 2nd December 2023]
https://www.codingrooms.com/blog/dictionary-with-for-loop-python
[Accessed 2nd December 2023]
"""

import re


def read_text_file(path: str) -> list[str]:
    """Read text file.

    Reads text file into a list of strings. Removes trailing new line
    characters.

    Parameters
    ----------
    path : str
        path to input text file.

    Returns
    -------
    list: str
        text file content.

    """
    with open(path, "r") as f:
        return [line.strip("\n") for line in f.readlines()]

DATAPATH = "input_day_2.txt"

read_text_file(DATAPATH)

max_possible_blocks = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def extract_game_details(game):
    """ Splits each line into the games contained in the line, extracts the 
    game number and number of cubes of each colour for each game. Iterates 
    through each colour block for each game to see if the blocks for the game 
    exceed maximum possible.

    Parameters
    ----------
    game : String
        Line in a list of possible games imported from txt file.
    
    Returns
    -------
    game_id_num: String
        Id number extracted from the string reporting the game using regular 
        expression. 
    
    game_possible: Boolean 
        Whether each game is possible based on the number of cubes required. 
        Game is possible = True

    """
    # Set as default to identify games not possible
    game_possible = True
    game_id_string = re.findall(r"(Game\s\d+)", game)[0]
    # Keep only game number to convert to integer to sum later
    game_id_num = int(re.sub((r"([^\d])"),"", game_id_string))
    
    # Split the games by finding the semi-colon separating them 
    sets_in_game = game.replace(game_id_string + ":", "")
    sets_in_game = sets_in_game.split(";")

    
    # Iterate through each game
    for game_set in sets_in_game:
        # Set number of each colour cubes as 0 for default
        game_cubes_dict = {
            "green": 0,
            "red": 0,
            "blue": 0,    
        }
        # Split block information by individual block
        blocks = game_set.split(",")
        for block in blocks:
            block = re.sub("^\s", "", block)
            # If block colour in dictionary, count nhow many and 
            # populate the dictionary
            for color in game_cubes_dict.keys():
                if color in block:
                    count = int(re.sub((r"[^\d]"),"", block))
                    game_cubes_dict[color] = count
        # If game blocks more than max, change game_possible to false
        for color in game_cubes_dict.keys():
            if game_cubes_dict[color] > max_possible_blocks[color]:
                game_possible = False
    
    
    return game_id_num, game_possible

list_of_games = read_text_file(DATAPATH)

game_outcomes = []

# extract game ID and outcome
for game in list_of_games:
    outcome = extract_game_details(game)
    game_outcomes.append(outcome)

# Create of list of successful games based on Boolean for game_possible
successful_games = []
for outcome in game_outcomes:
    if outcome[1] == True:
        successful_games.append(outcome[0])

print(sum(successful_games))