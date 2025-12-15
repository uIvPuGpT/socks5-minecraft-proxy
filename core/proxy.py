import socket,time

def socks5_connect(h,p,ph,pp,u,pw):
    #sock5 tunnel
    s=socket.socket()
    s.connect((ph,pp))
    s.sendall(b"\x05\x01\x02")
    s.recv(2)
    u=u.encode()
    pw=pw.encode()
    s.sendall(b"\x01"+bytes([len(u)])+u+bytes([len(pw)])+pw)
    s.recv(2)
    hb=h.encode()
    s.sendall(b"\x05\x01\x00\x03"+bytes([len(hb)])+hb+p.to_bytes(2,"big"))
    s.recv(10)
    return s

def proxy_latency(h,p,ph,pp,u,pw):
    #latency check
    t=time.time()
    s=socks5_connect(h,p,ph,pp,u,pw)
    s.close()
    return int((time.time()-t)*1000)
