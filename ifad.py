"""import ifaddr
adapters=ifaddr.get_adapters()

for adapter in adapters:
    print("Ips of network adapter" + adapter.nice_name)
    #nice name fetches the name of the adapter
    for ip in adapter.ips:
    #network interface :: 3 aspects 
    #-what is the type/name of the interface
    #-what is the ip address if configured
    #subnet
        print(" %s/%s" %(ip.ip, ip.network_prefix)) """
        
"""if you wish to include network interfaces that do not have a configured  IP address """

import ifaddr
adapters = ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IP s of network adapter" + adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print(" %s/%s" %(ip.ip, ip.network_prefix)) 
    else:
        print(" no ips configured ")

        