#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:47:56 2020

@author: issamubuntu
"""
import networkx as nx
import json
import os


with open(os.getcwd()+'/articles_opperationnels.txt')as f:
    s=f.read()
    dico_articles=json.loads(s)


with open(os.getcwd()+'/references_opperationnels.txt')as f:
    s=f.read()
    dico_references=json.loads(s)    
   

class Authors:
    def __init__(self,name):
        self.name=name.lower()
    
    def articles_of(self):
        """rendre tous les article que self.name a praticipé à leur rédaction  """
        
        l=[]    
        for article in dico_articles.keys():
            if self.name in dico_articles[article]:
                l.append(article)
        return l 
       
    def cited_by(self):
        s=set()
        if self.articles_of()==[]:
            return "cet autheur n'a pas d'article"
        else:
            
            for article in self.articles_of(): #articles_of(self.name):
                if article in dico_references.keys():# si article cite au moins un autre article
                    articles_cité_dans_article =dico_references[article]
                    for a in articles_cité_dans_article :
                        s=s.union(set(dico_articles[a]))
            l=list(s)
            return l    






#############################################################################################################################
def articles_of(author):
    articls_ecrit_par_author=[]
    for k,v in dico_articles.items():
        if author in v:
            articls_ecrit_par_author.append(k)
    articls_ecrit_par_author=list(set(articls_ecrit_par_author))   
    return articls_ecrit_par_author         



########################Construction du graph des citations d'articles########################################
Graph_articls=nx.DiGraph(dico_references)
nx.info(Graph_articls)
Graph_articls.add_nodes_from(dico_articles.keys())




###################################
#question :sort la liste pondérée des auteurs Bi qui influencent A avec une profondeur au plus N. La pondération 
#représente l’intensité de l’influence.
#######################################
def influencer_of(Author,N):# sort la liste des auteurs Bi qui influencent A à une profondeur maximum N
    s=set()
    for art_A in articles_of(Author):
        liste=list(nx.bfs_edges(Graph_articls,art_A,depth_limit=N))
        liste=[l[1] for l in liste]
        for art in liste:
            s=s.union(set(dico_articles[art]))
            s.discard(Author)
    return list(s)        




def Intencity_influencer_of(A,B,N):
    
    #A:auteur influencé , B:auteur influencant,N profondeur d'influence 
                        
    #==> sort les auteur qui influencent sur A avec profondeur au plus N (en cherchant dans le graph des articles avec un
    #rayon N)
    
    I=0
    for art_A in articles_of(A):
        for art_B in articles_of(B):
            try:
                liste1=list(nx.all_simple_paths(Graph_articls,art_A,art_B,N))#récuper tous les chemins entre art_A ==> ....==>art_B prof<=N
                liste2=[len(k)-1 for k in liste1]
                I+=sum([1/b for b in liste2])
            except: pass                    
    return I  


def influencer_of_ponderé(A,N):
    dico={}
    for B in influencer_of(A,N):
        dico[B]=Intencity_influencer_of(A,B,N)
    return dico    
        
  
############################################################################################################################################

#sort la liste pondérée des auteurs Bi influencés avec une profondeur d’au plus N par un auteur donné A.
# La pondération représente l’intensité de l’influence.
def influenced_by(Author,N):
    s=set()
    for art_A in articles_of(Author):
        liste=list(nx.bfs_edges(Graph_articls,art_A,depth_limit=N,reverse=True))
        liste=[l[1] for l in liste]
        for art in liste:
            s=s.union(set(dico_articles[art]))
            s.discard(Author)
    return list(s) 




def Intencity_influenced_by(A,B,N):#A:auteur influencé , B:auteur influencant,N profondeur d'influence 
                        #==> sort les auteur qui influencent sur A avec profondeur au plus N (en cherchant dans le graph des articles avec un ray
                        #rayon N)
    return Intencity_influencer_of(A,B,N)
                
    
def influenced_by_ponderé(B,N):
    dico={}
    for i in influenced_by(B,N):
        dico[i]=Intencity_influenced_by(i,B,N)
    return dico 




###################################################################################################################"
#                   Communauté
#######################################################################################################################    

def Community(Author,N):
    s=set(influenced_by(Author,N)).union(influencer_of(Author,N))
    
    return list(s)

       
    
if __name__=='__main__':
    pass
    










