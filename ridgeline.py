import pandas as pd
from joypy import joyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

infile = sys.argv[1]
df = pd.read_csv(f"{infile}")
column1 = sys.argv[2]
label =sys.argv[3]
column2 = sys.argv[4]
label1 = sys.argv[5]
outfile = sys.argv[6]
with PdfPages(outfile) as export_pdf:
# print(df.info())
 df[f'{column1}'] = df[f'{column1}'].astype(str)
 joyplot(df, by = f'{label}', column = f'{column2}')
 plt.xlabel(f"{label1}")
 export_pdf.savefig()
