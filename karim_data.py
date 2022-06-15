from random import random
import sqlite3
import random

dbconnect = sqlite3.connect('karim.db')
db = dbconnect.cursor()
#INSERT
def InsertConnexionToDB(username,password):
    db.execute("DROP TABLE IF EXISTS connexion")
    db.execute("CREATE TABLE connexion (user TEXT, password TEXT);")
    db.execute("INSERT INTO connexion VALUES (?, ?)", (username, password))
    dbconnect.commit()

def InsertMessageToDB(description,comment):
    db.execute("DROP TABLE IF EXISTS message")
    db.execute("CREATE TABLE message (description TEXT, comment TEXT);")
    db.execute("INSERT INTO message VALUES (?,?)", (description, comment))
    dbconnect.commit()

def InsertFollowToDB(account_name):
    db.execute("DROP TABLE IF EXISTS abonnement")
    db.execute("CREATE TABLE abonnement (account_name TEXT);")
    db.execute("INSERT INTO abonnement VALUES (?)", [account_name])
    dbconnect.commit()

def InsertPublicationToDB(media):
    db.execute("DROP TABLE IF EXISTS google_upload")
    db.execute("CREATE TABLE google_upload (media TEXT);")
    for i in media:
        db.execute("INSERT INTO google_upload VALUES (?)", i[0])


#SELECT
def SelectConnexionFromDB():
    dbconnect = sqlite3.connect('karim.db')
    db = dbconnect.cursor()
    username =  db.execute('SELECT username FROM connexion')
    mdp =  db.execute('SELECT password FROM connexion')
    return username, mdp

def SelectMessageFromDB():
    dbconnect = sqlite3.connect('karim.db')
    db = dbconnect.cursor()
    description =  db.execute('SELECT description FROM message')
    comment =  db.execute('SELECT comment FROM message')
    return description, comment

def SelectAbonnementFromDB():
    dbconnect = sqlite3.connect('karim.db')
    db = dbconnect.cursor()
    account_name =  db.execute('SELECT account_name FROM abonnement')
    return account_name

def SelectConnexionFromDB():
    dbconnect = sqlite3.connect('karim.db')
    db = dbconnect.cursor()
    pub_type1 =  db.execute('SELECT avec_ballon FROM google_upload')
    pub_type2 =  db.execute('SELECT action FROM google_upload')
    pub_type3 =  db.execute('SELECT common FROM google_upload')
    return pub_type1, pub_type2, pub_type3


# username = SelectAbonnementFromDB()[0]
# mdp = SelectAbonnementFromDB()[1]
# descript = SelectMessageFromDB()[0]
# comment = SelectMessageFromDB()[1]
# account_name = SelectMessageFromDB()
# pub_type1 = SelectConnexionFromDB()[0]
# pub_type2 = SelectConnexionFromDB()[1]
# pub_type3 = SelectConnexionFromDB()[2]






def RandomSelectAccount(username,mdp):
    rand = random.randrange(0,len(username))
    return username[rand], mdp[rand]

def RandomSelectMessage(description,comment):
    rand1 = random.randrange(0,len(description))
    rand2 = random.randrange(0,len(comment))
    return description[rand1], comment[rand2]

def RandomSelectSub(account_name):
    rand = random.randrange(0,len(account_name))
    return account_name[rand]

def RandomSelectMessage(avec_ballon,action,common):
    rand1 = random.randrange(0,len(avec_ballon))
    rand2 = random.randrange(0,len(action))
    rand3 = random.randrange(0,len(common))
    return avec_ballon[rand1], action[rand2], common[rand3]

# random_user = RandomSelectAccount[0]
# random_mdp = RandomSelectAccount()[1]
# random_description = RandomSelectMessage[0]
# random_comment = RandomSelectMessage[1]
# random_image = random.choice()
class Karim:
    def __init__( username, mdp, description, comment, image):
        username = random_user
        mdp = random_mdp
        description = random_description
        comment = random_comment
        image = random_image