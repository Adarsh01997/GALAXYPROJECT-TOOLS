from matplotlib.backends.backend_pdf import PdfPages
import sys
import matplotlib.pyplot as plt
import csv

infile = sys.argv[1]
Title = sys.argv[2]
outfile = sys.argv[3]
Subjects = []
Scores = []
  
with open(str(infile), 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        Subjects.append(row[0])
        Scores.append(int(row[1]))
        
with PdfPages(outfile) as export_pdf:
 plt.pie(Scores,labels = Subjects,autopct = '%.2f%%')
 plt.title(f'{Title}', fontsize = 20)
 export_pdf.savefig()

