import argparse
from itertools import permutations
from nltk.corpus import words


# function to handle parsing arguments from the commandline
def parse_arguments():
    parser = argparse.ArgumentParser(description='app to suggest words for the nyt spelling bee game.')
    parser.add_argument('all_letters', type=str, help='set of all letters')
    parser.add_argument('required_letter', type=str, help='required letter')
    args = parser.parse_args()
    return args


# prepare word dictionary
def get_dictionary():
    eng_dict = set(words.words())
    return eng_dict


# given a set of letters, returns an english word from its permutations
def generate_word(letters, required_letter, checked_words, eng_dict):
    # start with the longest words then go smaller
    for word_length in range(len(letters)+1, 1, -1):
        # returns first eng word encountered that has not been seen and contains the required letter
        for potential_word_letters in permutations(letters, word_length):
            potential_word = ''.join(potential_word_letters)
            if potential_word in checked_words or required_letter not in potential_word:
                continue
            elif potential_word in eng_dict:
                checked_words.add(potential_word)
                return potential_word, checked_words
    return -1, checked_words


def main():
    checked_words = set()
    args = parse_arguments()
    eng_dict = get_dictionary()
    potential_word = generate_word(args.all_letters, args.required_letter, checked_words, eng_dict)

    print(potential_word)

    # first pass will be using 0 repeat letters

    # second pass will be using 1 repeat letter for each letter


if __name__ == "__main__":
    main()
