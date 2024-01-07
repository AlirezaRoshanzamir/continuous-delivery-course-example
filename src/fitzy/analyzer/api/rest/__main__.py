import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "fitzy.analyzer.api.rest.app:app", host="0.0.0.0", port=6791, log_level="info"
    )
