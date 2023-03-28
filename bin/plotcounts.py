"""Plot word counts."""

import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description=(
  "Plot word counts."
  ))
parser.add_argument('infile', type=argparse.FileType('r'),
                    nargs='?', default='-',
                    help='Input file name')
parser.add_argument('outfile', type=str,
                    default=None,
                    help='Output file name')
parser.add_argument('-x', '--xlim', type=float, nargs=2,
                    metavar=('XMIN','XMAX'), default=None,
                    help="xlim of the plot")
args = parser.parse_args()

df = pd.read_csv(args.infile, header=None,
                 names=('word', 'word_frequency'))
df['rank'] = df['word_frequency'].rank(ascending=False,
                                       method='max')
df['inverse_rank'] = 1 / df['rank']
ax = df.plot.scatter(x='word_frequency',
                     y='inverse_rank',
                     figsize=[12, 6],
                     grid=True,
                     xlim=args.xlim)
#plt.show()
plt.savefig(args.outfile)
