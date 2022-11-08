import redis
r = redis.Redis()

'''
# print(r.ping())

# r = redis.Redis(host='foo.bar.com', port=12345)
# print(r.ping())

# r = redis.from_url('redis://foo.bar.com:12345')
# r.ping()

# https://redis-py.readthedocs.io/en/stable/commands.html
r = redis.Redis(decode_responses=True)
# print(type(r))
r.set('mykey', 'thevalueofmykey')
print(r.get('mykey'))

# redis-cli
# redis-server

# '''
# pyredis
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
print(r.get('Croatia').decode("utf-8"))