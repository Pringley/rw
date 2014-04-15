"""rw

Generate random words.

Usage:
  rw [--dict=<wordfile>] <numberofwords>
  rw (-h | --help)
  rw --version

Options:
  -h --help             Show this screen.
  --version             Show version.
  --dict=<wordfile>     Use given word file (optional).

"""
import random
import io
import docopt
import pkg_resources

__VERSION__ = '0.0.1'

def generate_words(numberofwords, wordlist):
    """Generate a list of random words from wordlist."""
    return [random.choice(wordlist) for _ in range(numberofwords)]

def read_wordlist(dictfile):
    """Read a wordlist from file (one word per line)."""
    return [line.strip() for line in dictfile.readlines()]

def load_file(filename):
    """Load a file from the package resources."""

def cli():
    """Run the command line interface."""
    args = docopt.docopt(__doc__, version=__VERSION__)
    numberofwords = int(args['<numberofwords>'])

    dictpath = args['--dict']
    if dictpath is not None:
        dictfile = open(dictpath)
    else:
        rawfile = pkg_resources.resource_stream(__name__, 'words.txt')
        dictfile = io.TextIOWrapper(rawfile, 'utf-8')
    with dictfile:
        wordlist = read_wordlist(dictfile)

    words = generate_words(numberofwords, wordlist)
    print(' '.join(words))
