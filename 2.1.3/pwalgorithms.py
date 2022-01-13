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
            if passphrase is password:
                return True, guesses
    return False, guesses
