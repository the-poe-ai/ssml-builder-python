from fastapi import FastAPI
from .routes import router

app = FastAPI(title="SSML Generator", description="SSML Generator API", version="0.1.0", contact={"name": "Poe.AI", "email": "cto@poeai.app"}, license_info={"name": "MIT License"})
app.include_router(router, prefix="/api", tags=["ssml"])