import redis
import json

'''
import datetime
r = redis.Redis()

today = datetime.date.today()
# print(type(today))    # datetime.date
stoday = today.isoformat() 
# print(type(stoday))     # str
# print(stoday)

visitors = {"dan", "jon", "alex"}
# print(r.sadd(today, *visitors))
temp = r.sadd(stoday, *visitors) 
# print(temp)

print(r.smembers(stoday))

print(r.scard(today.isoformat()))
'''
import random

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}

r = redis.Redis(db=1)
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        print(h_id, hat)
        # print(type(h_id), type(hat))
        # print(type(h_id))
#         pipe.hset(h_id, json.dumps(hat))
#     pipe.execute()
# r.bgsave()