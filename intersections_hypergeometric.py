#!/usr/bin/env python
# -*- coding: utf-8 -*-
#argv[0] = Gsea_set
#argv[1] = gene_set to intersection
#argv[3] = universe

#this program take three files, specific for each experiment platform, as arguments and returns the intersection, and the hypergeometric computation results
import sys
import argparse
import re
import scipy.stats as stats
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Take three files as argument:\
                                 1  gsea_set\
                                 2  gene_set\
                                 3  universe\
                                 Process this files through hypergeometric test and returns the intersection.\
                                 Output:\
                                 1 GSEA_set             set di GSEA\
                                 2 mirna_up             set di geni up regolati in un dato esperimento\
                                 3 num_GSEA             numero di geni nel set gsea\
                                 4 num_up               numero di geni nel set mirna_up\
                                 5 num_universo         numero di geni nell'universo\
                                 6 num_intersezione     numero di geni nell'intersezione\
                                 7 pvalue               probabilità di ottenere un intersezione più grande di quella ottenuta\
                                 8 intersezione         geni contenuti nell'intersezione")

#funzione che mi serve a raggruppare le liste in base al ser/esperimento
def group(seq, sep):
    g = []
    for el in seq:
        if re.match(sep, el):
            yield g
            g = []
        g.append(el)
    yield g



with open(sys.argv[1], 'r') as gsea_set:
    with open(sys.argv[2], 'r') as gene_set:
        with open(sys.argv[3], 'r') as universo_set:
            #crea sotto liste basate sui set GSEA
            gsea = list(gsea_set)
            for i, item in enumerate(gsea):
                gsea[i] = item.rstrip()
            gsea = list(group(gsea, '>.*'))
            
            #crea sottoliste basate sugli esperimenti
            genes = list(gene_set)
            for i, item in enumerate(genes):
                genes[i] = item.rstrip()
            genes = list(group(genes, '>.*'))
            
            #creo lista dei geni nell'universo
            universo = list(universo_set)
            for i, item in enumerate(universo):
                universo[i] = item.rstrip()
            num_universo = len(universo)-1
            
            #itero tra i due gruppi di liste per ottenere tutti gli incroci possibili
            gsea_clean = []
            for a in gsea:
                no_empty = [e for e in a if e != ' '] # tolgo gli item contenenti nulla
                gsea_clean.append(no_empty)
            gsea_clean = [x for x in filter(None, gsea_clean)]
            
            genes_clean = []
            for a in genes:
                no_empty = [e for e in a if e !='']# tolgo gli item contenenti nulla
                genes_clean.append(no_empty)
            genes_clean = [x for x in filter(None, genes_clean)]
            
            header=[['GSEA_set','miRNA', 'size_GSEA',  'size_mirna', 'size_universo', 'size_intersezione', 'pvalue', 'intersezione']]
            #import pdb; pdb.set_trace()
            for t in gsea_clean:
                #import pdb; pdb.set_trace()
                #print(t)
                #import pdb; pdb.set_trace()
                #print(set(t[1:]))
                for i in genes_clean:
                    
                    result = set(t[1:]).intersection(set(i[1:]))
                    num_geni  = len(i)-1
                    num_gsea = len(t)-1
                    num_intersection = len(result)
                    pvalue_low = str(stats.hypergeom.cdf(num_intersection,num_universo,num_gsea,num_geni)) #il pvalue che indica la probabilità di trovare un intersezione più piccola 
                    pvalue_high = str(stats.hypergeom.sf(num_intersection - 1,num_universo,num_gsea,num_geni))#il pvalue ditrovare un intersezione maggiore
                    table=[t[0:1], i[0:1], num_gsea, num_geni, num_universo, num_intersection,pvalue_high, result]
                    #print(t[0])
                    #print(len(table))
                    header.append(table)
                    #print(len(header))
                 
            print(tabulate(header, headers="firstrow"))
            #print('fine')
        
    


#print 'total number in population: ' + num_universo
#print 'total number with condition in population: ' + num_gsea
#print 'number in subset: ' + num_geni
#print 'number with condition in subset: ' + num_intersection
