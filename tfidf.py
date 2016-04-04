products = [] # stores ASIN
corpus = []

with open('chip_product_adjectives.txt') as input_file:
    for line in input_file:
        if line[0] != '[':
            products.append(line)
        else:
            corpus.append(line) # builds corpus

input_file.close()

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus) # calculates tfidf

features = tfidf_vectorizer.get_feature_names() # feature vector
tfidf_array = tfidf_matrix.toarray()

featureslength = len(features) # number of features in feature vector
tfidf_arraylength = len(tfidf_array) # total number of products

## following block of code is for writing to an output file
#
output = open('chips_tfidf.txt', 'w')
for i in range(tfidf_arraylength):
    output.write("[ ")
    for j in range(featureslength):
        outline = str(tfidf_array[i][j]) + ", "
        output.write(outline)
    output.write("]")
    output.write('\n')
output.close()

#print (featureslength)    # print number of features
#print (tfidf_arraylength) # print number of products
