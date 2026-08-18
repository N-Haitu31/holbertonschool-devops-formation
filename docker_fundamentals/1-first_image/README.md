# First Docker Image

A minimal Flask app running in a Docker container.

## Build

```
docker build -t first-image .
```

## Run

```
docker run -d -p 8082:5000 --name first-image-container first-image
```

## Verify

```
curl http://localhost:8082
```
