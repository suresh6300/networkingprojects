from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}
net_connect=ConnectHandler(**CSR)
output_runhost= net_connect.send_command('show ip int brief')
print(output_runhost)
net_connect.disconnect()
