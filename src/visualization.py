import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict

def plot_correlation_heatmap(correlation_matrix):
    plt.figure(figsize=(10,8))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap='coolwarm',
        vmin=-1,
        vmax=1,
        center=0
    )
    plt.title("Stock Price Correlations")
    plt.tight_layout()
    plt.show()

def plot_returns_distribution(returns_data):
    plt.figure(figsize=(12,6))
    for ticker in returns_data.columns:
        sns.kdeplot(data=returns_data[ticker].dropna(), label=ticker)
    plt.title("Distribution of Daily Returns")
    plt.xlabel("Daily Returns")
    plt.ylabel("Density")
    plt.legend()
    plt.show()