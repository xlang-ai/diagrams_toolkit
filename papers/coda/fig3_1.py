import matplotlib.pyplot as plt
import torch
import os
import seaborn as sns

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")


def plot():
    # Write the relative path from the name of this file
    relative_save_path = "fig3_1.png"

    save_path = os.path.join(father_path, relative_save_path)

    sns.set_style("darkgrid")
    column = [4, 8, 16, 32]
    base = [34.53, 34.35, 33.91, 33.17]
    coda = [35.65, 35.74, 35.84, 35.96]
    csfont = {'fontsize': 15, 'fontname': 'Times New Roman'}
    plt.figure(1)
    plt.plot(column, base, marker="o", label='Base')
    plt.plot(column, coda, color='tomato', marker='s', label='CODA')
    plt.xticks(column, fontsize=csfont['fontsize'])
    plt.yticks(fontsize=csfont['fontsize'])
    plt.xlabel("Number of heads", **csfont)
    plt.ylabel("BLEU", **csfont)
    plt.legend(fontsize=csfont['fontsize'])
    plt.savefig(save_path, format='png', bbox_inches='tight', pad_inches=0)

    return relative_save_path
