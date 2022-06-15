import karim_data
from random import random
import sqlite3
import random
import os.path



# path = './Insta image/'
# num_files = len([f for f in os.listdir(path)
#                 if os.path.isfile(os.path.join(path, f))])
# image = random.randrange(0,len(num_files))

#MANUAL SEND TO DB
karim_data.InsertConnexionToDB("kbnueve9bot","kleilla83")
karim_data.InsertConnexionToDB("test","test")

karim_data.InsertMessageToDB("Ala Madrid!", "Ala Madrid!")

karim_data.InsertFollowToDB("psg")
print(*karim_data.SelectMessageFromDB()[1])