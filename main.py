from fastapi import FastAPI
from api.routes.routes import router
import uvicorn


app = FastAPI(
    title="Techcombank_buddy",
    description="Hello! This is Techcombank Buddy!!!"
)

# Include tất cả các endpoint từ router
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)