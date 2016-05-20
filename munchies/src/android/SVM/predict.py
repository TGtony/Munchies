def predict_func(str):
    from sklearn.externals import joblib
    import os
    filename = os.path.join(os.path.dirname(__file__), 'svm_model.pk1')
    classification_model = joblib.load(filename)  # load SVM model

    pred = [[]]
    for i in str:
        pred[0].append(i)  # builds prediction vector from string

    result = classification_model.predict_proba(pred)[0]  # calculates probability

    sorted_results = list(
        map(lambda x: x[0], sorted(zip(classification_model.classes_, result), key=lambda x: x[1])))  # sort

    list_of_asin = ""
    for asin in sorted_results[:50]:  # top 50
        list_of_asin = list_of_asin + asin + " "  # store top 50 asin into 1 string separated by whitespaces

    return list_of_asin


if __name__ == '__main__':
    predict_func()
