import itertools


ciphertext = "qhcyrjxurstxzzkoamazzxerylpqajehdrymiwazzxnvkdwablttzyeqhcyrxhztklmprymgqanalrrgdhcfycrifcwpiyqagnvkdwablyhtq"
keylength = 5
symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
res = itertools.permutations(symbols, keylength)

plaintext = ""
for guess in res:
    while res < len(ciphertext):
        res = res ++ res


while not "the" in plaintext:

