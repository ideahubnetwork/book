import argparse
parser = argparse.ArgumentParser('a demo learning argparse')
parser.add_argument(dest='filename', nargs='*')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='text pattern to search for')
parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'}, default='slow', help='search speed')
args = parser.parse_args()

print(args.filename)
print(args.outfile)
print(args.speed)
print(args.verbose)