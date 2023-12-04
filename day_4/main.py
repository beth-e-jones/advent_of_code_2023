import re

# Set datapath
DATAPATH = "input.txt"

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
    list[str]
        text file content.

    """
    with open(path, "r") as f:
        return [line.strip("\n") for line in f.readlines()]
    

# Read in data and define full card
full_card = read_text_file(DATAPATH)


def get_score_wins(full_card):
    """For each row, identifies the numbers for both winning numbers and the 
    numbers the elves hold, checks how many matches there are between the two 
    sets of numbers, and calculates the sum of total points.

    Parameters
    ----------
    full_card : List of strings
        The input from Advent of Code, formed of a list of strings. Each string
        has 2 sets of numbers separated by | to distinguish between winning
        numbers and the numbers the elves hold.
        
    Returns
    ----------
    sum(points): Int
        The sum of the total points from the combined total of row points.
    """
    points = []
    # Split the line into card number, winning numbers, numbers_held
    for line in full_card:
        card_num, numbers = line.split(":")
        winning_nums, held_nums = numbers.split("|")
        
        #print(card_num)
        #print(numbers)
        
        # Use reg ex to identify numbers in the winning numbers
        winning_number_pattern = r"(\d+)"
        winning_numbers = re.findall(winning_number_pattern, winning_nums)
        #print(winning_numbers)
        
        # Use reg ex to identify numbers in the held numbers
        held_nums_pattern = r"(\d+)"
        held_numbers = re.findall(held_nums_pattern, held_nums)
        #print(held_numbers)
        
        # Find numbers that appear in both the winning and held numbers
        numbers_matching = set.intersection(set(winning_numbers), set(held_numbers))
        #print(numbers_matching)
        
        # Calculate points per row and append the score to list of points
        if len(numbers_matching) > 0:
            points_per_row = 2 ** (len(numbers_matching) - 1)
            points.append(points_per_row)
    
    # Sum the list of points for total points    
    return sum(points)
        

# Call the function
get_score_wins(full_card)


