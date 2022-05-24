import pandas as pd
import matplotlib.pyplot as plt
from os.path import isfile

def plot_training(path, nb_gen, heuristics):
    highest_score_run = []
    for i in range(1, nb_gen+1):
        file_name = path + f"/model_gen_{i}.csv"
        if isfile(file_name):
            df = pd.read_csv(file_name)
            highest_score_run.append(df["score"].max())

    if len(highest_score_run) != 0:
        plt.xlabel("Generation")
        plt.xticks(range(1,nb_gen+1)) #todo: see if we actually start at 1 => no
        plt.ylabel("Highest score")
        plt.title(f"Using {heuristics}")
        plt.suptitle("Evolution highest score over generations")
        plt.plot(range(1,len(highest_score_run)+1,1), highest_score_run)
        plt.savefig(path + "/graph.jpg")
        plt.show()