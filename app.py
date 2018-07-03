# BEGINNING OF MAIN PYTHON APPLICATION (app.py)


# Code Citation: Welcome to Flask
# URL: http://flask.pocoo.org/docs/0.12/
# Author: Flask
# Accessed on: 4/4/18
# Purpose of code: I am importing the Flask framework, which will allow me to perform web development with Python more efficiently.
from flask import Flask, render_template, request, url_for, redirect


# *API USED IS BELOW*
# Code Citation: Semantics 3 API Documentation
# URL: https://docs.semantics3.com/reference#keyword-api-1
# Author: Semantics3
# Accessed on: 4/3/18
# Purpose of code: I am importing the Semantics3 module, which is an API that will allow the user to search up various products on the internet by keyword.
from semantics3 import Products


# Here I am importing the JSON module, which will allow me to work with the JSON response from the Semantics3 API later.
import json

# Here I am importing the "decimal" module, which will help me find the average price of the search later.
from decimal import Decimal

# Here I am importing the "textblob" module which will help me to find the sentiment of the string by first "globbing" the string together.
from textblob import TextBlob

# Here I am importing all of the external functions from my "functions.py" file, which I will use later.
from functions import input_sentiment, crosscheck_email, character_counter


# Code Citation: Semantics 3 API Documentation
# URL: https://docs.semantics3.com/reference#keyword-api-1
# Author: Semantics3
# Accessed on: 4/3/18
# Purpose of code: The API key and secret will be passed along with the request, allowing me to access a response.
sem3 = Products(
	api_key = "SEM3D4E92E7495711694BF8E16042CB789B7",
	api_secret = "NjJmYWI3ZDQyZGZmMzk4ZjkwNjMzNWUxZjM0YjU0ODQ"
)


# I defined all of the global variables below.
user_list = []

email_list = []

password_list = []

price_list = []

username = ""

return_user = ""

return_item_num = ""

return_image = ""

return_name = ""

return_url = ""

return_price = ""

return_product_brand = ""

return_product_upc = ""

return_product_other_availability = ""

return_product_other_seller = ""

return_product_other_marketplace_name = ""

login_state = ""

message = ""

username_cart_list = []

image_cart_list = []

name_cart_list = []

price_cart_list = []

brand_cart_list = []

model_cart_list = []

location_cart_list = []

upc_cart_list = []

condition_cart_list = []

availability_cart_list = []

seller_cart_list = []

marketplace_cart_list = []

sku_cart_list = []

url_cart_list = []


# BEGINNING OF FLASK APPLICATION
app = Flask(__name__)



# Here I am defining the "app.route" of the homepage, so that when the URL is changed to the homepage, the "home.html" file will be rendered.
@app.route('/')
def index():
	return render_template('home.html')



