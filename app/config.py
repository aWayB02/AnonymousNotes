from dotenv import dotenv_values

config = dotenv_values(".env")

class Config:
    SECRET_KEY = config.get("SECRET_KEY", '12345')
