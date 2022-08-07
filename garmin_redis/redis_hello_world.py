import redis

def _redis_hello():
    r = redis.Redis(host='redis')
    r.mset({"hello": "world"})
    print(r.get('hello'))


if __name__ == "__main__":
    _redis_hello()