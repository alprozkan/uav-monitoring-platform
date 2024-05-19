from flask import Blueprint, request, jsonify
from app import db
from models import Drone, Task, Image
import random
import string
import os

api_bp = Blueprint('api', __name__)

@api_bp.route('/drones', methods=['GET'])
def get_drones():
    drones = Drone.query.all()
    return jsonify([{'id': drone.id, 'name': drone.name, 'model': drone.model} for drone in drones])

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(name=data['name'], description=data.get('description'), drone_id=data['drone_id'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id, 'name': task.name, 'description': task.description}), 201

@api_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({'id': task.id, 'name': task.name, 'description': task.description, 'drone_id': task.drone_id})

@api_bp.route('/tasks/<int:id>/execute', methods=['POST'])
def execute_task(id):
    task = Task.query.get_or_404(id)
    images = []
    for _ in range(5):
        img_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + '.jpg'
        img_path = os.path.join('images', img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(os.urandom(1024))  # Dummy noisy image
        image = Image(path=img_path, task_id=task.id)
        db.session.add(image)
        images.append(img_path)
    db.session.commit()
    return jsonify({'images': images})

@api_bp.route('/tasks/<int:id>/images', methods=['GET'])
def get_task_images(id):
    images = Image.query.filter_by(task_id=id).all()
    return jsonify([{'id': img.id, 'path': img.path} for img in images])
