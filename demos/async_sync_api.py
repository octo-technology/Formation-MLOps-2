import asyncio
import time
from contextlib import asynccontextmanager

import anyio
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    anyio.to_thread.current_default_thread_limiter().total_tokens = 1
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/blocking/{n}")
async def blocking(n: int):
    # async def + appel bloquant (time.sleep) -> bloque TOUTE la boucle
    # asyncio, qui est unique et partagée par toutes les requêtes.
    # 2 requêtes concurrentes (n=10 puis n=1) => la 2e attend ~11s.
    time.sleep(n)
    return {"message": "blocking async"}


@app.get("/nonblocking/{n}")
async def nonblocking(n: int):
    # async def + await asyncio.sleep -> ne bloque pas la boucle,
    # elle peut traiter d'autres requêtes pendant l'attente.
    # 2 requêtes concurrentes (n=10 puis n=1) => la 2e répond en ~1s.
    await asyncio.sleep(n)
    return {"message": "non-blocking async"}


@app.get("/sync/{n}")
def sync_threadpool(n: int):
    # def classique -> FastAPI l'exécute dans un threadpool, pas sur la
    # boucle asyncio. Concurrent aussi, mais via des threads OS
    # (jusqu'à la limite du threadpool), pas via des coroutines.
    time.sleep(n)
    return {"message": "sync in threadpool"}
