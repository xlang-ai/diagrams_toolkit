"""
@Author: Lin Zheng
@Editor: Tianbao Xie
"""
import matplotlib.pyplot as plt
import torch
import os
import seaborn as sns

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")


def plot():
    # Write the relative path from the name of this file
    relative_save_path = "fig2.png"

    save_path = os.path.join(father_path, relative_save_path)
    sns.set_style("darkgrid")
    """generate LM plots"""
    path = father_path
    sns.set(font_scale=7.)
    loaded_dict = torch.load(os.path.join(path, 'attn_head'))
    dec_js = loaded_dict['dec_js']
    cnt = loaded_dict['cnt']
    head_js = dec_js / cnt

    loaded_dict = torch.load(os.path.join(path, 'attn_base'))
    dec_js = loaded_dict['dec_js']
    cnt = loaded_dict['cnt']
    base_js = dec_js / cnt
    num_layer, num_head, _ = dec_js.shape

    figs, axes = plt.subplots(2, num_layer, figsize=(165, 21), sharex=True, sharey=True)

    vmax = 400

    def draw_js_heatmap(attn, title, ax=None):
        assert attn.dim() == 2
        if ax is not None:
            sns.heatmap(attn, cmap="YlGnBu", vmax=vmax, vmin=0, ax=ax, cbar=False, cbar_ax=None)
        else:
            ax = sns.heatmap(attn, cmap="YlGnBu", vmax=vmax, vmin=0)
        ax.set_title(title)

    cbar_ax = figs.add_axes([.91, .3, .005, .4])

    sns.heatmap(
        base_js[0],
        cmap="YlGnBu",
        vmax=vmax,
        vmin=0,
        ax=axes[0, 0],
        cbar_ax=cbar_ax,
    )
    axes[0, 0].set_title("Layer 0")

    for i, dec_js_i in enumerate(base_js[1:], start=1):
        draw_js_heatmap(dec_js_i, 'Layer {}'.format(i), ax=axes[0, i])
    for i, dec_js_i in enumerate(head_js):
        sns.heatmap(dec_js_i, cmap="YlGnBu", vmax=vmax, vmin=0, ax=axes[1, i], cbar=False, cbar_ax=None)

    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.clf()

    return relative_save_path
