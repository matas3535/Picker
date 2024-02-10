## < Imports >
import time
## < Arrays >
Emails = []
## < Variables >
Text = ""
## < Init >
with open("Emails.txt", "r") as File:
    Text = File.read()
## < Functions >
def Pick():
    Lines = Text.split("\n")
    ##
    for Index in Lines:
        Commas = Index.split(",")
        Email = Commas[0]
        ##
        if (Email.split("@")[1] == "gmail.com"):
            Emails.append(Email)
##
def Get():
    for Email in Emails:
        print(Email)
    ##
    print("Count", len(Emails))
    ##
    while (True):
        time.sleep(1)
## < Main >
Pick()
Get()
