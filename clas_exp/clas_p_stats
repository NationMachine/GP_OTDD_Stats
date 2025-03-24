import pandas as pd
import numpy as np
import re
import glob
import csv
from scipy import stats
from scipy.stats import pearsonr

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

archivos_en_directorio_mat = glob.glob("*.csv")
archivos_en_directorio_mat.sort(key=natural_keys)

datos = pd.read_csv(archivos_en_directorio_mat[1])
nombre = datos["OG"]
nombre = nombre.str.split('_').str.get(0)
nombre = nombre.unique()

def bivariate_stats(df, label):
  corr_df = pd.DataFrame(columns=['r', 'p', 'Pendiente','bool'])
  alpha = 0.05
  for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):        
      res = stats.linregress(df[label], df[col])
      corr_df.loc[col] = [round(res.rvalue, 2), round(res.pvalue, 2), round(res.slope,2), str(res.pvalue <= alpha)]
  return corr_df

cor_otdd = datos.corrwith(datos['OTDD'])
cor_m3gp = datos.corrwith(datos['num rasgos m3gp'])

con_otdd = bivariate_stats(datos, 'OTDD')['r']
con_m3gp = bivariate_stats(datos, 'num rasgos m3gp')['r']

con_otdd = bivariate_stats(datos, 'OTDD')['bool']
con_m3gp = bivariate_stats(datos, 'num rasgos m3gp')['bool']
cor_g = np.vstack((con_otdd,con_m3gp))
index = cor_m3gp.index
cor_g = pd.DataFrame(cor_g, columns=index, index = ('OTDD','M3GP features'))

dfs = np.array_split(datos, 7)

for p,datos in enumerate(dfs):
    problema = nombre[p]
 
    
    con_otdd = bivariate_stats(datos[0:29], 'OTDD')
    con_m3gp = bivariate_stats(datos[0:29], 'num rasgos m3gp')
    with open('Resultados_pvalue_num.csv','a', newline='') as file:      
        writer = csv.writer(file)
        info = 'p'
        writer.writerow(con_otdd[info])              
        writer.writerow(con_m3gp[info])  
        file.close()
        print(problema)
        
for p,datos in enumerate(dfs):
    problema = nombre[p]
    
    con_otdd = bivariate_stats(datos[0:29], 'OTDD')
    con_m3gp = bivariate_stats(datos[0:29], 'num rasgos m3gp')
    with open('Resultados_pvalue_bool.csv','a', newline='') as file:      
        writer = csv.writer(file)
        info = 'bool'
        writer.writerow(con_otdd[info])              
        writer.writerow(con_m3gp[info])  
        file.close()
        print(problema)
        
for p,datos in enumerate(dfs):
    problema = nombre[p]
    
    con_otdd = bivariate_stats(datos[0:29], 'OTDD')
    con_m3gp = bivariate_stats(datos[0:29], 'num rasgos m3gp')
    with open('Resultados_cor.csv','a', newline='') as file:      
        writer = csv.writer(file)
        info = 'r'
        writer.writerow(con_otdd[info])              
        writer.writerow(con_m3gp[info])  
        file.close()
        print(problema)          
