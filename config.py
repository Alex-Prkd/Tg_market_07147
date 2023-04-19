import os
from dotenv import load_dotenv


load_dotenv()


class BotConfig:
    TOKEN = os.environ.get("TOKEN")
    DATABASE_URI = os.environ.get("DATABASE")



class BotPhoto:
    PHOTO = ""
