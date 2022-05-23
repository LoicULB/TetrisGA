from typing import List

import Tetris
from TetrisAgents import GeneticAgent
import pandas as pd

def get_agent_dict(agent : GeneticAgent):
    """
    Get the dict of the agent's weight
    """
    data = {
        "weight_holes" : round(agent.weight_holes, 3),
        "weight_height" : round(agent.weight_height,3),
        "weight_bumpiness" : round(agent.weight_bumpiness,3),
        "weight_line_clear" : round(agent.weight_line_clear,3),
        "weight_hollow_columns" : round(agent.weight_hollow_columns, 3),
        "weight_row_transition" : round(agent.weight_row_transition,3),
        "weight_col_transition": round(agent.weight_col_transition,3),
        "weight_pit_count" : round(agent.weight_pit_count,3),
        "weight_to_consider " : agent.weight_to_consider,
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