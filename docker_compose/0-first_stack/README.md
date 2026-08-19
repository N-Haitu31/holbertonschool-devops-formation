# 0-first_stack/

A 3-service stack (API, web front, database) orchestrated with Docker Compose.

## Commands & Observations

- `docker compose up -d`: all 3 containers start, a dedicated network is created.
- `docker compose ps`: all `Up`. `api` and `web` have a published port, `db` doesn't — expected, no need to expose the database externally.
- `curl :5000`: the API responds ("Hello from the API service, stranger!").
- `curl :8090`: nginx responds with its default page.
- `docker compose down`: everything is removed cleanly.
