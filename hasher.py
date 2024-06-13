#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import argparse
import os
import sys
from huepy import *

parser = argparse.ArgumentParser()
parser.add_argument('-p', help='password to hash', dest='passw')
parser.add_argument('-f', help='hash function', dest='function')
parser.add_argument('-i', help='interactive mode', action='store_true', dest='interactive')
args = parser.parse_args()

os.system('clear')

def hash_password(password, hash_type):
    if hash_type == 'md5':
        return hashlib.md5(password).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(password).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(password).hexdigest()
    elif hash_type == 'sha384':
        return hashlib.sha384(password).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(password).hexdigest()
    else:
        return None

if args.interactive:
    password = input(que("Enter the password to hash: "))
    print(que("Choose the hash function:"))
    print(info("1. md5"))
    print(info("2. sha1"))
    print(info("3. sha256"))
    print(info("4. sha384"))
    print(info("5. sha512"))
    choice = input(que("Enter the number corresponding to your choice: "))
    hash_type = {
        '1': 'md5',
        '2': 'sha1',
        '3': 'sha256',
        '4': 'sha384',
        '5': 'sha512'
    }.get(choice)

    if not hash_type:
        print(bad('Invalid choice!'))
        sys.exit()
else:
    password = args.passw
    hash_type = args.function

if not password or not hash_type:
    print(bad('Password and hash type are required!'))
    sys.exit()

passw = bytes(password, 'utf-8')
hashed_password = hash_password(passw, hash_type)

if hashed_password:
    print(good(f"\n{hash_type.upper()}: {hashed_password}"))
else:
    print(bad('Invalid Hash Type!!'))
    print(info('Supported Hashes : md5/sha1/sha256/sha384/sha512'))
