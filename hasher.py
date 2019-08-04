
#!usr/bin/python3
#!-*- coding: utf-8 -*-

# Password Hasher by cybercroc.
# generate hashes from passwords in seconds!!

# import the required libraries.
import hashlib
import argparse
import os
import sys
from huepy import *

# making command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-p', help='password to hash', dest='passw')
parser.add_argument('-f', help='hash function', dest='function')
args = parser.parse_args()

# clear the console.
os.system('clear')

# C O D E  S T A R T

# variables
password = args.passw
hash_type = args.function

# if/else statements.
if hash_type == 'md5':
    print("\nMD5:")
    for i in range(1):
        passw = bytes(password, 'utf-8')
        hashh = hashlib.md5(passw).hexdigest()
        print(good(hashh))

elif hash_type == 'sha1':
    print("\nSHA-1:")
    for i in range(1):
        passw = bytes(password, 'utf-8')
        hashh = hashlib.md5(passw).hexdigest()
        print(good(hashh))

elif hash_type == 'sha256':
    print("\nSHA-256:")
    for i in range(1):
        passw = bytes(password, 'utf-8')
        hashh = hashlib.md5(passw).hexdigest()
        print(good(hashh))

elif hash_type == 'sha384':
    print("\nSHA-384:")
    for i in range(1):
        passw = bytes(password, 'utf-8')
        hashh = hashlib.md5(passw).hexdigest()
        print(good(hashh))

elif hash_type == 'sha512':
    print("\nSHA-512:")
    for i in range(1):
        passw = bytes(password, 'utf-8')
        hashh = hashlib.md5(passw).hexdigest()
        print(good(hashh))


else:
    print()
    print(bad('Invalid Hash Type!!'))
    print(info('Supported Hashes : md5/sha1/sha256/sha384/sha512'))
    sys.exit()

# C O D E  E N D
