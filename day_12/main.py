import re
import itertools


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
    
DATAPATH = "practice_input.txt"

springs = read_text_file(DATAPATH)


# split the lines into the symbols, pattern, and individual pattern items (just in case)
def find_statuses(springs):
    for line in springs:
        patterns, nums = line.split(" ")
        #print(statuses)
        #print(nums)
        split_nums = nums.split(",")
    #print(len(split_nums))
    
    groups_in_line = []
    
    # enumerate each pattern so can find index position of each symbol/group of symbols
    for line in enumerate(patterns):
        for groups in re.finditer(r"[\?+\#+]", patterns):
            # group symmbols found and append to a list
            groups_in_line.append(
                [groups.group(),
                    groups.start(),
                    #groups.end()
                ]
            )
    print(groups_in_line)
    
# next steps
# iterate through each line
# generate every possible combination of #s and ?s in the groups with a replace?
# generate grouped number of #s for each line
# set pattern_possible = False
# if length of groups of #s == len of the number pattern, pattern_possible == True
# append possible pattern and the line to a list

    
    
   
        
        
        

find_statuses(springs)