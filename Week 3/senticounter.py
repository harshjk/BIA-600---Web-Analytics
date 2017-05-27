# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:59:02 2017

@author: Harsh Kevadia
"""
def loadLexiconFromFile(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex
    
def loadLexiconFromLine(line):
    newLex = set()
    line=line.lower().strip()
    words=line.split(' ')
    for word in words:
        newLex.add(word.strip())
    return newLex
    
def run(path):
    freq={} 
    #load the positive and negative lexicons
    posLex=loadLexiconFromFile('positive-words.txt')
    
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        
        line=line.lower().strip()
        words = loadLexiconFromLine(line)
        
        for word in words: #for every word in the review
            if word in posLex:    
                if freq.get(word,None) == None:
                    freq[word] = 1
                else:
                    freq[word] = freq.get(word) + 1
            
    fin.close()
    return freq 



if __name__ == "__main__": 
    senti=run('textfile')
    #print(senti)
    for word in senti:
        print(word,":",senti.get(word))