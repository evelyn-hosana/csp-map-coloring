"""
main.py - entry point for CSP map coloring

parses CLI args, computes chromatic numbers, runs experiments, writes results to markdown

usage:
    python main.py                   # both maps, 5 trials, seed=42
    python main.py --map australia
    python main.py --map usa
    python main.py --trials 10
    python main.py --seed 0          # 0 = no fixed seed (truly random)
    python main.py --colors 4        # skip chromatic search, use k=4 for both maps
    python main.py --visualize       # save graph visualization
    python main.py --no-heuristics   # only run no-heuristic variants
    python main.py --heuristics      # only run heuristic variants
"""
import argparse
import os
import sys
import random
from maps import AUSTRALIA, USA, AUSTRALIA_POS, USA_POS
from chromatic import compute_chromatic_number
from experiment import run_experiment, write_results_md, NUM_TRIALS

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')

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
        default=NUM_TRIALS,
        help=f"trials per algorithm (default: {NUM_TRIALS})"
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help="random seed (default: 42; 0 = no fixed seed)"
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
        help="save graph visualization after solving"
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

def _output_filename(args):
    """Build unique output filename from CLI args"""
    parts = [args.map, f'{args.trials}trials', f'seed{args.seed}']
    if args.no_heuristics: parts.append('noh')
    elif args.heuristics: parts.append('h')
    return '_'.join(parts) + '.md'

def main():
    args = parse_args() # parse CLI args
    if args.seed != 0: random.seed(args.seed) # seed for reproducibility; skip if seed=0
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ordered list of (display_name, adjacency_dict, position_dict)
    maps_to_run = []
    if args.map in ('australia', 'both'): maps_to_run.append(('Australia', AUSTRALIA, AUSTRALIA_POS))
    if args.map in ('usa', 'both'): maps_to_run.append(('USA', USA, USA_POS))

    # --heuristics skips no-heuristic section and vice versa
    run_no_h = not args.heuristics
    run_h = not args.no_heuristics

    sections_label = (
        'without heuristics only' if args.no_heuristics else
        'with heuristics only' if args.heuristics else
        'all variants'
    )

    map_label = {'australia': 'Australia', 'usa': 'USA', 'both': 'Australia & USA'}.get(args.map, args.map)
    seed_label = args.seed if args.seed != 0 else 'random'
    print(f"\nCSP Map Coloring")
    print(f"Running {sections_label} on {map_label} ({args.trials} trials, seed={seed_label})")

    all_results = {}

    for map_name, adjacency, pos in maps_to_run:
        print(f"\n[{map_name}] Chromatic number...", end=' ', flush=True)

        # determine k
        if args.colors is not None:
            k = args.colors
            solution = None
            print(f"k={k} (forced)")
        else:
            k, solution = compute_chromatic_number(adjacency)
            print(f"k={k}")

        if args.visualize and solution:
            try:
                from visualize import draw_colored_map
                if map_name == "USA":
                    title = f"USA (50 States) Map Coloring Solution |  χ(G) = {k}"
                else:
                    title = f"{map_name} Map Coloring Solution |  χ(G) = {k}"    
                draw_colored_map(adjacency, solution, title, output_name=map_name,output_dir=OUTPUT_DIR, pos=pos)
                vis_path = os.path.join(OUTPUT_DIR, f'{map_name}.png')
                print(f"[{map_name}] Visualization saved at {vis_path}")
            except Exception as e:
                print(f"[{map_name}] Visualization skipped: {e}")

        results = run_experiment(
            adjacency, k, map_name, args.trials,
            run_no_heuristics=run_no_h,
            run_heuristics=run_h,
        )
        all_results[map_name] = results
        print(f"[{map_name}] Done!")

    output_path = os.path.join(OUTPUT_DIR, _output_filename(args))
    write_results_md(all_results, output_path)
    print(f"\nSaved results to {output_path}")
    os._exit(0)

if __name__ == '__main__':
    main()