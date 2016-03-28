output = open('chips_tfidf.txt', 'w')

corpus = []

def tf_idf_vectorization():
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

    features = tfidf_vectorizer.get_feature_names()
    array = tfidf_matrix.toarray()

    featureslength = len(features)
    arraylength = len(array)

    for i in range(arraylength):
        output.write("[ ")
        for j in range(featureslength):
            outline = str(features[j]) + ": " + str(array[i][j]) + ", "
            output.write(outline)
        output.write("]")
        output.write('\n')
    return

with open('output.txt') as input_file:
    for line in input_file:
        if line[0] != '[':
            if not len(corpus) == 0:
                check_corpus = []
                null = "[]\n"
                corpus_length = len(corpus)
                for i in range(corpus_length):
                    check_corpus.append(null)
                if corpus == check_corpus:
                    for i in range(corpus_length):
                        output.write("[]")
                        output.write('\n')
                else:
                    tf_idf_vectorization()
            corpus.clear()
            output.write(line)
        else:
            corpus.append(line)

if not len(corpus) == 0:
    check_corpus = []
    null = "[]\n"
    corpus_length = len(corpus)
    for i in range(corpus_length):
        check_corpus.append(null)
    if corpus == check_corpus:
        for i in range(corpus_length):
            output.write("[]")
            output.write('\n')
    else:
        tf_idf_vectorization()

input_file.close()
output.close()
