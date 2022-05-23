import argparse
from pathlib import Path
import sys

from TetrisSolo import TetrisSolo
from retrieve_best_agent import retrieve_best_agent


def main():
    parser = argparse.ArgumentParser(description="The Tetris game")
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help="Path of saved generation on which to evaluate the best agent",
        default="./SavedModel/ultimate", # TODO replace by our best trained agent
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
    game = TetrisSolo(args.tetrominoes_limit, agent.weight_to_consider, agent)
    game.launch()


if __name__ == '__main__':
    main()