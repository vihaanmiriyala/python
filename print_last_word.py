sentence = "Vihaan likes games"
last_word = ""

for i in range(len(sentence)):
    current_letter = sentence[len(sentence)-i-1]

    if current_letter == " ":
        break
    last_word = current_letter + last_word

print(last_word)