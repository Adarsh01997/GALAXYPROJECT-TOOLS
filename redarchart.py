import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from matplotlib.backends.backend_pdf import PdfPages
infile = sys.argv[1]
column1 = sys.argv[2]
column2=sys.argv[3]
column3=sys.argv[4]
column4=sys.argv[5]
label = sys.argv[6]
label1 = sys.argv[7]
outfile = sys.argv[8]
df_pw = pd.read_csv(infile)
# Remove rows where the password is missing
df_pw = df_pw.dropna(subset=[column1])

def to_seconds(column2, column3):
    if column3 == "seconds":
        return column2
    elif column3 == "minutes":
        return column2 * 60
    elif column3 == "hours":
        return column2 * 60 * 60
    elif column3 == "days":
        return column2 * 60 * 27
    elif column3 == "weeks":
        return column2 * 60 * 24 * 7
    elif column3 == "months":
        return column2 * 60 * 24 * 30
    elif column3 == "years":
        return column2 * 60 * 24 * 365
    else:
        return np.nan
TIMES = [
    to_seconds(row[f"{column2}"], row[f"{column3}"])
    for _, row in df_pw.iterrows()
]

TIME_MAX = np.max(TIMES)
TIME_MIN = np.min(TIMES)

with PdfPages(outfile) as export_pdf:
# 'low' and 'high' refer to the final dot size.
 def scale_to_interval(x, low=1, high=60):
    return ((x - TIME_MIN) / (TIME_MAX - TIME_MIN)) * (high - low) + low
    # Different sades of grey used in the plot
 GREY88 = "#e0e0e0"
 GREY85 = "#d9d9d9"
 GREY82 = "#d1d1d1"
 GREY79 = "#c9c9c9"
 GREY97 = "#f7f7f7"
 GREY60 = "#999999"

# Values for the x axis
 ANGLES = np.linspace(0, 2 * np.pi, len(TIMES), endpoint=False)

# Heights of the lines and y-position of the dot are given by the times.
 HEIGHTS = np.array(TIMES)

# Category values for the colors
 CATEGORY_CODES = pd.Categorical(df_pw[f"{column4}"]).codes

# Colormap taken from https://carto.com/carto-colors/
 COLORMAP = ["#5F4690", "#1D6996", "#38A6A5", "#0F8554", "#73AF48", 
            "#EDAD08", "#E17C05", "#CC503E", "#94346E", "#666666"]

# Select colors for each password according to its category.
 COLORS = np.array(COLORMAP)[CATEGORY_CODES]


# This is going to be helpful to create some space for labels within the circle 
# Don't worry if it doesn't make much sense yet, you're going to see it in action below
 PLUS = 1000
# Create a data frame with the information for the four passwords that are going to be labeled
 LABELS_DF = df_pw[df_pw[f"{column2}"] > 90].reset_index()
# Create labels
 LABELS_DF["label"] = [
    f"{pswrd}\nRank: {int(rank)}" 
    for pswrd, rank in zip(LABELS_DF[f"{label}"], LABELS_DF[f"{label1}"])
 ]

# Set positions for the labels
 LABELS_DF["x"] = [40, 332, 401, 496]
 LABELS_DF["y"] = [160000000, 90000000, 45000000, 48498112]
# Initialize layout in polar coordinates
 fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})

# Set background color to white, both axis and figure.
 fig.patch.set_facecolor("white")
 ax.set_facecolor("white")

# Use logarithmic scale for the radial axis
 ax.set_rscale('symlog')

# Angular axis starts at 90 degrees, not at 0
 ax.set_theta_offset(np.pi / 2)

# Reverse the direction to go counter-clockwise.
 ax.set_theta_direction(-1)

# Add lines
 ax.vlines(ANGLES, 0 + PLUS, HEIGHTS + PLUS, color=COLORS, lw=0.9)

# Add dots
 ax.scatter(ANGLES, HEIGHTS + PLUS, s=scale_to_interval(HEIGHTS), color=COLORS);
 export_pdf.savefig()