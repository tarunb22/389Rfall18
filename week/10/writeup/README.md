Writeup 10 - Crypto II
=====

Name: Tarun Balachander
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tarun Balachander

## Assignment 10 Writeup

### Part 1 (70 Pts)
I could not properly complete part 1 as I was unable to get md5py.py to run as my laptop was not running python 2 no matter what I did, I have python 3 installed but a lot of troubleshooting with did not help in properly getting python2 to run for that. From my understanding what I had to do was pad my message x80 and a variable amount of x00 and a malicious msg in order to get the flag. I tried to brute force place these messages within the server but was not having success.

### Part 2 (30 Pts)
gpg --gen-key can be used to generate a key.
gpg --import pubkey.asc can be used to import a friends key
gpg -e -u "your name" -r "their name" msg.txt will generate msg.txt.gpg
A website like iGolder offers pgp encryption/decryption aswell.
