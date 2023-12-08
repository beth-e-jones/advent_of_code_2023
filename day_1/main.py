
import pandas as pd
import re

"""
Resources used to solve problem
https://book.pythontips.com/en/latest/lambdas.html [Accessed 1st December 2023]
https://www.w3schools.com/python/python_lambda.asp [Acessed 2nd December 2023]
https://regexr.com/ [Accessed 1st December 2023] 
https://regex101.com/ [Accessed 1st December 2023]
https://www.datacamp.com/tutorial/python-list-index [Accessed 1st December 2023]
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
[Accessed 2nd December 2023]
https://www.geeksforgeeks.org/python-replace-string-by-kth-dictionary-value/ 
[Accessed 1st December 2023]

"""
# Set datapath for the input data
DATAPATH = "input.txt"

with open(DATAPATH) as f:
    lines = f.readlines()

calibration_points_list = [line.strip("\n") for line in lines]

print(type(calibration_points_list))


def identify_calibration_points(calibration_points_list):
    """Takes each string item in the list of calibration points and identifies
    the digits contained in the item, appends them to a list of digits, and
    returns a list of lists containing the digits from each string item.

    Parameters
    ----------
    calibration_points_list : list
        Set input from the advent of code website, containing 1000 string items
        with a mixture of digits and letter characters.
        
    Returns
    -------
    Numeric_calibration_points: List of lists
        This is a list of the separated out, individual digits contained in
        each string item from the input list. 
    """

    numeric_calibration_points = []
    
    for point in calibration_points_list:
        # Search for any digit to identify calibration points
        pattern = r"\d"
        calibration_point = re.findall(pattern,point)
        numeric_calibration_points.append(calibration_point)
    
    return numeric_calibration_points

# Call the function using the input from advent of code as the list of strings        
identify_calibration_points(calibration_points_list)

def find_digits(calibration_points_list):
    """Joins the separated digits found in every string into a single string of
    digits, identifies the first and last (where appplicable) number in each 
    string, joins them to form a list of 1 or 2 digit numbers and sums the list
    to identify the answer to part one. 
    
    Parameters
    ----------
    calibration_points_list : list of lists
        The output of the identify_calibration_points() function. List of the 
        separated out, individual digits contained in each string item from the
        original input list.
    
    Returns
    -------
    summed_calibrations: Integer
        This is the sum of all contents of the list of first and last digits
        for the joined number list. Where the number is a single digit e.g., 7
        this is added as 77 following the Advent of Code instructions.
    """

    numeric_calibrations_unjoined = identify_calibration_points(
        calibration_points_list
    )
    
    joined_digits_list = []
    first_last_digits_list = []
    
    for list_of_digits in numeric_calibrations_unjoined:
        # join digits to sum all calibration points later
        combined_digits = "".join(list_of_digits)
        # Add the combined string to the list of joined digits
        joined_digits_list.append(combined_digits)
    
    for number in joined_digits_list:
        # If single digit number, add same digit twice to make 2 digit number
        if len(number) <= 1:
            first_last_digit = str(number[0])+str(number[0])
            first_last_digits_list.append(int(first_last_digit))
        else:
            # Skips middle digits to keep only relevant digits
            first_last_digit = str(number[0]) + str(number[-1])
            first_last_digits_list.append(int(first_last_digit))
    
    summed_calibrations = sum(first_last_digits_list)
                
    print(f"The sum of all the calibration values is:",
              {summed_calibrations})


# %%
find_digits(calibration_points_list)

# %%                
"""Part 2"""

def words_to_digits(calibration_points_list):
    words_and_digits_list = []
    # Replacing while keeping first digit for overlapping numbers in text
    word_to_digit_dict = {
        "one": "o1",
        "two": "t2", 
        "three": "t3",
        "four": "f4",
        "five": "f5",
        "six": "s6", 
        "seven": "s7",
        "eight": "e8",
        "nine": "n9"
    }
    
    start_positions = {}
    
    for text in word_to_digit_dict.keys():
        start_index = calibration_points_list.find(text)
        if start_index != 1:
            start_positions[text] = calibration_points_list.find(text)
        
        if start_positions != {}:
            sorted_texts = sorted(start_positions.items(), key=lambda x: x[1])
            for sorted_text, _ in sorted_texts:
                words_and_digits_list = str(calibration_points_list.replace(
                    sorted_text[:-1], word_to_digit_dict[sorted_text]
                ))
    
    return words_and_digits_list

# %%
words_to_digits(calibration_points_list)
 # %%   
words_and_digits_list = words_to_digits(calibration_points_list)
replaced_calibration_points = identify_calibration_points(words_and_digits_list)
find_digits(replaced_calibration_points)