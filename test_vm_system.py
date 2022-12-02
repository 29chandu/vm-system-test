from datetime import datetime

import pytest
from logger import logger


@pytest.mark.cli
class TestSystem:

    def write_to_file(self, line):
        file_name = 'system_status_tracking.txt'
        with open(file_name, 'a') as f:
            f.write(f'{datetime.now()} :: {line}\n')

    def test_cpu_usage(self, ssh_client):
        logger.info('Running CPU usage test case')
        cpu_usage_cmd = r"top -bn2 | grep '%Cpu' | tail -1 | grep -P '(....|...) id,' | awk '" + \
            r'{print 100-$8}' + r"'"
        stdin, stdout, stderr = ssh_client.exec_command(cpu_usage_cmd)
        cpu_usage = float(stdout.readline())
        print('cpu usage: ', cpu_usage)
        stdin.close()
        self.write_to_file(f'CPU Usage- {cpu_usage}%')
        assert cpu_usage < 90

    def test_memory_usage(self, ssh_client):
        logger.info('Running memory usage test case')
        mem_usage_cmd = r"free -t | awk 'NR == 2 {print $3/$2*100}'"
        stdin, stdout, stderr = ssh_client.exec_command(mem_usage_cmd)
        mem_usage = float(stdout.readline())
        print('mem usage: ', mem_usage)
        stdin.close()
        self.write_to_file(f'Memory Usage- {mem_usage}%')
        assert mem_usage < 90

    def test_disk_usage(self, ssh_client):
        logger.info('Running disk usage test case')
        disk_usage_cmd = r"df -h --output='pcent' /"
        stdin, stdout, stderr = ssh_client.exec_command(disk_usage_cmd)
        disk_usage = float(stdout.readlines()[1].strip('%\n'))
        print('disk usage: ', disk_usage)
        stdin.close()
        self.write_to_file(f'Disk Usage- {disk_usage}%')
        assert disk_usage < 101
