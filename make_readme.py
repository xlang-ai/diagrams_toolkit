import os
import importlib

URL = "https://github.com/HKUNLP/diagrams_toolkit"
README_STR = """# diagrams_toolkit
 Source code for diagrams in the paper of HKU NLPers."""

PAPERS_DIR = './papers'

all_plots = []

for paper_dir in os.listdir(PAPERS_DIR):
    # each dir is a paper,a nd this function will
    if os.path.isfile(paper_dir):
        # skip the README.md and other non-dir-format items
        continue
    for plot_dir in os.listdir(os.path.join(PAPERS_DIR, paper_dir)):
        if plot_dir.endswith(".py"):
            # For python, call plot function and get the fig/table path.
            figure_path = importlib.import_module("papers.{}.{}".format(paper_dir, plot_dir.split('.')[0])).plot()
            all_plots.append({"figure_path": "{}/blob/main/papers/{}/{}".format(URL, paper_dir, figure_path),
                              "code_path": "{}/blob/main/papers/{}/{}".format(URL, paper_dir, plot_dir),
                              "paper": paper_dir})
        elif plot_dir.endswith(".tex"):
            # TODO: For tex, compile it and get the fig/table path.
            pass
        else:
            pass

HEADER = "| Figure | Code Source | Paper |\n|  ----  | ----  | ----  |"
ROWS = []
for plot_info in all_plots:
    ROWS.append(
        """| <a href="{}">  <img src="{}"  width="340" /></a> | [code]({}) | {} |""".format(plot_info['figure_path'],
                                                                                            plot_info['figure_path'],
                                                                                            plot_info['code_path'],
                                                                                            plot_info['paper']))

print("{}\n\n{}\n{}".format(README_STR, HEADER, '\n'.join(ROWS)))
