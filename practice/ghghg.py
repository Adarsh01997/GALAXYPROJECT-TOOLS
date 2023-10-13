from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import matplotlib.pyplot as plt
import csv

infile = sys.argv[1]
label = sys.argv[2]
xaxis = sys.argv[3]
yaxis = sys.argv[4]
outfile = sys.argv[5]

Names = []
Values = []

def f(x):

  
      with open(str(infile),'r') as csvfile:
       lines = csv.reader(csvfile, delimiter = ',')
    
      for row in lines:
        Names.append(row[0])
        Values.append(int(row[1]))
        with PdfPages(outfile) as export_pdf:
  
         plt.scatter(Names, Values, color = 'g',s = 100,)
         plt.xticks(rotation = 25)
         plt.xlabel(f'{xaxis}')
         plt.ylabel(f'{yaxis}')
         plt.title(f'{label}', fontsize = 20)
         plt.show()
         export_pdf.savefig()
        
   
 
    