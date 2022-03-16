import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")


def plot():
    # Write the relative path from the name of this file
    relative_save_path = "example.pdf"


    save_path = os.path.join(father_path, relative_save_path)

    fig = plt.figure(figsize=(6, .65))
    # ax = plt.subplot(111, frameon=False, aspect=.1)
    b = 0.025
    ax = fig.add_axes([b, 10 * b, 1 - 2 * b, 1 - 10 * b], frameon=False, aspect=0.05)

    cmap = plt.get_cmap("Oranges")
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, cax=ax, ticks=np.linspace(0, 1, 11),
                 orientation="horizontal")

    plt.savefig(save_path)

    return relative_save_path
