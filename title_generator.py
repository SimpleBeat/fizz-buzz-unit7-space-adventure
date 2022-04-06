# Generates a random sci-fi title

import random

def all_titles():
    beginning = ["The Last", "The First", "The Rising", "The Impossible", "The Lucky"]
    beginning_plus = ["Bright", "Space", "Dark", "Shiny", "Cosmic"]
    ending = ["Voyage", "Flight", "Journey", "Star", "Law"]
    ending_plus = ["of the Brave", "of Andromeda", "of Millenia", "of the Universe", "of the Worlds"]

    return [beginning, beginning_plus, ending, ending_plus]

def make_a_title():
    titles = all_titles()
    
    part1 = random.choice(titles[0])
    part2 = random.choice(titles[1])
    part3 = random.choice(titles[2])
    part4 = random.choice(titles[3])

    plus1 = random.choice([True, False])
    plus2 = random.choice([True, False])

    title = part1+" "

    if plus1:
        title += part2 + " "

    title += part3

    if plus2:
        title += " "
        title += part4
    
    return title