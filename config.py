import os


class Config(object):
    API_HASH = os.environ.get("aa7c2b3be68a7488abdb9de6ce78d311")
    BOT_TOKEN = os.environ.get("5927429053:AAGNa4VeQEOM5_Fj_mmq-21OqB6qr308DDU")
    API_ID = os.environ.get("14631157")
    OWNER = os.environ.get("5380833276")
    OWNER_USERNAME = os.environ.get("Dineth")
    PASSWORD = os.environ.get("Dilfilter2000")
    DATABASE_URL = os.environ.get("mongodb+srv://dilfilter123:dilfilter123@cluster0.tq9uv2k.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1002106332206")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
