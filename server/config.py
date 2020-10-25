import os
from dotenv import load_dotenv
load_dotenv()


ENVIRONMENT = 'prd'

if ENVIRONMENT == 'sbx':
    ZEN_URL = os.getenv("SBX_ZEN_URL")
    CLIENT_ID = os.getenv("SBX_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SBX_CLIENT_SECRET")

elif ENVIRONMENT == 'prd':
    ZEN_URL = os.getenv("PRD_ZEN_URL")
    CLIENT_ID = os.getenv("PRD_CLIENT_ID")
    CLIENT_SECRET = os.getenv("PRD_CLIENT_SECRET")
