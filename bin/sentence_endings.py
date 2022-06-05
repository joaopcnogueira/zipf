"""
Count the occurrences of sentence endings characters, e.g ".", "!" and "?"
"""

import argparse


def print_sentence_endings(collection_dict):
    """Print the sentence endings characters along with count information."""
    for k, v in collection_dict.items():
        print(f"Number of {k} is {v}")


def count_sentence_endings(reader):
    """Count the occurrence of sentence endings characters."""
    text = reader.read()
    sentence_endings_counts = {}
    sentence_endings_counts['.'] = text.count(".")
    sentence_endings_counts['!'] = text.count("!")
    sentence_endings_counts['?'] = text.count("?")
    return sentence_endings_counts


def main(args):
    """Run the command line program."""
    sentence_endings_counts = count_sentence_endings(args.infile)
    print_sentence_endings(sentence_endings_counts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    args = parser.parse_args()
    main(args)
