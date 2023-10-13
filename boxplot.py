import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys 
infile = sys.argv[1]
replace= sys.argv[2]
xaxis = sys.argv[3]
yaxis = sys.argv[4]
outfile = sys.argv[5]

s = str(xaxis)
g = str(yaxis)
df = pd.read_csv(f'{infile}')
mode = df[f'{replace}'].mode().values[0]
df[f'{replace}']= df[f'{replace}'].replace(np.nan, mode)

df.isnull().sum()
with PdfPages(outfile) as export_pdf:
    df = df.dropna(axis = 0, how ='any')
    sns.set(rc={'figure.figsize':(17,10)})
    sns.boxplot( x=f'{s}' , y=f'{g}', data=df, )
    export_pdf.savefig()

