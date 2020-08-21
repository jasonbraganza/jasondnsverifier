# Jason’s DNS Verifier  
---  

This is a tiny utility that verifies if your ISPs DNS lookups match those of standard DoH providers, Google and Cloudflare.

Requirements:
- Python 3.6
- And everything from the requirements.txt file.

You’ll need a text file full of sites, one per line.
  
`python jdv.py 'filename.txt'` to run the program