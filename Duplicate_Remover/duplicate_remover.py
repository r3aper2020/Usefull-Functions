import hashlib
import os
import sys
import yaml

config = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)

path = config["File_Path"]
# from sets import Set

def read_chunk(fobj, chunk_size = 2048):
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def remove_duplicates(dir, hashfun = hashlib.sha512):
    unique = set()
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        if os.path.isfile(filepath):
            hashobj = hashfun()
            for chunk in read_chunk(open(filepath,'rb')):
                hashobj.update(chunk)
                # the size of the hashobj is constant
                # print "hashfun: ", hashfun.__sizeof__()
            hashfile = hashobj.hexdigest()
            if hashfile not in unique:
                unique.add(hashfile)
            else: 
                os.remove(filepath)

try:
    ImageDir = config["Images_Path"]
    hashfun = hashlib.sha256
    remove_duplicates(ImageDir, hashfun)
except:
    print("[Error]: Path '{}' Doesn't Exist".format(ImageDir))