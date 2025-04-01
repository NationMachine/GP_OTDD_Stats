import pandas as pd
import numpy as np
import scipy
import scipy.io
import re
import glob
import os

import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.pylab import rcParams
from sklearn.manifold import TSNE
from sklearn import preprocessing


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

color_grama = ['darkgreen', 'darkblue', 'crimson', 'purple', 'darkorange', 'black', 'gold']
rcParams["figure.dpi"] = 300
rcParams['figure.figsize'] = 10,5
rcParams["figure.autolayout"] = True
rcParams["figure.constrained_layout.use"] = True
plt.rcParams.update({'font.size': 15})
    
plt.rc('axes', labelsize = 15)
plt.rc('axes', titlesize = 15)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

nombre = 'Global_problems'    
folder = os.getcwd() +'\\'+ nombre
    
isdir = os.path.isdir(folder)
if isdir== False:  
    problema_folder = os.mkdir(folder)
    
problema_folder = folder

csv_df = pd.read_csv(archivos_en_directorio_csv[0])

t = csv_df['nodos']*0.25

plt.xlabel('OTDD ')
plt.ylabel('M3GP Features')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['num rasgos m3gp'], hue = csv_df['tipo'], s = t, alpha = 0.7, palette=color_grama[0:2])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'global_O_vs_MF.pdf')
plt.savefig(problema_folder + '/'+ 'global_O_vs_MF.png')
plt.show()
plt.clf()

plt.xlabel('OTDD ')
plt.ylabel('Test Δerror%')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['error_test'], hue = csv_df['tipo'], s = t, alpha = 0.7, palette=color_grama[0:2])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'global_O_vs_Te.pdf')
plt.savefig(problema_folder + '/'+ 'global_O_vs_Te.png')
plt.show()
plt.clf()

plt.xlabel('OTDD ')
plt.ylabel('Train Δerror%')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['error_train'], hue = csv_df['tipo'], s = t, alpha = 0.7, palette=color_grama[0:2])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'global_O_vs_Tr.pdf')
plt.savefig(problema_folder + '/'+ 'global_O_vs_Tr.png')
plt.show()
plt.clf()

plt.xlabel('M3GP Features ')
plt.ylabel('Test Δerror%')
sns.scatterplot(x = csv_df['num rasgos m3gp'], y = csv_df['error_test'], hue = csv_df['tipo'], s = t, alpha = 0.7, palette=color_grama[0:2])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'global_Mf_vs_Te.pdf')
plt.savefig(problema_folder + '/'+ 'global_Mf_vs_Te.png')
plt.show()
plt.clf()

plt.xlabel('M3GP Features ')
plt.ylabel('Train Δerror%')
sns.scatterplot(x = csv_df['num rasgos m3gp'], y = csv_df['error_train'], hue = csv_df['tipo'], s = t, alpha = 0.7, palette=color_grama[0:2])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'global_Mf_vs_Tr.pdf')
plt.savefig(problema_folder + '/'+ 'global_Mf_vs_Tr.png')
plt.show()
plt.clf()

plt.xlabel('OTDD')
plt.ylabel('Δ features')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['dif rasgos'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama[0:2])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'Clas_problem_O_vs_DF.pdf')
plt.savefig(problema_folder + '/'+ 'Clas_problem_O_vs_DF.png')
plt.show()
plt.clf()
