
import ipaddress

IP = "172.16.12.0"

# convert the IP addresses to binary format
ip_bin = bin(int(ipaddress.IPv4Address(IP)))[2:]
print(ip_bin)

# convert the binary format to IP format
new_ip = str(ipaddress.ip_address(int(ip_bin, 2)))
print(new_ip)