Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. He is from Silver Spring, MD
   @kruegster1990 is his handle. Found both of these by searching online and found his stwity/twitter account.
   He also goes by kruegster1990 on instagram which I found using intel  techniques - he likes Pokémon (also a boarding pass on the insta AAC27670).
   Company is cornerstoneairlines which was found through the stwity account.
   Email is kruegster@tutanota.com which is found on the cornerstoneairlines webpage.

3. The IP address of the webserver is 142.93.118.186 I found this by running an nmap on cornerstoneairlines.co

4. By going to robots.txt I saw that there is a hidden directory called secret and found the flag: CMSC389R-{fly_th3_sk1es_w1th_u5}
Also by looking at the source code I found the flag: CMSC389R-{h1dden_fl4g_in_s0urce}

5. 142.93.117.193 links to the under construction gif/admin page. Ports 1337. Found using nmap. The associate server can also be seen just by viewing page source.

6. I found that the DNS hosting provider is Digital Ocean, INC and I found this by using reverse DNS. They are located in New York.

7. The operating system running on the associated server is Ubuntu, I found this on censys

8. *(BONUS)*
Cornerstone airlines source code flag:CMSC389R-{h1dden_fl4g_in_s0urce}
Cornerstone airlines secret dir flag: CMSC389R-{fly_th3_sk1es_w1th_u5}
Cornerstone airlines who is flag: CMSC389R-{dns-txt-rec0rd-ftw}
Inside cornerstone airlines shell: CMSC389R--{c0rn3rstone-air-27670}
### Part 2 (55 pts)

I just took the stub.py python brute force script and wrote it with basically looping through each password within rockyou.txt and checking if it would work against a username. The host was the admin page because that is what we are trying to get into. I then used nmap and ranged through different ports till I saw that port 1337 was open. In the end I actually did not use the brute force script to get into the cornerstone airlines administrator server. By using intel techniques to find sites with the username kruegster1990 I found the Instagram. With the multiple Pokémon pictures as well as the hints given I narrowed down the password choices to most likely either be pokemon, pikachu, or charizard. The tough part for me was finding the username. The username honestly took a good amount of trial and error but because I was able to narrow down the password it did not take too much time to get into the shell with the username kruegster and password pokemon. The instagram profile also provided the ticket information with a specific flight number (AAC27670) that I had previously recorded. Once I was in the shell, it was a fairly quick process to navigate to the flight information with the flag stored. I also validated that my brute force method worked by running it with the now known username and it did work.
