# 1. Create a Python Generators to generate the vowels. This should be a cyclic generators and will generate infinte list of vowels.
# -------------
# 2. Let's imagine a scenario where we have a Server instance running different services such as http and ssh on different ports. Some of these services have an active state while others are inactive.
#
# class Server:
#
#     services = [
#         {'active': False, 'protocol': 'ftp', 'port': 21},
#         {'active': True, 'protocol': 'ssh', 'port': 22},
#         {'active': True, 'protocol': 'http', 'port': 80},
#     ]
#
# - Create an iterators for the Server class which would loop over only the active ports
# - Create a generator class that does the same thing
#
# -------------
# 3.Write a password generator in Python. Be creative with how you generate passwords - strong
# passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The
# passwords should be random, generating a new password every time the user asks for a new
# password. Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word
# or two from a list.
#
# -------------
#4. Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.(https://www.nytimes.com/)

#Part 1
from itertools import cycle
print("Vowels generated in cyclic fashion:")
vowels = cycle(['a', 'e', 'i', 'o', 'u', 'y'])

for i in range(10):
    print(next(vowels))

#Part 2
class Server:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]

    def __init__(self):
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.__counter < len(self.services):
            self.__counter += 1
            if self.services[self.__counter - 1]['active']:

                return self.services[self.__counter - 1]

        raise StopIteration

def service_generator(server : Server = Server()):
    counter = 0
    while counter < len(server.services):
        if server.services[counter]["active"]:
            yield server.services[counter]
        counter += 1
    raise StopIteration


ser = Server()

ser_it = iter(ser)

print("\nMade with iterator:")
while True:
    try:
        print(next(ser_it))
    except StopIteration:
        break


print("\nMade with generator:")
ser_gen = service_generator()
while True:
    try:
        print(next(ser_gen))
    except RuntimeError or StopIteration:
        break


#Part 3
import random as r
import re


def main():
    password_generator()


def password_generator():
    pass_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTYUVWXYZ1234567890!@#$%^&*+="
    char_count = r.randrange(8, 12)
    password = ""
    for i in range(char_count):
        password += pass_chars[r.randrange(0, len(pass_chars))]


    while re.match(r'[A-Za-z0-9!@#$%^&*+=]{8,}', password) == False:
        password += pass_chars[r.randrange(0, len(pass_chars))]

    print("\nGenerated password:")
    print(password,"\n")


if __name__ == "__main__":
    main()

#Part 4
from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
html = requests.get(url, timeout=10).content
soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all(name="h2") #all article titles stored in h2 tags

print("\nNY Times home page articles right now:")
for article in divs[:-2]: #Leave out last 2 because they are headers for site index and navigation
    if article.get_text().strip() != "":
        print(article.get_text())
#print(divs)