from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        uter={
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**uter)
        print('connecting to '+IP)
        print('-'*79)
        output=net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()