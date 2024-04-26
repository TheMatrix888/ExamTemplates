from ipaddress import ip_network

n = 0
for ip in ip_network("114.179.203.128/255.255.255.192"):
    if bin(int(ip))[2:].count("1") % 3 == 0:
        n += 1
print(n)
