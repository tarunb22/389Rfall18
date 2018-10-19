Writeup 7 - Forensics I
======

Name: Tarun Balachander
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tarun Balachander

## Assignment 7 writeup

### Part 1 (40 pts)

1. The file is a JPEG

2. I looked at exiftool of the image and put the gps data 41°53'54.87"N 87°37'22.53"W into google.
This building is the John Hancock Center in Chicago, Illinois.

3. 2018:08:22 11:33:24

4. iPhone 8

5. 539.5 m above sea level.

6. 

CMSC389R-{look_I_f0und_a_string}

Through binwalk: CMSC389R-{abr@cadabra}

### Part 2 (55 pts)
CMSC389R-{dropping_files_is_fun}

I started off this part by running the binary flag which returned the string Where is the flag? I proceeded to perform various analysis tools that we saw in the powerpoints such as objdump and n to see various binary information of the code. I looked at different ways to perform objdump such as -a or -h but found it fairly confusing to properly follow what was happening. The tool that really helped me get pass the binary was performing gdb on the binary file. At first gdb was not to helpful as I was not to properly look into registers and in general it was not helpful. Through searching online I found the command disas /m main which really helped me make progress. I saw that it was moving a lot of hexadecimal values and when I ran all of them through a hexadecimal to ascii converter I got the clue /tmp/.stego. Next I went to my /tmp/ folder within  kali and performed ls -a to see all files within the folder and saw .stego which after a file .stego call saw it was a data file. I performed normal Forensics tools such as strings and exiftool but the one that yielded results was binwalk which I saw a jpeg file. I used the command binwalk -D 'jpeg image:jpeg' .stego which then extracted the jpeg properly for me. First I used xdg-open on the image and saw it was a picture of a stegosaurus. The file name being .stego and the picture lead me to believe I would need to be using steghide extract on this image. After some guessing on what the password was the word stegosaurus worked which created a file called flag which a simple cat flag gave me the flag CMSC389R-{dropping_files_is_fun}.