# When the URL is changed to "/register", the "register.html" file will be rendered. I have also defined the HTTP methods that we will use.
@app.route('/register', methods=["GET","POST"])
# Here I defined the function "user_data()", which will allow people to register for Cartify. Their respective account details will be saved to several lists.
def user_data():
	try:
		# If the user clicks the "register" button, continue.
		if request.method=="POST":
			# Requesting the input strings from the user.
			global username
			username = request.form['uregister']

			email = request.form['eregister']

			password = request.form['pregister']

			confirm_password = request.form['pregisterr']

			global user_list
			global email_list

			# If no string exists (user left any of the fields empty), return an error.
			if not username or not email or not password or not confirm_password:
				global message
				message = "Please make sure to fill in all boxes."
				return render_template("register.html", message=message)

			# If all of the text fields are filled in, continue.
			else: 
				message = ""

				# If the username is already in the "user_list", return an error.
				if username in user_list:
					message = "Sorry, username is already taken."
					return render_template("register.html", message=message)

				# If the username is not already in "user_list", continue.
				else: 
					username_error_message = ""

					# If the email is already in "email_list", return an error.
					if email in email_list:
						message = "Sorry, email is already taken."
					
					# If the email is not already in "email_list", continue.
					else:
						email_error_message = ""

						# If the username and/or email are taken, return an error. If not, continue.
						if username_error_message == "Sorry, username is already taken." or email_error_message == "Sorry, email is already taken.":
							register_status = False
							message = "Sorry, your login details are already already taken."
							return render_template("register.html", message=message)

						elif username_error_message == "Sorry, username is already taken." and email_error_message == "Sorry, email is already taken.":
							register_status = False
							message = "Sorry, both the username and email are already taken. Please try again."
							return render_template("register.html", message=message)

						elif username_error_message == "" and email_error_message == "":
							
							# Calling the input_sentiment function to find whether or not the user's attempted login details are appropriate.
							try_input_username = input_sentiment(username)
							try_input_email = input_sentiment(email)

							total_sentiment_number = try_input_username + try_input_email

							# If the sentiment of the username is less than 0 (inappropriate), return an error.
							if try_input_username < 0.0:
								message = "It appears that your username is inappropriate for this site. Please change it."
								return render_template("register.html", message=message)

							# If the sentiment of the email is elss than 0 (inappropriate), return an error.
							elif try_input_email < 0.0:
								message = "It appears that your email is inappropriate for this site. Please change it."
								return render_template("register.html", message=message)

							# If the total sentiment is less than 0 (inappropriate), return an error.
							elif total_sentiment_number < 0.0:
								message = "It appears that both your username and email are inappropriate for this site. Please change them."
								return render_template("register.html", message=message)

							# If the sentiment passes the test, continue.
							else:
								# Calling the crosscheck_email function to make sure that the email contains the appropriate characters.
								pass_status_email = crosscheck_email(email)

								# If the email contains the appropriate characters, continue. If not, return an error.
								if pass_status_email == "Success.":

									# If the password is the same as the "repeat password" input, continue. If not, return an error.
									if password == confirm_password:
										
										# Calling the character_counter function to count the number of characters in the attempted username.
										username_length = character_counter(username)

										# If the length of the username is greater than two, continue. If not, return an error.
										if username_length > 2:

											# Calling the character_counter function to count the number of characters in the attempted email.
											email_length = character_counter(email)

											# If the length of the email is greater than or equal to eight, continue. If not, return an error.
											if email_length >= 8:

												# Calling the character_counter function to count the number of characters in the attempted password.
												password_length = character_counter(password)

												# If the length of the password is greater than or equal to four, continue. If not, return an error.
												if password_length >= 4:
													# Append the details to their respective lists if they pass the above tests. If they don't, the process will be stopped and an error will be displayed.
													user_list.append(username)

													email_list.append(email)

													global password_list
													password_list.append(password)

													return redirect(url_for('login_main'))

												else:
													message="Sorry, your password needs to be at least four digits."
													return render_template("register.html", message=message)

											else:
												message = "Sorry, your email needs to be at least eight digits."
												return render_template("register.html", message=message)

										else:
											message = "Sorry, your username needs to be at least three digits."
											return render_template("register.html", message=message)

									else:
										message = "It appears that your passwords are different. Please confirm."
										return render_template("register.html", message=message)

								elif pass_status_email == "Email does not appear to be a valid address. Please try using a different email.":
									message = pass_status_email
									return render_template("register.html", message=message)

								else:
									message = ""
									return render_template("register.html", message=message)

						else:
							message = ""
							return render_template("register.html", message=message)

				return render_template("register.html", message=message)

	# If none of the above works, then an error is defined.
	except Exception as e:
		error ="Something went wrong."
		
	return render_template("register.html")



# Here I am defining the "app.route" of the dashboard, so that when the user is redirrected to the dashboard, it will render the "dashboard.html" file.
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html', username=username)



# When the URL is changed to "/search", the "search-page.html" file will be rendered. I have also defined the HTTP methods that we will use. Images are being provided through the API. 
@app.route('/search', methods=['GET','POST'])
def main_output():
	try: 
		# If the user clicks the search button, continue.
		if request.method == 'POST':

			# Get the string of what is entered into the textbox by the user.
			entered_search = request.form['search']

			# Code Citation: Semantics 3 API Documentation
			# URL: https://docs.semantics3.com/reference#keyword-api-1
			# Author: Semantics3
			# Accessed on: 4/4/18
			# Purpose of code: Will allow me to search the API for the input by the user and get the results.
			sem3.products_field("search", entered_search)
			results = sem3.get_products()


			sem3_list_counter = 0
			sem3_list = []
			try: 
				# For the sem3_id's in the results, append each of them to a list. If it cannot, then return a list with "N/A".
				for id in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_sem3 = results['results'][sem3_list_counter]['sem3_id']

					sem3_list_counter += 1 
					sem3_list.append(product_sem3)

			except Exception as e:
				sem3_list = ["N/A","N/A","N/A","N/A","N/A"]
			

			image_list = []
			image_list_counter = 0
			try:
				# For the images in results, append each of them to a list. If it cannot, then return a list with "N/A". 

