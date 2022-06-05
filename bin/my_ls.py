"""
List the files in a give directory with a given suffix sorted alphabetically.
This script was develop as an answer to the question 5.11.2.
For help: python bin/my_ls.py -h.
Usage: python bin/my_ls.py data csv
"""

import glob
import argparse


def get_sorted_files_list_names(dir: str, suffix: str):
    files_list_names = glob.glob(f"{dir}/*.{suffix}")
    sorted_files_list_names = sorted(files_list_names)
    return sorted_files_list_names


def print_files_list_names(files_list_names: list):
    str_files_list_names = '\n'.join(files_list_names)
    print(str_files_list_names)


def main(args):
    """Run the program."""
    files = get_sorted_files_list_names(args.dir, args.suffix)
    print_files_list_names(files_list_names=files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type=str, help='Directory')
    parser.add_argument('suffix', type=str, help='File suffix')
    args = parser.parse_args()
    main(args)
