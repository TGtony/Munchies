products = [] # stores ASIN
corpus = []

with open('chip_product_adjectives.txt') as input_file:
    for line in input_file:
        if line[0] != '[':
            line = line.strip('\n')
            products.append(line)
        else:
            line = line.strip('\n')
            corpus.append(line) # builds corpus

input_file.close()

target = [] # store target adjectives
with open("top300.txt") as f:
    for line in f:
        for word in line.split():
            target.append(word)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus) # calculates tfidf

features = tfidf_vectorizer.get_feature_names() # feature vector
tfidf_array = tfidf_matrix.toarray()

indices = [] # store indices of the target adj found in the feature vector
indices2 = [] # store indices of all adj in feature vector

import numpy as np

for i in range(len(target)): # if adj in features if equal to adj in target, add index
    for j in range(len(features)):
        if features[j] == target[i]:
            indices.append(j)

for i in range(len(features)): # generate list of indexes for comparison
    indices2.append(i)

indicesremove = np.setdiff1d(indices2, indices) # generate list of indexes that are not of the target

tfidf_array = np.delete(tfidf_array, indicesremove, 1) # delete all columns of unwanted adj
features = np.delete(features, indicesremove, None) # delete all columns of unwanted adj

from sklearn.svm import SVC

classification_model = SVC(probability = True)
classification_model.fit(tfidf_array, products)

from sklearn.externals import joblib
joblib.dump(classification_model, 'svm_model.pk1') # save SVM model

with open("features_list.txt", 'w') as output: #write features (adjectives) list to file
    for i in features:
        output.write(i + '\n')
output.close()
