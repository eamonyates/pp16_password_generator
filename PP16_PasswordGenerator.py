import random, string


def password_gen():
	
	weak_pass = string.ascii_lowercase
	strong_pass = string.ascii_letters + string.digits + string.punctuation

	while True:
		try:
			pass_length = int(input("How many characters do you want in your password: "))
			if pass_length < 8:
				print("Your password must be over 8 characters in length")
				continue
		except ValueError:
			print ("You must enter a number")
		else:
			break

	while True:
		try:
			user_choice = str(input("Do you want a weak or strong password: "))
			if user_choice.lower() == "weak":
				password = ''.join(random.sample(weak_pass, pass_length))
			elif user_choice.lower() == "strong":
				password = ''.join(random.sample(strong_pass, pass_length))
			else: 
				print ("You must enter either weak or strong")
				continue
		except ValueError: 
			print ("You must enter either weak or strong")
		else:
			break

	print (password)


if __name__ == "__main__":
	password_gen()
