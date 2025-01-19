import uvicorn
from fastapi import FastAPI
from gabolls.api.fast import app as fast_app
from gabolls.api.round import router as round_router

app = FastAPI()

# Include the routers from the different modules
app.include_router(fast_app.router, prefix="/api")
app.include_router(round_router, prefix="/api/round")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
