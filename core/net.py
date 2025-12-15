import socket,dns.resolver

def resolve(domain):
    #srv resolve
    r=dns.resolver.resolve("_minecraft._tcp."+domain,"srv")[0]
    return str(r.target).rstrip("."),r.port

def pipe(a,b):
    #back and forth socket pipe
    try:
        while True:
            d=a.recv(4096)
            if not d:break
            b.sendall(d)
    except:
        pass
    a.close()
    b.close()
