import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import report_router


app = FastAPI()

origins = [
    "localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=report_router,
    prefix="/api",
    tags=["Report"]
)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
    )
