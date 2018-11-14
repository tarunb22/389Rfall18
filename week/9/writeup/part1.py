#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r').read().splitlines()
hashes = open("../hashes", 'r').read().splitlines()
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
    for word in wordlist:
        h_hash = str(hashlib.sha512((salt + word).encode()).hexdigest())
        for hash in hashes:
            if hash == h_hash:
                print(salt + " " + word)
