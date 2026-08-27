from fastapi import FastAPI

app = FastAPI(title="Task Management API")

@app.get("/")
def home():
    return {"message": "FastAPI server is running"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}