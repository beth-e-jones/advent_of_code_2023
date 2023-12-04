import re
from math import prod

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

full_pattern = read_text_file("input.txt")


def find_patterns(pattern):
    """Uses reg ex to find the numbers in the pattern, identifies start and end
    index positions for the numbers, and defines the minimum and maximum row 
    and column numbers 

    Parameters
    ----------
    pattern : List of strings 
        Each row has a pattern of dots, special characters, and integers.
        
    Returns
    -------
    sum(part_numbers): Int
        The sum of all integers identified that have a special character in an
        index position next to any of the digits (including diagonal)
    """
    
    part_numbers = []
    # Sets characters per line to be the length of first row of pattern
    characters_per_line = len(pattern[0])
    
    for row_num, line in enumerate(pattern):
        part_numbers_in_line = []
        # Use reg ex to identify any digits in the row
        for numbers_in_line in re.finditer(r"\d+", line):
            # Append the grouped digits, start index, and end index
            part_numbers_in_line.append(
                [
                    numbers_in_line.group(),
                    numbers_in_line.start(),
                    numbers_in_line.end(),
                ]
            )
        
        # Set min and max possible rows to consider around the pattern to
        # account for numbers in the top/bottom line, then a default for others
        if row_num == 0:
            min_row = 0
            max_row = row_num + 1
        elif row_num == (len(pattern) - 1):
            min_row = row_num - 1
            max_row = len(pattern) - 1
        else:
            min_row = row_num - 1
            max_row = row_num + 1
        
        # Set min and max possible columns to consider around the pattern to
        # account for numbers in the first/last col, then a default for others 
        for part_number, start, end in part_numbers_in_line:
            if start - 1 < 0:
                min_col = 0
            else:
                min_col = start - 1

            if end + 1 > characters_per_line - 1:
                max_col = characters_per_line - 1
            else:
                max_col = end + 1

            # identifies string from the included columns and rows before and
            # after number
            grid_characters = []
            for row in range(min_row, max_row + 1):
                grid_characters.append(pattern[row][min_col:max_col])
            grid_string = "".join(grid_characters)
            
            # If a special character (anything other than digits or spaces) 
            # found in the cells around the number, append part number
            if re.search(r"[^\d\.]", grid_string):
                part_numbers.append(int(part_number))
    
    # sum part numbers list for answer
    return sum(part_numbers)
            
# call function and print the answer        
print(find_patterns(full_pattern))

# Part 2
def find_gear_ratio(pattern):
    gear_ratios = []
    characters_per_line = len(pattern[0])
    
    # Use reg ex to find all *s to represent gears
    for row_num, line in enumerate(pattern):
        gears = []
        for gear in re.finditer(r"\*", line):
            # Append the start index for each *
            gears.append([row_num, gear.start()])
            
        # Set min and max possible rows to consider around the pattern to
        # account for numbers in the top/bottom line, then a default for others
        if row_num == 0:
            min_row = 0
            max_row = row_num + 1
        elif row_num == (len(pattern) - 1):
            min_row = row_num - 1
            max_row = len(pattern) - 1
        else:
            min_row = row_num - 1
            max_row = row_num + 1
            
        # Set min and max possible columns to consider around the pattern to
        # account for numbers in the first/last col, then a default for others        
        for gear_row, gear_col in gears:
            if gear_col - 3 < 0:
                min_col = 0
            else:
                min_col = gear_col - 3
            
            if gear_col + 4 > characters_per_line - 1:
                max_col = characters_per_line
            else:
                max_col = gear_col + 4
            
            # Iterate through to find digits in the rows and patterns identified
            grid_part_numbers = []
            for row in range(min_row, max_row + 1):
                for part_number in re.finditer(r"\d+", pattern[row][min_col:max_col]):
                    # Find and store start and end index positions
                    start_idx  = part_number.start()
                    end_idx = part_number.end()
                    print(part_number.group(), start_idx, end_idx)
                    if (row == min_row) | (row == max_row):
                        # If index positions relative to * mean it will touch,
                        # append part number to list of part numbers
                        if (
                            (start_idx <= 4) and (end_idx >= 3)
                        ):
                            grid_part_numbers.append(int(part_number.group()))
                    else:
                        if (end_idx == 3) | (start_idx == 4):
                            grid_part_numbers.append(int(part_number.group()))
            print(grid_part_numbers)
            # if more than 2 items in each list of grid part numbers, multiply
            # both numbers and append score to list of ratios            
            if len(grid_part_numbers) == 2:
                gear_ratios.append(prod(grid_part_numbers))
        
                
    # sum the list of ratios        
    return sum(gear_ratios)


print(find_gear_ratio(full_pattern))
