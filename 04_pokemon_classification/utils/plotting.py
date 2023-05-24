import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def count_types(df, suptitle, plt_save_path):
    # Grouping the DataFrame by 'type' and getting the count of each type
    type_counts = df['type'].value_counts()

    # Specifying the colors for each type
    type_colors = {
        'bug': '#A6B91A',
        'dark': '#705746',
        'dragon': '#6F35FC',
        'electric': '#F7D02C',
        'fairy': '#D685AD',
        'fighting': '#C22E28',
        'fire': '#EE8130',
        'flying': '#A98FF3',
        'ghost': '#735797',
        'grass': '#7AC74C',
        'ground': '#E2BF65',
        'ice': '#96D9D6',
        'normal': '#A8A77A',
        'poison': '#A33EA1',
        'psychic': '#F95587',
        'rock': '#B6A136',
        'steel': '#B7B7CE',
        'water': '#6390F0'
    }

    # Creating the bar plot with specified colors
    plt.bar(type_counts.index, type_counts.values, color=[type_colors.get(t, 'gray') for t in type_counts.index])

    # Adding labels and title
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.title('Number of Pokémon per Type')
    plt.suptitle(suptitle)

    # Rotating x-axis labels for better readability
    plt.xticks(rotation=45)

    # Saving the plot
    plt.savefig(plt_save_path)

def plot_history(H, epochs, plt_save_path):
    plt.style.use("seaborn-colorblind")

    plt.figure(figsize=(12,6))
    plt.subplot(1,2,1)
    plt.plot(np.arange(0, epochs), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), H.history["val_loss"], label="val_loss", linestyle=":")
    plt.title("Loss curve")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.tight_layout()
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(np.arange(0, epochs), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, epochs), H.history["val_accuracy"], label="val_acc", linestyle=":")
    plt.title("Accuracy curve")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.tight_layout()
    plt.legend()
    plt.savefig(plt_save_path)

def plot_cm(y_test, y_pred, save_path, normalized:bool):
    """
    Plot confusion matrix
    """
    if normalized == False:
        cm = pd.crosstab(y_test, y_pred, 
                            rownames=['Actual'], colnames=['Predicted'])
        p = plt.figure(figsize=(10,10));
        p = sns.heatmap(cm, annot=True, fmt="d", cbar=False)
    elif normalized == True:
        cm = pd.crosstab(y_test, y_pred, 
                               rownames=['Actual'], colnames=['Predicted'], normalize='index')
        p = plt.figure(figsize=(10,10));
        p = sns.heatmap(cm, annot=True, fmt=".2f", cbar=False)

    # save plot
    plt.savefig(save_path)