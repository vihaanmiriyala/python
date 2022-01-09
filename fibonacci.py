
previous_number = 0
current_number = 1

for i in range(10):
    temp = current_number
    current_number = previous_number + current_number
    previous_number = temp
    print(current_number)