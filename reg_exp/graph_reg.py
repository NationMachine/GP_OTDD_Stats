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
from sklearn import preprocessing as pre

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# ---------------Regresion------------------

archivos_en_directorio_mat = glob.glob(os.getcwd() + "//reg_mats//*.mat")
archivos_en_directorio_csv = glob.glob(os.getcwd() + "//*.csv")
archivos_en_directorio_mat.sort(key=natural_keys)
archivos_en_directorio_csv.sort(key=natural_keys)

# ------------------------------------------

csv_df = pd.read_csv(archivos_en_directorio_csv[1])

csv_df = csv_df[150:]
archivos_en_directorio_mat=archivos_en_directorio_mat[150:]

for p,c in enumerate(archivos_en_directorio_mat):
    tsne = TSNE(n_components = 2, random_state = 42, n_jobs=-1)
    
    mat_dict = scipy.io.loadmat(archivos_en_directorio_mat[p])
    
# --------------------------------------------------------    
    x_train_og = mat_dict['x_train_og'].astype(float)
    x_train_m3gp = mat_dict['x_train_m3gp'].astype(float)
    y_train = mat_dict['y_train'].astype(int)
    y_train = pre.MinMaxScaler().fit_transform(y_train)
    
    x_test_og = mat_dict['x_test_og'].astype(float)
    x_test_m3gp = mat_dict['x_test_m3gp'].astype(float)
    y_test = mat_dict['y_test'].astype(int)
    y_test = pre.MinMaxScaler().fit_transform(y_test)
    
    Reges = np.unique(y_train)
    num_Reges = np.unique(y_train).size
    
    nombre = csv_df["Problema"][p+150]
    base = csv_df['OG'][p+150]
    bases = csv_df['Problema'].unique()
    split = len(nombre)
    
# --------------------------------------------------------    
    x_train_og_tsne = tsne.fit_transform(x_train_og)
    x_train_m3gp_tsne = tsne.fit_transform(x_train_m3gp)
    
    x_test_og_tsne = tsne.fit_transform(x_test_og)
    x_test_m3gp_tsne = tsne.fit_transform(x_test_m3gp)
   
    df_train_og_tsne = np.hstack((x_train_og_tsne,y_train))
    df_train_m3gp_tsne = np.hstack((x_train_m3gp_tsne,y_train))
    
    df_test_og_tsne = np.hstack((x_test_og_tsne,y_test))
    df_test_m3gp_tsne = np.hstack((x_test_m3gp_tsne,y_test))
    
    df_train_og_tsne = pd.DataFrame(df_train_og_tsne, columns=['componente 1', 'componente 2', 'Reges'])
    df_train_m3gp_tsne = pd.DataFrame(df_train_m3gp_tsne, columns=['componente 1', 'componente 2', 'Reges'])
    
    df_test_og_tsne = pd.DataFrame(df_test_og_tsne, columns=['componente 1', 'componente 2', 'Reges'])
    df_test_m3gp_tsne = pd.DataFrame(df_test_m3gp_tsne, columns=['componente 1', 'componente 2', 'Reges'])

    Reges_color = ['Greens','Blues','Reds','Purples','Oranges','Greys']
    
    if nombre == bases[0]:
        palette = Reges_color[0]
    elif nombre == bases[1]:
        palette = Reges_color[1]
    elif nombre == bases[2]:
        palette = Reges_color[2]
    elif nombre == bases[3]:
        palette = Reges_color[3]
    elif nombre == bases[4]:
        palette = Reges_color[4]
    else: 
        palette = Reges_color[5]
    
    rcParams["figure.dpi"] = 300
    rcParams['figure.figsize'] = 10,5
    rcParams["figure.autolayout"] = True
    rcParams["figure.constrained_layout.use"] = False
    plt.rcParams.update({'font.size': 15})
    
    plt.rc('axes', labelsize = 25)
    plt.rc('axes', titlesize = 25)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    
    folder = os.getcwd() +'\\'+ nombre
    
    isdir = os.path.isdir(folder)
    
    if isdir== False:  
        problema_folder = os.mkdir(folder)
    problema_folder = folder
    
