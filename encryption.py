import os
import random
import pickle

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

cwd = str(os.getcwd())

def caeser(text,key):
    ciphertext = ""
    for c in text.upper():
        if c.isalpha(): ciphertext += I2L[(L2I[c] + key)%26 ]
        else: ciphertext += c

    return ciphertext

def uncaeser(text,key):
    plaintext = ""
    for c in text.upper():
        if c.isalpha(): plaintext += I2L[(L2I[c] - key) %26]
        else: plaintext += c
    return plaintext


def encrypt():
    os.chdir(cwd)
    os.chdir('journals')
    folders = os.listdir()
    for folder in folders:
        os.chdir(folder)
        text_files = os.listdir()
        for textFile in text_files:
            with open(textFile) as file:
                content = file.read()
            key = random.randint(11,99)
            content_to_write = caeser(content,key)
            with open(textFile,'w') as file:
                file.write(content_to_write)
                file.write("\nKEY:{}".format(key))
            with open(textFile) as file:
                content_to_be_rewritten = file.read()
            with open(textFile,'wb') as file:
                pickle.dump(content_to_be_rewritten,file)

def decrypt():
    os.chdir(cwd)
    os.chdir('journals')
    folders = os.listdir()
    for folder in folders:
        os.chdir(folder)
        text_files = os.listdir()
        for textFile in text_files:
            with open(textFile,'rb') as file:
                content = pickle.load(file)
            key = int(content[-2:])
            content_to_rewrite = uncaeser(content,key)
            content_to_rewrite = content_to_rewrite[:-6]
            with open(textFile,'w') as file:
                file.write(content_to_rewrite)




