from fastapi import FastAPI
import alerts

app = FastAPI()
app.include_router(alerts.router)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)