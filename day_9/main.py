# %%
"""Find the next number in a list of sequences of numbers based on the pattern,
and sum them together to get the answer.

Resources used
https://regexr.com/ [Accessed 11th December 2023]
https://www.programiz.com/python-programming/recursion 
[Accessed 11th December 2023]
https://www.programiz.com/python-programming/methods/list/reverse

"""

def read_text_file(path):
    """Read text file.

    Reads text file into a list of strings. Removes trailing new line
    characters.

    Parameters
    ----------
    path : string
        path to input text file.

    Returns
    -------
    list: string
        text file content.

    """
    with open(path, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


input = read_text_file("input.txt")
print(input)


def get_numbers(input):
    """Takes the input text file, splits into integers and appends into an 
    empty list.

    Parameters
    ----------
    input : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    digits = []
    for line in input:
        digits_line = [int(x) for x in line.split(" ")]
        digits.append(digits_line)

    return digits

digits = get_numbers(input)


def find_differences(digits):
    """_summary_

    Parameters
    ----------
    digits : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """

    all_differences = [digits]
    diff_num = 0
    while True:
        #print(all_differences)
        differences = []
        for i in range(0, len(all_differences[diff_num]) - 1):
            #print(index,num)
            difference = all_differences[diff_num][i + 1] - all_differences[diff_num][i]
            differences.append(difference)
        #print(differences)

        all_differences.append(differences)
        diff_num += 1
        #print(differences)
    
        check_zeros = []
        for diff in differences:
            check_zeros.append(diff == 0)
        #print(check_zeros)
        
        if all(check_zeros):
            break
        
    #print(all_differences)
    
    last_values = []
    
    for i in all_differences:
        last_values.append(i[-1])
        
    
    return sum(last_values)


part_1_sums = []
part_2_sums = []
for digit_line in digits:
    total = find_differences(digit_line)
    part_1_sums.append(total)
    
    digit_line.reverse()
    total = find_differences(digit_line)
    part_2_sums.append(total)
    
print(sum(part_1_sums))
print(sum(part_2_sums))
