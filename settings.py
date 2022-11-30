import os

from dotenv import load_dotenv

local_run = False

if local_run is True:
    load_dotenv()


class Config:

    # SSH server info
    SSH_HOST = os.getenv('SSH_HOST')
    SSH_PORT = os.getenv('SSH_PORT')
    SSH_USER = os.getenv('SSH_USER')
    SSH_PASSWORD = os.getenv('SSH_PASSWORD')
