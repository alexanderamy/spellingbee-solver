def cleaner(letters):
    letters = ''.join([letter.lower() for letter in letters if letter.isalpha()])
    return letters
    