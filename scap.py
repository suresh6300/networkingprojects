"""import scapy.all as scapy
request = scapy.ARP()"""

"""import scapy.all as scapy
request = scapy.ARP()
print(request.summary())#ARP who has 0.0.0.0 says 10.10.0.21"""

import scapy.all as scapy 
request = scapy.ARP()
print(request.show())
  """hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = who-has
  hwsrc     = 00:50:56:bc:04:58
  psrc      = 10.10.0.21
  hwdst     = 00:00:00:00:00:00
  pdst      = 0.0.0.0"""

