import cPickle as pickle

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

    #if feature_v != False:
    for i in range(len(feature_v)):
        features[i] = feature_v[i]
    #else:
    #    return False
    return features

# Classifiers

classifier_f = open("pickled_algos/MNB_classifier.pickle", "rb")
MNB_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open("pickled_algos/BernoulliNB_classifier.pickle", "rb")
BernoulliNB_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open("pickled_algos/LogisticRegression_classifier.pickle", "rb")
LogisticRegression_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open("pickled_algos/LinearSVC_classifier.pickle", "rb")
LinearSVC_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open("pickled_algos/SGDC_classifier.pickle", "rb")
SGDClassifier_classifier = pickle.load(classifier_f)
classifier_f.close()

voted_classifier = VoteClassifier(
                                  SGDClassifier_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  LinearSVC_classifier)


def testAccount(username):
	features = extract_features(username)

# 	print "Vector values (Human -> 0, Bot -> 1)"
# 	print "Whether the account has tweeted at all:             ", str(features[0])
# 	print "How similar the account's tweets are to each other: ", str(features[1])
# 	print "Whether the account tweets in a scheduled pattern:  ", str(features[2])
# 	print "Proportion of tweets that contain links:            ", str(features[3])
# 	print "Frequency of posting tweets:                        ", str(features[4])
# 	print "Proportion of tweets that are just single links:    ", str(features[5])
# 	print "Frequency of common clickbait phrases used:         ", str(features[6])
# 	print "Ratio of friends to followers:                      ", str(features[7])
# 	print "Whether the account is verified:                    ", str(features[8])
# 	print "Result:",

	if max(features.values())==0:
		return "No such user."

	if features[8] == 0:
		return ('real', 1.0)

	return voted_classifier.classify(features), voted_classifier.confidence(features)

#Feature vector = 0) Whether it has tweeted
#                 1) Similar tweets
#                 2) Scheduled pattern
#                 3) Proportion of links
#                 4) How many tweets per day
#                 5) Proportion of solo links
#                 6) Clickbait phrases
#                 7) Friends to followers ratio
#                 8) Verified account
