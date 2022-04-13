import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")


def plot():
    # Write the relative path from the name of this file
    relative_save_path = "fig2.png"

    save_path = os.path.join(father_path, relative_save_path)


    # plt.rcParams['text.usetex'] = True
    # matplotlib.rcParams.update({'font.size': 4})
    # sns.set_style('whitegrid')
    sns.set()
    fig, axs = plt.subplots(2, 3, figsize=(12,7))


    xs = [[100, 1000, 10000, 20000, 100000, 200000, 1000000, 2000000],
         [100, 1000, 10000, 20000, 100000, 200000],
         [100, 1000, 10000, 20000, 100000, 200000],
         [100, 1000, 10000, 20000, 100000, 200000, 1000000, 2000000],
         [100, 1000, 10000, 20000, 100000, 200000],
         [100, 1000, 10000, 20000, 100000, 200000],
         ]
    means = [np.array([50.00, 75.93, 81.27, 82.69, 84.38, 84.68, 85.28, 85.22]),
              np.array([7.71, 8.22, 10.90, 24.40, 30.33, 31.71]),
              np.array([50.71, 50.52, 65.29, 68.21, 70.28, 69.81]),
              np.array([50.74, 80.73, 83.98, 84.70, 86.71, 88.33, 89.30, 90.02]),  # sst-2
              np.array([5.69, 5.70, 6.10, 7.56, 9.83, 9.78]),
              np.array([47.29, 58.12, 59.81, 58.96, 59.69, 60.05]),
              ]
    stds = [np.array([0.0000,1.9486,0.3113,1.4269,0.4080,0.0000,0.1852,0.1308]),
              np.array([0.5077,0.5273,0.7694,2.5424,0.3309,0.1607]),
              np.array([0.2994,0.0173,1.3481,1.0254,0.2991,1.2152]),
              np.array([0.3060, 0.3450, 1.6390, 0.2524, 0.1480, 1.1677, 0.5853, 0.2350]),  # sst-2
              np.array([0.2155,0.3190,0.5032,1.3134,0.2815,0.2040]),
              np.array([0.0000,1.5784,0.2050,1.6657,0.9007,0.2078]),
              ]
    sls = [(25000, 87.24),(87000, 84.67),(100000, 88.05),(6900, 89.68),(30000, 29.85),(2500, 58.12)]
    promptings = [80.64,13.32,60.6,89.22,6.3,57.04]
    y_labels = [r'{Acc.}',r'{F$_1$.}',r'{Acc.}',r'{Acc.}',r'{F$_1$.}',r'{Acc.}']
    x_labels = [r'{Scale of Pseudo Dataset} $|\mathcal{D}^g|$']*6
    titles = [r'\textbf{IMDb}', r'\textbf{SQuAD}', r'\textbf{QNLI}', r'\textbf{SST-2}', r'\textbf{AdversarialQA}', r'\textbf{RTE}']

    for i in range(2):
        for j in range(3):
            idx = i*3+j

            axs[i,j].plot(*sls[idx], 'g^', label=r'\textsc{Supervised}', markersize=10)
            axs[i,j].plot(xs[idx], [promptings[idx]] * len(xs[idx]), 'r--', label=r'\textsc{Prompting}', markersize=10)
            axs[i,j].plot(xs[idx], means[idx], 'b-', label=r'\textsc{ZeroGen}', marker='*', markersize=10)
            axs[i,j].fill_between(xs[idx], means[idx] - stds[idx], means[idx] + stds[idx], color='b', alpha=0.2)
            axs[i,j].set_xticks(xs[idx])
            axs[i, j].set_xticklabels(xs[idx])
            axs[i, j].set_xscale('log')
            axs[i,j].set_xlabel(x_labels[idx])
            axs[i, j].set_title(titles[idx])
            axs[i,j].set_ylabel(y_labels[idx])
            axs[i,j].legend()
    plt.tight_layout()
    plt.show()

    fig.savefig(save_path)

    return relative_save_path