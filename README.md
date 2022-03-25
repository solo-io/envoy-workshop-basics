
# How to run an example
Override the envoy.yaml in the served-config folder with a config from the 'configs' directory. 

then run: 

```
docker-compose up -d --build
```

Envoy admin, port 19000
Listener: port 8000

# How to test Lab4-2

After applying access log config to Envoy, tail the proxy logs like this:
`docker logs $(docker ps | grep envoyproxy | awk '{print $1}') -f`

Generate some good and bad requests against the proxy:

```
curl https://localhost:8443/hello -k -H "host: hello.envoyproxy.io" -H "Authorization: workshop"
Hello back!
```

```
curl https://localhost:8443/hello -k -H "host: hello.envoyproxy.io" -H "Authorization: bad-key" -i
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

Now look at the end of the Envoy logs. Note the `200 OK` response code for the first request, and the `403 Forbidden` response for the second request. The contents of these access log records can be heavily customized. 
```
[2022-03-25T20:44:19.126Z] "GET /hello HTTP/1.1" 200 - 0 11 5 1 "-" "curl/7.77.0" "3c79bdbe-32d9-415c-bbb9-a66e4dfd3f05" "hello.envoyproxy.io" "192.168.80.2:8080"
[2022-03-25T20:44:37.006Z] "GET /hello HTTP/1.1" 403 - 0 239 2 1 "-" "curl/7.77.0" "8045dde2-5bcb-4dbe-8801-e9f416d54650" "hello.envoyproxy.io" "-"
```