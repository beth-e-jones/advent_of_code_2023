
import pandas as pd
import re

# Set datapath for the input data
DATAPATH = "input.txt"

# Read in .txt file from the stored datapath
calibration_points_df = pd.read_table(DATAPATH,
                                      header=None)

# Check data read in successfully
calibration_points_df.head()

# Convert first column of dataframe to a list
calibration_points_list = calibration_points_df.iloc[:, 0].tolist()



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
    # Create empty list to add lists of digits to
    numeric_calibration_points = []
    
    for point in calibration_points_list:
        # Set regular expression pattern to search for (any digit)
        pattern = r"\d"
        # Find all digits in each calibration point
        calibration_point = re.findall(pattern,point)
        # Add the list of found digits to the list of calibration points
        numeric_calibration_points.append(calibration_point)
    
    # Return list of calibration points for use in later functions
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
    # Set variable as the output of the identify_calibration_points() function
    numeric_calibrations_unjoined = identify_calibration_points(
        calibration_points_list
    )
    
    # Create empty list of joined digits to iterate into
    joined_digits_list = []
    first_last_digits_list = []
    
    for list_of_digits in numeric_calibrations_unjoined:
        # join split digits into a single string for each list of split digits
        combined_digits = "".join(list_of_digits)
        # Add the combined string to the list of joined digits
        joined_digits_list.append(combined_digits)
    
    for number in joined_digits_list:
        # If single digit number, add same digit twice to make 2 digit number
        if len(number) <= 1:
            first_last_digit = str(number[0])+str(number[0])
            # Append to list of calibration values
            first_last_digits_list.append(int(first_last_digit))
        # Otherwise, combine first and last character and append to the list of 
        # calibration values
        else:
            first_last_digit = str(number[0]) + str(number[-1])
            first_last_digits_list.append(int(first_last_digit))
    
    summed_calibrations = sum(first_last_digits_list)
                
    print(f"The sum of all the calibration values is:",
              {summed_calibrations})



find_digits(calibration_points_list)
                  
"""Part 2"""

def words_to_digits(calibration_points_list):
    words_and_digits_list = []
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
    
    for point in calibration_points_list:
        for word in word_to_digit_dict.keys():
            point = str.replace(point, word[:-1], word_to_digit_dict[word])
        
        words_and_digits_list.append(point)
    
    return words_and_digits_list
    
    

def answer_2():
    words_and_digits_list = words_to_digits(calibration_points_list)
    dave = identify_calibration_points(words_and_digits_list)
    find_digits(dave)
    
 
    

answer_2()