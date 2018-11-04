#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

currByte = 8

timestamp = struct.unpack("<L", data[currByte:currByte + 4])
currByte += 4

author = struct.unpack("<8s", data[currByte:currByte + 8])
currByte += 8

sectCount = struct.unpack("<L", data[currByte:currByte + 4])
currByte += 4

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("Timestamp: " + str(timestamp))
print("Author: " + str(author))
print("Section Count: " + str(sectCount))
print("CurrByte: " + str(currByte))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
i = 0
while i  < 11:
    i += 1
    stype,slen = struct.unpack("<LL", data[currByte:currByte + 8])
    currByte += 8
    print("Section: " + str(i))
    print("stype: " + str(stype))
    print("slen: " + str(slen))
    if stype == 9:
        print("9 - ASCII")
        sdata = struct.unpack("<" + str(slen) + "s", data[currByte: currByte + slen])
        print(sdata)
        currByte += slen
    elif stype == 5:
        print("5 - WORDS")
        num = int(slen/4)
        j = 0
        while j < num:
            sdata = struct.unpack("<L", data[currByte:currByte + 4])
            print(sdata[0], end = '')
            currByte += 4
            j += 1
        print()
    elif stype == 6:
        print("6 - COORDS")
        sdata = struct.unpack("<dd", data[currByte: currByte+16])
        print(sdata)
        currByte += 16
    elif stype == 7:
        print("7 - REFERENCE")
        sdata = struct.unpack("<L", data[currByte:currByte + 4])
        currByte += 4
        print(sdata)
    elif stype == 1:
        print("1 - PNG")
        file = open('img.png', 'w')
        raw = data[currByte:currByte + slen]
        magic =  ('0x89', '0x50', '0x4e', '0x47', '0x0d', '0x0a', '0x1a', '0x0a')
        total = ''.join(magic) + str(raw)
        file.write(total)
        currByte += slen
    elif stype == 2:
        print("2 - DWORDS")
        num = int(slen/8)
        j = 0
        while j < num:
            sdata = struct.unpack("<q", data[currByte:currByte + 8])
            print(sdata[0], end = '')
            currByte += 8
            j += 1
        print()
