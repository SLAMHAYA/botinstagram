import bot_action
import karim_data
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

cl = Client()
cl.login("kbnueve9bot", "kleilla83")
karim_bot = bot_action
kb9data = karim_data

karim_bot.InstaConnect()
karim_bot.UploadImage(kb9data)
