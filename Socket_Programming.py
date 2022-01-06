
#!/usr/bin/env python3
import socket
import argparse
import http.server
import socketserver


#parser = argparse.ArgumentParser(description='Serve files from the current directory.')

host_name = socket.gethostname()

print(host_name)

#ip = socket.gethostbyname('localhost')
#ip = socket.gethostbyname('')
#ip = socket.gethostbyname(host_name)
ip=socket.gethostbyname('')
print(ip)

ls = [3, 14, 2, 1, 5]
lss=[]

for i in range(len(ls)):
    lower = None
    for j in range(len(ls)):
        if lower:
            if lower>ls[j]:
                lower=ls[j]
            else:
                pass
        else:
            lower=ls[j]
    lss.append(ls.pop(ls.index(lower)))
print(lss)
