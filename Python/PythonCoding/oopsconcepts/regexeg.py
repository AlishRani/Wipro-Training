import re

txt=input("Enter a text")
bpat=input("Enter a beginning pattern")
epat=input("Enter a ending pattern")

if re.search(pattern=bpat,string=txt):
    print("Beginning pattern available")
else:
    print("Beginning pattern not available")