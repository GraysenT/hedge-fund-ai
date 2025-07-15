def start_api():
    import uvicorn
    print("🚀 Starting FastAPI orchestrator on port 8000")
    uvicorn.run("orchestrator.api_app:app", host="0.0.0.0", port=8000, reload=False)