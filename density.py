import pandas as pd
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_pdf import PdfPages
infile = sys.argv[1]
column1 = sys.argv[2]
column2 = sys.argv[3]
label= sys.argv[4]
outfile = sys.argv[5]

with PdfPages(outfile) as export_pdf: 
# creating a dataframe
 df = pd.read_csv(infile)
 df.head()
 data_wide = df.pivot(columns=f'{column1}',
                     values=f'{column2}')
 data_wide.head()
 data_wide.plot.density(figsize = (7, 7),
                       linewidth = 4)
  
 plt.xlabel(f"{label}")
 export_pdf.savefig()