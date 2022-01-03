import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='app to suggest words for the nyt spelling bee game.')
    parser.add_argument('all_letters', type=str, help='set of all letters')
    parser.add_argument('required_letter', type=str, help='required letter')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()

if __name__ == "__main__":
    main()
