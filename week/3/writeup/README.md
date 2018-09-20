Writeup 3 - OSINT II, OpSec and RE
======

Name: Tarun Balachander

Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tarun Balachander

## Assignment 3 Writeup

### Part 1 (100 pts)

There was a lot of vulnerabilities that presented itself when looking at Fred Krueger, in order to help I will state 3 glaring issues that he should make sure he takes care of as fast as possible.


1) One glaring vulnerability is the extreme weakness of both your servers admin username and password. Having the username as just your last name as well as a password that can be easily deducted from personable likes (such as pokemon) makes it extremely easy to access the sever without even performing a brute force method as someone with just a bit of time, researching skills, and just a few attempts can get into the Cornerstone Airlines server with little effort. This glaring vulnerability is fairly easy to fix as well. Simply just adjusting the strength of both your username and password can go a very long way. Adding strength to your password is especially important as doing something such as P^k3m0n123 (adding special characters, numbers, upper/lowercase) will increase the strength of your password exponentially and make it extremely hard to brute force it quickly.


2) Another vulnerability that is a large issue is that the admin server IP is visible to anyone who comes across the website. The website should never have a visible or even have an admin page in the first place. Having a direct link to the admin server on your website is just giving away information to someone with malicious intent, and makes it a lot easy for someone to do damage. You should never have that IP visible to the general public as well as have plans for an admin page that a random person can attempt to access.


3) Letting the public know the admin server IP is leaving you very vulnerable, but leaving a port open on the admin server is also very bad. By leaving port 1337 open you are leaving yourself exposed to attacks on the website and the open port in combination with weak credentials makes it extremely easy to get access into the Cornerstone Airlines server as seen last week. It is important to not leave random ports open as you are more exposed to attacks. Having firewalls or better security would also help.


These are some glaring issues that are presenting with your companies webserver and are fairly simple fixes that can go a long way in stopping simple attacks that would have previously succeeded.
