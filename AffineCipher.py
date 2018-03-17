# Affine Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import sys, cryptomath, random
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front


def main():
    myMessage = """hello"""
    myKey = 96
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def encryptMessage(message, key):
    keyA, keyB = getKeyParts(key)
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # just append this symbol unencrypted
    return ciphertext

def decryptMessage(message, key):
    keyA, keyB = getKeyParts(key)
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext

# If affineCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()

