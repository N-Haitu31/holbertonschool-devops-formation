# Talk to your container

## Commands used

```
- docker build -t first-image .
- docker run -d -p 8082:5000 --name talk-container -e GREETING_NAME=Haitu first-image
- curl http://localhost:8082
- docker exec talk-container printenv GREETING_NAME
- docker inspect --format '{{.Config.Env}}' talk-container
```

## Observations

1 – The variable is injected at runtime, not at build time, which means a single image can be reused with different behaviours:

- with -e :
```
docker run -d -p 8082:5000 --name talk-container -e GREETING_NAME=Haitu first-image
curl http://localhost:8082
> Hello Haitu from Docker!
```

- without -e :
```
docker run -d -p 8083:5000 --name talk-container-default first-image
curl http://localhost:8083
> Hello stranger from Docker!
```

2 – The variable is confirmed internally via `exec`. The variable actually exists in the environment of the running process, not just visible from the outside via `curl`:
```
docker exec talk-container printenv GREETING_NAME
> Haitu
```

3 – `inspect` allows you to view the container’s full configuration.
```
docker inspect --format '{{.Config.Env}}' talk-container
> [GREETING_NAME=Haitu PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin...
```

Note : Appears mixed in with the system variables already present in the base image (PATH, LANG, GPG_KEY, PYTHON_VERSION...) — which shows that the -e flag adds your variable to the existing environment rather than replacing it.