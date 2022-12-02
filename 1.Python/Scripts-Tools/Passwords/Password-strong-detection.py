# Strong Password Detection using regular expression

import re


def strong_pass(Password):

	if re.match(r'([a-zA-Z0-9]).{8,}', Password) is not None:
		print('Strong Password')
	else:
		print('Weak Password')
