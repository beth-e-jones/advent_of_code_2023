# %%
from collections import Counter, defaultdict

DATAPATH = "practice_input.txt"

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


games = read_text_file(DATAPATH)
# %%
print(games)

# %%
for line in games:
    hand, bid = line.split(" ")
    print(hand, bid)

round = zip(hand, bid)
print(round)


# %%
def identify_hand(hand):
    cards_to_letters = {
        "A": "A", 
        "K": "B", 
        "Q": "C", 
        "J": "D", 
        "T": "E", 
        "9": "F", 
        "8": "G", 
        "7": "H", 
        "6": "I", 
        "5": "J", 
        "4": "K", 
        "3": "L",
        "2": "M"    
    }

    for key, value in cards_to_letters.items():
        if key in hand:
            hand = hand.replace(key, value)
    
    return hand

# %%
identify_hand(hand)

# %%
# iterate through game
# set running counts for all digits and numbers
# produce count at the end
# biggest_group = counts[hand]
#   if biggest group matches the key value, return a rank
# multiply score and rank together
# sum all these together


# 
# %%

# %%