# Images are being provided directly through the API. 
				for image in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_image = results['results'][image_list_counter]['images']
					
					# Code Citation: Python tips - How to easily convert a list to a string for display
					# URL: https://www.decalage.info/en/python/print_list
					# Author: Decalage
					# Accessed on: 4/6/18
					# Purpose of code: strip() allows me to remove the brackets and quotation marks from the image URL strings.
					product_image = str(product_image).strip('[]')
					product_image = str(product_image).strip("''")

					# Images are being provided directly through the API. 
					image_list_counter += 1
					image_list.append(product_image)

			except Exception as e:
				image_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the prices in results, append each of them to a list. If it cannot, then return a list with "N/A".
			price_list = []
			price_list_counter = 0
			try: 
				for price in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_price = results['results'][price_list_counter]['price']

					price_list_counter += 1
					price_list.append(product_price)

			except Exception as e:
				price_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the brands in results, append each of them to a list. If it cannot, then return a list with "N/A".
			brand_list = []
			brand_list_counter = 0
			try:
				for brand in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_brand = results['results'][brand_list_counter]['brand']

					brand_list_counter += 1
					brand_list.append(product_brand)

			except Exception as e:
				brand_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the models in results, append each of them to a list. If it cannot, then return a list with "N/A".
			model_list = []
			model_list_counter = 0
			try:
				for model in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_model = results['results'][model_list_counter]['model']

					model_list_counter += 1
					model_list.append(product_model)

			except Exception as e:
				model_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the names in results, append each of them to a list. If it cannot, then return a list with "N/A".
			name_list = []
			name_list_counter = 0
			try:
				for name in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_name = results['results'][name_list_counter]['name']

					name_list_counter += 1
					name_list.append(product_name)

			except Exception as e:
				name_list = ["N/A","N/A","N/A","N/A","N/A"]
				

			# For the geo_locations in results, append each of them to a list. If it cannot, then return a list with "N/A".
			geo_location_list = []
			geo_location_list_counter = 0
			try:
				for geo in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_geo_location = results['results'][geo_location_list_counter]['geo']

					# Code Citation: Python tips - How to easily convert a list to a string for display
					# URL: https://www.decalage.info/en/python/print_list
					# Author: Decalage
					# Accessed on: 4/6/18
					# Purpose of code: strip() allows me to remove the brackets and quotation marks from the image URL strings.
					product_geo_location = str(product_geo_location).strip('[]')
					product_geo_location = str(product_geo_location).strip("''")

					product_geo_location = product_geo_location.upper()
					geo_location_list_counter += 1
					geo_location_list.append(product_geo_location)
			except Exception as e:
				geo_location_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the product_ean's in results, append each of them to a list. If it cannot, then return a list with "N/A".
			ean_list = []
			ean_list_counter = 0
			try:
				for ean in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_ean = results['results'][ean_list_counter]['ean']

					ean_list_counter += 1
					ean_list.append(product_ean)

			except Exception as e:
				ean_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the product_colors in results, append each of them to a list. If it cannot, then return a list with "N/A".
			color_list = []
			color_list_counter = 0
			try:
				for color in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_color = results['results'][color_list_counter]['color']

					color_list_counter += 1
					color_list.append(product_color)

			except Exception as e:
				color_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the UPCs in results, append each of them to a list. If it cannot, then return a list with "N/A".
			upc_list = []
			upc_list_counter = 0
			try:
				for upc in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_upc = results['results'][upc_list_counter]['upc']

					upc_list_counter += 1
					upc_list.append(product_upc)

			except Exception as e:
				upc_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the other_prices in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_price_list = []
			other_price_list_counter = 0
			try:
				for other_price in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_price = results['results'][other_price_list_counter]['sitedetails'][0]['latestoffers'][0]['price']

					other_price_list_counter += 1
					other_price_list.append(product_other_price)
					
			except Exception as e:
				other_price_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the product_conditions in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_condition_list = []
			other_condition_list_counter = 0
			try:
				for other_condition in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_condition = results['results'][other_condition_list_counter]['sitedetails'][0]['latestoffers'][0]['condition']

					other_condition_list_counter += 1
					other_condition_list.append(product_other_condition)

			except Exception as e:
				other_condition_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the product_availabilities in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_availability_list = []
			other_availability_list_counter = 0
			try:
				for other_availability in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_availability = results['results'][other_availability_list_counter]['sitedetails'][0]['latestoffers'][0]['availability']

					other_availability_list_counter += 1
					other_availability_list.append(product_other_availability)

			except Exception as e:
				other_availability_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the product_sellers in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_seller_list = []
			other_seller_list_counter = 0
			try:
				for other_seller in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_seller = results['results'][other_seller_list_counter]['sitedetails'][0]['latestoffers'][0]['seller']

					other_seller_list_counter += 1
					other_seller_list.append(product_other_seller)

			except Exception as e:
				other_seller_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the marketplace_names in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_marketplace_name_list = []
			other_marketplace_name_list_counter = 0
			try: 
				for other_marketplace_name in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_marketplace_name = results['results'][other_marketplace_name_list_counter]['sitedetails'][0]['name']

					other_marketplace_name_list_counter += 1
					other_marketplace_name_list.append(product_other_marketplace_name)
				
			except Exception as e:
				other_marketplace_name_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the SKUs in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_sku_list = []
			other_sku_list_counter = 0
			try:
				for other_sku in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_sku = results['results'][other_sku_list_counter]['sitedetails'][0]['sku']

					other_sku_list_counter += 1
					other_sku_list.append(product_other_sku)
				
			except Exception as e:
				other_sku_list = ["N/A","N/A","N/A","N/A","N/A"]


			# For the URLs in results, append each of them to a list. If it cannot, then return a list with "N/A".
			other_url_list = []
			other_url_list_counter = 0
			try:
				for other_url in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_other_url = results['results'][other_url_list_counter]['sitedetails'][0]['url']

					other_url_list_counter += 1
					other_url_list.append(product_other_url)
				
			except Exception as e:
				other_url_list = ["N/A","N/A","N/A","N/A","N/A"]


			# Try to find the average price of the search. If not, return an error.
			try:
				price_av = 0
				price_av_list = []
				price_av_list_counter = 0
				# Append each of the product prices to a new list.
				for av_price in results:
					# Code Citation: Semantics 3 API Documentation
					# URL: https://docs.semantics3.com/reference#keyword-api-1
					# Author: Semantics3
					# Accessed on: 4/7/18
					# Purpose of code: Allow me to access the JSON response and retrieve the data. 
					product_av_price = results['results'][price_av_list_counter]['price']

					price_av_list_counter +=1
					price_av_list.append(product_av_price)

				for av in price_av_list:

					# Code Citation: JSON encoding and decoding with Python
					# URL: https://pythonspot.com/json-encoding-and-decoding-with-python/
					# Author: Python Tutorials
					# Accessed on: 4/8/18
					# Purpose of code: Allow me to proccess JSON response in order to find the average price of the search.
					num = json.loads(av, parse_float = Decimal)

					price_av += num

				# Find average by dividing by five and rounding.
				price_av_final = price_av/5
				price_av_final = str(round(price_av_final, 2))
				price_av_final = "Average Price: $" + price_av_final
			except Exception as e:
				price_av_final ="Sorry, we could not determine the average price of the search."



		return render_template('search-page.html', 
			output_message = zip(
				image_list,
				price_list,
				brand_list,
				model_list,
				name_list,
				geo_location_list,
				upc_list,
				other_price_list,
				other_condition_list,
				other_availability_list,
				other_seller_list,
				other_marketplace_name_list,
				other_sku_list,
				other_url_list))


	except Exception as e:
		return render_template("search-page.html")



