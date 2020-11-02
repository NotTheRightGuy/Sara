import os
import pickle

cwd = os.getcwd()

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
            with open(textFile[:-3]+"cd" , 'wb') as file:
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
            with open(textFile[:-2] +"txt",'w') as file:
                file.write(content)
            os.remove(textFile)
