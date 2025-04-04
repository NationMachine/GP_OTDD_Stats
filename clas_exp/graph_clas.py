import pandas as pd
import numpy as np
import scipy
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

# ---------------Clasificacion------------------
archivos_en_directorio_mat = glob.glob(os.getcwd() + "//mats_clas_python//*.mat")
archivos_en_directorio_csv = glob.glob(os.getcwd() + "//*.csv")
archivos_en_directorio_mat.sort(key=natural_keys)
archivos_en_directorio_csv.sort(key=natural_keys)

#------------------------------------------

for p,c in enumerate(archivos_en_directorio_mat):
    tsne = TSNE(n_components = 2, random_state = 42, n_jobs=-1)
    csv_df = pd.read_csv(archivos_en_directorio_csv[0])
    mat_dict = scipy.io.loadmat(archivos_en_directorio_mat[p])
    
#--------------------------------------------------------    
    x_train_og = mat_dict['x_train_og'].astype(float)
    x_train_m3gp = mat_dict['x_train_m3gp'].astype(float)
    y_train = mat_dict['y_train'].astype(int)
    y_train_txt = np.char.add('Class ', mat_dict['y_train'].astype(str))
    
    x_test_og = mat_dict['x_test_og'].astype(float)
    x_test_m3gp = mat_dict['x_test_m3gp'].astype(float)
    y_test = mat_dict['y_test'].astype(int)
    y_test_txt = np.char.add('Class ', mat_dict['y_test'].astype(str))
    
    clases = np.unique(y_train)
    num_clases = np.unique(y_train).size
    
    nombre = csv_df["Problema"][p]
    base = csv_df['OG'][p]
    
#--------------------------------------------------------    
    x_train_og = preprocessing.normalize(x_train_og)
    x_train_m3gp = preprocessing.normalize(x_train_m3gp)
    
    
    x_train_og_tsne = tsne.fit_transform(x_train_og)
    x_train_m3gp_tsne = tsne.fit_transform(x_train_m3gp)
    
    x_test_og_tsne = tsne.fit_transform(x_test_og)
    x_test_m3gp_tsne = tsne.fit_transform(x_test_m3gp)

    
    df_train_og_tsne = np.hstack((x_train_og_tsne,y_train))
    df_train_m3gp_tsne = np.hstack((x_train_m3gp_tsne,y_train))
    
    df_test_og_tsne = np.hstack((x_test_og_tsne,y_test))
    df_test_m3gp_tsne = np.hstack((x_test_m3gp_tsne,y_test))

    
    df_train_og_tsne = pd.DataFrame(df_train_og_tsne, columns=['componente 1', 'componente 2', 'clases'])
    df_train_m3gp_tsne = pd.DataFrame(df_train_m3gp_tsne, columns=['componente 1', 'componente 2', 'clases'])
    
    del df_train_og_tsne, df_train_m3gp_tsne, df_test_og_tsne, df_test_m3gp_tsne
    
#--------------------------------------------------------    

    clases_color = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 
                    'darkblue', 'darkorange', 'darkgreen', 'darkred', 'violet', 'brown', 'pink', 'yellow', 'lime', 'steelblue',
                    'deeppink', 'indigo', 'black', 'gold', 'rosybrown', 'gray']
    
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
    
    folder = os.getcwd() +'\\'+ nombre
    
    isdir = os.path.isdir(folder)
    
    if isdir== False:  
        problema_folder = os.mkdir(folder)
    problema_folder = folder
    
#--------------------------------------------------------    
    x = df_train_og_tsne['componente 1']
    y = df_train_og_tsne['componente 2']
    hue = df_train_og_tsne['clases']
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    sns.scatterplot(x = x, y = y, hue = hue, palette = clases_color)
    classes_txt = np.unique(y_train_txt).tolist()
    classes_txt.sort(key=natural_keys)
    L=plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Classes')
    for j,c in enumerate(clases):
        L.get_texts()[j].set_text(classes_txt[j])
    plt.savefig(problema_folder + '/'+ (base +'_OG_Train.pdf'))
    plt.show()
    plt.clf()
    print(base +'_OG_Train.pdf')
    del x, y, hue, L
    
    x = df_train_m3gp_tsne['componente 1']
    y = df_train_m3gp_tsne['componente 2']
    hue = df_train_m3gp_tsne['clases']
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    sns.scatterplot(x = x, y = y, hue = hue, palette = clases_color)
    classes_txt = np.unique(y_train_txt).tolist()
    classes_txt.sort(key=natural_keys)
    L=plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Classes')
    
    for j,c in enumerate(clases):
        L.get_texts()[j].set_text(classes_txt[j])
    plt.savefig(problema_folder + '/'+ (base +'_M3GP_Train.pdf'))
    plt.show()
    plt.clf()
    print((base +'_M3GP_Train.pdf'))
    
    del x, y, hue, L
    del df_train_m3gp_tsne, df_train_og_tsne, df_test_m3gp_tsne, df_test_og_tsne
    del y_test, y_test_txt, y_train, y_train_txt
    del x_train_og, x_train_m3gp, x_test_og, x_test_m3gp, tsne
    del x_train_og_tsne, x_train_m3gp_tsne, x_test_og_tsne, x_test_m3gp_tsne

