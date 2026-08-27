@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}