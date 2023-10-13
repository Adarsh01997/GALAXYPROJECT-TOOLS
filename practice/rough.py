# import pandas as pd
# import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import matplotlib.pyplot as plt
import csv
infile = sys.argv[1]
label = sys.argv[2]
xaxis = sys.argv[3]
yaxis = sys.argv[4]
outfile = sys.argv[5]

x = []
y = []
  
with open(str(infile),'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    
      
    for row in plots:
        
        x.append(row[0])
        y.append(int(row[1]))
with PdfPages(outfile) as export_pdf:
    plt.bar(x, y, color = 'g', width = 0.72, label = f"{label}")
    plt.xlabel(f'{xaxis}')
    plt.ylabel(f'{yaxis}')
    
    plt.legend()
    export_pdf.savefig()























# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True



# headers = ['Name', 'Age', 'Marks']

# df = pd.read_csv(infile, names=headers)


# df.set_index('Name').plot()
# with PdfPages(f'{outfile}.pdf') as pdf:
#     pdf.savefig()







# import matplotlib.pyplot as plt
# 
# import import pandas as pd
# xaxis=input("")
# yaxis=input("")


# with PdfPages(r'ram.pdf') as export_pdf:
# # Plot lines and/or markers to the Axes.
#  plt.plot(X, Y)
# # Set the x axis label of the current axis.

# # Set the y axis label of the current axis.
#  plt.ylabel(yaxis)
# # Set a title 
 
# # Display the figure.
#  export_pdf.savefig()
