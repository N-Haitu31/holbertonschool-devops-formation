# Docker Compose
 
## About
This project is about orchestrating multiple containers together with Docker Compose, instead of wiring them up by hand with a chain of separate `docker run` commands.
 
## What this project covers
- Defining multi-service stacks in a single `compose.yaml`
- Compose file anatomy: `build` vs `image`, ports, volumes, networks, environment variables, `depends_on`
- Ensuring services start in the right order with healthchecks and dependency conditions
- Parameterizing a stack with `.env` files
- Debugging and fixing a broken Compose stack