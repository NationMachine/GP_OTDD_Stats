import pandas as pd
import numpy as np

import re
import glob
import csv


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

archivos_en_directorio_mat = glob.glob("*.csv")

archivos_en_directorio_mat.sort(key=natural_keys)
    
datos = pd.read_csv(archivos_en_directorio_mat[0])
nombre = datos["OG"]
nombre = nombre.str.split('_').str.get(0)
nombre = nombre.unique()

dfs = np.array_split(datos, 7)

for p,datos in enumerate(dfs):

    nombre = datos["OG"]
    problema = nombre[p]
    
    print(problema)
    
    pro_M3GP_nodos = datos['nodos'][0:29].mean()
    pro_M3GP_otdd = datos['OTDD'][0:29].mean()
    pro_M3GP_rasgos = datos['num rasgos m3gp'][0:29].mean()
    pro_MD_train_m3gp = datos['MD_train_m3gp'][0:29].mean()
    pro_MD_train_og = datos['MD_train_og'][0:29].mean()
    pro_MD_test_m3gp = datos['MD_test_m3gp'][0:29].mean()
    pro_MD_test_og = datos['MD_test_og'][0:29].mean()
    
    med_M3GP_nodos = datos['nodos'][0:29].median()
    med_M3GP_otdd = datos['OTDD'][0:29].median()
    med_M3GP_rasgos = datos['num rasgos m3gp'][0:29].median()
    med_MD_train_m3gp = datos['MD_train_m3gp'][0:29].median()
    med_MD_train_og = datos['MD_train_og'][0:29].median()
    med_MD_test_m3gp = datos['MD_test_m3gp'][0:29].median()
    med_MD_test_og = datos['MD_test_og'][0:29].median()
    
    std_M3GP_nodos = datos['nodos'][0:29].std()
    std_M3GP_otdd = datos['OTDD'][0:29].std()
    std_M3GP_rasgos = datos['num rasgos m3gp'][0:29].std()
    std_MD_train_m3gp = datos['MD_train_m3gp'][0:29].std()
    std_MD_train_og = datos['MD_train_og'][0:29].std()
    std_MD_test_m3gp = datos['MD_test_m3gp'][0:29].std()
    std_MD_test_og = datos['MD_test_og'][0:29].std()
    
    Q1_M3GP_nodos = datos['nodos'][0:29].quantile(q=0.25)
    Q1_M3GP_otdd = datos['OTDD'][0:29].quantile(q=0.25)
    Q1_M3GP_rasgos = datos['num rasgos m3gp'][0:29].quantile(q=0.25)
    Q1_MD_train_m3gp = datos['MD_train_m3gp'][0:29].quantile(q=0.25)
    Q1_MD_train_og = datos['MD_train_og'][0:29].quantile(q=0.25)
    Q1_MD_test_m3gp = datos['MD_test_m3gp'][0:29].quantile(q=0.25)
    Q1_MD_test_og = datos['MD_test_og'][0:29].quantile(q=0.25)
    
    Q3_M3GP_nodos = datos['nodos'][0:29].quantile(q=0.75)
    Q3_M3GP_otdd = datos['OTDD'][0:29].quantile(q=0.75)
    Q3_M3GP_rasgos = datos['num rasgos m3gp'][0:29].quantile(q=0.75)
    Q3_MD_train_m3gp = datos['MD_train_m3gp'][0:29].quantile(q=0.75)
    Q3_MD_train_og = datos['MD_train_og'][0:29].quantile(q=0.75)
    Q3_MD_test_m3gp = datos['MD_test_m3gp'][0:29].quantile(q=0.75)
    Q3_MD_test_og = datos['MD_test_og'][0:29].quantile(q=0.75)
    
    
    OTDD = ['OTDD', pro_M3GP_otdd, med_M3GP_otdd, std_M3GP_otdd, Q1_M3GP_otdd, Q3_M3GP_otdd]
    
    MD_train_m3gp = ['MD_train_m3gp', pro_MD_train_m3gp, med_MD_train_m3gp, std_MD_train_m3gp, Q1_MD_train_m3gp, Q3_MD_train_m3gp]
    
    MD_train_og = ['MD_train_og', pro_MD_train_og, med_MD_train_og, std_MD_train_og, Q1_MD_train_og, Q3_MD_train_og]
    
    MD_test_m3gp = ['MD_test_m3gp', pro_MD_test_m3gp, med_MD_test_m3gp, std_MD_test_m3gp, Q1_MD_test_m3gp, Q3_MD_test_m3gp]
    
    MD_test_og = ['MD_test_og' ,pro_MD_test_og, med_MD_test_og, std_MD_test_og, Q1_MD_test_og, Q3_MD_test_og]
    
    rasgos_m3gp = ['rasgos_m3gp', pro_M3GP_rasgos, med_M3GP_rasgos, std_M3GP_rasgos, Q1_M3GP_rasgos, Q3_M3GP_rasgos]
    
    nodos = ['nodos', pro_M3GP_nodos, med_M3GP_nodos, std_M3GP_nodos, Q1_M3GP_nodos, Q3_M3GP_nodos]
    
    head =[' ','promedio',	'mediana',	'des std',	'Q1',	'Q3']
    index = ['OTDD', 'MD_train_m3gp', 'MD_train_og', 'MD_test_m3gp', 'MD_test_og', 'num rasgos m3gp', 'nodos']
    
    file = open('Resultados_clas_estadisticas.csv','a', newline='')
    writer = csv.writer(file)
    
    
    writer.writerow(problema)
    writer.writerow(head)
    writer.writerow(OTDD)
    writer.writerow(MD_train_m3gp)
    writer.writerow(MD_train_og)
    writer.writerow(MD_test_m3gp)
    writer.writerow(MD_test_og)
    writer.writerow(rasgos_m3gp)
    writer.writerow(nodos)
    
    file.close()
    
    file = open('Resultados_clas_mejora.csv','a', newline='')
    writer = csv.writer(file)
    
    mejora_med_test = datos['% ERROR test'][0:29].median()
    mejora_med_train = datos['% ERROR train'][0:29].median()
    mejora_pro_test = datos['% ERROR test'][0:29].mean()
    mejora_pro_train = datos['% ERROR train'][0:29].mean()
    
    writer.writerow(problema)
    linea = [' ', '% de mejora']
    writer.writerow(linea)

    linea = ['mediana test', mejora_med_test]
    writer.writerow(linea)

    linea = ['mediana train', mejora_med_train]
    writer.writerow(linea)

    linea = ['promedio test', mejora_pro_test]
    writer.writerow(linea)

    linea = ['promedio train', mejora_pro_train]
    writer.writerow(linea)
    file.close()
    
    file = open('Resultados_clas_pca.csv','a', newline='')
    writer = csv.writer(file)
    
    pro_PCA_n = datos['PCA'][0:29].mean()
    med_PCA_n = datos['PCA'][0:29].median()
    std_PCA_n = datos['PCA'][0:29].std()

    
    pro_Variance = datos['Variance'][0:29].mean()
    med_Variance = datos['Variance'][0:29].median()
    std_Variance = datos['Variance'][0:29].std()

    
    resultado = [problema, pro_PCA_n, med_PCA_n, std_PCA_n, pro_Variance, med_Variance, std_Variance]
    writer.writerow(resultado)
    file.close()
    resultados = pd.DataFrame(columns = ['Problema', "Varianza", "Componentes PCA"])

    resultado = [mat_cargado, varianza, componentes]

    file = open('Resultados_clas_PCA_m3gp.csv','a', newline='')
    writer = csv.writer(file)

    writer.writerow(resultado)
    file.close()
    
    del mat_cargado, varianza, componentes
