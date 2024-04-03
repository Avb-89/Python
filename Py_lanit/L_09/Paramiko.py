import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='localhost', username='sitis', password="205967", port=22, look_for_keys=False)
stdin, stdout, stderr = client.exec_command('mkdir -r hello')
stdin, stdout, stderr = client.exec_command('ls')
print(stdout.read())
client.close()