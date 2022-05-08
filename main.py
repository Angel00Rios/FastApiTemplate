from fastapi import FastAPI
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health", tags=["healthcheck"])
async def healthcheck():
    """Standard route for health check used to monitor service."""
    return JSONResponse(status_code=status.HTTP_200_OK, content={'status': 'alive'})

@app.post("/post", tags=["post"])
async def healthcheck(_input:str):
    """Standard route for health check used to monitor service."""
    print(_input)
    return JSONResponse(status_code=status.HTTP_200_OK, content={'status': 'alive'})