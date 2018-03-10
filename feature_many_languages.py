def get_feature(tweets):
	languages = []
	for tweet in tweets:
		lan = tweet.lang
		if lan not in languages:
			languages.append(lan)

	print languages

	if len(languages) > 3:
		return 1
	else:
		return 0