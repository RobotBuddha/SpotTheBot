import nltk
import cPickle as pickle
import random

from nltk import NaiveBayesClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode

import feature_builder

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = float(choice_votes) / len(votes)
        return conf


def extract_features(username):
    features = {}
    feature_v = feature_builder.calculateFeatureVector(username)

    for i in range(len(feature_v)):
        features[i] = feature_v[i]

    return features

pickle.DEFAULT_PROTOCOL = 2


data = open("put-your-data-here", 'r')

featuresets = []

for datapoint in data:
  datapoint = datapoint.split(',')
  feature_vector = extract_features(datapoint[0])
  featuresets.append((feature_vector, datapoint[1].strip()))

random.shuffle(featuresets)


training_set = featuresets[3000:]
testing_set = featuresets[:3000]

#print training_set

#MultinomialNB
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
save_classifier = open("pickled_algos/MNB_classifier.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

#BernoulliNB
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
save_classifier = open("pickled_algos/BernoulliNB_classifier.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

#LogisticRegression
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
save_classifier = open("pickled_algos/LogisticRegression_classifier.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

#LinearSVC
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
save_classifier = open("pickled_algos/LinearSVC_classifier.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

#SGDClassifier
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
save_classifier = open("pickled_algos/SGDC_classifier.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()


print "MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100
print "BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100
print "LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100
print "LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100
print "SGDC_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100

voted_classifier = VoteClassifier(
                                  SGDClassifier_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  LinearSVC_classifier)

print "voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100