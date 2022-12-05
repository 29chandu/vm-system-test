import pytest
from paramiko import SSHClient, AutoAddPolicy
from settings import Config


@pytest.fixture(autouse=True)
def ssh_client():
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname=Config.SSH_HOST, port=Config.SSH_PORT,
                   username=Config.SSH_USER, password=Config.SSH_PASSWORD)
    return client
