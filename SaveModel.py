from typing import List

import Tetris
from TetrisAgents import GeneticAgent
import pandas as pd

"""
Save the information of a generation into a csv file
"""

def get_agent_dict(agent : GeneticAgent):
    """
    Get the dict of the agent's weight
    """
    data = {
        "weight_holes" : round(agent.weight_array[0], 3),
        "weight_height" : round(agent.weight_array[1],3),
        "weight_bumpiness" : round(agent.weight_array[2],3),
        "weight_line_clear" : round(agent.weight_array[3],3),
        "weight_hollow_columns" : round(agent.weight_array[4], 3),
        "weight_row_transition" : round(agent.weight_array[5],3),
        "weight_col_transition": round(agent.weight_array[6],3),
        "weight_pit_count" : round(agent.weight_array[7],3),
        "weight_to_consider " : agent.weight_to_consider,
    }
    return data

def save_gen(agents_list : List[GeneticAgent], tetris_games : List[Tetris.Tetris]):
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