MACHINE LEARNING

1. Calculate tfidf & build model
    - Done by using tfidfandsvm.py
        - Takes as input top300.txt & chip_product_adjectives.txt
        - top300.txt (top 300 adjectives with best overall tfidf score, taken from after calculating tfidf)
        - chip_product_adjectives.txt (the adjectives of reviews)
        - Corpus is all reviews, Each individual product is a document
        - Tf-idf is done using scikit-learns' tfidfvectorizer
        - Output of tfidfvectorizer is a matrix, each row is 1 product, each column is 1 adjective.
        - Delete all other columns that are not of the top 300 adjectives
        - Feed tfidf matrix into scikit-learn's SVM classification (SVC)
        - Save model to svm_model.pk1 files
        - Output features_list.txt
            - Used to determine indices for prediction vector

2. Prediction
    - Done by using predict.py
        - Used by the website and android app
        - Takes as input a string of size 300 made up of 1s and 0s
        - String is converted into a prediction vector of size 300
        - A 1 in an index means that adjective is chosen, a 0 means that adjective isn't chosen
        - prediction vector is then passed into classification model
        - Model computates the probability of each product matching the vector.
        - Probability is then sorted and returns top 50 results.
