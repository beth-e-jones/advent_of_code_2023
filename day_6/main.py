import pandas as pd
import re
import numpy as np
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

results = read_text_file(DATAPATH)

def identify_wins(results):
    """Splits text file into two strings in each line, one with times and 
    numbers and one for distance and numbers. Iterates through each race and 
    each possible button hold starting at each millisecond in the race duration.
    Checks if possible distance travelled is higher than the record and if so, 
    adds 1 to win counter. Appends wins per race to a list of race wins and 
    returns product of all race wins.

    Parameters
    ----------
    results : List of strings
        Txt file split into 2 lines of strings for distance and time.
    
    Returns
    ----------
    results : _type_
        _description_
        
    """
    # Create empty list of wins
    wins = []
    
    # Split first line of input file to identify race times
    time_title, joined_times = results[0].split(":")
    times_pattern = r"(\d+)"
    times = re.findall(times_pattern, joined_times)
    
    # Split second line of input file to identify race distances
    distance_title, joined_distances = results[1].split(":")  
    distances_pattern = r"(\d+)"
    distances = re.findall(distances_pattern, joined_distances)
    
    # Zip race time and distance together into a tuple to iterate through
    for time, distance in zip(times, distances):
        # For each race, reset variables to zero
        speed = 0
        distance_travelled = 0
        time_left = 0
        race_wins = 0
        # Iterate through possible button start times for full time of race
        for button_time in range (0, int(time) + 1):
            travel_time = int(time) - button_time
            speed = button_time
            # Calculate distance travelled based on increasing speed 
            distance_travelled = speed * travel_time
            # If possible distance exceeds record distance, add win to count
            if distance_travelled > int(distance):
                race_wins = race_wins + 1
        wins.append(race_wins)
    
    # Return the product of all win counts for all races
    return np.prod(wins)
            
identify_wins(results)
