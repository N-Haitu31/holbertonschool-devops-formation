from flask import Flask
import os
import redis

GREETING_NAME = os.environ.get("GREETING_NAME", "stranger")

app = Flask(__name__)

r = redis.Redis(
    host='cache', port=6379, db=0, decode_responses=True
)

@app.route("/")
def home():
    return f"Hello from the API service, {GREETING_NAME}!"

@app.route("/cache-check")
def cache_check():
    count = r.incr("hits")
    return f"This endpoint has been hit {count} times (via Redis at 'cache')\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
