#!/usr/bin/env python3
""" Demo program"""

myFile_list =["Bob Bye,bob@big.com",
"Julie Roth, Jroth@thinktank.com", 
"John Davis, JDavis@KingOfTheWorld.com"]

print(" Opening myFile :{myFile_str}")
#file = open("emails")
for line in myFile_list:
    print(f"\t + line : {line}, {type(line)}")
    name, email = line.split(",")
    if name == "John Davis":
        print(f" Name found: {email}")
