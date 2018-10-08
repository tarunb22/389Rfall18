Writeup 5 - Binaries I
======

Name: Tarun Balachander

Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Tarun Balachander

## Assignment 5 Writeup

Overall Thoughts on this homework: I had a lot of trouble implementing these x86 commands properly. Assembly languages in general have never been a strong suit of mine and personally for this project it felt like all I really had for help was the power-point that was provided so it made this homework tough for me.

The way I approached both assembly functions was by trying to follow the C implementation and have my code echo what the C function would be doing. For memset I started off with creating an accumulator in register rcx that would act as i and would go through the indexes of the string. My comparison checks and breaks if rcx is greater than or equal to rdx (which is strl, and this statement is also equivalent to i < strl) and jumps to l2 if it is. Inside l1 I have essentially created a for loop that adds the value we want into the correct index of the str and increments it. For quite some time this was the extent of my implementation but it was not returning correctly, specifically I saw that I would lose the tail end of the string that should have remained intact. My solution to this was to grab the end of the string that was not to be overwritten in any way and save it to a register (specifically r10 in memsets case) and then append it back to the edited string after we add the value. This fixed seem to fix my issue of losing the data behind the indexes that are being overridden. I had a lot of trouble finding the proper fix for this because for me gdb was not working properly in order to see exactly what my code was doing. The issues that I saw was that no matter where I set my breakpoints gdb was not letting me step directly into my assembly functions itself and they would just run to completion, making it very hard to see exactly what my assembly function was doing line by line. Strncpy followed the path of memset very closely, as even their C algorithms are very similar. The only large change is that rather than load the rsi value directly to rax I had to grab the value at a certain index so that it would properly do dst[i] = src[i]. I had the same problem of strncpy not properly keeping the characters after the positions we edited so I did the same thing and saved that substring to a regsiteer (r12 in this case) and appended it back to my new string and that seemed to do the trick. 
