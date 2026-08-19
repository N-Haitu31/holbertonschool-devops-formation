# 1. Order matters

##  Healthchecks
 
`depends_on` alone only waits for a container to *start*, not to be *ready*.
Here, `db` has a `healthcheck` (`pg_isready`), and `api` declares
`depends_on: db: condition: service_healthy` — so `api` only starts once
Postgres is actually accepting connections.
 
### Proof in the logs
 
```
Container 1-healthchecks-db-1 Waiting
...
Container 1-healthchecks-db-1 Healthy
api-1  |  * Serving Flask app 'app'
```
 
`api` only prints its first log line after `db` is marked `Healthy`.
 
###   Commands
 
```
docker compose up
docker compose down
```