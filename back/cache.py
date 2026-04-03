#portfolio
#handle: _MUMINUL__ISLAM___

#code
from model import Product_Model
import os
import redis
import json

REDIS_CACHE_URL=os.getenv("REDIS_CACHE_URL", "redis://redis:6379/0")
REDIS_RATE_URL=os.getenv("REDIS_RATE_URL", "redis://redis:6379/1")

redis_connection=redis.Redis.from_url(REDIS_CACHE_URL, decode_responses=True)
redis_rate_limit_connection=redis.Redis.from_url(REDIS_RATE_URL,decode_responses=True)

def search_data(product_model_term,database):
    print(REDIS_CACHE_URL, REDIS_RATE_URL)
    cached=redis_connection.get(product_model_term.lower())
    if cached:
        print("Cache Hit")
        return json.loads(cached) # pyright: ignore[reportArgumentType]
    else:
        print("Cache Miss")
        product=database.query(Product_Model).filter(Product_Model.product_model==product_model_term).first()
        if product:
            product_dict={
                "product_id":product.product_id,
                "product_name":product.product_name,
                "product_model":product.product_model,
                "product_core":product.product_core
            }
            redis_connection.setex(product_model_term.lower(),30,json.dumps(product_dict))
            
    return product

def rate_limit():
    KEY="global_rate_limit"
    LIMIT=2
    WINDOW=15

    current=redis_rate_limit_connection.incr(KEY)
    if int(current)==1: # type: ignore
        redis_rate_limit_connection.expire(KEY,WINDOW)

    if int(current)>LIMIT: # type: ignore
        return False
    return True

def read_cache():
    for key in redis_connection.scan_iter('*'):
        value=redis_connection.get(key)
        print("Redis Cache: ",value)
        return value