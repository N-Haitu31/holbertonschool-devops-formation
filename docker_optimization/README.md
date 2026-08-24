# Docker: Optimization & Hardening
 
## About
This project turns working Docker images into production-ready ones: smaller, faster to rebuild, and locked down — with every improvement backed by real measured numbers, not just a feeling.
 
## What this project covers
- Slimming down a bloated image (layer ordering, `.dockerignore`, base image choice)
- Writing and repairing multi-stage builds to shrink final image size
- Persisting data with named volumes vs bind mounts
- Connecting containers over a custom network via DNS by service name
- Running a container as a non-root user
- Adding a working `HEALTHCHECK`
- Scanning an image for vulnerabilities with Trivy