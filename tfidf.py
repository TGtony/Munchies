products = [] # stores ASIN
corpus = []

with open('chip_product_adjectives.txt') as input_file:
    for line in input_file:
        if line[0] != '[':
            products.append(line)
        else:
            corpus.append(line) # builds corpus

input_file.close()

# the chosen adjectives:
target = ['healthy', 'sweet', 'fresh', 'hot', 'crunchy',
          'natural', 'cheese', 'organic', 'greasy', 'salty',
          'sour', 'crispy', 'thick', 'garlic', 'baked',
          'dry', 'spicy', 'mild', 'nacho', 'soft']

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

from sklearn.svm import SVR

numlabels = [] # assign an integer label to each product

for i in range(len(tfidf_array)):
    numlabels.append(i+1)

# test:
pred = [[0, 0.9, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

regression_model = SVR()
regression_model.fit(tfidf_array, numlabels)

result = regression_model.predict(pred)
print (result)

result_index = int(result) - 1 # get index number for product match

print (products[result_index]) # print product at index

# writing to an output file
#
#output = open('chips_tfidf.txt', 'w')
#for i in range(len(tfidf_array)):
#    for j in range(len(features)):
#        outline = str(tfidf_array[i][j]) + ", "
#        output.write(outline)
#    output.write('\n')
#output.close()
