import os

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
