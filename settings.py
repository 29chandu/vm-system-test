import os

from dotenv import load_dotenv

local_run = False

if local_run is True:
    load_dotenv()


class Config:

    # SSH server info
    SSH_HOST = os.getenv('SSH_HOST') or 'localhost'
    SSH_PORT = os.getenv('SSH_PORT') or '2222'
    SSH_USER = os.getenv('SSH_USER') or 'user'
    SSH_PASSWORD = os.getenv('SSH_PASSWORD') or 'pw'

    # Logging
    CONSOLE_LOG_LEVEL = 'INFO'
    FILE_LOG_LEVEL = 'INFO'
    LOG_FILE_PATH = 'test_logs.log'
