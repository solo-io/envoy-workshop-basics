
# How to run an example
Override the envoy.yaml in the served-config folder with a config from the 'configs' directory. 

then run: 

```
docker-compose up -d --build
```

Envoy admin, port 19000
Listener: port 8000

# How to test Lab3-2

Before applying ExtAuth filter, this works fine:
```
curl https://localhost:8443/hello -k -H "host: hello.envoyproxy.io"

Hello back!
```

After applying ExtAuth filter, this now fails with 403:
```
curl https://localhost:8443/hello -k -H "host: hello.envoyproxy.io" -i
HTTP/1.1 403 Forbidden
content-type: text/html; charset=utf-8
content-length: 239
server: envoy
date: Fri, 25 Mar 2022 20:11:08 GMT
x-envoy-upstream-service-time: 1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>You don&#x27;t have the permission to access the requested resource. It is either read-protected or not readable by the server.</p>
```

But adding the `Authorization` header causes it to succeed:
```
curl https://localhost:8443/hello -k -H "host: hello.envoyproxy.io" -H "Authorization: workshop"
Hello back!
```