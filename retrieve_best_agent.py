import ast
import os

import pandas as pd
import re

from TetrisAgents import GeneticAgent, TrainedAgent

"""
Used to retrieve the best agent from a training directory (directory of csv for each generation)
"""


def retrieve_max_file(directory_path: str):
    """
    Retrieve the file corresponding to the data of the last generation of a training directory
    :param directory_path: the training directory path
    """
    list_files = os.listdir(directory_path)
    sorted_list = sorted(list_files)
    max_file = ""
    pattern = re.compile("model_gen_[0-9]+.csv")
    max_nb_gen = 0
    for file in list_files:
        if pattern.match(file):

            nb_gen = int(re.search(r'\d+', file).group())
            if nb_gen > max_nb_gen:
                max_nb_gen = nb_gen
    if max_nb_gen == 0:
        raise "No valid file in this directory, must be regex : 'model_gen_\number.csv'"

    return f"./{directory_path}/model_gen_{max_nb_gen}.csv"


def retrieve_best_agent(directory_path: str):
    """
    Return the best agent from the last generation of a training directory
    :param directory_path: the training directory
    """
    max_file = retrieve_max_file(directory_path)
    df = pd.read_csv(max_file)
    row_max_score = df["score"].argmax()
    agent_info = list(df.iloc[row_max_score,])

    ast_lit = ast.literal_eval(agent_info[8])
    return TrainedAgent(agent_info[0:8], ast_lit)
