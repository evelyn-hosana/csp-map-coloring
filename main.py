"""
main.py - entry point for CSP map coloring.

parses CLI args, validates maps, computes chromatic numbers, runs experiments, and prints results tables.

usage:
    python main.py                   # both maps, 5 trials, seed=42
    python main.py --map australia
    python main.py --map usa
    python main.py --trials 10
    python main.py --seed 0          # 0 = no fixed seed (truly random)
    python main.py --colors 4        # skip chromatic search, use k=4 for both maps
    python main.py --visualize       # show graph after solving
    python main.py --no-heuristics   # only run no-heuristic variants
    python main.py --heuristics      # only run heuristic variants
"""
import argparse
import random
from maps import AUSTRALIA, USA

def parse_args():
    parser = argparse.ArgumentParser(description="CSP map coloring")
    parser.add_argument(
        '--map',
        choices=['australia', 'usa', 'both'],
        default='both',
        help="map to run (default: both)"
    )
    parser.add_argument(
        '--trials',
        type=int,
        default=5,
        help="trials per algorithm (default: 5)"
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help="random seed (default: 42)"
    )
    parser.add_argument(
        '--colors',
        type=int,
        default=None,
        help="force k colors instead of computing chromatic number"
    )
    parser.add_argument(
        '--visualize',
        action='store_true',
        help="show graph visualization after solving"
    )
    parser.add_argument(
        '--no-heuristics',
        action='store_true',
        dest='no_heuristics',
        help="only run no-heuristic variants"
    )
    parser.add_argument(
        '--heuristics',
        action='store_true',
        dest='heuristics',
        help="only run heuristic variants"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # seed random for reproducibility; skip if seed=0
    if args.seed != 0: random.seed(args.seed)

    print("Hello, this will be used for CSP map coloring!")

if __name__ == '__main__':
    main()