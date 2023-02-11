# Taking User inpur and store them is a list

text = input("Enter a text of your choice: ")
letters = []

# Converting input into same caps

text = text.lower()

# Take three letter input and append them in list

letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the third letter: ").lower())
