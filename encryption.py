import os
import pickle


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
            with open(textFile + ".cd", 'rb') as file:
                pickle.dump(content, file)
            os.remove(textFile)


def decrypt():
    os.chdir(cwd)
    os.chdir('journals')
    folders = os.listdir()
    for folder in folders:
        os.chdir(folder)
        text_files = os.listdir()
        for textFile in text_files:
            with open(textFile, 'rb') as file:
                content = pickle.load(file)
            with open(textFile + ".txt") as file:
                file.write(content)
