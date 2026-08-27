@app.get("/tasks/")
def list_tasks(completed: bool = False):
    return {
        "completed": completed
    }