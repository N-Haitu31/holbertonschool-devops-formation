# First Container

## Commands used

```
docker pull nginx
docker run -d -p 8081:80 --name my-nginx nginx
curl http://localhost:8081
docker exec -it my-nginx bash
docker logs my-nginx
docker stop my-nginx
docker rm my-nginx
docker images
```

## Observations

- 1 : whilst exploring the container using `exec`, I found `index.html` in the exact location from which the response displayed by `curl` originated (`ls /usr/share/nginx/html`)

- 2 : The logs provide traceability for every HTTP request, including the curl request (“GET / HTTP/1.1” 200 896 “-” “curl/7.81.0” “-”)

- 3 : Even after stopping and removing my-nginx with docker stop/docker rm, the nginx image itself is still listed by docker images — the image is a static, reusable template that persists independently, while the container was just one temporary running instance of it. I could create a new container from that same image anytime without pulling it again (nginx:latest)
