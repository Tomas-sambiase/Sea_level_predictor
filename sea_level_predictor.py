import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")
    plt.title("Rise in Sea Level")

    # Create line of best fit using all data
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
   
    #plt.plot([min(df["Year"]), future_year], [intercept_all, future_sea_level_all], color='red', linestyle='--', label='All Data Best Fit')
    min_valor = min(df["Year"])
    años = list(range(min_valor , 2051))

    plt.plot(años,[slope_all * x + intercept_all for x in años], color = "red", label = "Regression")
    
    # Create line of best fit using data since 2000
    df_from_2000 = df[df["Year"] >= 2000]
    slope_since_2000, intercept_since_2000, _, _, _ = linregress(df_from_2000["Year"], df_from_2000["CSIRO Adjusted Sea Level"])
    años_2 = list(range(2000,2051))
    plt.plot(años_2, [slope_since_2000 * x + intercept_since_2000 for x in años_2], color = "blue", label = "Regression 2")
    # Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Show plot
    plt.show()

    resultado1 = slope_all * 2050 + intercept_all
    resultado2 = slope_since_2000 * 2050 + intercept_since_2000
    print(resultado1,resultado2)

    # Save plot
    plt.savefig('sea_level_plot.png')

    return plt.gca()

draw_plot()
