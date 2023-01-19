import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['3563028'])
API_HASH = environ['d119ea76a256e81446faacdb20a204d8']
BOT_TOKEN = environ['1549499373:AAHdwakIA0gaYjbjfqe-3rc-oSp0qJ59ous']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 3000000))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split(1073936432 390369891)]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel,'-1001505575461') else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()
TUTORIAL = "https://youtu.be/FCU_XJmyG_U"
# MongoDB information
DATABASE_URI = environ['DATABASE_URI','mongodb+srv://ngrockers:myhero12@cluster0.zbsed.mongodb.net/myFirstDatabase?retryWrites=true&w=majority']
DATABASE_NAME = environ['DATABASE_NAME','']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "<b>Join [😍 MALLUROCKERS CLUB ❤️💥 ](https://t.me/Mallurockersclub) for Best New Movies </b>

<code>{file_name}</code> 

 Size {file_size}
":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "93b1d218":
    API_KEY=None
else:
    API_KEY=93b1d218
