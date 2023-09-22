from fastapi import FastAPI
import aioredis

app = FastAPI()
redis = aioredis.from_url("redis://redis:6379")


@app.get("/")
async def root():
    return {"hello": "world"}
