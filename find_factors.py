# find factors of a number other than 1 and itself
# a factor is a number that is divisible by that number

input_number = 18

for i in range(2, round(input_number / 2)):
    if (input_number / i).is_integer():
        print(i)





