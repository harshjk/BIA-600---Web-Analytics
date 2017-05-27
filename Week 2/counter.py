# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:47:55 2017

@author: Harsh Kevadia
"""
def run(path):
    freq = {}
    maxCount = 0
    maxWord = None
    fin = open(path)
    for line in fin:
        words=line.lower().strip().split(' ')
        for word in words:
            if freq.get(word,None) == None:
                freq[word] = 1
            else:
                freq[word] = freq.get(word) + 1
            if(maxCount < freq[word]):
                maxCount = freq[word]
                maxWord = word
    fin.close()
    return maxWord
print(run('textfile'))