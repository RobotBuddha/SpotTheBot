def get_feature(user):
	last_digits = user.screen_name[-8:]

	if last_digits.isnumeric():
		return 1
	else:
		return 0