# If the URL is changed to "/login" it will render the "login.html" file. I have also defined the HTTP methods that I will use.
@app.route('/login', methods=['GET','POST'])

# This function will allow the user to access their dashboard if they successfully login.
def login_main():
	error = ""

	try:
		if request.method=="POST":
			# Requesting the string from the username and password textboxes if the "login" button is clicked.
			try_username = request.form['username']
			try_password = request.form['password']

			# If the username and password are in the lists, redirrect the user to the dashboard.
			if try_username in user_list and try_password in password_list:
				username = try_username
				return render_template("dashboard.html",username=username)
			
			# If the email and password are in the lists, redirrect the user to the dashboard.
			elif try_username in email_list and try_password in password_list:
				username = try_username
				return render_template("dashboard.html", username=username)

			# If the above statements fail, return an error.
			else:
				error = "Sorry, either your username or password is incorrect."
				return render_template("login.html", error=error)
		
	except Exception as e:
		error = "Sorry, either your username or password is incorrect."
		return render_template("login.html", error = error)

	return render_template("login.html")



# Here I am defining the "app.route" of "/cart". The following function will be executed when the cart page is opened. I have also defined the HTTP methods of "GET" and "POST".
@app.route('/cart', methods=['GET','POST'])
# This function will append items to the global shopping cart for everyone to see.
def shopping_cart():
	if request.method=='POST':

		if request.form['cart'] == "Add to Global ":
			# Requesting the information of the product if it is added to the 
			image = request.form['image']
			name = request.form['name']
			price = request.form['price']
			product_brand = request.form['brand']
			product_model = request.form['model']
			product_location = request.form['location']
			product_upc = request.form['upc']
			product_condition = request.form['condition']
			product_availability = request.form['availability']
			product_seller = request.form['seller']
			marketplace_name = request.form['marketplace']
			product_sku = request.form['sku']
			product_url = request.form['url']
			
			# Here I am appending the details requested above to a new set of lists.
			global username_cart_list
			username_cart_list.append(username)

			global image_cart_list
			image_cart_list.append(image)

			global name_cart_list
			name_cart_list.append(name)

			global price_cart_list
			price_cart_list.append(price)

			global brand_cart_list
			brand_cart_list.append(product_brand)

			global model_cart_list
			model_cart_list.append(product_model)

			global location_cart_list
			location_cart_list.append(product_location)

			global upc_cart_list
			upc_cart_list.append(product_upc)

			global condition_cart_list
			condition_cart_list.append(product_condition)

			global availability_cart_list
			availability_cart_list.append(product_availability)

			global seller_cart_list
			seller_cart_list.append(product_seller)

			global marketplace_cart_list
			marketplace_cart_list.append(marketplace_name)

			global sku_cart_list
			sku_cart_list.append(product_sku)

			global url_cart_list
			url_cart_list.append(product_url)


		return render_template("cart.html", 
		# Zipping the lists together to make it easier to run it through a "for loop" in the HTML template later.
		output_cart_list = zip(
			username_cart_list,
			image_cart_list,
			name_cart_list,
			price_cart_list,
			brand_cart_list,
			model_cart_list,
			location_cart_list,
			upc_cart_list,
			condition_cart_list,
			availability_cart_list,
			seller_cart_list,
			marketplace_cart_list,
			sku_cart_list,
			url_cart_list)
		)

	else:
		return render_template("cart.html", 
		output_cart_list = zip(
			username_cart_list,
			image_cart_list,
			name_cart_list,
			price_cart_list,
			brand_cart_list,
			model_cart_list,
			location_cart_list,
			upc_cart_list,
			condition_cart_list,
			availability_cart_list,
			seller_cart_list,
			marketplace_cart_list,
			sku_cart_list,
			url_cart_list)
		)

	return render_template("cart.html", 
	output_cart_list = zip(
			username_cart_list,
			image_cart_list,
			name_cart_list,
			price_cart_list,
			brand_cart_list,
			model_cart_list,
			location_cart_list,
			upc_cart_list,
			condition_cart_list,
			availability_cart_list,
			seller_cart_list,
			marketplace_cart_list,
			sku_cart_list,
			url_cart_list)
	)

if __name__ == '__main__':
	app.run(debug=True)

# END OF MAIN PYTHON FILE (app.py)















