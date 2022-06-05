"""
Brief description of what the script does.
For help: python bin/script_template -h
"""

import argparse

def main(args):
    """Run the program."""
    print(f'Input file: {args.infile}')
    print(f'Output file: {args.outfile}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=str, help='Input file name')
    parser.add_argument('outfile', type=str, help='Output file name')
    args = parser.parse_args()
    main(args)
