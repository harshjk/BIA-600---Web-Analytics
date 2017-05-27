# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:12:20 2017

@author: Harsh Kevadia
"""

import operator
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
    
#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex
    
def processSentence(sentence,posLex,negLex,tagger):
    
    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    loadTagger = load(_POS_TAGGER)
    
    results = []
    
    sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces
    
    #tokenize the sentence
    terms = nltk.word_tokenize(sentence.lower())
    
    POSterms=getPOSterms(terms,tagger,loadTagger)
    nouns = POSterms['NN']

    fourgrams = ngrams(terms,4) #compute 2-grams
    
    #for each 2gram
    for tg in fourgrams:  
        if tg[0] == "not":
            if tg[2] in posLex or tg[2] in negLex:
                if tg[3] in nouns:
                    results.append(tg)
    
    return results;
    

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms

def getTop3(D):
    sorted_D=sorted(D.items(),key=operator.itemgetter(1),reverse=True)
    i=0
    top3=list()
    for key,value in sorted_D:
        if(i<3):
            top3.append(key)
            i=i+1
    return top3
    
def run(fpath):

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))

    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')
    
    #adjAfterAdv=[]
    results = []

    # for each sentence
    for sentence in sentences:  

        POStags=['NN','JJ'] # POS tags of interest 		
        
        results = processSentence(sentence,posLex,negLex,POStags)
        #nouns=POSterms['NN']

        #get the results for this sentence 
        #adjAfterAdv+=getAdvAdjTwograms(terms, nouns, adverbs)
		
    return results

if __name__=='__main__':
    print (run('input.txt'))
    stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000}
    print(getTop3(stats))