def encrypt_caesar(plaintext):
    ciphertext = ""
    for i in plaintext:
        if (ord(i) + 3 > ord("Z")) and (ord(i) + 3 < ord("a")):
            ciphertext += chr(ord(i)+3-26)
        else:
            if ord(i) + 3 > ord("z"):
                ciphertext += chr(ord(i) + 3 - 26)
            else:
                ciphertext += chr(ord(i) + 3)
    return ciphertext
primer = input()
primer = encrypt_caesar(primer)
print(primer)


def decrypt_caesar(ciphertext):
    plaintext = ""
    for i in ciphertext:
        if (ord(i) - 3 < ord("a")) and (ord(i) - 3 > ord("Z")):
            plaintext += chr(ord(i) - 3 + 26)
        else:
            if ord(i) - 3 < ord("A"):
                plaintext += chr(ord(i) - 3 + 26)
            else:
                plaintext += chr(ord(i) - 3)
    return plaintext
primer2 = input()
print(decrypt_caesar(primer2))
