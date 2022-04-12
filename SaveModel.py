from typing import List

import Tetris
from TetrisAgents import GeneticAgent
import pandas as pd

def get_agent_dict(agent : GeneticAgent):
    """
    Get the dict of the agent's weight
    """
    data = {
        "weight_holes" : agent.weight_holes,
        "weight_height" : agent.weight_height,
        "weight_bumpiness" : agent.weight_bumpiness,
        "weight_line_clear" : agent.weight_line_clear,
        "weight_hollow_columns" : agent.weight_hollow_columns,
        "weight_row_transition" : agent.weight_row_transition,
        "weight_col_transition": agent.weight_col_transition,
        "weight_pit_count" : agent.weight_pit_count,
        "weight_to_consider " : agent.weight_to_consider
    }
    return data

def save_gen(agents_list : List[GeneticAgent], tetris_games : List[Tetris.Tetris], weight_to_consider : List[int]):
    """
    Save a generation of the tetris game into a csv file.
    """
    data=[]
    for agent_index in range(len(agents_list)):
        agent_dict = get_agent_dict(agents_list[agent_index])
        agent_dict["score"] = tetris_games[agent_index].score
        data.append(agent_dict)

    gen_df = pd.DataFrame(data)
    return gen_df