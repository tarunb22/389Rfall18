Writeup 10 - Crypto II
=====

Name: Tarun Balachander
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tarun Balachander

## Assignment 10 Writeup

### Part 1 (40 Pts)
I got the flag: CMSC38R-{y0U-are_the_5ql_n1nja}

I tried to do a lot of different sql injection stuff like what we saw such as ' OR '1'='1'-- -but was not having much luck with the sql injection. I knew that you were ablke to navigate the different item ids by changing the value in the url. I tried the specific values that the prices provided and I ended up getting a flag by using id=1337. The other values that were provided in the table did not yield a flag.   

### Part 2 (60 Pts)
Level 1: This level was easy as it was fairly self explanatory, I entered <script>alert()</script> into the query and passed the level.

Level 2: We went over part of this level in class so I new I needed to be using an image tag as well as taking advantage of onerror in order to get alert() to work. I ended up typing <img src = "randsrc" onerror = "alert()"> into the chatbox and it worked.

Level 3: I had to use some of the hints for this level to fully understand what parts to look at. I understood that you could place stuff after the frame So I used oneror again and did level3/frame#6'onerror = 'alert()'; to get the alert to popup.

Level 4: This level was pretty confusing to me and I had to use all the hints and do a bit of research in order to understand how to properly escape and have alert called, I used ');alert(' to get it to work.

Level 5: window.location is shown as the next parameter, I had to look into the syntax of how to get alert() to work but I found out I can use javascript:alert() and it worked so all I had to do was go to the url with end changed to signup?next=javascript:alert() and click to next button to have an alert popup.

Level 6: I am still working on solving level 6 but so far have not been able to properly get the alert() to popup and advance past this stage.
