# Michael Gairson
# Reference https://www.geeksforgeeks.org/introduction-to-merkle-tree/
# Reference https://github.com/droid76/Merkle-Tree
#import Tkinter, tkFileDialog

import hashlib
import os

# Caluclates the hash value of the given files 
# Using SHA 1 
def fileHash(filename):
    hasher = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(-1)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

# Calaculates the top hash for the markle hash tree used for list of files
def merkleTree(files):
    hashes = [fileHash(file) for file in files]
    while len(hashes) > 1:
        hashes = [hashlib.sha1(hashes[i].encode('utf-8') + hashes[i+1].encode('utf-8')).hexdigest() for i in range(0, len(hashes), 2)]
    return hashes[0]

# file path
files = [] 

# Used to input the give text file used for hashing
# input from user
path = input("Enter the path for the files: ")
for f in os.listdir("."):
    if f.endswith('.txt'):
        files.append(f)

# GUI File PathWay 
#root = Tkinter.TK()
#files = tkFileDialog.askopenfilenames(parent=root, tile='Choose a File')


# calling the hash function
topHash = merkleTree(files)
print('Top hash:', topHash)


# Proving that the hash is different when a file is modified
#
os.system('echo "This is me changing the hash file" >> txt1.txt')
compTop = merkleTree(files)
print('New top hash:', compTop)