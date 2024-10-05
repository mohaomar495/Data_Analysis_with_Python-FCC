import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data
df = pd.read_csv("medical_examination.csv")

# 2 Add an overweight column to the data.
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = np.where(df["overweight"] > 25, 1, 0)

# 3 Normalize data (gluc, cholesterol)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)


# 4 Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot
    df_cat = pd.melt(df, id_vars = "cardio", value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # 6 Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable", "value"])["value"].count().to_frame()
    

    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : sns.catplot()
    df_cat.rename(columns = {"value":"total"}, inplace = True)
    df_cat.reset_index(inplace = True)



    # 8 create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : sns.catplot()
    fig = sns.catplot(df_cat, x = "variable", y = "total", hue = "value", col = "cardio", kind = "bar").fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10 Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 11 Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12 Calculate the correlation matrix and store it in the corr variable
    corr = df_heat.corr().round(1)

    # 13 Generate a mask for the upper triangle and store it in the mask variable
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # 14 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 8))

    # 15 Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap()
    heatmap = sns.heatmap(corr, annot = True, mask = mask, fmt="0.1f", square = True, vmin = 0, vmax = 1)
    heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation = 0)
    heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation = 90)

    # 16 save the into a .png file.
    fig.savefig('heatmap.png')
    return fig
