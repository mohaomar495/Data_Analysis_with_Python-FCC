import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # Create first line of best fit
    line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    X1 = np.arange(df['Year'].min(), 2051, 1)
    Y1 = X1 * line1.slope + line1.intercept
    plt.plot(X1, Y1, label="Best fit line (All years)")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    line2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    X2 = np.arange(2000, 2051, 1)
    Y2 = X2 * line2.slope + line2.intercept
    plt.plot(X2, Y2, label="Best fit line (2000 onwards)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()