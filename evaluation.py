import argparse
from pathlib import Path
import sys

import pandas as pd

from TetrisSolo import TetrisSolo
from retrieve_best_agent import retrieve_best_agent

"""
File used to evaluate the agent
"""

def main():
    parser = argparse.ArgumentParser(description="The Tetris game")
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help="Path of saved generation on which to evaluate the best agent",
        default="./SavedModel/training_tt5217_t800_all", # TODO replace by our best trained agent
    )
    parser.add_argument(
        "-t",
        '--tetrominoes_limit',
        type=int,
        help="The maximum number of tetrominoes after which the evaluation stops",
        default=500
    )

    args = parser.parse_args()
    if not Path(args.directory).is_dir():
        parser.print_help()
        print()
        print(f"Invalid path for generation file: {args.directory}")
        sys.exit()

    agent = retrieve_best_agent(args.directory)
    agent.weight_holes = agent.weight_array[0]
    agent.weight_height = agent.weight_array[1]
    agent.weight_bumpiness = agent.weight_array[2]
    agent.weight_line_clear = agent.weight_array[3]
    agent.weight_hollow_columns = agent.weight_array[4]
    agent.weight_row_transition = agent.weight_array[5]
    agent.weight_col_transition = agent.weight_array[6]
    agent.weight_pit_count = agent.weight_array[7]
    scores = []

    game = TetrisSolo(args.tetrominoes_limit, agent.weight_to_consider, agent)

    game.launch()
    scores.append(game.tetris_game.score)

if __name__ == '__main__':
    main()