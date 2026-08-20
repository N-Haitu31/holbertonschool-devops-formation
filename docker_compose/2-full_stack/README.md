# 2. Grow the stack

## Service roles
### 1. The role of each service:
- proxy : single entry point for external traffic (the only one with a published port)
- api : processes requests; no longer directly accessible from the outside
- db : persistent storage; a health check ensures that the api only connects to it when it is ready
- cache : fast in-memory storage for frequently accessed data; avoids placing a load on the db with every request
### 2. The path of a request:
External traffic → proxy (port 8091, sole entry point) → forwarded internally to the API (via its service name, port 5000, never exposed externally) → the API can then communicate with the DB and/or cache internally, always via service name, never via IP or localhost.

### 3. Why this structure:
- A single entry point = easier to secure and monitor than multiple open ports
- The database and cache are never exposed externally = reduced attack surface
- Everything communicates via service name = the stack functions identically regardless of where it runs (no hard-coded IP addresses)

## Commands and Observations

- docker compose up -d
- docker compose down
- curl http://localhost:8091/
>Hello from the API service, stranger!
- curl http://localhost:8091/cache-check
>This endpoint has been hit 1 times (via Redis at 'cache')
- curl http://localhost:8091/cache-check
>This endpoint has been hit 2 times (via Redis at 'cache')

## Conclusion
- The fact that the Redis counter increases from 1 to 2 between two calls proves that it is not just ‘present’, but is actually being used and persists between requests — not simply a connection that opens and closes without having any effect.
- The link to today’s objective: a single `docker compose up` command was enough to start four interdependent services (db, cache, api, proxy) in the correct order — compared to four `docker run` commands that had to be chained together and linked manually before Compose.