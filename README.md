
# How to run an example
Override the envoy.yaml in the served-config folder with a config from the 'configs' directory. 

then run: 

```
docker-compose up -d --build
```

Envoy admin, port 19000
Listener: port 8000

# Testing for Lab3-1

Confirm https works.
```
curl https://localhost:8443/hello -k -H "host: hello.envoyproxy.io"

Hello back!
```