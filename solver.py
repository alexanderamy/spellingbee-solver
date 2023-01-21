from reader import reader

ALPHABET = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
PATH = 'data\words_alpha.txt'
WORDS = reader(PATH)

def solver(letters):
    center = letters[0]
    letters = set(letters)
    illegal_letters = ALPHABET - letters

    solutions = []

    for word in WORDS:
        len_word = len(word)
        if len_word > 3:
            i = 0
            while i < len_word:
                if word[i] in illegal_letters:
                    break
                else:
                    i += 1
            if i == len_word:
                if center in word:
                    solutions.append(word)

    return solutions
    