# --------------------------------------------------------    
    x = df_train_og_tsne['componente 1']
    y = df_train_og_tsne['componente 2']
    hue = df_train_og_tsne['Reges']
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    
    ax = sns.scatterplot(x = x, y = y, hue = hue, palette = palette, alpha = 1)
    
    norm = plt.Normalize(hue.min(), hue.max())
    sm = plt.cm.ScalarMappable(cmap=palette, norm=norm)
    sm.set_array([])

    ax.get_legend().remove()

    plt.savefig(problema_folder + '/'+ (base +'_OG_Train.pdf'))
    plt.savefig(problema_folder + '/'+ (base +'_OG_Train.png'))
    plt.show()
    plt.clf()
    print(base +'_OG_Train')
    del x, y, hue,
    
    x = df_train_m3gp_tsne['componente 1']
    y = df_train_m3gp_tsne['componente 2']
    hue = df_train_m3gp_tsne['Reges']
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    
    ax = sns.scatterplot(x = x, y = y, hue = hue, palette = palette, alpha = 1)

    norm = plt.Normalize(hue.min(), hue.max())
    sm = plt.cm.ScalarMappable(cmap=palette, norm=norm)
    sm.set_array([])

    ax.get_legend().remove()
        
    plt.savefig(problema_folder + '/'+ (base +'_M3GP_Train.pdf'))
    plt.savefig(problema_folder + '/'+ (base +'_M3GP_Train.png'))
    plt.show()
    plt.clf()
    print((base +'_M3GP_Train'))
    
    x = df_test_og_tsne['componente 1']
    y = df_test_og_tsne['componente 2']
    hue = df_test_og_tsne['Reges']
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')

    ax = sns.scatterplot(x = x, y = y, hue = hue, palette = palette, alpha = 1)

    norm = plt.Normalize(hue.min(), hue.max())
    sm = plt.cm.ScalarMappable(cmap=palette, norm=norm)
    sm.set_array([])
    ax.get_legend().remove()

    plt.savefig(problema_folder + '/'+ (base +'_OG_Test.pdf'))
    plt.savefig(problema_folder + '/'+ (base +'_OG_Test.png'))
    plt.show()
    plt.clf()
    print(base +'_OG_Test')
    del x, y, hue,

    x = df_test_m3gp_tsne['componente 1']
    y = df_test_m3gp_tsne['componente 2']
    hue = df_test_m3gp_tsne['Reges']
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')

    ax = sns.scatterplot(x = x, y = y, hue = hue, palette = palette, alpha = 1)


    norm = plt.Normalize(hue.min(), hue.max())
    sm = plt.cm.ScalarMappable(cmap=palette, norm=norm)
    sm.set_array([])
    ax.get_legend().remove()

    
    plt.savefig(problema_folder + '/'+ (base +'_M3GP_Test.pdf'))
    plt.savefig(problema_folder + '/'+ (base +'_M3GP_Test.png'))
    plt.show()
    plt.clf()
    print((base +'_M3GP_Test'))
    
    del x, y, hue
    del df_train_m3gp_tsne, df_train_og_tsne, df_test_m3gp_tsne, df_test_og_tsne
    del x_train_og_tsne, x_train_m3gp_tsne, x_test_og_tsne, x_test_m3gp_tsne
color_grama = ['darkgreen', 'darkblue', 'crimson', 'purple', 'darkorange', 'black', 'gold']
color_grama = ['darkgreen', 'darkblue', 'crimson', 'purple', 'darkorange', 'black']
rcParams["figure.dpi"] = 300
rcParams['figure.figsize'] = 10,5
rcParams["figure.autolayout"] = True
rcParams["figure.constrained_layout.use"] = True
plt.rcParams.update({'font.size': 15})
    
plt.rc('axes', labelsize = 25)
plt.rc('axes', titlesize = 25)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

nombre = 'Reg_problems_size'    
folder = os.getcwd() +'\\'+ nombre
    
isdir = os.path.isdir(folder)
if isdir== False:  
    problema_folder = os.mkdir(folder)
    
problema_folder = folder

csv_df = pd.read_csv(archivos_en_directorio_csv[1])
t = csv_df['nodos']*0.25

plt.xlabel('OTDD ')
plt.ylabel('Train Δerror%')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['% ERROR train'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette = color_grama,legend=True)
plt.legend(bbox_to_anchor=(19, 19), loc=0, borderaxespad=0.,title='Problem')
plt.savefig(problema_folder + '/'+ 'Reg_problem_O_vs_TrE.pdf')
plt.show()
plt.clf()

plt.xlabel('OTDD ')
plt.ylabel('Test Δerror%')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['% ERROR test'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama,legend=False)
plt.savefig(problema_folder + '/'+ 'Reg_problem_O_vs_TeE.pdf')
plt.show()
plt.clf()


plt.xlabel('OTDD ')
plt.ylabel('M3GP Features')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['num rasgos m3gp'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama,legend=False)
plt.savefig(problema_folder + '/'+ 'Reg_problem_O_vs_MF.pdf')
plt.show()
plt.clf()


plt.xlabel('OTDD')
plt.ylabel('Δ features')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['dif rasgos'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama, legend=False)
plt.savefig(problema_folder + '/'+ 'Reg_problem_O_vs_DF.pdf')
plt.show()
plt.clf()


plt.xlabel('M3GP Features')
plt.ylabel('Train Δerror%')
sns.scatterplot(x = csv_df['num rasgos m3gp'], y = csv_df['% ERROR train'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama, legend=False)
plt.savefig(problema_folder + '/'+ 'Reg_problem_M_vs_TrE.pdf')
plt.show()
plt.clf()

plt.xlabel('M3GP Features')
plt.ylabel('Test Δerror%')
sns.scatterplot(x = csv_df['num rasgos m3gp'], y = csv_df['% ERROR test'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama, legend=False)
plt.savefig(problema_folder + '/'+ 'Reg_problem_M_vs_TeE.pdf')
plt.show()
plt.clf()

