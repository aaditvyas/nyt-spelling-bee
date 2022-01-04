from itertools import permutations
from nltk.corpus import words

SPELLING_BEE_LENGTH = 7
MIN_WORD_LENGTH = 4
REQUIRED_LETTER_LENGTH = 1


# function to handle parsing arguments from the commandline
def parse_arguments():
    def user_wants_to_continue_inputting():
        response = input("Would you like to try inputting again? [y]/n")
        result = response == '' or response.lower() == 'y'
        if not result:
            print("Thanks for using the app!")
            exit(0)
        return result

    all_letters = ''
    required_letter = ''

    print("\nWelcome to the nyt-spelling-bee app!")
    print("------------------------------------------\n")

    # get the SPELLING_BEE_LENGTH letters
    valid_input = False
    while not valid_input:
        message = "Please enter the " + str(SPELLING_BEE_LENGTH) + \
                  "letters in today's spelling bee challenge (no spaces): "
        all_letters = input(message)
        if len(all_letters) == SPELLING_BEE_LENGTH:
            valid_input = True
        else:
            print("Incorrect input received: ", all_letters)
            user_wants_to_continue_inputting()

    # get the required letter
    valid_input = False
    while not valid_input:
        required_letter = input("Please enter the required letter in today's spelling bee challenge: ")
        if len(required_letter) == REQUIRED_LETTER_LENGTH and required_letter in all_letters:
            valid_input = True
        else:
            if required_letter not in all_letters:
                print("Given letter ", required_letter, "is not in the given letters", all_letters)
            else:
                print("More than one letter was given: ", required_letter)
            user_wants_to_continue_inputting()

    print("------------------------------------------\n")
    print("Commands:")
    print("> Hit enter to generate next word")
    print("> Enter Q to quit the app\n")
    return all_letters, required_letter


# prepare word dictionary
def get_dictionary():
    eng_dict = set(words.words())
    return eng_dict


# given a set of letters, returns an english word from its permutations
def generate_word(letters, required_letter, checked_words, eng_dict):
    # start with the longest words then go smaller
    for word_length in range(len(letters)+1, MIN_WORD_LENGTH, -1):
        # returns first eng word encountered that has not been seen and contains the required letter
        for potential_word_letters in permutations(letters, word_length):
            potential_word = ''.join(potential_word_letters)
            if potential_word in checked_words or required_letter not in potential_word:
                continue
            elif potential_word in eng_dict:
                checked_words.add(potential_word)
                return potential_word, checked_words
    return -1, checked_words


# interacts with user while generating words
def generate_words(all_letters, required_letter):
    def user_wants_to_continue_getting_words():
        response = input("")
        continue_result = response == ''
        if not continue_result:
            print("------------------------------------------\n")
            print("Thanks for using the app!")
            exit(0)
        return continue_result

    checked_words = set()
    eng_dict = get_dictionary()
    letters_set = set(all_letters)
    repeat_multiple = 0
    looping_flag = True

    while looping_flag:
        for letter in letters_set:
            additional_letters = letter * repeat_multiple
            current_letters = all_letters + additional_letters
            potential_word, checked_words = generate_word(current_letters, required_letter, checked_words, eng_dict)

            # this letter set has been exhausted
            if potential_word != -1:
                print(potential_word)
            user_wants_to_continue_getting_words()
        repeat_multiple += 1


if __name__ == "__main__":
    input_letters, input_required_letter = parse_arguments()
    generate_words(input_letters, input_required_letter)
