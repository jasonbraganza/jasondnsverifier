## Problem - Compare domain lookups, against DoH Servers
  
- Take a list of domains (one per line) from a text file as input, find the IP address for the domain using the standard system level DNS, and then check against DoH answers from both cloudflare and google. and say if all answers match properly or not.

## Notes  
What do I need to do? (checklist)  

- Get a list of popular websites, (probably Alexa)  
- figure out a way to read them in  
- loop through each line, and look up its ip  
    - with the local dns (use the sockets module)
    - with Google’s [DoH json endpoint][gdoh] (use the requests module)
    - with Cloudflare’s [DoH json endpoint][cdoh] (ditto like Google)
- compare all the values
- Print if they match or not.  
  
  
## Experience  

- I should commit my work often. This took me two days, because I lost all of yesterday’s progress in a computer hiccough.  
- The program runs well. It intentionally limits itself to only the first result in the Google and Cloudflare lookups.    
- I should learn to focus more on what is at hand and not overthink the program.  
- I should be learning to build primitive little, handy dandy tools, not giant cathedrals.  
- I spent two hours fiddling with a way to create *another* program that would process files for me. (and abandoned it)  
- I need to read the documentation across sites *very carefully*.  
    - They are written with experienced programmers in mind, and not beginners like me.
    - For e.g. When I was trying to look up domain names with Cloudflare, I blindly copied the example and then wondered why it was not giving me the appropriate replies. I then realised I was missing a seperate parameter, `&ct=application/dns-json` which was quite clearly listed above, but not in the example below.  
- Which leads back to the fact, that I should stick to what is assigned, because just doing that much at this stage is taking me a long time. Improvements and features can wait until I am much more fluent.
- I realise I am trusting autocomplete too much, and I should at least *look* at what I am completing. I spent 40 minutes, wondering why my comparisons were not working, when in fact, I was using the wrong variables.  
  
## Code.   

Put your sites into a file called dumpsites.txt
Run check-ip.py  

[Gitlab][cgl] / [Github][cgh]


---  

[cgl]: https://gitlab.com/jasonbraganza/programming-practice/-/tree/master/check-ip
[cgh]: https://github.com/jasonbraganza/programming-practice/tree/master/check-ip
[cdoh]: https://developers.cloudflare.com/1.1.1.1/dns-over-https/json-format/
[gdoh]: https://developers.google.com/speed/public-dns/docs/doh/json