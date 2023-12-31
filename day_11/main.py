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

universe = read_text_file(DATAPATH)

def expand_universe(universe):
    all_cols = set(range(0, len(universe[0])))
    #print(all_cols)
    temp_universe = []
    galaxy_set = set()
    
    for i,line in enumerate(universe):
        temp_universe.append(line)
        if "#" not in line:
            temp_universe.append(line)
        galaxy_cols = [galaxy.start() for galaxy in re.finditer(r"#", line)]
        #print(galaxy_cols)
        for location in galaxy_cols:
            galaxy_set.add(location)
            
    empty_cols = sorted(all_cols.difference(galaxy_set), reverse=True)
    
    output_universe = []
    for line in temp_universe:
        temp_line = line
        for col in empty_cols:
            temp_line = temp_line[:col] + "." + temp_line[col:]
        output_universe.append(temp_line)
            
    
    return output_universe

output_universe = expand_universe(universe)

#expanded_universe = read_text_file("output.txt")
#assert output_universe == expanded_universe

def find_galaxies(expanded_universe):
    galaxy_positions = []
    for i, line in enumerate(expanded_universe):
        galaxy_cols = [galaxy.start() for galaxy in re.finditer(r"#", line)]
        for galaxy_col in galaxy_cols:
            galaxy_positions.append((i, galaxy_col))
    
    #print(len(galaxy_positions))
    #print(galaxy_positions)
    
    galaxy_finder = {
        id: coords for id, coords in zip(
            range(0, len(galaxy_positions)), galaxy_positions
        )
    }
    
    return galaxy_finder
    
    #print(galaxy_finder)
    
galaxy_finder = find_galaxies(output_universe)

def manhattan_distance(input_1,input_2):
    return sum(abs(val1-val2) for val1, val2 in zip(input_1,input_2))


def total_distances(galaxy_finder):
    manhattan_distances = []
    #print(galaxy_finder)
    for galaxy_1, galaxy_2 in itertools.combinations(galaxy_finder.keys(), 2):
        distance = manhattan_distance(galaxy_finder[galaxy_1],galaxy_finder[galaxy_2])
        manhattan_distances.append(distance)
    print(sum(manhattan_distances))
    

total_distances(galaxy_finder)

# Part 2

def galaxy_distances_with_expansion():
    unexpanded_galaxy_dict = find_galaxies(galaxy_finder)
    


