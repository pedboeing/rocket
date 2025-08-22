from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

# CREATE
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control ,title=data.get('title'), description=data.get('description', ''))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

# READ
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())

    output = {
        "message":task_list,
        "total_tasks":len(task_list)
    }
    
    if len(task_list) > 0:
        return jsonify(output)
    else:
        return jsonify({"message":"Nenhuma tarefa encontrada"})
    
# READ BY ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify({'message':task.to_dict()})

    return jsonify({'message':'Tarefa não encontrada'}), 404

# UPDATE
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None:
        return jsonify({'message':'Nenhuma tarefa encontrada'}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({'message':'Tarefa atualizada com sucesso'})

# DELETE
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({'message':'Nenhuma tarefa encontrada'}), 404
    
    tasks.remove(task)

    return jsonify({'message':'Tarefa deletada com sucesso'})



if __name__ == "__main__":
    app.run(debug=True)