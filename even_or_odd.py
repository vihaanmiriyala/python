# Find a given number is divisible by 2 or not

userInput = input("What is your number : ")

if int(userInput) % 2 == 0:
    print(userInput + " is an even number")
else:
    print(userInput + " is an odd number")