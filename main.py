#portfolio
#handle: _MUMINUL__ISLAM___

#author: MUMINUL ISLAM

#License: proprietary

#CODE
from database import get_db
from model import Product_Model
from schema import Product_Schema
from cache import search_data,rate_limit,read_cache
from worker import run_bg_task

from typing import List
from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import json

app=FastAPI()

#


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",response_model=List[Product_Schema] )
def read_database(db: Session=Depends(get_db)):
    result=db.query(Product_Model).all()
    return result


@app.get("/search/{input_product_model}",response_model=Product_Schema)
def search_database(input_product_model,db: Session=Depends(get_db)):
    if rate_limit():
        result=search_data(product_model_term=input_product_model, database=db)
        return result
    else:
        raise HTTPException(status_code=503)
    
@app.get("/background")
def background_job_run():
    result=run_bg_task()
    print(result)
    return json.loads(result)

@app.get("/cache")
def list_cache():
    cache_content=read_cache()
    if cache_content:
        return json.loads(cache_content) # type: ignore
    else:
        raise HTTPException(status_code=404)