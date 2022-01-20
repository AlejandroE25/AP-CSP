# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
    words = []
    dictionary_file = open("dictionary.txt")
    for line in dictionary_file:
        # store word, omitting trailing new-line
        words.append(line[:-1])
    dictionary_file.close()
    return words


guesses = 0


# analyze a one-word password
def one_word(password):
    words = get_dictionary()
    global guesses
    # get each word from the dictionary file
    for w in words:
        guesses += 1
        if w == password:
            return True, guesses
    return False, guesses


def two_words(password):
    words = get_dictionary()
    global guesses
    # get each word from the dictionary file
    for w1 in words:
        for w2 in words:
            guesses += 1
            passphrase = w1 + w2
            if passphrase == password:
                return True, guesses
    return False, guesses


numbers = ['1', '2', '3', '4', '5', '5', '6', '7', '8', '9', '0']


def twoWordsAndADigit(password):
    words = get_dictionary()
    global guesses
    for w in words:
        for sw in words:
            for n in numbers:
                guesses += 1
                phrase1 = n + w + sw
                phrase2 = w + sw + n

                if phrase1 == password:
                    return True, guesses
                if phrase2 == password:
                    return True, guesses + 1
    return False, guesses
