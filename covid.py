import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
import sys
from matplotlib.backends.backend_pdf import PdfPages

date = str(sys.argv[1])
outfile=(sys.argv[2])
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+date+'.csv'
df = pd.read_csv(path)
df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
df.rename(columns={'Country_Region': "Country"}, inplace=True)
world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
with PdfPages(outfile) as export_pdf:
    plt.figure(figsize=(12,10))
    plot = sns.barplot(top_20['Confirmed'], top_20['Country'])
    for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
        plot.text(value,i-0.05,f'{value:,.0f}',size=10)
    export_pdf.savefig()
    
    plt.figure(figsize=(12,10))
    plot = sns.barplot(top_20['Deaths'], top_20['Country'])
    for i,(value,name) in enumerate(zip(top_20['Deaths'],top_20['Country'])):
        plot.text(value,i-0.05,f'{value:,.0f}',size=10)
    export_pdf.savefig()
    

