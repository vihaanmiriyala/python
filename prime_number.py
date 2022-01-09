#a prime number is a number that has factors of 1 and itself

input_number = 21
is_prime = True


for i in range(2, input_number): #loop tells what numbers have to be pecercented by input number, i is a variable
    if input_number % i == 0:
        #this tells the computer that if input_number percented by i equals to 0,the number will not be prime
        is_prime = False #this assigns the value of the variable is_prime, "False"
        break #break command

print(is_prime) #this prints is_prime