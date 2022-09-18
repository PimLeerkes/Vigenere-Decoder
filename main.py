import itertools


#decrypts the ciphertext with a certain key:
def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)
    return plaintext


#checks if plaintext makes sense:
def sensible(plaintext, dictionary):
    if "the" in plaintext:
        count = 0
        for word in dictionary:
            if word in str.lower(plaintext):
                count = count + 1
        if count > 2:
            return True


if __name__ == "__main__":
    #asks user for ciphertext and keylength:
    ciphertext = input("Fill in the ciphertext: ")
    keylength = int(input("Fill in the keylength: "))

    #creates the list of possible keys:
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if str.isupper(ciphertext):
        for index in range(len(symbols)):
            symbols[index] = str.upper(symbols[index])
    keys = itertools.product(symbols, repeat=keylength)

    #creating list of possible words to be in the plaintext:
    dictionary = open("words.txt", "r")
    dictionary = dictionary.readlines()
    res = []
    for sub in dictionary:
        word = sub.replace("\n", "")
        if len(word) > 4:
            res.append(word)

    #iterating over all keys:
    for key in keys:
        plaintext = decrypt(ciphertext, key)
        if sensible(plaintext, res):
           print("plaintext: " + plaintext + ", key: " + str(key))
