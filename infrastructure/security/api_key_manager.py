import os
from dotenv import load_dotenv
load_dotenv()

def get_api_key(name):
    return os.getenv(name)