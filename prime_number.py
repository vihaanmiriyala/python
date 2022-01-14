

input_number = 1
is_prime = True


for i in range(2, input_number):
    if input_number % i == 0:
        is_prime = False
        break

print(is_prime)