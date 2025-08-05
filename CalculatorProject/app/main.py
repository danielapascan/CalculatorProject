from app.log_config import setup_logging
setup_logging()

from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
from app.db import init_db
from app.routes import pow, fibonacci, factorial, admin
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="MathOps Service", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(pow.router)
app.include_router(fibonacci.router)
app.include_router(factorial.router)
app.include_router(admin.router)

Instrumentator().instrument(app).expose(app)