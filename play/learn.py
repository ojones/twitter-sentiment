import pickle, json, os


def get_saved_classifier():
    myurl = "https://s3-us-west-2.amazonaws.com/ozclassifiers/web_classifier.p"
    import urllib
    opener = urllib.URLopener()
    myfile = opener.open(myurl)
    clf = pickle.load(myfile)
    return clf

def get_classifications(tweets):
    print('tweets')
    print(tweets)

    print('start retreiving')
    classifier = get_saved_classifier()

    print("classifications: ")
    classifications = classifier.predict(tweets).tolist()
    print(classifications)

    return classifications

if __name__ == '__main__':
    print(get_saved_classifier())
