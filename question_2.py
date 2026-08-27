from pydantic import BaseModel

class TaskIn(BaseModel):
    title: str
    completed: bool = False

@app.post("/tasks/")
def create_task(task: TaskIn):
    return {
        "success": True,
        "data": task
    }