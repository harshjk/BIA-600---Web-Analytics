# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:28:46 2017

@author: Harsh Kevadia
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def parse(file):
    fin=open(file)
    tags = []
    votes = []
    questions = []
    for line in fin: # for every line in the file (1 review per line)
      
        line=line.lower().strip()   
        
        dataLine=line.split('\t')
        if(len(dataLine) == 3):
            if(int(dataLine[1]) > -1):
                for i in range(int(dataLine[1]) + 1):
                    tags.append(dataLine[0])
                    votes.append(dataLine[1])
                    questions.append(dataLine[2])
    fin.close()
    return tags,votes,questions
if __name__ == "__main__":
    train_tags,train_votes,train_questions = parse('train.txt')
    test_tags,test_votes,test_questions = parse('test.txt')
    
    vectorizer = TfidfVectorizer(stop_words='english')
    train = vectorizer.fit_transform(train_questions)
    test = vectorizer.transform(test_questions)
    
    clf = MultinomialNB(alpha=0.1)
    
    clf.fit(train,train_tags)
    pred=clf.predict(test)
    
    print (accuracy_score(pred,test_tags))