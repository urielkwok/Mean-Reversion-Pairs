import matplotlib.pyplot as plt
import pandas as pd


def plot_z_values(z_values: pd.Series) -> None:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Plot of z-values vs time
    """
    plt.figure(figsize=(8,5))
    plt.plot(z_values)
    plt.xlabel("Time")
    plt.ylabel("Z-Values")
    plt.title("Z-Values vs Time")
    plt.savefig("z_values.png")
