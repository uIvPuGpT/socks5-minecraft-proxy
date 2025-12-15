import socket,threading,uuid
import config
from core.net import resolve,pipe
from core.proxy import socks5_connect,proxy_latency

logged=False
lock=threading.Lock()

def log(m):
    print(f"[{config.red}+{config.rst}] {m}",flush=True)

#resolve
host,port=resolve(config.domain)

#proxy test
lat=proxy_latency(
    host,port,
    config.proxy_host,
    config.proxy_port,
    config.proxy_user,
    config.proxy_pass
)

log(f"proxy {config.proxy_host}:{config.proxy_port} {lat}ms")
log(f"target {host}:{port}")

ls=socket.socket()
ls.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ls.bind(("127.0.0.1",config.listen_port))
ls.listen()

def handle(c):
    global logged
    #connect
    s=socks5_connect(
        host,port,
        config.proxy_host,
        config.proxy_port,
        config.proxy_user,
        config.proxy_pass
    )
    uid=str(uuid.uuid4())
    threading.Thread(target=pipe,args=(c,s),daemon=True).start()
    threading.Thread(target=pipe,args=(s,c),daemon=True).start()
    with lock:
        if not logged:
            logged=True
            log(f"login {uid}")

#loop
while True:
    c,_=ls.accept()
    threading.Thread(target=handle,args=(c,),daemon=True).start()
