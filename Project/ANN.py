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
    
    clf = MLPClassifier(solver='lbgfs', alpha=1e-10, hidden_layer_sizes=(50,50), max_iter=100, random_state=1000, activation='relu', batch_size='auto', learning_rate='adaptive' )
    #, beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08, learning_rate='constant', learning_rate_init=0.001, momentum=0.9, nesterovs_momentum=True, power_t=0.5, shuffle=True, solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False)
    
    #clf =  SVC(gamma=2, C=1)
    #clf = MultinomialNB(alpha=0.1)
    #clf = GaussianNB()
    clf.fit(train,train_tags)
    pred=clf.predict(test)
    
    print (accuracy_score(pred,test_tags))