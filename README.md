# Sawit 4KB Chess Engine — v5

Entry for the [make.fun](https://make.fun) `tiny-chess-01` competition: a complete
chess engine in a single `main.py` of **3,395 bytes** (Python 3.13 stdlib only,
4,096-byte limit).

`v5-source.py` is the readable source; `main.py` is the kit-packed entrypoint.

## Design

- 0x88 board, Michniewski piece-square tables (single phase)
- Alpha-beta + transposition table (131,072 entries)
- Null-move pruning (R=2), quiescence with delta pruning (margin 200)
- 2 killer moves per ply, PVS, history heuristic
- Node limit 110,000; resigns when the root score drops below −1500

## Results (local trials, fresh kit)

| Trial | Elo | Score |
|---|---|---|
| trial-0 (grading draw) | 1,451 | 2W / 4D / 0L |
| trial-1 | 1,654 | 4W / 2D / 0L |
| 8-game | 1,464 | 2W / 5D / 1L |

Practice grade on make.fun: **PASS — 1,451 ≥ floor 1,154, in the final.**

## License

MIT
