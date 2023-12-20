import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Set the initial value for 'start' and 'start_pst'
num1 = 1

redis_client.set("key", num1)
