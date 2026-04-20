# CSP Map Coloring

Solves the map coloring problem for Australia and USA using constraint satisfaction (CSP) backtracking. Computes the chromatic number for each map, then benchmarks six algorithm variants across multiple trials, measuring backtrack counts and execution time.

## Algorithms

Three variants **without heuristics** (random variable order per trial):
- DFS
- DFS + Forward Checking
- DFS + FC + Singleton Propagation

Three variants **with heuristics** (MRV + Degree Constraint for variable selection, LCV for value ordering):
- DFS + H
- DFS + FC + H
- DFS + FC + Singleton + H

## Files

| File | Description |
|------|-------------|
| `main.py` | Entry point — parses CLI args, runs chromatic number search, dispatches experiments, writes results |
| `maps.py` | Adjacency dictionaries and geographic coordinates for Australia (7 regions) and USA (50 states) |
| `csp.py` | `MapColoringCSP` class — holds variables, domains, adjacency, backtrack counter, and consistency checks |
| `algorithms.py` | All six solver variants built on a shared recursive backtracking skeleton |
| `heuristics.py` | MRV, Degree Constraint, and LCV heuristic functions used by heuristic variants |
| `chromatic.py` | Computes chromatic number by incrementing k until a valid coloring is found |
| `experiment.py` | Runs trials, enforces a 30-second timeout per trial (DNF if exceeded), aggregates results, and writes markdown output |
| `visualize.py` | Renders the colored map as a PNG using networkx and matplotlib (optional) |

## Usage

```bash
python main.py                    # both maps, 5 trials, seed=42
python main.py --map australia    # Australia only
python main.py --map usa          # USA only
python main.py --trials 10        # change trial count
python main.py --seed 0           # no fixed seed (truly random)
python main.py --colors 4         # skip chromatic search, force k=4
python main.py --no-heuristics    # only run non-heuristic variants
python main.py --heuristics       # only run heuristic variants
python main.py --visualize        # save colored graph as PNG
```

Results are written to `output/` as a markdown file named after the run parameters (e.g. `both_5trials_seed42.md`).

## Dependencies

The core program has no required dependencies. The `--visualize` flag requires:

```
pip install -r requirements.txt
```

This installs `matplotlib` and `networkx`, used only for graph rendering.
