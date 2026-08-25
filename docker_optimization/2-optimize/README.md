# 2 - Optimize
 
## About
The Dockerfile provided in this folder worked but was bloated: a full `node:20` base image, dependencies reinstalled on every code change, no `.dockerignore`, and the app running as root. This task rewrites it to be smaller, faster to rebuild, and locked down — with every improvement backed by measured numbers.
 
## Optimizations applied
- Switched the base image from `node:20` to `node:20-alpine`.
- Reordered the Dockerfile so dependencies (`package*.json` + `npm install`) are copied and installed **before** the rest of the code — a code-only change no longer invalidates the dependency layer's cache.
- Added a `.dockerignore` (`node_modules`, `npm-debug.log`, `.git`, `.env`) so the build context stays clean and never overwrites the image's own `npm install`.
- Created a dedicated non-root user (`appuser`) and switched to it with `USER` — `npm install` still runs as root (avoids permission issues), but the app itself runs as `appuser`.
## Before / After
 
| Metric | Before | After |
|---|---|---|
| Image size | 1.1 GB | 143 MB |
| Rebuild time (code-only change) | 6.812s | 1.265s |
| `npm install` on rebuild | re-run (not cached) | `CACHED` |
| Runs as | root (implicit) | `appuser` (non-root) |
 
Image size dropped by roughly **87%**, and rebuilding after a code-only change is about **5.4x faster** — because dependency installation no longer needs to be redone.
 
## How this was measured
 
```bash
# Baseline: build and check size
docker build -t optimize-baseline .
docker images optimize-baseline
 
# Baseline: rebuild time after a code-only change
# (edit index.js, then:)
time docker build -t optimize-baseline .
 
# Optimized: build and check size
docker build -t optimize-final .
docker images optimize-final
 
# Optimized: rebuild time after a code-only change
# (edit index.js, then:)
time docker build -t optimize-final .
 
# Confirm the app still works and runs as non-root
docker run -d -p 3001:3000 --name optimize-test optimize-final
curl http://localhost:3001
docker exec optimize-test whoami   # -> appuser
 
# Cleanup
docker stop optimize-test
docker rm optimize-test
```
 
The baseline's first build included downloading the full `node:20` image (~115s), so it isn't the relevant comparison — the code-only rebuild time (6.812s) is. In that build's log, `RUN npm install` was **not** cached even though only a text string changed, because `COPY . .` ran before it. In the optimized Dockerfile, the same test shows `CACHED [5/6] RUN npm install` — dependencies are untouched by a code change, exactly as intended.
 


