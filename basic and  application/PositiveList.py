from simplecrypt import decrypt, DecryptionException

with open("/home/valentine/Downloads/encrypted.bin", "rb") as inp, open('/home/valentine/Downloads/passwords.txt') as pas:
    encrypted = inp.read()
    decrypted = ''
    for line in pas:
        line = line.strip()
        try:
            decrypted = decrypt(line, encrypted).decode('utf8')
        except DecryptionException:
            pass
print(decrypted)

