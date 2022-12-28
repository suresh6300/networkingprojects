from netmiko import ConnectHandler

CSR={
    "device_type": "cisco-ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}
net_connect=ConnectHandler(**CSR)
#output_runhost= net_connect.send_command('show ip int brief')
#print(output_runhost)
#output_clock=net_connect.send_command('show clock')
#print(output_clock)
#output_route=net_connect.send_command('show ip ro')
#print(output_route)
output_runhost=net_connect.send_command('show run')
print(output_runhost)
net_connect.disconnect()