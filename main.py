# GLOBAL IMPORTS
import uvicorn, logging
from typing import Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

# LOCAL IMPORTS
from modules import config as cfg

# LOGGING FORMATTER
# logging.basicConfig(format=f'%(asctime)s | %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO, filename='./logs/server.log', force=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    logging.info('Server startup...')
    
    yield
    
    #SHUTDOWN
    logging.info('Server shutdown...')
    
app: FastAPI = FastAPI( 
    lifespan=lifespan,
    docs_url=None if not cfg.DEBUGGING else "/docs",
    redoc_url=None if not cfg.DEBUGGING else "/redoc"
)

if __name__ == "__main__": 
    if cfg.DEBUGGING:
        uvicorn.run(app='main:app', host=cfg.DEBUGGING_SOCKET, port=cfg.DEBUGGING_PORT, reload=True) # HTTP -> 80, HTTPS -> 443
    else: # PROD MODE  
        uvicorn.run(app='main:app', host='0.0.0.0', port=80, reload=True) # HTTP -> 80, HTTPS -> 443