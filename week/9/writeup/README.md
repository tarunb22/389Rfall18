Writeup 9 - Crypto I
=====

Name: Tarun Balachander
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tarun Balachander

## Assignment 9 Writeup

### Part 1 (60 Pts)

For part 1 the goal was to compare the created hash w/ hexdigest against the one within the hashes file. This was fairly easy other than converting the salt and word into a hash as it took some time to figure out it needed to be encoded as well as the proper order for it. Other than that it was fairly simple to print the salt + hash which I did and got:
k neptune
m jordan
p pizza
u loveyou

### Part 2 (40 Pts)

CMSC389R-{H4sh-5l!ngInG-h@sH3r}

This part was fairly simple as basically all I had to do was make sure I was reading and splitting the input from the trivia service correctly. I first had to handle and split the welcome message correctly in order to read the line that told you the hash encoding type and the str to hash. Basically I was seeing what type of encoding it was whether it was sha256, md5, or any other I was continuously running my code to see what the next one was and accounting for that. I figured the same line would be continuously repeated (Find me the _ hash of _ >>>) but when you got it right it actually wrote correct so I had to change the end of my code to remove that word so that the list remained in the same format so that my code would work properly. Once I got the template down it was just a matter of running the code and adding the new hash that I had not yet done till I got the flag. 
