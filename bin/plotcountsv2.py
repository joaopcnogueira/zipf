"""
Plot Word counts.
"""

import argparse
import pandas as pd


def load_csv(infile):
    """Loads the csv file."""
    df = pd.read_csv(args.infile, header=None, names=["word", "word_frequency"])
    return df


def create_plot_counts(df, xlim, outfile):
    """Create the word frequency plot."""
    fig_title = ' '.join(outfile.split('/')[-1].split('.')[0].split('_')).title()
    plot = df.head(xlim).plot(kind='bar', x='word', y='word_frequency',
                              rot=30, figsize=(12, 6),
                              title=f"Word Frequency of {fig_title}",
                              xlabel="Word", ylabel="Frequency",
                              legend=False)
    fig = plot.get_figure()
    fig.savefig(outfile)


def main(args):
    """Run the program."""
    df = load_csv(args.infile)
    create_plot_counts(df, xlim=args.xlim, outfile=args.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-o', '--outfile',
                        type=str, default='plotcounts.png',
                        help='Output file name')
    parser.add_argument('--xlim', type=int, default=10,
                        help='x-axis bounds')
    args = parser.parse_args()
    main(args)
