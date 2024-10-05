import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = True, index_col = "date")

# Clean data
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]

# Draw line plot
def draw_line_plot():
    df_line = df.reset_index()
    fig = df_line.plot.line(x = "date", y = "value", color="red", figsize = (12, 9), linewidth= 0.90).figure
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_months = df.groupby([df.index.year.rename("year"), df.index.month.rename("month")]).mean()
    df_months = df_months.unstack()

    # Draw bar plot
    fig = df_months.plot.bar(figsize = (12, 12)).figure
    plt.legend([calendar.month_name[i] for i in range(1, 13)], title = "Months")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(12, 9))

    # Year-wise box plot
    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    ax[0].set(ylabel='Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])

    # Month-wise box plot
    months = pd.date_range('2020-01', '2020-12', freq='MS').strftime('%b').tolist()
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1], order=months)
    ax[1].set(ylabel='Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
