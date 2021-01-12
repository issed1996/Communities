#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:11:09 2020

@author: issamubuntu
"""
import sys
import init




def main():
    try:
        if sys.argv[1] == 'init':
            #import init
            articles=sys.argv[2]
            references=sys.argv[3]
            init.initialisation(articles,references)

        if sys.argv[1]=='cite':
            import articls_authors as aa
            author_name=sys.argv[2]
            author=aa.Authors(author_name)
            print(author.cited_by())
            #articls_authors.cite(author_name)
    
        if sys.argv[1]=='influencés_par' :   
            import articls_authors as aa
            Author=sys.argv[2]
            N=int(sys.argv[3])
            print(aa.influenced_by_ponderé(Author,N))
            
        if sys.argv[1]=='influencant_sur':  
            import articls_authors as aa
            Author=sys.argv[2]
            N=int(sys.argv[3])
            print(aa.influencer_of_ponderé(Author,N))
    
        if sys.argv[1]== 'communautes':
            Author=  sys.argv[2] 
            N=int(sys.argv[3])
            import articls_authors as aa
            print(aa.Community(Author,N))
    except:
        print('try again...')
        
if __name__=='__main__':
    main()        
    
    
    
    
    
