from fastapi import FastAPI
from .routes import router
from scalar_fastapi import get_scalar_api_reference


app = FastAPI(
    title="SSML Generator",
    description="SSML Generator API",
    version="0.1.0",
    contact={"name": "Poe.AI", "email": "cto@poeai.app"},
    license_info={"name": "MIT License"},
)
app.include_router(router, prefix="/api", tags=["ssml"])


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)
