import telnetlib
from time import sleep

a = telnetlib.Telnet(host='172.18.30.2', port=4)
# a.write('\n')
# print (a.read_some())
# a.write('ss'.encode('utf-8'))
# print(a.read_some())

# a.write("\n".encode('utf-8'))
# a.read_until("login:".encode('utf-8'))
# sleep(2)
# a.write('superman\n'.encode('utf-8'))
# a.read_until("Password".encode('utf-8'))
# a.write('talent\n'.encode('utf-8'))
# sleep(1)
a.write('10.0.0.0\n'.encode('utf-8'))
# for i in range(1,10):
#     a.write('10.0.%d.8'%i)
#     sleep(1)



a.close()

'''
import telnetlib
a = telnetlib.Telnet(host='172.18.30.2', port=4)
from time import sleep
# a.write("\n".encode('utf-8'))
# a.read_until("login:".encode('utf-8'))
# sleep(2)
# a.write('superman\n'.encode('utf-8'))
# a.read_until("Password".encode('utf-8'))
# a.write('talent\n'.encode('utf-8'))
# sleep(1)
for i in range(1,10):
    a.write('network arp add ip 90.0.%d.3 mac-address 00-00-01-00-00-01 dev feth4\n'.encode('utf-8')%i)
    sleep(1)

'''
