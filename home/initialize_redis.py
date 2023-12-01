import redis

redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

start_value = 0
end_value = 10

redis_client.set("start", start_value)
redis_client.set("end", end_value)
