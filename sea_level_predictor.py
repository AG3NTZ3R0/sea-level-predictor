import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')
    df = df.rename(columns={'Year':'year', 'CSIRO Adjusted Sea Level':'csiro_sea_lvl'})

    # Create scatter plot
    plt.figure(1, figsize=(16, 9))
    plt.scatter(df['year'], df['csiro_sea_lvl'])

    # Create first line of best fit
    regress = linregress(df['year'], df['csiro_sea_lvl'])

    # Expand dataframe for future predictions
    last_year = df['year'].max()
    df = df.append([{'year': y} for y in range(last_year + 1, 2051)])
    plt.plot(df['year'], regress.intercept + regress.slope * df['year'], c='r', label='fit all')

    # Create second line of best fit
    df_recent = df.loc[(df['year'] >= 2000) & (df['year'] <= last_year)]
    regress2 = linregress(df_recent['year'], df_recent['csiro_sea_lvl'])
    df_recent = df_recent.append([{'year': y} for y in range(last_year + 1, 2051)])
    plt.plot(df_recent['year'], regress2.intercept + regress2.slope * df_recent['year'], c='b', label='fit recent')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()