import redis

r = redis.Redis(db=5)
r.lpush("ips", "51.218.112.236")
r.lpush("ips", "90.213.45.98")
r.lpush("ips", "115.215.230.176")
r.lpush("ips", "51.218.112.236")
print(r)