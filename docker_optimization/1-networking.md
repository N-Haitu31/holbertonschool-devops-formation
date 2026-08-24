# 1-networking.md

## Commands
 
```bash
# 1. Create a custom bridge network (not the default one)
docker network create my-net
 
# 2. Run two containers on that network
docker run -d --name web --network my-net nginx:alpine
docker run -d --name api --network my-net nginx:alpine
 
# 3. Prove web can reach api by name
docker exec web ping -c 3 api
 
# 4. Confirm it works the other way too, regardless of creation order
docker exec api ping -c 3 web
```
 
## Observations
 
`docker network create my-net` creates a new Docker network object, independent from any container — a custom bridge network, since `bridge` is the default driver when none is specified. This is different from Docker's default `bridge` network, where containers can only reach each other by IP, never by name.
 
Both `web` and `api` were started with `--network my-net`, attaching them to this custom network instead of the default one. `docker run` confirmed each container's ID (`e27e9817a1c3...` for `web`, `1dc3f16df408...` for `api`).
 
The actual proof is in `docker exec web ping -c 3 api`:
 
```
PING api (172.21.0.3): 56 data bytes
64 bytes from 172.21.0.3: seq=0 ttl=64 time=0.319 ms
64 bytes from 172.21.0.3: seq=1 ttl=64 time=0.082 ms
64 bytes from 172.21.0.3: seq=2 ttl=64 time=0.109 ms
 
--- api ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.082/0.170/0.319 ms
```
 
The first line is the key result: `web` only ever referred to the target as `api` — a name, not an address — and Docker resolved it automatically to `172.21.0.3`. That resolution is exactly what a custom network provides and the default `bridge` network doesn't. All 3 packets got a reply (0% packet loss), confirming the two containers can actually talk to each other, not just resolve each other's name.
 
Running the same test in reverse (`docker exec api ping -c 3 web`) succeeded identically. This confirms name resolution on a custom network isn't tied to which container was created first — it only requires both containers to be attached to the same network at the time of the test, and works symmetrically in both directions from then on.
 
## Conclusion
A custom bridge network gives containers attached to it a built-in DNS mechanism, resolving container names to their current internal IP automatically. This removes the need to hardcode or look up IPs, which is exactly what Docker Compose does under the hood for services in a `compose.yaml` — this task just did it by hand to see the mechanism directly.