from singletask_backend.api.app import app


@app.route('/tasks', methods=['POST'])
def task_create():
    pass
