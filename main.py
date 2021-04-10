import amino
import pyfiglet
import colorama
from colorama import Fore, Back, Style

print(Fore.LIGHTBLUE_EX)
print(Back.BLACK)
print(Style.BRIGHT)

Introduction = pyfiglet.figlet_format("Apollyon Spam Bot", font = "bulbhead")
print(Introduction)
print("Made By Major Gaston.")
client = amino.Client()
email = input("Email: ")
password = input("Password: ")
client.login(email=email, password=password)
print("Logged in!")

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
  print(name, id)

comId = input("Community ID: ")
sub_client = amino.SubClient(comId=comId, profile=client.profile)
print("Accessed the community.")

title = input("Wiki Title: ")
content = input("Wiki Content: ")

while True:
    try:

       sub_client.post_wiki(title=title, content=content)

    finally: pass
    print("Wiki spammed...")





