# Taking User inpur and store them is a list

text = input("Enter a text of your choice: ")
letters = []

# Converting input into same caps

text = text.lower()

# Take three letter input and append them in list

letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the third letter: ").lower())

print("\n")
print("LETTER REPETITIONS")

#  It will show number of letter repetation in that text

letter_repetition1 = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print(f"We have found the letter '{letters[0]}' repeated {letter_repetition1} times")
print(f"We have found the letter '{letters[1]}' repeated {letter_repetition2} times")
print(f"We have found the letter '{letters[2]}' repeated {letter_repetition3} times")

print("\n")
print("NUMBER OF WORDS")

# Calculate the number of words in the sentence.

words = text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("FIRST AND LAST LETTERS")

# Shows the first and last letter of the text

first_letter = text[0]
last_letter = text[-1]
print(f"The initial letter is '{first_letter}', the final letter is '{last_letter}'")

print("\n")
print("INVERTED TEXT")

# Shows the invered text

words.reverse()
inverted_text = ' '.join(words)
print(f"If we order your text backwards it will say '{inverted_text}'")

print("\n")
print("LOOKING FOR THE WORD PYTHON")

# Checks if word python in the text of not

is_python = 'python' in text
dic = {True: "was", False: "was not"}

print(f"The word 'Python' {dic[is_python]} found in the text")