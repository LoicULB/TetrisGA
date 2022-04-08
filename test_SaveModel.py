import pandas as pd

from SaveModel import get_agent_dict, save_gen
from TetrisAgents import GeneticAgent

agent = GeneticAgent()
agent.weight_holes= 0.1
agent.weight_height = 0.2
agent.weight_bumpiness = 0.3
agent.weight_line_clear = 0.4
agent.weight_hollow_columns = 0.5
agent.weight_row_transition = 0.6
agent.weight_col_transition = 0.7
agent.weight_pit_count = 0.8
agent.weight_to_consider = [i for i in range(8)]


def test_get_agent_dict():
    dictionary = get_agent_dict(agent)
    data = {
        "weight_holes": 0.1,
        "weight_height": 0.2,
        "weight_bumpiness": 0.3,
        "weight_line_clear": 0.4,
        "weight_hollow_columns": 0.5,
        "weight_row_transition": 0.6,
        "weight_col_transition": 0.7,
        "weight_pit_count": 0.8,
        "weight_to_consider ": [i for i in range(8)]
    }
    assert dictionary == data

def test_save_gen():
    df_goal = pd.DataFrame(columns=["weight_holes",
        "weight_height",
        "weight_bumpiness",
        "weight_line_clear",
        "weight_hollow_columns",
        "weight_row_transition",
        "weight_col_transition",
        "weight_pit_count",
        "weight_to_consider "])
    def_actual = save_gen([agent], [i for i in range(8)])
    assert df_goal.columns.all(def_actual.columns)