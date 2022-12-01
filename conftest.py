import pytest
from paramiko import SSHClient
from settings import Config


@pytest.fixture(autouse=True)
def ssh_client():
    print(
        f'\n\n\n\nDebug SSH info: host={Config.SSH_HOST}, port={Config.SSH_PORT}, user={Config.SSH_USER}, pw={Config.SSH_PASSWORD}\n\n\n\n\n')

    client = SSHClient()
    client.load_system_host_keys()
    client.connect(hostname=Config.SSH_HOST, port=Config.SSH_PORT,
                   username=Config.SSH_USER, password=Config.SSH_PASSWORD)
    return client
