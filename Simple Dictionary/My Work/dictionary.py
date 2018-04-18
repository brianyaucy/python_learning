import json
from difflib import get_close_matches

data = open("data.json", "r")
dictionary = json.load(data)
data.close()


def look_for_word(input_word):
    #input_word = input_word.lower()
    match = 0
    similar_words = get_close_matches(input_word, dictionary.keys())
    if input_word in dictionary:
        match += 1
        print(f"Found a match '{input_word}'!")
        print_definition(input_word)

    elif input_word.title() in dictionary:
        match += 1
        print(f"Found a match '{input_word.title()}'!")
        print_definition(input_word.title())

    elif input_word.capitalize() in dictionary:
        match += 1
        print(f"Found a match '{input_word.capitalized()}'!")
        print_definition(input_word.capitalized())

    elif len(similar_words) > 0:
        for word in similar_words:
            choice = input(f"""Do you mean the word '{word}'?
(Input 'Y' if Yes or the system will regard your option as No):  """)
            if choice.upper() == 'Y':
                match += 1
                print_definition(word)
                break
            else:
                pass
    if match == 0:
        print("No result.")


def print_definition(word):
    i = 1
    print(f"\nThe word '{word}' has the following definition(s):")
    for definition in dictionary[word]:
        print(f"-  Definition {i}: {definition}")
        i += 1


while True:
    option = 0
    option = input("""
Menu:
"f" - Find definitions of a word;
"q" - Quit the program

Your choice:  """)
    if option.lower() == 'f':
        user_input = input("\nEnter a word you are looking for: ")
        look_for_word(user_input)
    elif option.lower() == 'q':
        print("Closing program ...")
        break
    else:
        print("No such option!")

