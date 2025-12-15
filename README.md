# socks5 tcp proxy

minimal tcp forwarder that resolves a minecraft srv record and routes traffic through a socks5 proxy :D

## showcase:
https://github.com/user-attachments/assets/36a74946-a464-48af-a21d-794f22430d08


## structure
```

project/
├─ core/
│  ├─ net.py      # dns + socket piping
│  └─ proxy.py   # socks5 logic
├─ config.py     # all settings
└─ main.py       # startup + listener

```

## flow
```

client
|
v
local listener (25565)
|
v
main.py
|
+--> resolve srv (net.py)
|
+--> open socks5 tunnel (proxy.py)
|
v
target server

```

## run sequence
```

start
├─ load config
├─ resolve target domain
├─ test proxy latency
└─ listen for clients

on connect
├─ accept client socket
├─ connect to target via socks5
└─ pipe traffic both ways

```

run with:
```
python main.py

```


feel free to contribute to this!
