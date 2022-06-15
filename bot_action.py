import random
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import karim_data
import os

cl = Client()

initial_count = 0
dir = "./Insta image"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1
img_selector = random.randrange(0, initial_count)
# media = cl.photo_upload(
#     "./Insta image/"+str(img_selector)+".jpg",
#     *kb9_data.SelectMessageFromDB()[1],
# )
cl.login("kbnueve9bot", "kleilla83")


def InstaConnect():
    cl.login("kbnueve9bot", "kleilla83")


kb9_data = karim_data
media_pk = cl.media_pk_from_url("./Insta image/"+str(img_selector)+".jpg")
media_path = cl.video_download(media_pk)
adw0rd = cl.user_info_by_username('kbnueve9bot')
hashtag = cl.hashtag_info('dhbastards')


# def UploadStory(media_path, adw0rd,hashtag):
#     cl.video_upload_to_story(
#         media_path,
#         "Credits @adw0rd",
#         mentions=[StoryMention(user=adw0rd, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
#         links=[StoryLink(webUri='https://github.com/adw0rd/instagrapi')],
#         hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
#         medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)]
#     )

# media.dict()
# {'pk': 2573355619819242434,
#  'id': '2573355619819242434_1903424587',
#  'code': 'CO2ZU1QFMPC',
#  'taken_at': datetime.datetime(2021, 5, 14, 10, 25, 16, tzinfo=datetime.timezone.utc),
#  'media_type': 1,
#  'product_type': 'feed',
#  'thumbnail_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-15/e35/185426950_474602463640866_4228057388625412955_n.jpg?se=8&tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=7NrVvAEG7f4AX_XPaOK&edm=ACqnv0EBAAAA&ccb=7-4&oh=bd2c90c2dcb693184e07c2777e09bb0b&oe=60C4E326&_nc_sid=9ec724&ig_cache_key=MjU3MzM1NTYxOTgxOTI0MjQzNA%3D%3D.2-ccb7-4', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/185426950_474602463640866_4228057388625412955_n.jpg', query='se=8&tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=7NrVvAEG7f4AX_XPaOK&edm=ACqnv0EBAAAA&ccb=7-4&oh=bd2c90c2dcb693184e07c2777e09bb0b&oe=60C4E326&_nc_sid=9ec724&ig_cache_key=MjU3MzM1NTYxOTgxOTI0MjQzNA%3D%3D.2-ccb7-4'),
#  'location': {'pk': 107617247320879,
#   'name': 'Russia, Saint-Petersburg',
#   'address': 'Russia, Saint-Petersburg',
#   'lng': 30.30605,
#   'lat': 59.93318,
#   'external_id': 107617247320879,
#   'external_id_source': 'facebook_places'},
#  'user': {'pk': 1903424587,
#   'username': 'adw0rd',
#   'full_name': 'Mikhail Andreev',
#   'profile_pic_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724'),
#   'stories': []},
#  'comment_count': 0,
#  'like_count': 0,
#  'has_liked': None,
#  'caption_text': 'Test caption for photo with #hashtags and mention users such @adw0rd',
#  'usertags': [{'user': {'pk': 1903424587,
#     'username': 'adw0rd',
#     'full_name': 'Mikhail Andreev',
#     'profile_pic_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724'),
#     'stories': []},
#    'x': 0.5,
#    'y': 0.5}],
#  'video_url': None,
#  'view_count': 0,
#  'video_duration': 0.0,
#  'title': '',
#  'resources': []}

cl.video_upload_to_story(
    media_path,
    "Credits @adw0rd",
    mentions=[StoryMention(
        user=adw0rd, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    links=[StoryLink(webUri='https://github.com/adw0rd/instagrapi')],
    hashtags=[StoryHashtag(hashtag=hashtag, x=0.23,
                           y=0.32, width=0.5, height=0.22)],
    medias=[StoryMedia(media_pk=media_pk, x=0.5,
                       y=0.5, width=0.6, height=0.8)]
)


# client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAADskdwEAAAAAypElN8KA9lj%2F%2FMjgsTuqZmil5Q4%3Dm98kPUAGtIkulwNkanhWrbRvEaMq4kSQUN6gY6CqUjIL0ExSs7")


# # import tweepy
# # import glob
# # import random
# # import os
# # #Personal, every user should complete.
# # api_key = "IYyaaeGhjjcmcNOxnIidDf6d5"
# # api_secret = "cWfJhsOsRdSEfItqIgn29TaS8QW16MDoNbNaWKUlyM2nzNP3gD"
# # oauth_token = "your access token" # Access Token
# # oauth_token_secret = "your access token secret" # Access Token Secret
# # auth = tweepy.OAuthHandler(api_key, api_secret)
# # auth.set_access_token(oauth_token, oauth_token_secret)
# # api = tweepy.API(auth)
# # #Changes directory to where the script is located (easier cron scheduling, allows you to work with relative paths)
# # abspath = os.path.abspath(__file__)
# # dname = os.path.dirname(abspath)
# # os.chdir(dname)
# # def randomimagetwitt(folder):
# #     #Takes the folder where your images are as the input and twitts one random file.
# #     images = glob.glob(folder + "*")
# #     image_open = images[random.randint(0,len(images))-1]
# #     api.update_with_media(image_open)
