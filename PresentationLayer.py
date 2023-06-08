from flask import Flask, request

from BusinessLayer import *
from errors.api_errors import CustomError

app = Flask('Web Application')


@app.route('/api/task/<int:ident>/', methods=['GET'])
def get_task(ident):
    try:
        result = get_one_instance(ident)
    except CustomError as e:
        return e.message, e.status_code
    return result, 200


@app.route('/api/task/', methods=['GET'])
def get_all_tasks():
    data = get_all()
    return {'tasks': data}, 200


@app.route('/api/task/', methods=['POST'])
def create_task():
    data = request.json
    try:
        task = create_instance(data)
        return task, 200
    except CustomError as e:
        return e.message, e.status_code


@app.route('/api/task/<int:ident>', methods=['PUT'])
def update_task(ident):
    data = request.json
    try:
        updated_task = update_instance(ident, data)
    except CustomError as e:
        return e.message, e.status_code
    return updated_task, 200


@app.route('/api/task/<int:ident>', methods=['DELETE'])
def delete_task(ident):
    try:
        result = delete_single_instance(ident)
    except CustomError as e:
        return e.message, e.status_code
    return result, 204
