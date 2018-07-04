# BEGINNING OF PYTHON EXTERNAL FUNCTIONS (functions.py) 

from textblob import TextBlob

# This function uses Python's "textblob" module to "blob" together the string from the username that the user wants to register. It then uses "sentiment.polarity" to determine the sentiment of the username (on scale of -1...1, -1 is inappropriate, 1 is good),
def input_sentiment(attempted_username):
	attempted_sentiment = TextBlob(attempted_username)

	sentiment_return = attempted_sentiment.sentiment.polarity
	return sentiment_return

# This function checks if the attempted email that the user wants to register is fine by making sure that there is both an "@" symbol and "." in the email string. Also, it checks that there are no restricted characters in the email string.
def crosscheck_email(attempted_email):
	dec_list = []
	attempted_email = str(attempted_email)
	at_symbol = attempted_email.find("@")
	period_symbol = attempted_email.find(".")

	if at_symbol > 0 and period_symbol > 0:
		email_status_string = "Success."

		for char in attempted_email:
			char = ord(char)

			if char <= 45 or char == 47:
				dec_list.append(char)

			elif char >= 58 and char <= 63:
				dec_list.append(char)

			elif char >= 91 and char <= 96:
				dec_list.append(char)

			elif char >= 123:
				dec_list.append(char)

		if not dec_list:
			email_status_string = "Success."
			return email_status_string

		else:
			email_status_string = "Email does not appear to be a valid address. Please try using a different email."
			return email_status_string

	else: 
		email_status_string = "Email does not appear to be a valid address. Please try using a different email."
		return email_status_string

# This function takes in the string of each of the input fields and counts the number of characters in them. In "app.py" we will use this count to see whether or not the input by the user is too short.
def character_counter(attempt):
	counter = 0

	for char in attempt:
		counter += 1
	return counter

# END OF PYTHON EXTERNAL FUNCTIONS (functions.py)


