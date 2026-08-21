# Full Stack Architecture

## Diagram
```
                 ┌─────────┐
 client --curl-->│  proxy  │  (port 8091, only published port)
                 └────┬────┘
                      │ http://api:5000
                      ▼
                 ┌─────────┐
                 │   api   │
                 └────┬────┘
                 ┌─────┴─────┐
                 ▼           ▼
            ┌────────┐  ┌────────┐
            │   db   │  │  cache │
            └────────┘  └────────┘
```


## Services
- proxy : single entry point for external traffic (the only one with a published port)
- api : processes requests; no longer directly accessible from the outside
- db : persistent storage; a health check ensures that the api only connects to it when it is ready
- cache : fast in-memory storage for frequently accessed data; avoids placing a load on the db with every request

## Network
 `Compose` creates a dedicated network (2-full_stack_default) when the stack is launched; all services are automatically connected to it; it is this network that enables each service to reach the others by name (api, db, cache) rather than by IP address.

## Data & Volumes
The proxy mounts a configuration file (nginx.conf), not application data. The database (Postgres), on the other hand, has no volume declared — so its data is not retained after a `docker compose down` followed by an `up` (the Postgres container restarts with an empty database each time it is recreated).

## Request path
External traffic → proxy (port 8091, sole entry point) → forwarded internally to the API (via its service name, port 5000, never exposed externally) → the API can then communicate with the DB and/or cache internally, always via service name, never via IP or localhost.
