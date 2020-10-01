# anon-proxy-balancer
A dockerized load balancer that automatically distributes the traffic through a list of public proxies which is automatically renewed.


## Launch
```bash
docker-compose up -d
```

Alternatively:
```bash
docker run -p 9999:9999 -tid brunneis/anon-proxy-balancer
```

## Connection from Python
```python
import requests
response = requests.get('https://google.com/', proxies={'http': 'http://localhost:9999', 'https': 'http://localhost:9999'})
```
