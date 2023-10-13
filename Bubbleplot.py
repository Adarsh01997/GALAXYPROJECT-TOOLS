from pylab import *
from scipy import *
import sys 

infile = sys.argv[1]
Xlabel = sys.argv[2]
Ylabel = sys.argv[3]
outfile = sys.argv[4]
rdata = genfromtxt(infile,dtype='S8,f,f,f,f,f,f,f,i',delimiter=',')

rdata[0] = zeros(8) # cutting the label's titles
rdata[1] = zeros(8) # cutting the global statistics

x = []
y = []
color = []
area = []
with PdfPages(outfile) as export_pdf:
      for data in rdata:
             x.append(data[1]) # murder
             y.append(data[5]) # burglary
             color.append(data[6]) # larceny_theft 
             area.append(sqrt(data[8])) # population
 # plotting the first eigth letters of the state's name
             text(data[1], data[5], 
             data[0],size=11,horizontalalignment='center')

# making the scatter plot
             sct = scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w')
             sct.set_alpha(0.75)

             axis([0,11,200,1280])
             xlabel(str(Xlabel))
             ylabel(str(Ylabel))
             export_pdf.savefig()
