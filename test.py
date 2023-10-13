from matplotlib.backends.backend_pdf import PdfPages
import sys
import matplotlib.pyplot as plt
import csv
infile = sys.argv[1]
select = sys.argv[2]
color = sys.argv[3]
label = sys.argv[4]
xaxis = sys.argv[5]
yaxis = sys.argv[6]
outfile = sys.argv[7]

x = []
y = []
  
with open(str(infile),'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    
      
    for row in plots:
        
        x.append(row[0])
        y.append(int(row[1]))
with PdfPages(outfile) as export_pdf:
    if(select=='Bar' ):
      if(color =='r' or color=='g' or color =='b'):

       plt.bar(x, y, color = f'{color}', width = 0.72, label = f"{label}")
       plt.xlabel(f'{xaxis}')
       plt.ylabel(f'{yaxis}')
    
       plt.legend()
       export_pdf.savefig()
    elif(select=='scatter'):
      if(color =='r' or color=='g' or color =='b'):
       plt.scatter(x, y, color = f'{color}',s = 100,)      
       plt.xlabel(f'{xaxis}')
       plt.ylabel(f'{yaxis}')
       plt.title(f'{label}', fontsize = 10)
       export_pdf.savefig()
    
    elif(select=='line'):
      if(color =='r' or color=='g' or color =='b'):
       plt.plot(x, y, color = f'{color}', linestyle = 'dashed')
  
       
       plt.xlabel(f'{xaxis}')
       plt.ylabel(f'{yaxis}')
       plt.title(f'{label}', fontsize = 20)
       plt.grid()
       export_pdf.savefig()



    # elif(select=='piechart'):
    #     plt.pie(y,labels = x,autopct = '%.2f%%')
    #     plt.title(f'{label}', fontsize = 20)
    #     export_pdf.savefig()  
