# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:51:33 2017

@author: Harsh Kevadia
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

fw=open('training.txt','w')

computer_categories = ['comp.graphics','comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware']
computer_test_categories = ['comp.windows.x']

sports_categories = ['rec.sport.hockey']
sports_test_categories = ['rec.sport.baseball']

politics_categories = ['talk.politics.guns','talk.politics.mideast']
politics_test_categories = ['talk.politics.misc']

rec_categories = ['rec.motorcycles']
rec_test_categories = ['rec.autos']

computer_train = fetch_20newsgroups(subset='all',categories = computer_categories,remove=('headers', 'footers'))
computer_test = fetch_20newsgroups(subset='all',categories = computer_test_categories,remove=('headers', 'footers'))

sports_train = fetch_20newsgroups(subset='all',categories = sports_categories,remove=('headers', 'footers'))
sports_test = fetch_20newsgroups(subset='all',categories = sports_test_categories,remove=('headers', 'footers'))

politics_train = fetch_20newsgroups(subset='all',categories = politics_categories,remove=('headers', 'footers'))
politics_test = fetch_20newsgroups(subset='all',categories = politics_test_categories,remove=('headers', 'footers'))

rec_train = fetch_20newsgroups(subset='all',categories = rec_categories,remove=('headers', 'footers'))
rec_test = fetch_20newsgroups(subset='all',categories = rec_test_categories,remove=('headers', 'footers'))

fw.write(str(rec_train.data))

fw.close

#vectorizer = TfidfVectorizer()
#vectors = vectorizer.fit_transform(computer_train.data)

#Build a counter based on the training dataset
#counter = CountVectorizer()
#counter.fit(str(computer_train.data).strip('[]'))
"""
train = []
test = []

train.append(computer_train.data)
test.append(computer_test.data)

train.append(sports_train.data)
test.append(sports_test.data)

train.append(politics_train.data)
test.append(politics_test.data)

train.append(rec_train.data)
test.append(rec_test.data)


train.append(str(computer_train.data).strip('[]'))
test.append((str(computer_test.data).strip('[]')))

train.append(str(sports_train.data).strip('[]'))
test.append((str(sports_test.data).strip('[]')))

train.append(str(politics_train.data).strip('[]'))
test.append((str(politics_test.data).strip('[]')))

train.append(str(rec_train.data).strip('[]'))
test.append((str(rec_test.data).strip('[]')))
"""

vectorizer = TfidfVectorizer(stop_words='english')
train= []
test = []
c_train = vectorizer.fit_transform(computer_train.data)
c_test = vectorizer.transform(computer_test.data)
train.append(c_train)
test.append(c_test)
s_train = vectorizer.fit_transform(sports_train.data)
s_test = vectorizer.transform(sports_test.data)
train.append(s_train)
test.append(s_test)
p_train = vectorizer.fit_transform(politics_train.data)
p_test = vectorizer.transform(politics_test.data)
train.append(p_train)
test.append(p_test)
r_train = vectorizer.fit_transform(rec_train.data)
r_test = vectorizer.transform(rec_test.data)
train.append(r_train)
test.append(r_test)

#train = vectorizer.fit_transform(train)
#test = vectorizer.transform(test)
"""
train = []
train.append(vectorizer.fit_transform(computer_train.data))

train.append(vectorizer.fit_transform(sports_train.data))
train.append(vectorizer.fit_transform(politics_train.data))
train.append(vectorizer.fit_transform(rec_train.data))
"""
"""
test=[]
test.append(vectorizer.transform(computer_test.data))

test.append(vectorizer.transform(sports_test.data))
test.append(vectorizer.transform(politics_test.data))
test.append(vectorizer.transform(rec_test.data))
"""

#Build a counter based on the training dataset
#counter = CountVectorizer()
#counter.fit(train)


#count the number of times each term appears in a document and transform each doc into a count vector
#vectors = counter.transform(train)#transform the training data
#vectors_test = counter.transform(test)#transform the testing data
'''
vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(train)
vectors_test = vectorizer.transform(test)
'''
#count the number of times each term appears in a document and transform each doc into a count vector
#counts_train = vectors.transform(str(computer_train.data).strip('[]'))#transform the training data
#counts_test = vectors.transform(str(computer_test.data).strip('[]'))#transform the testing data

clf = MultinomialNB(alpha=.01)
#clf = RandomForestClassifier()

"""
lables = []
lables.append('comp')

lables.append('sports')
lables.append('politics')
lables.append('rec')
"""
train_label = []
test_label = []

c_train = np.full(computer_train.target.shape, 0 ,np.int64)
c_test = np.full(computer_test.target.shape, 0 ,np.int64)
train_label.append(c_train)
test_label.append(c_test)

s_train = np.full(sports_train.target.shape, 1 ,np.int64)
s_test = np.full(sports_test.target.shape, 1 ,np.int64)
train_label.append(s_train)
test_label.append(s_test)

p_train = np.full(politics_train.target.shape, 2 ,np.int64)
p_test = np.full(politics_test.target.shape, 2 ,np.int64)
train_label.append(p_train)
test_label.append(p_test)

r_train = np.full(rec_train.target.shape, 3 ,np.int64)
r_test = np.full(rec_test.target.shape, 3 ,np.int64)
train_label.append(r_train)
test_label.append(r_test)

#train_label = vectorizer.fit_transform(train_label)
#test_label = vectorizer.transform(test_label)

#clf.fit(train,train_label)
"""
#use hard voting to predict (majority voting)
pred=clf.predict(test)
#pred=clf.predict(vectors_test)
#metrics.f1_score(vectors_test.target, pred, average='macro')
#labels_test = ['comp', 'sport']
#print accuracy
print (accuracy_score(pred,test_label))
"""