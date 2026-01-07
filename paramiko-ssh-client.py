# https://docs.paramiko.org/en/2.6/

import paramiko

hostname, port, username, password = "", 22, "", ""

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname, port, username, password)

stdin, stdout, stderr = ssh.exec_command("ls -la")

print(stdout.read().decode())

ssh.close()
