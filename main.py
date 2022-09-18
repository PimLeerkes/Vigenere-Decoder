import itertools

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length])
        plaintext += chr(value + 65)
        print(value + 65)
    return plaintext


def sensible(plaintext):
    if "THE" in plaintext:
        return True


if __name__ == "__main__":
    ciphertext = "qhcyrjxurstxzzkoamazzxerylpqajehdrymiwazzxnvkdwablttzyeqhcyrxhztklmprymgqanalrrgdhcfycrifcwpiyqagnvkdwablyhtq"
    keylength = 5
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    keys = itertools.permutations(symbols, keylength)

    for key in keys:
        plaintext = decrypt(ciphertext, "STING")
        print(plaintext)
        if sensible(plaintext):
           print(plaintext)


