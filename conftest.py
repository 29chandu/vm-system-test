import pytest
from paramiko import SSHClient
from settings import Config


@pytest.fixture(autouse=True)
def ssh_client():
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(hostname=Config.SSH_HOST, port=Config.SSH_PORT,
                   username=Config.SSH_USER, password=Config.SSH_PASSWORD)
    return client
