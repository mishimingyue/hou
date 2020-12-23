import telnetlib
from time import sleep

a = telnetlib.Telnet(host='172.18.29.2', port=8)
# a.write('\n')
# print (a.read_some())
# a.write('ss'.encode('utf-8'))
# print(a.read_some())

a.write("\n".encode('utf-8'))
a.read_until("login:".encode('utf-8'))
sleep(2)
a.write('superman\n'.encode('utf-8'))
a.read_until("Password".encode('utf-8'))
a.write('talent\n'.encode('utf-8'))
a.close()
