# makes sentence uppercase

sentence_prompt = input("Enter your sentence: ").upper()
print(sentence_prompt)

# counts how many words are in the sentence

paragraph_count = len(input("Enter your paragraph: ").split())
print(f"There are {paragraph_count} words in your paragraph")

# checks if there are only numbers 

digit_checker = input("Enter only numbers: ").isnumeric()
print(digit_checker)

# replaces the letter "a" with the letter "o"

letter_replace = input("Enter your sentence: ").replace("a", "o")
print(letter_replace)

# gets the users initials from their full name

full_name = input("Enter your first and last name: ").split()
print(f"Your initials are: {full_name[0][0].upper()}.{full_name[1][0].upper()}.")

# gets the lenght of the users sentence

length = input("Enter your sentence: ")
print(len(length))

