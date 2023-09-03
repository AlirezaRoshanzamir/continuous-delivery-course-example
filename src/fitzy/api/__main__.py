import uvicorn

if __name__ == "__main__":
    uvicorn.run("fitzy.api.app:app", port=8000, log_level="info")
