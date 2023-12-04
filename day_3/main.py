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
    """_summary_

    Parameters
    ----------
    pattern : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    part_numbers = []
    characters_per_line = len(pattern[0])
    
    for row_num, line in enumerate(pattern):
        part_numbers_in_line = []
        for numbers_in_line in re.finditer(r"\d+", line):
            part_numbers_in_line.append(
                [
                    numbers_in_line.group(),
                    numbers_in_line.start(),
                    numbers_in_line.end(),
                ]
            )
        
        if row_num == 0:
            min_row = 0
            max_row = row_num + 1
        elif row_num == (len(pattern) - 1):
            min_row = row_num - 1
            max_row = len(pattern) - 1
        else:
            min_row = row_num - 1
            max_row = row_num + 1
            
        for part_number, start, end in part_numbers_in_line:
            if start - 1 < 0:
                min_col = 0
            else:
                min_col = start - 1

            if end + 1 > characters_per_line - 1:
                max_col = characters_per_line - 1
            else:
                max_col = end + 1

            grid_characters = []
            for row in range(min_row, max_row + 1):
                grid_characters.append(pattern[row][min_col:max_col])
            grid_string = "".join(grid_characters)
            
            if re.search(r"[^\d\.]", grid_string):
                part_numbers.append(int(part_number))
    
    return sum(part_numbers)
            
        
print(find_patterns(full_pattern))

def find_gear_ratio(pattern):
    gear_ratios = []
    characters_per_line = len(pattern[0])
    
    for row_num, line in enumerate(pattern):
        gears = []
        for gear in re.finditer(r"\*", line):
            gears.append([row_num, gear.start()])

        if row_num == 0:
            min_row = 0
            max_row = row_num + 1
        elif row_num == (len(pattern) - 1):
            min_row = row_num - 1
            max_row = len(pattern) - 1
        else:
            min_row = row_num - 1
            max_row = row_num + 1
        
        for gear_row, gear_col in gears:
            if gear_col - 3 < 0:
                min_col = 0
            else:
                min_col = gear_col - 3
            
            if gear_col + 4 > characters_per_line - 1:
                max_col = characters_per_line
            else:
                max_col = gear_col + 4
            
            grid_part_numbers = []
            for row in range(min_row, max_row + 1):
                for part_number in re.finditer(r"\d+", pattern[row][min_col:max_col]):
                    start_idx  = part_number.start()
                    end_idx = part_number.end()
                    print(part_number.group(), start_idx, end_idx)
                    if (row == min_row) | (row == max_row):
                        if (
                            (start_idx <= 4) and (end_idx >= 3)
                        ):
                            grid_part_numbers.append(int(part_number.group()))
                    else:
                        if (end_idx == 3) | (start_idx == 4):
                            grid_part_numbers.append(int(part_number.group()))
            print(grid_part_numbers)            
            if len(grid_part_numbers) == 2:
                gear_ratios.append(prod(grid_part_numbers))
        
                
            
    return sum(gear_ratios)


print(find_gear_ratio(full_pattern))
