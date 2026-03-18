def hello(name):
	print(f"hello in arvix {name}")

def check_password(password):
	secret = "123"
	return password == secret

def calculator():
	number1 = input("inter the first number: ")
	number2 = input("inter the second numbef: ")
	equals  = int(number1) + int(number2)
	print(f"{number1} + {number2} = {equals}")


hello(input("what is your name: "))

user_password = input("inter your password: ")

if check_password(user_password):
	print("The password is correct ✅")
	calculator()
		
else:
	print("Incorrect password ❌")