#--------------------------------------------------------

t = 100
t = csv_df['nodos']

plt.xlabel('OTDD ')
plt.ylabel('Train Δerror%')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['% ERROR train'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette = color_grama)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.show()
plt.clf()

plt.xlabel('OTDD ')
plt.ylabel('Test Δerror%')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['% ERROR test'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.show()
plt.clf()


plt.xlabel('OTDD ')
plt.ylabel('M3GP Features')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['num rasgos m3gp'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.show()
plt.clf()


plt.xlabel('OTDD')
plt.ylabel('Δ features')
sns.scatterplot(x = csv_df['OTDD'], y = csv_df['dif rasgos'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem')
plt.show()
plt.clf()


plt.xlabel('M3GP Features')
plt.ylabel('Train Δerror%')
sns.scatterplot(x = csv_df['num rasgos m3gp'], y = csv_df['% ERROR train'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem', fontsize="15")
plt.show()
plt.clf()


plt.xlabel('M3GP Features')
plt.ylabel('Test Δerror%')
sns.scatterplot(x = csv_df['dif rasgos'], y = csv_df['% ERROR test'], hue = csv_df['Problema'], s = t, alpha = 0.7, palette=color_grama)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Problem', fontsize="15")
plt.show()
plt.clf()

--------------------------------------------------------
csv_df = pd.read_csv(archivos_en_directorio_csv[1])
datos = csv_df

nombre = datos["OG"]
nombre = nombre.str.split('_').str.get(0)
nombre = nombre.unique()
split = len(nombre)
dfs = np.array_split(csv_df, split)
color_grama = ['darkgreen', 'darkblue', 'crimson', 'purple', 'darkorange', 'black', 'gold']
--------------------------------------------------------

for m,datos in enumerate(dfs):
    problema = nombre[m]
    
    print(problema)
    folder = os.getcwd() +'\\'+ nombre[m] + '_ind'
        
    isdir = os.path.isdir(folder)
        
    if isdir== False:  
        problema_folder = os.mkdir(folder)
        
    problema_folder = folder
    
    plt.xlabel('OTDD ')
    plt.ylabel('Train Δerror%')
    t = datos['nodos'][0:29]
    sns.scatterplot(x = datos['OTDD'][0:29], y = datos['% ERROR train'][0:29], s = t, alpha = 0.7, color=color_grama[m])
    plt.savefig(problema_folder + '/'+ (problema +'_O_vs_TrE.pdf'))
    plt.show()
    plt.clf()
    
    plt.xlabel('OTDD ')
    plt.ylabel('Test Δerror%')
    sns.scatterplot(x = datos['OTDD'][0:29], y = datos['% ERROR test'][0:29], s = t, alpha = 0.7, color=color_grama[m])
    plt.savefig(problema_folder + '/'+ (problema +'_O_vs_TeE.pdf'))
    plt.show()
    plt.clf()
    
    
    plt.xlabel('OTDD ')
    plt.ylabel('M3GP Features')
    sns.scatterplot(x = datos['OTDD'][0:29], y = datos['num rasgos m3gp'][0:29], s = t, alpha = 0.7, color=color_grama[m])
    plt.savefig(problema_folder + '/'+ (problema +'_O_vs_MF.pdf'))
    plt.show()
    plt.clf()
    
    plt.xlabel('OTDD')
    plt.ylabel('Δ features')
    sns.scatterplot(x = datos['OTDD'][0:29], y = datos['dif rasgos'][0:29], s = t, alpha = 0.7, color=color_grama[m])
    plt.savefig(problema_folder + '/'+ (problema +'_O_vs_DF.pdf'))
    plt.show()
    plt.clf()
     
    plt.xlabel('M3GP Features')
    plt.ylabel('Train Δerror%')
    sns.scatterplot(x = datos['num rasgos m3gp'][0:29], y = datos['% ERROR train'][0:29], s = t, alpha = 0.7, color=color_grama[m])
    plt.savefig(problema_folder + '/'+ (problema +'_MF_vs_TrE.pdf'))
    plt.show()
    plt.clf()
    
    plt.xlabel('M3GP Features')
    plt.ylabel('Test Δerror%')
    sns.scatterplot(x = datos['num rasgos m3gp'][0:29], y = datos['% ERROR test'][0:29], s = t, alpha = 0.7, color=color_grama[m])
    plt.savefig(problema_folder + '/'+ (problema +'_MF_vs_TeE.pdf'))
    plt.show()
    plt.clf()

    
