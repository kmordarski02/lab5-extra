import redis
import os
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)
print("Worker gotowy...")
while True:
    task = r.brpop("tasks")
    print(f"Wykonano zadanie: {task}")