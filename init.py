#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:31:00 2020

@author: issamubuntu
"""

import glob
import os 
import re
import json

##################################################################################################
def get_authors(numero_article,path_article):
    #path_article='/home/issamubuntu/Desktop/project_python'+'/hep-th-abs(1)/'+dic_years[numero_article[:2]]+'/'+numero_article+'.abs'
    with open(path_article) as f:
        s=f.read()
        line_authors_file_pattern="Author[s]{0,1}:.{0,}\n"
        line_authors=re.findall(line_authors_file_pattern,s)[0][8:-1] 
        
        line_authors_names=re.sub(r"(\(.+\){0,})","",line_authors).strip()#
        line_authors_names=line_authors_names.replace(' and ',',')

        pattern_authors_names=r"""[{}"\w+.\\~'_\s-]+"""
        list_authors_names=re.findall(pattern_authors_names,line_authors_names)

    
        list_authors_names=[name.strip().lower() for name in list_authors_names]
        #supprimer les chaines vides
        v=list_authors_names.count("")
        for i in range(v):
            list_authors_names.remove("")
        
        return list_authors_names

####################################################################################################
        
    
def créer_fichier_opperationel_articles(articles):
#    """"
 #   -->article: chaine contenant le chemin complet vers le dossier des articles
  #  -->references: chaine contenant le chemin complet vers le fichier des citations
   # """"
    chemins_articles=glob.glob(articles+'/**/*.abs')
    #chemin_citation=references
    
    liste_des_articles=[path[-11:-4] for path in chemins_articles ]
    
    dico={}
    for numero_article,path_article in zip(liste_des_articles,chemins_articles):
        
        dico[numero_article]=get_authors(numero_article,path_article)
    #construire le fichier contenant le dictionnaire dont les clé sont le num d'article et les valeurs sont une lise des auteurs  
    with open(os.getcwd()+'/articles_opperationnels.txt','w') as f:
        f.write(json.dumps(dico))    
    

################################################################################################################################
 
def créer_fichier_opperationel_citations(references):
   # with open(os.getcwd()+'/article_new.txt','r') as f:
    #    s=f.read()
     #   dico_authors= json.loads(s)

    chemin_citation=references
    dico_citations={}
    with open(chemin_citation,'r') as f:
        for line in f:
            num_articl_referencer=line.split()[0] 
            num_articl_referenced=line.split()[1] 
           
            if num_articl_referencer in dico_citations.keys():
                dico_citations[num_articl_referencer].append(num_articl_referenced)
            
            if num_articl_referencer not in dico_citations.keys():
                dico_citations[num_articl_referencer]=[num_articl_referenced]
    #construire le fichier contenant le dictionnaire dont les clé sont le num d'article et les valeurs sont une lise des auteurs  
    with open(os.getcwd()+'/references_opperationnels.txt','w') as f:
        f.write(json.dumps(dico_citations))            
                
def initialisation(articles,references):
    créer_fichier_opperationel_articles(articles)
    créer_fichier_opperationel_citations(references)
    


if __name__=='__main__':
    pass
    















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    