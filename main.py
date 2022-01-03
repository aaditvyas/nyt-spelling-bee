import argparse
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


def main():
    args = parse_arguments()
    eng_dict = get_dictionary()


if __name__ == "__main__":
    main()
