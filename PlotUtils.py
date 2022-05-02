import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join



def plot_training(path, nb_gen, heuristics):
    highest_score_run = []
    for i in range(1, nb_gen+1):
        file_name = path + f"/model_gen_{i}.csv"
        df = pd.read_csv(file_name)
        highest_score_run.append(df["score"].max())

    plt.xlabel("Generation")
    plt.xticks([i for i in range(1,nb_gen+1)])
    plt.ylabel("Highest score")
    plt.title(f"Using {heuristics}")
    plt.suptitle("Evolution highest score over generations")
    plt.plot(highest_score_run)
    plt.show()