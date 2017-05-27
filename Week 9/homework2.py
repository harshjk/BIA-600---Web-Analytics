# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:44:41 2017

@author: Harsh Kevadia
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
#from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn.svm import SVC

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

train_features = computer_train.data + sports_train.data + politics_train.data + rec_train.data
test_features = computer_test.data + sports_test.data + politics_test.data + rec_test.data

c_train = np.full(computer_train.target.shape, 0 ,np.int64)
c_test = np.full(computer_test.target.shape, 0 ,np.int64)

s_train = np.full(sports_train.target.shape, 1 ,np.int64)
s_test = np.full(sports_test.target.shape, 1 ,np.int64)

p_train = np.full(politics_train.target.shape, 2 ,np.int64)
p_test = np.full(politics_test.target.shape, 2 ,np.int64)

r_train = np.full(rec_train.target.shape, 3 ,np.int64)
r_test = np.full(rec_test.target.shape, 3 ,np.int64)

train_labels = np.concatenate((c_train,s_train,p_train,r_train))
test_labels = np.concatenate((c_test,s_test,p_test,r_test))

vectorizer = TfidfVectorizer(stop_words='english')
train = vectorizer.fit_transform(train_features)
test = vectorizer.transform(test_features)


#clf = BernoulliNB(alpha=0.01)
clf = MultinomialNB(alpha=0.01)
#clf = NearestCentroid()
#clf = KNeighborsClassifier(n_neighbors=30)
#clf = MLPClassifier()
#clf = tree.DecisionTreeClassifier()
#clf = SVC(C=0.01, kernel = 'poly', coef0 = 1.5)

clf.fit(train,train_labels)
pred=clf.predict(test)

print (accuracy_score(pred,test_labels))
