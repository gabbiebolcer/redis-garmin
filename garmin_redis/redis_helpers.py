import redis

def _redis_hello():
    data = {
        "hello": "world"
    }
    redis_commit(data=data)
    val = redis_get(key='hello')
    print(val)


def redis_commit(*,
                 host='redis',
                 port=6379,
                 data: dict = None):
    """Writes a key/value mapping redis server.
    
    Parameters:
    ----------
        host (str): redis host name, if using docker container, the container name
        port (int): redis port
        data (dict): data to add to the redis server
    
    Returns
    -------
        Nothing
    """
    redis_connection = redis.Redis(host=host,
                                   port=port)
    try:
        redis_connection.mset(data)
    except Exception as e:
        print(f"Error {e} when commiting to redis db.")


def redis_get(*,
              host='redis',
              port=6379,
              key: str = None):
    """Get a value from redis server.
    
    Parameters:
    ----------
        host (str): redis host name, if using docker container, the container name
        port (str): redis port
        key (str): key to fetch

    Returns:
    -------
        Value found for key (str)
    
    """
    redis_connection = redis.Redis(host=host,
                                   port=port)
    return redis_connection.get(key)


if __name__ == "__main__":
    _redis_hello()